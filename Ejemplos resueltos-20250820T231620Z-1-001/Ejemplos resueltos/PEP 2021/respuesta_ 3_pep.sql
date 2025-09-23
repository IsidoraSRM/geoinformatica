-- 1) Calculo de amenaza
-- amenaza = poblacion * nivel
-- 1.1) Unir tabla comuna con comuna_area
create table shp_comuna as
select *
from comuna as A
join  comuna_area as B
on A.codigo = B.codigo;

-- 1.2) Codificar nivel de amenaza asumiendo que viene como información discreta
create table area_cod as
select
case
	when (nivel = 'bajo') then 0
	when (nivel = 'medio') then 1
	when (nivel = 'alto') then 2
end as nivel, geom
from area_afectacion;

-- 1.2) Intersectar shp_comuna con area_afectacion
-- Nota: se debe utilizar mismo SRC y transformar a polígono
create table amenaza as
select cast(A.poblacion * B.nivel as real) as amenaza, st_intersection(ST_MakeValid(ST_BuildArea(A.geom)),ST_TRANSFORM(B.geom,32719)) as geom
from shp_comuna as A
join area_cod as B
on st_intersects(ST_MakeValid(ST_BuildArea(A.geom)),ST_TRANSFORM(B.geom,32719));

-- 1.3) crear indice espacial
SELECT AddGeometryColumn('amenaza', 'geom',32719, 'POLYGON', 'XY');
SELECT CreateSpatialIndex('amenaza', 'geom');

-- 2) Calculo de vulnerabilidad
-- vulnerabilidad = factor *(pobreza_multi + agua_potable + construccion)
-- 2.1) Unir tabla vivienda, hogar y abastecimiento a tabla zona
-- nota: se asume por el diagrama que la tabla vivienda ya 
-- se encuentra subdividida según la cantidad de hogares
-- (En caso de no ser así, pordefecto se extiende la cantidad de registros donde sea necesario)
-- Lo mismo ocurre con abastecimeinto, esta se encuentra a nivel de hogar
-- Por lo tanto, lo mismo ocurre con zona

-- Al unir las tablas debe quedar algo como
-- nota: el codigo censal se ejemplifica como str sólo para facilitar lectura
---------------------------------------------------------------------------------------------------------
-- TABLA ZONA consolidada
---------------------------------------------------------------------------------------------------------
-- id | factor | cod_zona | vivienda_id | hogar_id | agua_potable | pobreza_multi | construccion | geom
-- 1  | 23	   | A        | A			| A        |  0			  |  0 			  | 0			 |polygon
-- 2  | 12	   | A        | A			| B        |  0			  |  1 			  | 1			 |polygon
-- 3  | 13	   | A        | B			| A        |  0			  |  0 			  | 1			 |polygon
-- 4  | 15	   | B        | A			| A        |  1			  |  1 			  | 1			 |polygon
-- 5  | 5	   | B        | B			| A        |  1			  |  1 			  | 1			 |polygon
-- 6  | 12	   | C        | A			| A        |  1			  |  0 			  | 1			 |polygon
---------------------------------------------------------------------------------------------------------

-- Primero se debe transformar el codigo de zona (
-- sqlite no permite modificar tipo por lo que se debe crear denuevo)
create table zona_aux as
select id, factor, cast(cod_zona as int) as cod_zona, geom
from zona

-- aplicar join
create table zona_censal as
select zn.id, zn.factor, zn.cod_zona, viv.cod_vivienda, hog.cod_hogar, 
		abst.agua_potable, hog.pobreza_multi, viv.construccion, zn.geom
from zona_aux as zn
join abastecimiento as abst on zn.cod_zona = abst.cod_zona
join vivienda as viv on abst.vivienda_id = viv.cod_vivienda
join hogar as hog on viv.hogar_id = hog.cod_hogar;

-- 2.2) Disolver y agrupar a nivel de zona
-- Notar que al hacer la suma de agua_potable, pobreza_multi y construccion
-- obtenemos la cantidad de hogares que cumplen la condicion de vulnerabilidad
-- Sumar el factor de expansion, implica la misma logica


create table zona_agrupada as
Select zn.cod_zona as cod_zona, sum(zn.factor) as factor
		sum(zn.agua_potable) as tot_ap, sum(zn.pobreza_multi) as tot_pm, sum(zn.construccion) as tot_const, 
		st_unaryunion(st_collect(zn.geom)) as geom
From (SELECT aux.cod_zona as cod_zona, 
	aux.factor as factor, 
	aux.agua_potable as agua_potable, 
	aux.pobreza_multi as pobreza_multi, 
	case
		when (aux.construccion = 'No') then 0
		when (aux.construccion = 'Si') then 1
	end construccion
	From zona_censal as aux) as zn
Group by zn.cod_zona;

-- 2.3) crear indice espacial
SELECT AddGeometryColumn('zona_agrupada', 'geom',32719, 'POLYGON', 'XY');
SELECT CreateSpatialIndex('zona_agrupada', 'geom');

-- 2.3) calcular vulnerabilidad
create table vulnerabilidad as
select zn.cod_zona, 
	cast((zn.factor * (zn.tot_ap + zn.tot_pm + tot_const)) as real) as vulnerabilidad, 
	geom
from zona_agrupada as zn;

-- 3) calcular riesgo
-- riesgo = amenaza * vulnerabilidad
create table riesgo as
select vuln.cod_zona, 
	cast(amen.amenaza * vuln.vulnerabilidad as real) as riesgo, 
	st_intersection(amen.geom, vuln.geom) as geom
from amenaza as amen
join vulnerabilidad as vuln
on st_intersects(amen.geom, vuln.geom);

-- 3.1) crear indice espacial
SELECT AddGeometryColumn('riesgo', 'geom',32719, 'POLYGON', 'XY');
SELECT CreateSpatialIndex('riesgo', 'geom');

-- 3.2) mostrar resultado
select rsg.cod_zona as Zonaloc, rsg.riesgo as NvRiesgo, geom
from riesgo as rsg
order by NvRiesgo desc
limit 10;

-- 4) Limpiar resultados intrmedios
DROP TABLE IF EXISTS shp_comuna;
DROP TABLE IF EXISTS amenaza;
DROP TABLE IF EXISTS zona_aux;
DROP TABLE IF EXISTS zona_censal;
DROP TABLE IF EXISTS zona_agrupada;
DROP TABLE IF EXISTS vulnerabilidad;
---
title: Filtro dinámico
type: docs
weight: 130
url: /es/java/add-or-clear-pivot-filter/
description: Aprenda cómo agregar un filtro en la tabla dinámica con la biblioteca Aspose.Cells Java.
keywords: Agregar un filtro en la tabla dinámica sin office 2013, office 2016, office 2019 y office 365.
---

## **Escenarios de uso posibles**
Cuando creas una tabla dinámica con datos conocidos y deseas filtrar la tabla dinámica, necesitas aprender y usar el filtro. Puede ayudarte a filtrar eficazmente los datos que deseas. Usando la API de Aspose.Cells Java, puedes agregar un filtro en los valores de campo en Tablas Dinámicas. 

## **Agregar filtro en tabla dinámica en Excel**
Agregar filtro en tabla dinámica en Excel, sigue estos pasos:

1. Selecciona la Tabla Dinámica de la que deseas eliminar el filtro. 
2. Haz clic en la flecha desplegable del filtro que deseas agregar en la tabla dinámica.
3. Selecciona "Los 10 principales" en el menú desplegable.
<br>
<img src="3.png" width=80% />
4. Establece el modo de exhibición y el número de filtros.
<br>
<img src="4.png" width=80% />

## **Agregar filtro en tabla dinámica**
Por favor, vea el siguiente código de muestra. Establece los datos y crea una Tabla Dinámica basada en ellos. Luego añade un filtro en el campo de fila de la tabla dinámica. Finalmente, guarda el libro de trabajo en formato [XLSX de salida](out.xlsx). Después de ejecutar el código de ejemplo, se agrega una tabla dinámica con filtro top10 a la hoja de cálculo.

### **Código de muestra**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-Add-filter-in-PivotTable.java" >}}


## **Borrar filtro en tabla dinámica en Excel**
Limpiar filtro en Tabla Dinámica en Excel, sigue estos pasos:

1. Selecciona la Tabla Dinámica de la que deseas eliminar el filtro. 
2. Haz clic en la flecha desplegable para el filtro que deseas borrar en la tabla dinámica.
3. Selecciona "Limpiar filtro" en el menú desplegable.
<br>
<img src="1.png" width=80% />
4. Si deseas borrar todos los filtros de la tabla dinámica, también puedes hacer clic en el botón "Limpiar filtros" en la pestaña Analizar tabla dinámica en la cinta de Excel.
<br>
<img src="2.png" width=80% />

## **Borrar filtro en tabla dinámica**
Consulta el siguiente código de ejemplo. Establece los datos y crea una Tabla Dinámica basada en ello. Luego agrega un filtro en el campo de fila de la tabla dinámica. Finalmente, guarda el libro en formato [XLSX de salida](out_add.xlsx). Después de ejecutar el código de ejemplo, se añade un filtro top10 a la hoja de cálculo. Después de agregar un filtro, cuando necesitamos datos sin filtrar, podemos borrar el filtro en un campo de tabla dinámica específico. Después de ejecutar el código para borrar el filtro, este se eliminará en el campo de tabla dinámica específico. Consulta el [XLSX de salida](out_delete.xlsx).

### **Código de muestra**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-Clear-filter-in-PivotTable.java" >}}
{{< app/cells/assistant language="java" >}}

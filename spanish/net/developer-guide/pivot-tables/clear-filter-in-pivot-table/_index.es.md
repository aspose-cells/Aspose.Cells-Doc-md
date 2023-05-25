---
title: Borrar filtro en tabla dinámica
type: docs
weight: 130
url: /es/net/clear-filter-in-pivot-table/
description: Cómo borrar PivotFilter del PivotField específico en la tabla dinámica con Aspose.Cells.
keywords: Clear PivotFilter in pivot table.
---
##  **Posibles escenarios de uso**
 Cuando crea una tabla dinámica con datos conocidos y desea filtrar la tabla dinámica, debe aprender y usar el filtro. Puede ayudarlo a filtrar los datos que desea de manera efectiva. Al usar el Aspose.Cells API, puede operar el filtro en los valores de campo en las tablas dinámicas.

##  **Borrar filtro en tabla dinámica en Excel**
Borre el filtro en la tabla dinámica en Excel, siga estos pasos:

1.  Seleccione la tabla dinámica en la que desea borrar el filtro.
2. Haga clic en la flecha desplegable del filtro que desea borrar en la tabla dinámica.
3. Seleccione "Borrar filtro" en el menú desplegable.
<img src="1.png" width=80% />
4. Si desea borrar todos los filtros de la tabla dinámica, también puede hacer clic en el botón "Borrar filtros" en la pestaña Analizar tabla dinámica en la cinta de Excel.
<img src="2.png" width=80% />

##  **Borrar filtro en tabla dinámica usando C#**
 Borre el filtro en la tabla dinámica usando Aspose.Cells. Consulte el siguiente código de ejemplo.
1.  Establezca los datos y cree una tabla dinámica basada en ellos.
2. Agregue un filtro en el campo de fila de la tabla dinámica.
 3. Guarde el libro de trabajo en[salida XLSX](out_add.xlsx) formato. Después de ejecutar el código de ejemplo, se agrega una tabla dinámica con el filtro top10 a la hoja de trabajo.
 4. Borre el filtro en un campo pivote específico. Después de ejecutar el código para borrar el filtro, se borrará el filtro en el campo dinámico específico. Por favor, checa el[salida XLSX](out_delete.xlsx).

##  **Código de muestra**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-Clear-filter-in-PivotTable.cs" >}}
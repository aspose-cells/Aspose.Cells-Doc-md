---
title: Borrar filtro en tabla dinámica
type: docs
weight: 130
url: /es/python-net/clear-filter-in-pivot-table/
description: Cómo borrar PivotFilter del PivotField específico en la tabla dinámica con Aspose.Cells for Python via .NET.
keywords: Clear PivotFilter in pivot table.
---
##  **Posibles escenarios de uso**
 Cuando crea una tabla dinámica con datos conocidos y desea filtrar la tabla dinámica, necesita aprender y usar el filtro. Puede ayudarle a filtrar los datos que desea de forma eficaz. Al utilizar Aspose.Cells for Python via .NET API, puede operar el filtro en valores de campo en tablas dinámicas.

##  **Borrar filtro en tabla dinámica en Excel**
Borrar filtro en tabla dinámica en Excel, sigue estos pasos:

1. Seleccione la tabla dinámica en la que desea borrar el filtro.
2. Haga clic en la flecha desplegable del filtro que desea borrar en la tabla dinámica.
3. Seleccione "Borrar filtro" en el menú desplegable.
<img src="1.png" width=80% />
4. Si desea borrar todos los filtros de la tabla dinámica, también puede hacer clic en el botón "Borrar filtros" en la pestaña Analizar de tabla dinámica en la cinta de Excel.
<img src="2.png" width=80% />

##  **Borrar filtro en tabla dinámica usando C#**
 Borre el filtro en la tabla dinámica usando Aspose.Cells for Python via .NET. Consulte el siguiente código de muestra.
1.  Configure los datos y cree una tabla dinámica basada en ellos.
 2. Agregue un filtro en el campo de fila de la tabla dinámica.
 3. Guarde el libro de trabajo en[salida XLSX](out_add.xlsx) formato. Después de ejecutar el código de ejemplo, se agrega a la hoja de trabajo una tabla dinámica con el filtro top10.
 4. Borre el filtro en un campo dinámico específico. Después de ejecutar el código para borrar el filtro, se borrará el filtro en el campo dinámico específico. Por favor, checa el[salida XLSX](out_delete.xlsx).

##  **Código de muestra**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-Clear-filter-in-PivotTable.py" >}}
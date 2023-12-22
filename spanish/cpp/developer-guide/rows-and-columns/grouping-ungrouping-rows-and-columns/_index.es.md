---
title: Agrupar, desagrupar filas y columnas
type: docs
weight: 30
url: /es/cpp/grouping-ungrouping-rows-and-columns/
---
##  **Introducción**
En un archivo Excel Microsoft, puede crear un esquema para los datos que le permita mostrar y ocultar niveles de detalle con un solo clic del mouse.

Haga clic en *Símbolos de esquema**, 1,2,3, + y - para mostrar rápidamente solo las filas o columnas que proporcionan resúmenes o encabezados para las secciones de una hoja de trabajo, o puede usar los símbolos para ver detalles en un resumen individual o título.
##  **Gestión grupal de filas y columnas**
 Aspose.Cells proporciona una clase,[Libro de trabajo](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) que representa un archivo Excel Microsoft. El[Libro de trabajo](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) la clase contiene un[Hojas de trabajo](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) colección que permite el acceso a cada hoja de cálculo del archivo Excel. Una hoja de trabajo está representada por el[Hoja de cálculo](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) clase. El[Hoja de cálculo](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) clase proporciona una[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)colección que representa todas las celdas de la hoja de trabajo.

 El[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)La colección proporciona varios métodos para administrar filas o columnas en una hoja de trabajo; algunos de ellos se analizan a continuación con más detalle.
###  **Agrupación de filas y columnas**
 Es posible agrupar filas o columnas llamando al[Filas de grupo](https://reference.aspose.com/cells/cpp/aspose.cells/cells/grouprows/) y[Columnas de grupo](https://reference.aspose.com/cells/cpp/aspose.cells/cells/groupcolumns/) métodos de la[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)recopilación. Ambos métodos toman los siguientes parámetros:

- El índice de la primera fila/columna, la primera fila o columna del grupo.
- El último índice de fila/columna, la última fila o columna del grupo.
- Está oculto, un parámetro booleano que especifica si se deben ocultar filas/columnas después de agrupar o no.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-GroupingRowsColumns-new.cpp" >}}
####  **Configuración de grupo**
Microsoft Excel le permite configurar ajustes de grupo para mostrar:

- Filas de resumen debajo de los detalles.
- Columnas de resumen a la derecha del detalle.
##  **Desagrupar filas y columnas**
 Para desagrupar cualquier fila o columna agrupada, llame al[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) colección[Desagrupar filas](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungrouprows/) y[DesagruparColumnas](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungroupcolumns/)métodos. Ambos métodos toman dos parámetros:

- El índice de la primera fila o columna, la primera fila/columna que se desagrupará.
- El índice de la última fila o columna, la última fila/columna que se desagrupará.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-UnGroupingRowsColumns-new.cpp" >}}

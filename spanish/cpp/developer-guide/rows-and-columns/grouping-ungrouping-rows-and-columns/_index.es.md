---
title: Agrupación, Desagrupación de Filas y Columnas
type: docs
weight: 30
url: /es/cpp/grouping-ungrouping-rows-and-columns/
---
## **Introducción**
En un archivo de Excel Microsoft, puede crear un esquema para los datos que le permita mostrar y ocultar niveles de detalle con un solo clic del mouse.

 Haga clic en el**Símbolos de esquema**, 1, 2, 3, + y - para mostrar rápidamente solo las filas o columnas que proporcionan resúmenes o encabezados para las secciones de una hoja de trabajo, o puede usar los símbolos para ver detalles bajo un resumen o encabezado individual.
## **Gestión de grupos de filas y columnas**
 Aspose.Cells proporciona una clase,[ILibro de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) que representa un archivo de Excel Microsoft. los[ILibro de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) la clase contiene un[IHojas de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection) colección que permite el acceso a cada hoja de trabajo en el archivo de Excel. Una hoja de trabajo está representada por el[IHoja de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) clase. los[IHoja de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) la clase proporciona un[ICélulas](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)colección que representa todas las celdas de la hoja de cálculo.

 los[ICélulas](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)collection proporciona varios métodos para administrar filas o columnas en una hoja de trabajo, algunos de estos se analizan a continuación con más detalle.
### **Agrupación de filas y columnas**
 Es posible agrupar filas o columnas llamando al[Filas de grupo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a88e0180ed1a4a423e0bd3ac599ef9332) y[GrupoColumnas](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#aaa14179e2a84ba5c2857f8434570d3d8) métodos de la[ICélulas](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)recopilación. Ambos métodos toman los siguientes parámetros:

- El índice de la primera fila/columna, la primera fila o columna del grupo.
- El último índice de fila/columna, la última fila o columna del grupo.
- Está oculto, un parámetro booleano que especifica si ocultar filas/columnas después de la agrupación o no.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-GroupingRowsColumns.cpp" >}}
#### **Configuración de grupo**
Microsoft Excel le permite configurar ajustes de grupo para mostrar:

- Filas de resumen debajo del detalle.
- Columnas de resumen a la derecha del detalle.
## **Desagrupar filas y columnas**
 Para desagrupar filas o columnas agrupadas, llame al[ICélulas](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) colección[Desagrupar filas](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#adc1f6418506854ab41707bfef453ddb1) y[DesagruparColumnas](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#aa3bf9a9510d4e85f68db9ebdcadc8406)métodos. Ambos métodos toman dos parámetros:

- El índice de la primera fila o columna, la primera fila/columna a desagrupar.
- El índice de la última fila o columna, la última fila/columna que se desagrupará.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-UnGroupingRowsColumns.cpp" >}}

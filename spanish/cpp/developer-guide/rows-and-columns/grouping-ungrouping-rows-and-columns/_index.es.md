---
title: Agrupar, desagrupar filas y columnas
type: docs
weight: 30
url: /es/cpp/grouping-ungrouping-rows-and-columns/
---

## **Introducción**
En un archivo de Microsoft Excel, puedes crear un esquema para los datos que te permita mostrar y ocultar niveles de detalle con un solo clic de ratón.

Haz clic en los **Símbolos de resumen**, 1,2,3, + y - para mostrar rápidamente solo las filas o columnas que proporcionan resúmenes o encabezados de secciones en una hoja de cálculo, o puedes usar los símbolos para ver detalles bajo un resumen o encabezado individual.
## **Gestión de Agrupación de Filas y Columnas**
Aspose.Cells proporciona una clase, [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) que representa un archivo de Microsoft Excel. La clase [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contiene una colección [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) que permite el acceso a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La clase [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) proporciona una colección [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) que representa todas las celdas en la hoja de cálculo.

La colección [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) proporciona varios métodos para gestionar filas o columnas en una hoja de cálculo, algunos de estos se discuten a continuación con más detalle.
### **Agrupación de Filas y Columnas**
Es posible agrupar filas o columnas llamando a los métodos [GroupRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/grouprows/) y [GroupColumns](https://reference.aspose.com/cells/cpp/aspose.cells/cells/groupcolumns/) de la colección [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Ambos métodos toman los siguientes parámetros:

- El índice de la primera fila/columna, la primera fila o columna en el grupo.
- El índice de la última fila/columna, la última fila o columna en el grupo.
- Está oculto, un parámetro booleano que especifica si ocultar o no filas/columnas después de agrupar.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-GroupingRowsColumns-new.cpp" >}}
#### **Configuración de Grupo**
Microsoft Excel te permite configurar la configuración de grupo para mostrar:

- Filas resumen debajo del detalle.
- Columnas de resumen a la derecha del detalle.
## **Desagrupar Filas y Columnas**
Para desagrupar filas o columnas agrupadas, llame a los métodos [UngroupRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungrouprows/) y [UngroupColumns](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungroupcolumns/) de la colección [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Ambos métodos toman dos parámetros:

- El índice de la primera fila o columna que se desagrupará.
- El índice de la última fila o columna que se desagrupará.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-UnGroupingRowsColumns-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}

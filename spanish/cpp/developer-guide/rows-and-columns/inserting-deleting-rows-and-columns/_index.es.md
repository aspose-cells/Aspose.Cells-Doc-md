---
title: Insertar, eliminar filas y columnas
type: docs
weight: 40
url: /es/cpp/inserting-deleting-rows-and-columns/
---

## **Introducción**
Ya sea creando una nueva hoja de cálculo desde cero o trabajando en una hoja de cálculo existente, es posible que necesitemos agregar filas o columnas adicionales para acomodar más datos. Inversamente, es posible que también necesitemos eliminar filas o columnas de posiciones específicas en la hoja de cálculo. Para cumplir con estos requisitos, Aspose.Cells proporciona un conjunto muy simple de clases y métodos, que se discuten a continuación.
### **Gestión de filas y columnas**
Aspose.Cells proporciona una clase, [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), que representa un archivo de Microsoft Excel. La clase [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contiene una colección [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) que permite acceder a cada hoja de cálculo en un archivo de Excel. Una hoja de cálculo está representada por la clase [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La clase [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) proporciona una colección [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) que representa todas las celdas en la hoja de cálculo.

La colección [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) proporciona varios métodos para gestionar filas y columnas en una hoja de cálculo. Algunos de estos se discuten a continuación.

{{% alert color="primary" %}} 

Cuando se agregan filas o columnas, el contenido en la hoja de cálculo se desplaza hacia abajo o hacia la derecha, y si se eliminan filas o columnas, el contenido se desplaza hacia arriba o hacia la izquierda.

{{% /alert %}} 
#### **Insertar una fila**
Inserte una fila en la hoja de cálculo en cualquier ubicación llamando al método [InsertRow](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/) de la colección [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). El método [InsertRow](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/) toma el índice de la fila donde se insertará la nueva fila.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertRow-new.cpp" >}}


#### **Insertar Múltiples Filas**
Para insertar varias filas en una hoja de cálculo, llame al método [InsertRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) de la colección [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). El método [InsertRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) toma dos parámetros:

- Índice de la fila, el índice de la fila desde donde se insertarán las nuevas filas.
- Número de filas, el número total de filas que se deben insertar.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertingMultipleRows-new.cpp" >}}


#### **Eliminar Múltiples Filas**
Para eliminar varias filas de una hoja de cálculo, llame al método [DeleteRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/) de la colección [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). El método [DeleteRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/) toma dos parámetros:

- Índice de fila, el índice de la fila desde donde se eliminarán las filas.
- Número de filas, el número total de filas que deben ser eliminadas.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeletingMultipleRows-new.cpp" >}}


#### **Insertar una columna**
Los desarrolladores también pueden insertar una columna en la hoja de cálculo en cualquier ubicación llamando al método [InsertColumn](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/) de la colección [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). El método [InsertColumn](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/) toma el índice de la columna donde se insertará la nueva columna.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertColumn-new.cpp" >}}


#### **Eliminar una columna**
Para eliminar una columna de la hoja de cálculo en cualquier ubicación, llame al método [DeleteColumn](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/) de la colección [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). El método [DeleteColumn](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/) toma el índice de la columna a eliminar.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeleteColumn-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}

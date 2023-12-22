---
title: Insertar, eliminar filas y columnas
type: docs
weight: 40
url: /es/cpp/inserting-deleting-rows-and-columns/
---
##  **Introducción**
Ya sea que creemos una nueva hoja de trabajo desde cero o trabajemos en una hoja de trabajo existente, es posible que necesitemos agregar filas o columnas adicionales para acomodar más datos. A la inversa, es posible que también necesitemos eliminar filas o columnas de posiciones específicas en la hoja de trabajo. Para cumplir con estos requisitos, Aspose.Cells proporciona un conjunto de clases y métodos muy simple, que se analiza a continuación.
###  **Administrar filas y columnas**
 Aspose.Cells proporciona una clase,[Libro de trabajo](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) , que representa un archivo Excel Microsoft. El[Libro de trabajo](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) la clase contiene un[Hojas de trabajo](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)colección que permite el acceso a cada hoja de cálculo en un archivo Excel. Una hoja de trabajo está representada por el[Hoja de cálculo](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) clase. El[Hoja de cálculo](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) clase proporciona una[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)colección que representa todas las celdas de la hoja de trabajo.

 El[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)La colección proporciona varios métodos para administrar filas y columnas en una hoja de trabajo. Algunos de éstos se discuten a continuación.

{{% alert color="primary" %}} 

Cuando se agregan filas o columnas, el contenido de la hoja de cálculo se desplaza hacia abajo o hacia la derecha, y si se eliminan filas o columnas, el contenido se desplaza hacia arriba o hacia la izquierda.

{{% /alert %}} 
####  **Insertar una fila**
 Inserte una fila en la hoja de trabajo en cualquier ubicación llamando al[Insertar fila](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/) método de la[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) recopilación. El[Insertar fila](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/)El método toma el índice de la fila donde se insertará la nueva fila.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertRow-new.cpp" >}}


####  **Insertar varias filas**
 Para insertar varias filas en una hoja de trabajo, llame al[Insertar filas](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) método de la[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) recopilación. El[Insertar filas](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/)El método toma dos parámetros:

- Índice de fila, el índice de la fila desde donde se insertarán las nuevas filas.
- Número de filas, el número total de filas que deben insertarse.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertingMultipleRows-new.cpp" >}}


####  **Eliminar varias filas**
 Para eliminar varias filas de una hoja de cálculo, llame al[Eliminar filas](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/) método de la[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) recopilación. El[Eliminar filas](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/)El método toma dos parámetros:

- Índice de fila, el índice de la fila desde donde se eliminarán las filas.
- Número de filas, el número total de filas que deben eliminarse.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeletingMultipleRows-new.cpp" >}}


####  **Insertar una columna**
 Los desarrolladores también pueden insertar una columna en la hoja de trabajo en cualquier ubicación llamando al[Insertar columna](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/) método de la[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) recopilación.[Insertar columna](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/)El método toma el índice de la columna donde se insertará la nueva columna.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertColumn-new.cpp" >}}


####  **Eliminar una columna**
 Para eliminar una columna de la hoja de cálculo en cualquier ubicación, llame al[Eliminar columna](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/) método de la[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) recopilación. El[Eliminar columna](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/)El método toma el índice de la columna a eliminar.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeleteColumn-new.cpp" >}}

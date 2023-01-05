---
title: Insertar, eliminar filas y columnas
type: docs
weight: 40
url: /es/cpp/inserting-deleting-rows-and-columns/
---
## **Introducción**
Ya sea creando una nueva hoja de trabajo desde cero o trabajando en una hoja de trabajo existente, es posible que necesitemos agregar filas o columnas adicionales para acomodar más datos. A la inversa, es posible que también necesitemos eliminar filas o columnas de posiciones específicas en la hoja de trabajo. Para cumplir con estos requisitos, Aspose.Cells proporciona un conjunto de clases y métodos muy simple, que se analiza a continuación.
### **Gestión de filas y columnas**
 Aspose.Cells proporciona una clase,[ILibro de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) , que representa un archivo de Excel Microsoft. Él[ILibro de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) la clase contiene un[IHojas de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection) colección que permite el acceso a cada hoja de trabajo en un archivo de Excel. Una hoja de trabajo está representada por el[IHoja de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) clase. Él[IHoja de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) la clase proporciona una[ICélulas](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)colección que representa todas las celdas de la hoja de trabajo.

 Él[ICélulas](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)La colección proporciona varios métodos para administrar filas y columnas en una hoja de cálculo. Algunos de éstos se discuten a continuación.

{{% alert color="primary" %}} 

Cuando se agregan filas o columnas, el contenido de la hoja de cálculo se desplaza hacia abajo o hacia la derecha, y si se eliminan filas o columnas, el contenido se desplaza hacia arriba o hacia la izquierda.

{{% /alert %}} 
#### **Insertar una fila**
 Inserte una fila en la hoja de trabajo en cualquier lugar llamando al[Insertar fila](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ad9c067ccb5f34a7740f5d1cc3dbefbe7) metodo de la[ICélulas](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) recopilación. Él[Insertar fila](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ad9c067ccb5f34a7740f5d1cc3dbefbe7)El método toma el índice de la fila donde se insertará la nueva fila.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertRow.cpp" >}}


#### **Insertar varias filas**
 Para insertar varias filas en una hoja de trabajo, llame al[Insertar filas](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a61e4cd6dcaeeb0d11afd54616df75ee0) metodo de la[ICélulas](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) recopilación. Él[Insertar filas](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a61e4cd6dcaeeb0d11afd54616df75ee0)El método toma dos parámetros:

- Índice de fila, el índice de la fila desde donde se insertarán las nuevas filas.
- Número de filas, el número total de filas que deben insertarse.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertingMultipleRows.cpp" >}}


#### **Eliminación de varias filas**
Para eliminar varias filas de una hoja de trabajo, llame al[Eliminar filas](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a251261027b564ebdf27c2c6d5149c0e1) metodo de la[ICélulas](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) recopilación. Él[Eliminar filas](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a251261027b564ebdf27c2c6d5149c0e1)El método toma dos parámetros:

- Índice de fila, el índice de la fila desde donde se eliminarán las filas.
- Número de filas, el número total de filas que deben eliminarse.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeletingMultipleRows.cpp" >}}


#### **Insertar una columna**
 Los desarrolladores también pueden insertar una columna en la hoja de trabajo en cualquier ubicación llamando al[InsertarColumna](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a8e8cb6d0812129669258378649b3fd55) metodo de la[ICélulas](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) recopilación.[InsertarColumna](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a8e8cb6d0812129669258378649b3fd55)El método toma el índice de la columna donde se insertará la nueva columna.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertColumn.cpp" >}}


#### **Eliminar una columna**
 Para eliminar una columna de la hoja de cálculo en cualquier lugar, llame al[EliminarColumna](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ae00721fd2be220e7b73b2cab6a70e89b) metodo de la[ICélulas](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) recopilación. Él[EliminarColumna](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ae00721fd2be220e7b73b2cab6a70e89b)El método toma el índice de la columna a eliminar.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeleteColumn.cpp" >}}

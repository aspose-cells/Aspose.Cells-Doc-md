---
title: Insertar o Eliminar Filas o Columnas
type: docs
weight: 20
url: /es/net/insert-or-delete-rows-or-columns/
---

Ya sea que estemos creando una nueva hoja de cálculo desde cero o trabajando en una hoja de cálculo existente, es posible que necesitemos agregar filas o columnas adicionales en la hoja de cálculo para acomodar más datos o por alguna otra razón. Inversamente, también puede ser necesario eliminar filas o columnas de posiciones especificadas de la hoja de cálculo.
## **Administración de Filas/Columnas**
**Aspose.Cells** proporciona una clase, Workbook, que representa un archivo de Excel. La clase Workbook contiene una colección de Worksheets que permite acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase Worksheet. La clase Worksheet proporciona una colección de Cells que representa todas las celdas de la hoja de cálculo.

La colección de **Cells** proporciona varios métodos para administrar filas o columnas en una hoja de cálculo, de los cuales se discuten algunos a continuación con más detalle.
## **Insertar una Fila**
Los desarrolladores pueden insertar una fila en la hoja de cálculo en cualquier ubicación llamando al método InsertRow de la colección Cells. El método **InsertRow** toma el índice de la fila donde se insertará la nueva fila.

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(MyDir + "Row and Column Operation.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Inserting a row into the worksheet at 3rd position

worksheet.Cells.InsertRow(2);

//Saving the modified Excel file

workbook.Save(MyDir + "Inserting Row.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}
## **Insertar Múltiples Filas**
A veces, los desarrolladores pueden necesitar insertar múltiples filas en la hoja de cálculo. Esto se puede hacer llamando al método InsertRows de la colección Cells. El método InsertRows toma dos parámetros:

- **Índice de la Fila**, el índice de la fila desde donde se insertarán las nuevas filas
- **Número de Filas**, número total de filas que se deben insertar

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(MyDir + "Row and Column Operation.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Inserting 10 rows into the worksheet starting from 3rd row

worksheet.Cells.InsertRows(2, 10);

//Saving the modified Excel file

workbook.Save(MyDir + "Inserting Mutiple Rows.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}
## **Eliminar una Fila**
Los desarrolladores pueden eliminar una fila de la hoja de cálculo en cualquier ubicación llamando al método **DeleteRow** de la colección Cells. El método **DeleteRow** toma el índice de la fila que se desea eliminar.

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(MyDir + "Row and Column Operation.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Deleting 3rd row from the worksheet

worksheet.Cells.DeleteRow(2);

//Saving the modified Excel file

workbook.Save(MyDir + "Deleting Rows.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}
## **Eliminar Múltiples Filas**
Si los desarrolladores necesitan eliminar múltiples filas de la hoja de cálculo, también se puede hacer llamando al método DeleteRows de la colección Cells. El método DeleteRows toma dos parámetros:

- **Índice de la Fila**, el índice de la fila desde donde se eliminarán las filas.
- **Número de Filas**, número total de filas que se deben eliminar.

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(MyDir + "Row and Column Operation.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Deleting 10 rows from the worksheet starting from 3rd row

worksheet.Cells.DeleteRows(2, 10);

//Saving the modified Excel file

workbook.Save(MyDir + "Deleting Mutiple Rows.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}
## **Insertar una columna**
Los desarrolladores también pueden insertar una columna en la hoja de cálculo en cualquier ubicación llamando al método InsertColumn de la colección Cells. El método InsertColumn toma el índice de la columna donde se insertará la nueva columna.

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(MyDir + "Row and Column Operation.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Inserting a column into the worksheet at 2nd position

worksheet.Cells.InsertColumn(1);

//Saving the modified Excel file

workbook.Save(MyDir + "Inserting Column.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}
## **Eliminar una columna**
Para eliminar una columna de la hoja de cálculo en cualquier ubicación, los desarrolladores pueden llamar al método DeleteColumn de la colección Cells. El método DeleteColumn toma el índice de la columna a eliminar.

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(MyDir + "Row and Column Operation.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Deleting a column from the worksheet at 2nd position

worksheet.Cells.DeleteColumn(1);

//Saving the modified Excel file

workbook.Save(MyDir + "Deleting Column.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}
## **Descargar Código de Ejemplo**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Work%20with%20Rows%20n%20Columns%20%28Aspose.Cells%29.zip)

---
title: Insertar o eliminar filas o columnas
type: docs
weight: 20
url: /es/net/insert-or-delete-rows-or-columns/
---
Ya sea que estemos creando una nueva hoja de trabajo desde cero o estemos trabajando en una hoja de trabajo existente, es posible que necesitemos agregar filas o columnas adicionales en la hoja de trabajo para acomodar más datos o por alguna otra razón. A la inversa, también puede ser necesario eliminar filas o columnas de posiciones específicas de la hoja de trabajo.
## **Gestión de filas/columnas**
**Aspose.Cells** proporciona una clase, Libro de trabajo que representa un archivo de Excel. La clase de libro de trabajo contiene una colección de hojas de trabajo que permite acceder a cada hoja de trabajo en el archivo de Excel. Una hoja de trabajo está representada por la clase Worksheet. La clase Worksheet proporciona una colección Cells que representa todas las celdas de la hoja de trabajo.

**Cells**collection proporciona varios métodos para administrar filas o columnas en una hoja de trabajo, algunos de estos se analizan a continuación con más detalle.
## **Insertar una fila**
 Los desarrolladores pueden insertar una fila en la hoja de trabajo en cualquier lugar llamando al método InsertRow de la colección Cells.**Insertar fila** El método toma el índice de la fila donde se insertará la nueva fila.

{{< highlight "csharp" >}}

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
## **Insertar varias filas**
A veces, los desarrolladores pueden necesitar insertar varias filas en la hoja de trabajo. Se puede hacer llamando al método InsertRows de la colección Cells. El método InsertRows toma dos parámetros:

- **Índice de fila**, el índice de la fila desde donde se insertarán las nuevas filas
- **Número de filas**, número total de filas que deben insertarse

{{< highlight "csharp" >}}

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
## **Eliminación de una fila**
 Los desarrolladores pueden eliminar una fila de la hoja de trabajo en cualquier ubicación llamando al**Borrar fila** método de la colección Cells.**Borrar fila** El método toma el índice de la fila que debe eliminarse.

{{< highlight "csharp" >}}

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
## **Eliminación de varias filas**
Si los desarrolladores necesitan eliminar varias filas de la hoja de cálculo, también pueden hacerlo llamando al método DeleteRows de la colección Cells. El método DeleteRows toma dos parámetros:

- **Índice de fila**, el índice de la fila desde donde se eliminarán las filas.
- **Número de filas**, número total de filas que deben eliminarse.

{{< highlight "csharp" >}}

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
Los desarrolladores también pueden insertar una columna en la hoja de trabajo en cualquier ubicación llamando al método InsertColumn de la colección Cells. El método InsertColumn toma el índice de la columna donde se insertará la nueva columna.

{{< highlight "csharp" >}}

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
## **Eliminación de una columna**
Para eliminar una columna de la hoja de trabajo en cualquier ubicación, los desarrolladores pueden llamar al método DeleteColumn de la colección Cells. El método DeleteColumn toma el índice de la columna a eliminar.

{{< highlight "csharp" >}}

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
## **Descargar código de muestra**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Work%20with%20Rows%20n%20Columns%20%28Aspose.Cells%29.zip)

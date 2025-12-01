---
title: Insert or Delete Rows or Columns
type: docs
weight: 20
url: /net/insert-or-delete-rows-or-columns/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Whether we are creating a new worksheet from scratch or we are working on an existing worksheet, we may need to add extra rows or columns into the worksheet to accomodate more data or for some other reason. Inversely, it may also be required to delete rows or columns from specified positions of the worksheet.
## **Managing Rows/Columns**
**Aspose.Cells** provides a class, Workbook that represents an Excel file. Workbook class contains a Worksheets collection that allows to access each worksheet in the Excel file. A worksheet is represented by the Worksheet class. Worksheet class provides a Cells collection that represents all cells in the worksheet.

**Cells** collection provides several methods to manage rows or columns in a worksheet, few of these are discussed below in more detail.
## **Inserting a Row**
Developers can insert a row into the worksheet at any location by calling the InsertRow method of the Cells collection. **InsertRow** method takes the index of the row where the new row will be inserted.

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
## **Inserting Multiple Rows**
Sometimes, developers may need to insert multiple rows into the worksheet. It can be done by calling the InsertRows method of the Cells collection. InsertRows method takes two parameters:

- **Row Index**, the index of the row from where the new rows will be inserted
- **Number of Rows**, total number of rows that need to be inserted

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
## **Deleting a Row**
Developers can delete a row from the worksheet at any location by calling the **DeleteRow** method of the Cells collection. **DeleteRow** method takes the index of the row that needs to be deleted.

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
## **Deleting Multiple Rows**
If developers need to delete multiple rows from the worksheet, It can also be done by calling the DeleteRows method of the Cells collection. DeleteRows method takes two parameters:

- **Row Index**, the index of the row from where the rows will be deleted.
- **Number of Rows**, total number of rows that need to be deleted.

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
## **Inserting a Column**
Developers can also insert a column into the worksheet at any location by calling the InsertColumn method of the Cells collection. InsertColumn method takes the index of the column where the new column will be inserted.

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
## **Deleting a Column**
To delete a column from the worksheet at any location, developers can call DeleteColumn method of the Cells collection. DeleteColumn method takes the index of the column to delete.

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
## **Download Sample Code**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Work%20with%20Rows%20n%20Columns%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}

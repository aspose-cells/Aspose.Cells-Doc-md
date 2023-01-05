---
title: 插入或删除行或列
type: docs
weight: 20
url: /zh/net/insert-or-delete-rows-or-columns/
---
无论我们是从头开始创建新工作表还是处理现有工作表，我们都可能需要在工作表中添加额外的行或列以容纳更多数据或出于其他原因。反之，也可能需要从工作表的指定位置删除行或列。
## **管理行/列**
**Aspose.Cells**提供一个类，代表 Excel 文件的工作簿。 Workbook 类包含一个 Worksheets 集合，允许访问 Excel 文件中的每个工作表。工作表由 Worksheet 类表示。 Worksheet 类提供了一个 Cells 集合，代表工作表中的所有单元格。

**Cells**collection 提供了多种方法来管理工作表中的行或列，下面将详细讨论其中的一些方法。
## **插入一行**
开发人员可以通过调用 Cells 集合的 InsertRow 方法在工作表的任意位置插入一行。**插入行**方法采用将插入新行的行的索引。

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
## **插入多行**
有时，开发人员可能需要在工作表中插入多行。这可以通过调用 Cells 集合的 InsertRows 方法来完成。 InsertRows 方法有两个参数：

- **行索引**将插入新行的行的索引
- **行数**需要插入的总行数

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
## **删除一行**
开发人员可以通过调用**删除行**Cells采集方法。**删除行**方法采用需要删除的行的索引。

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
## **删除多行**
如果开发者需要从工作表中删除多行，也可以通过调用Cells集合的DeleteRows方法来完成。 DeleteRows 方法有两个参数：

- **行索引**，将从中删除行的行的索引。
- **行数**, 需要删除的总行数。

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
## **插入列**
开发人员还可以通过调用 Cells 集合的 InsertColumn 方法在工作表的任意位置插入一列。 InsertColumn 方法采用将插入新列的列的索引。

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
## **删除列**
要从工作表中的任何位置删除列，开发人员可以调用 Cells 集合的 DeleteColumn 方法。 DeleteColumn 方法获取要删除的列的索引。

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
## **下载示例代码**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [比特桶](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Work%20with%20Rows%20n%20Columns%20%28Aspose.Cells%29.zip)

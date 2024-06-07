---
title: 从文档导入导出数据
type: docs
weight: 10
url: /zh/net/import-export-data-from-document/
---

## **从文档导入数据**

数据是原始事实的集合，我们创建电子表格文档或报告来以更有意义的方式呈现这些原始事实。通常，我们自己添加数据到电子表格中，但有时我们需要重复使用现有的数据资源，这时就需要从不同的数据源导入数据到电子表格中。在本主题中，我们将讨论一些从不同数据源导入数据到工作表的技术。

## **使用Aspose.Cells导入数据**

当您使用**Aspose.Cells**打开Excel文件时，文件中的所有数据都会被自动导入，但Aspose.Cells还支持从不同的数据源导入数据。以下列出了一些这些数据源：

- **数组**
- **ArrayList**
- **DataTable**
- **DataColumn**
- **DataView**
- **DataGrid**
- **DataReader**
- **GridView**

Aspose.Cells提供了一个名为Workbook的类，代表一个Excel文件。Workbook类包含一个Worksheets集合，允许访问Excel文件中的每个工作表。工作表由Worksheet类表示。Worksheet类提供了一个Cells集合。

Cells集合提供了非常有用的方法，用于从不同的数据源导入数据。

### **从数组导入**

开发人员可以通过调用Cells集合的ImportArray方法从数组导入数据到他们的工作表。ImportArray方法有许多重载版本，但是典型的重载版本接受以下参数:

- 数组，表示需要导入其内容的数组对象
- 行号，表示将导入数据的第一个单元格的行号
- 列号，表示将导入数据的第一个单元格的列号
- 是否垂直，一个指定导入数据是垂直还是水平的布尔值

{{< highlight csharp >}}

//Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Creating an array containing names as string values

string[] names = new string[] { "laurence chen", "roman korchagin", "kyle huang" };

//Importing the array of names to 1st row and first column vertically

worksheet.Cells.ImportArray(names, 0, 0, true);

//Saving the Excel file

workbook.Save(MyDir+"DataImport from Array.xls");

{{< /highlight >}}

### **从ArrayList导入**

开发人员可以通过调用Cells集合的ImportArrayList方法将数据从ArrayList导入到其工作表。ImportArrayList方法接受以下参数: ArrayList，表示需要导入其内容的ArrayList对象

- 行号，表示将导入数据的第一个单元格的行号
- 列号，表示将导入数据的第一个单元格的列号
- 是否垂直，一个指定导入数据是垂直还是水平的布尔值

{{< highlight csharp >}}

//Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Instantiating an ArrayList object

ArrayList list = new ArrayList();

//Add few names to the list as string values

list.Add("laurence chen");

list.Add("roman korchagin");

list.Add("kyle huang");

list.Add("tommy wang");

//Importing the contents of ArrayList to 1st row and first column vertically

worksheet.Cells.ImportArrayList(list, 0, 0, true);

//Saving the Excel file

workbook.Save(MyDir + "DataImport from Array List.xls");

{{< /highlight >}}

### **从自定义对象导入**

开发人员可以使用ImportCustomObjects从对象集合导入数据到工作表。您可以向该方法提供列/属性的列表以显示您所需的对象列表。

{{< highlight csharp >}}

//Instantiate a new Workbook

Workbook book = new Workbook();

//Clear all the worksheets

book.Worksheets.Clear();

//Add a new Sheet "Data";

Worksheet sheet = book.Worksheets.Add("Data");

//Define List

List<WeeklyItem> list = new List<WeeklyItem>();

//Add data to the list of objects

list.Add(new WeeklyItem() { AtYarnStage = 1, InWIPStage = 2, Payment = 3, Shipment = 4, Shipment2 = 5 });

list.Add(new WeeklyItem() { AtYarnStage = 5, InWIPStage = 9, Payment = 7, Shipment = 2, Shipment2 = 5 });

list.Add(new WeeklyItem() { AtYarnStage = 7, InWIPStage = 3, Payment = 3, Shipment = 8, Shipment2 = 3 });

//We pick a few columns not all to import to the worksheet

sheet.Cells.ImportCustomObjects((System.Collections.ICollection)list,

new string[] { "Date", "InWIPStage", "Shipment", "Payment" },

true,

0,

0,

list.Count,

true,

"dd/mm/yyyy",

false);

//Auto-fit all the columns

book.Worksheets[0].AutoFitColumns();

//Save the Excel file

book.Save(MyDir+"ImportedCustomObjects.xls");

{{< /highlight >}}

### **从DataTable导入**

开发人员可以通过调用Cells集合的ImportDataTable方法将数据从DataTable导入到其工作表。ImportDataTable方法有许多重载版本，但是典型的重载版本接受以下参数:DataTable，表示需要导入其内容的DataTable对象

- 是否显示字段名称，指定DataTable的列名是否应作为第一行导入到工作表中
- 起始单元格，表示从哪个单元格（例如"A1"）开始导入DataTable的内容

{{< highlight csharp >}}

//Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Instantiating a "Products" DataTable object

DataTable dataTable = new DataTable("Products");

//Adding columns to the DataTable object

dataTable.Columns.Add("Product ID", typeof(Int32));

dataTable.Columns.Add("Product Name", typeof(string));

dataTable.Columns.Add("Units In Stock", typeof(Int32));

//Creating an empty row in the DataTable object

DataRow dr = dataTable.NewRow();

//Adding data to the row

dr[0] = 1;

dr[1] = "Aniseed Syrup";

dr[2] = 15;

//Adding filled row to the DataTable object

dataTable.Rows.Add(dr);

//Creating another empty row in the DataTable object

dr = dataTable.NewRow();

//Adding data to the row

dr[0] = 2;

dr[1] = "Boston Crab Meat";

dr[2] = 123;

//Adding filled row to the DataTable object

dataTable.Rows.Add(dr);

//Importing the contents of DataTable to the worksheet starting from "A1" cell,

//where true specifies that the column names of the DataTable would be added to

//the worksheet as a header row

worksheet.Cells.ImportDataTable(dataTable, true, "A1");

workbook.Save(MyDir+"Import From Data Table.xls");

{{< /highlight >}}

## **下载示例代码**

- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Import%20to%20Worksheet%20%28Aspose.Cells%29.zip)

## **从文档中导出数据**

Aspose.Cells不仅使用户可以从外部数据源向工作表导入数据，还允许他们将工作表数据导出到DataTable。我们知道DataTable是ADO.NET的一部分，用于保存数据。一旦数据存储在DataTable中，根据用户的需求可以以任何方式使用。

## **使用Aspose.Cells将数据导出到DataTable（.NET）**

开发人员可以通过调用Cells类的ExportDataTable或ExportDataTableAsString方法，轻松将其工作表数据导出到DataTable对象。这两种方法用于不同的场景，下面将更详细讨论这一点。

### **包含强类型数据的列**

我们知道电子表格将数据存储为行和列的序列。如果工作表的列中所有值都是强类型的（也就是说，列中的所有值必须具有相同的数据类型），那么我们就可以通过调用Cells类的ExportDataTable方法导出工作表内容。ExportDataTable方法接受以下参数将工作表数据导出为DataTable对象: 行号，表示将从哪个单元格开始导出数据的行号

- 列号，表示将从哪个单元格开始导出数据的列号
- 行数，表示要导出的行数
- 列数，表示要导出的列数
- 导出列名，一个布尔属性，指示是否应将工作表的第一行数据导出为DataTable的列名

{{< highlight csharp >}}

//Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(FOD_OpenFile.FileName, FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Exporting the contents of 2 rows and 2 columns starting from 1st cell to DataTable

DataTable dataTable = worksheet.Cells.ExportDataTable(0, 0,2, 2, true);

//Binding the DataTable with DataGrid

dataGridView1.DataSource = dataTable;

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

### **包含非强类型数据的列**

如果工作表的列中所有值都不是强类型的（即列中的值可能具有不同的数据类型），那么我们可以通过调用 Cells 类的**ExportDataTableAsString**方法导出工作表内容。**ExportDataTableAsString**方法接受与**ExportDataTable**方法相同的参数集以将工作表数据导出为**DataTable**对象。

{{< highlight csharp >}}

//Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(FOD_OpenFile.FileName, FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Exporting the contents of 2 rows and 2 columns starting from 1st cell to DataTable

DataTable dataTable = worksheet.Cells.ExportDataTableAsString(0, 0, 2, 2, true);

//Binding the DataTable with DataGrid

dataGridView2.DataSource = dataTable;

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

## **下载示例代码**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Export%20from%20Worksheet%20%28Aspose.Cells%29.zip)

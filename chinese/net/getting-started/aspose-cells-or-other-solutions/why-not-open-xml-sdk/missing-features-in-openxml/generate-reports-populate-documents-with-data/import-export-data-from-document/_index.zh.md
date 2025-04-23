---
title: 从文档中导入/导出数据
type: docs
weight: 10
url: /zh/net/import-export-data-from-document/
---

## **从文档中导入数据**

数据是原始事实的集合，我们创建电子表格文档或报告来以更有意义的方式呈现这些原始事实。通常，我们自己向电子表格添加数据，但有时候，我们需要重复使用现有的数据资源，这时就需要从不同的数据源导入数据到电子表格。在该主题中，我们将讨论从不同数据源导入数据到工作表的一些技术。

## **使用Aspose.Cells导入数据**

当您使用**Aspose.Cells**打开Excel文件时，文件中的所有数据都会自动导入，但Aspose.Cells还支持从不同数据源导入数据。下面列出了其中的一些数据源:

- **Array**
- **ArrayList**
- **DataTable**
- **DataColumn**
- **DataView**
- **DataGrid**
- **DataReader**
- **GridView**

Aspose.Cells提供了一个名为**Workbook**的类，表示Excel文件。Workbook类包含一个Worksheets集合，允许访问Excel文件中的每个工作表。工作表由Worksheet类表示。Worksheet类提供了Cells集合。

Cells集合提供非常有用的方法，可以从不同的数据源中导入数据。

### **从数组导入**

开发人员可以通过调用Cells集合的**ImportArray**方法将数据从数组导入其工作表。 ImportArray方法有许多重载版本，但典型的重载使用以下参数：

- 数组，表示需要导入其内容的数组对象
- 行号，表示导入数据的第一个单元格的行号
- 列号，表示导入数据的第一个单元格的列号
- 是否垂直，一个布尔值，指定垂直还是水平导入数据

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

开发人员可以通过调用Cells集合的**ImportArrayList**方法将数据从ArrayList导入其工作表。 ImportArray方法采用以下参数：**ArrayList**，表示需要导入其内容的ArrayList对象

- 行号，表示将要导入数据的第一个单元格的行号
- 列编号，表示要导入数据的第一个单元格的列号
- 是否垂直，一个布尔值，指定是垂直导入数据还是水平导入数据

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

开发人员可以使用**ImportCustomObjects**从对象集合中导入数据到工作表。您可以向该方法提供列/属性列表，以显示您期望的对象列表。

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

开发人员可以通过调用Cells集合的**ImportDataTable**方法，从**DataTable**导入数据到其工作表。 **ImportDataTable**方法有许多重载版本，但是一个典型的重载需要以下参数：**DataTable**，表示需要导入内容的**DataTable**对象

- **是否显示字段名**，指定是否将DataTable的列名导入到工作表作为第一行
- **起始单元格**，表示从何处（即"A1"）导入DataTable的内容

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

Aspose.Cells不仅可帮助用户从外部数据源导入数据到工作表中，还允许用户将工作表数据导出到**DataTable**中。我们知道**DataTable**是ADO.NET的一部分，用于保存数据。一旦数据存储在**DataTable**中，就可以根据用户的需求以任何方式使用。

## **使用 Aspose.Cells 将数据导出到 DataTable (.NET)**

开发人员可以通过调用Cells类的ExportDataTable或ExportDataTableAsString方法轻松将工作表数据导出到DataTable对象。这两种方法在不同的情况下使用，下面将更详细地讨论这两种方法。

### **包含强类型数据的列**

我们知道电子表格将数据存储为一系列行和列。如果工作表的所有列中的值都是强类型的（这意味着列中的所有值必须具有相同的数据类型），那么我们可以通过调用Cells类的**ExportDataTable**方法导出工作表内容。**ExportDataTable**方法采用以下参数将工作表数据导出为**DataTable**对象：**行号**，表示将要导出数据的第一个单元格的行号

- **列号**，表示将要导出数据的第一个单元格的列号
- **行数**，表示要导出的行数
- **列数**，表示要导出的列数
- **导出列名**，一个布尔属性，指示是否应将工作表的第一行数据作为DataTable的列名导出

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

如果工作表的所有列中的值都不是强类型的（这意味着列中的值可能具有不同的数据类型），那么我们可以通过调用Cells类的**ExportDataTableAsString**方法导出工作表内容。**ExportDataTableAsString**方法使用与**ExportDataTable**方法相同的一组参数将工作表数据导出为**DataTable**对象。

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
{{< app/cells/assistant language="csharp" >}}

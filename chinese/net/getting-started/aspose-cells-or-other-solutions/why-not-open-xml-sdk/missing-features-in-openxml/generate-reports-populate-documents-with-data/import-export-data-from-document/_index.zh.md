---
title: 从文档中导入导出数据
type: docs
weight: 10
url: /zh/net/import-export-data-from-document/
---
## **从文档中导入数据**

数据是原始事实的集合，我们创建电子表格文档或报告以更有意义的方式呈现这些原始事实。通常，我们自己将数据添加到电子表格中，但有时，我们需要重用现有的数据资源，这时就需要从不同的数据源导入数据到电子表格中。在本主题中，我们将讨论一些将数据从不同数据源导入工作表的技术。

## **使用 Aspose.Cells 导入数据**

当你使用**Aspose.Cells**打开Excel文件，自动导入文件中的所有数据，但Aspose.Cells还支持从不同数据源导入数据。下面列出了其中一些数据源：

- **大批**
- **数组列表**
- **数据表**
- **数据列**
- **数据视图**
- **数据网格**
- **数据阅读器**
- **网格视图**

Aspose.Cells提供了一个类，**工作簿**表示一个 Excel 文件。 Workbook 类包含一个 Worksheets 集合，允许访问 Excel 文件中的每个工作表。工作表由 Worksheet 类表示。 Worksheet 类提供了一个 Cells 集合。

Cells 集合提供了非常有用的方法来从不同的数据源导入数据。

### **从数组导入**

开发人员可以通过调用**导入数组**Cells采集方法。 ImportArray 方法有许多重载版本，但典型的重载采用以下参数：

- Array，表示需要导入内容的数组对象
- Row Number，表示要导入数据的第一个单元格的行号
- Column Number，表示将导入数据的第一个单元格的列号
- is Vertical，布尔值，指定垂直或水平导入数据

{{< highlight "csharp" >}}

//Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Creating an array containing names as string values

string[]names = new string[]{ "laurence chen", "roman korchagin", "kyle huang" };

//Importing the array of names to 1st row and first column vertically

worksheet.Cells.ImportArray(names, 0, 0, true);

//Saving the Excel file

workbook.Save(MyDir+"DataImport from Array.xls");

{{< /highlight >}}

### **从 ArrayList 导入**

开发人员可以通过调用**导入数组列表**Cells采集方法。 ImportArray 方法采用以下参数：**数组列表** ,代表需要导入内容的ArrayList对象

- Row Number ，表示要导入数据的第一个单元格的行号
- Column Number ，表示将导入数据的第一个单元格的列号
- 是 Vertical ，一个布尔值，指定垂直或水平导入数据

{{< highlight "csharp" >}}

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

开发人员可以使用以下方法将对象集合中的数据导入工作表**导入自定义对象**.您可以向该方法提供列/属性列表，以显示所需的对象列表。

{{< highlight "csharp" >}}

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

new string[]{ "Date", "InWIPStage", "Shipment", "Payment" },

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

### **从数据表导入**

开发人员可以从**数据表**通过调用他们的工作表**导入数据表**Cells采集方法。有许多重载版本**导入数据表**方法，但典型的重载采用以下参数：**数据表** , 代表**数据表**需要导入内容的对象

- **是否显示字段名称**指定是否应将 DataTable 的列名称作为第一行导入工作表
- **开始 Cell** 表示从中导入 DataTable 内容的起始单元格的名称（即“A1”）

{{< highlight "csharp" >}}

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

dr[0]= 1;

dr[1]= "Aniseed Syrup";

dr[2]= 15;

//Adding filled row to the DataTable object

dataTable.Rows.Add(dr);

//Creating another empty row in the DataTable object

dr = dataTable.NewRow();

//Adding data to the row

dr[0]= 2;

dr[1]= "Boston Crab Meat";

dr[2]= 123;

//Adding filled row to the DataTable object

dataTable.Rows.Add(dr);

//Importing the contents of DataTable to the worksheet starting from "A1" cell,

//where true specifies that the column names of the DataTable would be added to

//the worksheet as a header row

worksheet.Cells.ImportDataTable(dataTable, true, "A1");

workbook.Save(MyDir+"Import From Data Table.xls");

{{< /highlight >}}

## **下载示例代码**

- [比特桶](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Import%20to%20Worksheet%20%28Aspose.Cells%29.zip)

## **从文档中导出数据**

 Aspose.Cells 不仅方便其用户从外部数据源将数据导入工作表，还允许他们将工作表数据导出到**数据表**.据我们所知**数据表**是ADO.NET的一部分，用于保存数据。一旦数据存储在一个**数据表**，可根据用户要求任意使用。

## **使用Aspose.Cells将数据导出到DataTable（.NET）**

开发人员可以通过调用 Cells 类的 ExportDataTable 或 ExportDataTableAsString 方法轻松地将工作表数据导出到 DataTable 对象。这两种方法用于不同的场景，下面将对此进行更详细的讨论。

### **包含强类型数据的列**

我们知道电子表格将数据存储为一系列行和列。如果工作表列中的所有值都是强类型的（这意味着列中的所有值必须具有相同的数据类型），那么我们可以通过调用导出工作表内容**导出数据表** Cells 类的方法。**导出数据表**方法采用以下参数将工作表数据导出为**数据表**目的：**行号** , 表示要从中导出数据的第一个单元格的行号

- **列号** 表示要从中导出数据的第一个单元格的列号
- **行数** 表示要导出的行数
- **列数** 代表要导出的列数
- **导出列名**，一个布尔属性，指示工作表第一行中的数据是否应导出为 DataTable 的列名

{{< highlight "csharp" >}}

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

如果工作表列中的所有值都不是强类型的（这意味着列中的值可能具有不同的数据类型），那么我们可以通过调用导出工作表内容**ExportDataTableAsString** Cells 类的方法。**ExportDataTableAsString**方法采用与**导出数据表**将工作表数据导出为的方法**数据表**目的。

{{< highlight "csharp" >}}

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
- [比特桶](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Export%20from%20Worksheet%20%28Aspose.Cells%29.zip)

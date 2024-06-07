---
title: 装配电子表格
type: docs
weight: 10
url: /zh/net/assemble-spreadsheets/
---

本节描述如何：

从头开始创建新的Excel文件并向其中添加工作表。

- 向设计师电子表格添加工作表。
- 使用工作表名称访问工作表。
- 使用工作表名称从Excel文件中删除工作表。
- 使用工作表索引从Excel文件中删除工作表。
- Aspose.Cells提供一个代表Excel文件的Workbook类。Workbook类包含一个Worksheets集合，允许访问Excel文件中的每个工作表。

工作表由Worksheet类表示。Worksheet类提供了一系列属性和方法来管理工作表。
## **向新的Excel文件中添加工作表**
要以编程方式创建新的Excel文件：

- 创建Workbook类的对象。
- 调用Worksheets集合的Add方法。自动向Excel文件添加一个空工作表。可以通过向Worksheets集合传递新工作表的工作表索引来引用它。
- 获取工作表引用。
- 对工作表进行操作。
- 调用Workbook类的Save方法保存带有新工作表的新Excel文件。

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Setting the name of the newly added worksheet

worksheet.Name = "My Worksheet";

//Saving the Excel file

workbook.Save("Adding Worksheet.xls");

{{< /highlight >}}
## **向设计者电子表格添加工作表**
向设计师电子表格添加工作表的过程与添加新工作表的过程相同，唯一的区别是Excel文件已经存在，因此应在添加工作表之前将其打开。可以通过Workbook类打开设计师电子表格。

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("book1.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Setting the name of the newly added worksheet

worksheet.Name = "My Worksheet";

//Saving the Excel file

workbook.Save("Designer Spreadsheet.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}
## **使用工作表名称访问工作表**
通过指定名称或索引访问或获取任何工作表。

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("WorksHeet Operations.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing a worksheet using its sheet name

Worksheet worksheet = workbook.Worksheets["Sheet1"];

{{< /highlight >}}
## **使用表名删除工作表**
要从文件中删除工作表，请调用Worksheets集合的RemoveAt方法。将工作表名称传递给RemoveAt方法以删除特定的工作表。

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("WorksHeet Operations.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Removing a worksheet using its sheet name

workbook.Worksheets.RemoveAt("Sheet3");

workbook.Save("WorksHeet Operations.xls");

{{< /highlight >}}
## **使用工作表索引删除工作表**
当知道工作表名称时，通过名称删除工作表的方法效果很好。如果不知道工作表的名称，则使用重载版本的RemoveAt方法，该方法接收工作表的索引而不是工作表名称。

{{< highlight csharp >}}

 //creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("WorksHeet Operations.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Removing a worksheet using its sheet index

workbook.Worksheets.RemoveAt(1);

workbook.Save("WorksHeet Operations.xls");

{{< /highlight >}}
## **下载示例代码**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Assemble%20Worksheet%20%28Aspose.Cells%29.zip)

---
title: 组装电子表格
type: docs
weight: 10
url: /zh/net/assemble-spreadsheets/
---

本部分描述如何：

从头开始创建新的Excel文件并向其添加工作表

- 在设计电子表格中添加工作表
- 使用工作表名称访问工作表
- 使用工作表名称从Excel文件中移除工作表
- 使用工作表索引从Excel文件中移除工作表
- Aspose.Cells提供了一个名为Workbook的类，表示Excel文件。Workbook类包含了一个Worksheets集合，允许访问Excel文件中的每个工作表。

工作表由Worksheet类表示。Worksheet类提供了各种属性和方法来管理工作表。
## **向新的Excel文件添加工作表**
要通过程序创建新的Excel文件:

- 创建Workbook类的对象
- 调用Worksheets集合的Add方法。一个空的工作表会自动添加到Excel文件中。通过向Worksheets集合传递新工作表的工作表索引来引用它。
- 获得工作表的引用
- 对工作表进行操作
- 通过调用Workbook类的Save方法保存具有新工作表的新Excel文件

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
## **向设计电子表格添加工作表**
向设计电子表格添加工作表的过程与添加新工作表的过程相同，只是Excel文件已经存在，因此在添加工作表之前应该先打开它。可以通过Workbook类打开设计电子表格。

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
通过指定工作表的名称或索引来访问或获取任何工作表。

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("WorksHeet Operations.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing a worksheet using its sheet name

Worksheet worksheet = workbook.Worksheets["Sheet1"];

{{< /highlight >}}
## **使用工作表名称移除工作表**
要从文件中移除工作表，请调用Worksheets集合的RemoveAt方法。将工作表名称传递给RemoveAt方法以移除特定工作表。

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
## **通过页索引删除工作表**
按名称移除工作表适用于已知工作表名称的情况。如果不知道工作表的名称，可以使用重载版本的RemoveAt方法，该方法接受工作表的索引而不是工作表名称。

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

---
title: 组装电子表格
type: docs
weight: 10
url: /zh/net/assemble-spreadsheets/
---
本节介绍如何：

从头开始创建一个新的 Excel 文件并向其中添加工作表。

- 将工作表添加到设计器电子表格。
- 使用工作表名称访问工作表。
- 使用工作表名称从 Excel 文件中删除工作表。
- 使用工作表索引从 Excel 文件中删除工作表。
- Aspose.Cells 提供了一个类，Workbook，代表一个Excel文件。 Workbook 类包含一个 Worksheets 集合，允许访问 Excel 文件中的每个工作表。

工作表由 Worksheet 类表示。 Worksheet 类提供了广泛的属性和方法来管理工作表。
## **将工作表添加到新的 Excel 文件**
要以编程方式创建新的 Excel 文件：

- 创建工作簿类的对象。
- 调用 Worksheets 集合的 Add 方法。一个空工作表会自动添加到 Excel 文件中。可以通过将新工作表的工作表索引传递给 Worksheets 集合来引用它。
- 获取工作表参考。
- 在工作表上执行工作。
- 通过调用 Workbook 类的 Save 方法，保存带有新工作表的新 Excel 文件。

{{< highlight "csharp" >}}

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
## **将工作表添加到 Designer 电子表格**
将工作表添加到设计器电子表格的过程与添加新工作表的过程相同，只是 Excel 文件已经存在，因此应在添加工作表之前打开。工作簿类可以打开设计器电子表格。

{{< highlight "csharp" >}}

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
通过指定其名称或索引来访问或获取任何工作表。

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("WorksHeet Operations.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing a worksheet using its sheet name

Worksheet worksheet = workbook.Worksheets["Sheet1"];

{{< /highlight >}}
## **使用工作表名称删除工作表**
要从文件中删除工作表，请调用 Worksheets 集合的 RemoveAt 方法。将工作表名称传递给 RemoveAt 方法以删除特定工作表。

{{< highlight "csharp" >}}

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
当工作表的名称已知时，按名称删除工作表效果很好。如果您不知道工作表的名称，请使用 RemoveAt 方法的重载版本，该方法采用工作表的工作表索引而不是其工作表名称。

{{< highlight "csharp" >}}

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
- [比特桶](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Assemble%20Worksheet%20%28Aspose.Cells%29.zip)

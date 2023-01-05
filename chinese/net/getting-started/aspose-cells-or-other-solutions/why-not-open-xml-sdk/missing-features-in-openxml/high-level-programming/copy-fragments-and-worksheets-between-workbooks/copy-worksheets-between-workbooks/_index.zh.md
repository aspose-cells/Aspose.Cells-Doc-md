---
title: 在工作簿之间复制工作表
type: docs
weight: 10
url: /zh/net/copy-worksheets-between-workbooks/
---
Aspose.Cells 提供了一种方法 Aspose.Cells.Worksheet.Copy() 用于将数据和格式从源工作表复制到工作簿内或工作簿之间的另一个工作表。该方法将源工作表对象作为参数。

下面的示例演示如何将工作表从一个工作簿复制到另一个工作簿。

{{< highlight "csharp" >}}

string FilePath = @"..\..\..\示例文件\";

string FileName = FilePath + "在 Workbook.xlsx 之间复制工作表";

//创建一个新的工作簿。

工作簿 excelWorkbook0 = new Workbook();

//获取书中的第一个工作表。

工作表 ws0 = excelWorkbook0.Worksheets[0];

//将一些数据放入标题行（A1:A4）

对于 (int i = 0; i< 5; i++)

{

    ws0.Cells[i, 0].PutValue(string.Format("Header Row {0}", i));

}

//Put some detail data (A5:A999)

for (int i = 5; i < 1000; i++)

{

    ws0.Cells[i, 0].PutValue(string.Format("Detail Row {0}", i));

}

//Define a pagesetup object based on the first worksheet.

PageSetup pagesetup = ws0.PageSetup;

//The first five rows are repeated in each page...

//It can be seen in print preview.

pagesetup.PrintTitleRows = "$1:$5";

//Create another Workbook.

Workbook excelWorkbook1 = new Workbook();

//Get the first worksheet in the book.

Worksheet ws1 = excelWorkbook1.Worksheets[0];

//Name the worksheet.

ws1.Name = "MySheet";

//Copy data from the first worksheet of the first workbook into the

//first worksheet of the second workbook.

ws1.Copy(ws0);

//Save the excel file.

excelWorkbook1.Save(FileName);

{{< /highlight >}}
## **下载示例代码**
- [比特桶](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Copy%20between%20Workbooks%20%28Aspose.Cells%29.zip)

下面的示例演示如何将工作表从一个工作簿复制到另一个工作簿。

{{< highlight "csharp" >}}

 //创建一个新的工作簿。

工作簿 excelWorkbook0 = new Workbook();

//获取书中的第一个工作表。

工作表 ws0 = excelWorkbook0.Worksheets[0];

//将一些数据放入标题行（A1:A4）

对于 (int i = 0; i< 5; i++)

{

	ws0.Cells[i, 0].PutValue(string.Format("Header Row {0}", i));

}

//Put some detail data (A5:A999)

for (int i = 5; i < 1000; i++)

{

	ws0.Cells[i, 0].PutValue(string.Format("Detail Row {0}", i));

}

//Define a pagesetup object based on the first worksheet.

PageSetup pagesetup = ws0.PageSetup;

//The first five rows are repeated in each page...

//It can be seen in print preview.

pagesetup.PrintTitleRows = "$1:$5";

//Create another Workbook.

Workbook excelWorkbook1 = new Workbook();

//Get the first worksheet in the book.

Worksheet ws1 = excelWorkbook1.Worksheets[0];

//Name the worksheet.

ws1.Name = "MySheet";

//Copy data from the first worksheet of the first workbook into the

//first worksheet of the second workbook.

ws1.Copy(ws0);

//Save the excel file.

excelWorkbook1.Save("copyworksheet.xls");


{{< /highlight >}}
## **下载示例代码**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [比特桶](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Copy%20Sheet%20between%20Workbook%20%28Aspose.Cells%29.zip)

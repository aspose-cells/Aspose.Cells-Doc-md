---
title: 在工作簿中移动工作表
type: docs
weight: 30
url: /zh/net/move-worksheets-within-workbook/
---
Aspose.Cells提供了一个方法，Aspose.Cells.Worksheet.MoveTo()，用于将工作表移动到电子表格中的另一个位置。该方法将目标工作表索引作为参数。

下面的示例演示如何将工作表移动到工作簿中的另一个位置。

{{< highlight "csharp" >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Move Worksheet.xlsx";

//Open an existing excel file.

Workbook wb = new Workbook(FileName);

//Create a Worksheets object with reference to

//the sheets of the Workbook.

WorksheetCollection sheets = wb.Worksheets;

//Get the first worksheet.

Worksheet worksheet = sheets[0];

string test = worksheet.Name;

//Move the first sheet to the third position in the workbook.

worksheet.MoveTo(2);

//Save the excel file.

wb.Save(FileName);

{{< /highlight >}}
## **下载示例代码**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [比特桶](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Move%20Worksheet%20%28Aspose.Cells%29.zip)

---
title: 在 VSTO 和 Aspose.Cells 中添加指向 Cells 的超链接
type: docs
weight: 20
url: /zh/net/add-hyperlinks-to-cells-in-vsto-and-aspose-cells/
---
要向电子表格中的单元格添加超链接，请执行以下步骤：

1. 设置工作表：
1. 实例化一个 Application 对象。（仅限 VSTO。）
 1. 添加工作簿。
 1. 拿到第一张纸。
 1. 将文本添加到要添加超链接的单元格中。
1. 添加超链接。
1. 保存文档。

这些步骤显示在下面的代码示例中。第一个示例演示如何将 VSTO 与 C# 一起使用以将超链接添加到单元格。以下示例显示如何使用 Aspose.Cells for .NET 再次使用 C# 执行相同的操作。

代码示例生成一个 Excel 文件，该文件在第一个工作表的单元格 A1 中有一个超链接。

![待办事项：图片_替代_文本](picture1.png)

一个超链接被添加到单元格 A1。

## **VSTO**

{{< highlight "csharp" >}}

 //Instantiate the Application object.

Excel.Application ExcelApp = Application;

//Add a Workbook.

Excel.Workbook objBook = ExcelApp.Workbooks.Add(System.Reflection.Missing.Value);

//Get the First sheet.

Excel.Worksheet objSheet = (Excel.Worksheet)objBook.Sheets["Sheet1"];

//Define a range object(A1).

Excel.Range _range;

_range = objSheet.get_Range("A1", "A1");

//Add a hyperlink to it.

objSheet.Hyperlinks.Add(_range, "http://www.aspose.com/", Type.Missing, "Click to go to Aspose site", "Aspose Site!");

//Save the excel file.

objBook.SaveCopyAs("Hyperlink_test.xls");

//Quit the Application.

ExcelApp.Quit();

{{< /highlight >}}

## **Aspose.Cells**

{{< highlight "csharp" >}}

 //Instantiate a new Workbook object.

Workbook workbook = new Workbook();

//Get the First sheet.

Worksheet worksheet = workbook.Worksheets[0];

//Define A1 Cell.

Aspose.Cells.Cell cell = worksheet.Cells["A1"];

//Add a hyperlink to it.

int index = worksheet.Hyperlinks.Add("A1", 1, 1, "http://www.aspose.com/");

worksheet.Hyperlinks[index].TextToDisplay = "Aspose Site!";

worksheet.Hyperlinks[index].ScreenTip = "Click to go to Aspose site";

//Save the excel file.

workbook.Save("Hyperlink_test.xls");

{{< /highlight >}}

## **下载示例代码**

- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Add.Hyperlinks.to.Cells.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Add%20Hyperlinks%20to%20Cells%20\(Aspose.Cells\).zip/下载)
- [比特桶](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Add%20Hyperlinks%20to%20Cells%20\(Aspose.Cells\)。压缩）

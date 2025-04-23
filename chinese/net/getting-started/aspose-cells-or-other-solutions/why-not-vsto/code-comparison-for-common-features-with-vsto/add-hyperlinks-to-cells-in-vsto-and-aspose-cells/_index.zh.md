---
title: 在VSTO和Aspose.Cells中为单元格添加超链接
type: docs
weight: 20
url: /zh/net/add-hyperlinks-to-cells-in-vsto-and-aspose-cells/
---

要向电子表格中的单元格添加超链接，请执行以下步骤：

1. 设置工作表： 
   1. 实例化一个应用程序对象。(仅限于VSTO)
   1. 添加一个工作簿。
   1. 获取第一个工作表。
   1. 向要添加超链接的单元格中添加文本。
1. 添加超链接。
1. 保存文档。

下面的代码示例展示了这些步骤。首先的示例展示了如何使用VSTO和C#向单元格添加超链接。接下来的示例展示了如何使用Aspose.Cells for .NET再次使用C#做同样的事情。

代码示例生成一个Excel文件，其中包含第一个工作表上单元格A1中的超链接。

![todo:image_alt_text](picture1.png)

给单元格A1添加了一个超链接。

## **VSTO**

{{< highlight csharp >}}

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

{{< highlight csharp >}}

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
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Add%20Hyperlinks%20to%20Cells%20\(Aspose.Cells\).zip/download)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Add%20Hyperlinks%20to%20Cells%20\(Aspose.Cells\).zip)
{{< app/cells/assistant language="csharp" >}}

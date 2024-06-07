---
title: 旋转单元格文本
type: docs
weight: 100
url: /zh/net/rotating-cell-text/
---

{{% alert color="primary" %}}

有时，列标题比单元格中的数据要宽得多。这会在页面上造成不必要的空白。一个解决方案就是将文本垂直旋转，这样可以占用较少的水平空间。在 Microsoft Excel 中，旋转文本很容易。幸运的是，也可以通过编程的方式旋转文本，这样开发人员可以在他们的应用程序中创建电子表格时旋转标签。

本文介绍如何使用 [Aspose.Cells for .NET](/cells/zh/net/rotating-cell-text/) 旋转单元格中的文本，以及如何使用 [VSTO](/cells/zh/net/rotating-cell-text/) 进行相同操作的比较。

{{% /alert %}}

## **在单元格中旋转文本**

要在工作表单元格中旋转文本，请执行以下步骤:

1. 创建一个工作簿并获取一个工作表.
1. 添加示例文本.
1. 格式化文本: 旋转，添加背景颜色.
1. 保存文件。

随后的代码示例展示了如何首先在 [VSTO](/cells/zh/net/rotating-cell-text/) 中执行这些步骤（使用 C# 或 Visual Basic），然后在 [Aspose.Cells](/cells/zh/net/rotating-cell-text/) 中再次执行这些步骤（使用 C# 或 Visual Basic）。

本文中的代码示例给出了下面显示的输出。
**带有旋转文本的单元格。**

![todo:image_alt_text](rotating-cell-text_1.png)

### **使用 VSTO 旋转文本**

**C#**

{{< highlight csharp >}}

 using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;

//Instantiate the Application object.

Excel.ApplicationClass ExcelApp = new Excel.ApplicationClass();

//Add a Workbook.

Excel.Workbook objBook = ExcelApp.Workbooks.Add(System.Reflection.Missing.Value);

//Get the First sheet.

Excel.Worksheet objSheet = (Excel.Worksheet)objBook.Sheets["Sheet1"];

//Put some text into cell B2.

objSheet.Cells[2, 2] = "Aspose Heading";

//Define a range object(B2).

Excel.Range _range;

_range = objSheet.get_Range("B2", "B2");

//Specify the angle of rotation of the text.

_range.Orientation = 45;

//Set the background color.

_range.Interior.Color = System.Drawing.ColorTranslator.ToWin32(Color.FromArgb(0, 51, 105));

//Set the font color of cell text

_range.Font.Color = System.Drawing.ColorTranslator.ToOle(System.Drawing.Color.White);



//Save the excel file.

objBook.SaveCopyAs("c:\\VSTO_RotateText_test.xlsx");

//Quit the Application.

ExcelApp.Quit();



{{< /highlight >}}

#### **使用 Aspose.Cells for .NET 旋转文本**

**C#**

{{< highlight csharp >}}

 // Instantiate a new Workbook.

 Workbook objworkbook = new Workbook();

// Get the First sheet.

Worksheet objworksheet = objworkbook.Worksheets[0];

// Get Cells.

Cells objcells = objworksheet.Cells;// Get a particular Cell.

Cell objcell = objcells["B2"];// Put some text value.

objcell.PutValue("Aspose Heading");



// Get associated style object of the cell.

Style objstyle = objcell.GetStyle();

// Specify the angle of rotation of the text.

objstyle.RotationAngle = 45;



// Set the custom fill color of the cells.

objstyle.ForegroundColor = Color.FromArgb(0, 51, 105);



// Set the background pattern for fill color.

objstyle.Pattern = BackgroundType.Solid;

// Set the font color of cell text

objstyle.Font.Color = Color.White;



// Assign the updated style object back to the cell

objcell.SetStyle(objstyle);



// Save the work book

objworkbook.Save("c:\\RotateText_test.xlsx");



{{< /highlight >}}

---
title: 旋转 Cell 文本
type: docs
weight: 100
url: /zh/net/rotating-cell-text/
---
{{% alert color="primary" %}}

有时，列标题比下面单元格中的数据宽得多。这会导致页面上出现不必要的空白。一种解决方案是垂直旋转文本，以减少水平空间。在 Microsoft Excel 中，旋转文本很容易。幸运的是，也可以通过编程方式旋转文本，这样开发人员就可以在他们的应用程序中创建的电子表格中旋转标签。

本文着眼于如何使用旋转单元格中的文本[Aspose.Cells for .NET](/cells/zh/net/rotating-cell-text/)与做同样的事情相比[VSTO](/cells/zh/net/rotating-cell-text/).

{{% /alert %}}

## **Cells 中的旋转文本**

要旋转工作表单元格中的文本，请执行以下步骤：

1. 创建工作簿并获取工作表。
1. 添加示例文本。
1. 格式化文本：旋转，添加背景颜色。
1. 保存文件。

下面的代码示例展示了如何首先执行这些步骤[VSTO](/cells/zh/net/rotating-cell-text/)，使用 C# 或 Visual Basic，然后在[Aspose.Cells](/cells/zh/net/rotating-cell-text/), 再次使用 C# 或 Visual Basic。

本文中的代码示例给出如下所示的输出。
**带有旋转文本的单元格。**

![待办事项：图片_替代_文本](rotating-cell-text_1.png)

### **使用 VSTO 旋转文本**

**C#**

{{< highlight "csharp" >}}

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

objSheet.Cells[2, 2]= "Aspose Heading";

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

#### **旋转文本 Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}

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

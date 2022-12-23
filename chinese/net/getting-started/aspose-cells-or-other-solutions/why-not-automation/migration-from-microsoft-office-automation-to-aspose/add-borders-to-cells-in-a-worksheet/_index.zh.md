---
title: 在工作表中为 Cells 添加边框
type: docs
weight: 50
url: /zh/net/add-borders-to-cells-in-a-worksheet/
---
{{% alert color="primary" %}}

Aspose.Cells for .NET 允许您通过您的应用程序执行用户可以在 Microsoft Excel 中执行的几乎任何任务。 Aspose.Cells 性能强大且功能强大，并且具有独立于 Microsoft Automation 工作的额外优势。本文介绍如何使用 Aspose.Cells for .NET 与 VSTO 相比，如何为工作表中的单元格添加边框。

{{% /alert %}}

## **为 Cells 添加边框**

要为电子表格中的单元格添加边框，请执行以下步骤：

1. 设置工作表：
 1.实例化一个Application对象。
 （仅限 VSTO。）
 1. 添加工作簿。
 1. 拿到第一张纸。
 1. 向要添加边框的单元格添加文本。
1. 添加边框：
 1. 定义一个范围。
1. 对范围应用边框样式。
对您要设置的每个范围和每个边框样式重复此操作。此示例应用细线、细线、中线和粗线。
1. 结束：
 1.自动调整单元格所在的列以整齐地调整文本。
 1. 保存文件。

这些步骤显示在下面的代码中。第一个代码示例展示了如何使用[VSTO](/cells/zh/net/add-borders-to-cells-in-a-worksheet/)使用 C# 或 Visual Basic。在 VSTO 示例之后是显示如何使用执行相同步骤的示例[Aspose.Cells for .NET](/cells/zh/net/add-borders-to-cells-in-a-worksheet/)再次使用 C# 或 Visual Basic。 Aspose.Cells 代码示例要短得多，因为 Aspose.Cells 针对高效编码进行了优化。

该代码生成一个 Excel 文件，其中第一个工作表上有许多单元格，每个单元格具有不同的边框：

![待办事项：图片_替代_文本](add-borders-to-cells-in-a-worksheet_1.png)

**Cells 应用了边框。**

### **使用 VSTO 添加边框**

**C#**

{{< highlight "csharp" >}}

 .......

using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;

.......

//Instantiate the Application object.

Excel.ApplicationClass ExcelApp = new Excel.ApplicationClass();

//Add a Workbook.

Excel.Workbook objBook = ExcelApp.Workbooks.Add(System.Reflection.Missing.Value);

//Get the First sheet.

Excel.Worksheet objSheet = (Excel.Worksheet)objBook.Sheets["Sheet1"];



//Put some text into different cells (A2, A4, A6, A8).

objSheet.Cells[2, 1]= "Hair Lines";

objSheet.Cells[4, 1]= "Thin Lines";

objSheet.Cells[6, 1]= "Medium Lines";

objSheet.Cells[8, 1]= "Thick Lines";

//Define a range object(A2).

Excel.Range _range;

_range = objSheet.get_Range("A2", "A2");

//Get the borders collection.

Excel.Borders borders = _range.Borders;

//Set the hair lines style.

borders.LineStyle = Excel.XlLineStyle.xlContinuous;

borders.Weight = 1d;



//Define a range object(A4).

_range = objSheet.get_Range("A4", "A4");

//Get the borders collection.

borders = _range.Borders;

//Set the thin lines style.

borders.LineStyle = Excel.XlLineStyle.xlContinuous;

borders.Weight = 2d;



//Define a range object(A6).

_range = objSheet.get_Range("A6", "A6");

//Get the borders collection.

borders = _range.Borders;

//Set the medium lines style.

borders.LineStyle = Excel.XlLineStyle.xlContinuous;

borders.Weight = 3d;



//Define a range object(A8).

_range = objSheet.get_Range("A8", "A8");

//Get the borders collection.

borders = _range.Borders;

//Set the thick lines style.

borders.LineStyle = Excel.XlLineStyle.xlContinuous;

borders.Weight = 4d;



//Auto-fit Column A.

objSheet.get_Range("A2", "A2").EntireColumn.AutoFit();



//Save the excel file.

objBook.SaveAs("f:\\test\\ApplyBorders.xls",

Microsoft.Office.Interop.Excel.XlFileFormat.xlExcel8,

Type.Missing,

Type.Missing,

Type.Missing,

Type.Missing,

Microsoft.Office.Interop.Excel.XlSaveAsAccessMode.xlNoChange,

Type.Missing,

Type.Missing,

Type.Missing,

Type.Missing,

Type.Missing);



//Quit the Application.

ExcelApp.Quit();



{{< /highlight >}}

### **使用 Aspose.Cells 添加边框 for .NET**

**C#**

{{< highlight "csharp" >}}

 .......

using Aspose.Cells;

.......

//Instantiate a new Workbook.

Workbook objBook = new Workbook();  

//Get the First sheet.

Worksheet objSheet = objBook.Worksheets["Sheet1"];



//Put some text into different cells (A2, A4, A6, A8).

objSheet.Cells[1, 0].PutValue("Hair Lines");

objSheet.Cells[3, 0].PutValue("Thin Lines");

objSheet.Cells[5, 0].PutValue("Medium Lines");

objSheet.Cells[7, 0].PutValue("Thick Lines");

//Define a range object(A2).

Aspose.Cells.Range _range;

_range = objSheet.Cells.CreateRange("A2", "A2");

//Set the borders with hair lines style.

_range.SetOutlineBorders( CellBorderType.Hair, Color.Black);

//Define a range object(A4).

_range = objSheet.Cells.CreateRange("A4", "A4");

//Set the borders with thin lines style.

_range.SetOutlineBorders(CellBorderType.Thin, Color.Black);

//Define a range object(A6).

_range = objSheet.Cells.CreateRange("A6", "A6");

//Set the borders with medium lines style.

_range.SetOutlineBorders(CellBorderType.Medium, Color.Black);

//Define a range object(A8).

_range = objSheet.Cells.CreateRange("A8", "A8");

//Set the borders with thick lines style.

_range.SetOutlineBorders(CellBorderType.Thick, Color.Black);

//Auto-fit Column A.

objSheet.AutoFitColumn(0);

//Save the excel file.

objBook.Save("f:\\test\\ApplyBorders.xls");        



{{< /highlight >}}

---
title: 在工作表中的单元格添加边框
type: docs
weight: 50
url: /zh/net/add-borders-to-cells-in-a-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells 允许您通过应用程序执行几乎在 Microsoft Excel 中用户可以执行的任何任务。Aspose.Cells 性能优越且稳健，并且具有独立于 Microsoft Automation 的附加优势。本文展示了如何使用 Aspose.Cells for .NET 相对于 VSTO 在工作表中添加单元格边框。

{{% /alert %}}

## **向单元格添加边框**

要在电子表格中添加单元格边框，执行以下步骤：

1. 设置工作表：
   1. 实例化一个Application对象。
      （仅限VSTO。）
   1. 添加一个工作簿。
   1. 获取第一个工作表。
   1. 向要添加边框的单元格添加文本。
1. 添加边框:
   1. 定义一个范围。
   1. 对范围应用边框样式。
      对于要设置的每个范围和每种边框样式重复。此示例应用了发线、细线、中线和粗线。
1. 完成:
   1. 自动调整包含单元格的列以适应文本
   1. 保存文档。

下面的代码显示了这些步骤。首先的代码示例显示了如何使用 [VSTO](/cells/zh/net/add-borders-to-cells-in-a-worksheet/) 以及 C# 或 Visual Basic 实现它们。在 VSTO 示例之后是使用 [Aspose.Cells for .NET](/cells/zh/net/add-borders-to-cells-in-a-worksheet/) 的示例，同样使用 C# 或 Visual Basic。Aspose.Cells 代码示例要简短得多，因为 Aspose.Cells 针对高效编码进行了优化。

该代码生成具有不同边框的第一个工作表上的一些单元格的Excel文件:

![todo:image_alt_text](add-borders-to-cells-in-a-worksheet_1.png)

**应用了边框的单元格**

### **使用 VSTO 添加边框**

**C#**

{{< highlight csharp >}}

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

objSheet.Cells[2, 1] = "Hair Lines";

objSheet.Cells[4, 1] = "Thin Lines";

objSheet.Cells[6, 1] = "Medium Lines";

objSheet.Cells[8, 1] = "Thick Lines";

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

### **使用 Aspose.Cells for .NET 添加边框**

**C#**

{{< highlight csharp >}}

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

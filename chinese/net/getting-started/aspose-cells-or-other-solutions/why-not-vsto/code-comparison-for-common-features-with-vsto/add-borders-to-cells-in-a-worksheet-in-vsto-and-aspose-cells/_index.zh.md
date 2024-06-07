---
title: 在VSTO和Aspose.Cells中的工作表中为单元格添加边框
type: docs
weight: 10
url: /zh/net/add-borders-to-cells-in-a-worksheet-in-vsto-and-aspose-cells/
---

要向电子表格中的单元格添加边框，请执行以下步骤：

1. 设置工作表： 
   1. 实例化一个应用程序对象（仅限VSTO）
   1. 添加一个工作簿
   1. 获取第一个工作表
   1. 向要添加边框的单元格添加文本
1. 添加边框： 
   1. 定义一个区域
   1. 将边框样式应用于该区域
   1. 对每个区域和希望设置的每种边框样式重复此操作。 本示例应用了细边线、细线、中线和粗线
1. 完成： 
   1. 调整单元格所在列的宽度，以使文本整齐地适合
   1. 保存文档

以下代码显示了这些步骤。 首先的代码示例展示了如何使用C#或Visual Basic在VSTO中实现它们。 在VSTO示例之后，有示例显示如何使用Aspose.Cells for .NET执行相同的步骤，同样使用C#或Visual Basic。 Aspose.Cells的代码示例要短得多，因为Aspose.Cells经过了有效编码优化。

该代码生成一个包含第一个工作表上多个具有不同边框的单元格的Excel文件：

![todo:image_alt_text](picture1.png)

应用了边框的单元格
## **VSTO**
{{< highlight csharp >}}

 //Instantiate the Application object.

Excel.Application ExcelApp = Application;

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

objBook.SaveAs("ApplyBorders.xls",

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
## **Aspose.Cells**
{{< highlight csharp >}}

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

 _range.SetOutlineBorders(CellBorderType.Hair, Color.Black);

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

objBook.Save("ApplyBorders.xls");


{{< /highlight >}}
## **下载示例代码**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Add.Borders.to.Cells.in.a.Worksheet.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Add%20Borders%20to%20Cells%20in%20a%20Worksheet%20\(Aspose.Cells\).zip/download)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Add%20Borders%20to%20Cells%20in%20a%20Worksheet%20\(Aspose.Cells\).zip)

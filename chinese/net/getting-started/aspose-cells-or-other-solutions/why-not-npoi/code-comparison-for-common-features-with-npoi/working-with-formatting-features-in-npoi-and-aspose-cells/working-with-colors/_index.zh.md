---
title: 使用颜色
type: docs
weight: 20
url: /zh/net/working-with-colors/
---

## **Aspose.Cells - 使用颜色**
**C#**

{{< highlight cs >}}

 Workbook workbook = new Workbook(); // Creating a Workbook object

workbook.Worksheets.Add();

Worksheet worksheet = workbook.Worksheets[0];

//Accessing cell from the worksheet

Cell cell = worksheet.Cells["B2"];

Style style = cell.GetStyle();            

//Setting the foreground color to yellow            

style.BackgroundColor = Color.Yellow;

//Setting the background pattern to vertical stripe

style.Pattern = BackgroundType.VerticalStripe;            

//Saving the modified style to the "B2" cell.

cell.SetStyle(style);

// === Setting Foreground ===

//Adding custom color to the palette at 55th index

Color color = Color.FromArgb(212, 213, 0);

workbook.ChangePalette(color, 55);

//Accessing cell from the worksheet

cell = worksheet.Cells["B3"];

//Adding some value to the cell

cell.PutValue("Hello Aspose!");

workbook.Save("test.xlsx", SaveFormat.Xlsx); //Workbooks can be saved in many formats


{{< /highlight >}}
## **NPOI - HSSF XSSF - 使用颜色**
**C#**

{{< highlight cs >}}

 IWorkbook wb = new XSSFWorkbook();

// Create a Worksheet

ISheet ws = wb.CreateSheet("Sheet1");


// Aqua background

ICellStyle style = wb.CreateCellStyle();

style.FillBackgroundColor = IndexedColors.Aqua.Index;

style.FillPattern = FillPattern.BigSpots;

IRow row = ws.CreateRow(0);

ICell cell = row.CreateCell(1);

cell.SetCellValue("X");

cell.CellStyle = style;            

// Orange "foreground", foreground being the fill foreground not the font color.

style = wb.CreateCellStyle();

style.FillBackgroundColor = IndexedColors.Orange.Index;

style.FillPattern = FillPattern.SolidForeground;

cell = row.CreateCell(2);

cell.SetCellValue("X");

cell.CellStyle = style;

FileStream sw = File.Create("test.xlsx");

wb.Write(sw);

sw.Close();

{{< /highlight >}}
## **下载运行代码**
从以下社交编码网站之一下载**使用颜色**：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_Vs_NPOI_HWPF_and_XWPF_v1.1/Working.With.Colors.zip)

{{% alert color="primary" %}} 

欲了解更多详情，请访问[数据格式设置功能](http://www.aspose.com/docs/display/cellsjava/Working+with+Data+Formatting)。

{{% /alert %}}

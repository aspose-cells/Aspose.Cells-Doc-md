---
title : "Working With Fonts" 
description : "" 
weight : 20922 
toc : false
type: docs
url: /net/plugins/npoi/codeinnpoi/formattingfeatures/working+with+fonts/
---

# Aspose.Cells for .NET : Working With Fonts


## Aspose.Cells - Working With Fonts

**C#**

{{< code lang="c#" >}}
Workbook workbook = new Workbook(); // Creating a Workbook object
workbook.Worksheets.Add();
Worksheet worksheet = workbook.Worksheets[0];

// Adding some value to cell
Cell cell = worksheet.Cells["A1"];
cell.PutValue("This is Aspose test of fonts!");

// Setting the font name to "Times New Roman"
Style style = cell.GetStyle();
Font font = style.Font;

font.Name = "Courier New";
font.Size = 24;
font.IsBold = true;
font.Underline = FontUnderlineType.Single;
font.Color = Color.Blue;
font.IsStrikeout = true;

cell.SetStyle(style);

workbook.Save("test.xlsx", SaveFormat.Xlsx); //Workbooks can be saved in many formats

{{< /code >}}

## NPOI - HSSF XSSF - Working With Fonts

**C#**

{{< code lang="c#" >}}
IWorkbook wb = new XSSFWorkbook();

// Create a Worksheet
ISheet ws = wb.CreateSheet("Sheet1");

// Create a new font and alter it
IFont font = wb.CreateFont();
font.FontHeightInPoints = 24;
font.FontName = "Courier New";
font.IsItalic = true;
font.IsStrikeout = true;            

// Fonts are set into a style so create a new one to use.
ICellStyle style = wb.CreateCellStyle();
style.SetFont(font);

IRow row = ws.CreateRow(0);

// Create a cell and put a value in it.
ICell cell = row.CreateCell(1);
cell.SetCellValue("Thisi s a test of fonts");
cell.CellStyle = style;

FileStream sw = File.Create("test.xlsx");
wb.Write(sw);
sw.Close();
{{< /code >}}

## Download Running Code

Download **Working With Fonts** form any of the below mentioned social coding sites:

*   [CodePlex](https://asposenpoi.codeplex.com/downloads/get/1508250)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_Vs_NPOI_HWPF_and_XWPF_v1.1/Working.with.Fonts.zip)

For more details, visit [Data Formating Features](http://www.aspose.com/docs/display/cellsjava/Working+with+Data+Formatting).


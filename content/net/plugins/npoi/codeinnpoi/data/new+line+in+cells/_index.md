---
title : "New Line in Cells" 
description : "" 
weight : 20918 
toc : false
type: docs
url: /net/plugins/npoi/codeinnpoi/data/new+line+in+cells/
---

# Aspose.Cells for .NET : New Line in Cells


## Aspose.Cells - New Line in Cells

To ensure that text in a cell can be read, explicit line breaks and text wrapping can be applied. Text wrapping turns one line into several in a cell, which explicit line breaks put in breaks exactly where you want them.

To wrap text in a cell, use the `Aspose.Cells.Style.IsTextWrapped` property.

**C#**

{{< code lang="c#" >}}
Workbook workbook = new Workbook(); // Creating a Workbook object
Worksheet sheet = workbook.Worksheets[0];
sheet.Cells[2,2].Value = "Use \n with word wrap on to create a new line";

//Get Cell's Style
Style style = sheet.Cells[2, 2].GetStyle();

//Set Text Wrap property to true
style.IsTextWrapped = true;

//Set Cell's Style
sheet.Cells[2, 2].SetStyle(style);

workbook.Save("test.xlsx");
{{< /code >}}

## NPOI - HSSF XSSF - New Line in Cells

`CellStyle.setWrapText` should be true for wrapped text.

**C#**

{{< code lang="c#" >}}
IWorkbook workbook = new XSSFWorkbook();
ISheet sheet = workbook.CreateSheet("Sheet1");

IRow row = sheet.CreateRow(2);
ICell cell = row.CreateCell(2);
cell.SetCellValue("Use \n with word wrap on to create a new line");

//to enable newlines you need set a cell styles with wrap=true
ICellStyle cs = workbook.CreateCellStyle();
cs.WrapText = true;
cell.CellStyle = cs;

FileStream sw = File.Create("test.xlsx");
workbook.Write(sw);
sw.Close();
{{< /code >}}

## Download Running Code

Download **New Line in Cells** form any of the below mentioned social coding sites:

*   [CodePlex](https://asposenpoi.codeplex.com/downloads/get/1479035)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/New.Line.In.Cells.Aspose.Cells.zip)

For more details, visit [Line Breaks and Text Wrapping](http://www.aspose.com/docs/display/cellsnet/Line+Breaks+and+Text+Wrapping).


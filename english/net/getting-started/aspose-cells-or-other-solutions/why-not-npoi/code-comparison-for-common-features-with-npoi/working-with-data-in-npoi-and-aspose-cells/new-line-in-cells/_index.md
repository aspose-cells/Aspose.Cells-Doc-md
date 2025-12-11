---
title: New Line in Cells
type: docs
weight: 30
url: /net/new-line-in-cells/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - New Line in Cells**
To ensure that text in a cell can be read, explicit line breaks and text wrapping can be applied. Text wrapping turns a single line into multiple lines in a cell, while explicit line breaks place breaks exactly where you want them.

To wrap text in a cell, use the Aspose.Cells.Style.IsTextWrapped property.

**C#**

{{< highlight cs >}}

Workbook workbook = new Workbook(); // Creating a Workbook object

Worksheet sheet = workbook.Worksheets[0];

sheet.Cells[2, 2].Value = "Use \n with word wrap on to create a new line";

// Get the cell's style
Style style = sheet.Cells[2, 2].GetStyle();

// Set Text Wrap property to true
style.IsTextWrapped = true;

// Set the cell's style
sheet.Cells[2, 2].SetStyle(style);

workbook.Save("test.xlsx");

{{< /highlight >}}

## **NPOI - HSSF XSSF - New Line in Cells**
CellStyle.SetWrapText should be set to true for wrapped text.

**C#**

{{< highlight cs >}}

IWorkbook workbook = new XSSFWorkbook();

ISheet sheet = workbook.CreateSheet("Sheet1");

IRow row = sheet.CreateRow(2);

ICell cell = row.CreateCell(2);

cell.SetCellValue("Use \n with word wrap on to create a new line");

// To enable newlines you need to set a cell style with WrapText = true
ICellStyle cs = workbook.CreateCellStyle();
cs.WrapText = true;
cell.CellStyle = cs;

FileStream sw = File.Create("test.xlsx");
workbook.Write(sw);
sw.Close();

{{< /highlight >}}

## **Download Running Code**
Download **New Line in Cells** from any of the below mentioned social coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/New.Line.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 
For more details, visit [Line Breaks and Text Wrapping](/cells/net/line-breaks-and-text-wrapping/).
{{% /alert %}}

{{< app/cells/assistant language="csharp" >}}

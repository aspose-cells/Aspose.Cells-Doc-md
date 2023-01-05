---
title: Ny linje på Cells
type: docs
weight: 30
url: /sv/net/new-line-in-cells/
---
## **Aspose.Cells - Ny linje i Cells**
För att säkerställa att text i en cell kan läsas kan explicita radbrytningar och textbrytning tillämpas. Textbrytning förvandlar en rad till flera i en cell, vilka explicita radbrytningar sätts i brytningar precis där du vill ha dem.

Om du vill radbryta text i en cell använder du egenskapen Aspose.Cells.Style.IsTextWrapped.

**C#**

{{< highlight "cs" >}}

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

{{< /highlight >}}
## **NPOI - HSSF XSSF - Ny linje i Cells**
CellStyle.setWrapText ska vara sant för radbruten text.

**C#**

{{< highlight "cs" >}}

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

{{< /highlight >}}
## **Ladda ner Running Code**
 Ladda ner**Ny linje på Cells** bilda någon av nedan nämnda sociala kodningswebbplatser:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/New.Line.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 För mer information, besök[Radbrytningar och textbrytning](/cells/sv/net/line-breaks-and-text-wrapping/).

{{% /alert %}}

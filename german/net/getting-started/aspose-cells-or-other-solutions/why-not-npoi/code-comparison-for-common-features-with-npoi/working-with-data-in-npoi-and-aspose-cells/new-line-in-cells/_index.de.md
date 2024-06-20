---
title: Neue Zeile in Zellen
type: docs
weight: 30
url: /de/net/new-line-in-cells/
---

## **Aspose.Cells - Neue Zeile in Zellen**
Um sicherzustellen, dass der Text in einer Zelle gelesen werden kann, können explizite Zeilenumbrüche und Textumbrüche angewendet werden. Textumbrüche verwandeln eine Zeile in mehrere in einer Zelle, wobei explizite Zeilenumbrüche genau dort eingefügt werden, wo Sie sie haben möchten.

Um Text in einer Zelle umzubrechen, verwenden Sie die Eigenschaft Aspose.Cells.Style.IsTextWrapped.

**C#**

{{< highlight cs >}}

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
## **NPOI - HSSF XSSF - Neue Zeile in Zellen**
CellStyle.setWrapText sollte für umgebrochenen Text true sein.

**C#**

{{< highlight cs >}}

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
## **Laufenden Code herunterladen**
Laden Sie **Neue Zeile in Zellen** von einer der unten genannten sozialen Coding-Websites herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/New.Line.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

Für weitere Details besuchen Sie [Zeilenumbrüche und Textumbruch](/cells/de/net/line-breaks-and-text-wrapping/).

{{% /alert %}}

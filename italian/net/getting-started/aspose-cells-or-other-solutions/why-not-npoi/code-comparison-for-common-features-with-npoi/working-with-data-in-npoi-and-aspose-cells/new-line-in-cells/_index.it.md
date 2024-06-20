---
title: Nuova Linea nelle Celle
type: docs
weight: 30
url: /it/net/new-line-in-cells/
---

## **Aspose.Cells - Nuova Linea nelle Celle**
Per garantire che il testo in una cella possa essere letto, possono essere applicati ritorni a capo espliciti e a capo automatico del testo. Il ritorno a capo del testo trasforma una riga in più in una cella, mentre i ritorni a capo espliciti inseriscono spazi esattamente dove si desidera.

Per andare a capo nel testo di una cella, utilizzare la proprietà Aspose.Cells.Style.IsTextWrapped.

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
## **NPOI - HSSF XSSF - Nuova riga nelle celle**
CellStyle.setWrapText dovrebbe essere vero per il testo a capo automatico.

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
## **Scarica il codice in esecuzione**
Scarica **Nuova riga nelle celle** da uno dei siti di codice sociale menzionati di seguito:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/New.Line.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

Per ulteriori dettagli, visita [Interruzioni di linea e testo avvolgente](/cells/it/net/line-breaks-and-text-wrapping/).

{{% /alert %}}

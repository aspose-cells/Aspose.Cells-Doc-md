---
title: Conversione di Excel in formato OFD
description: Aspose.Cells è una libreria .NET per lavorare con file di fogli di calcolo che supporta la conversione di cartelle di lavoro Excel in formato OFD (Open Fixed-layout Document). Questo articolo mostra come creare contenuto Excel ed esportarlo come OFD, nonché come convertire file Excel esistenti in OFD utilizzando Aspose.Cells.
linktitle: Conversione di Excel in formato OFD
keywords: Aspose.Cells, libreria .NET, foglio di calcolo, Excel in OFD, conversione OFD, SaveFormat.Ofd, documento a layout fisso, esportazione cartella di lavoro
type: docs
weight: 195
url: /it/net/converting-excel-to-ofd-format/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells supporta la conversione di cartelle di lavoro Excel direttamente in formato OFD (Open Fixed-layout Document) utilizzando il valore di enumerazione `SaveFormat.Ofd`. Il documento OFD risultante preserva il layout visibile, il contenuto, le celle unite, la larghezza delle colonne, l'altezza delle righe, i caratteri, i colori, i bordi e i formati numerici della cartella di lavoro. Ciò rende Aspose.Cells adatto per flussi di lavoro di archiviazione, stampa, deposito normativo e invio alle autorità governative che richiedono un output a layout fisso.
{{% /alert %}}

## **Introduzione**
OFD (Open Fixed-layout Document) è uno standard nazionale cinese (GB/T 33190-2016) per la rappresentazione di documenti digitali in un layout fisso basato su pagine. Svolge un ruolo simile a PDF per i casi d'uso in cui l'aspetto visivo del documento sorgente deve essere preservato esattamente come è stato creato. OFD è ampiamente adottato per invii governativi, depositi normativi, fatture elettroniche e archiviazione a lungo termine nella Repubblica Popolare Cinese.
La conversione di cartelle di lavoro Excel in OFD è un requisito comune in scenari in cui il contenuto del foglio di calcolo deve essere distribuito come artefatto di sola lettura, con layout bloccato, anziché come foglio di calcolo modificabile. Esempi includono l'invio di una fattura finalizzata a un cliente, l'archiviazione di un rapporto finanziario trimestrale o l'invio di un foglio di calcolo del budget a un'autorità di regolamentazione. Aspose.Cells soddisfa questo requisito tramite il valore di enumerazione `SaveFormat.Ofd`, che scrive la cartella di lavoro direttamente in OFD senza richiedere un passaggio di conversione intermedio. L'output OFD preserva i valori delle celle, gli intervalli uniti, i caratteri, i colori, i bordi, i formati numerici e le opzioni di impostazione della pagina configurate sulla cartella di lavoro.

{{% alert color="primary" %}}
L'output OFD generato da Aspose.Cells preserva il layout visibile della cartella di lavoro sorgente, incluso il contenuto delle celle, le celle unite, la larghezza delle colonne e l'altezza delle righe. Anche la formattazione delle celle come caratteri, colori, bordi, allineamento e formati numerici viene resa nell'output a layout fisso. Le opzioni di impostazione della pagina configurate sul foglio di lavoro, come formato carta, orientamento e area di stampa, influenzano il layout del documento OFD risultante.
{{% /alert %}}

## **Creazione di una cartella di lavoro Excel e salvataggio come OFD**
Aspose.Cells consente di creare una cartella di lavoro a livello di codice, popolarla con dati e quindi salvarla direttamente in formato OFD utilizzando l'enumerazione `SaveFormat.Ofd`. L'esempio seguente crea una fattura da zero. Aggiunge un logo aziendale, informazioni di intestazione, una sezione di fatturazione, voci di dettaglio e totali calcolati, quindi esporta la cartella di lavoro in un documento OFD.

### **Creazione di una fattura con un logo**
L'esempio costruisce un foglio di lavoro fattura inserendo un'immagine del logo nell'area in alto a sinistra, compilando il nome dell'azienda e i dettagli di contatto, aggiungendo un titolo "INVOICE" (FATTURA) su celle unite, registrando il numero e la data della fattura, elencando il cliente da fatturare, costruendo una tabella di voci con colonne descrizione, quantità, prezzo unitario e totale, e calcolando il subtotale, l'imposta e il totale complessivo utilizzando formule di cella. La formattazione come intestazioni in grassetto, formato valuta per i prezzi, bordi e larghezza delle colonne viene applicata utilizzando oggetti `Style` e `Font`. Infine, la cartella di lavoro viene salvata con l'estensione `.ofd` utilizzando `SaveFormat.Ofd`.

```csharp
using System;
using Aspose.Cells;
using System.Drawing;
string dataDir = "C:\\Temp\\";
// Create a new Workbook
Workbook workbook = new Workbook();
// Obtain the first worksheet
Worksheet worksheet = workbook.Worksheets[0];
// Set column widths
worksheet.Cells.SetColumnWidth(0, 5);
worksheet.Cells.SetColumnWidth(1, 35);
worksheet.Cells.SetColumnWidth(2, 12);
worksheet.Cells.SetColumnWidth(3, 15);
worksheet.Cells.SetColumnWidth(4, 15);
worksheet.Cells.SetColumnWidth(5, 5);
// Insert company logo
worksheet.Pictures.Add(1, 1, dataDir + "logo.png");
// Company name and contact details
worksheet.Cells["B3"].PutValue("Acme Corporation");
worksheet.Cells["B4"].PutValue("123 Business Street");
worksheet.Cells["B5"].PutValue("City, State 12345");
worksheet.Cells["B6"].PutValue("Phone: (555) 123-4567");
// INVOICE title - merge cells
worksheet.Cells.Merge(7, 1, 2, 4);
Cell titleCell = worksheet.Cells["B8"];
titleCell.PutValue("INVOICE");
Style titleStyle = workbook.CreateStyle();
titleStyle.Font.IsBold = true;
titleStyle.Font.Size = 20;
titleStyle.HorizontalAlignment = TextAlignmentType.Center;
titleCell.SetStyle(titleStyle);
// Invoice number and date
worksheet.Cells["B11"].PutValue("Invoice Number:");
worksheet.Cells["C11"].PutValue("INV-2024-001");
worksheet.Cells["B12"].PutValue("Date:");
worksheet.Cells["C12"].PutValue(DateTime.Now.ToString("yyyy-MM-dd"));
// Bill-to section
worksheet.Cells["B14"].PutValue("Bill To:");
worksheet.Cells["B15"].PutValue("Client Name");
worksheet.Cells["B16"].PutValue("Client Address");
worksheet.Cells["B17"].PutValue("Client City, State");
// Line items header
Cell headerDesc = worksheet.Cells["B19"];
Cell headerQty = worksheet.Cells["C19"];
Cell headerPrice = worksheet.Cells["D19"];
Cell headerTotal = worksheet.Cells["E19"];
headerDesc.PutValue("Description");
headerQty.PutValue("Quantity");
headerPrice.PutValue("Unit Price");
headerTotal.PutValue("Total");
Style headerStyle = workbook.CreateStyle();
headerStyle.Font.IsBold = true;
headerStyle.Font.Color = Color.White;
headerStyle.ForegroundColor = Color.Navy;
headerStyle.Pattern = BackgroundType.Solid;
headerStyle.HorizontalAlignment = TextAlignmentType.Center;
headerStyle.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
headerStyle.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
headerStyle.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
headerStyle.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;
headerDesc.SetStyle(headerStyle);
headerQty.SetStyle(headerStyle);
headerPrice.SetStyle(headerStyle);
headerTotal.SetStyle(headerStyle);
// Currency style with borders
Style currencyStyle = workbook.CreateStyle();
currencyStyle.Custom = "\"$\"#,##0.00";
currencyStyle.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
currencyStyle.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
currencyStyle.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
currencyStyle.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;
// Plain border style for description/quantity cells
Style borderStyle = workbook.CreateStyle();
borderStyle.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
borderStyle.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
borderStyle.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
borderStyle.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;
// Line items rows
object[,] lineItems = new object[,] {
    {"Product A - Widget", 2, 50.00},
    {"Product B - Gadget", 3, 75.00},
    {"Product C - Service", 1, 100.00}
};
for (int i = 0; i < lineItems.GetLength(0); i++)
{
    int row = 20 + i;
    Cell descCell = worksheet.Cells[row, 1];
    Cell qtyCell = worksheet.Cells[row, 2];
    Cell priceCell = worksheet.Cells[row, 3];
    Cell totalCell = worksheet.Cells[row, 4];
    descCell.PutValue(lineItems[i, 0]);
    qtyCell.PutValue(lineItems[i, 1]);
    priceCell.PutValue(lineItems[i, 2]);
    totalCell.Formula = "C" + (row + 1) + "*D" + (row + 1);
    descCell.SetStyle(borderStyle);
    qtyCell.SetStyle(borderStyle);
    priceCell.SetStyle(currencyStyle);
    totalCell.SetStyle(currencyStyle);
}
// Subtotal, tax, grand total
worksheet.Cells["B24"].PutValue("Subtotal:");
Cell subtotalCell = worksheet.Cells["E24"];
subtotalCell.Formula = "SUM(E21:E23)";
worksheet.Cells["B25"].PutValue("Tax (10%):");
Cell taxCell = worksheet.Cells["E25"];
taxCell.Formula = "E24*0.1";
worksheet.Cells["B26"].PutValue("Grand Total:");
Cell grandTotalCell = worksheet.Cells["E26"];
grandTotalCell.Formula = "E24+E25";
// Bold + currency style for total values
Style totalStyle = workbook.CreateStyle();
totalStyle.Font.IsBold = true;
totalStyle.Custom = "\"$\"#,##0.00";
subtotalCell.SetStyle(totalStyle);
taxCell.SetStyle(totalStyle);
grandTotalCell.SetStyle(totalStyle);
// Bold style for total labels
Style boldStyle = workbook.CreateStyle();
boldStyle.Font.IsBold = true;
worksheet.Cells["B24"].SetStyle(boldStyle);
worksheet.Cells["B25"].SetStyle(boldStyle);
worksheet.Cells["B26"].SetStyle(boldStyle);
// Save the workbook as an OFD file
workbook.Save(dataDir + "Invoice.ofd", SaveFormat.Ofd);
```

## **Conversione di un file Excel esistente in OFD**
Aspose.Cells può anche caricare una cartella di lavoro Excel esistente dal disco ed esportarla direttamente in formato OFD. Ciò è utile per pipeline di conversione in batch, flussi di lavoro di archiviazione e scenari in cui la cartella di lavoro sorgente è stata prodotta da un altro strumento e deve solo essere riemessa come artefatto a layout fisso. L'esempio seguente carica una cartella di lavoro `.xlsx` esistente, legge i dati dalle sue celle, applica eventuali regolazioni di impostazione della pagina e salva il risultato come documento OFD.

```csharp
using System;
using Aspose.Cells;
string dataDir = "C:\\Examples\\";
// Open an existing Excel workbook from disk
Workbook workbook = new Workbook(dataDir + "SampleBook.xlsx");
// (1) Read and display values from selected cells to confirm the file was loaded
Worksheet firstSheet = workbook.Worksheets[0];
Console.WriteLine("First sheet name: " + firstSheet.Name);
Console.WriteLine("Cell A1: " + firstSheet.Cells["A1"].StringValue);
Console.WriteLine("Cell B1: " + firstSheet.Cells["B1"].StringValue);
Console.WriteLine("Cell C1: " + firstSheet.Cells["C1"].StringValue);
// (2) Iterate over the Worksheets collection to enumerate available sheets
Console.WriteLine("\nAvailable worksheets:");
for (int i = 0; i < workbook.Worksheets.Count; i++)
{
    Worksheet ws = workbook.Worksheets[i];
    Console.WriteLine("  [" + i + "] " + ws.Name);
}
// (3) Optionally update a timestamp cell to reflect the conversion
firstSheet.Cells["A1"].PutValue("Converted on: " + DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss"));
// Append a summary header row at the top of the data block
firstSheet.Cells.InsertRow(0);
firstSheet.Cells["A1"].PutValue("Conversion Summary");
firstSheet.Cells["A2"].PutValue("Generated: " + DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss"));
// (4) Configure PageSetup properties on the worksheet
PageSetup pageSetup = firstSheet.PageSetup;
pageSetup.Orientation = PageOrientationType.Landscape;
pageSetup.PaperSize = PaperSizeType.PaperA4;
pageSetup.FitToPagesTall = 1;
pageSetup.FitToPagesWide = 1;
// (5) Optionally set the print area for the OFD output
int lastRow = firstSheet.Cells.MaxDataRow;
int lastCol = firstSheet.Cells.MaxDataColumn;
string lastColLetter = CellsHelper.ColumnIndexToName(lastCol);
string printArea = "A1:" + lastColLetter + (lastRow + 1);
firstSheet.PageSetup.PrintArea = printArea;
Console.WriteLine("\nPrint area set to: " + printArea);
// (6) Save the workbook as an OFD file
workbook.Save(dataDir + "SampleBook.ofd", SaveFormat.Ofd);
Console.WriteLine("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd");
```

## **Articoli correlati**
- [Divisione di file Excel in più file](/cells/it/net/splitting-excel-files-into-multiple-files/)
- [Inserimento di un'immagine in una cella](/cells/it/net/inserting-an-image-into-a-cell/)
- [Lettura e scrittura di file DBF](/cells/it/net/dbf/)
- [Conversione di sparkline in immagine e HTML in Aspose.Cells for .NET](/cells/it/net/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="csharp" >}}
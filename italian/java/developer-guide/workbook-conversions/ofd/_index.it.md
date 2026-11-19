---
title: Conversione di Excel in formato OFD
description: Aspose.Cells è una libreria Java per lavorare con file di fogli di calcolo che supporta la conversione di cartelle di lavoro Excel in formato OFD (Open Fixed-layout Document). Questo articolo mostra come creare contenuti Excel ed esportarli come OFD, nonché come convertire file Excel esistenti in OFD utilizzando Aspose.Cells.
linktitle: Conversione di Excel in formato OFD
keywords: Aspose.Cells, libreria Java, foglio di calcolo, Excel in OFD, conversione OFD, SaveFormat.Ofd, documento a layout fisso, esportazione cartella di lavoro
type: docs
weight: 195
url: /it/java/converting-excel-to-ofd-format/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells supporta la conversione diretta delle cartelle di lavoro Excel in formato OFD (Open Fixed-layout Document) utilizzando il valore di enumerazione `SaveFormat.Ofd`. Il documento OFD risultante preserva il layout visibile, il contenuto, le celle unite, la larghezza delle colonne, l'altezza delle righe, i caratteri, i colori, i bordi e i formati numerici della cartella di lavoro. Questo rende Aspose.Cells adatto per flussi di lavoro di archiviazione, stampa, deposito normativo e presentazione alle autorità governative che richiedono un output a layout fisso.
{{% /alert %}}

## **Introduzione**
OFD (Open Fixed-layout Document) è uno standard nazionale cinese (GB/T 33190-2016) per la rappresentazione di documenti digitali in un layout fisso, basato su pagine. Svolge un ruolo simile a quello del PDF per casi d'uso in cui l'aspetto visivo del documento sorgente deve essere preservato esattamente come è stato creato. OFD è ampiamente adottato per le presentazioni alle autorità governative, i depositi normativi, le fatture elettroniche e l'archiviazione a lungo termine nella Repubblica Popolare Cinese.
La conversione delle cartelle di lavoro Excel in OFD è un requisito comune negli scenari in cui il contenuto del foglio di calcolo deve essere distribuito come artefatto di sola lettura, con layout bloccato, anziché come foglio di calcolo modificabile. Esempi includono l'invio di una fattura finalizzata a un cliente, l'archiviazione di un rapporto finanziario trimestrale o la presentazione di un foglio di calcolo del budget a un'autorità di regolamentazione. Aspose.Cells soddisfa questo requisito attraverso il valore di enumerazione `SaveFormat.Ofd`, che scrive la cartella di lavoro direttamente in OFD senza richiedere un passaggio intermedio di conversione. L'output OFD preserva i valori delle celle, gli intervalli uniti, i caratteri, i colori, i bordi, i formati numerici e le opzioni di impostazione della pagina configurate sulla cartella di lavoro.

{{% alert color="primary" %}}
L'output OFD generato da Aspose.Cells preserva il layout visibile della cartella di lavoro sorgente, inclusi il contenuto delle celle, le celle unite, la larghezza delle colonne e l'altezza delle righe. Anche la formattazione delle celle come caratteri, colori, bordi, allineamento e formati numerici viene resa nell'output a layout fisso. Le opzioni di impostazione della pagina configurate sul foglio di lavoro, come il formato carta, l'orientamento e l'area di stampa, influenzano il layout del documento OFD risultante.
{{% /alert %}}

## **Creazione di una cartella di lavoro Excel e salvataggio come OFD**
Aspose.Cells consente di creare una cartella di lavoro a livello di codice, popolarla con dati e quindi salvarla direttamente in formato OFD utilizzando l'enumerazione `SaveFormat.Ofd`. L'esempio seguente crea una fattura da zero. Aggiunge un logo aziendale, le informazioni di intestazione, una sezione destinatario della fattura, le voci e i totali calcolati, quindi esporta la cartella di lavoro in un documento OFD.

### **Creazione di una fattura con un logo**
L'esempio costruisce un foglio di lavoro per fattura inserendo un'immagine del logo nell'area in alto a sinistra, compilando il nome dell'azienda e i dettagli di contatto, aggiungendo un titolo "INVOICE" attraverso celle unite, registrando il numero e la data della fattura, elencando il cliente da fatturare, costruendo una tabella delle voci con colonne di descrizione, quantità, prezzo unitario e totale, e calcolando il subtotale, l'imposta e il totale generale utilizzando formule nelle celle. La formattazione come intestazioni in grassetto, formato valuta per i prezzi, bordi e larghezze delle colonne viene applicata utilizzando gli oggetti `Style` e `Font`. Infine, la cartella di lavoro viene salvata con l'estensione `.ofd` utilizzando `SaveFormat.Ofd`.

```java
import com.aspose.cells.*;
import java.text.SimpleDateFormat;
import java.util.Date;
String dataDir = "C:\\Temp\\";
// Create a new Workbook
Workbook workbook = new Workbook();
// Obtain the first worksheet
Worksheet worksheet = workbook.getWorksheets().get(0);
// Set column widths
worksheet.getCells().setColumnWidth(0, 5);
worksheet.getCells().setColumnWidth(1, 35);
worksheet.getCells().setColumnWidth(2, 12);
worksheet.getCells().setColumnWidth(3, 15);
worksheet.getCells().setColumnWidth(4, 15);
worksheet.getCells().setColumnWidth(5, 5);
// Insert company logo
worksheet.getPictures().add(1, 1, dataDir + "logo.png");
// Company name and contact details
worksheet.getCells().get("B3").putValue("Acme Corporation");
worksheet.getCells().get("B4").putValue("123 Business Street");
worksheet.getCells().get("B5").putValue("City, State 12345");
worksheet.getCells().get("B6").putValue("Phone: (555) 123-4567");
// INVOICE title - merge cells
worksheet.getCells().merge(7, 1, 2, 4);
Cell titleCell = worksheet.getCells().get("B8");
titleCell.putValue("INVOICE");
Style titleStyle = workbook.createStyle();
titleStyle.getFont().setBold(true);
titleStyle.getFont().setSize(20);
titleStyle.setHorizontalAlignment(TextAlignmentType.CENTER);
titleCell.setStyle(titleStyle);
// Invoice number and date
worksheet.getCells().get("B11").putValue("Invoice Number:");
worksheet.getCells().get("C11").putValue("INV-2024-001");
worksheet.getCells().get("B12").putValue("Date:");
worksheet.getCells().get("C12").putValue(new SimpleDateFormat("yyyy-MM-dd").format(new Date()));
// Bill-to section
worksheet.getCells().get("B14").putValue("Bill To:");
worksheet.getCells().get("B15").putValue("Client Name");
worksheet.getCells().get("B16").putValue("Client Address");
worksheet.getCells().get("B17").putValue("Client City, State");
// Line items header
Cell headerDesc = worksheet.getCells().get("B19");
Cell headerQty = worksheet.getCells().get("C19");
Cell headerPrice = worksheet.getCells().get("D19");
Cell headerTotal = worksheet.getCells().get("E19");
headerDesc.putValue("Description");
headerQty.putValue("Quantity");
headerPrice.putValue("Unit Price");
headerTotal.putValue("Total");
Style headerStyle = workbook.createStyle();
headerStyle.getFont().setBold(true);
headerStyle.getFont().setColor(Color.getWhite());
headerStyle.setBackgroundColor(Color.getNavy());
headerStyle.setHorizontalAlignment(TextAlignmentType.CENTER);
headerStyle.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN);
headerStyle.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN);
headerStyle.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN);
headerStyle.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN);
headerDesc.setStyle(headerStyle);
headerQty.setStyle(headerStyle);
headerPrice.setStyle(headerStyle);
headerTotal.setStyle(headerStyle);
// Currency style with borders
Style currencyStyle = workbook.createStyle();
currencyStyle.setCustom("\"$\"#,##0.00");
currencyStyle.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN);
currencyStyle.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN);
currencyStyle.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN);
currencyStyle.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN);
// Plain border style for description/quantity cells
Style borderStyle = workbook.createStyle();
borderStyle.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN);
borderStyle.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN);
borderStyle.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN);
borderStyle.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN);
// Line items rows
Object[][] lineItems = new Object[][] {
    {"Product A - Widget", 2, 50.00},
    {"Product B - Gadget", 3, 75.00},
    {"Product C - Service", 1, 100.00}
};
for (int i = 0; i < lineItems.length; i++)
{
    int row = 20 + i;
    Cell descCell = worksheet.getCells().get(row, 1);
    Cell qtyCell = worksheet.getCells().get(row, 2);
    Cell priceCell = worksheet.getCells().get(row, 3);
    Cell totalCell = worksheet.getCells().get(row, 4);
    descCell.putValue(lineItems[i][0]);
    qtyCell.putValue(lineItems[i][1]);
    priceCell.putValue(lineItems[i][2]);
    totalCell.setFormula("C" + row + "*D" + row);
    descCell.setStyle(borderStyle);
    qtyCell.setStyle(borderStyle);
    priceCell.setStyle(currencyStyle);
    totalCell.setStyle(currencyStyle);
}
// Subtotal, tax, grand total
worksheet.getCells().get("B24").putValue("Subtotal:");
Cell subtotalCell = worksheet.getCells().get("E24");
subtotalCell.setFormula("SUM(E20:E22)");
worksheet.getCells().get("B25").putValue("Tax (10%):");
Cell taxCell = worksheet.getCells().get("E25");
taxCell.setFormula("E24*0.1");
worksheet.getCells().get("B26").putValue("Grand Total:");
Cell grandTotalCell = worksheet.getCells().get("E26");
grandTotalCell.setFormula("E24+E25");
// Bold + currency style for total values
Style totalStyle = workbook.createStyle();
totalStyle.getFont().setBold(true);
totalStyle.setCustom("\"$\"#,##0.00");
subtotalCell.setStyle(totalStyle);
taxCell.setStyle(totalStyle);
grandTotalCell.setStyle(totalStyle);
// Bold style for total labels
Style boldStyle = workbook.createStyle();
boldStyle.getFont().setBold(true);
worksheet.getCells().get("B24").setStyle(boldStyle);
worksheet.getCells().get("B25").setStyle(boldStyle);
worksheet.getCells().get("B26").setStyle(boldStyle);
// Save the workbook as an OFD file
workbook.save(dataDir + "Invoice.ofd", SaveFormat.Ofd);
```

## **Conversione di un file Excel esistente in OFD**
Aspose.Cells può anche caricare una cartella di lavoro Excel esistente dal disco ed esportarla direttamente in formato OFD. Ciò è utile per pipeline di conversione in batch, flussi di lavoro di archiviazione e scenari in cui la cartella di lavoro sorgente è stata prodotta da un altro strumento e deve solo essere riemessa come artefatto a layout fisso. L'esempio seguente carica una cartella di lavoro `.xlsx` esistente, legge i dati dalle sue celle, applica le regolazioni opzionali di impostazione della pagina e salva il risultato come documento OFD.

```java
import com.aspose.cells.*;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
String dataDir = "C:\\Examples\\";
// Open an existing Excel workbook from disk
Workbook workbook = new Workbook(dataDir + "SampleBook.xlsx");
// (1) Read and display values from selected cells to confirm the file was loaded
Worksheet firstSheet = workbook.getWorksheets().get(0);
System.out.println("First sheet name: " + firstSheet.getName());
System.out.println("Cell A1: " + firstSheet.getCells().get("A1").getStringValue());
System.out.println("Cell B1: " + firstSheet.getCells().get("B1").getStringValue());
System.out.println("Cell C1: " + firstSheet.getCells().get("C1").getStringValue());
// (2) Iterate over the Worksheets collection to enumerate available sheets
System.out.println("\nAvailable worksheets:");
for (int i = 0; i < workbook.getWorksheets().getCount(); i++)
{
    Worksheet ws = workbook.getWorksheets().get(i);
    System.out.println("  [" + i + "] " + ws.getName());
}
// (3) Optionally update a timestamp cell to reflect the conversion
String timestamp1 = LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));
firstSheet.getCells().get("A1").putValue("Converted on: " + timestamp1);
// Append a summary header row at the top of the data block
firstSheet.getCells().insertRow(0);
firstSheet.getCells().get("A1").putValue("Conversion Summary");
String timestamp2 = LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));
firstSheet.getCells().get("A2").putValue("Generated: " + timestamp2);
// (4) Configure PageSetup properties on the worksheet
PageSetup pageSetup = firstSheet.getPageSetup();
pageSetup.setOrientation(PageOrientationType.LANDSCAPE);
pageSetup.setPaperSize(PaperSizeType.PAPER_A_4);
pageSetup.setFitToPagesTall(1);
pageSetup.setFitToPagesWide(1);
// (5) Optionally set the print area for the OFD output
int lastRow = firstSheet.getCells().getMaxDataRow();
int lastCol = firstSheet.getCells().getMaxDataColumn();
String lastColLetter = CellsHelper.columnIndexToName(lastCol);
String printArea = "A1:" + lastColLetter + (lastRow + 1);
firstSheet.getPageSetup().setPrintArea(printArea);
System.out.println("\nPrint area set to: " + printArea);
// (6) Save the workbook as an OFD file
workbook.save(dataDir + "SampleBook.ofd", SaveFormat.Ofd);
System.out.println("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd");
```

## **Articoli correlati**
- [Divisione di file Excel in più file](/cells/it/java/splitting-excel-files-into-multiple-files/)
- [Inserimento di un'immagine in una cella](/cells/it/java/inserting-an-image-into-a-cell/)
- [Lettura e scrittura di file DBF](/cells/it/java/dbf/)
- [Conversione di sparkline in immagine e HTML in Aspose.Cells for Java](/cells/it/java/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="java" >}}
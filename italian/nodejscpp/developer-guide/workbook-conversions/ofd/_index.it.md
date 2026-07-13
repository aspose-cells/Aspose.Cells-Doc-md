---
title: Conversione di Excel nel formato OFD
linktitle: Conversione di Excel nel formato OFD
description: Aspose.Cells è una libreria Node.js per lavorare con file di fogli di calcolo che supporta la conversione di cartelle di lavoro Excel nel formato OFD (Open Fixed-layout Document). Questo articolo mostra come creare contenuto Excel ed esportarlo come OFD, nonché come convertire file Excel esistenti in OFD utilizzando Aspose.Cells.
keywords: Aspose.Cells, libreria Node.js, foglio di calcolo, Excel in OFD, conversione OFD, SaveFormat.Ofd, documento a layout fisso, esportazione cartella di lavoro
type: docs
weight: 195
url: /it/nodejs-cpp/converting-excel-to-ofd-format/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells supporta la conversione diretta di cartelle di lavoro Excel nel formato OFD (Open Fixed-layout Document) utilizzando il valore di enumerazione `SaveFormat.Ofd`. Il documento OFD risultante preserva il layout visibile, il contenuto, le celle unite, la larghezza delle colonne, l'altezza delle righe, i caratteri, i colori, i bordi e i formati numerici della cartella di lavoro. Ciò rende Aspose.Cells adatto ad archiviazione, stampa, depositi normativi e flussi di lavoro di invio alle autorità governative che richiedono un output a layout fisso.

{{% /alert %}}
## **Introduzione**
OFD (Open Fixed-layout Document) è uno standard nazionale cinese (GB/T 33190-2016) per la rappresentazione di documenti digitali in un layout fisso basato su pagine. Svolge un ruolo simile a PDF per i casi d'uso in cui l'aspetto visivo del documento sorgente deve essere preservato esattamente come è stato creato. OFD è ampiamente adottato per le presentazioni governative, i depositi normativi, le fatture elettroniche e l'archiviazione a lungo termine nella Repubblica Popolare Cinese.

La conversione delle cartelle di lavoro Excel in OFD è un requisito comune negli scenari in cui il contenuto del foglio di calcolo deve essere distribuito come artefatto di sola lettura con layout bloccato anziché come foglio di calcolo modificabile. Esempi includono l'invio di una fattura finalizzata a un cliente, l'archiviazione di un rapporto finanziario trimestrale o la presentazione di un foglio di calcolo del budget a un'autorità di regolamentazione. Aspose.Cells soddisfa questo requisito tramite il valore di enumerazione `SaveFormat.Ofd`, che scrive la cartella di lavoro direttamente in OFD senza richiedere un passaggio intermedio di conversione. L'output OFD preserva i valori delle celle, gli intervalli uniti, i caratteri, i colori, i bordi, i formati numerici e le opzioni di impostazione della pagina configurate sulla cartella di lavoro.

{{% alert color="primary" %}}

L'output OFD generato da Aspose.Cells preserva il layout visibile della cartella di lavoro sorgente, inclusi il contenuto delle celle, le celle unite, la larghezza delle colonne e l'altezza delle righe. Anche la formattazione delle celle come caratteri, colori, bordi, allineamento e formati numerici viene riprodotta nell'output a layout fisso. Le opzioni di impostazione della pagina configurate sul foglio di lavoro, come formato carta, orientamento e area di stampa, influenzano il layout del documento OFD risultante.

{{% /alert %}}
## **Creazione di una cartella di lavoro Excel e salvataggio come OFD**
Aspose.Cells consente di creare una cartella di lavoro a livello di codice, popolarla con dati e quindi salvarla direttamente nel formato OFD utilizzando l'enumerazione `SaveFormat.Ofd`. L'esempio seguente crea una fattura da zero. Aggiunge il logo dell'azienda, le informazioni di intestazione, una sezione di fatturazione, le voci della fattura e i totali calcolati, quindi esporta la cartella di lavoro in un documento OFD.
### **Creazione di una fattura con un logo**
L'esempio costruisce un foglio di lavoro della fattura inserendo un'immagine del logo nell'area in alto a sinistra, popolando il nome dell'azienda e i dettagli di contatto, aggiungendo un titolo "INVOICE" (FATTURA) su celle unite, registrando il numero e la data della fattura, elencando il cliente fatturato, costruendo una tabella delle voci con colonne descrizione, quantità, prezzo unitario e totale, e calcolando il subtotale, l'imposta e il totale complessivo utilizzando formule di cella. La formattazione come intestazioni in grassetto, formato valuta per i prezzi, bordi e larghezza delle colonne viene applicata utilizzando gli oggetti `Style` e `Font`. Infine, la cartella di lavoro viene salvata con l'estensione `.ofd` utilizzando `SaveFormat.Ofd`.

```javascript
let dataDir = "C:\\Temp\\";

// Crea una nuova cartella di lavoro
let workbook = new AsposeCells.Workbook();

// Ottieni il primo foglio di lavoro
let worksheet = workbook.getWorksheets().get(0);

// Imposta la larghezza delle colonne
worksheet.getCells().setColumnWidth(0, 5);
worksheet.getCells().setColumnWidth(1, 35);
worksheet.getCells().setColumnWidth(2, 12);
worksheet.getCells().setColumnWidth(3, 15);
worksheet.getCells().setColumnWidth(4, 15);
worksheet.getCells().setColumnWidth(5, 5);

// Inserisci il logo dell'azienda
worksheet.getPictures().add(1, 1, dataDir + "logo.png");

// Nome dell'azienda e dettagli di contatto
worksheet.getCells().get("B3").putValue("Acme Corporation");
worksheet.getCells().get("B4").putValue("123 Business Street");
worksheet.getCells().get("B5").putValue("City, State 12345");
worksheet.getCells().get("B6").putValue("Phone: (555) 123-4567");

// Titolo FATTURA - unisci celle
worksheet.getCells().merge(7, 1, 2, 4);
let titleCell = worksheet.getCells().get("B8");
titleCell.putValue("INVOICE");

let titleStyle = workbook.createStyle();
titleStyle.getFont().setIsBold(true);
titleStyle.getFont().setSize(20);
titleStyle.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);
titleCell.setStyle(titleStyle);

// Numero fattura e data
worksheet.getCells().get("B11").putValue("Invoice Number:");
worksheet.getCells().get("C11").putValue("INV-2024-001");
worksheet.getCells().get("B12").putValue("Date:");
let now = new Date();
let dateStr = `${now.getFullYear()}-${String(now.getMonth() + 1).padStart(2, '0')}-${String(now.getDate()).padStart(2, '0')}`;
worksheet.getCells().get("C12").putValue(dateStr);

// Sezione intestazione fattura
worksheet.getCells().get("B14").putValue("Bill To:");
worksheet.getCells().get("B15").putValue("Client Name");
worksheet.getCells().get("B16").putValue("Client Address");
worksheet.getCells().get("B17").putValue("Client City, State");

// Intestazione voci
let headerDesc = worksheet.getCells().get("B19");
let headerQty = worksheet.getCells().get("C19");
let headerPrice = worksheet.getCells().get("D19");
let headerTotal = worksheet.getCells().get("E19");

headerDesc.putValue("Description");
headerQty.putValue("Quantity");
headerPrice.putValue("Unit Price");
headerTotal.putValue("Total");

let headerStyle = workbook.createStyle();
headerStyle.getFont().setIsBold(true);
headerStyle.getFont().setColor(AsposeCells.Color.White);
headerStyle.setBackgroundColor(AsposeCells.Color.Navy);
headerStyle.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);
headerStyle.getBorders().getByBorderType(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
headerStyle.getBorders().getByBorderType(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
headerStyle.getBorders().getByBorderType(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
headerStyle.getBorders().getByBorderType(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Thin);

headerDesc.setStyle(headerStyle);
headerQty.setStyle(headerStyle);
headerPrice.setStyle(headerStyle);
headerTotal.setStyle(headerStyle);

// Stile valuta con bordi
let currencyStyle = workbook.createStyle();
currencyStyle.setCustom("\"$\"#,##0.00");
currencyStyle.getBorders().getByBorderType(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
currencyStyle.getBorders().getByBorderType(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
currencyStyle.getBorders().getByBorderType(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
currencyStyle.getBorders().getByBorderType(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Thin);

// Stile bordo semplice per celle descrizione/quantità
let borderStyle = workbook.createStyle();
borderStyle.getBorders().getByBorderType(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
borderStyle.getBorders().getByBorderType(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
borderStyle.getBorders().getByBorderType(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
borderStyle.getBorders().getByBorderType(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Thin);

// Righe voci
let lineItems = [
    ["Product A - Widget", 2, 50.00],
    ["Product B - Gadget", 3, 75.00],
    ["Product C - Service", 1, 100.00]
];

for (let i = 0; i < lineItems.length; i++) {
    let row = 20 + i;
    let descCell = worksheet.getCells().get(row, 1);
    let qtyCell = worksheet.getCells().get(row, 2);
    let priceCell = worksheet.getCells().get(row, 3);
    let totalCell = worksheet.getCells().get(row, 4);

    descCell.putValue(lineItems[i][0]);
    qtyCell.putValue(lineItems[i][1]);
    priceCell.putValue(lineItems[i][2]);
    totalCell.setFormula("C" + row + "*D" + row);

    descCell.setStyle(borderStyle);
    qtyCell.setStyle(borderStyle);
    priceCell.setStyle(currencyStyle);
    totalCell.setStyle(currencyStyle);
}

// Subtotale, tasse, totale generale
worksheet.getCells().get("B24").putValue("Subtotal:");
let subtotalCell = worksheet.getCells().get("E24");
subtotalCell.setFormula("SUM(E20:E22)");

worksheet.getCells().get("B25").putValue("Tax (10%):");
let taxCell = worksheet.getCells().get("E25");
taxCell.setFormula("E24*0.1");

worksheet.getCells().get("B26").putValue("Grand Total:");
let grandTotalCell = worksheet.getCells().get("E26");
grandTotalCell.setFormula("E24+E25");

// Stile grassetto + valuta per i valori totali
let totalStyle = workbook.createStyle();
totalStyle.getFont().setIsBold(true);
totalStyle.setCustom("\"$\"#,##0.00");

subtotalCell.setStyle(totalStyle);
taxCell.setStyle(totalStyle);
grandTotalCell.setStyle(totalStyle);

// Stile grassetto per le etichette dei totali
let boldStyle = workbook.createStyle();
boldStyle.getFont().setIsBold(true);

worksheet.getCells().get("B24").setStyle(boldStyle);
worksheet.getCells().get("B25").setStyle(boldStyle);
worksheet.getCells().get("B26").setStyle(boldStyle);

// Salva la cartella di lavoro come file OFD
workbook.save(dataDir + "Invoice.ofd", AsposeCells.SaveFormat.Ofd);
```
## **Conversione di un file Excel esistente in OFD**
Aspose.Cells può anche caricare una cartella di lavoro Excel esistente dal disco ed esportarla direttamente nel formato OFD. Ciò è utile per pipeline di conversione in batch, flussi di lavoro di archiviazione e scenari in cui la cartella di lavoro sorgente è stata prodotta da un altro strumento e deve essere semplicemente riemessa come artefatto a layout fisso. L'esempio seguente carica una cartella di lavoro `.xlsx` esistente, legge i dati dalle sue celle, applica eventuali regolazioni di impostazione della pagina e salva il risultato come documento OFD.

```javascript
let workbook = new AsposeCells.Workbook(dataDir + "SampleBook.xlsx");

// (1) Legge e visualizza i valori dalle celle selezionate per confermare che il file è stato caricato
let firstSheet = workbook.getWorksheets().get(0);
console.log("First sheet name: " + firstSheet.getName());
console.log("Cell A1: " + firstSheet.getCells().get("A1").getStringValue());
console.log("Cell B1: " + firstSheet.getCells().get("B1").getStringValue());
console.log("Cell C1: " + firstSheet.getCells().get("C1").getStringValue());

// (2) Itera sulla raccolta Worksheets per elencare i fogli disponibili
console.log("\nAvailable worksheets:");
for (let i = 0; i < workbook.getWorksheets().getCount(); i++)
{
    let ws = workbook.getWorksheets().get(i);
    console.log("  [" + i + "] " + ws.getName());
}

// (3) Opzionalmente aggiorna una cella con un timestamp per riflettere la conversione
firstSheet.getCells().get("A1").putValue("Converted on: " + formatDate(new Date()));

// Aggiunge una riga di intestazione di riepilogo all'inizio del blocco di dati
firstSheet.getCells().insertRow(0);
firstSheet.getCells().get("A1").putValue("Conversion Summary");
firstSheet.getCells().get("A2").putValue("Generated: " + formatDate(new Date()));

// (4) Configura le proprietà di PageSetup sul foglio di lavoro
let pageSetup = firstSheet.getPageSetup();
pageSetup.setOrientation(AsposeCells.PageOrientationType.Landscape);
pageSetup.setPaperSize(AsposeCells.PaperSizeType.PaperA4);
pageSetup.setFitToPagesTall(1);
pageSetup.setFitToPagesWide(1);

// (5) Opzionalmente imposta l'area di stampa per l'output OFD
let lastRow = firstSheet.getCells().getMaxDataRow();
let lastCol = firstSheet.getCells().getMaxDataColumn();
let lastColLetter = AsposeCells.CellsHelper.columnIndexToName(lastCol);
let printArea = "A1:" + lastColLetter + (lastRow + 1);
firstSheet.getPageSetup().setPrintArea(printArea);
console.log("\nPrint area set to: " + printArea);

// (6) Salva la cartella di lavoro come file OFD
workbook.save(dataDir + "SampleBook.ofd", AsposeCells.SaveFormat.Ofd);
console.log("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd");
```

## **Articoli correlati**
- [Divisione di file Excel in più file](/cells/it/nodejs-cpp/splitting-excel-files-into-multiple-files/)
- [Inserimento di un'immagine in una cella](/cells/it/nodejs-cpp/inserting-an-image-into-a-cell/)
- [Lettura e scrittura di file DBF](/cells/it/nodejs-cpp/dbf/)
- [Conversione di Sparkline in immagine e HTML in Aspose.Cells for Node.js via C++](/cells/it/nodejs-cpp/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="javascript" >}}
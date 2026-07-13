---
title: Conversione di Excel in formato OFD
linktitle: Conversione di Excel in formato OFD
description: Aspose.Cells for Node.js via Java è una libreria per fogli di calcolo che supporta la conversione di cartelle di lavoro Excel in formato OFD (Open Fixed-layout Document). Questo articolo dimostra come creare contenuto Excel ed esportarlo come OFD, nonché come convertire file Excel esistenti in OFD utilizzando Aspose.Cells.
keywords: Aspose.Cells, libreria Node.js via Java, foglio di calcolo, Excel in OFD, conversione OFD, SaveFormat.Ofd, documento a layout fisso, esportazione cartella di lavoro
type: docs
weight: 195
url: /it/nodejs-java/converting-excel-to-ofd-format/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells supporta la conversione diretta di cartelle di lavoro Excel in formato OFD (Open Fixed-layout Document) utilizzando il valore di enumerazione `SaveFormat.Ofd`. Il documento OFD risultante preserva il layout visibile, il contenuto, le celle unite, le larghezze delle colonne, le altezze delle righe, i caratteri, i colori, i bordi e i formati numerici della cartella di lavoro. Questo rende Aspose.Cells adatto per flussi di lavoro di archiviazione, stampa, deposito normativo e presentazione governativa che richiedono un output a layout fisso.

{{% /alert %}}
## **Introduzione**
OFD (Open Fixed-layout Document) è uno standard nazionale cinese (GB/T 33190-2016) per la rappresentazione di documenti digitali in un layout fisso basato su pagine. Svolge un ruolo simile al PDF per casi d'uso in cui l'aspetto visivo del documento sorgente deve essere preservato esattamente come è stato creato. OFD è ampiamente adottato per le presentazioni governative, i depositi normativi, le fatture elettroniche e l'archiviazione a lungo termine nella Repubblica Popolare Cinese.

La conversione di cartelle di lavoro Excel in OFD è un requisito comune in scenari in cui il contenuto del foglio di calcolo deve essere distribuito come un artefatto di sola lettura con layout bloccato anziché come un foglio di calcolo modificabile. Gli esempi includono l'invio di una fattura finalizzata a un cliente, l'archiviazione di un rapporto finanziario trimestrale o la presentazione di un foglio di calcolo del budget a un'autorità di regolamentazione. Aspose.Cells soddisfa questo requisito attraverso il valore di enumerazione `SaveFormat.Ofd`, che scrive la cartella di lavoro direttamente in OFD senza richiedere un passaggio di conversione intermedio. L'output OFD preserva i valori delle celle, gli intervalli uniti, i caratteri, i colori, i bordi, i formati numerici e le opzioni di impostazione della pagina configurate sulla cartella di lavoro.

{{% alert color="primary" %}}

L'output OFD generato da Aspose.Cells preserva il layout visibile della cartella di lavoro sorgente, inclusi il contenuto delle celle, le celle unite, le larghezze delle colonne e le altezze delle righe. Anche la formattazione delle celle come caratteri, colori, bordi, allineamento e formati numerici viene riprodotta nell'output a layout fisso. Le opzioni di impostazione della pagina configurate sul foglio di lavoro, come dimensione della carta, orientamento e area di stampa, influenzano il layout del documento OFD risultante.

{{% /alert %}}
## **Creazione di una cartella di lavoro Excel e salvataggio come OFD**
Aspose.Cells consente di creare una cartella di lavoro a livello di codice, popolarla con dati e quindi salvarla direttamente in formato OFD utilizzando l'enumerazione `SaveFormat.Ofd`. L'esempio seguente crea una fattura da zero. Aggiunge un logo aziendale, informazioni di intestazione, una sezione di fatturazione, voci e totali calcolati, quindi esporta la cartella di lavoro in un documento OFD.
### **Creazione di una fattura con un logo**
L'esempio costruisce un foglio di lavoro fattura inserendo un'immagine del logo nell'area in alto a sinistra, popolando il nome dell'azienda e i dettagli di contatto, aggiungendo un titolo "INVOICE" (FATTURA) su celle unite, registrando il numero e la data della fattura, elencando il cliente fatturato, costruendo una tabella di voci con colonne descrizione, quantità, prezzo unitario e totale, e calcolando il subtotale, l'imposta e il totale complessivo utilizzando formule di cella. La formattazione come intestazioni in grassetto, formato valuta per i prezzi, bordi e larghezze delle colonne viene applicata utilizzando gli oggetti `Style` e `Font`. Infine, la cartella di lavoro viene salvata con l'estensione `.ofd` utilizzando `SaveFormat.Ofd`.

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
titleStyle.setHorizontalAlignment(AsposeCells.TextAlignmentType.CENTER);
titleCell.setStyle(titleStyle);

// Numero e data fattura
worksheet.getCells().get("B11").putValue("Invoice Number:");
worksheet.getCells().get("C11").putValue("INV-2024-001");
worksheet.getCells().get("B12").putValue("Date:");
worksheet.getCells().get("C12").putValue(new Date().toISOString().slice(0, 10));

// Sezione "Fatturare a"
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
headerStyle.getFont().setColor(AsposeCells.Color.getWhite());
headerStyle.setBackgroundColor(AsposeCells.Color.getNavy());
headerStyle.setHorizontalAlignment(AsposeCells.TextAlignmentType.CENTER);
headerStyle.getBorders().get(AsposeCells.BorderType.TOP_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
headerStyle.getBorders().get(AsposeCells.BorderType.BOTTOM_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
headerStyle.getBorders().get(AsposeCells.BorderType.LEFT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
headerStyle.getBorders().get(AsposeCells.BorderType.RIGHT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);

headerDesc.setStyle(headerStyle);
headerQty.setStyle(headerStyle);
headerPrice.setStyle(headerStyle);
headerTotal.setStyle(headerStyle);

// Stile valuta con bordi
let currencyStyle = workbook.createStyle();
currencyStyle.setCustom("\"$\"#,##0.00");
currencyStyle.getBorders().get(AsposeCells.BorderType.TOP_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
currencyStyle.getBorders().get(AsposeCells.BorderType.BOTTOM_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
currencyStyle.getBorders().get(AsposeCells.BorderType.LEFT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
currencyStyle.getBorders().get(AsposeCells.BorderType.RIGHT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);

// Stile bordo semplice per celle descrizione/quantità
let borderStyle = workbook.createStyle();
borderStyle.getBorders().get(AsposeCells.BorderType.TOP_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
borderStyle.getBorders().get(AsposeCells.BorderType.BOTTOM_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
borderStyle.getBorders().get(AsposeCells.BorderType.LEFT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
borderStyle.getBorders().get(AsposeCells.BorderType.RIGHT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);

// Righe voci
let lineItems = [
    ["Product A - Widget", 2, 50.00],
    ["Product B - Gadget", 3, 75.00],
    ["Product C - Service", 1, 100.00]
];

for (let i = 0; i < lineItems.length; i++)
{
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

// Subtotale, tasse, totale complessivo
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

// Stile grassetto per etichette totali
let boldStyle = workbook.createStyle();
boldStyle.getFont().setIsBold(true);

worksheet.getCells().get("B24").setStyle(boldStyle);
worksheet.getCells().get("B25").setStyle(boldStyle);
worksheet.getCells().get("B26").setStyle(boldStyle);

// Salva la cartella di lavoro come file OFD
workbook.save(dataDir + "Invoice.ofd", AsposeCells.SaveFormat.Ofd);
```
## **Conversione di un file Excel esistente in OFD**
Aspose.Cells può anche caricare una cartella di lavoro Excel esistente dal disco ed esportarla direttamente in formato OFD. Ciò è utile per pipeline di conversione in batch, flussi di lavoro di archiviazione e scenari in cui la cartella di lavoro sorgente è stata prodotta da un altro strumento e deve solo essere riemessa come artefatto a layout fisso. L'esempio seguente carica una cartella di lavoro `.xlsx` esistente, legge i dati dalle sue celle, applica regolazioni facoltative di impostazione della pagina e salva il risultato come documento OFD.

```javascript
const AsposeCells = require("aspose.cells");

const dataDir = "C:\\Examples\\";

// Apre una cartella di lavoro Excel esistente dal disco
const workbook = new AsposeCells.Workbook(dataDir + "SampleBook.xlsx");

// (1) Legge e visualizza i valori dalle celle selezionate per confermare che il file è stato caricato
const firstSheet = workbook.getWorksheets().get(0);
console.log("First sheet name: " + firstSheet.getName());
console.log("Cell A1: " + firstSheet.getCells().get("A1").getStringValue());
console.log("Cell B1: " + firstSheet.getCells().get("B1").getStringValue());
console.log("Cell C1: " + firstSheet.getCells().get("C1").getStringValue());

// (2) Itera sulla raccolta Worksheets per elencare i fogli disponibili
console.log("\nAvailable worksheets:");
for (let i = 0; i < workbook.getWorksheets().getCount(); i++)
{
    const ws = workbook.getWorksheets().get(i);
    console.log("  [" + i + "] " + ws.getName());
}

// (3) Facoltativamente aggiorna una cella con il timestamp per riflettere la conversione
firstSheet.getCells().get("A1").putValue("Converted on: " + formatDate(new Date()));

// Aggiunge una riga di intestazione di riepilogo all'inizio del blocco di dati
firstSheet.getCells().insertRow(0);
firstSheet.getCells().get("A1").putValue("Conversion Summary");
firstSheet.getCells().get("A2").putValue("Generated: " + formatDate(new Date()));

// (4) Configura le proprietà PageSetup sul foglio di lavoro
const pageSetup = firstSheet.getPageSetup();
pageSetup.setOrientation(AsposeCells.PageOrientationType.Landscape);
pageSetup.setPaperSize(AsposeCells.PaperSizeType.PaperA4);
pageSetup.setFitToPagesTall(1);
pageSetup.setFitToPagesWide(1);

// (5) Facoltativamente imposta l'area di stampa per l'output OFD
const lastRow = firstSheet.getCells().getMaxDataRow();
const lastCol = firstSheet.getCells().getMaxDataColumn();
const lastColLetter = AsposeCells.CellsHelper.columnIndexToName(lastCol);
const printArea = "A1:" + lastColLetter + (lastRow + 1);
firstSheet.getPageSetup().setPrintArea(printArea);
console.log("\nPrint area set to: " + printArea);

// (6) Salva la cartella di lavoro come file OFD
workbook.save(dataDir + "SampleBook.ofd", AsposeCells.SaveFormat.Ofd);
console.log("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd");

function formatDate(date) {
    const pad = (n) => n.toString().padStart(2, '0');
    return date.getFullYear() + "-" + pad(date.getMonth() + 1) + "-" + pad(date.getDate()) + " " + pad(date.getHours()) + ":" + pad(date.getMinutes()) + ":" + pad(date.getSeconds());
}
```

## **Articoli correlati**
- [Divisione di file Excel in più file](/cells/it/nodejs-java/splitting-excel-files-into-multiple-files/)
- [Inserimento di un'immagine in una cella](/cells/it/nodejs-java/inserting-an-image-into-a-cell/)
- [Lettura e scrittura di file DBF](/cells/it/nodejs-java/dbf/)
- [Conversione di Sparkline in immagine e HTML in Aspose.Cells for Node.js via Java](/cells/it/nodejs-java/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="javascript" >}}
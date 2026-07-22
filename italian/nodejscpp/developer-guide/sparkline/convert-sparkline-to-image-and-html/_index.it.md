---
title: Convertire Sparkline in Immagine e HTML in Aspose.Cells for Node.js via C++
linktitle: Convert Sparkline to Image and HTML
description: Scopri come eseguire il rendering delle sparkline Aspose.Cells in immagini autonome per l'incorporamento nelle celle ed esportare fogli di lavoro ricchi di sparkline in HTML utilizzando HtmlSaveOptions.
keywords: Aspose.Cells, Node.js via C++, sparkline, Sparkline.toImage, cell.embeddedImage, HtmlSaveOptions, rendering sparkline, convertire sparkline in immagine, esportare sparkline in HTML
type: docs
weight: 120
url: /it/nodejs-cpp/convert-sparkline-to-image-and-html/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Le sparkline sono grafici in miniatura inseriti all'interno delle celle di un foglio di lavoro. Aspose.Cells consente di estrarre ogni sparkline come immagine autonoma (da incorporare in un'altra cella o in un report esterno) e di esportare l'intero foglio di lavoro ricco di sparkline in HTML per la distribuzione basata su browser. La proprietà `cell.embeddedImage` utilizzata in questo articolo è disponibile in **Aspose.Cells 26.5 e versioni successive**.
{{% /alert %}}

## **Introduzione**

Le sparkline sono un modo compatto per visualizzare i trend direttamente all'interno di un foglio di lavoro. Mentre gli utenti di Excel le vedono sul posto, molti scenari reali richiedono che una sparkline lasci la cella — ad esempio, per essere incorporata in una cella diversa come immagine statica, allegata a un'email automatizzata o renderizzata come parte di un report HTML pubblicato sul web.

Aspose.Cells supporta entrambe queste operazioni. Il metodo `Sparkline.toImage` esegue il rendering di una singola sparkline in un flusso, e i byte risultanti possono essere assegnati a `cell.embeddedImage` in modo che l'immagine venga memorizzata all'interno di una singola cella della cartella di lavoro. Separatamente, `HtmlSaveOptions` consente di convertire l'intera cartella di lavoro — comprese le sparkline — in un file HTML autonomo. Questo articolo illustra entrambi i flussi di lavoro end to end.

## **Flusso di lavoro 1 — Eseguire il rendering delle sparkline in immagini e incorporarle nelle celle**

In questo flusso di lavoro verrà creato un foglio di lavoro che contiene un piccolo intervallo di valori di origine, verranno collegati tre diversi gruppi di sparkline (Linea, Colonna e In pila/Vittoria-Perdita) a tale intervallo, verrà eseguito il rendering di ciascun gruppo come PNG e tali byte PNG verranno scritti nelle celle adiacenti come immagini incorporate. Il risultato finale è un singolo file `.xlsx` che contiene sia le sparkline attive sia le loro controparti immagine renderizzate.

### **Istruzioni passo-passo**

1. Definire una directory di lavoro e assicurarsi che esista su disco.
2. Creare una nuova `Workbook` e ottenere un riferimento al primo `Worksheet`.
3. Popolare le celle da `A1` a `E1` con cinque valori numerici di esempio (ad esempio, vendite giornaliere o letture di temperatura).
4. Aggiungere tre oggetti `SparklineGroup` al foglio di lavoro chiamando `worksheet.sparklineGroups.add(...)`:
   - Un gruppo `SparklineType.Line` ancorato a `F1`, con intervallo di dati `A1:E1`.
   - Un gruppo `SparklineType.Column` ancorato a `G1`, con intervallo di dati `A1:E1`.
   - Un gruppo `SparklineType.Stacked` (vittoria/perdita) ancorato a `H1`, con intervallo di dati `A1:E1`.
5. Creare un'istanza di `ImageOrPrintOptions` e impostare il suo `ImageType` su `ImageType.Png` in modo che ogni sparkline venga renderizzata come PNG trasparente.
6. Per ciascuno dei tre gruppi, eseguire il rendering della sua singola sparkline utilizzando `group.sparklines[0].toImage(memoryStream, imageOrPrintOptions)`, convertire il flusso in un `Buffer` (o `Uint8Array`), e assegnare i byte rispettivamente a `worksheet.cells["F2"].embeddedImage`, `worksheet.cells["G2"].embeddedImage`, e `worksheet.cells["H2"].embeddedImage`.
7. Salvare la cartella di lavoro come `output_with_sparklines.xlsx`.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Popola dati di esempio nelle celle A1:E1
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// Aggiungi un gruppo di sparkline Line ancorato a F1 (colonna 5, riga 0)
let lineArea = new AsposeCells.CellArea();
lineArea.setStartColumn(5);
lineArea.setEndColumn(5);
lineArea.setStartRow(0);
lineArea.setEndRow(0);
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, lineArea);

// Aggiungi un gruppo di sparkline Column ancorato a G1 (colonna 6, riga 0)
let columnArea = new AsposeCells.CellArea();
columnArea.setStartColumn(6);
columnArea.setEndColumn(6);
columnArea.setStartRow(0);
columnArea.setEndRow(0);
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "A1:E1", false, columnArea);

// Aggiungi un gruppo di sparkline Win/Loss (Stacked) ancorato a H1 (colonna 7, riga 0)
let stackedArea = new AsposeCells.CellArea();
stackedArea.setStartColumn(7);
stackedArea.setEndColumn(7);
stackedArea.setStartRow(0);
stackedArea.setEndRow(0);
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);

// Configura le opzioni immagine per l'output PNG
let imageOptions = new AsposeCells.ImageOrPrintOptions();
imageOptions.setImageType(AsposeCells.ImageType.Png);

// Converti la sparkline Line in immagine e incorporala nella cella F2
let lineSp = worksheet.getSparklineGroups().get(lineIdx).getSparklines().get(0);
let linePath = "line_sparkline.png";
lineSp.toImage(linePath, imageOptions);
worksheet.getCells().get("F2").setEmbeddedImage(fs.readFileSync(linePath));

// Converti la sparkline Column in immagine e incorporala nella cella G2
let columnSp = worksheet.getSparklineGroups().get(columnIdx).getSparklines().get(0);
let columnPath = "column_sparkline.png";
columnSp.toImage(columnPath, imageOptions);
worksheet.getCells().get("G2").setEmbeddedImage(fs.readFileSync(columnPath));

// Converti la sparkline Win/Loss in immagine e incorporala nella cella H2
let stackedSp = worksheet.getSparklineGroups().get(stackedIdx).getSparklines().get(0);
let stackedPath = "stacked_sparkline.png";
stackedSp.toImage(stackedPath, imageOptions);
worksheet.getCells().get("H2").setEmbeddedImage(fs.readFileSync(stackedPath));

// Salva la cartella di lavoro su disco
workbook.save("output_with_sparklines.xlsx");
```

Il codice sopra produce una cartella di lavoro in cui ogni rappresentazione visiva di una sparkline è duplicata in due forme: la sparkline nativa e attiva ancorata alla riga 1, e un'immagine PNG statica incorporata direttamente in una cella adiacente nella riga 2. Poiché le immagini vivono all'interno del file stesso, la cartella di lavoro rimane un singolo artefatto autonomo che può essere inviato via email o archiviato senza rompere i riferimenti alle immagini incorporate. Eseguire il rendering di ciascun gruppo di sparkline come PNG, convertire il flusso in un `Buffer` e assegnare l'array alla proprietà `embeddedImage` della cella di destinazione — l'assegnazione è ciò che rende l'immagine parte del contenuto memorizzato della cella.

{{% alert color="primary" %}}
Poiché ogni gruppo di sparkline è ancorato a una singola cella, è possibile accedervi tramite l'indicizzatore `group.sparklines[0]` invece di enumerare con `forEach`. Ciò mantiene breve il codice di rendering e corrisponde al tipico schema "una sparkline per cella di ancoraggio". La memorizzazione dei byte dell'immagine tramite `cell.embeddedImage` richiede Aspose.Cells 26.5 o versioni successive.
{{% /alert %}}

## **Flusso di lavoro 2 — Esportare il foglio di lavoro con sparkline in HTML**

Una volta che la cartella di lavoro contiene sparkline attive (e opzionalmente controparti immagine incorporate), l'intero foglio di lavoro può essere pubblicato sul web salvandolo come HTML. La classe `HtmlSaveOptions` espone le manopole necessarie per controllare questa esportazione; in questo flusso di lavoro riutilizzerai il file `output_with_sparklines.xlsx` prodotto dal Flusso di lavoro 1 e lo convertirai in un documento HTML pulito e a pagina singola.

### **Istruzioni passo-passo**

1. Assicurarsi che il file `output_with_sparklines.xlsx` prodotto dal Flusso di lavoro 1 sia disponibile su disco nella directory di lavoro.
2. Caricare quel file in una nuova istanza di `Workbook`.
3. Creare un'istanza di `HtmlSaveOptions` e impostare la sua proprietà `exportActiveWorksheetOnly` su `true` in modo che il file HTML risultante contenga solo il foglio di lavoro attivo anziché l'intera cartella di lavoro.
4. Chiamare `workbook.save("sparklines.html", htmlOptions)` per scrivere l'output HTML su disco.

```javascript
let workbook = new AsposeCells.Workbook("output_with_sparklines.xlsx");
let htmlOptions = new AsposeCells.HtmlSaveOptions();
htmlOptions.setExportActiveWorksheetOnly(true);
workbook.save("sparklines.html", htmlOptions);
```

Il codice sopra prende la cartella di lavoro ricca di sparkline dal Flusso di lavoro 1 e la trasforma in un file HTML portatile. Le sparkline vengono preservate come rendering SVG o PNG in linea all'interno dell'HTML generato, a seconda della modalità di esportazione, così gli utenti finali possono visualizzare i trend in qualsiasi browser moderno senza bisogno di Excel installato. Impostando `exportActiveWorksheetOnly` su `true`, si evita di pubblicare accidentalmente fogli nascosti o dati ausiliari — viene esportato solo il foglio di lavoro attualmente visibile all'utente.

{{% alert color="primary" %}}
La classe `HtmlSaveOptions` offre proprietà aggiuntive per la regolazione fine dell'output, come `exportHiddenWorksheet`, `exportImagesAsBase64`, e `encoding`. Regolare queste secondo necessità per il proprio target di distribuzione.
{{% /alert %}}

## **Riepilogo delle API**

I flussi di lavoro sopra si basano su un piccolo insieme di API Aspose.Cells che lavorano insieme.

- `SparklineGroup` e l'accessore di raccolta `worksheet.sparklineGroups` vengono utilizzati per dichiarare il tipo (Linea, Colonna, In pila), l'intervallo di dati e la cella di ancoraggio per ciascun gruppo di sparkline. In questo articolo ogni gruppo è ancorato a una singola cella, quindi il gruppo viene raggiunto tramite `worksheet.sparklineGroups[i]`.
- `Sparkline` e l'indicizzatore `group.sparklines[0]` restituiscono la singola sparkline all'interno di un gruppo. Poiché ogni gruppo nell'esempio contiene esattamente una sparkline, non è richiesto alcun ciclo `forEach`.
- `Sparkline.toImage(Stream, ImageOrPrintOptions)` è il metodo di rendering che scrive un'immagine della sparkline in un `Stream` fornito. Il metodo restituisce `void`; i byte vengono letti dal flusso dopo la chiamata.
- `cell.embeddedImage` è una proprietà `Buffer` (o `Uint8Array`) che memorizza un'immagine all'interno di una singola cella. È disponibile in **Aspose.Cells 26.5 e versioni successive** ed è il modo consigliato per reintegrare una sparkline renderizzata da `toImage` nella stessa cartella di lavoro.
- `htmlSaveOptions.exportActiveWorksheetOnly` (un `bool`) limita l'esportazione HTML al foglio di lavoro attivo. È una delle proprietà più comunemente utilizzate su `HtmlSaveOptions` durante la generazione di report a pagina singola.
- `imageOrPrintOptions.imageType` si trova nel namespace `Aspose.Cells.Drawing` e seleziona il formato immagine (ad esempio, `ImageType.Png`) utilizzato durante il rendering con `toImage` e durante la stampa dei fogli di lavoro in immagini.

## **Articoli correlati**

- [Sparklines in Aspose.Cells for Node.js via C++](/cells/it/nodejs-cpp/sparkline/)
- [Inserimento di un'immagine in una cella](/cells/it/nodejs-cpp/inserting-an-image-into-a-cell/)
- [Rendering di array a cella singola SmartMarker | Aspose.Cells Node.js via C++](/cells/it/nodejs-cpp/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="javascript" >}}
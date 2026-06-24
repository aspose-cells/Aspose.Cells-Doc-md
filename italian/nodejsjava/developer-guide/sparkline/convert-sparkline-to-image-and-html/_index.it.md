---
title: Convertire Sparkline in Immagine e HTML in Aspose.Cells for Node.js via Java
linktitle: Convert Sparkline to Image and HTML
description: Scopri come eseguire il rendering degli sparkline di Aspose.Cells in immagini autonome per l'incorporamento nelle celle ed esportare fogli di lavoro ricchi di sparkline in HTML utilizzando HtmlSaveOptions.
keywords: Aspose.Cells, Node.js via Java, sparkline, Sparkline.toImage, Cell.EmbeddedImage, HtmlSaveOptions, rendering sparkline, convertire sparkline in immagine, esportare sparkline in HTML
type: docs
weight: 120
url: /it/nodejs-java/convert-sparkline-to-image-and-html/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Gli sparkline sono grafici in miniatura posizionati all'interno delle celle di un foglio di lavoro. Aspose.Cells consente di estrarre ogni sparkline come immagine autonoma (da incorporare in un'altra cella o in un report esterno) e anche di esportare l'intero foglio di lavoro ricco di sparkline in HTML per la distribuzione basata su browser. La proprietà `Cell.EmbeddedImage` utilizzata in questo articolo è disponibile in **Aspose.Cells 26.5 e versioni successive**.
{{% /alert %}}

## **Introduzione**

Gli sparkline sono un modo compatto per visualizzare le tendenze direttamente all'interno di un foglio di lavoro. Mentre gli utenti di Excel li vedono sul posto, molti scenari reali richiedono che uno sparkline esca dalla cella, ad esempio per essere incorporato in una cella diversa come immagine statica, allegato a un'email automatizzata o renderizzato come parte di un report HTML pubblicato sul web.

Aspose.Cells supporta entrambe queste operazioni. Il metodo `Sparkline.toImage` esegue il rendering di un singolo sparkline in un flusso, e i byte risultanti possono essere assegnati a `Cell.EmbeddedImage` in modo che l'immagine venga memorizzata all'interno di una singola cella della cartella di lavoro. Separatamente, `HtmlSaveOptions` consente di convertire l'intera cartella di lavoro — sparkline inclusi — in un file HTML autonomo. Questo articolo illustra entrambi i flussi di lavoro end-to-end.

## **Flusso di lavoro 1 — Renderizzare gli Sparkline in Immagini e Incorporarli nelle Celle**

In questo flusso di lavoro costruirai un foglio di lavoro che contiene un piccolo intervallo di valori sorgente, collegherai tre diversi gruppi di sparkline (Linea, Colonna e Stack/Win-Loss) a tale intervallo, renderizzerai ciascun gruppo come PNG e scriverai quei byte PNG nelle celle adiacenti come immagini incorporate. Il risultato finale è un singolo file `.xlsx` che contiene sia gli sparkline attivi sia le loro controparti di immagine renderizzate.

### **Istruzioni passo-passo**

1. Definisci una directory di lavoro e assicurati che esista su disco.
2. Crea una nuova `Workbook` e ottieni un riferimento al primo `Worksheet`.
3. Popola le celle da `A1` a `E1` con cinque valori numerici di esempio (ad esempio, vendite giornaliere o letture di temperatura).
4. Aggiungi tre oggetti `SparklineGroup` al foglio di lavoro chiamando `worksheet.sparklineGroups.add(...)`:
   - Un gruppo `SparklineType.Line` ancorato a `F1`, con intervallo dati `A1:E1`.
   - Un gruppo `SparklineType.Column` ancorato a `G1`, con intervallo dati `A1:E1`.
   - Un gruppo `SparklineType.Stacked` (win/loss) ancorato a `H1`, con intervallo dati `A1:E1`.
5. Crea un'istanza di `ImageOrPrintOptions` e imposta il suo `ImageType` su `ImageType.Png` in modo che ogni sparkline venga renderizzato come PNG trasparente.
6. Per ciascuno dei tre gruppi, renderizza il suo singolo sparkline utilizzando `group.sparklines[0].toImage(outputStream, imageOptions)`, converti il `ByteArrayOutputStream` in un `byte[]` e assegna l'array rispettivamente a `worksheet.cells.get("F2").setEmbeddedImage(...)`, `worksheet.cells.get("G2").setEmbeddedImage(...)` e `worksheet.cells.get("H2").setEmbeddedImage(...)`.
7. Salva la cartella di lavoro come `output_with_sparklines.xlsx`.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Popola i dati di esempio nelle celle A1:E1
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// Aggiungi un gruppo di sparkline a linee ancorato in F1 (colonna 5, riga 0)
let lineArea = new AsposeCells.CellArea();
lineArea.setStartColumn(5);
lineArea.setEndColumn(5);
lineArea.setStartRow(0);
lineArea.setEndRow(0);
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, lineArea);

// Aggiungi un gruppo di sparkline a colonne ancorato in G1 (colonna 6, riga 0)
let columnArea = new AsposeCells.CellArea();
columnArea.setStartColumn(6);
columnArea.setEndColumn(6);
columnArea.setStartRow(0);
columnArea.setEndRow(0);
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "A1:E1", false, columnArea);

// Aggiungi un gruppo di sparkline Win/Loss (In pila) ancorato in H1 (colonna 7, riga 0)
let stackedArea = new AsposeCells.CellArea();
stackedArea.setStartColumn(7);
stackedArea.setEndColumn(7);
stackedArea.setStartRow(0);
stackedArea.setEndRow(0);
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);

// Configura le opzioni dell'immagine per l'output PNG
let imageOptions = new AsposeCells.ImageOrPrintOptions();
imageOptions.setImageType(AsposeCells.ImageType.Png);

// Converti la sparkline a linee in immagine e incorporala nella cella F2
let lineSp = worksheet.getSparklineGroups().get(lineIdx).getSparklines().get(0);
let lineMs = new java.io.ByteArrayOutputStream();
lineSp.toImage(lineMs, imageOptions);
worksheet.getCells().get("F2").setEmbeddedImage(lineMs.toByteArray());

// Converti la sparkline a colonne in immagine e incorporala nella cella G2
let columnSp = worksheet.getSparklineGroups().get(columnIdx).getSparklines().get(0);
let columnMs = new java.io.ByteArrayOutputStream();
columnSp.toImage(columnMs, imageOptions);
worksheet.getCells().get("G2").setEmbeddedImage(columnMs.toByteArray());

// Converti la sparkline Win/Loss in immagine e incorporala nella cella H2
let stackedSp = worksheet.getSparklineGroups().get(stackedIdx).getSparklines().get(0);
let stackedMs = new java.io.ByteArrayOutputStream();
stackedSp.toImage(stackedMs, imageOptions);
worksheet.getCells().get("H2").setEmbeddedImage(stackedMs.toByteArray());

// Salva la cartella di lavoro su disco
workbook.save("output_with_sparklines.xlsx");
```

Il codice sopra produce una cartella di lavoro in cui ogni rappresentazione visiva di uno sparkline è duplicata in due forme: lo sparkline nativo e attivo ancorato alla riga 1, e un'immagine PNG statica incorporata direttamente in una cella adiacente alla riga 2. Poiché le immagini vivono all'interno del file stesso, la cartella di lavoro rimane un singolo artefatto autonomo che può essere inviato via email o archiviato senza rompere i riferimenti alle immagini incorporate. Renderizza ciascun gruppo di sparkline come PNG, converti il `ByteArrayOutputStream` in un `byte[]` e assegna l'array alla proprietà `setEmbeddedImage` della cella di destinazione — l'assegnazione è ciò che rende l'immagine parte del contenuto memorizzato della cella.

{{% alert color="primary" %}}
Poiché ogni gruppo di sparkline è ancorato a una singola cella, puoi accedervi tramite l'indicizzatore `group.sparklines[0]` invece di enumerare con `forEach`. Questo mantiene breve il codice di rendering e corrisponde al tipico schema "uno sparkline per cella di ancoraggio". La memorizzazione dei byte dell'immagine tramite `Cell.EmbeddedImage` richiede Aspose.Cells 26.5 o versioni successive.
{{% /alert %}}

## **Flusso di lavoro 2 — Esportare il Foglio di Lavoro con Sparkline in HTML**

Una volta che la cartella di lavoro contiene sparkline attivi (e opzionalmente le controparti immagine incorporate), l'intero foglio di lavoro può essere pubblicato sul web salvandolo come HTML. La classe `HtmlSaveOptions` espone le manopole necessarie per controllare questa esportazione; in questo flusso di lavoro riutilizzerai il file `output_with_sparklines.xlsx` prodotto dal Flusso di lavoro 1 e lo convertirai in un documento HTML pulito e a pagina singola.

### **Istruzioni passo-passo**

1. Assicurati che il file `output_with_sparklines.xlsx` prodotto dal Flusso di lavoro 1 sia disponibile su disco nella tua directory di lavoro.
2. Carica quel file in una nuova istanza di `Workbook`.
3. Crea un'istanza di `HtmlSaveOptions` e imposta la sua proprietà `ExportActiveWorksheetOnly` su `true` in modo che il file HTML risultante contenga solo il foglio di lavoro attivo anziché l'intera cartella di lavoro.
4. Chiama `workbook.save("sparklines.html", htmlOptions)` per scrivere l'output HTML su disco.

```javascript
let workbook = new AsposeCells.Workbook("output_with_sparklines.xlsx");
let htmlOptions = new AsposeCells.HtmlSaveOptions();
htmlOptions.setExportActiveWorksheetOnly(true);
workbook.save("sparklines.html", htmlOptions);
```

Il codice sopra prende la cartella di lavoro ricca di sparkline dal Flusso di lavoro 1 e la trasforma in un file HTML portatile. Gli sparkline vengono preservati come rendering SVG o PNG inline all'interno dell'HTML generato, a seconda della modalità di esportazione, così gli utenti finali possono visualizzare le tendenze in qualsiasi browser moderno senza bisogno di Excel installato. Impostando `ExportActiveWorksheetOnly` su `true`, eviti di pubblicare accidentalmente fogli nascosti o dati ausiliari — viene esportato solo il foglio di lavoro attualmente visibile all'utente.

{{% alert color="primary" %}}
La classe `HtmlSaveOptions` offre proprietà aggiuntive per la messa a punto dell'output, come `ExportHiddenWorksheet`, `ExportImagesAsBase64` e `Encoding`. Regolale secondo necessità per il tuo target di distribuzione.
{{% /alert %}}

## **Riepilogo delle API**

I flussi di lavoro sopra si basano su un piccolo insieme di API di Aspose.Cells che lavorano insieme.

- `SparklineGroup` e l'accessore di raccolta `worksheet.sparklineGroups` sono utilizzati per dichiarare il tipo (Line, Column, Stacked), l'intervallo dati e la cella di ancoraggio per ciascun gruppo di sparkline. In questo articolo ogni gruppo è ancorato a una singola cella, quindi il gruppo viene raggiunto tramite `worksheet.sparklineGroups[i]`.
- `Sparkline` e l'indicizzatore `group.sparklines[0]` restituiscono il singolo sparkline all'interno di un gruppo. Poiché ogni gruppo nell'esempio contiene esattamente uno sparkline, non è richiesto alcun ciclo `forEach`.
- `Sparkline.toImage(OutputStream, ImageOrPrintOptions)` è il metodo di rendering che scrive un'immagine dello sparkline in un `OutputStream` fornito. Il metodo restituisce `void`; leggi i byte dal flusso dopo la chiamata.
- `Cell.EmbeddedImage` è una proprietà `byte[]` che memorizza un'immagine all'interno di una singola cella. È disponibile in **Aspose.Cells 26.5 e versioni successive** ed è il modo consigliato per reintrodurre uno sparkline renderizzato da `toImage` nella stessa cartella di lavoro.
- `HtmlSaveOptions.ExportActiveWorksheetOnly` (un `boolean`) limita l'esportazione HTML al foglio di lavoro attivo. È una delle proprietà più comunemente utilizzate su `HtmlSaveOptions` quando si generano report a pagina singola.
- `ImageOrPrintOptions.ImageType` si trova nel namespace `com.aspose.cells.drawing` e seleziona il formato immagine (ad esempio, `ImageType.Png`) utilizzato durante il rendering con `toImage` e durante la stampa dei fogli di lavoro in immagini.

## **Articoli correlati**

- [Sparklines in Aspose.Cells for Aspose.Cells for Node.js via Java](/cells/it/nodejs-java/sparkline/)
- [Inserting an Image into a Cell](/cells/it/nodejs-java/inserting-an-image-into-a-cell/)
- [SmartMarker Single Cell Array Rendering | Aspose.Cells for Aspose.Cells for Node.js via Java](/cells/it/nodejs-java/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="javascript" >}}
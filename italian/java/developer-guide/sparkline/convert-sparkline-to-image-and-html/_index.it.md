---
title: Convertire Sparkline in Immagine e HTML in Aspose.Cells for Java
linktitle: Convert Sparkline to Image and HTML
description: Scopri come renderizzare le sparkline di Aspose.Cells in immagini standalone per l'incorporamento nelle celle ed esportare fogli di lavoro ricchi di sparkline in HTML utilizzando HtmlSaveOptions.
keywords: Aspose.Cells, Java, sparkline, Sparkline.toImage, Cell.EmbeddedImage, HtmlSaveOptions, renderizzare sparkline, convertire sparkline in immagine, esportare sparkline in HTML
type: docs
weight: 120
url: /it/java/convert-sparkline-to-image-and-html/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Le sparkline sono grafici in miniatura posizionati all'interno delle celle del foglio di lavoro. Aspose.Cells consente di estrarre ogni sparkline come immagine standalone (per l'incorporamento in un'altra cella o in un report esterno) e anche di esportare l'intero foglio di lavoro ricco di sparkline in HTML per la distribuzione basata su browser. La proprietà `Cell.EmbeddedImage` utilizzata in questo articolo è disponibile in **Aspose.Cells 26.5 e versioni successive**.
{{% /alert %}}

## **Introduzione**

Le sparkline sono un modo compatto per visualizzare i trend direttamente all'interno di un foglio di lavoro. Mentre gli utenti di Excel le vedono in posizione, molti scenari reali richiedono che una sparkline lasci la cella — ad esempio, per essere incorporata in una cella diversa come immagine statica, allegata a un'email automatizzata, o renderizzata come parte di un report HTML pubblicato sul web.

Aspose.Cells supporta entrambe queste operazioni. Il metodo `Sparkline.toImage` renderizza una singola sparkline in uno stream, e i byte risultanti possono essere assegnati a `Cell.EmbeddedImage` (tramite `setEmbeddedImage`) in modo che l'immagine sia memorizzata all'interno di una singola cella della cartella di lavoro. Separatamente, `HtmlSaveOptions` consente di convertire l'intera cartella di lavoro — sparkline incluse — in un file HTML autonomo. Questo articolo illustra entrambi i flussi di lavoro end to end.

## **Flusso di lavoro 1 — Renderizzare le Sparkline in Immagini e Incorporarle nelle Celle**

In questo flusso di lavoro costruirai un foglio di lavoro che contiene un piccolo intervallo di valori sorgente, collegherai tre diversi gruppi di sparkline (Linea, Colonna e Stack/Win-Loss) a quell'intervallo, renderizzerai ciascun gruppo come PNG, e scriverai quei byte PNG nelle celle adiacenti come immagini incorporate. Il risultato finale è un singolo file `.xlsx` che contiene sia le sparkline live sia le loro controparti immagine renderizzate.

### **Istruzioni passo-passo**

1. Definisci una directory di lavoro e assicurati che esista su disco.
2. Crea una nuova `Workbook` e ottieni un riferimento al primo `Worksheet`.
3. Popola le celle da `A1` a `E1` con cinque valori numerici di esempio (ad esempio, vendite giornaliere o letture di temperatura).
4. Aggiungi tre oggetti `SparklineGroup` al foglio di lavoro chiamando `worksheet.getSparklineGroups().add(...)`:
   - Un gruppo `SparklineType.LINE` ancorato a `F1`, con intervallo di dati `A1:E1`.
   - Un gruppo `SparklineType.COLUMN` ancorato a `G1`, con intervallo di dati `A1:E1`.
   - Un gruppo `SparklineType.STACKED` (win/loss) ancorato a `H1`, con intervallo di dati `A1:E1`.
5. Crea un'istanza di `ImageOrPrintOptions` e chiama `setImageType(ImageType.PNG)` in modo che ogni sparkline venga renderizzata come PNG trasparente.
6. Per ciascuno dei tre gruppi, renderizza la sua singola sparkline usando `group.getSparklines().get(0).toImage(byteArrayOutputStream, imageOptions)`, converti il `ByteArrayOutputStream` in un `byte[]`, e assegna l'array rispettivamente tramite `worksheet.getCells().get("F2").setEmbeddedImage(...)`, `worksheet.getCells().get("G2").setEmbeddedImage(...)`, e `worksheet.getCells().get("H2").setEmbeddedImage(...)`.
7. Chiama `workbook.save("output_with_sparklines.xlsx")` per salvare la cartella di lavoro su disco.

```java
import com.aspose.cells.*;
import java.io.*;

// Crea una nuova cartella di lavoro e accedi al primo foglio di lavoro
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// Popola dati di esempio nelle celle A1:E1
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// Aggiungi un gruppo di sparkline a linee ancorato in F1 (colonna 5, riga 0)
CellArea lineArea = CellArea.createCellArea(5, 0, 5, 0);
int lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, lineArea);

// Aggiungi un gruppo di sparkline a colonne ancorato in G1 (colonna 6, riga 0)
CellArea columnArea = CellArea.createCellArea(6, 0, 6, 0);
int columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, columnArea);

// Aggiungi un gruppo di sparkline Win/Loss (in pila) ancorato in H1 (colonna 7, riga 0)
CellArea stackedArea = CellArea.createCellArea(7, 0, 7, 0);
int stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, stackedArea);

// Configura le opzioni dell'immagine per l'output PNG
ImageOrPrintOptions imageOptions = new ImageOrPrintOptions();
imageOptions.setImageType(ImageType.PNG);

// Converti la sparkline a linee in immagine e incorporala nella cella F2
Sparkline lineSp = worksheet.getSparklineGroups().get(lineIdx).getSparklines().get(0);
ByteArrayOutputStream lineMs = new ByteArrayOutputStream();
lineSp.toImage(lineMs, imageOptions);
worksheet.getCells().get("F2").setEmbeddedImage(lineMs.toByteArray());

// Converti la sparkline a colonne in immagine e incorporala nella cella G2
Sparkline columnSp = worksheet.getSparklineGroups().get(columnIdx).getSparklines().get(0);
ByteArrayOutputStream columnMs = new ByteArrayOutputStream();
columnSp.toImage(columnMs, imageOptions);
worksheet.getCells().get("G2").setEmbeddedImage(columnMs.toByteArray());

// Converti la sparkline Win/Loss in immagine e incorporala nella cella H2
Sparkline stackedSp = worksheet.getSparklineGroups().get(stackedIdx).getSparklines().get(0);
ByteArrayOutputStream stackedMs = new ByteArrayOutputStream();
stackedSp.toImage(stackedMs, imageOptions);
worksheet.getCells().get("H2").setEmbeddedImage(stackedMs.toByteArray());

// Salva la cartella di lavoro su disco
workbook.save("output_with_sparklines.xlsx");
```

Il codice sopra produce una cartella di lavoro in cui ogni rappresentazione visiva di una sparkline è duplicata in due forme: la sparkline live e nativa ancorata alla riga 1, e un'immagine PNG statica incorporata direttamente in una cella adiacente sulla riga 2. Poiché le immagini vivono all'interno del file stesso, la cartella di lavoro rimane un singolo artefatto autonomo che può essere inviato via email o archiviato senza rompere i riferimenti delle immagini incorporate. Renderizza ogni gruppo di sparkline come PNG, converti il `ByteArrayOutputStream` in un `byte[]`, e assegna l'array alla proprietà `EmbeddedImage` della cella di destinazione tramite `setEmbeddedImage(byte[])` — l'assegnazione è ciò che rende l'immagine parte del contenuto memorizzato della cella.

{{% alert color="primary" %}}
Poiché ogni gruppo di sparkline è ancorato a una singola cella, puoi indirizzarlo tramite l'indicizzatore `group.getSparklines().get(0)` invece di enumerare con un ciclo `for`. Ciò mantiene breve il codice di rendering e corrisponde al tipico pattern "una sparkline per cella di ancoraggio". La memorizzazione dei byte dell'immagine tramite `Cell.EmbeddedImage` (impostato tramite `setEmbeddedImage`) richiede Aspose.Cells 26.5 o versioni successive.
{{% /alert %}}

## **Flusso di lavoro 2 — Esportare il Foglio di Lavoro con Sparkline in HTML**

Una volta che la cartella di lavoro contiene sparkline live (e opzionalmente controparti immagine incorporate), l'intero foglio di lavoro può essere pubblicato sul web salvandolo come HTML. La classe `HtmlSaveOptions` espone le manopole necessarie per controllare questa esportazione; in questo flusso di lavoro riutilizzerai il file `output_with_sparklines.xlsx` prodotto dal Flusso di lavoro 1 e lo convertirai in un documento HTML pulito e a pagina singola.

### **Istruzioni passo-passo**

1. Assicurati che il file `output_with_sparklines.xlsx` prodotto dal Flusso di lavoro 1 sia disponibile su disco nella tua directory di lavoro.
2. Carica quel file in una nuova istanza di `Workbook`.
3. Istanzia `HtmlSaveOptions` e chiama `setExportActiveWorksheetOnly(true)` in modo che il file HTML risultante contenga solo il foglio di lavoro attivo anziché l'intera cartella di lavoro.
4. Chiama `workbook.save("sparklines.html", htmlOptions)` per scrivere l'output HTML su disco.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook("output_with_sparklines.xlsx");
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();
htmlOptions.setExportActiveWorksheetOnly(true);
workbook.save("sparklines.html", htmlOptions);
```

Il codice sopra prende la cartella di lavoro ricca di sparkline dal Flusso di lavoro 1 e la trasforma in un file HTML portatile. Le sparkline vengono preservate come rendering SVG o PNG inline all'interno dell'HTML generato, a seconda della modalità di esportazione, così gli utenti finali possono visualizzare i trend in qualsiasi browser moderno senza bisogno di Excel installato. Impostando `ExportActiveWorksheetOnly` su `true` tramite `setExportActiveWorksheetOnly(true)`, eviti di pubblicare accidentalmente fogli nascosti o dati ausiliari — viene esportato solo il foglio di lavoro attualmente visibile all'utente.

{{% alert color="primary" %}}
La classe `HtmlSaveOptions` offre proprietà aggiuntive per ottimizzare l'output, come `ExportHiddenWorksheet`, `ExportImagesAsBase64`, e `Encoding`. Regolale secondo necessità per il tuo target di distribuzione.
{{% /alert %}}

## **Riepilogo API**

I flussi di lavoro sopra si basano su un piccolo insieme di API di Aspose.Cells che lavorano insieme.

- `SparklineGroup` e l'accessor di collezione `worksheet.getSparklineGroups()` sono usati per dichiarare il tipo (Linea, Colonna, Stack), l'intervallo di dati, e la cella di ancoraggio per ciascun gruppo di sparkline. In questo articolo ciascun gruppo è ancorato a una singola cella, quindi il gruppo viene raggiunto tramite `worksheet.getSparklineGroups().get(i)`.
- `Sparkline` e l'indicizzatore `group.getSparklines().get(0)` restituiscono la singola sparkline all'interno di un gruppo. Poiché ogni gruppo nell'esempio contiene esattamente una sparkline, non è richiesto alcun ciclo `for`.
- `Sparkline.toImage(Stream, ImageOrPrintOptions)` è il metodo di rendering che scrive un'immagine della sparkline in un `Stream` fornito. Il metodo restituisce `void`; leggi i byte dallo stream dopo la chiamata.
- `Cell.EmbeddedImage` è una proprietà `byte[]` (assegnata tramite `cell.setEmbeddedImage(byte[])`) che memorizza un'immagine all'interno di una singola cella. È disponibile in **Aspose.Cells 26.5 e versioni successive** ed è il modo consigliato per reintrodurre una sparkline renderizzata da `toImage` nella stessa cartella di lavoro.
- `HtmlSaveOptions.setExportActiveWorksheetOnly(boolean)` limita l'esportazione HTML al foglio di lavoro attivo. È una delle proprietà più comunemente usate su `HtmlSaveOptions` quando si generano report a pagina singola.
- `ImageOrPrintOptions.setImageType(ImageType)` risiede nel package `com.aspose.cells.drawing` e seleziona il formato immagine (ad esempio, `ImageType.PNG`) usato durante il rendering con `toImage` e durante la stampa dei fogli di lavoro in immagini.

## **Articoli Correlati**

- [Sparklines in Aspose.Cells for Aspose.Cells for Java](/cells/it/java/sparkline/)
- [Inserimento di un'Immagine in una Cella](/cells/it/java/inserting-an-image-into-a-cell/)
- [Rendering di Array a Cella Singola con SmartMarker | Aspose.Cells Java](/cells/it/java/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="java" >}}
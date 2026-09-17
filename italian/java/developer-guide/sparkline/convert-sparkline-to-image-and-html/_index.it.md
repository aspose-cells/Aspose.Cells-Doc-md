---
title: Converti Sparkline in Immagine e HTML in Aspose.Cells for Java
description: Scopri come rendere le sparkline Aspose.Cells come immagini autonome da incorporare nelle celle ed esportare fogli di lavoro ricchi di sparkline in HTML utilizzando HtmlSaveOptions.
linktitle: Converti Sparkline in Immagine e HTML
keywords: Aspose.Cells, Java, sparkline, Sparkline.toImage, Cell.EmbeddedImage, HtmlSaveOptions, render sparkline, convert sparkline to image, export sparkline to HTML
type: docs
weight: 120
url: /it/java/convert-sparkline-to-image-and-html/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Le sparkline sono grafici in miniatura collocati all'interno delle celle di un foglio di lavoro. Aspose.Cells consente di estrarre ogni sparkline come immagine autonoma (da incorporare in un'altra cella o in un report esterno) e di esportare l'intero foglio di lavoro ricco di sparkline in HTML per la distribuzione tramite browser. La proprietà `Cell.EmbeddedImage` utilizzata in questo articolo è disponibile in **Aspose.Cells 26.5 e versioni successive**.

## **Introduzione**
Le sparkline rappresentano un modo compatto per visualizzare i trend direttamente all'interno di un foglio di lavoro. Mentre gli utenti di Excel le vedono nella loro posizione originale, molti scenari reali richiedono che una sparkline esca dalla cella, ad esempio per essere incorporata in una cella diversa come immagine statica, allegata a un'email automatica o resa come parte di un report HTML pubblicato sul web.
Aspose.Cells supporta entrambe queste operazioni. Il metodo `Sparkline.toImage` rende una singola sparkline in uno stream e i byte risultanti possono essere assegnati a `Cell.EmbeddedImage` (tramite `setEmbeddedImage`) in modo che l'immagine venga memorizzata all'interno di una singola cella della cartella di lavoro. Separatamente, `HtmlSaveOptions` consente di convertire l'intera cartella di lavoro, sparkline comprese, in un file HTML autonomo. Questo articolo illustra entrambi i flussi di lavoro dall'inizio alla fine.

## **Flusso di lavoro 1 — Rendi le sparkline come immagini e incorporale nelle celle**
In questo flusso di lavoro creerai un foglio di lavoro che contiene un piccolo intervallo di valori di origine, aggiungerai tre diversi gruppi di sparkline (Linea, Colonna e Impilata/Win-Loss) a tale intervallo, renderai ciascun gruppo come PNG e scriverai i byte PNG nelle celle adiacenti come immagini incorporate. Il risultato finale è un singolo file `.xlsx` che contiene sia le sparkline attive sia le relative controparti come immagini rese.

### **Istruzioni passo per passo**
1. Definisci una directory di lavoro e assicurati che esista sul disco.
2. Crea una nuova `Workbook` e ottieni un riferimento al primo `Worksheet`.
3. Popola le celle da `A1` a `E1` con cinque valori numerici di esempio (ad esempio, vendite giornaliere o letture della temperatura).
4. Aggiungi tre oggetti `SparklineGroup` al foglio di lavoro chiamando `worksheet.getSparklineGroups().add(...)`:
   - Un gruppo `SparklineType.LINE` ancorato a `F1`, con intervallo di dati `A1:E1`.
   - Un gruppo `SparklineType.COLUMN` ancorato a `G1`, con intervallo di dati `A1:E1`.
   - Un gruppo `SparklineType.STACKED` (win/loss) ancorato a `H1`, con intervallo di dati `A1:E1`.
5. Crea un'istanza di `ImageOrPrintOptions` e chiama `setImageType(ImageType.PNG)` in modo che ogni sparkline venga resa come PNG trasparente.
7. Chiama `workbook.save("output_with_sparklines.xlsx")` per salvare la cartella di lavoro su disco.

```java
import com.aspose.cells.*;
import java.io.*;
// Create a new workbook and access the first worksheet
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// Populate sample data in cells A1:E1
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// Add a Line sparkline group anchored at F1 (column 5, row 0)
CellArea lineArea = CellArea.createCellArea(5, 0, 5, 0);
int lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, lineArea);
// Add a Column sparkline group anchored at G1 (column 6, row 0)
CellArea columnArea = CellArea.createCellArea(6, 0, 6, 0);
int columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, columnArea);
// Add a Win/Loss (Stacked) sparkline group anchored at H1 (column 7, row 0)
CellArea stackedArea = CellArea.createCellArea(7, 0, 7, 0);
int stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, stackedArea);
// Configure image options for PNG output
ImageOrPrintOptions imageOptions = new ImageOrPrintOptions();
imageOptions.setImageType(ImageType.PNG);
// Convert the Line sparkline to image and embed it in cell F2
Sparkline lineSp = worksheet.getSparklineGroups().get(lineIdx).getSparklines().get(0);
ByteArrayOutputStream lineMs = new ByteArrayOutputStream();
lineSp.toImage(lineMs, imageOptions);
worksheet.getCells().get("F2").setEmbeddedImage(lineMs.toByteArray());
// Convert the Column sparkline to image and embed it in cell G2
Sparkline columnSp = worksheet.getSparklineGroups().get(columnIdx).getSparklines().get(0);
ByteArrayOutputStream columnMs = new ByteArrayOutputStream();
columnSp.toImage(columnMs, imageOptions);
worksheet.getCells().get("G2").setEmbeddedImage(columnMs.toByteArray());
// Convert the Win/Loss sparkline to image and embed it in cell H2
Sparkline stackedSp = worksheet.getSparklineGroups().get(stackedIdx).getSparklines().get(0);
ByteArrayOutputStream stackedMs = new ByteArrayOutputStream();
stackedSp.toImage(stackedMs, imageOptions);
worksheet.getCells().get("H2").setEmbeddedImage(stackedMs.toByteArray());
// Save the workbook to disk
workbook.save("output_with_sparklines.xlsx");
```

Il codice sopra produce una cartella di lavoro in cui ogni rappresentazione visiva di una sparkline è duplicata in due forme: la sparkline nativa e attiva ancorata alla riga 1 e un'immagine PNG statica incorporata direttamente in una cella adiacente sulla riga 2. Poiché le immagini risiedono all'interno del file stesso, la cartella di lavoro rimane un singolo artefatto autonomo che può essere inviato via email o archiviato senza rompere i riferimenti alle immagini incorporate. Rendi ogni gruppo di sparkline come PNG, converti il `ByteArrayOutputStream` in un `byte[]` e assegna l'array alla proprietà `EmbeddedImage` della cella di destinazione tramite `setEmbeddedImage(byte[])` — l'assegnazione è ciò che rende l'immagine parte del contenuto memorizzato nella cella.

{{% alert color="primary" %}}
Poiché ogni gruppo di sparkline è ancorato a una singola cella, puoi accedervi tramite l'indicizzatore `group.getSparklines().get(0)` invece di enumerare con un ciclo `for`. Questo mantiene breve il codice di rendering e corrisponde al tipico schema "una sparkline per cella di ancoraggio". La memorizzazione dei byte dell'immagine tramite `Cell.EmbeddedImage` (impostato tramite `setEmbeddedImage`) richiede Aspose.Cells 26.5 o versioni successive.

## **Flusso di lavoro 2 — Esporta il foglio di lavoro con sparkline in HTML**
Una volta che la cartella di lavoro contiene sparkline attive (e opzionalmente le controparti come immagini incorporate), l'intero foglio di lavoro può essere pubblicato sul web salvandolo come HTML. La classe `HtmlSaveOptions` espone le opzioni necessarie per controllare questa esportazione; in questo flusso di lavoro riutilizzerai il file `output_with_sparklines.xlsx` prodotto dal Flusso di lavoro 1 e lo convertirai in un documento HTML pulito e a pagina singola.

### **Istruzioni passo per passo**
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
La classe `HtmlSaveOptions` offre proprietà aggiuntive per ottimizzare l'output, come `ExportHiddenWorksheet`, `ExportImagesAsBase64` e `Encoding`. Regolale secondo necessità per il tuo target di distribuzione.

## **Riepilogo delle API**
I flussi di lavoro sopra si basano su un piccolo insieme di API Aspose.Cells che lavorano insieme.
- `SparklineGroup` e l'accessore di collection `worksheet.getSparklineGroups()` sono utilizzati per dichiarare il tipo (Line, Column, Stacked), l'intervallo di dati e la cella di ancoraggio per ciascun gruppo di sparkline. In questo articolo ogni gruppo è ancorato a una singola cella, quindi il gruppo viene raggiunto tramite `worksheet.getSparklineGroups().get(i)`.
- `Sparkline` e l'indicizzatore `group.getSparklines().get(0)` restituiscono la singola sparkline all'interno di un gruppo. Poiché ogni gruppo nell'esempio contiene esattamente una sparkline, non è necessario alcun ciclo `for`.
- `Sparkline.toImage(Stream, ImageOrPrintOptions)` è il metodo di rendering che scrive un'immagine della sparkline in uno `Stream` fornito. Il metodo restituisce `void`; leggi i byte dallo stream dopo la chiamata.
- `HtmlSaveOptions.setExportActiveWorksheetOnly(boolean)` limita l'esportazione HTML al foglio di lavoro attivo. È una delle proprietà più comunemente utilizzate su `HtmlSaveOptions` quando si generano report a pagina singola.
- `ImageOrPrintOptions.setImageType(ImageType)` risiede nel package `com.aspose.cells.drawing` e seleziona il formato immagine (ad esempio, `ImageType.PNG`) utilizzato durante il rendering con `toImage` e quando si stampano i fogli di lavoro come immagini.

## **Articoli correlati**
- [Sparklines in Aspose.Cells for Java](/it/java/sparkline/)
- [Inserimento di un'immagine in una cella](/it/java/inserting-an-image-into-a-cell/)
- [Rendering di array a cella singola SmartMarker | Aspose.Cells Java](/it/java/SmartMarker-Single-Cell-Array-Rendering/)
{{% /alert %}}

{{% /alert %}}

{{% /alert %}}

{{< app/cells/assistant language="java" >}}
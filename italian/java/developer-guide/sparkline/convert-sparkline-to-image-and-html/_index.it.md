---
title: Converti lo Sparkline in immagine e HTML con Aspose.Cells for Java
description: Scopri come eseguire il rendering degli sparkline di Aspose.Cells in immagini autonome per l'incorporamento nelle celle ed esportare in HTML i fogli di lavoro ricchi di sparkline utilizzando HtmlSaveOptions.
linktitle: Converti lo Sparkline in immagine e HTML
keywords: Aspose.Cells, Java, sparkline, Sparkline.toImage, Cell.EmbeddedImage, HtmlSaveOptions, rendering di sparkline, conversione di sparkline in immagine, esportazione di sparkline in HTML
type: docs
weight: 120
url: /it/java/convert-sparkline-to-image-and-html/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Gli sparkline sono grafici in miniatura collocati all'interno delle celle del foglio di lavoro. Aspose.Cells consente di estrarre ogni sparkline come immagine autonoma (per l'incorporamento in un'altra cella o in un report esterno) ed anche di esportare l'intero foglio di lavoro ricco di sparkline in HTML per la distribuzione tramite browser. La proprietà `Cell.EmbeddedImage` utilizzata in questo articolo è disponibile in **Aspose.Cells 26.5 e versioni successive**.
{{% /alert %}}

## **Introduzione**
Gli sparkline sono un modo compatto per visualizzare tendenze direttamente all'interno di un foglio di lavoro. Mentre gli utenti di Excel li visualizzano nella rispettiva posizione, molti scenari reali richiedono che uno sparkline leave la cella — ad esempio, per essere incorporato in un'altra cella come immagine statica, allegato a un'email automatizzata o renderizzato come parte di un report HTML pubblicato sul web.
Aspose.Cells supporta entrambe queste operazioni. Il metodo `Sparkline.toImage` esegue il rendering di un singolo sparkline in uno stream e i byte risultanti possono essere assegnati a `Cell.EmbeddedImage` (tramite `setEmbeddedImage`), in modo che l'immagine venga memorizzata all'interno di una singola cella della cartella di lavoro. Separatamente, `HtmlSaveOptions` consente di convertire l'intera cartella di lavoro — sparkline inclusi — in un file HTML autonomo. Questo articolo illustra entrambi i flussi di lavoro dall'inizio alla fine.

## **Flusso di lavoro 1 — Rendering degli sparkline in immagini e incorporamento nelle celle**
In questo flusso di lavoro verrà creato un foglio di lavoro contenente un breve intervallo di valori di origine, quindi verranno associati all'intervallo tre diversi gruppi di sparkline (Line, Column e Stacked/Win-Loss), ciascuno verrà renderizzato come PNG e i relativi byte PNG verranno scritti nelle celle adiacenti come immagini incorporate. Il risultato finale è un singolo file `.xlsx` che contiene sia gli sparkline nativi e attivi sia le rispettive controparti come immagini renderizzate.

### **Istruzioni passo dopo passo**
1. Definire una directory di lavoro e assicurarsi che esista sul disco.
2. Creare un nuovo `Workbook` e ottenere un riferimento al primo `Worksheet`.
3. Popolare le celle da `A1` a `E1` con cinque valori numerici di esempio (ad esempio, vendite giornaliere o rilevazioni della temperatura).
4. Aggiungere tre oggetti `SparklineGroup` al foglio di lavoro chiamando `worksheet.getSparklineGroups().add(...)`:
   - Un gruppo `SparklineType.LINE` ancorato a `F1`, con intervallo di dati `A1:E1`.
   - Un gruppo `SparklineType.COLUMN` ancorato a `G1`, con intervallo di dati `A1:E1`.
   - Un gruppo `SparklineType.STACKED` (win/loss) ancorato a `H1`, con intervallo di dati `A1:E1`.
5. Creare un'istanza di `ImageOrPrintOptions` e chiamare `setImageType(ImageType.PNG)` in modo che ogni sparkline venga renderizzato come PNG trasparente.
6. Chiamare `workbook.save("output_with_sparklines.xlsx")` per salvare la cartella di lavoro sul disco.

```java
import com.aspose.cells.*;
import java.io.*;
// Crea un nuovo workbook e accedi al primo foglio di lavoro
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// Popola le celle A1:E1 con dati di esempio
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// Aggiungi un gruppo di sparkline Line ancorato a F1 (colonna 5, riga 0)
CellArea lineArea = CellArea.createCellArea(0, 5, 0, 5);
int lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, lineArea);
// Aggiungi un gruppo di sparkline Column ancorato a G1 (colonna 6, riga 0)
CellArea columnArea = CellArea.createCellArea(0, 6, 0, 6);
int columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, columnArea);
// Aggiungi un gruppo di sparkline Win/Loss (Stacked) ancorato a H1 (colonna 7, riga 0)
CellArea stackedArea = CellArea.createCellArea(0, 7, 0, 7);
int stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, stackedArea);
// Configura le opzioni immagine per l'output PNG
ImageOrPrintOptions imageOptions = new ImageOrPrintOptions();
imageOptions.setImageType(ImageType.PNG);
// Converti la sparkline Line in un'immagine e incorporala nella cella F2
Sparkline lineSp = worksheet.getSparklineGroups().get(lineIdx).getSparklines().get(0);
ByteArrayOutputStream lineMs = new ByteArrayOutputStream();
lineSp.toImage(lineMs, imageOptions);
worksheet.getCells().get("F2").setEmbeddedImage(lineMs.toByteArray());
// Converti la sparkline Column in un'immagine e incorporala nella cella G2
Sparkline columnSp = worksheet.getSparklineGroups().get(columnIdx).getSparklines().get(0);
ByteArrayOutputStream columnMs = new ByteArrayOutputStream();
columnSp.toImage(columnMs, imageOptions);
worksheet.getCells().get("G2").setEmbeddedImage(columnMs.toByteArray());
// Converti la sparkline Win/Loss in un'immagine e incorporala nella cella H2
Sparkline stackedSp = worksheet.getSparklineGroups().get(stackedIdx).getSparklines().get(0);
ByteArrayOutputStream stackedMs = new ByteArrayOutputStream();
stackedSp.toImage(stackedMs, imageOptions);
worksheet.getCells().get("H2").setEmbeddedImage(stackedMs.toByteArray());
// Salva il workbook su disco
workbook.save("output_with_sparklines.xlsx");
```

Il codice sopra produce una cartella di lavoro in cui ogni rappresentazione visiva di uno sparkline è duplicata in due forme: lo sparkline nativo e attivo ancorato alla riga 1 e un'immagine PNG statica incorporata direttamente in una cella adiacente della riga 2. Poiché le immagini risiedono all'interno del file stesso, la cartella di lavoro rimane un unico artefatto autonomo che può essere inviato via email o archiviato senza compromettere i riferimenti alle immagini incorporate. Eseguire il rendering di ogni gruppo di sparkline come PNG, convertire il `ByteArrayOutputStream` in un `byte[]` e assegnare l'array alla proprietà `EmbeddedImage` della cella di destinazione tramite `setEmbeddedImage(byte[])` — l'assegnazione è ciò che rende l'immagine parte del contenuto memorizzato nella cella.

{{% alert color="primary" %}}
Poiché ogni gruppo di sparkline è ancorato a una singola cella, è possibile indirizzarlo tramite l'indicizzatore `group.getSparklines().get(0)` anziché enumerarlo con un ciclo `for`. In questo modo il codice di rendering rimane breve e corrisponde al modello tipico di "uno sparkline per cella di ancoraggio". La memorizzazione dei byte dell'immagine tramite `Cell.EmbeddedImage` (impostata con `setEmbeddedImage`) richiede Aspose.Cells 26.5 o versioni successive.
{{% /alert %}}

## **Flusso di lavoro 2 — Esportazione del foglio di lavoro con sparkline in HTML**
Una volta che la cartella di lavoro contiene sparkline attivi (e, facoltativamente, le rispettive controparti come immagini incorporate), l'intero foglio di lavoro può essere pubblicato sul web salvandolo come HTML. La classe `HtmlSaveOptions` espone le opzioni necessarie per controllare questa esportazione; in questo flusso di lavoro verrà riutilizzato il file `output_with_sparklines.xlsx` prodotto dal Flusso di lavoro 1 e convertito in un documento HTML pulito e di una sola pagina.

### **Istruzioni passo dopo passo**
1. Assicurarsi che il file `output_with_sparklines.xlsx` prodotto dal Flusso di lavoro 1 sia disponibile sul disco nella directory di lavoro.
2. Caricare quel file in una nuova istanza di `Workbook`.
3. Istanziare `HtmlSaveOptions` e chiamare `setExportActiveWorksheetOnly(true)` in modo che il file HTML risultante contenga solo il foglio di lavoro attivo anziché l'intera cartella di lavoro.
4. Chiamare `workbook.save("sparklines.html", htmlOptions)` per scrivere l'output HTML sul disco.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("output_with_sparklines.xlsx");
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();
htmlOptions.setExportActiveWorksheetOnly(true);
workbook.save("sparklines.html", htmlOptions);
```

Il codice sopra trasforma la cartella di lavoro ricca di sparkline del Flusso di lavoro 1 in un file HTML portabile. Gli sparkline vengono preservati come SVG inline o rendering PNG all'interno dell'HTML generato, a seconda della modalità di esportazione, in modo che gli utenti finali possano visualizzare le tendenze in qualsiasi browser moderno senza dover installare Excel. Impostando `ExportActiveWorksheetOnly` su `true` tramite `setExportActiveWorksheetOnly(true)`, si evita di pubblicare inadvertitamente fogli nascosti o dati ausiliari — viene esportato solo il foglio di lavoro attualmente visibile all'utente.

{{% alert color="primary" %}}
La classe `HtmlSaveOptions` offre ulteriori proprietà per regolare con precisione l'output, come `ExportHiddenWorksheet`, `ExportImagesAsBase64` e `Encoding`. Modificarle in base alle esigenze dell'ambiente di distribuzione.
{{% /alert %}}

## **Riepilogo delle API**
I flussi di lavoro descritti sopra si basano su un piccolo set di API di Aspose.Cells che operano in modo integrato.
- `SparklineGroup` e l'accessore della raccolta `worksheet.getSparklineGroups()` vengono utilizzati per dichiarare il tipo (Line, Column, Stacked), l'intervallo di dati e la cella di ancoraggio per ogni gruppo di sparkline. In questo articolo ogni gruppo è ancorato a una singola cella, quindi il gruppo viene recuperato tramite `worksheet.getSparklineGroups().get(i)`.
- `Sparkline` e l'indicizzatore `group.getSparklines().get(0)` restituiscono il singolo sparkline all'interno di un gruppo. Poiché ogni gruppo nell'esempio contiene esattamente uno sparkline, non è necessario alcun ciclo `for`.
- `Sparkline.toImage(Stream, ImageOrPrintOptions)` è il metodo di rendering che scrive un'immagine dello sparkline in uno `Stream` fornito. Il metodo restituisce `void`; dopo la chiamata, i byte vengono letti dallo stream.
- `HtmlSaveOptions.setExportActiveWorksheetOnly(boolean)` limita l'esportazione HTML al foglio di lavoro attivo. È una delle proprietà di `HtmlSaveOptions` più comunemente utilizzate quando si generano report a pagina singola.
- `ImageOrPrintOptions.setImageType(ImageType)` si trova nel package `com.aspose.cells.drawing` e seleziona il formato dell'immagine (ad esempio, `ImageType.PNG`) utilizzato durante il rendering con `toImage` e durante la stampa dei fogli di lavoro in immagini.

{{< app/cells/assistant language="java" >}}
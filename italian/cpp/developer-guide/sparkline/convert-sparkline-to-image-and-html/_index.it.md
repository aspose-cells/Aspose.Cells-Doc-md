---
title: Convertire Sparkline in Immagine e HTML in Aspose.Cells for C++
linktitle: Convertire Sparkline in Immagine e HTML
description: Scopri come renderizzare le sparkline di Aspose.Cells in immagini autonome per l'incorporamento nelle celle ed esportare fogli di lavoro ricchi di sparkline in HTML utilizzando HtmlSaveOptions.
keywords: Aspose.Cells, C++, sparkline, Sparkline.ToImage, Cell.EmbeddedImage, HtmlSaveOptions, renderizzare sparkline, convertire sparkline in immagine, esportare sparkline in HTML
type: docs
weight: 120
url: /it/cpp/convert-sparkline-to-image-and-html/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Le sparkline sono grafici in miniatura posizionati all'interno delle celle del foglio di lavoro. Aspose.Cells consente di estrarre ogni sparkline come immagine autonoma (da incorporare in un'altra cella o in un report esterno) e anche di esportare l'intero foglio di lavoro ricco di sparkline in HTML per la distribuzione tramite browser. La proprietà `Cell.EmbeddedImage` utilizzata in questo articolo è disponibile in **Aspose.Cells 26.5 e versioni successive**.

## **Introduzione**
Le sparkline sono un modo compatto per visualizzare i trend direttamente all'interno di un foglio di lavoro. Mentre gli utenti di Excel le vedono sul posto, molti scenari reali richiedono che una sparkline lasci la cella, ad esempio per essere incorporata in una cella diversa come immagine statica, allegata a un'email automatizzata o renderizzata come parte di un report HTML pubblicato sul web.
Aspose.Cells supporta entrambe queste operazioni. Il metodo `Sparkline.ToImage` renderizza una singola sparkline in un array di byte `Vector<uint8_t>`, e i byte risultanti possono essere assegnati a `Cell.EmbeddedImage` in modo che l'immagine sia memorizzata all'interno di una singola cella della cartella di lavoro. Separatamente, `HtmlSaveOptions` consente di convertire l'intera cartella di lavoro, comprese le sparkline, in un file HTML autonomo. Questo articolo illustra entrambi i flussi di lavoro end to end.

## **Flusso di lavoro 1 — Renderizzare le Sparkline in Immagini e Incorporarle nelle Celle**
In questo flusso di lavoro verrà creato un foglio di lavoro che contiene un piccolo intervallo di valori sorgente, verranno associati tre diversi gruppi di sparkline (Line, Column e Stacked/Win-Loss) a tale intervallo, ogni gruppo verrà renderizzato come PNG e i byte di tali PNG verranno scritti nelle celle adiacenti come immagini incorporate. Il risultato finale è un singolo file `.xlsx` che contiene sia le sparkline attive sia le relative controparti di immagine renderizzate.

### **Istruzioni passo-passo**
1. Definire una directory di lavoro e assicurarsi che esista sul disco.
2. Creare un nuovo `Workbook` e ottenere un riferimento al primo `Worksheet`.
3. Popolare le celle da `A1` a `E1` con cinque valori numerici di esempio (ad esempio, vendite giornaliere o letture di temperatura).
4. Aggiungere tre oggetti `SparklineGroup` al foglio di lavoro chiamando `worksheet.SparklineGroups.Add(...)`:
   - Un gruppo `SparklineType.Line` ancorato a `F1`, con intervallo dati `A1:E1`.
   - Un gruppo `SparklineType.Column` ancorato a `G1`, con intervallo dati `A1:E1`.
   - Un gruppo `SparklineType.Stacked` (win/loss) ancorato a `H1`, con intervallo dati `A1:E1`.
5. Creare un'istanza di `ImageOrPrintOptions` e impostare il suo `ImageType` su `ImageType.Png` in modo che ogni sparkline venga renderizzata come PNG trasparente.
6. Per ciascuno dei tre gruppi, renderizzare la sua singola sparkline utilizzando `group.Sparklines[0].ToImage(imageOptions)` — la chiamata restituisce i byte dell'immagine direttamente come `Vector<uint8_t>` — e assegnare l'array rispettivamente a `worksheet.GetCells().Get("F2"].EmbeddedImage`, `worksheet.GetCells().Get("G2"].EmbeddedImage` e `worksheet.GetCells().Get("H2"].EmbeddedImage`.
7. Salvare la cartella di lavoro come `output_with_sparklines.xlsx`.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.GetCells().Get(u"A1").PutValue(5);
    worksheet.GetCells().Get(u"B1").PutValue(-3);
    worksheet.GetCells().Get(u"C1").PutValue(8);
    worksheet.GetCells().Get(u"D1").PutValue(-2);
    worksheet.GetCells().Get(u"E1").PutValue(6);
    CellArea lineArea;
    lineArea.StartColumn = 5;
    lineArea.EndColumn = 5;
    lineArea.StartRow = 0;
    lineArea.EndRow = 0;
    int lineIdx = worksheet.GetSparklineGroups().Add(SparklineType::Line, U16String("A1:E1"), false, lineArea);
    CellArea columnArea;
    columnArea.StartColumn = 6;
    columnArea.EndColumn = 6;
    columnArea.StartRow = 0;
    columnArea.EndRow = 0;
    int columnIdx = worksheet.GetSparklineGroups().Add(SparklineType::Column, U16String("A1:E1"), false, columnArea);
    CellArea stackedArea;
    stackedArea.StartColumn = 7;
    stackedArea.EndColumn = 7;
    stackedArea.StartRow = 0;
    stackedArea.EndRow = 0;
    int stackedIdx = worksheet.GetSparklineGroups().Add(SparklineType::Stacked, U16String("A1:E1"), false, stackedArea);
    ImageOrPrintOptions imageOptions;
    imageOptions.SetImageType(ImageType::Png);
    Sparkline lineSp = worksheet.GetSparklineGroups().Get(lineIdx).GetSparklines().Get(0);
    Vector<uint8_t> lineImg = lineSp.ToImage(imageOptions);
    worksheet.GetCells().Get(u"F2").SetEmbeddedImage(lineImg);
    Sparkline columnSp = worksheet.GetSparklineGroups().Get(columnIdx).GetSparklines().Get(0);
    Vector<uint8_t> columnImg = columnSp.ToImage(imageOptions);
    worksheet.GetCells().Get(u"G2").SetEmbeddedImage(columnImg);
    Sparkline stackedSp = worksheet.GetSparklineGroups().Get(stackedIdx).GetSparklines().Get(0);
    Vector<uint8_t> stackedImg = stackedSp.ToImage(imageOptions);
    worksheet.GetCells().Get(u"H2").SetEmbeddedImage(stackedImg);
    workbook.Save(u"output_with_sparklines.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

Il codice sopra produce una cartella di lavoro in cui ogni rappresentazione visiva di una sparkline è duplicata in due forme: la sparkline nativa attiva ancorata alla riga 1, e un'immagine PNG statica incorporata direttamente in una cella adiacente alla riga 2. Poiché le immagini risiedono all'interno del file stesso, la cartella di lavoro rimane un singolo artefatto autonomo che può essere inviato via email o archiviato senza rompere i riferimenti delle immagini incorporate. Renderizzare ogni gruppo di sparkline come PNG — `Sparkline.ToImage(ImageOrPrintOptions)` restituisce i byte dell'immagine direttamente come `Vector<uint8_t>` — e assegnare l'array alla proprietà `EmbeddedImage` della cella di destinazione — l'assegnazione è ciò che rende l'immagine parte del contenuto memorizzato della cella.

{{% alert color="primary" %}}
Poiché ogni gruppo di sparkline è ancorato a una singola cella, è possibile accedervi tramite l'indicizzatore `group.Sparklines[0]` invece di enumerare con `foreach`. Questo mantiene breve il codice di rendering e corrisponde al tipico pattern "una sparkline per cella di ancoraggio". La memorizzazione dei byte dell'immagine tramite `Cell.EmbeddedImage` richiede Aspose.Cells 26.5 o versioni successive.

## **Flusso di lavoro 2 — Esportare il Foglio di Lavoro con Sparkline in HTML**
Una volta che la cartella di lavoro contiene sparkline attive (e opzionalmente controparti di immagini incorporate), l'intero foglio di lavoro può essere pubblicato sul web salvandolo come HTML. La classe `HtmlSaveOptions` espone le opzioni necessarie per controllare questa esportazione; in questo flusso di lavoro verrà riutilizzato il file `output_with_sparklines.xlsx` prodotto dal Flusso di lavoro 1 e convertito in un documento HTML pulito a pagina singola.

### **Istruzioni passo-passo**
1. Assicurarsi che il file `output_with_sparklines.xlsx` prodotto dal Flusso di lavoro 1 sia disponibile sul disco nella directory di lavoro.
2. Caricare quel file in una nuova istanza di `Workbook`.
3. Istanziare `HtmlSaveOptions` e impostare la sua proprietà `ExportActiveWorksheetOnly` su `true` in modo che il file HTML risultante contenga solo il foglio di lavoro attivo anziché l'intera cartella di lavoro.
4. Chiamare `workbook.Save("sparklines.html", htmlOptions)` per scrivere l'output HTML su disco.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook(u"output_with_sparklines.xlsx");
    HtmlSaveOptions htmlOptions;
    htmlOptions.SetExportActiveWorksheetOnly(true);
    workbook.Save(u"sparklines.html", htmlOptions);
    Aspose::Cells::Cleanup();
    return 0;
}
```

Il codice sopra prende la cartella di lavoro ricca di sparkline dal Flusso di lavoro 1 e la trasforma in un file HTML portatile. Le sparkline vengono conservate come renderizzazioni SVG o PNG inline all'interno dell'HTML generato, a seconda della modalità di esportazione, così gli utenti finali possono visualizzare i trend in qualsiasi browser moderno senza bisogno di Excel installato. Impostando `ExportActiveWorksheetOnly` su `true`, si evita di pubblicare accidentalmente fogli nascosti o dati ausiliari — viene esportato solo il foglio di lavoro attualmente visibile all'utente.

{{% alert color="primary" %}}
La classe `HtmlSaveOptions` offre proprietà aggiuntive per ottimizzare l'output, come `ExportHiddenWorksheet`, `ExportImagesAsBase64` e `Encoding`. Regolarle secondo le necessità per il proprio target di distribuzione.

## **Riepilogo delle API**
I flussi di lavoro sopra si basano su un piccolo insieme di API di Aspose.Cells che lavorano insieme.
- `SparklineGroup` e l'accessore della collezione `worksheet.SparklineGroups` vengono utilizzati per dichiarare il tipo (Line, Column, Stacked), l'intervallo dati e la cella di ancoraggio per ciascun gruppo di sparkline. In questo articolo ogni gruppo è ancorato a una singola cella, quindi il gruppo viene raggiunto tramite `worksheet.SparklineGroups[i]`.
- `Sparkline` e l'indicizzatore `group.Sparklines[0]` restituiscono la singola sparkline all'interno di un gruppo. Poiché ogni gruppo nell'esempio contiene esattamente una sparkline, non è richiesto alcun ciclo `foreach`.
- `Sparkline.ToImage(ImageOrPrintOptions)` è il metodo di rendering che restituisce un'immagine della sparkline direttamente come array di byte `Vector<uint8_t>`.
- `HtmlSaveOptions.ExportActiveWorksheetOnly` (un `bool`) limita l'esportazione HTML al foglio di lavoro attivo. È una delle proprietà più comunemente utilizzate su `HtmlSaveOptions` durante la generazione di report a pagina singola.
- `ImageOrPrintOptions.ImageType` risiede nel namespace `Aspose.Cells.Drawing` e seleziona il formato immagine (ad esempio, `ImageType.Png`) utilizzato durante il rendering con `ToImage` e durante la stampa di fogli di lavoro in immagini.

## **Articoli correlati**
- [Sparkline in Aspose.Cells for C++](/cells/it/cpp/sparkline/)
- [Inserimento di un'Immagine in una Cella](/cells/it/cpp/inserting-an-image-into-a-cell/)
- [Rendering di Array a Cella Singola con SmartMarker | Aspose.Cells for C++](/cells/it/cpp/SmartMarker-Single-Cell-Array-Rendering/)
{{% /alert %}}

{{% /alert %}}

{{% /alert %}}

{{< app/cells/assistant language="cpp" >}}
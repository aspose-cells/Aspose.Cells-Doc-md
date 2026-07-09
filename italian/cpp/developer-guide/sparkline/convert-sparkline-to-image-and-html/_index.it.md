---
title: Convertire Sparkline in Immagine e HTML in Aspose.Cells for C++
linktitle: Convert Sparkline to Image and HTML
description: Scopri come renderizzare gli sparkline di Aspose.Cells in immagini autonome per l'incorporamento nelle celle ed esportare fogli di lavoro ricchi di sparkline in HTML utilizzando HtmlSaveOptions.
keywords: Aspose.Cells, C++, sparkline, Sparkline.ToImage, Cell.EmbeddedImage, HtmlSaveOptions, renderizzare sparkline, convertire sparkline in immagine, esportare sparkline in HTML
type: docs
weight: 120
url: /it/cpp/convert-sparkline-to-image-and-html/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Gli sparkline sono grafici in miniatura posizionati all'interno delle celle del foglio di lavoro. Aspose.Cells consente di estrarre ogni sparkline come immagine autonoma (da incorporare in un'altra cella o in un report esterno) e anche di esportare l'intero foglio di lavoro ricco di sparkline in HTML per la distribuzione basata su browser. La proprietà `Cell.EmbeddedImage` utilizzata in questo articolo è disponibile in **Aspose.Cells 26.5 e versioni successive**.
{{% /alert %}}

## **Introduzione**

Gli sparkline rappresentano un modo compatto per visualizzare le tendenze direttamente all'interno di un foglio di lavoro. Mentre gli utenti di Excel li vedono sul posto, molti scenari reali richiedono che uno sparkline lasci la cella — ad esempio, per essere incorporato in una cella diversa come immagine statica, allegato a un'email automatizzata, oppure renderizzato come parte di un report HTML pubblicato sul web.

Aspose.Cells supporta entrambe queste operazioni. Il metodo `Sparkline.ToImage` renderizza un singolo sparkline in uno stream, e i byte risultanti possono essere assegnati a `Cell.EmbeddedImage` in modo che l'immagine venga memorizzata all'interno di una singola cella della cartella di lavoro. Separatamente, `HtmlSaveOptions` consente di convertire l'intera cartella di lavoro — sparkline inclusi — in un file HTML autonomo. Questo articolo illustra entrambi i flussi di lavoro passo dopo passo.

## **Flusso di lavoro 1 — Renderizzare gli Sparkline in Immagini e Incorporarli nelle Celle**

In questo flusso di lavoro creerai un foglio di lavoro che contiene un piccolo intervallo di valori sorgente, assocerai tre diversi gruppi di sparkline (Linea, Colonna e Stackato/Vittoria-Perdita) a tale intervallo, renderizzerai ciascun gruppo come PNG e scriverai quei byte PNG nelle celle adiacenti come immagini incorporate. Il risultato finale è un singolo file `.xlsx` che contiene sia gli sparkline attivi sia le loro controparti sotto forma di immagine renderizzata.

### **Istruzioni Passo per Passo**

1. Definisci una directory di lavoro e assicurati che esista su disco.
2. Crea una nuova `Workbook` e ottieni un riferimento al primo `Worksheet`.
3. Popola le celle da `A1` a `E1` con cinque valori numerici di esempio (ad esempio, vendite giornaliere o letture di temperatura).
4. Aggiungi tre oggetti `SparklineGroup` al foglio di lavoro chiamando `worksheet.SparklineGroups.Add(...)`:
   - Un gruppo `SparklineType.Line` ancorato a `F1`, con intervallo di dati `A1:E1`.
   - Un gruppo `SparklineType.Column` ancorato a `G1`, con intervallo di dati `A1:E1`.
   - Un gruppo `SparklineType.Stacked` (vittoria/perdita) ancorato a `H1`, con intervallo di dati `A1:E1`.
5. Crea un'istanza di `ImageOrPrintOptions` e imposta il suo `ImageType` su `ImageType.Png` in modo che ogni sparkline venga renderizzato come PNG trasparente.
6. Per ciascuno dei tre gruppi, renderizza il suo singolo sparkline utilizzando `group.Sparklines[0].ToImage(memoryStream, imageOptions)`, converti il `MemoryStream` in un `Vector<uint8_t>`, e assegna l'array rispettivamente a `worksheet.Cells["F2"].EmbeddedImage`, `worksheet.Cells["G2"].EmbeddedImage`, e `worksheet.Cells["H2"].EmbeddedImage`.
7. Salva la cartella di lavoro come `output_with_sparklines.xlsx`.

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

Il codice sopra produce una cartella di lavoro in cui ogni rappresentazione visiva di uno sparkline viene duplicata in due forme: lo sparkline nativo e attivo ancorato alla riga 1, e un'immagine PNG statica incorporata direttamente in una cella adiacente sulla riga 2. Poiché le immagini vivono all'interno del file stesso, la cartella di lavoro rimane un singolo artefatto autonomo che può essere inviato via email o archiviato senza rompere i riferimenti alle immagini incorporate. Renderizza ciascun gruppo di sparkline come PNG, converti il `MemoryStream` in un `Vector<uint8_t>`, e assegna l'array alla proprietà `EmbeddedImage` della cella di destinazione — è l'assegnazione che rende l'immagine parte del contenuto memorizzato della cella.

{{% alert color="primary" %}}
Poiché ciascun gruppo di sparkline è ancorato a una singola cella, è possibile accedervi attraverso l'indicizzatore `group.Sparklines[0]` invece di enumerare con `foreach`. Questo mantiene breve il codice di rendering e corrisponde al tipico pattern "uno sparkline per cella di ancoraggio". La memorizzazione dei byte dell'immagine tramite `Cell.EmbeddedImage` richiede Aspose.Cells 26.5 o versioni successive.
{{% /alert %}}

## **Flusso di lavoro 2 — Esportare il Foglio di Lavoro con Sparkline in HTML**

Una volta che la cartella di lavoro contiene sparkline attivi (e opzionalmente controparti di immagini incorporate), l'intero foglio di lavoro può essere pubblicato sul web salvandolo come HTML. La classe `HtmlSaveOptions` espone le opzioni necessarie per controllare questa esportazione; in questo flusso di lavoro riutilizzerai il file `output_with_sparklines.xlsx` prodotto dal Flusso di lavoro 1 e lo convertirai in un documento HTML pulito e a pagina singola.

### **Istruzioni Passo per Passo**

1. Assicurati che il file `output_with_sparklines.xlsx` prodotto dal Flusso di lavoro 1 sia disponibile su disco nella tua directory di lavoro.
2. Carica quel file in una nuova istanza di `Workbook`.
3. Crea un'istanza di `HtmlSaveOptions` e imposta la sua proprietà `ExportActiveWorksheetOnly` su `true` in modo che il file HTML risultante contenga solo il foglio di lavoro attivo anziché l'intera cartella di lavoro.
4. Chiama `workbook.Save("sparklines.html", htmlOptions)` per scrivere l'output HTML su disco.

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

Il codice sopra prende la cartella di lavoro ricca di sparkline dal Flusso di lavoro 1 e la trasforma in un file HTML portatile. Gli sparkline vengono preservati come rendering SVG o PNG inline all'interno dell'HTML generato, a seconda della modalità di esportazione, così gli utenti finali possono visualizzare le tendenze in qualsiasi browser moderno senza bisogno di Excel installato. Impostando `ExportActiveWorksheetOnly` su `true`, eviti di pubblicare accidentalmente fogli nascosti o dati ausiliari — viene esportato solo il foglio di lavoro attualmente visibile all'utente.

{{% alert color="primary" %}}
La classe `HtmlSaveOptions` offre proprietà aggiuntive per la messa a punto dell'output, come `ExportHiddenWorksheet`, `ExportImagesAsBase64`, e `Encoding`. Regolale secondo necessità per il tuo target di distribuzione.
{{% /alert %}}

## **Riepilogo delle API**

I flussi di lavoro sopra si basano su un piccolo insieme di API di Aspose.Cells che lavorano insieme.

- `SparklineGroup` e l'accessore alla collezione `worksheet.SparklineGroups` vengono utilizzati per dichiarare il tipo (Line, Column, Stacked), l'intervallo di dati e la cella di ancoraggio per ciascun gruppo di sparkline. In questo articolo ciascun gruppo è ancorato a una singola cella, quindi il gruppo viene raggiunto tramite `worksheet.SparklineGroups[i]`.
- `Sparkline` e l'indicizzatore `group.Sparklines[0]` restituiscono il singolo sparkline all'interno di un gruppo. Poiché ogni gruppo nell'esempio contiene esattamente uno sparkline, non è richiesto alcun ciclo `foreach`.
- `Sparkline.ToImage(Stream, ImageOrPrintOptions)` è il metodo di rendering che scrive un'immagine dello sparkline in uno `Stream` fornito. Il metodo restituisce `void`; leggi i byte dallo stream dopo la chiamata.
- `Cell.EmbeddedImage` è una proprietà `Vector<uint8_t>` che memorizza un'immagine all'interno di una singola cella. È disponibile in **Aspose.Cells 26.5 e versioni successive** ed è il modo consigliato per reimportare uno sparkline renderizzato da `ToImage` nella stessa cartella di lavoro.
- `HtmlSaveOptions.ExportActiveWorksheetOnly` (un `bool`) limita l'esportazione HTML al foglio di lavoro attivo. È una delle proprietà più comunemente utilizzate su `HtmlSaveOptions` quando si generano report a pagina singola.
- `ImageOrPrintOptions.ImageType` risiede nel namespace `Aspose.Cells.Drawing` e seleziona il formato dell'immagine (ad esempio, `ImageType.Png`) utilizzato durante il rendering con `ToImage` e durante la stampa dei fogli di lavoro in immagini.

## **Articoli Correlati**

- [Sparklines in Aspose.Cells for Aspose.Cells for C++](/cells/it/cpp/sparkline/)
- [Inserimento di un'Immagine in una Cella](/cells/it/cpp/inserting-an-image-into-a-cell/)
- [SmartMarker Single Cell Array Rendering | Aspose.Cells for C++](/cells/it/cpp/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="cpp" >}}
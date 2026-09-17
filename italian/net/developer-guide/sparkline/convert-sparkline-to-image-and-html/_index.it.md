---
title: Convertire Sparkline in Immagine e HTML in Aspose.Cells for .NET
description: Scopri come renderizzare le sparkline di Aspose.Cells in immagini standalone per l'incorporamento nelle celle ed esportare fogli di lavoro ricchi di sparkline in HTML utilizzando HtmlSaveOptions.
linktitle: Convertire Sparkline in Immagine e HTML
keywords: Aspose.Cells, .NET, sparkline, Sparkline.ToImage, Cell.EmbeddedImage, HtmlSaveOptions, renderizzare sparkline, convertire sparkline in immagine, esportare sparkline in HTML
type: docs
weight: 120
url: /it/net/convert-sparkline-to-image-and-html/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Le sparkline sono grafici in miniatura posizionati all'interno delle celle del foglio di lavoro. Aspose.Cells consente di estrarre ogni sparkline come immagine standalone (per l'incorporamento in un'altra cella o in un report esterno) e anche di esportare l'intero foglio di lavoro ricco di sparkline in HTML per la distribuzione basata su browser. La proprietà `Cell.EmbeddedImage` utilizzata in questo articolo è disponibile in **Aspose.Cells 26.5 e successivi**.

## **Introduzione**
Le sparkline sono un modo compatto per visualizzare i trend direttamente all'interno di un foglio di lavoro. Mentre gli utenti di Excel le vedono sul posto, molti scenari del mondo reale richiedono che una sparkline lasci la cella, ad esempio per essere incorporata in una cella diversa come immagine statica, allegata a un'email automatica o renderizzata come parte di un report HTML pubblicato sul web.
Aspose.Cells supporta entrambe queste operazioni. Il metodo `Sparkline.ToImage` renderizza una singola sparkline in un flusso e i byte risultanti possono essere assegnati a `Cell.EmbeddedImage`, così che l'immagine venga memorizzata all'interno di una singola cella della cartella di lavoro. Separatamente, `HtmlSaveOptions` consente di convertire l'intera cartella di lavoro, sparkline incluse, in un file HTML autonomo. Questo articolo illustra entrambi i flussi di lavoro end-to-end.

## **Flusso di Lavoro 1 — Renderizzare le Sparkline come Immagini e Incorporarle nelle Celle**
In questo flusso di lavoro creerai un foglio di lavoro che contiene un piccolo intervallo di valori sorgente, collegherai tre diversi gruppi di sparkline (Linea, Colonna e Stack/Win-Loss) a tale intervallo, renderizzerai ciascun gruppo come PNG e scriverai i byte PNG nelle celle adiacenti come immagini incorporate. Il risultato finale è un singolo file `.xlsx` che contiene sia le sparkline attive sia le loro controparti immagine renderizzate.

### **Istruzioni Passo-Passo**
1. Crea una nuova `Workbook` e ottieni un riferimento al primo `Worksheet`.
2. Popola le celle da `A1` a `E1` con cinque valori numerici di esempio (ad esempio, vendite giornaliere o letture di temperatura).
3. Aggiungi tre oggetti `SparklineGroup` al foglio di lavoro chiamando `worksheet.SparklineGroups.Add(...)`:
   - Un gruppo `SparklineType.Line` ancorato in `F1`, con intervallo dati `A1:E1`.
   - Un gruppo `SparklineType.Column` ancorato in `G1`, con intervallo dati `A1:E1`.
   - Un gruppo `SparklineType.Stacked` (win/loss) ancorato in `H1`, con intervallo dati `A1:E1`.
4. Crea un'istanza di `ImageOrPrintOptions` e imposta il suo `ImageType` su `ImageType.Png` in modo che ogni sparkline venga renderizzata come immagine PNG.
5. Salva la cartella di lavoro come `output_with_sparklines.xlsx`.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Charts;
using Aspose.Cells.Drawing;
using Aspose.Cells.Rendering;
// Crea una nuova cartella di lavoro e accedi al primo foglio di lavoro
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// Popola dati di esempio nelle celle A1:E1
worksheet.Cells["A1"].PutValue(5);
worksheet.Cells["B1"].PutValue(-3);
worksheet.Cells["C1"].PutValue(8);
worksheet.Cells["D1"].PutValue(-2);
worksheet.Cells["E1"].PutValue(6);
// Aggiungi un gruppo di sparkline di tipo Linea ancorato a F1 (colonna 5, riga 0)
CellArea lineArea = new CellArea();
lineArea.StartColumn = 5;
lineArea.EndColumn = 5;
lineArea.StartRow = 0;
lineArea.EndRow = 0;
int lineIdx = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, lineArea);
// Aggiungi un gruppo di sparkline di tipo Colonna ancorato a G1 (colonna 6, riga 0)
CellArea columnArea = new CellArea();
columnArea.StartColumn = 6;
columnArea.EndColumn = 6;
columnArea.StartRow = 0;
columnArea.EndRow = 0;
int columnIdx = worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, columnArea);
// Aggiungi un gruppo di sparkline Win/Loss (In pila) ancorato a H1 (colonna 7, riga 0)
CellArea stackedArea = new CellArea();
stackedArea.StartColumn = 7;
stackedArea.EndColumn = 7;
stackedArea.StartRow = 0;
stackedArea.EndRow = 0;
int stackedIdx = worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, stackedArea);
// Configura le opzioni dell'immagine per l'output PNG
ImageOrPrintOptions imageOptions = new ImageOrPrintOptions();
imageOptions.ImageType = ImageType.Png;
// Converti la sparkline Linea in immagine e incorporala nella cella F2
Sparkline lineSp = worksheet.SparklineGroups[lineIdx].Sparklines[0];
using (MemoryStream ms = new MemoryStream())
{
    lineSp.ToImage(ms, imageOptions);
    worksheet.Cells["F2"].EmbeddedImage = ms.ToArray();
}
// Converti la sparkline Colonna in immagine e incorporala nella cella G2
Sparkline columnSp = worksheet.SparklineGroups[columnIdx].Sparklines[0];
using (MemoryStream ms = new MemoryStream())
{
    columnSp.ToImage(ms, imageOptions);
    worksheet.Cells["G2"].EmbeddedImage = ms.ToArray();
}
// Converti la sparkline Win/Loss in immagine e incorporala nella cella H2
Sparkline stackedSp = worksheet.SparklineGroups[stackedIdx].Sparklines[0];
using (MemoryStream ms = new MemoryStream())
{
    stackedSp.ToImage(ms, imageOptions);
    worksheet.Cells["H2"].EmbeddedImage = ms.ToArray();
}
// Salva la cartella di lavoro su disco
workbook.Save("output_with_sparklines.xlsx");
```

Il codice sopra produce una cartella di lavoro in cui ogni rappresentazione visiva di una sparkline esiste in due forme: la sparkline nativa e attiva ancorata alla riga 1, e un'immagine PNG statica incorporata direttamente in una cella adiacente sulla riga 2. Poiché le immagini risiedono all'interno del file stesso, la cartella di lavoro rimane un singolo artefatto autonomo che può essere inviato via email o archiviato senza rompere i riferimenti delle immagini incorporate.

{{% alert color="primary" %}}
Poiché ogni gruppo di sparkline è ancorato a una singola cella, puoi accedervi tramite l'indicizzatore `group.Sparklines[0]` invece di enumerare con `foreach`. Ciò mantiene breve il codice di rendering e corrisponde al tipico pattern "una sparkline per cella di ancoraggio". La memorizzazione dei byte dell'immagine tramite `Cell.EmbeddedImage` richiede Aspose.Cells 26.5 o successivi.

## **Flusso di Lavoro 2 — Esportare il Foglio di Lavoro con Sparkline in HTML**
Una volta che la cartella di lavoro contiene sparkline attive (e facoltativamente controparti immagine incorporate), l'intero foglio di lavoro può essere pubblicato sul web salvandolo come HTML. La classe `HtmlSaveOptions` espone le opzioni necessarie per controllare questa esportazione; in questo flusso di lavoro riutilizzerai il file `output_with_sparklines.xlsx` prodotto dal Flusso di Lavoro 1 e lo convertirai in un documento HTML pulito e a pagina singola.

### **Istruzioni Passo-Passo**
1. Assicurati che il file `output_with_sparklines.xlsx` prodotto dal Flusso di Lavoro 1 sia disponibile su disco nella tua directory di lavoro.
2. Carica quel file in una nuova istanza di `Workbook`.
3. Crea un'istanza di `HtmlSaveOptions` e imposta la sua proprietà `ExportActiveWorksheetOnly` su `true` in modo che il file HTML risultante contenga solo il foglio di lavoro attivo anziché l'intera cartella di lavoro.
4. Chiama `workbook.Save("sparklines.html", htmlOptions)` per scrivere l'output HTML su disco.

```csharp
using System;
using System.IO;
using Aspose.Cells;
Workbook workbook = new Workbook("output_with_sparklines.xlsx");
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();
htmlOptions.ExportActiveWorksheetOnly = true;
workbook.Save("sparklines.html", htmlOptions);
```

Il codice sopra prende la cartella di lavoro ricca di sparkline dal Flusso di Lavoro 1 e la trasforma in un file HTML portatile. I gruppi di sparkline vengono renderizzati come immagini inline all'interno della tabella HTML generata, così gli utenti finali possono visualizzare i trend in qualsiasi browser moderno senza bisogno di Excel installato. Impostando `ExportActiveWorksheetOnly` su `true`, eviti di pubblicare accidentalmente fogli nascosti o dati ausiliari: viene esportato solo il foglio di lavoro attualmente visibile all'utente.

{{% alert color="primary" %}}
La classe `HtmlSaveOptions` offre proprietà aggiuntive per ottimizzare l'output, come `ExportHiddenWorksheet`, `ExportImagesAsBase64` ed `Encoding`. Modificale secondo necessità per il tuo target di distribuzione.

## **Riepilogo API**
I flussi di lavoro sopra si basano su un piccolo set di API Aspose.Cells che lavorano insieme.
- `SparklineGroup` e l'accessore di raccolta `worksheet.SparklineGroups` sono usati per dichiarare il tipo (Linea, Colonna, Stack), l'intervallo dati e la cella di ancoraggio per ciascun gruppo di sparkline. In questo articolo ogni gruppo è ancorato a una singola cella, quindi il gruppo viene raggiunto tramite `worksheet.SparklineGroups[i]`.
- `Sparkline` e l'indicizzatore `group.Sparklines[0]` restituiscono la singola sparkline all'interno di un gruppo. Poiché ogni gruppo nell'esempio contiene esattamente una sparkline, non è richiesto alcun ciclo `foreach`.
- `Sparkline.ToImage(Stream, ImageOrPrintOptions)` è il metodo di rendering che scrive un'immagine della sparkline in uno `Stream` fornito. Il metodo restituisce `void`; leggi i byte dal flusso dopo la chiamata.
- `HtmlSaveOptions.ExportActiveWorksheetOnly` (un `bool`) limita l'esportazione HTML al foglio di lavoro attivo. È una delle proprietà più comunemente utilizzate su `HtmlSaveOptions` quando si generano report a pagina singola.
- `ImageOrPrintOptions.ImageType` risiede nel namespace `Aspose.Cells.Drawing` e seleziona il formato immagine (ad esempio, `ImageType.Png`) utilizzato durante il rendering con `ToImage` e durante la stampa dei fogli di lavoro come immagini.

## **Articoli Correlati**
- [Creazione di Sparkline in Aspose.Cells for .NET](/it/net/creating-sparklines/)
{{% /alert %}}

{{% /alert %}}

{{% /alert %}}

{{< app/cells/assistant language="csharp" >}}
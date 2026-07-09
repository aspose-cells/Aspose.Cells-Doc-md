---
title: Convertire Sparkline in Immagine e HTML in Aspose.Cells for .NET
linktitle: Convert Sparkline to Image and HTML
description: Scopri come renderizzare le sparkline di Aspose.Cells in immagini autonome per l'incorporamento nelle celle ed esportare fogli di lavoro ricchi di sparkline in HTML utilizzando HtmlSaveOptions.
keywords: Aspose.Cells, .NET, sparkline, Sparkline.ToImage, Cell.EmbeddedImage, HtmlSaveOptions, renderizzare sparkline, convertire sparkline in immagine, esportare sparkline in HTML
type: docs
weight: 120
url: /it/net/convert-sparkline-to-image-and-html/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Le sparkline sono grafici in miniatura posizionati all'interno delle celle del foglio di lavoro. Aspose.Cells consente di estrarre ciascuna sparkline come immagine autonoma (da incorporare in un'altra cella o in un report esterno) e di esportare l'intero foglio di lavoro ricco di sparkline in HTML per la distribuzione basata su browser. La proprietà `Cell.EmbeddedImage` utilizzata in questo articolo è disponibile in **Aspose.Cells 26.5 e versioni successive**.
{{% /alert %}}

## **Introduzione**

Le sparkline sono un modo compatto per visualizzare tendenze direttamente all'interno di un foglio di lavoro. Mentre gli utenti di Excel le vedono sul posto, molti scenari reali richiedono che una sparkline lasci la cella, ad esempio per essere incorporata in una cella diversa come immagine statica, allegata a un'email automatizzata o renderizzata come parte di un report HTML pubblicato sul web.

Aspose.Cells supporta entrambe queste operazioni. Il metodo `Sparkline.ToImage` renderizza una singola sparkline in un flusso e i byte risultanti possono essere assegnati a `Cell.EmbeddedImage`, così che l'immagine venga memorizzata all'interno di una singola cella della cartella di lavoro. Separatamente, `HtmlSaveOptions` consente di convertire l'intera cartella di lavoro, comprese le sparkline, in un file HTML autonomo. Questo articolo illustra entrambi i flussi di lavoro passo dopo passo.

## **Flusso di lavoro 1 — Renderizzare le Sparkline in Immagini e Incorporarle nelle Celle**

In questo flusso di lavoro creerai un foglio di lavoro contenente un piccolo intervallo di valori di origine, collegherai tre diversi gruppi di sparkline (Line, Column e Stacked/Win-Loss) a tale intervallo, renderizzerai ciascun gruppo come PNG e scriverai i byte PNG nelle celle adiacenti come immagini incorporate. Il risultato finale è un singolo file `.xlsx` che contiene sia le sparkline attive sia le relative controparti come immagini renderizzate.

### **Istruzioni passo-passo**

1. Definisci una directory di lavoro e assicurati che esista su disco.
2. Crea una nuova `Workbook` e ottieni un riferimento al primo `Worksheet`.
3. Popola le celle da `A1` a `E1` con cinque valori numerici di esempio (ad esempio, vendite giornaliere o letture di temperatura).
4. Aggiungi tre oggetti `SparklineGroup` al foglio di lavoro chiamando `worksheet.SparklineGroups.Add(...)`:
   - Un gruppo `SparklineType.Line` ancorato a `F1`, con intervallo di dati `A1:E1`.
   - Un gruppo `SparklineType.Column` ancorato a `G1`, con intervallo di dati `A1:E1`.
   - Un gruppo `SparklineType.Stacked` (win/loss) ancorato a `H1`, con intervallo di dati `A1:E1`.
5. Crea un'istanza di `ImageOrPrintOptions` e imposta il suo `ImageType` su `ImageType.Png` in modo che ciascuna sparkline venga renderizzata come PNG trasparente.
6. Per ciascuno dei tre gruppi, renderizza la sua singola sparkline utilizzando `group.Sparklines[0].ToImage(memoryStream, imageOptions)`, converti il `MemoryStream` in un `byte[]` e assegna l'array rispettivamente a `worksheet.Cells["F2"].EmbeddedImage`, `worksheet.Cells["G2"].EmbeddedImage` e `worksheet.Cells["H2"].EmbeddedImage`.
7. Salva la cartella di lavoro come `output_with_sparklines.xlsx`.

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

// Aggiungi un gruppo di sparkline Linea ancorato in F1 (colonna 5, riga 0)
CellArea lineArea = new CellArea();
lineArea.StartColumn = 5;
lineArea.EndColumn = 5;
lineArea.StartRow = 0;
lineArea.EndRow = 0;
int lineIdx = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, lineArea);

// Aggiungi un gruppo di sparkline Colonna ancorato in G1 (colonna 6, riga 0)
CellArea columnArea = new CellArea();
columnArea.StartColumn = 6;
columnArea.EndColumn = 6;
columnArea.StartRow = 0;
columnArea.EndRow = 0;
int columnIdx = worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, columnArea);

// Aggiungi un gruppo di sparkline Vinte/ Perse (In pila) ancorato in H1 (colonna 7, riga 0)
CellArea stackedArea = new CellArea();
stackedArea.StartColumn = 7;
stackedArea.EndColumn = 7;
stackedArea.StartRow = 0;
stackedArea.EndRow = 0;
int stackedIdx = worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, stackedArea);

// Configura le opzioni immagine per l'output PNG
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

// Converti la sparkline Vinte/Perse in immagine e incorporala nella cella H2
Sparkline stackedSp = worksheet.SparklineGroups[stackedIdx].Sparklines[0];
using (MemoryStream ms = new MemoryStream())
{
    stackedSp.ToImage(ms, imageOptions);
    worksheet.Cells["H2"].EmbeddedImage = ms.ToArray();
}

// Salva la cartella di lavoro su disco
workbook.Save("output_with_sparklines.xlsx");
```

Il codice sopra produce una cartella di lavoro in cui ciascuna rappresentazione visiva di una sparkline è duplicata in due forme: la sparkline nativa e attiva ancorata alla riga 1 e un'immagine PNG statica incorporata direttamente in una cella adiacente sulla riga 2. Poiché le immagini vivono all'interno del file stesso, la cartella di lavoro rimane un singolo artefatto autonomo che può essere inviato via email o archiviato senza rompere i riferimenti alle immagini incorporate. Renderizza ciascun gruppo di sparkline come PNG, converti il `MemoryStream` in un `byte[]` e assegna l'array alla proprietà `EmbeddedImage` della cella di destinazione: è l'assegnazione che rende l'immagine parte del contenuto memorizzato della cella.

{{% alert color="primary" %}}
Poiché ciascun gruppo di sparkline è ancorato a una singola cella, puoi accedervi tramite l'indicizzatore `group.Sparklines[0]` invece di enumerare con `foreach`. Questo mantiene il codice di rendering breve e corrisponde al tipico schema "una sparkline per cella di ancoraggio". La memorizzazione dei byte dell'immagine tramite `Cell.EmbeddedImage` richiede Aspose.Cells 26.5 o versioni successive.
{{% /alert %}}

## **Flusso di lavoro 2 — Esportare il Foglio di lavoro con Sparkline in HTML**

Una volta che la cartella di lavoro contiene le sparkline attive (e facoltativamente le controparti come immagini incorporate), l'intero foglio di lavoro può essere pubblicato sul web salvandolo come HTML. La classe `HtmlSaveOptions` espone i parametri necessari per controllare questa esportazione; in questo flusso di lavoro riutilizzerai il file `output_with_sparklines.xlsx` prodotto dal Flusso di lavoro 1 e lo convertirai in un documento HTML pulito a pagina singola.

### **Istruzioni passo-passo**

1. Assicurati che il file `output_with_sparklines.xlsx` prodotto dal Flusso di lavoro 1 sia disponibile su disco nella tua directory di lavoro.
2. Carica quel file in una nuova istanza di `Workbook`.
3. Istanzia `HtmlSaveOptions` e imposta la sua proprietà `ExportActiveWorksheetOnly` su `true` in modo che il file HTML risultante contenga solo il foglio di lavoro attivo anziché l'intera cartella di lavoro.
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

Il codice sopra prende la cartella di lavoro ricca di sparkline dal Flusso di lavoro 1 e la trasforma in un file HTML portatile. Le sparkline vengono preservate come rendering SVG o PNG inline all'interno dell'HTML generato, a seconda della modalità di esportazione, così gli utenti finali possono visualizzare le tendenze in qualsiasi browser moderno senza bisogno di Excel installato. Impostando `ExportActiveWorksheetOnly` su `true`, eviti di pubblicare accidentalmente fogli nascosti o dati ausiliari: viene esportato solo il foglio di lavoro attualmente visibile all'utente.

{{% alert color="primary" %}}
La classe `HtmlSaveOptions` offre proprietà aggiuntive per ottimizzare l'output, come `ExportHiddenWorksheet`, `ExportImagesAsBase64` e `Encoding`. Modificale secondo le necessità del tuo target di distribuzione.
{{% /alert %}}

## **Riepilogo delle API**

I flussi di lavoro sopra si basano su un piccolo insieme di API di Aspose.Cells che lavorano insieme.

- `SparklineGroup` e l'accessore alla collezione `worksheet.SparklineGroups` sono utilizzati per dichiarare il tipo (Line, Column, Stacked), l'intervallo di dati e la cella di ancoraggio per ciascun gruppo di sparkline. In questo articolo ciascun gruppo è ancorato a una singola cella, quindi il gruppo viene raggiunto tramite `worksheet.SparklineGroups[i]`.
- `Sparkline` e l'indicizzatore `group.Sparklines[0]` restituiscono la singola sparkline all'interno di un gruppo. Poiché ogni gruppo nell'esempio contiene esattamente una sparkline, non è necessario alcun ciclo `foreach`.
- `Sparkline.ToImage(Stream, ImageOrPrintOptions)` è il metodo di rendering che scrive un'immagine della sparkline in un `Stream` fornito. Il metodo restituisce `void`; leggi i byte dal flusso dopo la chiamata.
- `Cell.EmbeddedImage` è una proprietà `byte[]` che memorizza un'immagine all'interno di una singola cella. È disponibile in **Aspose.Cells 26.5 e versioni successive** ed è il modo consigliato per reinserire una sparkline renderizzata da `ToImage` nella stessa cartella di lavoro.
- `HtmlSaveOptions.ExportActiveWorksheetOnly` (un `bool`) limita l'esportazione HTML al foglio di lavoro attivo. È una delle proprietà più comunemente utilizzate su `HtmlSaveOptions` quando si generano report a pagina singola.
- `ImageOrPrintOptions.ImageType` risiede nel namespace `Aspose.Cells.Drawing` e seleziona il formato dell'immagine (ad esempio, `ImageType.Png`) utilizzato durante il rendering con `ToImage` e durante la stampa dei fogli di lavoro in immagini.

## **Articoli correlati**

- [Sparkline in Aspose.Cells for .NET](/cells/it/net/sparkline/)
- [Inserimento di un'immagine in una cella](/cells/it/net/inserting-an-image-into-a-cell/)
- [Rendering di array a cella singola con SmartMarker | Aspose.Cells .NET](/cells/it/net/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="csharp" >}}
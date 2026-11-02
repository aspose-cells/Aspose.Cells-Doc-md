---
title: Convertire un grafico sparkline in un'immagine e in HTML con Aspose.Cells for JavaScript via C++
linktitle: Convertire un grafico sparkline in un'immagine e in HTML con Aspose.Cells for JavaScript via C++
description: Scopri come renderizzare i grafici sparkline di Aspose.Cells in immagini autonome per l'incorporamento nelle celle ed esportare in HTML i fogli di lavoro contenenti grafici sparkline utilizzando HtmlSaveOptions.
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++, grafico sparkline, sparkline.toImage, cell.embeddedImage, HtmlSaveOptions, rendering di grafici sparkline, conversione di un grafico sparkline in immagine, esportazione di un grafico sparkline in HTML
type: docs
weight: 120
url: /it/javascript-cpp/convert-sparkline-to-image-and-html/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
I grafici sparkline sono grafici in miniatura inseriti nelle celle di un foglio di lavoro. Aspose.Cells consente di estrarre ciascun grafico sparkline sotto forma di immagine autonoma (per incorporarla in un'altra cella o in un rapporto esterno) e di esportare l'intero foglio di lavoro contenente grafici sparkline in HTML per la distribuzione tramite browser. La proprietà `cell.embeddedImage` utilizzata in questo articolo è disponibile in **Aspose.Cells 26.5 e versioni successive**.
{{% /alert %}}

## **Introduzione**
I grafici sparkline sono un modo compatto per visualizzare le tendenze direttamente all'interno di un foglio di lavoro. Anche se in Excel sono visualizzati direttamente nelle celle, in molti scenari reali è necessario estrarre il grafico sparkline dalla cella, ad esempio per incorporarlo in un'altra cella come immagine statica, allegarlo a un'e-mail automatizzata o renderizzarlo come parte di un rapporto HTML pubblicato sul web.
Aspose.Cells supporta entrambe le operazioni. Il metodo `sparkline.toImage` restituisce i dati dell'immagine di un singolo grafico sparkline sotto forma di `Buffer`; i byte così ottenuti possono essere assegnati a `cell.embeddedImage`, in modo che l'immagine venga memorizzata all'interno di una singola cella della cartella di lavoro. In modo indipendente, `HtmlSaveOptions` consente di convertire l'intera cartella di lavoro — compresi i grafici sparkline — in un unico file HTML autonomo. Questo articolo illustra entrambi i flussi di lavoro dall'inizio alla fine.

## **Flusso di lavoro 1 — Generare i grafici sparkline in immagini e incorporarli nelle celle**
In questo flusso di lavoro verrà creato un foglio di lavoro contenente un piccolo intervallo di valori di origine. All'intervallo saranno associati tre diversi gruppi di grafici sparkline (Line, Column e Stacked/Win-Loss); ciascun gruppo verrà renderizzato in formato PNG e i relativi byte PNG saranno scritti in celle adiacenti come immagini incorporate. Il risultato finale è un unico file `.xlsx` che contiene sia i grafici sparkline attivi sia le rispettive immagini PNG.

### **Istruzioni dettagliate**
1. Creare un nuovo `Workbook` e ottenere un riferimento al primo `Worksheet`.
2. Popolare le celle da `A1` a `E1` con cinque valori numerici di esempio (ad esempio, vendite giornaliere o temperature rilevate).
3. Aggiungere tre oggetti `SparklineGroup` al foglio di lavoro chiamando `worksheet.getSparklineGroups().add(...)`:
   - Un gruppo `SparklineType.Line` ancorato a `F1`, con intervallo di dati `A1:E1`.
   - Un gruppo `SparklineType.Column` ancorato a `G1`, con intervallo di dati `A1:E1`.
   - Un gruppo `SparklineType.Stacked` (win/loss) ancorato a `H1`, con intervallo di dati `A1:E1`.
4. Creare un'istanza di `ImageOrPrintOptions` e impostare la proprietà `imageType` su `ImageType.Png`, in modo che ogni grafico sparkline venga renderizzato come immagine PNG.
5. Salvare la cartella di lavoro come `output_with_sparklines.xlsx`.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, CellArea, ImageOrPrintOptions } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            // Crea un nuovo workbook e accedi al primo foglio di lavoro
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            // Popola le celle A1:E1 con dati di esempio
            cells.get("A1").value = 5;
            cells.get("B1").value = -3;
            cells.get("C1").value = 8;
            cells.get("D1").value = -2;
            cells.get("E1").value = 6;
            // Aggiungi un gruppo di sparkline a linea ancorato a F1 (colonna 5, riga 0)
            const lineArea = new CellArea();
            lineArea.startColumn = 5;
            lineArea.endColumn = 5;
            lineArea.startRow = 0;
            lineArea.endRow = 0;
            const lineIdx = worksheet.sparklineGroups.add(
                AsposeCells.SparklineType.Line,
                "A1:E1",
                false,
                lineArea
            );
            // Aggiungi un gruppo di sparkline a colonna ancorato a G1 (colonna 6, riga 0)
            const columnArea = new CellArea();
            columnArea.startColumn = 6;
            columnArea.endColumn = 6;
            columnArea.startRow = 0;
            columnArea.endRow = 0;
            const columnIdx = worksheet.sparklineGroups.add(
                AsposeCells.SparklineType.Column,
                "A1:E1",
                false,
                columnArea
            );
            // Aggiungi un gruppo di sparkline vincita/perdita (impilato) ancorato a H1 (colonna 7, riga 0)
            const stackedArea = new CellArea();
            stackedArea.startColumn = 7;
            stackedArea.endColumn = 7;
            stackedArea.startRow = 0;
            stackedArea.endRow = 0;
            const stackedIdx = worksheet.sparklineGroups.add(
                AsposeCells.SparklineType.Stacked,
                "A1:E1",
                false,
                stackedArea
            );
            // Configura le opzioni immagine per l'output PNG
            const imageOptions = new ImageOrPrintOptions();
            imageOptions.imageType = AsposeCells.ImageType.Png;
            // Converti lo sparkline a linea in immagine e incorporalo nella cella F2
            const lineSp = worksheet.sparklineGroups.get(lineIdx).sparklines.get(0);
            cells.get("F2").embeddedImage = lineSp.toImage(imageOptions);
            // Converti lo sparkline a colonna in immagine e incorporalo nella cella G2
            const columnSp = worksheet.sparklineGroups.get(columnIdx).sparklines.get(0);
            cells.get("G2").embeddedImage = columnSp.toImage(imageOptions);
            // Converti lo sparkline vincita/perdita in immagine e incorporalo nella cella H2
            const stackedSp = worksheet.sparklineGroups.get(stackedIdx).sparklines.get(0);
            cells.get("H2").embeddedImage = stackedSp.toImage(imageOptions);
            // Salva il workbook su disco
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_with_sparklines.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

Il codice precedente produce una cartella di lavoro in cui ogni rappresentazione visiva di un grafico sparkline è presente in due forme: il grafico sparkline nativo e dinamico ancorato alla riga 1 e un'immagine PNG statica incorporata direttamente in una cella adiacente della riga 2. Poiché le immagini sono contenute nel file stesso, la cartella di lavoro rimane un unico artefatto autonomo, che può essere inviato via e-mail o archiviato senza compromettere i riferimenti alle immagini incorporate.

{{% alert color="primary" %}}
Poiché ogni gruppo di grafici sparkline è ancorato a una singola cella, è possibile accedervi tramite l'indicizzatore `group.getSparklines()[0]` anziché enumerare la raccolta. In questo modo, il codice di rendering rimane breve e corrisponde al modello tipico «un grafico sparkline per cella di ancoraggio». L'assegnazione dei byte dell'immagine tramite `cell.embeddedImage` richiede Aspose.Cells 26.5 o versioni successive.
{{% /alert %}}

## **Flusso di lavoro 2 — Esportare il foglio di lavoro con grafici sparkline in HTML**
Una volta che la cartella di lavoro contiene grafici sparkline attivi (e, facoltativamente, immagini statiche corrispondenti incorporate), l'intero foglio di lavoro può essere pubblicato sul web salvandolo come HTML. La classe `HtmlSaveOptions` espone le impostazioni necessarie per controllare questa esportazione; in questo flusso di lavoro verrà riutilizzato il file `output_with_sparklines.xlsx` prodotto dal Flusso di lavoro 1 e convertito in un documento HTML pulito e di una sola pagina.

### **Istruzioni dettagliate**
1. Assicurarsi che il file `output_with_sparklines.xlsx` prodotto dal Flusso di lavoro 1 sia disponibile su disco nella directory di lavoro.
2. Caricare il file in una nuova istanza di `Workbook`.
3. Istantiare `HtmlSaveOptions` e impostare la proprietà `exportActiveWorksheetOnly` su `true`, in modo che il file HTML risultante contenga solo il foglio di lavoro attivo anziché l'intera cartella di lavoro.
4. Chiamare `workbook.save("sparklines.html", htmlOptions)` per scrivere l'output HTML su disco.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, HtmlSaveOptions } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');
            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }
            try {
                const file = fileInput.files[0];
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const htmlOptions = new HtmlSaveOptions();
                htmlOptions.exportActiveWorksheetOnly = true;
                const outputData = workbook.save(AsposeCells.SaveFormat.Html, htmlOptions);
                const blob = new Blob([outputData], { type: "text/html" });
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "sparklines.html";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                result.innerHTML = `<p style="color: red;">${error.message}</p>`;
            }
        });
    </script>
</html>
```

Il codice precedente trasforma in un file HTML portatile la cartella di lavoro contenente grafici sparkline, prodotta dal Flusso di lavoro 1. I gruppi di grafici sparkline vengono renderizzati come immagini incorporate all'interno della tabella HTML generata, consentendo agli utenti finali di visualizzare le tendenze in qualsiasi browser moderno senza dover installare Excel. Impostando `exportActiveWorksheetOnly` su `true`, si evita di pubblicare involontariamente fogli nascosti o dati ausiliari: viene esportato soltanto il foglio di lavoro attualmente visibile all'utente.

{{% alert color="primary" %}}
La classe `HtmlSaveOptions` offre proprietà aggiuntive per regolare con precisione l'output, come `exportHiddenWorksheet`, `exportImagesAsBase64` e `encoding`. Regolare queste proprietà in base alle esigenze dell'ambiente di distribuzione.
{{% /alert %}}

## **Riepilogo delle API**
I flussi di lavoro precedenti si basano su un insieme ridotto di API Aspose.Cells che interagiscono tra loro.
- `SparklineGroup` e il metodo di accesso alla raccolta `worksheet.getSparklineGroups()` consentono di definire il tipo (Line, Column, Stacked), l'intervallo di dati e la cella di ancoraggio di ogni gruppo di grafici sparkline. In questo articolo ogni gruppo è ancorato a una singola cella, quindi il gruppo viene raggiunto tramite `worksheet.getSparklineGroups()[i]`.
- La classe `Sparkline` e l'indicizzatore `group.getSparklines()[0]` consentono di ottenere il singolo grafico sparkline contenuto in un gruppo. Poiché ogni gruppo nell'esempio contiene esattamente un grafico sparkline, non è necessario alcun ciclo di iterazione.
- `sparkline.toImage(imageOrPrintOptions)` è il metodo di rendering che restituisce un'immagine del grafico sparkline sotto forma di `Buffer`. I byte restituiti possono essere assegnati direttamente a `cell.embeddedImage`.
- `HtmlSaveOptions.exportActiveWorksheetOnly` (un valore booleano) limita l'esportazione in HTML al foglio di lavoro attivo. È una delle proprietà più utilizzate di `HtmlSaveOptions` durante la generazione di rapporti di una sola pagina.
- `ImageOrPrintOptions.imageType` seleziona il formato dell'immagine (ad esempio, `ImageType.Png`) utilizzato per il rendering con `toImage` e per la stampa dei fogli di lavoro in immagini.

{{< app/cells/assistant language="javascript-cpp" >}}
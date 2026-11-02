---
title: Camera di Excel in Aspose.Cells for JavaScript via C++
linktitle: Camera di Excel
description: Scopri come utilizzare la Camera di Excel in Aspose.Cells for JavaScript via C++ per creare un'immagine dinamica collegata a un intervallo di celle, che si aggiorna con i dati di origine e conserva l'intera formattazione della sorgente.
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++, Camera di Excel, immagine dinamica, immagine collegata, picture.formula, updateSelectedValue, createRange, toImage, Buffer
type: docs
weight: 90
url: /it/javascript-cpp/excel-camera/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

La Camera di Excel è un oggetto del foglio di lavoro che visualizza un'immagine aggiornata in tempo reale di un intervallo di celle e si colloca sul livello di disegno alla stregua di un'immagine ordinaria. Aspose.Cells supporta due modalità di creazione: un'immagine dinamica che si aggiorna automaticamente ogni volta che cambiano i dati di origine e un'immagine statica che cattura una singola istantanea di un intervallo. Questo articolo illustra entrambi gli approcci, così da consentire di scegliere quello più adatto alla struttura del documento.

## Che cos'è la Camera di Excel?
La Camera di Excel è essenzialmente un oggetto `Picture` ancorato a una riga e a una colonna specifiche del livello di disegno del foglio di lavoro. A differenza di un'immagine regolare inserita, la Camera è collegata a un intervallo di origine tramite una formula in stile A1, come `"A1:F10"`. Quando una qualsiasi cella all'interno dell'intervallo cambia, l'immagine della Camera viene aggiornata automaticamente per riflettere il nuovo contenuto. La Camera preserva l'intera formattazione dell'area di origine, inclusi bordi, colori di sfondo, font e formati di numero, in modo che tutto ciò che è visibile nelle celle appaia anche nell'immagine della Camera. La Camera è quindi particolarmente utile per dashboard, riepiloghi, pannelli laterali e layout di report, in cui si desidera un'anteprima visibile di un'area lontana del foglio di lavoro senza dover scorrere né ripetere i dati. Occorre tenere conto di due aspetti: è necessario chiamare `updateSelectedValue()` prima di salvare la cartella di lavoro e il file deve essere esportato in HTML o PDF, poiché tali formati si basano sui dati dell'immagine incorporata anziché su un ricalcolo in tempo reale.

## Metodo 1 — Aggiungere un'immagine dinamica tramite la Camera
La Camera dinamica è l'approccio più comune ed è il più vicino allo strumento Camera integrato in Excel. Funziona aggiungendo un'immagine priva di contenuto iniziale, quindi assegnandole una `formula` che fa riferimento all'intervallo di origine. Dopo l'assegnazione della formula, la chiamata a `updateSelectedValue()` aggiorna i dati dell'immagine incorporata, mantenendola sincronizzata con le celle di origine. La Camera non è implementata tramite una classe dedicata, ma si basa interamente sul tipo `Picture` standard.
Le API chiave sono:
- `worksheet.getPictures().add(upperLeftRow, upperLeftColumn, null)` — aggiunge un'immagine ancorata alla riga e alla colonna indicate. Passando `null` come parametro dell'immagine, viene creata un'immagine vuota che funge da segnaposto per una Camera dinamica. Il metodo restituisce l'indice della nuova immagine.
- `worksheet.getPictures().get(index)` — recupera un oggetto `Picture` specifico dalla raccolta.
- `picture.formula` — una proprietà di tipo `string` che contiene il riferimento in stile A1 all'intervallo di origine riprodotto dalla Camera, ad esempio `"A1:F10"`.
- `picture.updateSelectedValue()` — un metodo di tipo `void` che aggiorna i dati dell'immagine incorporata dalle celle a cui `formula` fa riferimento.

{{% alert color="primary" %}}
`updateSelectedValue()` DEVE essere chiamato prima del salvataggio quando l'output è in formato HTML o PDF; in caso contrario, il file esportato non conterrà i dati dell'immagine e la Camera apparirà vuota nel risultato renderizzato.
Il codice seguente crea una cartella di lavoro, aggiunge un'immagine vuota ancorata alla riga 10 e alla colonna 6, la collega all'intervallo di origine `A1:F10` tramite la proprietà `formula`, aggiorna i dati dell'immagine incorporata e salva la cartella di lavoro.
{{% /alert %}}

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
        const { Workbook, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "CameraDemo";
            // Camera dinamica: aggiungi un'immagine vuota, collegala tramite Formula a A1:F10, quindi aggiorna
            const pictures = worksheet.pictures;
            const index = pictures.add(10, 6, null);
            const picture = pictures.get(0);
            picture.formula = "A1:F10";
            picture.updateSelectedValue();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], {
                type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_dynamic.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## Metodo 2 — Aggiungere un'immagine statica tramite la Camera
La Camera statica è essenzialmente un'anteprima renderizzata una sola volta di un intervallo di celle. Invece di mantenere un collegamento in tempo reale, l'intervallo viene convertito una sola volta in byte di immagine, i quali vengono racchiusi in un `Buffer` e aggiunti come immagine regolare. Il contenuto dell'immagine rimane quindi fisso al momento della creazione e non si aggiorna automaticamente quando cambiano le celle di origine.
Le API chiave sono:
- `cells.createRange(address)` — costruisce un oggetto `Range` da un indirizzo in stile A1, come `"A1:F10"`.
- `range.toImage(options)` — renderizza l'intervallo in byte di immagine. Il passaggio di `null` utilizza le opzioni di rendering predefinite; sono disponibili sovraccarichi per un controllo più preciso sull'output.
- `Buffer.from(imageBytes)` — racchiude i byte dell'immagine generata in un `Buffer` che può essere passato a `worksheet.getPictures().add`.
- `worksheet.getPictures().add(upperLeftRow, upperLeftColumn, imageBuffer)` — aggiunge l'immagine ancorata alla riga e alla colonna indicate, questa volta passando il `Buffer` prodotto dal rendering.
Il codice seguente crea una cartella di lavoro, costruisce un `Range` per `A1:F10`, lo renderizza in byte di immagine tramite `range.toImage(null)`, racchiude i byte in un `Buffer`, aggiunge l'immagine ancorata alla riga 10 e alla colonna 6 e salva la cartella di lavoro.

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
        const { Workbook, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "CameraDemo";
            // Camera statica: crea Range, esegui il rendering in byte, inseriscilo in MemoryStream e aggiungilo come immagine
            const range = worksheet.cells.createRange("A1:F10");
            const imageData = range.toImage();
            const pictures = worksheet.pictures;
            pictures.add(10, 6, imageData);
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_static.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## Scegliere tra la modalità dinamica e quella statica
- **Camera dinamica:** si aggiorna a ogni ricalcolo, supporta l'esportazione in HTML e PDF dopo `updateSelectedValue()` e mantiene il comportamento di collegamento in tempo reale per l'intero ciclo di vita del file.
- **Camera statica:** un rendering eseguito una sola volta che non si aggiorna mai, utile quando si desidera un'istantanea visiva fissa incorporata al momento della compilazione anziché una visualizzazione dinamica dei dati.
Aspose.Cells supporta sia una Camera dinamica con aggiornamento automatico basata su `picture.formula` e `updateSelectedValue()`, sia una Camera statica, prodotta una sola volta e basata su `range.toImage` e `Buffer`. Scegli l'approccio dinamico quando il risultato deve restare sincronizzato con le celle di origine e quello statico quando è sufficiente un'istantanea visiva fissa al momento della compilazione.

## Articoli correlati
- [Convertire Sparkline in immagine e HTML con Aspose.Cells for JavaScript via C++](/cells/it/javascript-cpp/convert-sparkline-to-image-and-html/)
- [Aggiungere campi filtro a una tabella pivot in Aspose.Cells for JavaScript via C++](/cells/it/javascript-cpp/add-page-field-in-pivot-table/)
- [Applicare stili alle tabelle pivot in Aspose.Cells for JavaScript via C++](/cells/it/javascript-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}
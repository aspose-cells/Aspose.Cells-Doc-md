---
title: Imposta la larghezza della colonna in unità scalabili come em o percentuale con JavaScript tramite C++
linktitle: Impostare la larghezza della colonna su un unità scalabile come em o percentuale
type: docs
weight: 130
url: /it/javascript-cpp/set-column-width-to-scalable-unit-like-em-or-percent/
description: Impara come impostare la larghezza delle colonne in unità scalabili come em o percentuale in Aspose.Cells for JavaScript tramite C++. Migliora la presentazione delle tabelle HTML generate.
---

Generare un file HTML da un foglio di calcolo è molto comune. La dimensione delle colonne è definita in "pt," che funziona in molti casi. Tuttavia, potrebbe esserci un caso in cui questa dimensione fissa potrebbe non essere necessaria. Ad esempio, se la larghezza di un pannello contenitore è 600px, dove questa pagina HTML viene visualizzata, potresti ottenere una barra di scorrimento orizzontale se la larghezza della tabella generata è maggiore. È stato richiesto che questa dimensione fissa venga cambiata in un'unità scalabile come em o percentuale per ottenere una presentazione migliore. Il codice di esempio seguente può essere usato dove [**HtmlSaveOptions.widthScalable**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#widthScalable--) è impostato su **true** per creare larghezze scalabili.

I file di origine e i file di output di esempio possono essere scaricati dai seguenti collegamenti:

[sampleForScalableColumns.xlsx](73990150.xlsx)

[outsampleForScalableColumns.zip](73990151.zip)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Scalable Columns to HTML</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, HtmlSaveOptions, SaveFormat } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify Html Save Options
            const options = new HtmlSaveOptions();

            // Set the property for scalable width (converted from setWidthScalable)
            options.widthScalable = true;

            // Specify image save format (converted from setExportImagesAsBase64)
            options.exportImagesAsBase64 = true;

            // Save the workbook in Html format with specified Html Save Options
            const outputData = workbook.save(SaveFormat.Html, options);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outsampleForScalableColumns.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File converted to HTML successfully! Click the download link to get the result.</p>';
        });
    </script>
</html>
```

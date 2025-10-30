---
title: Converti Excel in HTML con tooltip usando JavaScript tramite C++  
linktitle: Convertire Excel in HTML con tooltip  
type: docs  
weight: 200  
url: /it/javascript-cpp/convert-excel-to-html-with-tooltip/  
description: Scopri come convertire i file Excel in formato HTML con tooltip per visualizzare correttamente il testo completo utilizzando Aspose.Cells for JavaScript tramite C++.  
---

## **Convertire Excel in HTML con tooltip**

Potrebbero esserci casi in cui il testo viene troncato nell'HTML generato e desideri visualizzare il testo completo come tooltip al hover. Aspose.Cells for JavaScript tramite C++ supporta questa funzionalità fornendo la proprietà [**HtmlSaveOptions.addTooltipText**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#addTooltipText--). Impostando la proprietà [**HtmlSaveOptions.addTooltipText**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#addTooltipText--) su **true** aggiungerà il testo completo come tooltip nell'HTML generato.

Nell'immagine seguente è mostrato il tooltip nel file HTML generato.

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

Il seguente esempio di codice carica il [file Excel sorgente](98107416.xlsx) e genera il [file HTML di output](98107417.zip) con il tooltip.

Codice di Esempio

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Add Tooltip to HTML Example</title>
    </head>
    <body>
        <h1>Add Tooltip to HTML Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions } = AsposeCells;

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

            // Instantiate a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create HtmlSaveOptions and enable tooltip text
            const options = new HtmlSaveOptions();
            options.addTooltipText = true;

            // Save workbook as HTML with the specified options
            const outputData = workbook.save(SaveFormat.Html, options);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'AddTooltipToHtmlSample_out.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML file created successfully! Click the download link to get the result.</p>';
        });
    </script>
</html>
```

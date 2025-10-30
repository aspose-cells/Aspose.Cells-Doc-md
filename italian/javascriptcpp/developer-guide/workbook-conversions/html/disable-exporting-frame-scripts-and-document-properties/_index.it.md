---
title: Disabilita l Esportazione di Script di Frame e Proprietà del Documento con JavaScript tramite C++
linktitle: Disabilita l Esportazione degli Script Frame e delle Proprietà del Documento
type: docs
weight: 310
url: /it/javascript-cpp/disable-exporting-frame-scripts-and-document-properties/
description: Impara come disabilitare l esportazione di script di frame e proprietà del documento durante la conversione di un workbook in HTML usando Aspose.Cells for JavaScript tramite C++.
--- 

{{% alert color="primary" %}}

Aspose.Cells esporta script di frame e proprietà del documento durante la conversione di un workbook in HTML. La versione 8.6.0 di Aspose.Cells for JavaScript tramite C++ introduce un'opzione che consente di disabilitare opzionalmente l'esportazione di script di frame e proprietà del documento. Usa la proprietà `HtmlSaveOptions.exportFrameScriptsAndProperties` per disabilitare l'esportazione.

{{% /alert %}}

## **Disabilita l'esportazione degli script frame e delle proprietà del documento**

Il seguente codice di esempio ti permette di disabilitare l'esportazione degli script frame e delle proprietà del documento. Una volta convertito un workbook in HTML, il file di output non conterrà alcuno script frame o proprietà del documento.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to HTML Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions, Utils } = AsposeCells;

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

            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Disable exporting frame scripts and document properties
            const options = new HtmlSaveOptions();
            options.exportFrameScriptsAndProperties = false;

            // Save workbook as HTML
            const outputData = workbook.save(SaveFormat.Html, options);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```

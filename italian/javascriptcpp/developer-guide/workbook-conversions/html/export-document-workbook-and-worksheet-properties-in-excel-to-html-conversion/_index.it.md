---
title: Esporta le proprietà del documento, cartella di lavoro e foglio di lavoro nella conversione da Excel a HTML con JavaScript via C++
linktitle: Esportare le proprietà del documento, del foglio di lavoro e del foglio di calcolo in HTML
type: docs
weight: 50
url: /it/javascript-cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
description: Scopri come esportare le proprietà di Documento, Cartella di Lavoro e Foglio di Lavoro in Excel in HTML utilizzando Aspose.Cells for JavaScript via C++.
---

## **Possibili Scenari di Utilizzo**  

Quando un file Microsoft Excel viene esportato in HTML usando Microsoft Excel o Aspose.Cells for JavaScript via C++, vengono esportate anche varie tipologie di proprietà di Documento, Cartella di Lavoro e Foglio di Lavoro come mostrato nello screenshot seguente. Puoi evitare di esportare queste proprietà impostando [**HtmlSaveOptions.exportDocumentProperties**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportDocumentProperties--), [**HtmlSaveOptions.exportWorkbookProperties**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportWorkbookProperties--) e [**HtmlSaveOptions.exportWorksheetProperties**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportWorksheetProperties--) su **false**. Il valore predefinito di queste proprietà è **true**. Lo screenshot seguente mostra come appaiono queste proprietà nell'HTML esportato.  

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)  

## **Esportare le proprietà del documento, del foglio di lavoro e del foglio di calcolo in HTML**  

Il codice di esempio di seguito carica il [file Excel di esempio](61767776.xlsx) e lo converte in HTML senza esportare le proprietà di Documento, Cartella di Lavoro e Foglio di Lavoro nell'[output HTML](61767779.zip).  

## **Codice di Esempio**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Export HTML without Properties</title>
    </head>
    <body>
        <h1>Export Excel to HTML (without document/workbook/worksheet properties)</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load the sample Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify Html Save Options
            const options = new HtmlSaveOptions();

            // We do not want to export document, workbook and worksheet properties
            options.exportDocumentProperties = false;
            options.exportWorkbookProperties = false;
            options.exportWorksheetProperties = false;

            // Export the Excel file to Html with Html Save Options
            const outputData = workbook.save(SaveFormat.Html, options);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputExportDocumentWorkbookAndWorksheetPropertiesInHTML.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            resultDiv.innerHTML = '<p style="color: green;">Export completed successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```

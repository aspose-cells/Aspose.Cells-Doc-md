---
title: Escludi Stili Inutilizzati durante la conversione da Excel a HTML con JavaScript tramite C++
linktitle: Escludere Stili Non Utilizzati durante la conversione da Excel a HTML
type: docs
weight: 30
url: /it/javascript-cpp/exclude-unused-styles-during-excel-to-html-conversion/
description: Impara come escludere gli stili inutilizzati durante la conversione da Excel a HTML usando Aspose.Cells for JavaScript tramite C++.
---

## **Possibili Scenari di Utilizzo**  

I file Microsoft Excel possono contenere molti stili inutilizzati. Quando esporti il file Excel in formato HTML, anche questi stili inutilizzati vengono esportati. Ciò può aumentare la dimensione dell'HTML. Puoi escludere gli stili inutilizzati durante la conversione di file Excel in HTML usando la proprietà [**HtmlSaveOptions.excludeUnusedStyles**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#excludeUnusedStyles--). Impostandola su **true**, tutti gli stili inutilizzati vengono esclusi dall'HTML di output. La schermata seguente mostra un esempio di stile inutilizzato all’interno dell’HTML di output.  

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)  

## **Escludere Stili Non Utilizzati durante la conversione da Excel a HTML**  

Il codice di esempio seguente crea una cartella di lavoro e crea anche uno stile nominato inutilizzato. Poiché [**HtmlSaveOptions.excludeUnusedStyles**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#excludeUnusedStyles--) è impostato su **true**, questo stile nominato inutilizzato non verrà esportato in [output HTML](61767778.zip). Se lo imposti su **false**, questo stile inutilizzato sarà presente nell’HTML di output, visibile nel markup HTML come mostrato nella schermata sopra.  

## **Codice di Esempio**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Exclude Unused Styles</title>
    </head>
    <body>
        <h1>Exclude Unused Styles from Excel to HTML</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
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

            if (fileInput.files.length > 0 && fileInput.files[0].size === 0) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select a valid Excel file.</p>';
                return;
            }

            // Instantiate workbook from selected file or create a new one
            let wb;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                wb = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                wb = new Workbook();
            }

            // Create an unused named style
            const style = wb.createStyle();
            style.name = "UnusedStyle_XXXXXXXXXXXXXX";

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Put some value in cell C7
            const cell = ws.cells.get("C7");
            cell.value = "This is sample text.";

            // Specify html save options, we want to exclude unused styles
            const opts = new HtmlSaveOptions();
            // Comment this line to include unused styles
            opts.excludeUnusedStyles = true;

            // Save the workbook in html format
            const outputData = wb.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: "text/html" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputExcludeUnusedStylesInExcelToHTML.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML generated successfully. Click the download link to get the result.</p>';
        });
    </script>
</html>
```

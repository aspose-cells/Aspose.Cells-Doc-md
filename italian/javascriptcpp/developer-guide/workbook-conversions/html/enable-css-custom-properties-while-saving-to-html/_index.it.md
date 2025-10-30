---
title: Abilita le Proprietà Personalizzate CSS durante il salvataggio in HTML con JavaScript tramite C++
linktitle: Abilita le Proprietà Personalizzate CSS durante il salvataggio in HTML
type: docs
weight: 320
url: /it/javascript-cpp/enable-css-custom-properties-while-saving-to-html/
description: Impara come abilitare le proprietà personalizzate CSS durante il salvataggio di file Excel in HTML usando Aspose.Cells for JavaScript tramite C++. 
---

## **Possibili Scenari di Utilizzo**

Quando salvi il file Excel in HTML, per lo scenario in cui ci sono più occorrenze di un'immagine base64, con proprietà personalizzate i dati dell'immagine devono essere salvati una sola volta, migliorando così le prestazioni dell'HTML risultante. Usa la proprietà [**HtmlSaveOptions.enableCssCustomProperties**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#enableCssCustomProperties--) e impostala **true** durante il salvataggio in HTML.
![todo:image_alt_text](enable-css-custom-properties-while-saving-to-html-1.jpg) 


## **Abilita le Proprietà CSS Personalizzate durante il salvataggio in HTML**

Il codice di esempio seguente mostra l'uso della proprietà [**HtmlSaveOptions.enableCssCustomProperties**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#enableCssCustomProperties--). La schermata mostra l'effetto di questa proprietà quando non è impostata su **true**. Scarica il [file Excel di esempio](50528260.xlsx) utilizzato in questo codice e l'[output HTML](50528261.zip) generato per riferimento.



## **Codice di Esempio**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Enable CSS Custom Properties Example</title>
    </head>
    <body>
        <h1>Enable CSS Custom Properties Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create HtmlSaveOptions and set properties (converted from setters to property assignments)
            const opts = new AsposeCells.HtmlSaveOptions();
            opts.exportImagesAsBase64 = true;
            opts.enableCssCustomProperties = true;

            // Save the workbook to HTML using SaveFormat.Html and provided options
            const outputData = workbook.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputEnableCssCustomProperties.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML saved successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

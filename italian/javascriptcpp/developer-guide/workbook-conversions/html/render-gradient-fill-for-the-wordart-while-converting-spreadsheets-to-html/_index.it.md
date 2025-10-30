---
title: Renderizzare la riempitura con sfumatura per WordArt durante la conversione di fogli di calcolo in HTML con JavaScript tramite C++
linktitle: Rendere il riempimento a gradienti per il WordArt durante la conversione dei fogli di calcolo in HTML
type: docs
weight: 90
url: /it/javascript-cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/
description: Impara come renderizzare la riempitura con sfumatura per WordArt durante la conversione di fogli di calcolo in HTML usando Aspose.Cells for JavaScript tramite C++.
---

## **Possibili Scenari di Utilizzo**  
Prima di Aspose.Cells 17.1, Aspose.Cells non rendeva il riempimento a gradiente di WordArt quando il file Excel veniva convertito in formato HTML. Dalla versione 17.1 di Aspose.Cells, il riempimento a gradiente di WordArt è supportato. La schermata seguente confronta l'effetto sul riempimento a gradiente convertendo il file Excel con Aspose.Cells 17.1 e le versioni precedenti.  

![todo:image_alt_text](render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to-html_1.png)  

## **Rendi il riempimento a sfumatura per l'WordArt durante la conversione dei fogli di calcolo in HTML**  
Il seguente esempio di codice converte il [file excel di origine](22774111.xlsx) in [formato HTML di output](22774109.zip). Il file excel di origine contiene un oggetto WordArt con riempimento a gradiente come mostrato nella schermata sopra.  

## **Codice di Esempio**  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Source Gradient Fill</title>
    </head>
    <body>
        <h1>Source Gradient Fill to HTML Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to HTML</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file (.xls, .xlsx, .csv).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save workbook to HTML format
            const outputData = workbook.save(SaveFormat.Html);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_sourceGradientFill.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Converted HTML File';

            resultDiv.innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```

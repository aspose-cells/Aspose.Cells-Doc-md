---
title: Ottieni oggetti serie di icone, barre di dati o scala colori usati nella formattazione condizionale
linktitle: Ottieni oggetti serie di icone, barre di dati o scala colori usati nella formattazione condizionale
description: Scopri come usare Aspose.Cells for JavaScript via C++ per recuperare set di icone, barre dati e oggetti di scala di colori nella formattazione condizionale dai file di fogli di calcolo.
keywords: Aspose.Cells, Formattazione condizionale, Set di icone, Barre dati, Scala di colori, Foglio di calcolo, JavaScript via C++
type: docs
weight: 10
url: /it/javascript-cpp/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/
---

{{% alert color="primary" %}}  

A volte è necessario recuperare serie di icone utilizzate nella formattazione condizionale di una cella o di un intervallo di celle e si desidera creare un file immagine basato su di esse. Potresti avere bisogno di leggere le barre di dati o le scale colori utilizzate nella formattazione condizionale. Aspose.Cells supporta questa funzionalità.

{{% /alert %}}  

Il seguente esempio di codice mostra come leggere i set di icone usati per la formattazione condizionale. Con l'API semplice di Aspose.Cells, i dati immagine del set di icone vengono salvati come immagine.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Aspose.Cells Example - Extract Conditional Formatting Icon</title>
    </head>
    <body>
        <h1>Extract Conditional Formatting Icon</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
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
            const resultEl = document.getElementById('result');

            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Open workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Get the A1 cell
            const cell = sheet.cells.get("A1");

            // Get the conditional formatting result object
            const cfr = cell.conditionalFormattingResult;

            // Get the icon set
            const icon = cfr.conditionalFormattingIcon;

            // Get image data from the icon and create a downloadable blob
            const imageData = icon.imageData;
            const blob = new Blob([imageData], { type: 'image/jpeg' });

            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'imgIcon.out.jpg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Extracted Icon Image';

            resultEl.innerHTML = '<p style="color: green;">Icon image extracted. Click the download link to save the image.</p>';
        });
    </script>
</html>
```

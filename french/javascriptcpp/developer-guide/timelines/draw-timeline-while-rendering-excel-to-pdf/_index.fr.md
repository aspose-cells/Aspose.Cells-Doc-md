---
title: Tracer la chronologie lors de la rendu d Excel en PDF avec JavaScript via C++
linktitle: Dessiner la chronologie lors du rendu d Excel en PDF
type: docs
weight: 60
url: /fr/javascript-cpp/draw-timeline-while-rendering-excel-to-pdf/
description: Gérer les chronologies de fichiers Excel avec Aspose.Cells for JavaScript via C++.
keywords: Rendu de la chronologie en PDF sans Office 2013, Office 2016, Office 2019 et Office 365 JavaScript via C++
---

## **Dessiner une chronologie lors du rendu d'Excel en PDF**
Si vous avez un fichier Excel avec une chronologie appliquée et que vous souhaitez exporter le fichier Excel en PDF avec les paramètres de la chronologie, Aspose.Cells for JavaScript via C++ supporte cela par défaut. Il suffit d'exporter le fichier Excel avec une chronologie en PDF, et le PDF généré affichera la chronologie appliquée.

Le code d'exemple suivant charge le [fichier Excel d'exemple](input.xlsx) qui contient une chronologie existante. Il enregistre ensuite le classeur sous la forme de [fichier PDF de sortie](out.pdf). La capture d'écran suivante compare le fichier Excel source et le fichier PDF généré.

<img src="out.png" width="60%">

## **Code d'exemple**
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
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Saving the workbook to PDF format (browser)
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

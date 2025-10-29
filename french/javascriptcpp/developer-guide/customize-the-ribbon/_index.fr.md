---
title: Personnaliser le XML du ruban avec JavaScript via C++
linktitle: Personnaliser le menu Excel
type: docs
weight: 1500
url: /fr/javascript-cpp/customizing-the-ribbon-xml/
description: Apprenez à personnaliser le XML du ruban dans Excel en utilisant Aspose.Cells for JavaScript via C++. 
---

{{% alert color="primary" %}} 

Microsoft Office a remplacé les menus et les barres d'outils par un ruban en haut de la fenêtre de l'application depuis Office 2007. Le ruban est personnalisable. 
Aspose.Cells for JavaScript via C++ vous permet de

- Conserver Ribbon XML sans l'analyser,
- Lire et écrire Ribbon XML sans l'analyser,
- Obtenir et définir les données de Ribbon XML.

Si vous souhaitez modifier le Ribbon XML, vous devez l'analyser avec un analyseur XML ou un autre outil Ribbon XML.

{{% /alert %}} 

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Set Ribbon XML</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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

            // Loads the workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Set custom ribbon XML
            const ribbonXml = `<customUI xmlns="http://schemas.microsoft.com/office/2006/01/customui"></customUI>`;
            workbook.ribbonXml = ribbonXml;

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            const outputFileName = 'output_' + (file.name || 'modified.xlsx');
            downloadLink.download = outputFileName;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Ribbon XML set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

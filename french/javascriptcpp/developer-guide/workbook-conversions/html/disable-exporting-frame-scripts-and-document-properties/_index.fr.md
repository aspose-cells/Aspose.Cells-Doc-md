---
title: Désactiver l exportation des scripts de cadre et des propriétés du document avec JavaScript via C++
linktitle: Désactiver l exportation des scripts de trame et des propriétés du document
type: docs
weight: 310
url: /fr/javascript-cpp/disable-exporting-frame-scripts-and-document-properties/
description: Apprenez comment désactiver l exportation des scripts de cadre et des propriétés du document lors de la conversion d un classeur en HTML avec Aspose.Cells for JavaScript via C++.
--- 

{{% alert color="primary" %}}

 Aspose.Cells exporte les scripts de cadre et les propriétés du document lors de la conversion d'un classeur en HTML. La version 8.6.0 de Aspose.Cells for JavaScript via C++ introduit une option qui vous permet de désactiver optionnellement l'exportation des scripts de cadre et des propriétés du document. Veuillez utiliser la propriété `HtmlSaveOptions.exportFrameScriptsAndProperties` pour désactiver l'export.

{{% /alert %}}

## **Désactiver l'exportation des scripts de trame et des propriétés du document**

Le code d'exemple suivant vous permet de désactiver l'exportation des scripts de trame et des propriétés du document. Une fois que vous avez converti un classeur en HTML, le fichier de sortie ne contiendra aucun script de trame et aucune propriété du document.

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

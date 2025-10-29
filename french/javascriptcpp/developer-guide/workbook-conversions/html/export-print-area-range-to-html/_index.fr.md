---
title: Exporter la plage de la zone d’impression en HTML avec JavaScript via C++
linktitle: Exporter la plage de zone d impression au format HTML
type: docs
weight: 60
url: /fr/javascript-cpp/export-print-area-range-to/
---

## **Scénarios d'utilisation possibles**

Il s'agit d'un scénario courant où nous devons exporter uniquement la zone d'impression, c'est-à-dire une plage sélectionnée de cellules au lieu de toute la feuille en HTML. Cette fonctionnalité est déjà disponible pour le rendu PDF ; cependant, vous pouvez maintenant effectuer cette tâche pour HTML également. Tout d'abord, définissez la zone d'impression dans l'objet de configuration de la page de la feuille de calcul. Ensuite, utilisez le drapeau [**HtmlSaveOptions.exportPrintAreaOnly()**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportPrintAreaOnly--) pour n'exporter que la plage sélectionnée.

## Code d'exemple

Le code d'exemple suivant charge un classeur puis exporte la zone d'impression au format HTML. Le fichier d'exemple pour tester cette fonctionnalité peut être téléchargé à partir du lien suivant :

[sampleInlineCharts.xlsx](79527946.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Export Print Area to HTML Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Set the print area.
            worksheet.pageSetup.printArea = "D2:M20";

            // Initialize HtmlSaveOptions
            const options = new AsposeCells.HtmlSaveOptions();

            // Set flag to export print area only
            options.exportPrintAreaOnly = true;

            // Save to HTML format (options specify HTML)
            const outputData = workbook.save(options);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputInlineCharts.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Export completed successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```

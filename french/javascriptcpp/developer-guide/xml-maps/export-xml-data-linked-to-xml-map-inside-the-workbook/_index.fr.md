---
title: Exporter les données XML liées à la carte XML à l intérieur du classeur avec JavaScript via C++
linktitle: Exporter les données XML liées à la carte XML à l intérieur du classeur
type: docs
weight: 20
url: /fr/javascript-cpp/export-xml-data-linked-to-xml-map-inside-the-workbook/
description: Apprenez comment exporter les données XML liées aux cartes XML dans votre classeur en utilisant Aspose.Cells for JavaScript via C++. 
---

## **Exporter des données XML liées à la carte XML à l'intérieur du classeur**

Veuillez utiliser la méthode [**Workbook.exportXml()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#exportXml-string-) pour exporter les données XML liées à vos cartographies XML dans votre classeur. Le code d'exemple suivant exporte les données XML de toutes les cartographies XML du classeur une par une. Veuillez vérifier le [fichier Excel d'exemple](5115497.xlsx) utilisé dans ce code et les [données XML exportées de la première cartographie XML](5472487.xml).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Export XML Maps Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="downloads"></div>
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

            // Instantiating a Workbook object with the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Clear previous downloads/results
            const downloadsContainer = document.getElementById('downloads');
            downloadsContainer.innerHTML = '';
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.style.display = 'none';
            document.getElementById('result').innerHTML = '';

            // Export all XML data from all XML Maps from the Workbook.
            for (let i = 0; i < workbook.worksheets.xmlMaps.count; i++) {
                // Access the XML Map.
                const map = workbook.worksheets.xmlMaps.get(i);

                // Exports its XML Data (returns data that can be downloaded)
                const xmlData = workbook.exportXml(map.name);

                // Create a downloadable link for each exported XML
                const blob = new Blob([xmlData], { type: 'application/xml' });
                const link = document.createElement('a');
                link.href = URL.createObjectURL(blob);
                link.download = `${map.name}.xml`;
                link.textContent = `Download ${map.name}.xml`;
                link.style.display = 'block';
                downloadsContainer.appendChild(link);
            }

            if (downloadsContainer.children.length === 0) {
                document.getElementById('result').innerHTML = '<p style="color: orange;">No XML Maps found in the workbook.</p>';
            } else {
                document.getElementById('result').innerHTML = '<p style="color: green;">Export completed. Use the links below to download the XML files.</p>';
            }
        });
    </script>
</html>
```

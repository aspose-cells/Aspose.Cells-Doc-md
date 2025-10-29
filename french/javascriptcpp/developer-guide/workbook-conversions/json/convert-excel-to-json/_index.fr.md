---
title: Convertir Excel en JSON avec JavaScript via C++
linktitle: Convertir Excel en JSON
type: docs
weight: 300
url: /fr/javascript-cpp/convert-excel-to-json/
description: Apprenez comment convertir un fichier Excel en JSON en utilisant Aspose.Cells for JavaScript via C++. 
keywords: Exportation du classeur en JSON JavaScript via C++, Conversion Excel en JSON JavaScript via C++
---

{{% alert color="primary" %}}  
 Aspose.Cells supporte la conversion d’un classeur en fichier JSON (JavaScript Object Notation).  
{{% /alert %}}  

## **Convertir un classeur Excel en JSON**  

Inutile de se demander comment convertir un classeur Excel en JSON, car la bibliothèque Aspose.Cells for JavaScript via C++ offre la meilleure solution. L'API Aspose.Cells supporte la conversion de feuilles de calcul en format JSON. Pour exporter le classeur en JSON, passez [**SaveFormat.Json**](https://reference.aspose.com/cells/javascript-cpp/saveformat/) comme deuxième paramètre de la méthode [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-). Vous pouvez également utiliser la classe [**JsonSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/jsonsaveoptions/) pour spécifier des paramètres supplémentaires lors de l'exportation de la feuille de calcul en JSON.  

L’exemple de code suivant montre comment exporter un classeur Excel en JSON. Veuillez consulter le code pour convertir le [fichier source](sample.xlsx) en fichier JSON généré par le code à titre de référence.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to JSON Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Convert the workbook to JSON
            const outputData = workbook.save(SaveFormat.Json);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample_out.json';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download JSON File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion to JSON completed. Click the download link to get the JSON file.</p>';
        });
    </script>
</html>
```  

L’exemple de code suivant utilise la classe JsonSaveOptions pour spécifier des paramètres supplémentaires et montre comment exporter un classeur Excel en JSON. Veuillez consulter le code pour convertir le [fichier source](sample.xlsx) en fichier JSON généré par le code à titre de référence.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Workbook to JSON Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, JsonSaveOptions, Utils } = AsposeCells;

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

            // Load your source workbook
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create an options of saving the file.
            const options = new JsonSaveOptions();

            // Set the exporting range.
            options.exportArea = CellArea.createCellArea("B1", "C4");

            // Convert the workbook to json file.
            const outputData = workbook.save(SaveFormat.Json, options);

            const blob = new Blob([outputData], { type: 'application/json' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample_out.json';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download JSON File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the JSON file.</p>';
        });
    </script>
</html>
```

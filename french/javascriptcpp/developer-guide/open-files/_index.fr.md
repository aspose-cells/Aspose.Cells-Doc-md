---
title: Chargement et gestion des fichiers Excel, OpenOffice, Json, Csv et Html
linktitle: Ouvrir des fichiers
type: docs
weight: 20
url: /fr/javascript-cpp/loading-saving-and-managing/
description: Avec Aspose.Cells, il est simple de créer, ouvrir et gérer des fichiers Excel, CSV, TSV, ODS, HTML, Numbers, Json, XML, Pdf, Jpg, Tiff, Image, Mht, et XPS en utilisant JavaScript via C++.
---

{{% alert color="primary" %}}

 Avec Aspose.Cells, il est simple de créer, ouvrir et gérer des fichiers Excel, par exemple pour extraire des données ou utiliser un modèle de concepteur pour accélérer le développement.

{{% /alert %}}

## **Création d'un nouveau classeur**
L'exemple suivant crée un nouveau classeur à partir de zéro.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Set Cell Value</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Create Workbook</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/Aspose.Cells.lic",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            // Instantiate a Workbook object (new blank workbook)
            const wb = new Workbook();

            // Access the first worksheet in the workbook
            const sheet = wb.worksheets.get(0);

            // Access the "A1" cell in the sheet
            const cell = sheet.cells.get("A1");

            // Input the "Hello World!" text into the "A1" cell
            cell.value = "Hello World!";

            // Save the Excel file and prepare download link
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'MyBook_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and cell updated. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Ouverture et enregistrement d'un fichier**
 Avec Aspose.Cells, il est simple d’ouvrir, d’enregistrer et de gérer des fichiers Excel.

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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Creating a Workbook object and opening an Excel file using its file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Adding new sheet
            const sheetIndex = workbook.worksheets.add("MySheet");
            const sheet = workbook.worksheets.get(sheetIndex);

            // Setting active sheet
            workbook.worksheets.activeSheetIndex = 1;

            // Setting values.
            const cells = sheet.cells;

            // Setting text
            cells.get("A1").putValue("Hello!");

            // Setting number
            cells.get("A2").putValue(1000);

            // Setting Date Time
            const cell = cells.get("A3");
            cell.putValue(new Date());
            const style = cell.style;
            style.number = 14;
            cell.style = style;

            // Setting formula
            cells.get("A4").formula = "=SUM(A1:A3)";

            // Saving the workbook and providing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'dest.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Sujets avancés**
- [Différentes façons d'ouvrir des fichiers](/cells/fr/javascript-cpp/different-ways-to-open-files/)
- [Filtrer les noms définis lors du chargement du classeur](/cells/fr/javascript-cpp/filter-defined-names-while-loading-workbook/)
- [Filtrer les objets lors du chargement du classeur ou de la feuille de calcul](/cells/fr/javascript-cpp/filter-objects-while-loading-workbook-or-worksheet/)
- [Filtrer le type de données lors du chargement du classeur à partir du fichier modèle](/cells/fr/javascript-cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/)
- [Obtenir des avertissements lors du chargement d'un fichier Excel](/cells/fr/javascript-cpp/get-warnings-while-loading-excel-file/)
- [Charger le fichier Excel source sans graphiques](/cells/fr/javascript-cpp/load-source-excel-file-without-charts/)
- [Charger des feuilles de calcul spécifiques dans un classeur](/cells/fr/javascript-cpp/load-specific-worksheets-in-a-workbook/)
- [Charger le classeur avec une taille de papier d'imprimante spécifiée](/cells/fr/javascript-cpp/load-workbook-with-specified-printer-paper-size/)
- [Ouvrir des fichiers de différentes versions de Microsoft Excel](/cells/fr/javascript-cpp/opening-different-microsoft-excel-versions-files/)
- [Ouvrir des fichiers avec différents formats](/cells/fr/javascript-cpp/opening-files-with-different-formats/)
- [Optimiser l'utilisation de la mémoire lors du travail avec de gros fichiers contenant de grands ensembles de données](/cells/fr/javascript-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)
- [Lire des feuilles de calcul numériques développées par Apple Inc. à l'aide d'Aspose.Cells](/cells/fr/javascript-cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [Arrêter la conversion ou le chargement à l'aide de InterruptMonitor lorsqu'il prend trop de temps](/cells/fr/javascript-cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/)
- [Utiliser l'API LightCells](/cells/fr/javascript-cpp/using-lightcells-api/)
- [Convertir CSV en JSON](/cells/fr/javascript-cpp/convert-csv-to-json/)
- [Convertir Excel en JSON](/cells/fr/javascript-cpp/convert-excel-to-json/)
- [Convertir JSON en CSV](/cells/fr/javascript-cpp/convert-json-to-csv/)
- [Convertir JSON en Excel](/cells/fr/javascript-cpp/convert-json-to-excel/)
- [Convertir Excel en Html](/cells/fr/javascript-cpp/convert-excel-to-html/)

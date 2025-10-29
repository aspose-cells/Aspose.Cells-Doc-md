---
title: Convertir Excel en CSV, TSV et Txt avec JavaScript via C++
linktitle: Enregistrer en CSV, TSV et Txt
type: docs
weight: 40
url: /fr/javascript-cpp/convert-excel-to-csv-tsv-and-txt/
description: Apprenez comment convertir des fichiers Excel en formats CSV, TSV et TXT en utilisant Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}

Aspose.Cells permet de convertir des fichiers Excel, ODS, JSON, et autres formats en CSV, TSV, et TXT.

{{% /alert %}}

## **Enregistrer le classeur au format texte ou CSV**

Parfois, vous souhaitez convertir ou enregistrer un classeur avec plusieurs feuilles de calcul au format texte. Pour les formats texte (par exemple TXT, TabDelim, CSV, etc.), par défaut, Microsoft Excel et Aspose.Cells enregistrent uniquement le contenu de la feuille active.

L’exemple de code suivant explique comment sauvegarder l’intégralité du classeur au format texte. Chargez le classeur source, qui peut être n’importe quel fichier de feuille de calcul Microsoft Excel ou OpenOffice (XLS, XLSX, XLSM, XLSB, ODS, etc.) avec n’importe quel nombre de feuilles.

Lorsque le code est exécuté, il convertit les données de toutes les feuilles du classeur au format TXT

Vous pouvez modifier le même exemple pour enregistrer votre fichier au format CSV. Par défaut, [**TxtSaveOptions.separator**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#separator--) est une virgule, alors ne spécifiez pas de séparateur si vous enregistrez au format CSV.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Txt Save Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Txt Save Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TxtSaveOptions, Utils } = AsposeCells;

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

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Text save options. You can use any type of separator
            const opts = new TxtSaveOptions();
            opts.separator = '\t';
            opts.exportAllSheets = true;

            // Save entire workbook data into file (as text)
            const outputData = workbook.save(SaveFormat.Txt, opts);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.txt';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Text File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook saved as text. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Enregistrement de fichiers texte avec séparateur personnalisé**

Les fichiers texte contiennent des données de feuille de calcul sans mise en forme. Le fichier est un type de fichier texte brut qui peut avoir des délimiteurs personnalisés entre ses données

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Export Workbook to TXT/CSV Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, TxtSaveOptions, SaveFormat } = AsposeCells;

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

            // Create a Workbook object from the uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Instantiate Text File's Save Options
            const options = new TxtSaveOptions();

            // Specify the separator
            options.separator = ";";

            // Optionally specify CSV save format if required by the API
            options.saveFormat = SaveFormat.CSV;

            // Save the workbook to CSV/TXT using the options
            const outputData = wb.save(SaveFormat.CSV, options);
            const blob = new Blob([outputData], { type: 'text/csv' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.csv';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download CSV File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File converted successfully! Click the download link to get the result.</p>';
        });
    </script>
</html>
```


## **Sujets avancés**
- [Conserver les séparateurs pour les lignes vides lors de l'exportation de feuilles de calcul au format CSV](/cells/fr/javascript-cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Supprimer les lignes et colonnes vides en tête lors de l'exportation de feuilles de calcul au format CSV](/cells/fr/javascript-cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)

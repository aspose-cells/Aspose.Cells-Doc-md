---
title: Conserver les séparateurs pour les lignes blanches lors de l exportation de feuilles de calcul au format CSV avec JavaScript via C++
linktitle: Conserver les séparateurs pour les lignes vides lors de l exportation de feuilles de calcul au format CSV
type: docs
weight: 160
url: /fr/javascript-cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
---

## **Conserver les séparateurs pour les lignes vides lors de l'exportation de feuilles de calcul au format CSV**  

Aspose.Cells offre la possibilité de conserver les séparateurs de ligne lors de la conversion de feuilles de calcul en format CSV. Pour cela, vous pouvez utiliser la propriété [**TxtSaveOptions.keepSeparatorsForBlankRow**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#keepSeparatorsForBlankRow--) de [**TxtSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/). [**TxtSaveOptions.keepSeparatorsForBlankRow**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#keepSeparatorsForBlankRow--) est une propriété booléenne. Pour garder les séparateurs pour les lignes vides lors de la conversion du fichier Excel en CSV, définissez la propriété [**TxtSaveOptions.keepSeparatorsForBlankRow**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#keepSeparatorsForBlankRow--) à **true**.  

Le code d'exemple suivant charge le [fichier Excel source](84378743.xlsx). Il définit la propriété [**TxtSaveOptions.keepSeparatorsForBlankRow**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#keepSeparatorsForBlankRow--) à **true** et le sauvegarde en tant que [output.csv](84378744.csv). La capture d'écran montre la comparaison entre le fichier Excel source, la sortie par défaut générée lors de la conversion en CSV, et la sortie générée en définissant [**TxtSaveOptions.keepSeparatorsForBlankRow**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#keepSeparatorsForBlankRow--) à **true**.  

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)  

## **Code d'exemple**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells TxtSaveOptions Example</title>
    </head>
    <body>
        <h1>TxtSaveOptions to CSV Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to CSV</button>
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

            // Create a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Instantiate TxtSaveOptions
            const options = new TxtSaveOptions();

            // Set KeepSeparatorsForBlankRow to true to show separators in blank rows
            options.keepSeparatorsForBlankRow = true;

            // Save the workbook to CSV using the options
            const outputData = workbook.save(SaveFormat.CSV, options);

            const blob = new Blob([outputData], { type: 'text/csv' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.csv';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download CSV File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File converted successfully! Click the download link to get the CSV file.</p>';
        });
    </script>
</html>
```

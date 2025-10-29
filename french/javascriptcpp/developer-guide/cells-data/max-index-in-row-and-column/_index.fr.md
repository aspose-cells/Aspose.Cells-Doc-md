---
title: Obtenir l indice de colonne maximal dans la ligne et l indice de ligne maximal dans la colonne
type: docs
weight: 600
url: /fr/javascript-cpp/get-max-index-in-row-and-column/
description: Apprenez à obtenir l indice de la colonne maximale dans une ligne et l indice de la ligne maximale dans une colonne via l API Aspose.Cells for JavaScript en C++.
keywords: Obtenez l indice de la colonne maximale dans une ligne en JavaScript via C++, Obtenez l indice de la ligne maximale dans une colonne en JavaScript via C++, Obtenez l indice de la colonne de données maximale dans une ligne en JavaScript via C++, Obtenez l indice de la ligne de données maximale dans une colonne en JavaScript via C++.
---

## **Scénarios d'utilisation possibles**
Lorsque vous avez seulement besoin de manipuler certaines données sur les lignes ou colonnes, vous devez connaître la plage de données des lignes et colonnes. Aspose.Cells for JavaScript via C++ offre cette fonctionnalité. Pour obtenir l'indice de la colonne maximum d'une ligne, vous pouvez utiliser les méthodes [**Row.lastCell**](https://reference.aspose.com/cells/javascript-cpp/row/#lastCell--) et [**Row.lastDataCell**](https://reference.aspose.com/cells/javascript-cpp/row/#lastDataCell--), puis utiliser la méthode [**Cell.column**](https://reference.aspose.com/cells/javascript-cpp/cell/#column--) pour obtenir l'indice de la colonne maximum et l'indice de la colonne de données maximum. Mais pour obtenir l'indice de la ligne maximum et l'indice de la ligne de données maximum d'une colonne, vous devez créer une plage sur la colonne, puis parcourir cette plage pour trouver la dernière cellule, et enfin appeler la méthode [**Cell.row**](https://reference.aspose.com/cells/javascript-cpp/cell/#row--) sur la cellule.

Aspose.Cells for JavaScript via C++ fournit les propriétés et méthodes suivantes pour vous aider à atteindre vos objectifs.
- [**Row.lastCell**](https://reference.aspose.com/cells/javascript-cpp/row/#lastCell--)
- [**Row.lastDataCell**](https://reference.aspose.com/cells/javascript-cpp/row/#lastDataCell--)
- [**Cell.column**](https://reference.aspose.com/cells/javascript-cpp/cell/#column--)
- [**Cell.row**](https://reference.aspose.com/cells/javascript-cpp/cell/#row--)

## **Obtenir l’indice de la colonne maximale dans une ligne et l’indice de la ligne maximale dans une colonne**
Cet exemple montre comment :

1. Charger le [fichier d'exemple](sample.xlsx).
1. Obtenir la ligne qui a besoin d'obtenir l'indice de colonne maximal et l'indice de colonne de données maximal.
1. Appeler la méthode [**Cell.column**](https://reference.aspose.com/cells/javascript-cpp/cell/#column--) sur la cellule.
1. Créez une plage basée sur la colonne.
1. Obtenez l'itérateur et parcourez la plage.
1. Appeler la méthode [**Cell.row**](https://reference.aspose.com/cells/javascript-cpp/cell/#row--) sur la cellule.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            #result pre { background: #f4f4f4; padding: 10px; }
            #downloadLink { display: none; margin-top: 10px; display: inline-block; }
        </style>
    </head>
    <body>
        <h1>Get Max Row/Column Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink">Download Result</a>
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
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const sheet = workbook.worksheets.get(0);

            // Accessing cells collection
            const cells = sheet.cells;

            // Check row at index 1
            const row = cells.checkRow(1);
            const outputLines = [];

            if (row != null) {
                // get Maximum column index of Row which contains data or style.
                outputLines.push("Max column index in row: " + row.lastCell.column);

                // get Maximum column index of Row which contains data.
                outputLines.push("Max data column index in row: " + row.lastDataCell.column);
            } else {
                outputLines.push("Row 1 is empty (checkRow returned null).");
            }

            // create the range of column B (index 1)
            const columnRange = cells.createRange(1, 1, true);

            var max_row_index  = cells.maxRow + 1;
            var maxRow = 0;
            var maxDataRow = 0;

            for (let row_index = 0; row_index < max_row_index; row_index++) {
                var curr_cell = cells.get(row_index, 1);

                if (curr_cell) {
                    if (curr_cell.stringValue) {
                        maxDataRow = curr_cell.row;
                    }

                    if (curr_cell.stringValue || curr_cell.hasCustomStyle) {
                        maxRow = curr_cell.row;
                    }
                }
            }

            // Maximum row index of Column which contains data or style.
            outputLines.push("Max row index in Column: " + maxRow);

            // Maximum row index of Column which contains data.
            outputLines.push("Max data row index in Column: " + maxDataRow);

            resultDiv.innerHTML = '<pre>' + outputLines.join('\n') + '</pre>';
        });
    </script>
</html>
```

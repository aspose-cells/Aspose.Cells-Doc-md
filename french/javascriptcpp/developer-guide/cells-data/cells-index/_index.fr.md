---
title: Obtenir l indice des cellules
type: docs
weight: 600
url: /fr/javascript-cpp/get-cells-index/
description: Apprenez comment obtenir une ligne ou une colonne par le nom de la ligne, de la colonne ou des cellules. Convertissez le nom de la cellule en indices de ligne et de colonne zéro basés en utilisant Aspose.Cells for JavaScript via C++.
keywords: Obtenir l index de la ligne et de la colonne par le nom de la cellule, obtenir l index de la colonne par le nom de la colonne, obtenir l index de la ligne par le nom de la ligne, obtenir l index par le nom de la cellule. 
---

{{% alert color="primary" %}}
La vue par défaut d'Excel est la référence de style A1, chaque colonne est définie comme A, B, C.... , et les cellules sont nommées A1, B2, C3... et ainsi de suite.
Vous pouvez vouloir savoir quelle est la ligne et la colonne de cette cellule.

{{% /alert %}}


## **Scénarios d'utilisation possibles**
Lorsque vous avez seulement besoin de manipuler des données spécifiques sur la feuille de calcul par index de ligne et de colonne, vous devez connaître les index de la colonne et de la ligne de cette cellule spécifique. 
Aspose.Cells for JavaScript via C++ offre cette fonctionnalité pour obtenir l'index de ligne et de colonne par le nom de la ligne, de la colonne et de la cellule. 
Aspose.Cells for JavaScript via C++ fournit les propriétés et méthodes suivantes pour vous aider à atteindre vos objectifs.
- [**CellsHelper.cellNameToIndex(string)**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#cellNameToIndex-string-)
- [**CellsHelper.columnIndexToName**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#columnIndexToName-number-)
- [**CellsHelper.columnNameToIndex**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#columnNameToIndex-string-)
- [**CellsHelper.rowIndexToName**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#rowIndexToName-number-)
- [**CellsHelper.rowNameToIndex**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#rowNameToIndex-string-)

Remarque : L'indexation est basée sur zéro dans Aspose.Cells for JavaScript via C++, mais l'ID de la ligne est basé sur 1 dans MS Excel.

## **Obtenir les indices des cellules en utilisant Aspose.Cells for JavaScript via C++**
Cet exemple montre comment :

1. Créer un classeur et ajouter des données.
1. Trouver la cellule spécifique dans la première feuille de calcul.
1. Obtenir l'index de ligne et l'index de colonne par le nom de la cellule.
1. Obtenir l'index de colonne par le nom de la colonne.
1. Obtenir l'index de ligne par le nom de la ligne.

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
        const { Workbook, SaveFormat, CellsHelper } = AsposeCells;

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

        document.getElementById('runExample').addEventListener('click', () => {
            // Create a new workbook
            const workbook = new Workbook();

            // Access cells of the first worksheet
            const cells = workbook.worksheets.get(0).cells;

            let cell = cells.get("A1");
            cell.putValue("Fruit");
            cell = cells.get("B1");
            cell.putValue("Count");
            cell = cells.get("C1");
            cell.putValue("Price");

            cell = cells.get("A2");
            cell.putValue("Apple");
            cell = cells.get("A3");
            cell.putValue("Mango");
            cell = cells.get("A4");
            cell.putValue("Blackberry");
            cell = cells.get("A5");
            cell.putValue("Cherry");

            cell = cells.get("B2");
            cell.putValue(5);
            cell = cells.get("B3");
            cell.putValue(3);
            cell = cells.get("B4");
            cell.putValue(6);
            cell = cells.get("B5");
            cell.putValue(4);

            cell = cells.get("C2");
            cell.putValue(5);
            cell = cells.get("C3");
            cell.putValue(20);
            cell = cells.get("C4");
            cell.putValue(30);
            cell = cells.get("C5");
            cell.putValue(60);

            // Find the cell containing "Blackberry"
            const curr = cells.find("Blackberry", null);

            // Current cell name
            const currentCellName = curr.name;

            // get row and column index of current cell
            const rowCol = CellsHelper.cellNameToIndex(curr.name);
            const currRow = rowCol[0];
            const currCol = rowCol[1];

            // get column name by column index
            const columnName = CellsHelper.columnIndexToName(currCol);

            // get row name by row index
            const rowName = CellsHelper.rowIndexToName(currRow);

            // get column index by column name
            const columnIndex = CellsHelper.columnNameToIndex(columnName);

            // get row index by row name
            const rowIndex = CellsHelper.rowNameToIndex(rowName);

            const outputs = [];
            outputs.push("Current Cell Name: " + currentCellName);
            outputs.push("Row Index: " + currRow + "  Column Index: " + currCol);
            outputs.push("Column Name: " + columnName + " Row Name: " + rowName);
            outputs.push("Column Index: " + columnIndex + " Row Index: " + rowIndex);
            outputs.push("columnIndex == currCol: " + (columnIndex == currCol));
            outputs.push("rowIndex == currRow: " + (rowIndex == currRow));

            document.getElementById('result').innerHTML = '<pre>' + outputs.join('\n') + '</pre>';

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';
        });
    </script>
</html>
```

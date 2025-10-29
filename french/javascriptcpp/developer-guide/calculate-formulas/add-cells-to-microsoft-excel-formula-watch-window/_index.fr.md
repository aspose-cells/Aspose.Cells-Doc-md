---
title: Ajouter des cellules à la fenêtre de surveillance des formules Excel avec JavaScript via C++
linktitle: Ajouter des cellules à la fenêtre de surveillance des formules Microsoft Excel
description: Comment utiliser la bibliothèque Aspose.Cells pour ajouter des cellules à la fenêtre de surveillance des formules dans Excel avec JavaScript via C++. En chargeant un fichier Excel existant ou en créant un nouveau, nous pouvons manipuler les cellules et définir des formules. Enfin, nous enregistrons le fichier Excel modifié sur le disque.
keywords: Aspose.Cells, Excel, fenêtre de surveillance des formules, cellules, ajout, JavaScript via C++
type: docs
weight: 60
url: /fr/javascript-cpp/add-cells-to-microsoft-excel-formula-watch-window/
---

## **Scénarios d'utilisation possibles**

La fenêtre de surveillance dans Microsoft Excel est un outil pratique pour suivre les valeurs des cellules et leurs formules dans une fenêtre. Vous pouvez ouvrir la *Fenêtre de surveillance* en utilisant Microsoft Excel en cliquant sur *Formules > Surveillance > Fenêtre*. Elle comporte un bouton *Ajouter une surveillance* qui permet d'ajouter des cellules pour inspection. De même, vous pouvez utiliser la méthode [**CellWatchCollection.add(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cellwatchcollection/#add-number-number-) pour ajouter des cellules à la *Fenêtre de surveillance* via l'API Aspose.Cells.

## **Ajouter des cellules à la fenêtre de surveillance des formules Microsoft Excel**

Le code d'exemple suivant définit la formule des cellules C1 et E1 et les ajoute toutes deux à la Fenêtre de surveillance. Ensuite, il enregistre le classeur en tant que [fichier Excel de sortie](67338481.xlsx). Si vous ouvrez le fichier Excel de sortie et visualisez la *Fenêtre de surveillance*, vous verrez les deux cellules comme illustré dans cette capture d'écran.

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **Code d'exemple**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Add Cells to Formula Watch Window</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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
            // This example creates a new workbook (like the original JavaScript example).
            // If a user-selected file is provided, it will be ignored for this specific example.
            if (!fileInput) {
                document.getElementById('result').innerHTML = '<p style="color: red;">File input not available.</p>';
                return;
            }

            // Instantiate a new empty workbook
            const wb = new Workbook();

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Put some integer values in cell A1 and A2
            ws.cells.get("A1").value = 10;
            ws.cells.get("A2").value = 30;

            // Access cell C1 and set its formula
            const c1 = ws.cells.get("C1");
            c1.formula = "=Sum(A1,A2)";

            // Add cell C1 into cell watches by name
            ws.cellWatches.add(c1.name);

            // Access cell E1 and set its formula
            const e1 = ws.cells.get("E1");
            e1.formula = "=A2*A1";

            // Add cell E1 into cell watches by its row and column indices
            ws.cellWatches.add(e1.row, e1.column);

            // Save workbook to output XLSX format and provide download link
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputAddCellsToMicrosoftExcelFormulaWatchWindow.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

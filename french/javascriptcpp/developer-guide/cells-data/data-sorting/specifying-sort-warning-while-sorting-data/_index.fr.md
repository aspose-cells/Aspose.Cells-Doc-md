---
title: Spécification d avertissement de tri lors du tri des données
type: docs
weight: 140
url: /fr/javascript-cpp/specifying-sort-warning-while-sorting-data/
description: Apprenez comment préciser l’avertissement de tri lors du tri des données en utilisant le script Aspose.Cells for Java en C++ API.
keywords: Ajouter un avertissement de tri lors du tri des données, définir un avertissement de tri lors du tri des données, sélectionner un avertissement de tri lors du tri des données.
---

## **Scénarios d'utilisation possibles**

Veuillez considérer ces données textuelles, c’est-à-dire {11, 111, 22}. Ces données sont triées parce qu’en termes de texte, 111 précède 22. Mais si vous souhaitez trier ces données non pas en tant que texte mais en tant que nombres, elles deviendront {11, 22, 111} car numériquement 111 vient après 22. Le script Aspose.Cells for Java en C++ fournit la propriété {0} pour gérer ce problème. Veuillez définir cette propriété à **true** et vos données textuelles seront triées comme des données numériques. La capture d’écran suivante montre l’avertissement de tri affiché par Microsoft Excel lorsque des données textuelles qui ressemblent à des données numériques sont triées.

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

## **Code d'exemple**

Le code d'exemple suivant illustre l'utilisation de la propriété [**DataSorter.sortAsNumber**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#sortAsNumber-boolean-) comme expliqué précédemment. Veuillez consulter son [fichier Excel d'exemple](43352075.xlsx) et son [fichier Excel de sortie](43352076.xlsx) pour plus d'aide.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Sort As Number Example</title>
    </head>
    <body>
        <h1>Sort As Number Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellsHelper, CellArea, SortOrder } = AsposeCells;

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

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Create your cell area.
            const ca = AsposeCells.CellArea.createCellArea("A1", "A20");

            // Create your sorter.
            const sorter = workbook.dataSorter;

            // Find the index for column A.
            const idx = CellsHelper.columnNameToIndex("A");

            // Add key in sorter, it will sort in Ascending order.
            sorter.addKey(idx, SortOrder.Ascending);

            // Set sort as number
            sorter.sortAsNumber = true;

            // Perform sort.
            sorter.sort(worksheet.cells, ca);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSortAsNumber.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Sort completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

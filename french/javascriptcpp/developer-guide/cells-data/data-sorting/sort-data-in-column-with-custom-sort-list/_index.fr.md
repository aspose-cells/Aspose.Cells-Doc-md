---
title: Trier les données dans une colonne avec une liste de tri personnalisée
type: docs
weight: 290
url: /fr/javascript-cpp/sort-data-in-column-with-custom-sort-list/
description: Apprenez comment trier les données dans la colonne en utilisant une liste personnalisée via le script Aspose.Cells for Java en C++ API.
keywords: Trier les données dans une colonne avec une liste de tri personnalisée, trier les données par liste personnalisée.
---

## **Scénarios d'utilisation possibles**

Vous pouvez trier des données dans une colonne à l'aide d'une liste personnalisée. Cela peut être fait en utilisant la méthode [**DataSorter.addKey**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#addKey-number-sortorder-string-). Cependant, cette méthode ne fonctionne que si les éléments de la liste personnalisée ne contiennent pas de virgules. Si elles contiennent des virgules comme "USA,US", "China,CN", vous devez utiliser la méthode [**DataSorter.addKey(number, SortOrder, string[])**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#addKey-number-sortorder-stringarray-). Ici, le dernier paramètre n'est pas une chaîne, mais un tableau de chaînes.

## **Trier les données dans une colonne avec une liste de tri personnalisée**

Le code d'exemple suivant explique comment utiliser la méthode [**DataSorter.addKey(number, SortOrder, string[])**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#addKey-number-sortorder-stringarray-) pour trier les données avec une liste de tri personnalisée. Veuillez voir le [fichier Excel d'exemple](50528327.xlsx) utilisé dans ce code et le [fichier Excel de sortie](50528328.xlsx) généré par celui-ci. La capture d'écran suivante montre l'effet du code sur le fichier Excel d'exemple lors de son exécution.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **Code d'exemple**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Custom Sort List</title>
    </head>
    <body>
        <h1>Custom Sort List Example</h1>
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

            // Instantiating a Workbook object from uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Specify cell area - sort from A1 to A40
            const ca = AsposeCells.CellArea.createCellArea("A1", "A40");

            // Create Custom Sort list
            const customSortList = ["USA,US", "Brazil,BR", "China,CN", "Russia,RU", "Canada,CA"];

            // Add Key for Column A, Sort it in Ascending Order with Custom Sort List
            wb.dataSorter.addKey(0, AsposeCells.SortOrder.Ascending, customSortList);

            wb.dataSorter.sort(ws.cells, ca);

            // Save the output Excel file
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSortData_CustomSortList.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Sorting completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

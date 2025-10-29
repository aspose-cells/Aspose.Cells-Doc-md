---
title: Formatter les cellules du tableau croisé dynamique
type: docs
weight: 30
url: /fr/javascript-cpp/format-pivot-table-cells/
description: Comment formater les cellules du tableau croisé dynamique avec Aspose.Cells for JavaScript via C++.
keywords: Formater les cellules du tableau croisé dynamique
---

{{% alert color="primary" %}}

Parfois, vous souhaitez formater les cellules du tableau croisé dynamique. Par exemple, vous souhaitez appliquer une couleur de fond aux cellules du tableau croisé dynamique. Aspose.Cells for JavaScript via C++ fournit deux méthodes [**PivotTable.formatAll(style)**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#formatAll-style-) et [**PivotTable.format(row, column, style)**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#format-number-number-style-), que vous pouvez utiliser à cet effet.

[**PivotTable.formatAll(style)**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#formatAll-style-) applique le style à l'ensemble du tableau croisé dynamique tandis que [**PivotTable.format(row, column, style)**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#format-number-number-style-) applique le style à une seule cellule du tableau croisé dynamique.

{{% /alert %}}
Le code d'exemple suivant charge le [fichier Excel d'exemple](pivot_format.xlsx) contenant deux tableaux croisés dynamiques, et réalise l'opération de mise en forme de l'ensemble du tableau croisé dynamique et de mise en forme des cellules individuelles dans le tableau croisé dynamique.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Pivot Table Formatting Example</title>
    </head>
    <body>
        <h1>Pivot Table Formatting Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm" />
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

            // Access the worksheet by its name
            const worksheet = workbook.worksheets.get("Sheet1");

            // Access the pivot table (second pivot table, index 1)
            const pivotTable = worksheet.pivotTables.get(1);

            // Create a style object with background color light blue
            const style = workbook.createStyle();
            style.pattern = AsposeCells.BackgroundType.Solid;
            style.backgroundColor = AsposeCells.Color.LightBlue;

            // Format entire pivot table with light blue color
            pivotTable.formatAll(style);

            // Create another style object with yellow color
            const style2 = workbook.createStyle();
            style2.pattern = AsposeCells.BackgroundType.Solid;
            style2.backgroundColor = AsposeCells.Color.Yellow;

            // Access the first pivot table (index 0)
            const pivotTable2 = worksheet.pivotTables.get(0);

            // Format the cell of pivot table at row 16, column 5 (0-based indices)
            pivotTable2.format(16, 5, style2);

            // Saving the workbook object and preparing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Pivot tables formatted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## Articles Connexes

- [Formatage du tableau croisé dynamique](/cells/fr/javascript-cpp/formatting-pivot-table/)
- [Travailler avec les formats d'affichage des données de DataField dans le tableau croisé dynamique](/cells/fr/javascript-cpp/working-with-data-display-formats-of-datafield-in-pivot-table/)

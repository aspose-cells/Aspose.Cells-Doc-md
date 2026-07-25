---
title: Définir l option du tableau croisé dynamique  Afficher les cellules vides
type: docs
weight: 40
url: /fr/javascript-cpp/setting-pivot-table-option-for-empty-cells-show/
---

{{% alert color="primary" %}}

Vous pouvez définir différentes options de tableau croisé dynamique en utilisant Aspose.Cells for JavaScript via C++. L'une de ces options est "Pour les cellules vides, afficher". En réglant cette option, toutes les cellules vides d'un tableau croisé dynamique sont affichées sous forme d'une chaîne spécifiée.

{{% /alert %}}

## **Définition de l'option de tableau croisé dynamique dans Microsoft Excel**

Pour trouver et définir cette option dans Microsoft Excel :

1. Sélectionnez un tableau croisé dynamique et faites un clic droit.
1. Sélectionnez **Options du tableau croisé dynamique**.
1. Sélectionnez l'onglet **Mise en page et format**.
1. Sélectionnez l'option **Afficher pour les cellules vides** et spécifiez une chaîne.

## **Configuration des options du tableau croisé dynamique à l'aide de Aspose.Cells for JavaScript via C++**

Aspose.Cells for JavaScript via C++ fournit les propriétés [**PivotTable.displayNullString**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#displayNullString-boolean-) et [**PivotTable.nullString**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#nullString-string-) pour définir l'option "Pour les cellules vides, afficher" du tableau croisé dynamique.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells PivotTable Update Example</title>
    </head>
    <body>
        <h1>Update PivotTable Null Display Example</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            await AsposeCells.onReady();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet and its first pivot table
            const worksheet = workbook.worksheets.get(0);
            const pt = worksheet.pivotTables.get(0);

            // Indicating if or not display the empty cell value
            pt.displayNullString = true;
            // Indicating the null string
            pt.nullString = "null";

            // Recalculate pivot table data
            pt.calculateData();

            // Do not refresh data on opening file
            pt.refreshDataOnOpeningFile = false;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Pivot table updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## Articles Connexes

- [Formatage du tableau croisé dynamique](/cells/fr/javascript-cpp/formatting-pivot-table/)

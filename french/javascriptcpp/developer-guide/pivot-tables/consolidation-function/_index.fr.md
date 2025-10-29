---
title: Fonction de consolidation
type: docs
weight: 20
url: /fr/javascript-cpp/consolidation-function/
description: Comment appliquer la fonction de consolidation aux champs de données du tableau croisé dynamique en utilisant Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells for JavaScript via C++ Excel, bibliothèque JavaScript Excel, fonction de consolidation aux champs de données du tableau croisé dynamique en utilisant Aspose.Cells for JavaScript via C++ Excel Library.
---

## **Fonction de consolidation**

Aspose.Cells for JavaScript via C++ peut être utilisé pour appliquer la fonction de consolidation aux champs de données (ou champs de valeur) du tableau croisé dynamique. Dans Microsoft Excel, vous pouvez cliquer avec le bouton droit sur le champ de valeur puis sélectionner l’option **Paramètres du champ de valeur...** puis aller à l’onglet **Résumer les valeurs par**. À partir de là, vous pouvez choisir n’importe quelle fonction de consolidation comme Somme, Comptage, Moyenne, Max, Min, Produit, Comptage distinct, etc.

L’enumération [**ConsolidationFunction**](https://reference.aspose.com/cells/javascript-cpp/consolidationfunction/) de Aspose.Cells for JavaScript via C++ supporte les fonctions de consolidation suivantes.

- ConsolidationFunction.Average
- ConsolidationFunction.Count
- ConsolidationFunction.CountNums
- ConsolidationFunction.DistinctCount
- ConsolidationFunction.Max
- ConsolidationFunction.Min
- ConsolidationFunction.Product
- ConsolidationFunction.StdDev
- ConsolidationFunction.StdDevp
- ConsolidationFunction.Sum
- ConsolidationFunction.Var
- ConsolidationFunction.Varp

## **Comment appliquer la fonction de consolidation aux champs de données du tableau croisé dynamique en utilisant Aspose.Cells for JavaScript via C++**

Le code suivant applique la fonction de consolidation **Moyenne** au premier champ de données (ou champ de valeur) et la fonction de consolidation **Nombre distinct** au deuxième champ de données (ou champ de valeur).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - PivotTable Consolidation Function</title>
    </head>
    <body>
        <h1>Apply Consolidation Function to PivotTable</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet of the workbook
            const worksheet = workbook.worksheets.get(0);

            // Access the first pivot table of the worksheet
            const pivotTable = worksheet.pivotTables.get(0);

            // Apply Average consolidation function to first data field
            pivotTable.dataFields.get(0).function = AsposeCells.ConsolidationFunction.Average;

            // Apply DistinctCount consolidation function to second data field
            pivotTable.dataFields.get(1).function = AsposeCells.ConsolidationFunction.DistinctCount;

            // Calculate the data to make changes affect
            pivotTable.calculateData();

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PivotTable consolidation functions applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

La fonction de consolidation DISTINCT_COUNT est prise en charge uniquement par Microsoft Excel 2013.

{{% /alert %}}

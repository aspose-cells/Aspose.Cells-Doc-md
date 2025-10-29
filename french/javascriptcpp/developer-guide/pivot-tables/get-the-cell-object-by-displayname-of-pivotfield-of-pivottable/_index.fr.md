---
title: Obtenez l objet Cell par le nom d affichage du champ de tableau croisé dynamique du tableau croisé dynamique
type: docs
weight: 70
url: /fr/javascript-cpp/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/
description: Comment obtenir l’objet Cell par DisplayName du PivotField du PivotTable avec Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells for JavaScript via C++ Excel, bibliothèque JavaScript Excel, Obtenir l’objet Cell par DisplayName du PivotField du PivotTable en utilisant Aspose.Cells for JavaScript via C++ Excel Library.
---

{{% alert color="primary" %}}

Aspose.Cells for JavaScript via C++ fournit la méthode [**PivotTable.cellByDisplayName(string)**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#cellByDisplayName-string-) que vous pouvez utiliser pour accéder à l’objet cellule par le nom d’affichage du champ pivot. Cette méthode est utile lorsque vous souhaitez mettre en évidence ou formater l’en-tête de votre champ pivot. Cet article explique comment récupérer l’objet cellule par le nom d’affichage du champ de données, puis appliquer un format.

{{% /alert %}}

## **Comment obtenir l'objet Cell par le nom d'affichage du champ de tableau croisé dynamique du tableau croisé dynamique**

Le code suivant accède au premier tableau croisé dynamique de la feuille de calcul, puis obtient la cellule par le nom d'affichage du deuxième champ de données du tableau croisé dynamique. Il change ensuite la couleur de remplissage et la couleur de la police de la cellule en bleu clair et noir respectivement. Les captures d'écran ci-dessous montrent à quoi ressemble le tableau croisé dynamique avant et après l'exécution du code.

|**Tableau croisé dynamique - Avant**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_1.png)|

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Pivot Table Cell Styling Example</h1>
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
            const resultDiv = document.getElementById('result');
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first pivot table inside the worksheet
            const pivotTable = worksheet.pivotTables.get(0);

            // Access cell by display name of 2nd data field of the pivot table
            const dataFieldDisplayName = pivotTable.dataFields.get(1).displayName;
            const cell = pivotTable.cellByDisplayName(dataFieldDisplayName);

            // Access cell style and set its fill color and font color
            const style = cell.style;
            style.foregroundColor = AsposeCells.Color.LightBlue;
            style.font.color = AsposeCells.Color.Black;

            // Set the style of the cell
            pivotTable.format(cell.row, cell.column, style);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

|**Tableau croisé dynamique - Après**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_2.png)|

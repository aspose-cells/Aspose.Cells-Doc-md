---
title: Afficher la plage de cellules comme étiquettes de données avec JavaScript via C++
linktitle: Afficher la plage de cellules en tant qu étiquettes de données
description: Découvrez comment afficher une plage de cellules en tant qu’étiquettes de données dans les graphiques en utilisant Aspose.Cells for JavaScript via C++. Notre guide vous montrera comment lier les étiquettes à votre source de données et les formater pour fournir des informations précises et significatives dans vos graphiques.
keywords: Aspose.Cells for JavaScript via C++, création de graphiques, étiquettes de données, plage de cellules, source de données, mise en forme, précision, informations significatives.
type: docs
weight: 130
url: /fr/javascript-cpp/showing-cell-range-as-the-data-labels/
---

{{% alert color="primary" %}}
 Dans Microsoft Excel 2013, vous pouvez afficher une plage de cellules pour les étiquettes de données. Aspose.Cells for JavaScript via C++ supporte cette fonctionnalité.
{{% /alert %}}

## **Case à cocher pour afficher la plage de cellules en tant qu'étiquettes de données**

Pour afficher la plage de cellules en tant qu'étiquettes de données dans Microsoft Excel :

1. Sélectionnez les étiquettes de données de la série et cliquez avec le bouton droit pour ouvrir le menu contextuel.  
1. Sélectionnez **Format des étiquettes de données**. Les options d'étiquetage sont affichées.  
1. Sélectionnez ou désélectionnez l'option **L'étiquette contient - Valeur à partir des cellules**.  

Le code d'exemple ci-dessous accède aux étiquettes de données d'une série de graphique et définit la propriété [**DataLabels.showCellRange**](https://reference.aspose.com/cells/javascript-cpp/datalabels/#showCellRange--) sur **true** pour sélectionner l'option **Label Contains - Value From Cells**.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Show Range in Data Labels</title>
    </head>
    <body>
        <h1>Show Range in Data Labels Example</h1>
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

            // Create workbook from the source Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the chart inside the worksheet
            const chart = worksheet.charts.get(0);

            // Check the "Label Contains - Value From Cells"
            const dataLabels = chart.nSeries.get(0).dataLabels;
            dataLabels.showCellRange = true;

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

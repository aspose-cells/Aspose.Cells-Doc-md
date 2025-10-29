---
title: Désactiver le retour à la ligne du texte pour les étiquettes de données du graphique avec JavaScript via C++
description: Apprenez à désactiver le retour à la ligne du texte pour les étiquettes de données dans les graphiques en utilisant Aspose.Cells for JavaScript via C++. Notre guide vous montrera comment empêcher les longues étiquettes de se chevaucher et offrir des affichages de graphique plus lisibles et clairs.
keywords: Aspose.Cells for JavaScript via C++, graphique, étiquettes de données, retour à la ligne du texte, chevauchement, lisibilité, affichages.
type: docs
weight: 70
url: /fr/javascript-cpp/disable-text-wrapping-for-data-labels-of-the-chart/
---

{{% alert color="primary" %}}

Microsoft Excel 2013 permet aux utilisateurs de mettre en forme ou de défaire le retour à la ligne à l'intérieur des étiquettes de données du graphique. Par défaut, le texte à l'intérieur des étiquettes de données du graphique est à l'état de retour à la ligne.

Aspose.Cells fournit une propriété [**DataLabels.isTextWrapped()**](https://reference.aspose.com/cells/javascript-cpp/datalabels/#isTextWrapped--) que vous pouvez définir sur vrai ou faux pour activer ou désactiver respectivement le retour à la ligne du texte des étiquettes de données.

{{% /alert %}}

L'exemple de code ci-dessous montre comment désactiver le retour à la ligne pour les étiquettes de données du graphique.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Disable Data Label Text Wrapping</h1>
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

            // Instantiating a Workbook object by loading uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the first chart inside the worksheet
            const chart = worksheet.charts.get(0);

            // Disable the Text Wrapping of Data Labels in all Series
            chart.nSeries.get(0).dataLabels.isTextWrapped = false;
            chart.nSeries.get(1).dataLabels.isTextWrapped = false;
            chart.nSeries.get(2).dataLabels.isTextWrapped = false;

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

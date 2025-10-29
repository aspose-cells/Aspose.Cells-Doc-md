---
title: Étiquette de données personnalisée en texte enrichi du point de graphique avec JavaScript via C++
description: Découvrez comment ajouter des étiquettes de données personnalisées en texte enrichi aux points de graphique dans Aspose.Cells for JavaScript via C++. Notre guide vous montrera comment formater les étiquettes avec différentes polices, couleurs et options d’alignement pour améliorer l’apparence et la lisibilité de vos graphiques.
keywords: Aspose.Cells for JavaScript via C++, création de graphiques, texte enrichi, étiquettes de données personnalisées, polices, couleurs, alignement, apparence, lisibilité.
type: docs
weight: 10
url: /fr/javascript-cpp/rich-text-custom-data-label-of-chart-point/
---

{{% alert color="primary" %}}

Vous pouvez utiliser Aspose.Cells pour créer des étiquettes de données personnalisées en texte enrichi pour les points du graphique. Aspose.Cells propose la méthode [**ChartTextFrame.characters(number, number)**](https://reference.aspose.com/cells/javascript-cpp/charttextframe/#characters-number-number-) pour retourner l'objet [**FontSetting**](https://reference.aspose.com/cells/javascript-cpp/fontsetting) qui peut être utilisé pour définir les propriétés de police du texte comme sa couleur, sa graisse, etc.

{{% /alert %}}

## Étiquette de données personnalisée en texte enrichi du point du graphique

Le code suivant accède au premier point du graphique de la première série, définit son texte, puis définit la police des 10 premiers caractères en réglant leur couleur en rouge et leur graisse à **true**.

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

            // Creating a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the first chart inside the sheet
            const chart = worksheet.charts.get(0);

            // Access the data label of first series first point
            const dlbls = chart.nSeries.get(0).points.get(0).dataLabels;

            // Set data label text
            dlbls.text = "Rich Text Label";

            // Set the font setting of the first 10 characters
            const fntSetting = dlbls.characters(0, 10);
            const font = fntSetting.font;
            font.color = AsposeCells.Color.Red;
            font.isBold = true;

            // Save the workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Data label updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

---
title: Ajouter un filigrane WordArt au graphique avec JavaScript via C++
linktitle: Ajouter un filigrane WordArt au graphique
description: Apprenez comment utiliser Aspose.Cells for JavaScript via C++ pour ajouter un filigrane WordArt à un graphique dans Microsoft Excel. Notre guide montrera comment créer et positionner un filigrane WordArt pour améliorer l aspect visuel et l unicité de votre graphique.
keywords: Aspose.Cells for JavaScript, Filigrane WordArt, Filigrane de graphique, Microsoft Excel, Attrait visuel, Unicité du graphique.
type: docs
weight: 50
url: /fr/javascript-cpp/add-wordart-watermark-to-chart/
---

{{% alert color="primary" %}}  

Vous pouvez utiliser WordArt pour ajouter des effets spéciaux de texte aux feuilles de calcul. Par exemple, étirer un titre, décorer du texte, faire en sorte que le texte s'adapte à une forme prédéfinie, ou appliquer le texte affecté à la zone de traçage d'un graphique comme filigrane. Le WordArt devient un objet que vous pouvez déplacer ou positionner dans vos feuilles de calcul pour ajouter des décorations.  

L'exemple suivant montre comment ajouter une forme WordArt en filigrane pour la zone de traçage du graphique.  

{{% /alert %}}  

L'exemple suivant montre comment ajouter une forme WordArt en filigrane pour la zone de traçage d'un graphique existant.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Add WordArt Watermark to Chart</h1>
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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet's first chart
            const chart = workbook.worksheets.get(0).charts.get(0);

            // Add a WordArt watermark (shape) to the chart's plot area
            const wordart = chart.shapes.addTextEffectInChart(AsposeCells.MsoPresetTextEffect.TextEffect2,
                "CONFIDENTIAL", "Arial Black", 66, false, false, 1200, 500, 2000, 3000);

            // Get the shape's fill format and set transparency
            const wordArtFormat = wordart.fill;
            wordArtFormat.transparency = 0.9;

            // Get the line format and set weight to invisible (0.0)
            const lineFormat = wordart.line;
            lineFormat.weight = 0.0;

            // Save the modified workbook to a downloadable file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">WordArt watermark added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

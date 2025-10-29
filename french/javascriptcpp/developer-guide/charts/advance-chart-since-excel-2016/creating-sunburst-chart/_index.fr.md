---
title: Comment créer un graphique Sunburst avec JavaScript via C++
linktitle: Comment créer un diagramme en cercles emboîtés
description: Apprenez à créer un graphique Sunburst en Aspose.Cells for JavaScript via C++, un graphique qui présente des données en cercle. Notre guide vous aidera à configurer diverses propriétés et formats de votre graphique, y compris les étiquettes de données, légendes, couleurs, et plus.
keywords: Aspose.Cells for JavaScript via C++, graphique Sunburst, créer, définir les propriétés, étiquettes de données, légende, format, couleur, cercle, rendu de données.
type: docs
weight: 162
url: /fr/javascript-cpp/creating-sunburst-chart/
---

## **Scénarios d'utilisation possibles**
Les graphiques en treemap sont efficaces pour comparer les proportions au sein de la hiérarchie ; cependant, les graphiques en treemap ne sont pas idéaux pour montrer les niveaux hiérarchiques entre les plus grandes catégories et chaque point de données. Un graphique en rayon de soleil est beaucoup plus adapté pour cela. Le graphique en rayon de soleil est idéal pour afficher des données hiérarchiques. Chaque niveau de la hiérarchie est représenté par un anneau ou un cercle, le cercle le plus intérieur étant le sommet de la hiérarchie. Un graphique en rayon de soleil sans données hiérarchiques (un seul niveau de catégories) ressemble à un graphique en anneau. Cependant, un graphique en rayon de soleil avec plusieurs niveaux de catégories montre comment les anneaux extérieurs se rapportent aux anneaux intérieurs. Le graphique en rayon de soleil est le plus efficace pour montrer comment un anneau est divisé en ses parties contributives, alors qu'un autre type de graphique hiérarchique, le graphique en treemap, est idéal pour comparer les tailles relatives.

![todo:image_alt_text](sample.png)
## **Diagramme sunburst**
Après avoir exécuté le code ci-dessous, vous verrez le diagramme sunburst comme indiqué ci-dessous.

![todo:image_alt_text](result.png)
## **Code d'exemple**
Le code d'exemple suivant charge le [fichier Excel d'exemple](sunburst.xlsx) et génère le [fichier Excel de sortie](out.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Sunburst Chart Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Sunburst Chart Example</h1>
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

            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const worksheet = workbook.worksheets.get(0);

            const pieIdx = worksheet.charts.add(AsposeCells.ChartType.Sunburst, 5, 6, 25, 12);
            const chart = worksheet.charts.get(pieIdx);

            chart.showLegend = true;
            chart.title.text = "Sunburst Chart";
            chart.nSeries.add("D2:D16", true);
            chart.nSeries.categoryData = "A2:C16";
            chart.nSeries.get(0).dataLabels.showCategoryName = true;
            chart.plotArea.area.fillFormat.fillType = AsposeCells.FillType.None;

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Sunburst chart created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

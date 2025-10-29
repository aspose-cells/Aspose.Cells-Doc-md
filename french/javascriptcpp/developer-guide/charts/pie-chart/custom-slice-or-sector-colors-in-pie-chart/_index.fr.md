---
title: Couleurs personnalisées pour tranches ou secteurs dans un graphique à secteurs avec JavaScript via C++
linktitle: Couleurs personnalisées de tranche ou de secteur dans le diagramme circulaire
description: Apprenez comment utiliser Aspose.Cells for JavaScript via C++ pour personnaliser les couleurs des tranches et des secteurs dans un graphique à secteurs. Notre guide montrera comment attribuer des couleurs uniques à chaque tranche, secteur ou légion pour une meilleure apparence visuelle et représentation des données.
keywords: Aspose.Cells for JavaScript via C++, Graphique à secteurs, Couleurs personnalisées pour tranches, Couleurs de secteur personnalisées, Attraction visuelle, Représentation des données.
type: docs
weight: 60
url: /fr/javascript-cpp/custom-slice-or-sector-colors-in-pie-chart/
---

{{% alert color="primary" %}}

Cet article explique comment ajouter des couleurs personnalisées aux tranches/secteurs d'un diagramme circulaire. Par défaut, les diagrammes circulaires utilisent le modèle par défaut de Microsoft Excel. Pour utiliser d'autres couleurs, redéfinissez les couleurs dans le diagramme.

{{% /alert %}}

Pour définir une couleur personnalisée pour les tranches ou secteurs individuels d'un diagramme circulaire :

1. Accédez à l’objet [**Series**](https://reference.aspose.com/cells/javascript-cpp/series)’s [**ChartPoint**](https://reference.aspose.com/cells/javascript-cpp/chartpoint).
1. Attribuez la couleur de votre choix en utilisant la propriété [**ChartPoint.foregroundColor**](https://reference.aspose.com/cells/javascript-cpp/area/#foregroundColor--).

Cet article explique également comment :

- Les données de catégorie d'un graphique.
- Un titre de graphique lié à une cellule.
- Les paramètres de police du titre du graphique.
- La position de la légende.

{{% alert color="primary" %}}

[**ChartPoint.foregroundColor**](https://reference.aspose.com/cells/javascript-cpp/area/#foregroundColor--) n'est pas spécifique aux diagrammes circulaires mais peut être utilisé pour tous les types de diagrammes.

{{% /alert %}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Pie Chart Example</h1>
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

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Put the sample values used in a pie chart
            worksheet.cells.get("C3").value = "India";
            worksheet.cells.get("C4").value = "China";
            worksheet.cells.get("C5").value = "United States";
            worksheet.cells.get("C6").value = "Russia";
            worksheet.cells.get("C7").value = "United Kingdom";
            worksheet.cells.get("C8").value = "Others";

            // Put the sample values used in a pie chart
            worksheet.cells.get("D2").value = "% of world population";
            worksheet.cells.get("D3").value = 25;
            worksheet.cells.get("D4").value = 30;
            worksheet.cells.get("D5").value = 10;
            worksheet.cells.get("D6").value = 13;
            worksheet.cells.get("D7").value = 9;
            worksheet.cells.get("D8").value = 13;

            // Create a pie chart with desired length and width
            const pieIdx = worksheet.charts.add(AsposeCells.ChartType.Pie, 1, 6, 15, 14);

            // Access the pie chart
            const pie = worksheet.charts.get(pieIdx);

            // Set the pie chart series
            pie.nSeries.add("D3:D8", true);

            // Set the category data
            pie.nSeries.categoryData = "=Sheet1!$C$3:$C$8";

            // Set the chart title that is linked to cell D2
            pie.title.linkedSource = "D2";

            // Set the legend position at the bottom.
            pie.legend.position = AsposeCells.LegendPositionType.Bottom;

            // Set the chart title's font name and color
            pie.title.font.name = "Calibri";
            pie.title.font.size = 18;

            // Access the chart series
            const srs = pie.nSeries.get(0);

            // Color the individual points with custom colors
            srs.points.get(0).area.foregroundColor = new AsposeCells.Color(0, 246, 22, 219);
            srs.points.get(1).area.foregroundColor = new AsposeCells.Color(0, 51, 34, 84);
            srs.points.get(2).area.foregroundColor = new AsposeCells.Color(0, 46, 74, 44);
            srs.points.get(3).area.foregroundColor = new AsposeCells.Color(0, 19, 99, 44);
            srs.points.get(4).area.foregroundColor = new AsposeCells.Color(0, 208, 223, 7);
            srs.points.get(5).area.foregroundColor = new AsposeCells.Color(0, 222, 69, 8);

            // Autofit all columns
            worksheet.autoFitColumns();

            // Saving the modified Excel file and offering download
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

---
title: X axel vs. Kat.axel med JavaScript via C++
linktitle: X axel vs. Kategori axel
description: Lär dig att skilja mellan X axeln och Kat.axeln i Aspose.Cells for JavaScript via C++. Vår guide hjälper dig att förstå skillnaderna i deras användning och egenskaper, samt hur du konfigurerar dem enligt dina behov.
keywords: Aspose.Cells for JavaScript via C++, X axel, Kat.axel, skillnad, användning, egenskaper, konfiguration.
type: docs
weight: 180
url: /sv/javascript-cpp/X-axis-vs-category-axis/
---

## **Möjliga användningsscenario**
Det finns olika typer av X-axlar. Medan Y-axeln är en Värde typ axel kan X-axeln vara en Kategori typ axel eller en Värde typ axel. Genom att använda en Värde-axel behandlas datan som kontinuerligt varierande numerisk data, och markören placeras vid en punkt längs axeln som varierar enligt dess numeriska värde. Genom att använda en Kategori-axel behandlas datan som en följd av icke-numeriska textetiketter, och markören placeras vid en punkt längs axeln enligt dess position i följden. Exemplet nedan illustrerar skillnaden mellan Värde- och Kategori-axlar.
Vår provdata visas i [provtabellfilen](sample.png) nedan. Den första kolumnen innehåller våra X-axeldata, som kan behandlas som Kategorier eller som Värden. Observera att siffrorna inte är jämnt fördelade, och de förekommer inte ens i numerisk ordning.

![todo:image_alt_text](sample.png)
## **Hantera X- och Kategori-axeln som i Microsoft Excel**
Vi kommer visa denna data på två typer av diagram, det första är XY (Scatter) diagram med X som värdeaxel, det andra är linjediagram med X som kategorilänk.

![todo:image_alt_text](compare.png)
## **Exempelkod**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Charts and X Axis</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType, LegendPositionType, FillType, Utils } = AsposeCells;

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

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            // Access the first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Put the sample values used in charts
            worksheet.cells.get("A2").putValue(1);
            worksheet.cells.get("A3").putValue(3);
            worksheet.cells.get("A4").putValue(2.5);
            worksheet.cells.get("A5").putValue(3.5);
            worksheet.cells.get("B1").putValue("Cats");
            worksheet.cells.get("C1").putValue("Dogs");
            worksheet.cells.get("D1").putValue("Fishes");
            worksheet.cells.get("B2").putValue(7);
            worksheet.cells.get("B3").putValue(6);
            worksheet.cells.get("B4").putValue(5);
            worksheet.cells.get("B5").putValue(4);
            worksheet.cells.get("C2").putValue(7);
            worksheet.cells.get("C3").putValue(5);
            worksheet.cells.get("C4").putValue(4);
            worksheet.cells.get("C5").putValue(3);
            worksheet.cells.get("D2").putValue(8);
            worksheet.cells.get("D3").putValue(7);
            worksheet.cells.get("D4").putValue(3);
            worksheet.cells.get("D5").putValue(2);

            // Create Line Chart: X as Category Axis
            let pieIdx = worksheet.charts.add(ChartType.LineWithDataMarkers, 6, 15, 20, 21);
            // Retrieve the Chart object
            let chart = worksheet.charts.get(pieIdx);
            // Add Series
            chart.nSeries.add("B2:D5", true);
            // Set the category data
            chart.nSeries.categoryData = "=Sheet1!$A$2:$A$5";
            // Set the first series name
            chart.nSeries.get(0).name = "Cats";
            // Set the second series name
            chart.nSeries.get(1).name = "Dogs";
            // Set the third series name
            chart.nSeries.get(2).name = "Fishes";
            // Set the Legend at the bottom of the chart area
            chart.legend.position = LegendPositionType.Bottom;
            // Fill the PlotArea area with nothing 
            chart.plotArea.area.fillFormat.fillType = FillType.None;

            // Create XY (Scatter) Chart: X as Value Axis
            pieIdx = worksheet.charts.add(ChartType.ScatterConnectedByLinesWithDataMarker, 6, 6, 20, 12);
            // Retrieve the Chart object
            chart = worksheet.charts.get(pieIdx);
            // Add Series
            chart.nSeries.add("B2:D5", true);
            // Set X values for series 
            chart.nSeries.get(0).xValues = "{1,3,2.5,3.5}";
            chart.nSeries.get(1).xValues = "{1,3,2.5,3.5}";
            chart.nSeries.get(2).xValues = "{1,3,2.5,3.5}";
            // Set the first series name
            chart.nSeries.get(0).name = "Cats";
            // Set the second series name
            chart.nSeries.get(1).name = "Dogs";
            // Set the third series name
            chart.nSeries.get(2).name = "Fishes";
            // Set the Legend at the bottom of the chart area
            chart.legend.position = LegendPositionType.Bottom;
            // Fill the PlotArea area with nothing 
            chart.plotArea.area.fillFormat.fillType = FillType.None;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'XAxis.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

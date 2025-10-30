---
title: Skapa ett High Low Close (HLC) aktiediagram med JavaScript via C++
linktitle: Skapa High Low Close (HLC) Stock Chart
description: Lär dig hur du skapar ett High Low Close aktiediagram med Aspose.Cells for JavaScript via C++. Vår steg för steg guide visar hur du ritar aktiemarknadsdata, inklusive högsta, lägsta och stängningspriser, på ett diagram för bättre analys och visualisering.
keywords: Aspose.Cells for JavaScript via C++, High Low Close aktiediagram, aktiemarknadsdata, analys, visualisering.
type: docs
weight: 181
url: /sv/javascript-cpp/create-high-low-close-stock-chart/
---

## **Möjliga användningsscenario**  
 High-Low-Close (HLC) aktiediagram använder fyra kolumner av data. Den första kolumnen är en kategori, oftast ett datum men aktie namn kan också användas. Nästa tre kolumner är för höga, låga och stängningspriser. Prisintervallet för varje kategori indikeras av en vertikal linje från lågt till högt, och stängningspriset visas med ett tickmärke som sträcker sig till höger om denna linje.  

![todo:image_alt_text](sample.png)  
## **Synlighetsförbättringar i diagrammet**  
Ibland, för att göra diagrammet mer intuitivt, kan vi ändra utseendet på markören (stäng) eller få den att visas på den sekundära axeln.  

![todo:image_alt_text](sample2.png)  
## **Exempelkod**  
Följande exempelkod laddar [exempel Excel-filen](High-Low-Close.xlsx) och genererar [utdatamappar Excel-filen](out.xlsx).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>High-Low-Close Stock Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Create an instance of Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Create High-Low-Close-Stock Chart
            const pieIdx = worksheet.charts.add(AsposeCells.ChartType.StockHighLowClose, 5, 6, 20, 12);

            // Retrieve the Chart object
            const chart = worksheet.charts.get(pieIdx);

            // Set the legend can be showed
            chart.showLegend = true;

            // Set the chart title name 
            chart.title.text = "High-Low-Close Stock";

            // Set the Legend at the bottom of the chart area
            chart.legend.position = AsposeCells.LegendPositionType.Bottom;

            // Set data range (range and orientation)
            chart.chartDataRange = ["A1:D9", true];

            // Set category data 
            chart.nSeries.categoryData = "A2:A9";

            // Set the marker with the built-in data for the 3rd series (index 2)
            const series2 = chart.nSeries.get(2);
            const marker = series2.marker;
            marker.markerStyle = AsposeCells.ChartMarkerType.Dash;
            marker.markerSize = 20;
            marker.area.formatting = AsposeCells.FormattingType.Custom;
            marker.area.foregroundColor = AsposeCells.Color.Maroon;

            // Fill the PlotArea area with nothing 
            chart.plotArea.area.fillFormat.fillType = AsposeCells.FillType.None;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

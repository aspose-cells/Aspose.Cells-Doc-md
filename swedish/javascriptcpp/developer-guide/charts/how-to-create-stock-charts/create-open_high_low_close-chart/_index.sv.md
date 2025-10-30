---
title: Skapa ett öppet hög låg stäng (OHLC) aktiediagram med JavaScript via C++
description: Lär dig hur du skapar ett öppet hög låg stäng aktiediagram med Aspose.Cells for JavaScript via C++. Vår guide visar hur man ritar aktiemarknadsdata, inklusive öppnings , högsta , lägsta och stängningspriser, på ett diagram för bättre analys och visualisering.
keywords: Aspose.Cells for JavaScript via C++, Öppet Hög Låg Stäng aktiediagram, aktiemarknadsdata, analys, visualisering.
type: docs
weight: 182
url: /sv/javascript-cpp/create-open-high-low-close-stock-chart/
---

## **Möjliga användningsscenario**
Det öppen-hög-låg-stänga (OHLC) diagrammet använder fem datakolumner, i ordning: kategori, öppen, hög, låg och stänga. Prisintervallet i varje kategori indikeras igen av en vertikal linje, medan intervallet mellan öppen och stänga ges av en bredare stångformad stapel; om priset ökar i kategorin (stänga är högre än öppen), fylls stapeln med en färg, medan om priset minskar, fylls stapeln med en annan färg. Den här typen av diagram kallas ofta ett ljusstakdiagram.

![todo:image_alt_text](data.png)

![todo:image_alt_text](sample.png)
## **Synlighetsförbättringar i diagrammet**
Vi använder ofta färger snarare än svart och vitt för att indikera ökande och minskande priser. I den första uppsättningen av candlesticks nedan visar rött stigande priser och grönt fallande priser.

![todo:image_alt_text](sample2.png)
## **Exempelkod**
Följande exempelkod laddar den [exempelfil för Excel](Open-High-Low-Close.xlsx) och genererar den [utfärdade Excelfilen](out.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Open-High-Low-Close Stock Chart Example</h1>
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Create High-Low-Close-Stock Chart
            const pieIdx = worksheet.charts.add(AsposeCells.ChartType.StockOpenHighLowClose, 5, 6, 20, 12);

            // Retrieve the Chart object
            const chart = worksheet.charts.get(pieIdx);

            // Set the legend can be showed
            chart.showLegend = true;

            // Set the chart title name 
            chart.title.text = "Open-High-Low-Close Stock";

            // Set the Legend at the bottom of the chart area
            chart.legend.position = AsposeCells.LegendPositionType.Bottom;

            // Set data range
            chart.chartDataRange = ["A1:E9", true];

            // Set category data 
            chart.nSeries.categoryData = "A2:A9";

            // Set the DownBars and UpBars with different color
            chart.nSeries.get(0).downBars.area.foregroundColor = AsposeCells.Color.Green;
            chart.nSeries.get(0).upBars.area.foregroundColor = AsposeCells.Color.Red;

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

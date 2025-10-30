---
title: Skapa Volym Hög Låg Stäng (VHLC) aktiediagram med JavaScript via C++
linktitle: Skapa Volym Öppen Hög Låg Stäng (VOHLC) Aktiediagram
description: Lär dig hur du skapar ett volym hög låg stäng aktiediagram med Aspose.Cells for JavaScript via C++. Vår guide visar hur man ritar aktiemarknadsdata, inklusive volym, högsta, lägsta och stängningspriser, på ett diagram för bättre analys och visualisering.
keywords: Aspose.Cells for JavaScript via C++, Volym Låg High Stäng Stokchart, Aktiemarknadsdata, Analys, Visualisering.
type: docs
weight: 183
url: /sv/javascript-cpp/create-volume-high-low-close-stock-chart/
---

## **Möjliga användningsscenario**
Det tredje aktiediagrammet vi tittar på är Volym Hög Låg Stäng diagrammet. Återigen är det viktigt att upprepa att du måste ha data i rätt ordning. Om du behöver omorganisera din datatabell bör du göra det innan du skapar ditt diagram.
Detta diagram inkluderar en kolumn för volym direkt efter den första (kategori) kolumnen, och diagrammen innehåller ett kolumn-diagram på den primära axeln som visar denna volym, medan priserna flyttas till den sekundära axeln.

![todo:image_alt_text](data.png)
## **Volym-Öppen-Hög-Låg-Stäng (VOHLC) aktiediagram**

![todo:image_alt_text](sample.png)
## **Exempelkod**
Följande exempelkod laddar den [exempelfil för Excel](Volume-Open-High-Low-Close.xlsx) och genererar den [utfärdade Excelfilen](out.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Volume-High-Low-Close Stock Chart Example</h1>
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

            // Create an instance of Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            // Access the first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Create High-Low-Close-Stock Chart
            const pieIdx = worksheet.charts.add(AsposeCells.ChartType.StockVolumeHighLowClose, 5, 6, 20, 12);
            // Retrieve the Chart object
            const chart = worksheet.charts.get(pieIdx);
            // Set the legend can be showed
            chart.showLegend = true;
            // Set the chart title name 
            chart.title.text = "Volume-High-Low-Close Stock";
            // Set the Legend at the bottom of the chart area
            chart.legend.position = AsposeCells.LegendPositionType.Bottom;
            // Set data range (converted from setChartDataRange(range, isVertical))
            chart.chartDataRange = ["A1:E9", true];
            // Set category data 
            chart.nSeries.categoryData = "A2:A9";
            // Set Color for the first series(Volume) data 
            chart.nSeries.get(0).area.foregroundColor = new AsposeCells.Color(79, 129, 189);
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

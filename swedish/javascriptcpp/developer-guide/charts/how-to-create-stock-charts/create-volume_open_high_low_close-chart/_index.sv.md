---
title: Skapa volym öppna high low stäng(AKT) aktiekarta med JavaScript via C++
description: Lär dig hur du skapar en volym öppna high low stäng aktiekarta med Aspose.Cells for JavaScript via C++. Vår guide visar hur man plottrar aktiemarknadsdata, inklusive volym, öppnings , hög , låg och stängningspriser, på en diagram för bättre analys och visualisering.
keywords: Aspose.Cells for JavaScript via C++, Volym Öppna High Low Stäng Stokchart, Aktiemarknadsdata, Analys, Visualisering.
type: docs
weight: 184
url: /sv/javascript-cpp/create-volume-open-high-low-close-stock-chart/
---

## **Möjliga användningsscenario**
Det fjärde aktiediagrammet vi tittar på är Volume Open High Low Close-diagrammet. Återigen är det viktigt att påpeka att du måste ha data i rätt ordning. Om du behöver omarrangera din datatabell bör du göra det innan du skapar diagrammet. Detta diagram inkluderar en kolumn för volym precis efter den första (kategori-) kolumnen, och diagrammen inkluderar ett kolumndiagram på primäraxeln som visar denna volym, medan priserna flyttas till sekundäraxeln.

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
        <h1>Volume-Open-High-Low-Close Stock Chart Example</h1>
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

            // Create an instance of Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            // Access the first worksheet.
            const worksheet = workbook.worksheets.get(0);
            // Create High-Low-Close-Stock Chart
            const pieIdx = worksheet.charts.add(AsposeCells.ChartType.StockVolumeOpenHighLowClose, 5, 6, 20, 12);
            // Retrieve the Chart object
            const chart = worksheet.charts.get(pieIdx);
            // Set the legend can be showed
            chart.showLegend = true;
            // Set the chart title name 
            chart.title.text = "Volume-Open-High-Low-Close Stock";
            // Set the Legend at the bottom of the chart area
            chart.legend.position = AsposeCells.LegendPositionType.Bottom;
            // Set data range (preserve both arguments as an array)
            chart.chartDataRange = ["A1:F9", true];
            // Set category data 
            chart.nSeries.categoryData = "A2:A9";
            // Set Color for the first series (Volume) data 
            chart.nSeries.get(0).area.foregroundColor = new AsposeCells.Color(79, 129, 189);
            // Fill the PlotArea area with nothing 
            chart.plotArea.area.fillFormat.fillType = AsposeCells.FillType.None;
            // Save the Excel file and provide download link
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

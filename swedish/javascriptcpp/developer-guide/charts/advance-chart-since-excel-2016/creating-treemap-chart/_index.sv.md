---
title: Hur man skapar ett TreeMap diagram med JavaScript via C++
linktitle: Hur man skapar Träddiagramdiagram
description: Lär dig hur man skapar ett Treemap diagram i Aspose.Cells for JavaScript via C++. Vår guide hjälper dig att förstå de olika egenskaper och formateringsalternativ som finns för Treemap diagram, inklusive färger, etiketter och datarendering.
keywords: Aspose.Cells for JavaScript via C++, Treemap diagram, skapa, egenskaper, formatering, färger, etiketter, datarendering, cirkulärt diagram, hierarkisk diagram
type: docs
weight: 161
url: /sv/javascript-cpp/creating-treemap-chart/
---

## **Möjliga användningsscenario**  
Ett träd-diagram ger en hierarkisk vy av dina data och gör det lätt att upptäcka mönster, till exempel vilka objekt som är bästsäljare i en butik. Trädstammarna representeras av rektanglar och varje underavdelning visas som en mindre rektangel. Träddiagrammet visar kategorier med färg och närhet och kan enkelt visa mycket data som skulle vara svårt med andra diagramtyper.  

![todo:image_alt_text](sample.png)  
## **Träddiagram**  
Efter att ha kört koden nedan kommer du att se träddiagrammet som visas nedan.  

![todo:image_alt_text](result.png)  
## **Exempelkod**  
Följande exempelkod laddar den [prov Excel-fil](treemap.xlsx) och genererar [utdata Excel-fil](ut.xlsx).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Treemap Chart Example</title>
    </head>
    <body>
        <h1>Treemap Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType, FillType } = AsposeCells;

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

            // Instantiate Workbook with uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);
            // Add a Treemap chart at row 5, column 6 with height 20 and width 12
            const pieIdx = worksheet.charts.add(ChartType.Treemap, 5, 6, 20, 12);
            // Retrieve the Chart object
            const chart = worksheet.charts.get(pieIdx);
            // Set the legend to be shown
            chart.showLegend = true;
            // Set the chart title text
            chart.title.text = "TreeMap Chart";
            // Add series data range (D2:F13)
            chart.nSeries.add("D2:F13", true);
            // Set category data (A2:C13)
            chart.nSeries.setCategoryData("A2:C13");
            // Show the DataLabels with category names for first series
            chart.nSeries.get(0).dataLabels.showCategoryName = true;
            // Fill the PlotArea area with nothing
            chart.plotArea.area.fillFormat.fillType = FillType.None;

            // Save the modified Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Treemap chart created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

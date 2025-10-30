---
title: Hur man skapar ett Sunburst diagram med JavaScript via C++
linktitle: Hur man skapar Solifjäderdiagram
description: Lär dig hur man skapar ett sunburst diagram i Aspose.Cells for JavaScript via C++, ett diagram som visar data i en cirkel. Vår guide hjälper dig att ställa in olika egenskaper och formatering av ditt diagram, inklusive datamärken, legender, färger och mer.
keywords: Aspose.Cells for JavaScript via C++, sunburst diagram, skapa, ställa in egenskaper, datamärken, legend, formatering, färg, cirkel, datarendering.
type: docs
weight: 162
url: /sv/javascript-cpp/creating-sunburst-chart/
---

## **Möjliga användningsscenario**
Treemap-diagram är bra för att jämföra proportioner inom hierarkin; dock är treemap-diagram inte bra på att visa hierarkiska nivåer mellan de största kategorierna och varje datapunkt. Ett sunburst-diagram är mycket bättre för att visa detta. Sunburst-diagrammet är idealiskt för att visa hierarkiska data. Varje nivå av hierarkin representeras av en ring eller cirkel, där den innersta cirkeln är toppen av hierarkin. Ett sunburst-diagram utan hierarkiska data (en nivå av kategorier) liknar ett hålkakardiagram. Men ett sunburst-diagram med flera kategorinivåer visar hur de yttre ringarna relaterar till de inre. Sunburst-diagrammet är mest effektivt för att visa hur en ring är uppdelad i dess bidragande delar, medan en annan typ av hierarkiskt diagram, treemap, är idealiskt för att jämföra relativa storlekar.

![todo:image_alt_text](sample.png)
## **Solfjäderdiagram**
Efter att ha kört koden nedan kommer du att se solfjäderdiagrammet som visas nedan.

![todo:image_alt_text](result.png)
## **Exempelkod**
Följande exempelkod läser in [provkalkylbladet](sunburst.xlsx) och genererar [utmatningskalkylbladet](out.xlsx).

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

---
title: Hantera titlar på Excel diagram med JavaScript via C++
description: Lär dig hur man använder Aspose.Cells for JavaScript via C++ för att lägga till och formatera diagram och axelrubriker i Microsoft Excel. Vår guide visar hur man ställer in olika typer av titlar, justerar deras utseende och ändrar axelrubriker för bättre datapräsentering och tydlighet.
keywords: Aspose.Cells for JavaScript via C++, diagramrubriker, axelrubriker, Microsoft Excel, datarpresentation, utseende.
linktitle: Titlar
type: docs
weight: 50
url: /sv/javascript-cpp/chart-and-axis-titles/
---

{{% alert color="primary" %}}

I Excel-diagram finns det 2 typer av titlar:
1. Diagramtitel 
1. Axeltitlar

{{% /alert %}}

## **Tillval för titlar**
Aspose.Cells for JavaScript via C++ tillåter också att hantera diagramrubriker i realtid. Med objektet [Title](https://reference.aspose.com/cells/javascript-cpp/title/) kan du ändra text, font och fyllningsformat för rubriker.

|![todo:image_alt_text](chart_title.png)|

## **Inställning av diagram- eller axeltitlar**
Du kan använda Microsoft Excel för att ställa in rubriker för ett diagram och dess axlar i en WYSIWYG-miljö. Aspose.Cells for JavaScript via C++ tillåter också utvecklare att ställa in rubriker i ett diagram och dess axlar i realtid. Alla diagram och deras axlar har ett [Title](https://reference.aspose.com/cells/javascript-cpp/title/) -egenskap som kan användas för att ställa in deras rubriker som visas nedan i ett exempel.

Följande kodexempel visar hur du kan ställa in titlar på diagram och axlar.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Chart Example</h1>
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
            // Instantiate a Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").value = 50;
            worksheet.cells.get("A2").value = 100;
            worksheet.cells.get("A3").value = 150;
            worksheet.cells.get("B1").value = 60;
            worksheet.cells.get("B2").value = 32;
            worksheet.cells.get("B3").value = 50;

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
            chart.nSeries.add("A1:B3", true);

            // Setting the foreground color of the plot area
            chart.plotArea.area.foregroundColor = AsposeCells.Color.Blue;

            // Setting the foreground color of the chart area
            chart.chartArea.area.foregroundColor = AsposeCells.Color.Yellow;

            // Setting the foreground color of the 1st SeriesCollection area
            chart.nSeries.get(0).area.foregroundColor = AsposeCells.Color.Red;

            // Setting the foreground color of the area of the 1st SeriesCollection point
            chart.nSeries.get(0).points.get(0).area.foregroundColor = AsposeCells.Color.Cyan;

            // Filling the area of the 2nd SeriesCollection with a gradient
            chart.nSeries.get(1).area.fillFormat.oneColorGradient(AsposeCells.Color.Lime, 1, AsposeCells.GradientStyleType.Horizontal, 1);

            // Setting the title of a chart
            chart.title.text = "Title";

            // Setting the font color of the chart title to blue
            chart.title.font.color = AsposeCells.Color.Blue;

            // Setting the title of category axis of the chart
            chart.categoryAxis.title.text = "Category";

            // Setting the title of value axis of the chart
            chart.valueAxis.title.text = "Value";

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Fortsatta ämnen**
- [Läs diagramunderrubrik från ODS-fil](/cells/sv/javascript-cpp/read-chart-subtitle-from-ods-file/)

---
title: Legende von Excel Diagrammen mit JavaScript über C++ verwalten
description: Erfahren Sie, wie Sie Aspose.Cells for JavaScript über C++ effektiv nutzen und anpassen können, um Diagramm Legenden in Microsoft Excel optimal zu verwenden. Unser umfassender Leitfaden erklärt die Funktion der Legende, wie man darauf zugreift und sieändert sowie die Visualisierung und das Datenverständnis mit Legenden verbessert.
keywords: Aspose.Cells for JavaScript über C++, Diagramm Legenden, Microsoft Excel, Visualisierung, Datenverständnis
linktitle: Legende
type: docs
weight: 50
url: /de/javascript-cpp/chart-legend/
---

## **Legendenoptionen**
Aspose.Cells for JavaScript über C++ ermöglicht auch die Verwaltung der Legende eines Diagramms zur Laufzeit. Das [Legend](https://reference.aspose.com/cells/javascript-cpp/legend/) Objekt kann verschoben, aktualisiert und formatiert werden.

|![todo:image_alt_text](chart_legend.png)|

## **Festlegen der Legende des Diagramms**
Es ist einfach, die Legende des Diagramms mit Aspose.Cells [Legend](https://reference.aspose.com/cells/javascript-cpp/legend/) zu verwalten.

Das folgende Code-Snippet zeigt, wie die Legende verwaltet wird:


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Chart Legend Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType, Color, LegendPositionType } = AsposeCells;

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
                // No file selected - a new workbook will be created
            }

            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").putValue(50);
            worksheet.cells.get("A2").putValue(100);
            worksheet.cells.get("A3").putValue(150);
            worksheet.cells.get("B1").putValue(60);
            worksheet.cells.get("B2").putValue(32);
            worksheet.cells.get("B3").putValue(50);

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
            chart.nSeries.add("A1:B3", true);

            // Setting the title of a chart
            chart.title.text = "Title";

            // Setting the font color of the chart title to blue
            chart.title.font.color = Color.Blue;

            // Move the legend to left
            chart.legend.position = LegendPositionType.Left;

            // Set font color of the legend
            chart.legend.font.color = Color.Blue;

            // Saving the modified Excel file and providing a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'chart_legend.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart with legend created successfully! Click the download link to get the workbook.</p>';
        });
    </script>
</html>
```

## **Erweiterte Themen**
- [Setzen Sie den Text des Fülls des Diagrammlegendeneintrags auf keinen mithilfe von Aspose.Cells](/cells/de/javascript-cpp/set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells/)

---
title: Open High Low Close (OHLC) Aktienchart mit JavaScript via C++ erstellen
description: Lernen Sie, wie man mit Aspose.Cells for JavaScript via C++ ein Open High Low Close Aktienchart erstellt. Unser Leitfaden zeigt, wie man Börsendaten, einschließlich Eröffnung, Hoch, Tief und Schluss, auf einem Diagramm darstellt, um eine bessere Analyse und Visualisierung zu ermöglichen.
keywords: Aspose.Cells for JavaScript via C++, Open High Low Close Aktienchart, Börsendaten, Analyse, Visualisierung.
type: docs
weight: 182
url: /de/javascript-cpp/create-open-high-low-close-stock-chart/
---

## **Mögliche Verwendungsszenarien**
Das Open-High-Low-Close (OHLC) Diagramm verwendet fünf Datenkategorien in dieser Reihenfolge: Kategorie, Öffnen, Hoch, Tief und Schlusskurs. Die Preisspanne in jeder Kategorie wird erneut durch eine vertikale Linie angezeigt, während die Spanne zwischen Öffnen und Schließen durch eine breitere, freischwebende Leiste angegeben wird. Wenn der Preis in der Kategorie steigt (Schlusskurs höher als Öffnungspreis), wird die Leiste mit einer Farbe gefüllt, während sie bei sinkenden Preisen mit einer anderen Farbe gefüllt wird. Dieser Diagrammtyp wird oft als Candlestick-Diagramm bezeichnet.

![todo:image_alt_text](data.png)

![todo:image_alt_text](sample.png)
## **Verbesserungen der Sichtbarkeit im Diagramm**
Wir verwenden oft Farben anstelle von Schwarz-Weiß, um steigende und fallende Kurse anzuzeigen. Im ersten Satz von Kerzencharts unten zeigt Rot steigende und Grün fallende Kurse.

![todo:image_alt_text](sample2.png)
## **Beispielcode**
Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](Open-High-Low-Close.xlsx) und generiert die [Ausgabedatei Excel](out.xlsx).

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

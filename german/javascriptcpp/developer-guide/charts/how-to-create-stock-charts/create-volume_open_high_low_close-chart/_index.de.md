---
title: Erstellen Sie ein Volume Open High Low Close (VOHLC) Aktienchart mit JavaScript via C++
description: Lernen Sie, wie man mit Aspose.Cells for JavaScript via C++ ein Volume Open High Low Close Aktienchart erstellt. Unser Leitfaden zeigt, wie man Börsendaten, einschließlich Volumen, Eröffnung, Hoch, Tief und Schluss, auf einem Diagramm darstellt, um eine bessere Analyse und Visualisierung zu ermöglichen.
keywords: Aspose.Cells for JavaScript via C++, Volume Open High Low Close Aktienchart, Börsendaten, Analyse, Visualisierung.
type: docs
weight: 184
url: /de/javascript-cpp/create-volume-open-high-low-close-stock-chart/
---

## **Mögliche Verwendungsszenarien**
Das vierte Aktienchart, das wir uns ansehen werden, ist das Volume Open High Low Close-Chart. Hier ist es erneut wichtig zu wiederholen, dass die Daten in der richtigen Reihenfolge vorliegen müssen. Wenn Sie Ihre Datentabelle neu anordnen müssen, tun Sie dies vor dem Erstellen des Charts. Das Chart enthält eine Spalte für Volumen unmittelbar nach der ersten (Kategorie-)Spalte. Die Charts zeigen auf der primären Achse ein SäulenDiagramm für das Volumen, während die Preise auf die sekundäre Achse verschoben werden.

![todo:image_alt_text](data.png)
## **Volume-Open-High-Low-Close (VOHLC) Aktiendiagramm**

![todo:image_alt_text](sample.png)
## **Beispielcode**
Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](Volume-Open-High-Low-Close.xlsx) und generiert die [Ausgabedatei Excel](out.xlsx).

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

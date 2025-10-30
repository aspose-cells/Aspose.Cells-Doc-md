---
title: Hoch Tief Schluss (HLC) Aktienchart mit JavaScript via C++ erstellen
linktitle: Erstellen eines Hoch Tief Schluss(HLC) Aktiendiagramms
description: Lernen Sie, wie man ein Hoch Tief Schluss (HLC) Aktienchart mit Aspose.Cells for JavaScript via C++ erstellt. Unser Schritt für Schritt Leitfaden zeigt, wie man Börsendaten, einschließlich Hoch , Tief und Schlusskurse, auf einem Diagramm darstellt für eine bessere Analyse und Visualisierung.
keywords: Aspose.Cells for JavaScript via C++, Hoch Tief Schluss Aktienchart, Börsendaten, Analyse, Visualisierung.
type: docs
weight: 181
url: /de/javascript-cpp/create-high-low-close-stock-chart/
---

## **Mögliche Verwendungsszenarien**  
Der High-Low-Close (HLC)-Aktienchart verwendet vier Datenkolonnen. Die erste Spalte ist eine Kategorie, normalerweise ein Datum, aber auch Aktiennamen können verwendet werden. Die nächsten drei Spalten sind für Hoch-, Tief- und Schlusskurse. Der Preisbereich für jede Kategorie wird durch eine vertikale Linie von Tief zu Hoch angezeigt, und der Schlusskurs wird durch ein Zeitsymbol rechts von dieser Linie dargestellt.  

![todo:image_alt_text](sample.png)  
## **Verbesserungen der Sichtbarkeit im Diagramm**  
Manchmal können wir das Aussehen des Markers (Schlusskurs) anpassen oder ihn auf der sekundären Achse anzeigen, um das Diagramm übersichtlicher zu gestalten.  

![todo:image_alt_text](sample2.png)  
## **Beispielcode**  
Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](High-Low-Close.xlsx) und generiert die [Ausgabe-Excel-Datei](out.xlsx).  

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

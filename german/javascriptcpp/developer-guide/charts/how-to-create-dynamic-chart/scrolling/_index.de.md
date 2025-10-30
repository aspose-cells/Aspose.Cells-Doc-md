---
title: Wie man ein dynamisches scrollendes Diagramm mit JavaScript via C++ erstellt
linktitle: Wie man ein dynamisches Bildlaufdiagramm erstellt
description: Lernen Sie, wie man ein dynamisches scrollendes Diagramm mit Aspose.Cells for JavaScript via C++ erstellt. Unser Schritt für Schritt Leitfaden zeigt, wie man sanfte Datenübergänge und automatisches Scrollen in Ihrem Diagramm implementiert für eine kontinuierliche und aktualisierte Anzeige.
keywords: Aspose.Cells for JavaScript via C++, Dynamisches scrollendes Diagramm, Datenübergänge, Sanftes Scrollen, Kontinuierliche Anzeige, Aktualisierte Visualisierung.
type: docs
weight: 75
url: /de/javascript-cpp/create-dynamic-scrolling-chart/
---

## **Mögliche Verwendungsszenarien**
Das dynamische Bildlaufdiagramm ist eine Art grafische Darstellung, die verwendet wird, um Daten anzuzeigen, die sich im Laufe der Zeit ändern. Es ist darauf ausgelegt, einen Echtzeit-Blick auf Daten zu bieten, der es Benutzern ermöglicht, kontinuierliche Aktualisierungen und Trends zu verfolgen. Das Diagramm aktualisiert sich kontinuierlich, wenn neue Daten hinzugefügt werden, und scrollt automatisch, um die neuesten Informationen anzuzeigen.

Dynamische Bildlaufdiagramme werden in verschiedenen Branchen wie Finanzen, Börsenanalyse, Wetterverfolgung und sozialen Medienanalysen häufig eingesetzt. Sie ermöglichen es Benutzern, Datenmuster zu visualisieren und zu analysieren und auf Echtzeitinformationen basierende fundierte Entscheidungen zu treffen.

Diese Diagramme sind normalerweise interaktiv und ermöglichen es dem Benutzer, herein- oder herauszuzoomen, durch historische Daten zu scrollen und Zeitintervalle anzupassen. Sie unterstützen oft mehrere Datenreihen, die einen umfassenden Überblick über verschiedene Metriken und ihre Korrelationen bieten.

Insgesamt sind dynamische Bildlaufdiagramme wertvolle Werkzeuge zur Überwachung und Analyse von zeitbezogenen Daten, zur Unterstützung von Echtzeit-Entscheidungsfindung und zur Verbesserung der Datenvisualisierungsfähigkeiten.

## **Verwenden Sie Aspose.Cells, um ein dynamisches Scroll-Diagramm zu erstellen**
 Im nächsten Abschnitt zeigen wir, wie man mit Aspose.Cells for JavaScript via C++ ein dynamisches scrollendes Diagramm erstellt. Wir präsentieren den Code für das Beispiel sowie die Excel-Datei, die damit erstellt wurde.

## **Beispielcode**
Der folgende Beispielcode generiert die [Dynamische Bildlaufdiagramm-Datei](DynamicScrollingChart.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Dynamic Scrolling Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils, ChartType } = AsposeCells;

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
            // Create a new workbook and access the first worksheet.
            const workbook = new Workbook();
            const sheets = workbook.worksheets;
            const sheet = sheets.get(0);

            // Populate the data for the chart. Add values to cells and set series names.
            sheet.cells.get("A1").value = "Day";
            sheet.cells.get("B1").value = "Sales";
            // In this example, we will add 30 days of data
            const allDays = 30;
            const showDays = 10;
            let currentDay = 1;

            for (let i = 0; i < allDays; i++) {
                const cellA = `A${i + 2}`;
                const cellB = `B${i + 2}`;
                sheet.cells.get(cellA).value = i + 1;
                sheet.cells.get(cellB).value = 50 * (i % 2) + 20 * (i % 3) + 10 * Math.floor(i / 3);
            }

            // This is the Dynamic Scrolling Control Data
            sheet.cells.get("G19").value = "Start Day";
            sheet.cells.get("G20").value = currentDay;
            sheet.cells.get("H19").value = "Show Days";
            sheet.cells.get("H20").value = showDays;

            // Set the dynamic range for the chart's data source. 
            let index = sheets.names.add("Sheet1!ChtScrollData");
            sheets.names.get(index).refersTo = "=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)";

            // Set the dynamic range for the chart's data labels. 
            index = sheets.names.add("Sheet1!ChtScrollLabels");
            sheets.names.get(index).refersTo = "=OFFSET(Sheet1!$A$2,Sheet1!$G$20,0,Sheet1!$H$20,1)";

            // Add a ScrollBar for the Dynamic Scrolling Chart
            const bar = sheet.shapes.addScrollBar(2, 0, 3, 0, 200, 30);
            bar.min = 0;
            bar.max = allDays - showDays;
            bar.currentValue = currentDay;
            bar.linkedCell = "$G$20";

            // Create a chart object and set its data source.
            const chartIndex = sheet.charts.add(ChartType.Line, 2, 4, 15, 10);
            const chart = sheet.charts.get(chartIndex);
            chart.nSeries.add("Sales", true);
            chart.nSeries.get(0).values = "Sheet1!ChtScrollData";
            chart.nSeries.get(0).xValues = "Sheet1!ChtScrollLabels";

            // Save the workbook as an Excel file.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'DynamicScrollingChart.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Anmerkungen**
In der generierten Datei können Sie auf die Bildlaufleiste zugreifen, während das Diagramm dynamisch die neuesten 10 Datensätze zählt. Dies wird mithilfe der "OFFSET"-Formel im Beispielcode durchgeführt:

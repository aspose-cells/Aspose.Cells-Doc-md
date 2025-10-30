---
title: Wie man ein dynamisches rollendes Diagramm mit JavaScript via C++ erstellt
linktitle: Wie erstellt man ein dynamisches Rollbalkendiagramm
description: Lernen Sie, wie man ein dynamisches rollendes Diagramm mit Aspose.Cells for JavaScript via C++ erstellt. Unser Leitfaden zeigt, wie man glatte Datenübergänge und rollierende Durchschnitte in Ihrem Diagramm implementiert, um eine fortlaufende und aktualisierte Anzeige zu gewährleisten.
keywords: Aspose.Cells for JavaScript via C++, Dynamisches rollendes Diagramm, Datenübergänge, Glatte Durchschnitte, Kontinuierliche Anzeige, Aktualisierte Visualisierung.
type: docs
weight: 74
url: /de/javascript-cpp/create-dynamic-rolling-chart/
---

## **Mögliche Verwendungsszenarien**
Ein dynamisches Rollbalkendiagramm bezieht sich auf eine grafische Darstellung, die Datenpunkte ständig verschiebt und aktualisiert. Es handelt sich um einen Diagrammtyp, der sich ständig selbst aktualisiert und dabei ein rollendes Fenster der neuesten Datenpunkte zeigt, während ältere Datenpunkte gelöscht werden, wenn neue hinzukommen.

Dynamische Rollbalkendiagramme werden häufig verwendet, um Trends und Muster in Echtzeit- oder Streaming-Daten zu visualisieren. Sie sind besonders nützlich in Szenarien, in denen zeitliche Aspekte und Veränderungen im Laufe der Zeit entscheidend sind, wie z.B. Börsenmarktanalysen, Wetterüberwachung oder Live-Performance-Verfolgung.

Diese Diagramme verwenden typischerweise Animationen oder automatisches Scrollen, um sicherzustellen, dass die aktuellsten Informationen stets präsentiert werden. Die Länge des rollenden Fensters kann angepasst werden, um einen bestimmten Zeitraum anzuzeigen, wie z.B. die letzten Stunde, den Tag oder die Woche.

Zusammenfassend ist ein dynamisches Rollbalkendiagramm eine kontinuierlich aktualisierte grafische Darstellung, die die neuesten Datenpunkte anzeigt und ältere löscht, so dass Benutzer Echtzeit-Trends und Muster beobachten können.

## **Verwenden Sie Aspose.Cells, um ein dynamisches Rollbalkendiagramm zu erstellen**
In den nächsten Absätzen zeigen wir Ihnen, wie Sie unter Verwendung von Aspose.Cells ein dynamisches Rollbalkendiagramm erstellen. Wir zeigen Ihnen den Code für das Beispiel, sowie die mit diesem Code erstellte Excel-Datei.

## **Beispielcode**
Der folgende Beispielcode wird die [Datei für das dynamische Rollbalkendiagramm](DynamicRollingChart.xlsx) generieren.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Dynamic Rolling Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType, Utils } = AsposeCells;

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
            sheet.cells.get("A1").value = "Month";
            sheet.cells.get("A2").value = 1;
            sheet.cells.get("A3").value = 2;
            sheet.cells.get("A4").value = 3;
            sheet.cells.get("A5").value = 4;
            sheet.cells.get("A6").value = 5;
            sheet.cells.get("A7").value = 6;
            sheet.cells.get("A8").value = 7;

            sheet.cells.get("B1").value = "Sales";
            sheet.cells.get("B2").value = 50;
            sheet.cells.get("B3").value = 45;
            sheet.cells.get("B4").value = 55;
            sheet.cells.get("B5").value = 60;
            sheet.cells.get("B6").value = 55;
            sheet.cells.get("B7").value = 65;
            sheet.cells.get("B8").value = 70;

            // Set the dynamic range for the chart's data source.
            let index = sheets.names.add("Sheet1!ChtData");
            sheets.names.get(index).refersTo = "=OFFSET(Sheet1!$B$1,COUNT(Sheet1!$B:$B),0,-5,1)";

            // Set the dynamic range for the chart's data labels.
            index = sheets.names.add("Sheet1!ChtLabels");
            sheets.names.get(index).refersTo = "=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)";

            // Create a chart object and set its data source.
            const chartIndex = sheet.charts.add(ChartType.Line, 10, 3, 25, 10);
            const chart = sheet.charts.get(chartIndex);
            chart.nSeries.add("Sales", true);
            chart.nSeries.get(0).values = "Sheet1!ChtData";
            chart.nSeries.get(0).xValues = "Sheet1!ChtLabels";

            // Save the workbook as an Excel file.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'DynamicRollingChart.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Anmerkungen**
In der generierten Datei können Sie weiterhin Daten in den Spalten A und B hinzufügen, während das Diagramm dynamisch die neuesten 5 Datensätze zählt. Dies wird im Beispielcode mit der "OFFSET"-Formel durchgeführt:

---
title: Verwalten Sie DataLabels der Excel Diagramme mit JavaScript via C++
description: Erfahren Sie, wie Sie Data Labels in Excel Diagrammen mit Aspose.Cells for JavaScript via C++ effektiv verwalten. Dieser umfassende Leitfaden behandelt verschiedene Verwaltungsaufgaben, einschließlich Hinzufügen, Entfernen und Ändern von Labels zur Verbesserung der Lesbarkeit und Benutzerfreundlichkeit von Diagrammen.
keywords: Aspose.Cells for JavaScript, Excel Diagramme, Datenetiketten, Verwaltung, Lesbarkeit, Benutzerfreundlichkeit, Hinzufügen, Entfernen, Ändern.
linktitle: Datenbeschriftungen
type: docs
weight: 50
url: /de/javascript-cpp/insert-datalabels-to-chart/
---

{{% alert color="primary" %}}  

Datenbeschriftungen sind ein wichtiger Bestandteil eines Diagramms.  
Wir können leicht den Wert, den Prozentsatz usw. jeder Serie erfahren.  

{{% /alert %}}  

## **Datenbeschriftungen-Optionen**  
Aspose.Cells for JavaScript via C++ ermöglicht auch die Verwaltung der Datenetiketten des Diagramms zur Laufzeit, mit dem [DataLabels](https://reference.aspose.com/cells/javascript-cpp/datalabels/) Objekt, es ist einfach, Datenetiketten des Diagramms zu verschieben, zu aktualisieren und zu formatieren.  

|![todo:image_alt_text](chart_datalabels.png)|  

## **Verwalten der Datenbeschriftungen eines Diagramms**  
Es ist einfach, die Datenetiketten des Diagramms mit Aspose.Cells [DataLabels](https://reference.aspose.com/cells/javascript-cpp/datalabels/) zu verwalten.  

Der folgende Codeausschnitt zeigt, wie DataLabels verwaltet werden können:  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Chart Data Labels Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        let asposeReady = false;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            asposeReady = true;
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const resultDiv = document.getElementById('result');
            if (!asposeReady) {
                resultDiv.innerHTML = '<p style="color: red;">Aspose.Cells is not initialized yet. Please wait and try again.</p>';
                return;
            }

            // Instantiate a new Workbook object
            const workbook = new Workbook();

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
            const chartIndex = worksheet.charts.add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
            chart.nSeries.add("A1:B3", true);

            // Show value labels
            chart.nSeries.get(0).dataLabels.showValue = true;
            // Show series name labels
            chart.nSeries.get(1).dataLabels.showSeriesName = true;
            // Move labels to center
            chart.nSeries.get(1).dataLabels.position = AsposeCells.LabelPositionType.Center;

            // Save the file and prepare download
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'chart_datalabels.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  

## **Erweiterte Themen**  
- [Hinzufügen von benutzerdefinierten Beschriftungen zu Datenpunkten in der Serie des Diagramms](/cells/de/javascript-cpp/adding-custom-labels-to-data-points-in-the-series-of-the-chart/)  
- [Textumbruch für Datenbeschriftungen des Diagramms deaktivieren](/cells/de/javascript-cpp/disable-text-wrapping-for-data-labels-of-the-chart/)  
- [Ändern der Größe der Datenbeschriftungsform des Diagramms, um den Text anzupassen](/cells/de/javascript-cpp/resize-chart-s-data-label-shape-to-fit-text/)  
- [Benutzerdefinierte Datenauswahl im Diagrammpunkt](/cells/de/javascript-cpp/rich-text-custom-data-label-of-chart-point/)  
- [Festlegen des Formtyps von Datenbeschriftungen des Diagramms](/cells/de/javascript-cpp/set-the-shape-type-of-data-labels-of-chart/)  
- [Anzeigen von Zellenbereichen als Datenbeschriftungen](/cells/de/javascript-cpp/showing-cell-range-as-the-data-labels/)

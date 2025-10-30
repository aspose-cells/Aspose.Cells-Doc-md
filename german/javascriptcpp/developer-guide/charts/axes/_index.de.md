---
title: Achsen von Excel Diagrammen mit JavaScript via C++ verwalten
description: Erfahren Sie, wie Sie Diagramm Achsen in Aspose.Cells for JavaScript via C++ konfigurieren. Unser Leitfaden zeigt Ihnen, wie Sie primäre und sekundäre Achsen anpassen, ihre Bereiche einstellen und ihre Eigenschaften ändern, um Ihre Diagramme zu verbessern.
keywords: Aspose.Cells for JavaSkript über C++, Diagrammachsen, Konfiguration, Primäre Achsen, Sekundäre Achsen, Bereich, Eigenschaften.
linktitle: Achsen
type: docs
weight: 50
url: /de/javascript-cpp/chart-axes/
---

{{% alert color="primary" %}}  

In Excel-Diagrammen gibt es 3 Arten von Achsen:  
1. Horizontale (Kategorie) Achse : X-Achse  
1. Vertikale(Wert) Achse: Y-Achse  
1. Tiefen(Serien) Achse: Z-Achse  

{{% /alert %}}  

## **Achsenoptionen**  
Aspose.Cells for JavaSkript über C++ ermöglicht auch die Verwaltung der Diagrammachsen zur Laufzeit. Mit dem [Axis](https://reference.aspose.com/cells/javascript-cpp/axis/) Objekt können Sie alle Optionen der Achse wie in Excel ändern.  

|![todo:image_alt_text](chart_axes.png)|  

## **X- und Y-Achsen verwalten**  
In Excel-Diagrammen sind horizontale und vertikale Achsen die beiden beliebtesten Achsen.  

Das folgende Codebeispiel zeigt, wie man die Optionen der X- und Y-Achsen festlegt.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Chart Axes</title>
    </head>
    <body>
        <h1>Chart Axes Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType } = AsposeCells;

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

            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").value = "Series1";
            worksheet.cells.get("A2").value = 50;
            worksheet.cells.get("A3").value = 100;
            worksheet.cells.get("A4").value = 150;
            worksheet.cells.get("B1").value = "Series2";
            worksheet.cells.get("B2").value = 60;
            worksheet.cells.get("B3").value = 32;
            worksheet.cells.get("B4").value = 50;

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
            chart.chartDataRange = ["A1:B4", true];

            // Hiding X axis
            chart.categoryAxis.isVisible = false;

            // Setting max value of Y axis
            chart.valueAxis.maxValue = 200;
            // Setting major unit
            chart.valueAxis.majorUnit = 50;

            // Save the file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'chart_axes.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully. Click the download link to download the file.</p>';
        });
    </script>
</html>
```  

## **Erweiterte Themen**  
- [Ändern der Richtung der Markierungstexte](/cells/de/javascript-cpp/change-tick-label-direction/)  
- [Bestimmen Sie, welche Achse im Diagramm existiert](/cells/de/javascript-cpp/determine-which-axis-exists-in-the-chart/)  
- [Behandeln Sie automatische Einheiten der Diagrammachse wie Microsoft Excel](/cells/de/javascript-cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/)  
- [Lesen Sie die Achsenbeschriftungen nach der Berechnung des Diagramms](/cells/de/javascript-cpp/read-axis-labels-after-calculating-the-chart/)  
- [Wie man die Kategorieachse im Excel-Diagramm einstellt](/cells/de/javascript-cpp/how-to-set-category-axis/)

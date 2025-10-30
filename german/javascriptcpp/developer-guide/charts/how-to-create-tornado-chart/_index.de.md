---
title: Wie man mit JavaScript über C++ ein Tornado Diagramm erstellt
linktitle: Wie man ein Tornado Diagramm erstellt
type: docs
weight: 73
url: /de/javascript-cpp/create-tornado-chart/
description: Lernen Sie, wie Sie mit Aspose.Cells for JavaScript über C++ API ein Tornado Diagramm erstellen.
keywords: JavaScript erstellt ein Tornado Diagramm, fügt ein Tornado Diagramm hinzu, insertiert ein Tornado Diagramm
---

## **Einführung**
Ein Tornado-Diagramm, auch als Tornado-Diagramm oder Tornado-Grafik bekannt, ist eine Art der Datendarstellung, die oft für die Sensitivitätsanalyse in Excel verwendet wird. Es hilft Ihnen, den Einfluss von sich ändernden Variablen auf ein bestimmtes Ergebnis oder Resultat zu verstehen.

## **Wie man ein Tornado-Diagramm in Excel erstellt**
Sie können ein Tornado-Diagramm in Excel erstellen, indem Sie diesen Schritten folgen:
1. Wählen Sie die Daten aus und gehen Sie zu Einfügen --> Diagramme --> Säulen- oder Balkendiagramm einfügen --> Gestapeltes Balkendiagramm. Klicken Sie darauf.
<br>
<img src="1.png" width=70% />
2. Ändern Sie die Y-Achse: Klicken Sie mit der rechten Maustaste auf die y-Achse. Klicken Sie auf Achsenformat. Klicken Sie in Beschriftungen auf das Dropdown-Menü für die Position der Beschriftung und wählen Sie Niedrigstes Element aus.
<br>
<img src="2.png" width=70% />
3. Wählen Sie eine beliebige Leiste aus und gehen Sie zur Formatierung. Legen Sie einen geeigneten Abstand fest.
<br>
<img src="3.png" width=70% />
4. Entfernen wir das Minuszeichen (-) aus dem Tornado-Diagramm. Wählen Sie die x-Achse aus. Gehen Sie zur Formatierung. Klicken Sie in den Achsenoptionen auf die Nummer. Wählen Sie in der Kategorie Benutzerdefiniert aus. Im Formatcode schreiben Sie ###0,###0. Klicken Sie auf Hinzufügen.
<br>
<img src="4.png" width=70% />
5. Klicken Sie auf die y-Achse und gehen Sie zu den Achsenoptionen. Überprüfen Sie in den Achsenoptionen Kategorien in umgekehrter Reihenfolge.
<br>
<img src="5.png" width=70% />

## ** Wie man ein Tornado-Diagramm in Aspose.Cells for JavaScript via C++ hinzufügt**
Bitte sehen Sie sich den folgenden Beispielcode an. Es lädt die [Beispieldatei Excel](sample.xlsx), die einige Beispieldaten enthält. Danach erstellt es das gestapelte Balkendiagramm basierend auf den Anfangsdaten und setzt relevante Eigenschaften. Schließlich speichert es die Arbeitsmappe im [Ausgabe-XLSX-Format](out.xlsx). Der folgende Screenshot zeigt das von Aspose.Cells erstellte Tornado-Diagramm in der Ausgabe-Excel-Datei.
<br>
<img src="6.png" width=70% />

### **Beispielcode**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xlsx" />
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
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const sheet = workbook.worksheets.get(0);
            const charts = sheet.charts;

            // Add bar chart
            const index = charts.add(AsposeCells.ChartType.BarStacked, 8, 1, 24, 8);
            const chart = charts.get(index);

            // Set data for bar chart
            chart.chartDataRange = "A1:C7";

            // Set properties for bar chart
            chart.title.text = "Tornado chart";
            chart.style = 2;
            chart.plotArea.area.foregroundColor = AsposeCells.Color.White;
            chart.plotArea.border.color = AsposeCells.Color.White;
            chart.legend.position = AsposeCells.LegendPositionType.Bottom;

            chart.categoryAxis.tickLabelPosition = AsposeCells.TickLabelPositionType.Low;
            chart.category```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xlsx" />
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
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const sheet = workbook.worksheets.get(0);
            const charts = sheet.charts;

            // Add bar chart
            const index = charts.add(AsposeCells.ChartType.BarStacked, 8, 1, 24, 8);
            const chart = charts.get(index);

            // Set data for bar chart
            chart.chartDataRange = "A1:C7";

            // Set properties for bar chart
            chart.title.text = "Tornado chart";
            chart.style = 2;
            chart.plotArea.area.foregroundColor = AsposeCells.Color.White;
            chart.plotArea.border.color = AsposeCells.Color.White;
            chart.legend.position = AsposeCells.LegendPositionType.Bottom;

            chart.categoryAxis.tickLabelPosition = AsposeCells.TickLabelPositionType.Low;
            chart.categoryAxis.isPlotOrderReversed = true;

            chart.gapWidth = 10;

            const valueAxis = chart.valueAxis;
            valueAxis.tickLabels.numberFormat = "#,##0;#,##0";

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

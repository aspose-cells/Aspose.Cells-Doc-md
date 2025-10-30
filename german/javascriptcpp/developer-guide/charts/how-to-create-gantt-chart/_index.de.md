---
title: Wie man mit JavaScript über C++ ein Gantt Diagramm erstellt
linktitle: So erstellen Sie ein Gantt Diagramm
type: docs
weight: 72
url: /de/javascript-cpp/how-to-create-gantt-chart/
description: Lernen Sie, wie man mit Aspose.Cells for JavaScript über C++ API ein Gantt Diagramm erstellt.
keywords: JavaScript erstellt ein Gantt Diagramm, fügt ein Gantt Diagramm hinzu, insertiert ein Gantt Diagramm
---

## **Was ist ein Gantt-Diagramm?**

Ein Gantt-Diagramm ist eine Art Balkendiagramm, das einen Projektzeitplan veranschaulicht. Es zeigt die Anfangs- und Enddaten der verschiedenen Elemente eines Projekts. Jede Aufgabe oder Aktivität wird durch einen Balken dargestellt, dessen Länge ihrer Dauer entspricht. Gantt-Diagrams zeigen auch Abhängigkeiten zwischen Aufgaben, sodass Projektmanager die Reihenfolge der Aufgaben visualisieren können. Sie werden häufig im Projektmanagement verwendet, um Projekte effektiv zu planen, zu planen und zu verfolgen.

## **So erstellen Sie ein Gantt-Diagramm in Excel**

Sie können in Excel ein Gantt-Diagramm erstellen, indem Sie diese Schritte befolgen:
1. Fügen Sie einige Daten für das Gantt-Diagramm hinzu. 
<br>
<img src="00.png" width=50% />
1. Wählen Sie die Daten aus und gehen Sie zu Einfügen --> Diagramme --> Säulen- oder Balkendiagramm einfügen --> Gestapeltes Balkendiagramm. In unserem Beispiel sind das B1:B7, dann fügen Sie ein **Gestapeltes Balken**-Diagramm ein.
<br>
<img src="1.png" width=50% />

1. Wählen Sie das Diagramm aus, **Daten auswählen** -> **Hinzufügen**, stellen Sie den **Seriennamen** und die **Serienwerte** wie folgt ein.
<br>
<img src="2.png" width=50% />

1. Wählen Sie das Diagramm aus, bearbeiten Sie die **Horizontalen (Kategorie) Achsenbeschriftungen**.
<br>
<img src="3.png" width=50% />

1. **Achse formatieren** des Y-Achse, wählen Sie **Kategorien umkehren**.
1. Wählen Sie die **Blaue Serie** und setzen Sie die **Füllung -> Keine Füllung**.
1. **Achse formatieren** der X-Achse, setzen Sie die **Minimale und Maximale Werte** (01.05.2019:43470, 30.01.2019:43494).
<br>
<img src="4.png" width=50% />

1. **Datenbeschriftungen hinzufügen** für das Diagramm, jetzt erhalten Sie ein Gantt-Diagramm.
<br>
<img src="0.png" width=50% />


## **So fügen Sie ein Gantt-Diagramm in Aspose.Cells hinzu**
Bitte sehen Sie sich den folgenden Beispielcode an. Es lädt die [Beispiel-Excel-Datei](sample.xlsx), die einige Beispieldaten enthält. Anschließend erstellt es das gestapelte Balkendiagramm basierend auf den Anfangsdaten und setzt die entsprechenden Eigenschaften. Schließlich speichert es die Arbeitsmappe im [Ausgabe XLSX-Format](result.xlsx). Der folgende Screenshot zeigt das von Aspose.Cells erstellte Gantt-Diagramm in der Ausgabedatei.
<br>
<img src="5.png" width=60% />

### **Beispielcode**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Chart Example</title>
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Create BarStacked Chart
            const i = worksheet.charts.add(AsposeCells.ChartType.BarStacked, 5, 6, 20, 15);

            // Retrieve the Chart object
            const chart = worksheet.charts.get(i);

            // Set the chart title name 
            chart.title.text = "Gantt Chart";

            // Set the chart title is Visible
            chart.title.isVisible = true;

            // Set data range
            chart.chartDataRange = "B1:B6";

            // Add series data range
            chart.nSeries.add("C2:C6", true);

            // No fill for one serie
            chart.nSeries.get(0).area.fillFormat.fillType = AsposeCells.FillType.None;

            // Set the Horizontal(Category) Axis
            chart.nSeries.setCategoryData("A2:A6");

            // Reverse the Horizontal(Category) Axis
            chart.categoryAxis.isPlotOrderReversed = true;

            // Set the value axis's MinValue and MaxValue
            const minValue = parseFloat(worksheet.cells.get("B2").value);
            const maxValue = parseFloat(worksheet.cells.get("D6").value);
            chart.valueAxis.minValue = isNaN(minValue) ? 0 : minValue;
            chart.valueAxis.maxValue = isNaN(maxValue) ? 0 : maxValue;

            chart.plotArea.area.fillFormat.fillType = AsposeCells.FillType.None;

            // Show the DataLabels
            chart.nSeries.get(1).dataLabels.showValue = true;

            // Disable the Legend
            chart.showLegend = false;

            // Save the result
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'result.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

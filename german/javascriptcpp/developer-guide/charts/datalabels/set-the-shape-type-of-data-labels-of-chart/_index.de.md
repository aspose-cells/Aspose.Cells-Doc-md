---
title: Setzen Sie den Shape Typ der Datenbeschriftungen im Diagramm mit JavaScript via C++
linktitle: Legen Sie den Formtyp der Datenbeschriftungen des Diagramms fest
description: Erfahren Sie, wie Sie den Shape Typ der Datenbeschriftungen in Diagrammen mit Aspose.Cells for JavaScript via C++ festlegen. Dieser Leitfaden erklärt die verfügbaren Shape Typen und zeigt, wie Sie den geeigneten Shape für Ihre Datenbeschriftungen auswählen, um Präsentation und Benutzerfreundlichkeit zu verbessern.
keywords: Aspose.Cells for JavaScript via C++, Diagrammerstellung, Datenbeschriftungen, Shape Typen, Präsentation, Benutzerfreundlichkeit.
type: docs
weight: 110
url: /de/javascript-cpp/set-the-shape-type-of-data-labels-of-chart/
---

## **Mögliche Verwendungsszenarien**
Sie können den Formtyp der Datenetiketten im Diagramm mit der Eigenschaft `DataLabels.shapeType` ändern. Es nimmt den Wert der Enumeration `DataLabelShapeType` an und ändert entsprechend den Formtyp der Datenetiketten. Einige seiner Werte sind

{{< highlight javascript >}}
 DataLabelShapeType.BentLineCallout
DataLabelShapeType.DownArrowCallout
DataLabelShapeType.Ellipse
DataLabelShapeType.LineCallout
DataLabelShapeType.Rect
etc.
{{< /highlight >}}

## **Festlegen des Formtyps von Datenbeschriftungen des Diagramms**
Das folgende Beispiel ändert den Shape-Typ der Datenbeschriftungen im Diagramm auf `DataLabelShapeType.WedgeEllipseCallout`. Bitte beachten Sie die [Beispieldatei Excel](60489778.xlsx), die in diesem Beispiel verwendet wird, und die [Ausgabedatei Excel](60489779.xlsx), die daraus generiert wurde. Der Screenshot zeigt die Wirkung des Codes auf die Beispiel-Excel-Datei.

![todo:image_alt_text](set-the-shape-type-of-data-labels-of-chart_1.png)
## **Beispielcode**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Shape Type of Data Labels of Chart Example</title>
    </head>
    <body>
        <h1>Set Shape Type of Data Labels of Chart Example</h1>
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
            const resultDiv = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Accessing the first chart
            const chart = worksheet.charts.get(0);

            // Accessing the first series
            const series = chart.nSeries.get(0);

            // Set the shape type of data labels i.e. Speech Bubble Oval
            series.dataLabels.shapeType = AsposeCells.DataLabelShapeType.WedgeEllipseCallout;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSetShapeTypeOfDataLabelsOfChart.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Shape type set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

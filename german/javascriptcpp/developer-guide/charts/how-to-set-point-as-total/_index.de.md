---
title: Wie man Punkte in JavaScript über C++ als Total setzt
linktitle: So setzen Sie einen Punkt als Gesamtwert
description: Lernen Sie, wie man in Waterfall Diagrammen Punkte mit Aspose.Cells for JavaScript via C++ auf Total setzt.
keywords: Waterfall Diagramm, Punkt, Als Total setzen, JavaScript via C++
type: docs
weight: 72
url: /de/javascript-cpp/how-to-set-point-as-total/
---

## Was bedeutet "Punkt als Gesamtwert setzen" in Excel-Diagrammen

In einigen Excel-Diagrammen, zum Beispiel Wasserfalldiagrammen, sind einige Punktdaten die Summe der vorherigen Punkte, und Sie müssen möglicherweise "Punkt als Gesamtwert setzen". Wir zeigen den Beispielcode und die Abbildung unten.

## Ein Wasserfall-Diagramm muss "Punkt als Gesamtwert setzen" 

![todo:image_alt_text](set-as-total1.png)

Dieses Bild zeigt ein Waterfall-Diagramm in Excel. Wir können sehen, dass es vier Datenpunkte gibt, die mit "Total" beginnen, und sie werden verwendet, um alle vorherigen Datenpunkte zu zählen. In diesem Bild sind die Einstellungen nicht ganz richtig. Wenn wir einen Punkt "Total 2024" auswählen, sehen wir, dass die Option "Als Total setzen" in Excel nicht aktiviert ist. Unten befindet sich die [Beispieldatei](SampleSheet.xlsx), die modifiziert werden muss, und wir verwenden Aspose.Cells for JavaScript via C++, um sie korrekt einzurichten.

## Verwendung von Aspose.Cells for JavaScript via C++, um "Punkt als Total setzen" 

Wir verwenden den folgenden Code, um die Datei richtig einzurichten:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Chart Subtotals Example</title>
    </head>
    <body>
        <h1>Set Chart Subtotals Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Accessing the chart named "Graphiq5"
            const chart = worksheet.charts.get("Graphiq5");

            // set some points as total column 
            // In this example, we set points 0, 4, 8, 12 as total
            chart.nSeries.get(0).layoutProperties.subtotals = [0, 4, 8, 12];

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Sie können die folgende korrekte [Ausgabedatei](output.xlsx) herunterladen

Wie im untenstehenden Bild gezeigt, sind die vier "Total"-Datenpunkte korrekt eingestellt, und Sie können den Unterschied zum vorherigen Diagramm erkennen.

![todo:image_alt_text](set-as-total2.png)

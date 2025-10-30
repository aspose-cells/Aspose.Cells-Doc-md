---
title: Wie man Serien mit JavaScript über C++ unsichtbar macht
linktitle: Wie man Serien unsichtbar macht
description: Erfahren Sie, wie Sie Serien in einem Excel Diagramm mit Aspose.Cells for JavaScript über C++ unsichtbar machen. 
keywords: Excel Diagramm, Serie, Unsichtbar, IsFiltered JavaScript über C++
type: docs
weight: 74
url: /de/javascript-cpp/how-to-set-series-invisible/
---

## Wie man Serien in Excel-Diagrammen unsichtbar macht

In Excel-Diagrammen können Sie mit einem Rechtsklick auf das Diagramm "Daten auswählen" wählen und im Popup-Fenster festlegen, ob eine Serie sichtbar sein soll, indem Sie sie an- oder abwählen. Sie können die folgende [Beispieldatei](SeriesFiltered.xlsx) herunterladen und in Excel öffnen, um diese Funktion wie in der Abbildung gezeigt zu erreichen. Anschließend erklären wir, wie man dies mit der Aspose.Cells-Bibliothek umsetzt.

![todo:image_alt_text](series-invisible.png)

## Wie man Serien mit Aspose.Cells unsichtbar macht 

Wir verwenden den folgenden Code, um Serien mit Aspose.Cells unsichtbar zu machen:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Modify Chart Series Color Variation</h1>
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

            // Access the first worksheet and its charts
            const charts = workbook.worksheets.get(0).charts;
            const chart = charts.get("Chart 1");

            // Access filtered NSeries and NSeries collections (properties instead of getters)
            const nSeriesFiltered = chart.filteredNSeries;
            const nSeries = chart.nSeries;

            // Set IsColorVaried on series (converted from setIsColorVaried to property assignment)
            nSeries.get(1).isColorVaried = true;
            nSeries.get(0).isColorVaried = true;

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Sie können die folgende [Inputdatei](SeriesFiltered.xlsx) und [Ausgabedatei](output.xlsx) erhalten.

Wie in der Abbildung unten gezeigt, sind die ersten beiden Serien, die ursprünglich sichtbar waren, in der Ausgabedatei unsichtbar geworden.
![todo:image_alt_text](output.png)

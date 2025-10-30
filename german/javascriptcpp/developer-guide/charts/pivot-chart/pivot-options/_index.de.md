---
title: So verwalten Sie PivotChart mit PivotOptions für JavaScript via C++
linktitle: Pivot Optionen
type: docs
weight: 10
url: /de/javascript-cpp/how-to-manage-pivotchart-with-pivotoptions/
description: Wie man PivotChart mit PivotOptions in JavaScript via C++ verwaltet.
keywords: PivotChart JavaScript via C++
---

## Was ist ein PivotChart

Ein PivotChart in Excel ist eine grafische Darstellung von Daten, die aus einer PivotTable erstellt wird. Es ermöglicht Benutzern, Daten dynamisch zu visualisieren und zu analysieren, indem Informationen in Diagrammform zusammengefasst und angezeigt werden. PivotCharts sind interaktiv und können leicht modifiziert werden, um verschiedene Perspektiven der Daten zu zeigen, was es zu einem leistungsstarken Werkzeug für die Datenanalyse und Präsentation in Excel macht.

## Wie man PivotChart mit PivotOptions verwaltet

Durch die Verwendung von Aspose.Cells for JavaScript via C++ können Sie [**PivotOptions**](https://reference.aspose.com/cells/javascript-cpp/pivotoptions/) zur Verwaltung von PivotChart verwenden.

Beispiel-Datei und Code:
[Beispiel-Datei](Sample.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Hide PivotChart ZoneFilter Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            // Accessing the first worksheet and the first chart
            const worksheet = workbook.worksheets.get(0);
            const chart = worksheet.charts.get(0);
            const opt = chart.pivotOptions;

            // Hide ZoneFilter in PivotChart
            opt.dropZoneFilter = false; // HideZoneFilter

            // Save the file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'HideZoneFilter.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">ZoneFilter hidden successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Mit dem obigen Beispielcode können Sie die Ergebnisdatei mit folgender Wirkung überprüfen, wie im Bild gezeigt:

**![Ergebnis](Output.png)**

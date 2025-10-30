---
title: Legentexte der Diagrammlinie mit Aspose.Cells for JavaScript via C++ auf none setzen
linktitle: Legenden Eintragsfüllung des Diagramms auf keinen Text setzen mit Aspose.Cells
description: Lernen Sie, wie man mit Aspose.Cells for JavaScript via C++ die Textfarbe des Legenden Eintrags auf none setzt. Dieser Leitfaden zeigt, wie man die Füllfarbe der Legenden Einträge in Microsoft Excel Diagrammen für eine bessere Visualisierung und individuelle Gestaltung ändert.
keywords: Aspose.Cells for JavaScript via C++, Diagramm Legenden Eintrag Füllung, Microsoft Excel, Visualisierung, Anpassung.
type: docs
weight: 320
url: /de/javascript-cpp/set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells/
---

{{% alert color="primary" %}}

Wenn Sie die Füllfarbe des Legendeneintrags des Diagramms auf keine setzen möchten, damit sie nicht im Diagramm-Legendenbereich angezeigt wird, setzen Sie [**LegendEntry.isTextNoFill()**](https://reference.aspose.com/cells/javascript-cpp/legendentry/#isTextNoFill--) auf **true**.

{{% /alert %}}

Der folgende Beispielcode setzt den Text der zweiten Diagrammlegendeneintragsfüllung auf keine. Laden Sie bitte die [Beispieldatei Excel](5115219.xlsx) herunter, die in diesem Code verwendet wird, und die [Ausgabedatei Excel](5115217.xlsx), die von ihr generiert wird, zur Referenz.

Das folgende Screenshot hebt die Wirkung dieses Codes auf die [Beispieldatei Excel](5115219.xlsx) hervor.

![todo:image_alt_text](set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells_1.png)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Chart Legend Entry Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Access the first chart inside the sheet
            const chart = sheet.charts.get(0);

            // Set text of second legend entry fill to none
            const legendEntry = chart.legend.legendEntries.get(1);
            legendEntry.isTextNoFill = true;

            // Save the workbook in xlsx format and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ChartLegendEntry_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

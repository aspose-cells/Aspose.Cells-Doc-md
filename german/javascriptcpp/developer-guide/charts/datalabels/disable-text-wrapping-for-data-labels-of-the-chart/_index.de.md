---
title: Deaktivieren Sie das Textumbruch für Datenbeschriftungen des Diagramms mit JavaScript via C++
description: Lernen Sie, wie Sie den Textumbruch für Datenbeschriftungen in Diagrammen mit Aspose.Cells for JavaScript via C++ deaktivieren. Unsere Anleitung zeigt, wie Sie lange Beschriftungen daran hindern, sich zu überlappen, und für klarere und besser lesbare Diagramme sorgen.
keywords: Aspose.Cells for JavaScript via C++, Diagrammerstellung, Datenbeschriftungen, Textumbruch, Überlappung, Lesbarkeit, Anzeigen.
type: docs
weight: 70
url: /de/javascript-cpp/disable-text-wrapping-for-data-labels-of-the-chart/
---

{{% alert color="primary" %}}

Microsoft Excel 2013 ermöglicht es Benutzern, Texte in den Datenbeschriftungen des Diagramms umzubrechen oder nicht umzubrechen. Standardmäßig ist der Text in den Datenbeschriftungen des Diagramms umgebrochen.

Aspose.Cells bietet eine [**DataLabels.isTextWrapped()**](https://reference.aspose.com/cells/javascript-cpp/datalabels/#isTextWrapped--)-Eigenschaft, die Sie auf true oder false setzen können, um den Textumbruch von Datenetiketten entsprechend zu aktivieren oder zu deaktivieren.

{{% /alert %}}

Der folgende Codebeispiel zeigt, wie der Textumbruch für die Datenbeschriftungen des Diagramms deaktiviert wird.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Disable Data Label Text Wrapping</h1>
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

            // Instantiating a Workbook object by loading uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the first chart inside the worksheet
            const chart = worksheet.charts.get(0);

            // Disable the Text Wrapping of Data Labels in all Series
            chart.nSeries.get(0).dataLabels.isTextWrapped = false;
            chart.nSeries.get(1).dataLabels.isTextWrapped = false;
            chart.nSeries.get(2).dataLabels.isTextWrapped = false;

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

---
title: Pivot Verbindung mit JavaScript über C++ hinzufügen
linktitle: Pivot Verbindung hinzufügen
type: docs
weight: 30
url: /de/javascript-cpp/add-pivot-connection/
description: Erfahren Sie, wie Sie eine Pivot Verbindung mit Aspose.Cells for JavaScript über C++ hinzufügen.
keywords: Pivot Verbindung ohne Office 2013, Office 2016, Office 2019 und Office 365 JavaScript über C++ hinzufügen.
---

## **Mögliche Verwendungsszenarien**

Wenn Sie eine Slicer und eine Pivot-Tabelle in Excel verknüpfen möchten, klicken Sie mit der rechten Maustaste auf den Slicer und wählen Sie „Berichtverbindungen...“. In der Optionenliste können Sie die Kontrollkästchen aktivieren. Bitte verwenden Sie auch die Methode [**Slicer.addPivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/javascript-cpp/slicer/#addPivotConnection-PivotTable-), um eine Slicer mit einer Pivot-Tabelle programmgesteuert mit der Aspose.Cells API zu verknüpfen.

## **Slicer und PivotTable verknüpfen**

Das folgende Beispiel lädt die [Beispiel-Excel-Datei](add-pivot-connection.xlsx), die einen vorhandenen Slicer enthält. Es greift auf den Slicer zu und verknüpft ihn mit der Pivot-Tabelle. Abschließend wird die Arbeitsmappe als [Ausgabedatei](add-pivot-connection-out.xlsx) gespeichert.

## **Beispielcode**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Add Pivot Connection Example</title>
    </head>
    <body>
        <h1>Add Pivot Connection Example</h1>
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

            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const worksheet = workbook.worksheets.get(0);

            const pivotTable = worksheet.pivotTables.get(0);

            const slicer = worksheet.slicers.get(0);

            slicer.addPivotConnection(pivotTable);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'add-pivot-connection-out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Pivot connection added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

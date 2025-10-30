---
title: Pivot Verbindung mit JavaScript über C++ entfernen
linktitle: Pivot Verbindung entfernen
type: docs
weight: 30
url: /de/javascript-cpp/remove-pivot-connection/
description: Erfahren Sie, wie Sie die Pivot Verbindung mit Aspose.Cells for JavaScript über C++ entfernen.
keywords: Pivot Verbindung ohne Office 2013, Office 2016, Office 2019 und Office 365 JavaScript über C++ entfernen.
---

## **Mögliche Verwendungsszenarien**

Wenn Sie einen Slicer und eine Pivot-Tabelle in Excel entkoppeln möchten, klicken Sie mit der rechten Maustaste auf den Slicer und wählen Sie "Berichtverbindungen...". In der Optionsliste können Sie die Checkbox bedienen. Ebenso, wenn Sie einen Slicer und eine Pivot-Tabelle programmgesteuert mit der Aspose.Cells for JavaScript API über C++ entkoppeln möchten, verwenden Sie bitte die [**Slicer.removePivotConnection(PivotTable)**](https://reference.aspose.com/cells/javascript-cpp/slicer/#removePivotConnection-pivottable-) Methode. Damit werden der Slicer und die Pivot-Tabelle entkoppelt.

## **Slicer und Pivot-Tabelle dissoziieren**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](remove-pivot-connection.xlsx), die einen bestehenden Slicer enthält. Er greift auf die Slicer zu und trennt dann den Slicer von der Pivot-Tabelle. Schließlich speichert er die Arbeitsmappe als [Ausgabedatei Excel](remove-pivot-connection-out.xlsx).

## **Beispielcode**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Remove Pivot Connection</title>
    </head>
    <body>
        <h1>Remove Pivot Connection Example</h1>
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Access the first PivotTable inside the PivotTable collection.
            const pivotTable = worksheet.pivotTables.get(0);

            // Access the first slicer inside the slicer collection.
            const slicer = worksheet.slicers.get(0);

            // Remove PivotTable connection.
            slicer.removePivotConnection(pivotTable);

            // Save the workbook in output XLSX format.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'remove-pivot-connection-out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Pivot connection removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

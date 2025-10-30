---
title: Rendern von Office Add Ins beim Konvertieren von Excel nach PDF mit JavaScript über C++
linktitle: Office Add Ins beim Konvertieren von Excel in PDF rendern
type: docs
weight: 100
url: /de/javascript-cpp/render-office-add-ins-while-converting-excel-to-pdf/
---

## **Mögliche Verwendungsszenarien**

Früher konnte Aspose.Cells Office-Add-Ins beim Speichern einer Excel-Datei in PDF-Format nicht rendern. Jetzt funktioniert es einwandfrei. Es sind keine speziellen Methoden oder Eigenschaften erforderlich, um Office-Add-Ins im Ausgabe-PDF zu rendern. Speichern Sie einfach Ihre Excel-Datei im PDF-Format, und die Office-Add-Ins werden gerendert.

## **Office-Add-Ins beim Konvertieren von Excel in PDF anzeigen**

Das folgende Beispiel speichert die [Beispiel-Excel-Datei](60489769.xlsx), die Office-Add-Ins enthält. Bitte sehen Sie sich das [Ausgabe-PDF, das mit der früheren Version (z.B. 17.11) generiert wurde](60489770.pdf), und das [Ausgabe-PDF, das mit der neueren Version (z.B. 17.12 und später) erstellt wurde](60489771.pdf). Das Ausgabe-PDF der vorherigen Version ist Leer, während das neuere eine Office-Add-In anzeigt.

## **Beispielcode**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Render Office Add-Ins to PDF Example</title>
    </head>
    <body>
        <h1>Render Office Add-Ins to PDF Example</h1>
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

            // Get Aspose.Cells version (converted from getVersion())
            const version = AsposeCells.CellsHelper.version;

            // Save workbook to PDF format
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = `output-${version}.pdf`;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Saved to PDF successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

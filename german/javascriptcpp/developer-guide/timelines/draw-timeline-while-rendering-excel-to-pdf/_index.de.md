---
title: Zeitleiste beim Rendern von Excel in PDF mit JavaScript via C++ zeichnen
linktitle: Zeitleiste beim Rendern von Excel in PDF zeichnen
type: docs
weight: 60
url: /de/javascript-cpp/draw-timeline-while-rendering-excel-to-pdf/
description: Verwalten Sie Zeitachsen von Excel Dateien mit Aspose.Cells for JavaScript via C++.
keywords: Rendering der Zeitleiste nach PDF ohne Office 2013, Office 2016, Office 2019 und Office 365 JavaScript via C++
---

## **Zeitleiste beim Rendern von Excel in PDF zeichnen**
Wenn Sie eine Excel-Datei haben, die eine Zeitleiste enthält, und Sie möchten die Excel-Datei mit den Zeitleisteneinstellungen in PDF exportieren, unterstützt Aspose.Cells for JavaScript via C++ dies jetzt standardmäßig. Sie exportieren einfach die Excel-Datei mit Zeitleiste nach PDF, und das erzeugte PDF zeigt die Zeitleiste an.

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](input.xlsx), die eine vorhandene Zeitachse enthält. Anschließend speichert er die Arbeitsmappe als [ausgegebene PDF-Datei](out.pdf). Der folgende Screenshot vergleicht die Quell-Excel-Datei und die generierte PDF-Datei.

<img src="out.png" width="60%">

## **Beispielcode**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Saving the workbook to PDF format (browser)
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

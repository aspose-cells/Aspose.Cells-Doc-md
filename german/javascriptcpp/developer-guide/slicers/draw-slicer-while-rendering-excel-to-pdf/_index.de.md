---
title: Slicer zeichnen beim Rendern von Excel zu PDF
type: docs
weight: 60
url: /de/javascript-cpp/draw-slicer-while-rendering-excel-to-pdf/
---

## **Slicer zeichnen beim Rendern von Excel zu PDF**
Wenn Sie eine Excel-Datei mit einem Slicer haben und diese mit den Slicer-Einstellungen nach PDF exportieren möchten, unterstützt Aspose.Cells for JavaScript über C++ dies jetzt standardmäßig. Sie exportieren einfach die Excel-Datei mit Slicer als PDF, und das erzeugte PDF zeigt den angewendeten Slicer.

Der folgende Beispielcode lädt die [Beispieldatei](94044165.xlsx), die bereits einen Slicer enthält. Dann speichert er die Arbeitsmappe als [Ausgabe-PDF-Datei](94044166.pdf). Der folgende Screenshot vergleicht die Quell-Excel-Datei und die generierte PDF-Datei.

![todo:image_alt_text](draw-slicer-while-rendering-excel-to-pdf_1.jpg)

## **Beispielcode**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Save as PDF</title>
    </head>
    <body>
        <h1>Save Excel as PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
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

            // Instantiating a Workbook object by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save the workbook to PDF format
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SampleSlicerChart.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

---
title: Rita Slicer vid rendering av Excel till PDF
type: docs
weight: 60
url: /sv/javascript-cpp/draw-slicer-while-rendering-excel-to-pdf/
---

## **Rita Slicer vid rendering av Excel till PDF**
Om du har en Excel-fil som har slicer applicerad och du vill exportera Excel till PDF med slicer-inställningarna, stöder Aspose.Cells for JavaScript via C++ detta nu som standard. Exportera helt enkelt Excel-filen med slicer till PDF, den genererade PDF:en visar slicern applicerad.

Följande exempelkod laddar in [exempel Excel-filen](94044165.xlsx) som innehåller en befintlig slicer. Den sparar sedan arbetsboken som [utmatnings PDF-filen](94044166.pdf). Följande skärmdump jämför käll-Excel-filen och den genererade PDF-filen.

![todo:image_alt_text](draw-slicer-while-rendering-excel-to-pdf_1.jpg)

## **Exempelkod**
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

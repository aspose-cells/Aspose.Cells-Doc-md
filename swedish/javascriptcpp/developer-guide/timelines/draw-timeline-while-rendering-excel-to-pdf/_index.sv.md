---
title: Rita tidslinje när du renderar Excel till PDF med JavaScript via C++
linktitle: Rita tidslinje vid rendering av Excel till PDF
type: docs
weight: 60
url: /sv/javascript-cpp/draw-timeline-while-rendering-excel-to-pdf/
description: Hantera tidslinjer för Excel filer med Aspose.Cells for JavaScript via C++.
keywords: Rendera tidslinje till PDF utan Office 2013, Office 2016, Office 2019 och Office 365 JavaScript via C++
---

## **Rita tidslinje vid rendering av Excel till PDF**
Om du har en Excel-fil med en tillämpad tidslinje och du vill exportera Excel till PDF med tidslinjeinställningarna, stöder Aspose.Cells for JavaScript via C++ detta nu som standard. Du exporterar enkelt Excel-filen med tidslinje till PDF, och den genererade PDF:en visar den tillämpade tidslinjen.

Följande exempelkod laddar in den [exempel-Excel-filen](input.xlsx) som innehåller en befintlig tidslinje. Sedan sparar den arbetsboken som [utmatnings-PDF-filen](out.pdf). Följande skärmbild jämför käll-Excel-filen och den genererade PDF-filen.

<img src="out.png" width="60%">

## **Exempelkod**
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

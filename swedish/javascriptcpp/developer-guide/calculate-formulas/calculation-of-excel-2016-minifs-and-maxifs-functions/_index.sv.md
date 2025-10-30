---
title: Beräkning av Excel 2016 MINIFS och MAXIFS funktioner med JavaScript via C++
description: Denna artikel introducerar hur man använder Aspose.Cells biblioteket för att beräkna MINIFS och MAXIFS funktioner i Microsoft Excel 2016 med JavaScript via C++. Ladda en befintlig Excel fil eller skapa en ny, och använd Aspose.Cells metoder för att beräkna dessa funktioner och spara resultaten till disk.
keywords: Aspose.Cells, Excel, 2016, MINIFS funktion, MAXIFS funktion, beräkning JavaScript via C++
type: docs
weight: 300
url: /sv/javascript-cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/
---

## **Möjliga användningsscenario**
Microsoft Excel 2016 stöder MINIFS och MAXIFS funktioner. Dessa funktioner stöds inte i Excel 2013 eller tidigare versioner. Aspose.Cells for JavaScript via C++ stöder också beräkning av dessa funktioner. Följande skärmbild visar användningen av dessa funktioner. Läs de röda kommentarerna i skärmbilden för att förstå hur dessa funktioner fungerar.

![todo:image_alt_text](calculation-of-excel-2016-minifs-and-maxifs-functions_1.png)

## **Beräkning av Excel 2016 MINIFS och MAXIFS funktioner**
Följande exempel kod laddar [exempel excel-fil](5115149.xlsx) och anropar [Workbook.calculateFormula()](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) metoden för att utföra formelberäkningen via Aspose.Cells for JavaScript via C++, och sparar sedan resultaten i [utdata PDF](5115154.pdf).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>MINIFS and MAXIFS Calculation to PDF</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions } = AsposeCells;

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

            // Load your source workbook containing MINIFS and MAXIFS functions
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Perform Aspose.Cells formula calculation
            workbook.calculateFormula();

            // Save the calculations result in pdf format
            const options = new PdfSaveOptions();
            options.onePagePerSheet = true;

            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputMINIFSAndMAXIFS.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF Result';

            document.getElementById('result').innerHTML = '<p style="color: green;">Calculation and conversion completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

---
title: Rendera solid rutenät medan du konverterar Excel till PDF med JavaScript via C++
linktitle: Rendera Solid Gridline när du konverterar Excel till PDF
type: docs
weight: 390
url: /sv/javascript-cpp/render-solid-gridline-while-converting-excel-to-pdf/
description: Lär dig hur man renderar solida rutnätslinjer när man konverterar Excel till PDF med Aspose.Cells for JavaScript via C++. 
keywords: Rendera solid rutnätslinje till PDF JavaScript via C++, konvertera Excel till PDF med solid rutnätslinje JavaScript via C++, PdfSaveOptions för solid rutnätslinje JavaScript via C++ 
---

För kompatibilitet med äldre versioner renderar Aspose.Cells rutnätslinjer som prickade linjer som standard vid konvertering av Excel till PDF. Moderna Excel-versioner visar dock rutnätslinjer som solid linje idag.

Med alternativet [PdfSaveOptions.gridlineTypes](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions), kan Aspose.Cells for JavaScript via C++ också rendera rutnätslinjer som solida linjer.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Generate PDF with Gridlines</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, Utils } = AsposeCells;

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

            // Loads the workbook which contains hidden external links (as in original JavaScript example)
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create an empty Workbook
            const wb = new Workbook();

            // Prepare data
            const worksheet = wb.worksheets.get(0);
            const cell = worksheet.cells.get("D9");
            cell.value = "gridline";

            // Enable to print gridline
            worksheet.pageSetup.printGridlines = true;

            // Set to render gridline as solid line
            const pdfSaveOptions = new PdfSaveOptions();
            pdfSaveOptions.gridlineType = AsposeCells.GridlineType.Hair;

            // Save the pdf file with PdfSaveOptions
            const outputData = wb.save(SaveFormat.Pdf, pdfSaveOptions);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'test_Cs.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

![solid-gridline.png](solid-gridline.png)

---
title: Save Specified Worksheets to PDF with JavaScript via C++
linktitle: Save Specified Worksheets to PDF
type: docs
weight: 140
url: /javascript-cpp/save-specified-worksheets-to-pdf/
description: Learn how to save specified worksheets to PDF using Aspose.Cells for JavaScript via C++. 
---

By default, Aspose.Cells saves all **visible** worksheets in a workbook to a PDF file. With [**PdfSaveOptions.sheetSet**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#sheetSet--) option, you can save specified worksheets to a PDF file. e.g. you can save the active worksheet to PDF, save all worksheets (both visible and hidden worksheets) to PDF, save custom multiple worksheets to PDF.

## **Save Active Worksheet to PDF**

If you want to only export the active sheet to PDF, you can achieve this by passing [**SheetSet.active**](https://reference.aspose.com/cells/javascript-cpp/sheetset/#active--) to [**PdfSaveOptions.sheetSet**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#sheetSet--) option.

The sheet `Sheet2` is the active sheet of the source file [sheetset-example.xlsx](sheetset-example.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells SheetSet to PDF Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>SheetSet to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Convert to PDF</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, SheetSet } = AsposeCells;
        
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

            // Prepare PdfSaveOptions and set active sheet set
            const pdfSaveOptions = new PdfSaveOptions();
            pdfSaveOptions.sheetSet = SheetSet.active;

            // Save workbook to PDF using PdfSaveOptions
            const outputData = workbook.save(SaveFormat.Pdf, pdfSaveOptions);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```

## **Save All Worksheets to PDF**

[**SheetSet.visible**](https://reference.aspose.com/cells/javascript-cpp/sheetset/#visible--) indicates visible sheets in a workbook, and [**SheetSet.all**](https://reference.aspose.com/cells/javascript-cpp/sheetset/#all--) indicates all sheets including both visible sheets and hidden/invisible sheets in a workbook. If you want to export all sheets to PDF, you can just pass  [**SheetSet.all**](https://reference.aspose.com/cells/javascript-cpp/sheetset/#all--) to [**PdfSaveOptions.sheetSet**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#sheetSet--) option.

The source file [sheetset-example.xlsx](sheetset-example.xlsx) contains all four sheets with hidden sheet `Sheet3`.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells: SheetSet to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, SheetSet, Utils } = AsposeCells;
        
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

            // Open the template excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Set all sheets to output
            const pdfSaveOptions = new PdfSaveOptions();
            pdfSaveOptions.sheetSet = SheetSet.all;

            // Save the pdf file with PdfSaveOptions
            const outputData = workbook.save(SaveFormat.Pdf, pdfSaveOptions);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

## **Save Specified Worksheets to PDF**

If you want to export desired/custom multiple sheets to PDF, you can achieve this by passing multiple sheet indices to [**PdfSaveOptions.sheetSet**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#sheetSet--) option.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Specific Sheets to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, PdfSaveOptions, SheetSet, SaveFormat, Utils } = AsposeCells;
        
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

            // Opening the Excel file through the file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Set custom multiple sheets (Sheet1, Sheet3) to output
            const sheetSet = new SheetSet([0, 2]);
            const pdfSaveOptions = new PdfSaveOptions();
            pdfSaveOptions.sheetSet = sheetSet;

            // Save the pdf file with PdfSaveOptions
            const outputData = workbook.save(SaveFormat.Pdf, pdfSaveOptions);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF created successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```

## **Reorder Worksheets to PDF**

If you want to reorder sheets (e.g. in reverse order) to PDF without modifying the source file, you can achieve this by passing reordered sheet indices to [**PdfSaveOptions.sheetSet**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#sheetSet--) option.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>SheetSet to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, SheetSet, Utils } = AsposeCells;
        
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

            // Instantiating a Workbook object by opening the Excel file from the file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Reorder sheets(Sheet1, Sheet2, Sheet3, Sheet4) to sheets(Sheet4, Sheet3, Sheet2, Sheet1)
            const sheetSet = new SheetSet([3, 2, 1, 0]);
            const pdfSaveOptions = new PdfSaveOptions();
            pdfSaveOptions.sheetSet = sheetSet;

            // Save the pdf file with PdfSaveOptions
            const outputData = workbook.save(SaveFormat.Pdf, pdfSaveOptions);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF created successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}} 

If your spreadsheet contains formulas, it is best to call [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) just before rendering the spreadsheet to PDF format. Doing so will ensure that the formula dependent values are recalculated, and the correct values are rendered in the PDF.

{{% /alert %}}
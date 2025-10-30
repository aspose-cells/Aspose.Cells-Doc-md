---
title: Spara specificerade kalkylblad till PDF med JavaScript via C++
linktitle: Spara angivna arkpapper till PDF
type: docs
weight: 140
url: /sv/javascript-cpp/save-specified-worksheets-to-pdf/
description: Lär dig att spara angivna kalkylblad till PDF med hjälp av Aspose.Cells for JavaScript via C++. 
---

Som standard sparar Aspose.Cells alla **synliga** kalkylblad i ett arbetsbok till en PDF-fil. Med [**PdfSaveOptions.sheetSet**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#sheetSet--) -alternativet kan du spara angivna kalkylblad till en PDF-fil. Till exempel kan du spara det aktiva kalkylbladet till PDF, spara alla kalkylblad (både synliga och dolda) till PDF, spara anpassade flera kalkylblad till PDF.

## **Spara aktivt arkpapp till PDF**

Om du bara vill exportera det aktiva bladet till PDF kan du uppnå detta genom att ange [**SheetSet.active**](https://reference.aspose.com/cells/javascript-cpp/sheetset/#active--) till [**PdfSaveOptions.sheetSet**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#sheetSet--)-alternativet.

Arbetsbladet `Sheet2` är det aktiva bladet i källfilen [sheetset-example.xlsx](sheetset-example.xlsx).

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

## **Spara alla arbetsblad till PDF**

[**SheetSet.visible**](https://reference.aspose.com/cells/javascript-cpp/sheetset/#visible--) indikerar synliga blad i en arbetsbok, och [**SheetSet.all**](https://reference.aspose.com/cells/javascript-cpp/sheetset/#all--) indikerar alla blad inklusive både synliga och dolda/osynliga blad i en arbetsbok. Om du vill exportera alla blad till PDF kan du bara skicka [**SheetSet.all**](https://reference.aspose.com/cells/javascript-cpp/sheetset/#all--) till [**PdfSaveOptions.sheetSet**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#sheetSet--) alternativet.

Källfilen [sheetset-example.xlsx](sheetset-example.xlsx) innehåller alla fyra ark med dolt ark `Ark3`.

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

## **Spara angivna arbetsblad som PDF**

Om du vill exportera önskat/anpassat flera blad till PDF kan du göra detta genom att ange flera bladindextal till [**PdfSaveOptions.sheetSet**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#sheetSet--)-alternativet.

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

## **Omordna arbetsblad till PDF**

Om du vill omordna blad (t.ex. i omvänd ordning) till PDF utan att ändra källfilen kan du uppnå detta genom att skicka omordnade bladindextal till [**PdfSaveOptions.sheetSet**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#sheetSet--) alternativet.

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

Om ditt kalkylblad innehåller formler, är det bäst att anropa [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) strax innan du renderar kalkylbladet till PDF-format. Genom att göra det säkerställs att formelberoende värden beräknas om och de korrekta värdena renderas i PDF-filen.

{{% /alert %}}

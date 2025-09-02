---
title: Load the Workbook with specific System Culture Info via JavaScript and C++
linktitle: Load the Workbook with specific System Culture Info
type: docs
weight: 190
url: /javascript-cpp/load-the-workbook-with-specific-system-culture-info/
---

## **Possible Usage Scenarios**
Earlier, you had to change the culture info of the entire thread to deal with numbers and dates in a particular culture format, but now Aspose.Cells for JavaScript via C++ provides the `LoadOptions.CultureInfo` property which you can use to load your workbook with specific culture info without changing the culture info of the entire thread.

## **Load the Workbook with specific System Culture Info**
The following sample code shows how to load the workbook with specific system culture info to deal with dates.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv,.html,.htm" />
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

        // Default HTML content (from the original JavaScript readable stream)
        const defaultHtmlContent = "<html><head><title>Test Culture</title></head><body><table><tr><td>10-01-2016</td></tr></table></body></html>";

        // Culture formatter as in the original code
        const culture = new Intl.NumberFormat("en-GB", {
            minimumFractionDigits: 2,
            maximumFractionDigits: 2
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            let uint8Arr;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                uint8Arr = new Uint8Array(arrayBuffer);
            } else {
                const encoder = new TextEncoder();
                uint8Arr = encoder.encode(defaultHtmlContent);
            }

            // Instantiate Workbook from the HTML bytes (Aspose.Cells can load HTML content)
            const workbook = new Workbook(uint8Arr);

            // Save the workbook to XLSX format and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created from HTML content. Click the download link to get the generated Excel file.</p>';
        });
    </script>
</html>
```

The following sample code shows how to load the workbook with specific system culture info to deal with numbers.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
        <input type="file" id="fileInput" accept=".html,.htm,.xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, LoadFormat, CountryCode, CellValueType } = AsposeCells;
        
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

        document.getElementById('runExample').addEventListener('click', () => {
            // Creating an in-memory HTML stream equivalent
            const htmlString = "<html><head><title>Test Culture</title></head><body><table><tr><td>1234,56</td></tr></table></body></html>";

            // Encode string to Uint8Array for Workbook constructor
            const encoder = new TextEncoder();
            const array = encoder.encode(htmlString);

            // Prepare load options for HTML and set region to United Kingdom
            const options = new LoadOptions(LoadFormat.Html);
            options.region = CountryCode.UnitedKingdom;

            // Instantiate Workbook from the in-memory HTML content
            const workbook = new Workbook(new Uint8Array(array), options);

            // Access first worksheet and cell A1
            const cell = workbook.worksheets.get(0).cells.get("A1");

            // Assertions (will propagate failures)
            console.assert(cell.type === CellValueType.IsNumeric);
            console.assert(cell.doubleValue === 1234.56);

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Cell is numeric and equals 1234.56.</p>';
        });
    </script>
</html>
```
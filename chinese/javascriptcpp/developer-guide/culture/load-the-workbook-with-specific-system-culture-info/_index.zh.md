---
title: 用特定系统文化信息加载工作簿via JavaScript和C++
linktitle: 使用特定系统的区域设置信息加载工作簿
type: docs
weight: 190
url: /zh/javascript-cpp/load-the-workbook-with-specific-system-culture-info/
---

## **可能的使用场景**
以前，你需要更改整个线程的文化信息以处理特定文化格式的数字和日期，但现在Aspose.Cells for JavaScript通过C++提供了`LoadOptions.CultureInfo`属性，可以在不更改整个线程文化信息的情况下加载具有特定文化信息的工作簿。

## **使用特定系统的区域设置信息加载工作簿**
下列示例代码演示如何使用特定系统文化信息加载工作簿以处理日期。

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

下列示例代码演示如何使用特定系统文化信息加载工作簿以处理数字。

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

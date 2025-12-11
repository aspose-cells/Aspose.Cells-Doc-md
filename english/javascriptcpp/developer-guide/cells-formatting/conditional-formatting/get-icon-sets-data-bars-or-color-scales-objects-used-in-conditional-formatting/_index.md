---
title: Get Icon Sets, Data Bars or Color Scales Objects used in Conditional Formatting
linktitle: Get Icon Sets, Data Bars or Color Scales Objects used in Conditional Formatting
description: Learn how to use Aspose.Cells for JavaScript via C++ to retrieve icon sets, data bars, and color scale objects in conditional formatting from spreadsheet files.
keywords: Aspose.Cells, Conditional Formatting, Icon Set, Data Bar, Color Scale, Spreadsheet, JavaScript via C++
type: docs
weight: 10
url: /javascript-cpp/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/
---

{{% alert color="primary" %}}  

Sometimes, you need to retrieve icon sets that are used in the conditional formatting of a cell or a range of cells and you want to create an image file based on them. You might need to read the data bars or color scales used in the conditional formatting. Aspose.Cells supports this feature.

{{% /alert %}}  

The following code sample shows how to read icon sets that are used for conditional formatting. With Aspose.Cells' simple API, the icon set's image data is saved as an image.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Aspose.Cells Example - Extract Conditional Formatting Icon</title>
    </head>
    <body>
        <h1>Extract Conditional Formatting Icon</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;
        
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
            const resultEl = document.getElementById('result');

            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Open workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Get the A1 cell
            const cell = sheet.cells.get("A1");

            // Get the conditional formatting result object
            const cfr = cell.conditionalFormattingResult;

            // Get the icon set
            const icon = cfr.conditionalFormattingIcon;

            // Get image data from the icon and create a downloadable blob
            const imageData = icon.imageData;
            const blob = new Blob([imageData], { type: 'image/jpeg' });

            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'imgIcon.out.jpg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Extracted Icon Image';

            resultEl.innerHTML = '<p style="color: green;">Icon image extracted. Click the download link to save the image.</p>';
        });
    </script>
</html>
```
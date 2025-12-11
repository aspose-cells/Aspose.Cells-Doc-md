---
title: Export Similar Border Style When Border Style Is Not Supported by Web Browsers with JavaScript via C++
linktitle: Export Similar Border Style When Border Style Is Not Supported by Web Browsers
type: docs
weight: 70
url: /javascript-cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
description: Learn how to export borders that are not supported by web browsers when converting Excel files to HTML using Aspose.Cells for JavaScript via C++.
---

## **Possible Usage Scenarios**

Microsoft Excel supports some types of dashed borders that are not supported by web browsers. When you convert such an Excel file into HTML using Aspose.Cells for JavaScript via C++, those borders are removed. However, Aspose.Cells can also support the display of such borders with the [**HtmlSaveOptions.exportSimilarBorderStyle**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportSimilarBorderStyle--) property. Set its value to **true**, and the unsupported borders will also be exported to the HTML file.

## **Export Similar Border Style When Border Style Is Not Supported by Web Browsers**

The following sample code loads the [sample Excel file](64716806.xlsx) that contains some unsupported borders, as shown in the screenshot below. The screenshot further illustrates the effect of the [**HtmlSaveOptions.exportSimilarBorderStyle**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportSimilarBorderStyle--) property in the [output HTML](64716804.zip).

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **Sample Code**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Export Similar Border Style Example</title>
    </head>
    <body>
        <h1>Export Similar Border Style Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions } = AsposeCells;
        
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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify HTML Save Options – Export Similar Border Style
            const opts = new HtmlSaveOptions();
            opts.exportSimilarBorderStyle = true;

            // Save the workbook in HTML format with the specified HTML Save Options
            const outputData = workbook.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputExportSimilarBorderStyle.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Export completed successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```
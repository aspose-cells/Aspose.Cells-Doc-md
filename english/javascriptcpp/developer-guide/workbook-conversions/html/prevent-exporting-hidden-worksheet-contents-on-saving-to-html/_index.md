---
title: Prevent Exporting Hidden Worksheet Contents on Saving to HTML with JavaScript via C++
linktitle: Prevent Exporting Hidden Worksheet Contents on Saving to HTML
type: docs
weight: 210
url: /javascript-cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/
description: Learn how to prevent exporting hidden worksheet contents when saving Excel files to HTML using Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}

You can save Excel workbooks to HTML. However, if the workbook contains hidden worksheets, Aspose.Cells by default exports the hidden worksheet contents to the HTML output (**_files**) directory, which contains files such as worksheets, images, *tabstrip.htm*, *stylesheet.css*, etc. Sometimes, exporting the content of the hidden worksheets in this way isn’t appropriate. For example, if the hidden worksheet contains images that should not be exported to the **_files** directory.

{{% /alert %}}

Aspose.Cells for JavaScript via C++ provides the [**HtmlSaveOptions.exportHiddenWorksheet**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportHiddenWorksheet--) property. By default, it is set to **true**, and hidden worksheets are exported to HTML. If you set it to **false**, Aspose.Cells will not export hidden worksheet contents.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - HTML Without Hidden Content</title>
    </head>
    <body>
        <h1>Save Workbook as HTML Without Hidden Worksheet Content</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions, Utils } = AsposeCells;
        
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
            
            // Create HtmlSaveOptions and do not export hidden worksheet contents
            const options = new HtmlSaveOptions();
            options.exportHiddenWorksheet = false;
            
            // Save workbook to HTML format using the options
            const outputData = workbook.save(SaveFormat.Html, options);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'HtmlWithoutHiddenContent_out.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';
            
            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook saved to HTML without hidden content. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
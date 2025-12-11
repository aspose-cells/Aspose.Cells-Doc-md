---
title: Specify how to cross string in output HTML using HtmlCrossType with JavaScript via C++
linktitle: Specify how to cross string in output HTML using HtmlCrossType
type: docs
weight: 140
url: /javascript-cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
description: Learn how to control string overflow in HTML output by specifying HtmlCrossType in Aspose.Cells for JavaScript via C++.
---

## **Possible Usage Scenarios**

When a cell contains text or a string that is larger than the width of the cell, the string overflows if the next cell in the next column is null or empty. When you save your Excel file into HTML, you can control this overflow by specifying the cross type using the [**HtmlCrossType**](https://reference.aspose.com/cells/javascript-cpp/htmlcrosstype) enumeration. It has the following values:

- **HtmlCrossType.Default**: Display like MS Excel; depends on the next cell. If the next cell is null, the string will cross; otherwise, it will be truncated.

- **HtmlCrossType.MSExport**: Display the string as MS Excel does when exporting to HTML.

- **HtmlCrossType.Cross**: Display HTML cross string; the performance for creating large HTML files will be more than ten times faster than setting the value to Default or FitToCell.

- **HtmlCrossType.FitToCell**: Only display the string within the width of the cell.

## **Specify how to cross string in output HTML using HtmlCrossType**

The following sample code loads the [sample Excel file](51740732.xlsx) and saves it to HTML format by specifying different [**HtmlCrossType**](https://reference.aspose.com/cells/javascript-cpp/htmlcrosstype). Please download the [output HTML files](51740734.zip) generated with this code. The sample Excel file contains the image bordered in red, as shown in the screenshot, which demonstrates the effect of the [**HtmlCrossType**](https://reference.aspose.com/cells/javascript-cpp/htmlcrosstype) values on output HTML.

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Sample Code**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Export HTML Cross String Type Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions, HtmlCrossType, Utils } = AsposeCells;
        
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify HTML Cross Type via HtmlSaveOptions
            const opts = new HtmlSaveOptions();
            // Applying the sequence of assignments as in the original JavaScript code
            opts.htmlCrossStringType = HtmlCrossType.Default;
            opts.htmlCrossStringType = HtmlCrossType.MSExport;
            opts.htmlCrossStringType = HtmlCrossType.Cross;
            opts.htmlCrossStringType = HtmlCrossType.FitToCell;

            // Save workbook to HTML using the specified options
            const outputData = workbook.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: "text/html" });
            const downloadLink = document.getElementById('downloadLink');
            const fileName = 'out' + opts.htmlCrossStringType + '.htm';
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = fileName;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML exported successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
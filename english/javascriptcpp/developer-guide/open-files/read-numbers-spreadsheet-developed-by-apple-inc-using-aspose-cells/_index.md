---
title: Read Numbers Spreadsheet Developed by Apple Inc. using Aspose.Cells for JavaScript via C++
linktitle: Read Numbers Spreadsheet Developed by Apple Inc. using Aspose.Cells
type: docs
weight: 140
url: /javascript-cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/
description: Learn how to read Numbers spreadsheets developed by Apple Inc. using Aspose.Cells for JavaScript via C++. 
---

## **Possible Usage Scenarios**

Numbers is a spreadsheet application developed by Apple Inc. Aspose.Cells can read Numbers spreadsheets, but it does not support writing to them. It can read Numbers spreadsheets' Data, Style, and Formulas.

## **Read Numbers Spreadsheet Developed by Apple Inc. using Aspose.Cells for JavaScript via C++**

The following sample code loads the [Sample Numbers Spreadsheet](sampleNumbersByAppleInc.numbers) and converts it to [Output PDF Format](outputNumbersByAppleInc.pdf). You will have to use the [**LoadOptions**](https://reference.aspose.com/cells/javascript-cpp/loadoptions) class and specify [**LoadFormat.Numbers**](https://reference.aspose.com/cells/javascript-cpp/loadformat) as a parameter in its constructor to load it successfully. Please download both of them from the given links. You can try the code with any Numbers spreadsheet. Please also read the comments of the code for more help.

## **Sample Code**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Numbers to PDF Example</title>
    </head>
    <body>
        <h1>Convert Apple Numbers to PDF</h1>
        <input type="file" id="fileInput" accept=".numbers" />
        <button id="runExample">Convert to PDF</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFormat } = AsposeCells;
        
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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select a .numbers file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Specify load options to load Numbers spreadsheet
            const opts = new LoadOptions(LoadFormat.Numbers);

            // Load the Numbers spreadsheet in workbook with above load options
            const wb = new Workbook(new Uint8Array(arrayBuffer), opts);

            // Save the workbook to PDF format
            const outputData = wb.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputNumbersByAppleInc.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```
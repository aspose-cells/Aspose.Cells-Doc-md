---
title: Convert Revision of XLSB to XLSM with JavaScript via C++
linktitle: Convert Revision of XLSB to XLSM
type: docs
weight: 290
url: /javascript-cpp/convert-revision-of-xlsb-to-xlsm/
description: Learn how to fully convert revisions of XLSB files into XLSM format using Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}

Aspose.Cells now supports fully converting revisions of XLSB files into XLSM files. Revisions are found inside the path \xl\revisions. You can view them by changing the XLSB file extension to .zip. The \xl\revisions path contains files ending with .bin extensions.

When you convert your XLSB file into an XLSM file using Aspose.Cells, these .bin files successfully convert to .xml files as shown in these two screenshots.

{{% /alert %}}

The following code sample shows you how to convert the XLSB file into XLSM format using Aspose.Cells for JavaScript via C++.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert XLSB to XLSM Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsb,.csv" />
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

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file (.xlsb, .xls, .xlsx).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Open workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save Workbook to XLSM format
            const outputData = workbook.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Converted XLSM File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook converted to XLSM successfully. Click the download link to save the file.</p>';
        });
    </script>
</html>
```
---
title: Editing Hyperlinks of Worksheet
type: docs
weight: 330
url: /javascript-cpp/editing-hyperlinks-of-worksheet/
description: Learn how to edit hyperlinks of a worksheet using Aspose.Cells for JavaScript via the C++ API.
keywords: Edit Hyperlinks, Edit Hyperlinks of Worksheet, Edit hyperlink of Cell, Access all the hyperlinks of the worksheet
---

{{% alert color="primary" %}}  
Aspose.Cells allows you to access all the hyperlinks of the worksheet using the [**Worksheet.hyperlinks**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#hyperlinks--) collection. You can access each hyperlink from this collection one by one and edit its properties.  
{{% /alert %}}  

The following sample code accesses all the hyperlinks of the worksheet and uses their [**Hyperlink.address**](https://reference.aspose.com/cells/javascript-cpp/hyperlink/#address-string-) method to set the hyperlink address to the Aspose website.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Hyperlinks Update Example</title>
    </head>
    <body>
        <h1>Hyperlinks Update Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;
        
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

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Updating all hyperlinks in the worksheet to the specified address
            for (let i = 0; i < worksheet.hyperlinks.count; i++) {
                const hl = worksheet.hyperlinks.get(i);
                hl.address = "http://www.aspose.com";
            }

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Hyperlinks updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
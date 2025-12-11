---
title: Remove Unused Styles inside the Workbook with JavaScript via C++
linktitle: Remove Unused Styles inside the Workbook
type: docs
weight: 340
url: /javascript-cpp/remove-unused-styles-inside-the-workbook/
description: Learn how to remove unused styles from a workbook using Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}  
Unused styles in Excel files not only take up space but also cause performance issues while converting to different formats like PDF, HTML, etc. Aspose.Cells provides the [**Workbook.removeUnusedStyles()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#removeUnusedStyles--) to remove all the unused styles from the workbook.  
{{% /alert %}}  

The following code explains the usage of [**Workbook.removeUnusedStyles()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#removeUnusedStyles--). The code loads the [template Excel file](5115520.xlsx) which you can download from the provided link. It contains an unused style named **AsposeStyle**; this style and all other unused styles will be removed after the execution of the code.  

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Remove Unused Styles</title>
    </head>
    <body>
        <h1>Remove Unused Styles Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Remove all unused styles from the workbook
            workbook.removeUnusedStyles();

            // Save the modified workbook as XLSX and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Unused styles removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
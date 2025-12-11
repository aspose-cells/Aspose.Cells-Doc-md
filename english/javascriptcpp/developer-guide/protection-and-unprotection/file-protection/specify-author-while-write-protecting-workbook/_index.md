---
title: Specify Author while Write Protecting Workbook with JavaScript via C++
linktitle: Specify Author while Write Protecting Workbook
type: docs
weight: 40
url: /javascript-cpp/specify-author-while-write-protecting-workbook/
description: Specify an author name while write protecting a workbook using Aspose.Cells for JavaScript via C++.
---

## **Possible Usage Scenarios**

You can specify an author name while write‑protecting your workbook using Aspose.Cells API. Please use [**Workbook.author**](https://reference.aspose.com/cells/javascript-cpp/writeprotection/#author--) property for this purpose.

## **Specify Author while Write-Protecting Workbook**

The following sample code explains the usage of [**Workbook.author**](https://reference.aspose.com/cells/javascript-cpp/writeprotection/#author--) property. The code creates an empty workbook, write‑protects it with a password, specifies the author name, and saves it as an output Excel file ([output Excel file](67338582.xlsx)). The following screenshot illustrates the effect of the sample code on the output Excel file for your reference.

![todo:image_alt_text](specify-author-while-write-protecting-workbook_1.png)

## **Sample Code**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Specify Author While Write Protecting Workbook</h1>
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
            // Create an empty workbook.
            const workbook = new Workbook();

            // Write-protect the workbook with a password.
            workbook.settings.writeProtection.password = "1234";

            // Specify the author while write-protecting the workbook.
            workbook.settings.writeProtection.author = "SimonAspose";

            // Save the workbook in XLSX format.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSpecifyAuthorWhileWriteProtectingWorkbook.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and write-protected successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
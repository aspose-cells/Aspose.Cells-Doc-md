---
title: Implement 1904 Date System with JavaScript via C++
description: Aspose.Cells is a JavaScript library for working with spreadsheet files. It supports the implementation of the 1904 date system, allowing users to calculate and format based on the January 1, 1904 date system. This article describes how to implement the 1904 date system using the Aspose.Cells library.
keywords: Aspose.Cells, 1904 date system, spreadsheet, calculation, formatting, JavaScript via C++
type: docs
weight: 7000
url: /javascript-cpp/implement-1904-date-system/
---

{{% alert color="primary" %}} 

Microsoft Excel supports two date systems: the 1900 date system (the default date system implemented in Excel for Windows) and the 1904 date system. The 1904 date system is normally used to provide compatibility with Macintosh Excel files and is the default system when you are using Excel for Macintosh. You can set the 1904 date system for Excel files using Aspose.Cells for JavaScript via C++. 

{{% /alert %}} 

To implement the 1904 date system in Microsoft Excel (for example, Microsoft Excel 2003):

1. From the **Tools** menu, select **Options**, and then select the **Calculation** tab.
2. Select the **1904 date system** option.
3. Click **OK**.

|**Selecting 1904 date system in Microsoft Excel**|
| :- |
|![todo:image_alt_text](implement-1904-date-system_1.png)|

See the following sample code demonstrating how to achieve this using Aspose.Cells APIs.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Enable 1904 Date System</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Implement 1904 date system
            workbook.settings.date1904 = true;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Mybook.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">1904 date system enabled. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
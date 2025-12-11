---
title: Hiding the Display of Zero Values in the Worksheet with JavaScript via C++
linktitle: Hiding the Display of Zero Values in the Worksheet
type: docs
weight: 50
url: /javascript-cpp/hiding-the-display-of-zero-values-in-the-worksheet/
description: This article shows sample code that explains how to programmatically hide zero values in an Excel spreadsheet using the JavaScript library via C++.
keywords: hide zero values of excel worksheet in JavaScript via C++
---

{{% alert color="primary" %}} 

Sometimes, you need to hide zero values in a spreadsheet. It might be a personal preference or a formatting standard.

{{% /alert %}} 

To hide zero values in a worksheet in Microsoft Excel (for example, Microsoft Excel 2003):

1. From the **Tools** menu, select **Options**, and then select the **View** tab.
2. Deselect the **Zero values** option.
3. Click **OK**.

Please see the following sample code that demonstrates hiding zeros using Aspose.Cells for JavaScript via C++.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Hide Zero Values Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet of the workbook
            const sheet = workbook.worksheets.get(0);

            // Hide zero values in the sheet
            sheet.displayZeros = false;

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputfile.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
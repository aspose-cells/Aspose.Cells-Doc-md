---
title: AutoFill range of Excel file with JavaScript via C++
linktitle: AutoFill Range
type: docs
weight: 105
url: /javascript-cpp/autofill-ranges/
description: Learn how to perform an autofill operation in a specified range of an Excel file using Aspose.Cells for JavaScript via C++.
---

## **Perform an autofill in the specified range in Excel**

In Excel, select a range, move the mouse to the bottom‑right, and drag the “plus” sign to autofill data.

## **Auto‑Fill Ranges with Aspose.Cells for JavaScript via C++**

The following example shows how to perform an AutoFill operation on a range.

[range_autofill.xlsx](range_autofill.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Range AutoFill Example</title>
    </head>
    <body>
        <h1>Range AutoFill Example</h1>
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

            // Create a Workbook
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            // Get Cells
            const cells = workbook.worksheets.get(0).cells;
            // Create Range
            const src = cells.createRange("C3:C4");
            const dest = cells.createRange("C5:C10");
            // AutoFill
            src.autoFill(dest, AsposeCells.AutoFillType.Series);
            // Save the Workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'range_autofill_result.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">AutoFill completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
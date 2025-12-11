---
title: Page Setup Features with JavaScript via C++
linktitle: Page Setup Features
type: docs
weight: 60
url: /javascript-cpp/page-setup-features/
description: Explore page setup features using Aspose.Cells for JavaScript via C++. Learn how to configure page dimensions, orientations, and settings.
keywords: Page setup features JavaScript via C++, Configure page dimensions JavaScript via C++, Page orientation settings JavaScript via C++
---

## **Introduction**
With Aspose.Cells for JavaScript via C++, you can manipulate various page‑setup features of an Excel workbook. These features include setting page size, orientation, margins, and more. Proper configuration of these features allows for a better printing and viewing experience.

## **Setting Page Size and Orientation**
You can specify the page size and orientation of a worksheet by using the `PageSetup` class. It provides various properties to manage page dimensions and layout.

### **Example Code**
Here’s an example code snippet demonstrating how to set the page size and orientation.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Page Setup Example</title>
    </head>
    <body>
        <h1>Page Setup Example</h1>
        <p>You may optionally upload an existing Excel file to modify. If none is selected, a new workbook will be created.</p>
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
            let workbook;

            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Set the page size to A4 (paperSize = 0)
            worksheet.pageSetup.paperSize = 0;

            // Set the page orientation to Landscape (orientation = 1)
            worksheet.pageSetup.orientation = 1;

            // Save the workbook as XLSX and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'PageSetupExample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page setup updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Setting Margins**
You can also set the margins for the page using the same `PageSetup` class. The margins can be adjusted for the left, right, top, and bottom sides.

### **Example Code**
Here’s how you can set the margins of a worksheet.
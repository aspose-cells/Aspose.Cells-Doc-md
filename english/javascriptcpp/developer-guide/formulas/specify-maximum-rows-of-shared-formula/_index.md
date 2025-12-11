---
title: Specify Maximum Rows of Shared Formula with JavaScript via C++
linktitle: Specify Maximum Rows of Shared Formula
type: docs
weight: 40
url: /javascript-cpp/specify-maximum-rows-of-shared-formula/
description: Learn how to specify the maximum rows for shared formulas using Aspose.Cells for JavaScript via C++.
---

## **Possible Usage Scenarios**  

The default maximum number of rows for the shared formula is 64. It can be any number, e.g., 1000. The performance of the shared formula changes with a different number of rows. Therefore, Aspose.Cells provides the [**WorkbookSettings.maxRowsOfSharedFormula**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#maxRowsOfSharedFormula--) property that can be used to specify the maximum rows of the shared formula. The shared formula will be split into several shared formulae if the total rows of the shared formula are greater than it, as shown in the following screenshot.  

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)  

## **Specify Maximum Rows of Shared Formula**  

The following sample code explains the usage of the [**WorkbookSettings.maxRowsOfSharedFormula**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#maxRowsOfSharedFormula--) property. It sets the maximum rows of the shared formula to 5, adds the shared formula to cell D1 for 100 rows, and saves it to the [output Excel file](61767856.xlsx). If you extract the contents of the output Excel file and check the *sheet1.xml*, you will see the shared formula splits after every 5 rows as highlighted in the above screenshot.  

## **Sample Code**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Specify Maximum Rows Of Shared Formula Example</title>
    </head>
    <body>
        <h1>Specify Maximum Rows Of Shared Formula Example</h1>
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

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new workbook if no file is provided
                workbook = new Workbook();
            }

            // Set the max rows of shared formula to 5
            workbook.settings.maxRowsOfSharedFormula = 5;

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Access cell D1
            const cell = ws.cells.get("D1");

            // Set the shared formula for 100 rows
            cell.sharedFormula = ["=Sum(A1:A2)", 100, 1];

            // Save the output Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSpecifyMaximumRowsOfSharedFormula.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
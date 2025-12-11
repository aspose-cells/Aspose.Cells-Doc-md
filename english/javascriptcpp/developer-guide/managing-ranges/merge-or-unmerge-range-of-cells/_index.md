---
title: Merge or Unmerge Range of Cells with JavaScript via C++
linktitle: Merge or Unmerge Range of Cells
type: docs
weight: 190
url: /javascript-cpp/merge-or-unmerge-range-of-cells/
description: Merge and Unmerge Cells in a Range in Excel with JavaScript via C++ code.
keywords: JavaScript merge and unmerge cells in a range, JavaScript merge and unmerge cells in range, merge and unmerge cells in range with JavaScript, merge and unmerge cells in range using JavaScript, merge and unmerge cells in excel using JavaScript, merge and unmerge cells in excel with JavaScript, JavaScript merge and unmerge cells in excel, JavaScript merge cells in excel, JavaScript unmerge cells in excel, merge cells in range with JavaScript
---

{{% alert color="primary" %}}

You can use Aspose.Cells to merge or unmerge a range of cells. Aspose.Cells provides the [**Range.merge()**](https://reference.aspose.com/cells/javascript-cpp/range/#merge--) and [**Range.unMerge()**](https://reference.aspose.com/cells/javascript-cpp/range/#unMerge--) methods for this purpose. This article explains how to merge a range of cells into a single cell.

{{% /alert %}}

## **Example**

The following sample code first creates a range – A1:D4 – then merges the cells in the range into a single cell using the [**Range.merge()**](https://reference.aspose.com/cells/javascript-cpp/range/#merge--) method. Similarly, you can unmerge cells by creating a range and calling the [**Range.unMerge()**](https://reference.aspose.com/cells/javascript-cpp/range/#unMerge--) method.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create and Merge Range Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        
        let asposeInitialized = false;
        const runButton = document.getElementById('runExample');
        runButton.disabled = true;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
            asposeInitialized = true;
            runButton.disabled = false;
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            if (!asposeInitialized) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Aspose.Cells is not initialized yet. Please wait.</p>';
                return;
            }

            // Creating a workbook
            const workbook = new Workbook();

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Create a range
            const range = worksheet.cells.createRange("A1:D4");

            // Merge range into a single cell
            range.merge();

            // Saving the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and range merged successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
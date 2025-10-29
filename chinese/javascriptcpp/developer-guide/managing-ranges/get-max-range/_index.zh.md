---
title: 使用JavaScript via C++获取工作表中的最大范围
linktitle: 获取工作表中的最大范围
type: docs
weight: 360
url: /zh/javascript-cpp/get-max-range-in-a-worksheet/
description: 本文介绍了如何使用Aspose.Cells for JavaScript via C++获取Excel文件的最大区域、最大数据区域和最大显示区域。
---

{{% alert color="primary" %}}

在从工作表读取数据时，我们需要知道最大的区域。

在从工作表复制所有数据时，我们需要知道最大的区域。

在导出指定区域为HTML和PDF时，我们需要知道最大区域。

Aspose.Cells for JavaScript via C++ 提供了多种查找工作表最大区域的方法。

{{% /alert %}}

## **获取最大范围**
在Aspose.Cells中，如果初始化了[**row**](https://reference.aspose.com/cells/javascript-cpp/row/)和[**column**](https://reference.aspose.com/cells/javascript-cpp/column/)对象，这些行和列将被计入最大区域，即使空行或空列没有数据。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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

            // Loads the workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get all the worksheets in the book.
            const worksheets = workbook.worksheets;
            const sheet = worksheets.get(0);

            // Gets the max data range.
            let maxRow = sheet.cells.maxRow;
            let maxColumn = sheet.cells.maxColumn;
            // The range is A1:B3 (based on maxRow/maxColumn).
            let range = sheet.cells.createRange(0, 0, maxRow + 1, maxColumn + 1);

            // Clear cell A10
            const cell = sheet.cells.get("A10");
            cell.value = null;

            // Recalculate maxRow/maxColumn after clearing
            maxRow = sheet.cells.maxRow;
            maxColumn = sheet.cells.maxColumn;
            // The range is updated (e.g., A1:B10).
            range = sheet.cells.createRange(0, 0, maxRow + 1, maxColumn + 1);

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **获取最大数据范围**
在大多数情况下，我们只需要获取包含所有数据的所有范围，即使范围外的空单元格被格式化。
以及有关形状、表格和数据透视表的设置将被忽略。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
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

            // Instantiate a new Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get all the worksheets in the book.
            const worksheets = workbook.worksheets;
            const sheet = worksheets.get(0);

            // Gets the max data range.
            let maxRow = sheet.cells.maxDataRow;
            let maxColumn = sheet.cells.maxDataColumn;
            // The range is A1:B3 (based on maxRow/maxColumn).
            let range = sheet.cells.createRange(0, 0, maxRow + 1, maxColumn + 1);

            // Clear cell A10 by setting its value to null
            const cell = sheet.cells.get("A10");
            cell.value = null;

            // Recalculate max data range after clearing the cell
            maxRow = sheet.cells.maxDataRow;
            maxColumn = sheet.cells.maxDataColumn;
            // The range is still A1:B3 (after clearing A10).
            range = sheet.cells.createRange(0, 0, maxRow + 1, maxColumn + 1);

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **获取最大显示范围**
当我们将工作表中的所有数据导出到 HTML、PDF 或图像时，需要获取一个包含所有可见对象的区域，包括数据、样式、图形、表格和数据透视表。
以下代码演示如何将最大显示范围渲染为HTML：

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Export Range to HTML</h1>
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

            // Instantiate a new Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get all the worksheets in the book.
            const worksheets = workbook.worksheets;

            // Gets the max display range.
            const range = worksheets.get(0).cells.maxDisplayRange;

            // Save the range to html
            const saveOptions = new AsposeCells.HtmlSaveOptions();
            saveOptions.exportActiveWorksheetOnly = true;
            saveOptions.exportArea = AsposeCells.CellArea.createCellArea(
                range.firstRow,
                range.firstColumn,
                range.firstRow + range.rowCount - 1,
                range.firstColumn + range.columnCount - 1
            );

            // Save the range to HTML format and provide download link
            const outputData = workbook.save(SaveFormat.Html, saveOptions);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'html.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Range exported successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```

这是 [源 Excel 文件](Book1.xlsx)。

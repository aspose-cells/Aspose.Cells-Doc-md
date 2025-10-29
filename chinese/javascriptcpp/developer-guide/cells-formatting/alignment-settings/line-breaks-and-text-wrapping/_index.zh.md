---
title: 行尾和文本换行
linktitle: 行尾和文本换行
description: 如何在JavaScript via C++中使用Aspose.Cells库实现文本换行和自动换行。通过使用Aspose.Cells库，你可以轻松在单元格中插入文本并设置换行方式，如手动换行、自动换行等。本文详细介绍如何实现这些功能，并提供示例代码供参考。
keywords: Aspose.Cells，换行符，文本换行，文本布局 JavaScript via C++
type: docs
weight: 60
url: /zh/javascript-cpp/line-breaks-and-text-wrapping/
---

{{% alert color="primary" %}}
为了确保单元格中的文本可以被读取，可以应用明确的行尾和文本换行。文本换行将单元格中的一行变成了多行，而明确的行尾则将文本换行放在您想要的确切位置。
{{% /alert %}}

## **将单元格中的文本自动换行**
要在单元格中换行，使用 [**Aspose.Cells.Style.isTextWrapped(boolean)**](https://reference.aspose.com/cells/javascript-cpp/style/#isTextWrapped-boolean-) 方法。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Wrapping Text Example</title>
    </head>
    <body>
        <h1>Wrapping Text Example</h1>
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

            if (fileInput.files.length === 0) {
                // No file selected - create a new workbook
            }

            let wb;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                wb = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                wb = new Workbook();
            }

            // Open first Worksheet in the workbook
            const ws = wb.worksheets.get(0);

            // Get Worksheet Cells Collection
            const cell = ws.cells;

            // Increase the width of First Column Width
            cell.columns.get(0).width = 35;

            // Increase the height of first row
            cell.rows.get(0).height = 36;

            // Add Text to the First Cell
            const firstCell = cell.checkCell(0, 0);
            firstCell.value = "I am using the latest version of Aspose.Cells to test this functionality";

            // Make Cell's Text wrap
            const style = firstCell.style;
            style.isTextWrapped = true;
            firstCell.style = style;

            // Save Excel File
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'WrappingText.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


## **使用显式换行符**
你可以在 JavaScript 中使用 '\n' 在单元格中插入显式换行符。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Wrapping Text Example</title>
    </head>
    <body>
        <h1>Wrapping Text Example</h1>
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
            let wb;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                wb = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // No file selected - create a new workbook
                wb = new Workbook();
            }

            // Open first Worksheet in the workbook
            const ws = wb.worksheets.get(0);

            // Get Worksheet Cells Collection
            const cells = ws.cells;

            // Increase the width of First Column Width
            cells.columns.get(0).width = 35;

            // Increase the height of first row
            cells.rows.get(0).height = 65;

            // Add Text to the First Cell with Explicit Line Breaks
            const firstCell = cells.checkCell(0, 0);
            firstCell.putValue("I am using\nthe latest version of \nAspose.Cells to \ntest this functionality");

            // Make Cell's Text wrap
            const style = firstCell.style;
            style.isTextWrapped = true;
            firstCell.style = style;

            // Save Excel File
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'WrappingText.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

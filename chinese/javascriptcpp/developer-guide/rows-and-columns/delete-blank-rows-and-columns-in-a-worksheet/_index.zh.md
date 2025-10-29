---
title: 用JavaScript通过C++删除工作表中的空白行和列
linktitle: 在工作表中删除空行和空列
type: docs
weight: 300
url: /zh/javascript-cpp/delete-blank-rows-and-columns-in-a-worksheet/
description: 学习如何使用Aspose.Cells for JavaScript通过C++删除工作表中的所有空白行和列。 
---

{{% alert color="primary" %}}

可以从工作表中删除所有空白行和列。这在例如从微软Excel文件生成PDF文件时非常有用，只转换包含数据或相关对象的行和列。

使用以下Aspose.Cells方法来删除空行和空列:

1. 要删除空行，请使用[**Cells.deleteBlankRows()**](https://reference.aspose.com/cells/javascript-cpp/cells/#deleteBlankRows--)方法。请注意，对于将要被删除的空行，不仅需要[**Row.isBlank()**](https://reference.aspose.com/cells/javascript-cpp/row/#isBlank--)为true，还必须在这些行中的任何单元格没有可见的注释定义，也不应该和任何数据透视表的范围相交。
2. 要删除空白列，使用 [**Cells.deleteBlankColumns()**](https://reference.aspose.com/cells/javascript-cpp/cells/#deleteBlankColumns--) 方法。

{{% /alert %}}

## 删除空白行的JavaScript代码

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Delete Blank Rows Example</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access worksheets collection
            const sheets = workbook.worksheets;

            // Get first worksheet
            const sheet = sheets.get(0);

            // Delete blank rows from the worksheet
            sheet.cells.deleteBlankRows();

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'mybook.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Blank rows deleted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## 删除空白列的JavaScript代码

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Delete Blank Columns Example</title>
    </head>
    <body>
        <h1>Delete Blank Columns Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create a Worksheets object with reference to the sheets of the Workbook.
            const sheets = workbook.worksheets;

            // Get first Worksheet from WorksheetCollection
            const sheet = sheets.get(0);

            // Delete the Blank Columns from the worksheet
            sheet.cells.deleteBlankColumns();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'mybook.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Blank columns deleted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

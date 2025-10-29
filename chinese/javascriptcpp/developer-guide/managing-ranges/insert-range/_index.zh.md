---
title: 使用JavaScript通过C++插入区域
linktitle: 插入范围
type: docs
weight: 105
url: /zh/javascript-cpp/insert-ranges-to-excel/
description: 学习如何在Excel中插入区域并移动其他数据，使用Aspose.Cells for JavaScript via C++。
---

## **介绍**

在 Excel 中，您可以选择一个范围，然后插入一个范围，并向右或向下移动其他数据。

**![移动选项](InsertRange.png)**

## **使用C++的Aspose.Cells for JavaScript插入区域**

Aspose.Cells for JavaScript via C++ 提供 [Cells.insertRange(CellArea, 数字, ShiftType, boolean)] 方法用于插入区域。

## **插入范围并向右移动单元格**

使用Aspose.Cells插入范围并向右移动单元格的示例代码：

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Instantiate a new Workbook.
            const newWorkbook = new Workbook();

            // Get all the worksheets in the book.
            const worksheets = newWorkbook.worksheets;

            // Get the first worksheet in the worksheets collection.
            const worksheet = newWorkbook.worksheets.get(0);

            // Create a range of cells.
            const sourceRange = worksheet.cells.createRange("A1", "A2");

            // Input some data with some formattings into
            // A few cells in the range.
            sourceRange.get(0, 0).value = "Test";
            sourceRange.get(1, 0).value = "123";

            const ca = AsposeCells.CellArea.createCellArea("A1", "A2");
            worksheet.cells.insertRange(ca, AsposeCells.ShiftType.Right);

            const check = worksheet.cells.get("B1").value === "Test";
            if (check) {
                resultDiv.innerHTML = '<p style="color: green;">Value check passed: B1 === "Test".</p>';
            } else {
                resultDiv.innerHTML = '<p style="color: red;">Value check failed: B1 !== "Test".</p>';
            }

            // Saving the modified new workbook and providing download link
            const outputData = newWorkbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';
        });
    </script>
</html>
```

## **插入范围并向下移动单元格**

使用Aspose.Cells插入范围并向下移动单元格的示例代码：

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Instantiate a new Workbook.
            const newWorkbook = new Workbook();

            // Get all the worksheets in the book.
            const worksheets = newWorkbook.worksheets;

            // Get the first worksheet in the worksheets collection.
            const worksheet = newWorkbook.worksheets.get(0);

            // Create a range of cells.
            const sourceRange = worksheet.cells.createRange("A1", "A2");

            // Input some data with some formattings into
            // A few cells in the range.
            const cell00 = sourceRange.get(0, 0);
            cell00.value = "Test";
            const cell10 = sourceRange.get(1, 0);
            cell10.value = 123;

            const ca = AsposeCells.CellArea.createCellArea("A1", "A2");
            worksheet.cells.insertRange(ca, AsposeCells.ShiftType.Down);

            const check = worksheet.cells.get("A3").value === "Test";
            console.log(check);
            document.getElementById('result').innerHTML = `<p style="color: green;">Check result: ${check}</p>`;

            const outputData = newWorkbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result Excel File';
        });
    </script>
</html>
```

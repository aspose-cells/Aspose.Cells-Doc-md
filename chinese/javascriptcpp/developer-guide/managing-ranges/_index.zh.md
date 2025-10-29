---
title: 使用 JavaScript 通过 C++ 管理范围
linktitle: 范围
type: docs
weight: 105
url: /zh/javascript-cpp/managing-ranges/
description: 学习如何用 C++ 版的 Script 管理 Excel 中的范围。创建范围，设置值、样式，执行各种操作。
---

## **介绍**

在Excel中，可以使用鼠标框选择多个单元格；所选的单元格集合称为“范围”。

例如，您可以在Excel的单元格"A1"中点击左键，然后拖到"C4"单元格。您也可以使用Aspose.Cells for JavaScript通过C++轻松将所选的矩形区域创建为对象。

以下是如何创建范围、放置值、设置样式以及在“范围”对象上执行更多操作的方法。

## **使用Aspose.Cells for JavaScript via C++ 管理范围**

Aspose.Cells提供了一个代表Microsoft Excel文件的类，[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) 类包含一个[**Workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)集合，允许访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)类提供[**cells**](https://reference.aspose.com/cells/javascript-cpp/cells)集合。

### **创建范围**

当您想创建覆盖 A1:C4 的矩形区域时，您可以使用以下代码：

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get Cells (converted from getWorksheets().get(0).getCells() to properties)
            const cells = workbook.worksheets.get(0).cells;

            // Create Range A1:C4
            const range = cells.createRange("A1:C4");

            // Save the workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Range A1:C4 created successfully. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **将值放入范围单元格**

假设您有一个涵盖 A1:C4 的单元格范围。该矩阵形成 4 * 3 = 12 个单元格。单个范围单元格是按顺序排列的：Range[0,0]、Range[0,1]、Range[0,2]、Range[1,0]、Range[1,1]、Range[1,2]、Range[2,0]、Range[2,1]、Range[2,2]、Range[3,0]、Range[3,1]、Range[3,2]。

以下示例展示如何向范围单元格输入一些值。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Range Value Example</title>
    </head>
    <body>
        <h1>Range Value Example</h1>
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
                workbook = new Workbook();
            }

            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            const range = cells.createRange("A1:C4");

            range.get(0, 0).value = "A1";
            range.get(0, 1).value = "B1";
            range.get(0, 2).value = "C1";
            range.get(3, 0).value = "A4";
            range.get(3, 1).value = "B4";
            range.get(3, 2).value = "C4";

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'RangeValueTest.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and ready for download.</p>';
        });
    </script>
</html>
```

### **设置范围单元格的样式**

以下示例演示了如何设置范围内单元格的样式。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Range Style Example</h1>
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
            const resultDiv = document.getElementById('result');

            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Gets Cells
            const cells = workbook.worksheets.get(0).cells;
            // Creates Range
            const range = cells.createRange("A1:C4");
            // Puts value
            range.get(0, 0).value = "A1";
            range.get(3, 2).value = "C4";
            // Sets Style
            let style00 = workbook.createStyle();
            style00.pattern = AsposeCells.BackgroundType.Solid;
            style00.foregroundColor = new AsposeCells.Color(255, 0, 0); // Red
            range.get(0, 0).style = style00;
            let style32 = workbook.createStyle();
            style32.pattern = AsposeCells.BackgroundType.HorizontalStripe;
            style32.foregroundColor = new AsposeCells.Color(0, 255, 0); // Green
            range.get(3, 2).style = style32;
            // Saves the Workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'RangeStyleTest.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook created successfully. Click the download link to save the file.</p>';
        });
    </script>
</html>
```

### **获取范围的当前区域**

CurrentRegion 是一个返回代表当前区域的 Range 对象的属性。 

当前区域是由任意组合空行和空列所限定的范围。只读。

在Excel中，你可以通过以下方法获取当前区域：
1. 用鼠标框选一个区域（范围1）。
2. 点击“主页 - 编辑 - 查找和选择 - 转到特殊 - 当前区域”，或使用“Ctrl+Shift+*”，你会看到Excel自动帮你选择一个区域（范围2）。完成后，范围2即为范围1的当前区域。

请下载以下测试文件，在Excel中打开，用鼠标框选一个区域“A1:D7”，然后点击“Ctrl+Shift+*”，你将看到区域“A1:C3”被选中。

[current_region.xlsx](current_region.xlsx)

现在请运行以下示例，查看它在Aspose.Cells中的工作方式：

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Get Current Region Example</h1>
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

            // Creating a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Get Cells
            const cells = worksheet.cells;

            // Create Range
            const src = cells.createRange("A1:D7");

            // Get CurrentRegion (converted from getCurrentRegion())
            const A1C3 = src.currentRegion;

            // Save the workbook (no modifications were required by original code)
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.current_region.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Current region obtained successfully. Click the download link to download the file.</p>';
        });
    </script>
</html>
```


## **高级主题**
- [Excel文件的自动填充范围](/cells/zh/javascript-cpp/autofill-ranges/)
- [复制Excel的区域](/cells/zh/javascript-cpp/copy-ranges-of-Excel/)
- [仅复制区域数据](/cells/zh/javascript-cpp/copy-range-data-only/)
- [复制具有样式的区域数据](/cells/zh/javascript-cpp/copy-range-data-with-style/)
- [仅复制区域样式](/cells/zh/javascript-cpp/copy-range-style-only/)
- [创建联合范围](/cells/zh/javascript-cpp/create-union-range/)
- [剪切和粘贴范围](/cells/zh/javascript-cpp/cut-and-paste-cells/)
- [删除区域](/cells/zh/javascript-cpp/delete-ranges-from-Excel/)
- [获取区域的地址、单元格计数、偏移、整行和整列](/cells/zh/javascript-cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [插入范围](/cells/zh/javascript-cpp/insert-ranges-to-Excel/)
- [合并或取消合并单元格范围](/cells/zh/javascript-cpp/merge-or-unmerge-range-of-cells/)
- [在工作表中移动单元格范围](/cells/zh/javascript-cpp/move-range-of-cells-in-a-worksheet/)
- [创建工作簿和工作表范围命名](/cells/zh/javascript-cpp/create-workbook-and-worksheet-scoped-named-ranges/)
- [在范围内搜索和替换数据](/cells/zh/javascript-cpp/search-and-replace-data-in-a-range/)

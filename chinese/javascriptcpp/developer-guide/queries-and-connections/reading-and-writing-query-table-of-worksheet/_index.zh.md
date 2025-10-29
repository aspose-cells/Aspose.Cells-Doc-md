---
title: 使用JavaScript通过C++读取和写入工作表的查询表。
linktitle: 工作表的查询表读取和写入
type: docs
weight: 40
url: /zh/javascript-cpp/reading-and-writing-query-table-of-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells提供了Worksheet.QueryTables集合，它按索引返回QueryTable类型的对象。它有以下两个属性

- QueryTable.adjustColumnWidth
- QueryTable.preserveFormatting

这两个都是布尔值。你可以在Microsoft Excel中通过数据 > 连接 > 属性查看它们。

{{% /alert %}}

## 工作表的查询表读取和写入

以下示例读取第一个工作表的第一个QueryTable，并打印两个QueryTable属性，然后将QueryTable.preserveFormatting设置为true。

您可以从以下链接下载用于此代码的源Excel文件和代码生成的输出Excel文件。

- [源Excel文件](5115533.xlsx)
- [输出Excel文件](5115537.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells QueryTable Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample" disabled>Run Example</button>
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
            document.getElementById('runExample').disabled = false;
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

            // Create workbook from source excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first Query Table
            const qt = worksheet.queryTables.get(0);

            // Read Query Table Data (properties converted from getters)
            const adjustColumnWidth = qt.adjustColumnWidth;
            const preserveFormatting = qt.preserveFormatting;

            resultDiv.innerHTML = `<p>Adjust Column Width: ${adjustColumnWidth}</p><p>Preserve Formatting: ${preserveFormatting}</p>`;

            // Now set Preserve Formatting to true (setter converted to property assignment)
            qt.preserveFormatting = true;

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML += '<p style="color: green;">PreserveFormatting set to true. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### 控制台输出



{{< highlight java >}}

Adjust Column Width: True

Preserve Formatting: False

{{< /highlight >}}

## 检索查询表结果范围

Aspose.Cells提供了读取查询表结果范围的选项。以下代码演示了通过读取查询表的结果范围地址来实现此功能。示例文件可以从[这里](72417290.xlsx)下载。

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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const worksheet = workbook.worksheets.get(0);
            const queryTable = worksheet.queryTables.get(0);
            const resultRange = queryTable.resultRange;
            const address = resultRange.address;

            const addressText = (address && typeof address.toString === 'function') ? address.toString() : String(address);
            console.log(addressText);
            document.getElementById('result').innerHTML = `<p>Query table result range address: ${addressText}</p>`;
        });
    </script>
</html>
```

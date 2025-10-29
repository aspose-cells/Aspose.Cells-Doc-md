---
title: 用JavaScript通过C++自动填充Excel文件的范围
linktitle: 自动填充范围
type: docs
weight: 105
url: /zh/javascript-cpp/autofill-ranges/
description: 学习如何使用C++的JavaScript在Excel文件的指定范围内执行自动填充操作。
---

## **在Excel中指定范围执行自动填充**

在Excel中，选择一个范围，将鼠标移动到右下角，然后拖动“加号”以自动填充数据。

## **使用C++的JavaScript自动填充范围**

以下示例显示了如何在范围内执行AutoFill操作，并 

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

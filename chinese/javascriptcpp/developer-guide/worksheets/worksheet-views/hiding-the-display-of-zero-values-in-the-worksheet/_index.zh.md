---
title: 用JavaScript通过C++隐藏工作表中的零值显示
linktitle: 隐藏工作表中零值的显示
type: docs
weight: 50
url: /zh/javascript-cpp/hiding-the-display-of-zero-values-in-the-worksheet/
description: 本文章将为您展示一段示例代码，说明如何通过C++的JavaScript库以编程方式隐藏Excel电子表格中的零值。
keywords: 通过 C++ 使用 Aspose.Cells for JavaScript 在 JavaScript 中隐藏 Excel 工作表的零值
---

{{% alert color="primary" %}} 

有时，您需要在电子表格中隐藏零值。这可能是个人偏好或格式化标准。

{{% /alert %}} 

要在Microsoft Excel中隐藏工作表中的零值（例如Microsoft Excel 2003）：

1. 从**工具**菜单中选择**选项**，然后选择**视图**选项卡。
1. 取消选中**零值**选项。
1. 点击**确定**。

请参阅以下示例代码，演示如何使用 C++ 的 Aspose.Cells for JavaScript 隐藏零值。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Hide Zero Values Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get First worksheet of the workbook
            const sheet = workbook.worksheets.get(0);

            // Hide the zero values in the sheet
            sheet.displayZeros = false;

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputfile.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

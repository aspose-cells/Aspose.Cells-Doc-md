---
title: 用 JavaScript 通过 C++ 实现 1904 日期系统
description: Aspose.Cells 是一个用于操作电子表格文件的 JavaScript 库。它支持实现 1904 日期系统，允许用户基于1904年1月1日的日期进行计算和格式化。本文介绍如何使用 Aspose.Cells 库实现1904日期系统。
keywords: Aspose.Cells、1904 日期系统、电子表格、计算、格式化、JavaScript 通过 C++
type: docs
weight: 7000
url: /zh/javascript-cpp/implement-1904-date-system/
---

{{% alert color="primary" %}} 

Microsoft Excel 支持两种日期系统：1900 日期系统（Excel for Windows 中的默认日期系统）和 1904 日期系统。1904 日期系统通常用于与 Macintosh 版 Excel 文件的兼容，如果你使用的是 Mac 版 Excel，则默认使用该系统。你可以使用 C++ 脚本设置 Excel 文件为 1904 日期系统。 

{{% /alert %}} 

在Microsoft Excel中实现1904日期系统（例如，Microsoft Excel 2003）的方法：

1. 从“工具”菜单中选择“选项”，并选择“计算”选项卡。
1. 选择“1904日期系统”选项。
1. 点击**确定**。

|**在Microsoft Excel中选择1904日期系统**|
| :- |
|![todo:image_alt_text](implement-1904-date-system_1.png)|

请参阅以下示例代码，了解如何使用Aspose.Cells API 实现此功能。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Enable 1904 Date System</h1>
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

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Implement 1904 date system
            workbook.settings.date1904 = true;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Mybook.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">1904 date system enabled. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

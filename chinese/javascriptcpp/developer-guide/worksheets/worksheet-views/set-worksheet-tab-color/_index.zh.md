---
title: 用 JavaScript 和 C++ 设置工作表标签颜色
linktitle: 设置工作表标签颜色
type: docs
weight: 120
url: /zh/javascript-cpp/set-worksheet-tab-color/
description: 本文展示了使用 JavaScript 和 C++ 以编程方式设置 Excel 工作表标签颜色的示例代码。
keywords: 用 C++ 和 JavaScript 设置 Excel 标签颜色的代码
---

{{% alert color="primary" %}}

Aspose.Cells允许您更改单个工作表标签的颜色，使其与其他工作表区分开。例如，您可以将支出设置为红色，销售设置为绿色，资产设置为蓝色，等等。

{{% /alert %}}
## **使用Microsoft Excel设置工作表标签颜色**
1. 在当前工作表底部的标签工作表上右键单击。
1. 选择**标签颜色**。
1. 从调色板中选择一种颜色。
1. 点击**确定**。
## **使用Aspose.Cells设置工作表选项卡颜色**
以下示例代码显示如何使用Aspose.Cells来设置选项卡颜色。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Worksheet Tab Color Example</title>
    </head>
    <body>
        <h1>Set Worksheet Tab Color Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const worksheet = workbook.worksheets.get(0);
            worksheet.tabColor = AsposeCells.Color.Red;
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'worksheettabcolor.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';
            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet tab color set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

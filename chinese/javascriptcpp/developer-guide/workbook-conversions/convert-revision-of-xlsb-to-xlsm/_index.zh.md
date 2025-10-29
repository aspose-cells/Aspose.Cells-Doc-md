---
title: 使用 JavaScript 通过 C++ 将 XLSB 的修订转换为 XLSM
linktitle: 将XLSB文件的修订版本转换为XLSM
type: docs
weight: 290
url: /zh/javascript-cpp/convert-revision-of-xlsb-to-xlsm/
description: 学习如何完全将 XLSB 文件的修订转换为 XLSM 格式，使用 Aspose.Cells for JavaScript 通过 C++。
---

{{% alert color="primary" %}}

Aspose.Cells 现支持完全将 XLSB 文件的修订转换为 XLSM 文件。修订存放在路径 \xl\revisions 内。将 XLSB 文件扩展名改为 ZIP 后可查看这些修订。\xl\revisions 路径内包含以 .bin 结尾的文件。

当你使用 Aspose.Cells 将 XLSB 文件转换为 XLSM 文件时，这些 .bin 文件会成功转换为 .xml 文件，效果如这两张截图所示。

{{% /alert %}}

 以下代码示例演示如何使用 Aspose.Cells for JavaScript 通过 C++ 将 XLSB 文件转换为 XLSM 格式。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert XLSB to XLSM Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsb,.csv" />
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
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file (.xlsb, .xls, .xlsx).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Open workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save Workbook to XLSM format
            const outputData = workbook.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Converted XLSM File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook converted to XLSM successfully. Click the download link to save the file.</p>';
        });
    </script>
</html>
```

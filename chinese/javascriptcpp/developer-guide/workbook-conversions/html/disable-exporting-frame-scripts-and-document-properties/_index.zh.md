---
title: 通过C++中的JavaScript禁用导出框架脚本和文档属性
linktitle: 在保存为HTML时禁用导出框架脚本和文档属性
type: docs
weight: 310
url: /zh/javascript-cpp/disable-exporting-frame-scripts-and-document-properties/
description: 学习在将工作簿转换为HTML时，如何使用C++中的Aspose.Cells for JavaScript禁用导出框架脚本和文档属性。
--- 

{{% alert color="primary" %}}

Aspose.Cells在将工作簿转换为HTML时会导出框架脚本和文档属性。8.6.0版本的C++中的Aspose.Cells for JavaScript增加了一个选项，允许你有选择性地禁用导出框架脚本和文档属性。请使用`HtmlSaveOptions.exportFrameScriptsAndProperties`属性来禁用导出。

{{% /alert %}}

## **禁用导出框架脚本和文档属性**

以下示例代码允许您禁用导出框架脚本和文档属性。一旦您将工作簿转换为HTML，输出文件将不包含任何框架脚本和文档属性。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to HTML Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions, Utils } = AsposeCells;

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

            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Disable exporting frame scripts and document properties
            const options = new HtmlSaveOptions();
            options.exportFrameScriptsAndProperties = false;

            // Save workbook as HTML
            const outputData = workbook.save(SaveFormat.Html, options);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```

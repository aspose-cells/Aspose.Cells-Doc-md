---
title: 在使用C++中的JavaScript保存为HTML时禁用CSS
linktitle: 禁用CSS在保存为HTML时
type: docs
weight: 320
url: /zh/javascript-cpp/disable-css-while-saving-to-html/
description: 学习如何在使用C++中的Aspose.Cells for JavaScript将Excel文件保存为HTML时禁用CSS。 
---

## **可能的使用场景**

当将您的 Excel 文件保存为单页面 HTML 时，通常 CSS 元素会嵌入在 HTML 文件中，并位于 HEAD 段中。如果您将此文件作为电子邮件的内容/正文附件，大多数电子邮件客户端会剥离 CSS 元素，导致排版不正确。Aspose.Cells 24.12 版本引入了一个选项，允许您可选择禁用 CSS，从而使样式可以直接应用于 HTML 元素本身。如果要将 HTML 作为电子邮件内容/正文，请使用 [**HtmlSaveOptions.disableCss**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#disableCss--) 属性并将其设置为 **true**。

## ** 禁用CSS在保存为HTML时**

以下示例代码演示了 [**HtmlSaveOptions.disableCss**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#disableCss--) 属性的用法。 

## **示例代码**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Disable CSS Example</title>
    </head>
    <body>
        <h1>Disable CSS Save Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions } = AsposeCells;

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

            const opts = new HtmlSaveOptions();
            opts.disableCss = true;

            const outputData = workbook.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDisable.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML file generated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

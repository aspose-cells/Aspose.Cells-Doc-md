---
title: 在使用C++中的JavaScript保存为HTML时启用CSS自定义属性
linktitle: 在保存为HTML时启用CSS自定义属性
type: docs
weight: 320
url: /zh/javascript-cpp/enable-css-custom-properties-while-saving-to-html/
description: 学习在使用C++中的Aspose.Cells for JavaScript将Excel文件保存为HTML时，如何启用CSS自定义属性。 
---

## **可能的使用场景**

当您将您的 Excel 文件保存为 HTML 时，对于存在多次出现的同一基础图片的场景，使用自定义属性可以仅保存一次图片数据，从而提升生成 HTML 的性能。请使用 [**HtmlSaveOptions.enableCssCustomProperties**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#enableCssCustomProperties--) 属性并在保存为 HTML 时将其设置为 **true**。
![todo:image_alt_text](enable-css-custom-properties-while-saving-to-html-1.jpg) 


## **在保存为HTML时启用CSS自定义属性**

以下示例代码展示了 [**HtmlSaveOptions.enableCssCustomProperties**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#enableCssCustomProperties--) 属性的用法。截图显示了未将此属性设置为 **true** 时的效果。请下载此代码用的【示例 Excel 文件】(50528260.xlsx) 和生成的【输出 HTML】(50528261.zip) 以供参考。



## **示例代码**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Enable CSS Custom Properties Example</title>
    </head>
    <body>
        <h1>Enable CSS Custom Properties Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create HtmlSaveOptions and set properties (converted from setters to property assignments)
            const opts = new AsposeCells.HtmlSaveOptions();
            opts.exportImagesAsBase64 = true;
            opts.enableCssCustomProperties = true;

            // Save the workbook to HTML using SaveFormat.Html and provided options
            const outputData = workbook.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputEnableCssCustomProperties.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML saved successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

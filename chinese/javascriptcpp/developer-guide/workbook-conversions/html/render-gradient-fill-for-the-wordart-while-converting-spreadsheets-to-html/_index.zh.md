---
title: 在使用 JavaScript 通过 C++ 将电子表格转换为 HTML 时，为 WordArt 渲染渐变填充
linktitle: 在将电子表格转换为HTML格式时渲染文字艺术的渐变填充
type: docs
weight: 90
url: /zh/javascript-cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/
description: 学习如何在使用 Aspose.Cells for JavaScript 通过 C++ 将电子表格转换为 HTML 时，为 WordArt 渲染渐变填充。
---

## **可能的使用场景**  
在Aspose.Cells 17.1之前，转换为HTML格式时不支持WordArt的渐变填充。从Aspose.Cells 17.1版本开始，支持WordArt渐变填充。以下截图比较了使用Aspose.Cells 17.1和旧版本转换Excel文件时渐变填充的效果。  

![todo:image_alt_text](render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to-html_1.png)  

## **在将电子表格转换为HTML时渲染WordArt的渐变填充**  
以下示例代码将[源Excel文件](22774111.xlsx)转换成[输出HTML格式](22774109.zip)。源Excel文件中包含带有渐变填充的WordArt对象，如上截图所示。  

## **示例代码**  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Source Gradient Fill</title>
    </head>
    <body>
        <h1>Source Gradient Fill to HTML Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to HTML</button>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file (.xls, .xlsx, .csv).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save workbook to HTML format
            const outputData = workbook.save(SaveFormat.Html);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_sourceGradientFill.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Converted HTML File';

            resultDiv.innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```

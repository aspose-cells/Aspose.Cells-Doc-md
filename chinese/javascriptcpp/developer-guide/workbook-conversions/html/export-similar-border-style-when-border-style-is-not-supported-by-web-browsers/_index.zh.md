---
title: 使用JavaScript via C++导出不被网页浏览器支持的边框样式时，导出类似的边框样式。  
linktitle: 在Web浏览器不支持边框样式时导出类似的边框样式  
type: docs  
weight: 70  
url: /zh/javascript-cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/  
description: 学习如何在将Excel文件转换为HTML时导出网页浏览器不支持的边框，使用Aspose.Cells for JavaScript via C++。  
---  

## **可能的使用场景**  

Microsoft Excel支持一些虚线边框类型，但网页浏览器不支持。当你使用Aspose.Cells for JavaScript via C++将此类Excel文件转换为HTML时，这些边框会被移除。然而，Aspose.Cells也可以支持显示这种边框，通过[**HtmlSaveOptions.exportSimilarBorderStyle**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportSimilarBorderStyle--)属性设置。请将其值设为**true**，未支持的边框也会导出到HTML文件中。  

## **在Web浏览器不支持边框样式时导出相似的边框样式**  

 以下示例代码加载包含一些不支持的边框的[示例Excel文件](64716806.xlsx)，如截图所示。截图还展示了[**HtmlSaveOptions.exportSimilarBorderStyle**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportSimilarBorderStyle--)属性在[输出HTML](64716804.zip)中的效果。  

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)  

## **示例代码**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Export Similar Border Style Example</title>
    </head>
    <body>
        <h1>Export Similar Border Style Example</h1>
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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify Html Save Options - Export Similar Border Style
            const opts = new HtmlSaveOptions();
            opts.exportSimilarBorderStyle = true;

            // Save the workbook in Html format with specified Html Save Options
            const outputData = workbook.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputExportSimilarBorderStyle.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Export completed successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```

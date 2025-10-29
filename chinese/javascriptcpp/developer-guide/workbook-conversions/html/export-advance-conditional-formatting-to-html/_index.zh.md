---
title: 在使用JavaScript via C++将Excel转换为HTML时导出数据条、色阶和图标集条件格式。
linktitle: 在将Excel转换为HTML时，导出数据条、颜色刻度和图标集条件格式
type: docs
weight: 30
url: /zh/javascript-cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/
---

{{% alert color="primary" %}} 

您可以在将Excel文件转换为HTML时导出数据条、色阶和图标集条件格式。此功能由Microsoft Excel部分支持，但Aspose.Cells for JavaScript via C++完全支持。

{{% /alert %}}  

## **在将Excel转换为HTML时，导出数据条、颜色刻度和图标集条件格式**  
下面的截图展示了具有 DataBar、ColorScale 和 IconSet 有条件格式的[sample excel file](5115558.xlsx)。您可以从给定的链接下载[sample excel file](5115558.xlsx)。  

![todo:image_alt_text](conversion_1.png)  

下面的截图展示了 Aspose.Cells 输出的 HTML 文件，显示了 DataBar、ColorScale 和 IconSet 有条件格式。正如您所看到的，它看起来与[sample excel file](5115558.xlsx)完全一样。  

![todo:image_alt_text](conversion_2.png)  

### **示例代码**  
以下示例代码将示例Excel文件转换为HTML，属于常规[Excel转HTML转换](/cells/zh/javascript-cpp/convert-workbook-to-different-formats/#convertworkbooktodifferentformats-convertingexcelworkbooktohtml)。  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Converting Excel to HTML Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load your sample excel file in a workbook object
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save it in HTML format
            const outputData = workbook.save(SaveFormat.Html);

            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ConvertingToHTMLFiles_out.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```

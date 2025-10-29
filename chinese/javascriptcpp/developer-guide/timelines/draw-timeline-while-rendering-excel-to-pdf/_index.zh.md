---
title: 使用JavaScript通过C++在渲染Excel为PDF时绘制时间线
linktitle: 将Excel渲染为PDF时绘制时间轴
type: docs
weight: 60
url: /zh/javascript-cpp/draw-timeline-while-rendering-excel-to-pdf/
description: 使用Aspose.Cells for JavaScript通过C++管理Excel文件的时间线。
keywords: 在没有Office 2013、Office 2016、Office 2019和Office 365的情况下，使用JavaScript通过C++将时间线渲染为PDF
---

## **将Excel文件应用时间轴并导出为PDF。Aspose.Cells for Java现在默认支持此功能。只需将带有时间轴的Excel文件导出为PDF，生成的PDF将显示应用的时间轴。**
如果您的Excel文件应用了时间线，并且您希望使用时间线设置将Excel导出为PDF，Aspose.Cells for JavaScript通过C++默认支持此功能。只需将带有时间线的Excel文件导出为PDF，生成的PDF将显示已应用的时间线。

以下示例代码加载包含现有时间轴的[样本Excel文件](input.xlsx)，然后将工作簿另存为[输出PDF文件](out.pdf)。以下屏幕截图比较了源Excel文件和生成的PDF文件。

<img src="out.png" width="60%">

## **示例代码**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Saving the workbook to PDF format (browser)
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

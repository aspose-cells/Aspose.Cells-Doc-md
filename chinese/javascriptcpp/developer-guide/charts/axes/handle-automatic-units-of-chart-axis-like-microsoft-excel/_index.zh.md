---
title: 用JavaScript通过C++处理图表轴的自动单位
linktitle: 处理图表轴的自动单位，类似Microsoft Excel
description: 学习如何在Aspose.Cells for JavaScript中通过C++处理图表轴上的自动单位。我们的指南将向您展示如何配置和自定义自动单位，包括科学记数法的显示和缩放调整。
keywords: Aspose.Cells for JavaScript via C++，图表轴，自动单位，Microsoft Excel，配置，自定义，科学记数法，缩放。
type: docs
weight: 120
url: /zh/javascript-cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/
---

## **可能的使用场景**  
早期版本的Aspose.Cells for JavaScript via C++在将图表渲染为图像或PDF时未能正确处理图表轴的自动单位。现在，Aspose.Cells for JavaScript通过C++支持自动单位的处理。无需代码更改，只需将您的图表转换为图像或PDF即可，它会像Microsoft Excel一样渲染轴线。  

## **处理Microsoft Excel的图表轴的自动单位**  
以下示例代码加载了[示例Excel文件](61767755.xlsx)，并生成了[输出PDF图表](61767752.pdf)。截图显示了红色矩形中的图表轴自动单位，并且还将示例Excel文件中的图表与输出的PDF图表进行了比较，两者完全相同。  

![todo:image_alt_text](handle-automatic-units-of-chart-axis-like-microsoft-excel_1.png)  

## **示例代码**  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Handle Automatic Units Of Chart Axis Like Microsoft Excel</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

        const readyPromise = AsposeCells.onReady({
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

            await readyPromise;

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first chart
            const chart = worksheet.charts.get(0);

            // Render chart to pdf
            const outputData = await chart.toPdf();

            // Create download link for the generated PDF
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputHandleAutomaticUnitsOfChartAxisLikeMicrosoftExcel.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart rendered to PDF successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

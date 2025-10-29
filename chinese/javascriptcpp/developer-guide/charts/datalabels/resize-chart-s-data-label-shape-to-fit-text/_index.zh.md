---
title: 使用 JavaScript 通过 C++ 调整图表的数据标签形状以适应文本
linktitle: 调整图表数据标签形状以适应文本
description: 学习如何在 Aspose.Cells for JavaScript 通过 C++ 中调整图表中数据标签的大小以适应文本。我们的指南将展示如何调整标签容器的大小和形状，以确保文本正确显示，无截断或重叠。
keywords: Aspose.Cells for JavaScript 通过 C++，绘图，数据标签，形状调整，文本适应，截断，重叠。
type: docs
weight: 220
url: /zh/javascript-cpp/resize-chart-s-data-label-shape-to-fit-text/
---

{{% alert color="primary" %}}  
Excel应用程序提供了**调整形状以适应文本**选项，用于图表的数据标签，以增大形状的尺寸，以使文本适应其中。  
{{% /alert %}}  

## **如何在Microsoft Excel中调整图表数据标签的形状以适应文本**  

此选项可通过在 Excel 界面中选择图表上的任意数据标签，右键点击并选择 **格式数据标签** 菜单，然后在 **大小与属性** 标签下展开 **对齐方式**，以显示相关属性，包括 **调整形状以适应文本** 选项。  

## **如何使用 Aspose.Cells for JavaScript 通过 C++ 调整图表的数据标签形状以适应文本**  

为了模仿Excel的调整数据标签形状以适应文本的功能，Aspose.Cells API已暴露布尔类型的[**DataLabels.isResizeShapeToFitText()**](https://reference.aspose.com/cells/javascript-cpp/charttextframe/#isResizeShapeToFitText--)属性。以下代码展示了[**DataLabels.isResizeShapeToFitText()**](https://reference.aspose.com/cells/javascript-cpp/charttextframe/#isResizeShapeToFitText--)属性的简单使用场景。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Chart Data Labels Resize Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet that contains the Chart
            const sheet = workbook.worksheets.get(0);

            for (let c = 0; c < sheet.charts.count; c++) {
                // Access the Chart
                const chart = sheet.charts.get(c);

                for (let index = 0; index < chart.nSeries.count; index++) {
                    // Access the DataLabels of indexed NSeries
                    const labels = chart.nSeries.get(index).dataLabels;

                    // Set ResizeShapeToFitText property to true
                    labels.isResizeShapeToFitText = true;
                }

                // Calculate Chart
                chart.calculate();
            }

            // Save the result
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

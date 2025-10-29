---
title: 使用 JavaScript 通过 C++ 设置图表中数据标签的形状类型
linktitle: 设置图表数据标签的形状类型
description: 学习如何使用 Aspose.Cells for JavaScript 通过 C++ 设置图表中数据标签的形状类型。本指南将介绍不同的形状类型，并指导你如何选择合适的形状以增强显示效果和可用性。
keywords: Aspose.Cells for JavaScript 通过 C++，绘图，数据标签，形状类型，表现，实用性。
type: docs
weight: 110
url: /zh/javascript-cpp/set-the-shape-type-of-data-labels-of-chart/
---

## **可能的使用场景**
您可以使用 `DataLabels.shapeType` 属性更改图表中的数据标签的形状类型。它采用 `DataLabelShapeType` 枚举值，并相应地更改数据标签的形状类型。部分值包括

{{< highlight javascript >}}
 DataLabelShapeType.BentLineCallout
DataLabelShapeType.DownArrowCallout
DataLabelShapeType.Ellipse
DataLabelShapeType.LineCallout
DataLabelShapeType.Rect
etc.
{{< /highlight >}}

## **设置图表数据标签的形状类型**
以下示例代码将图表数据标签的形状类型更改为`DataLabelShapeType.WedgeEllipseCallout`。请参阅此代码使用的[示例Excel文件](60489778.xlsx)和由其生成的[输出Excel文件](60489779.xlsx)。截屏展示了代码在示例Excel文件上的效果。

![todo:image_alt_text](set-the-shape-type-of-data-labels-of-chart_1.png)
## **示例代码**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Shape Type of Data Labels of Chart Example</title>
    </head>
    <body>
        <h1>Set Shape Type of Data Labels of Chart Example</h1>
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
            const resultDiv = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Accessing the first chart
            const chart = worksheet.charts.get(0);

            // Accessing the first series
            const series = chart.nSeries.get(0);

            // Set the shape type of data labels i.e. Speech Bubble Oval
            series.dataLabels.shapeType = AsposeCells.DataLabelShapeType.WedgeEllipseCallout;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSetShapeTypeOfDataLabelsOfChart.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Shape type set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

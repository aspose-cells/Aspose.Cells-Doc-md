---
title: 用JavaScript通过C++在图表中设置图片为背景填充
linktitle: 在图表中设置图片作为背景填充
description: 学习如何使用Aspose.Cells for Java脚本通过C++将图片设置为图表背景填充。我们的指南将向您展示如何导入和定位图片，调整其大小和颜色，以及应用格式选项以增强图表的外观。
keywords: Aspose.Cells for Java脚本通过C++，图表，背景填充，图片，导入，定位，大小，颜色，格式化。
type: docs
weight: 30
url: /zh/javascript-cpp/set-picture-as-background-fill-in-the-chart/
---

{{% alert color="primary" %}}

Aspose.Cells允许您为不同对象如图表区域、图表区或图例框添加渐变、纹理、图案或图片作为填充效果。本文展示了如何向图表背景添加图像。

{{% /alert %}}

要实现这一点，Aspose.Cells提供了[**Chart.plotArea**](https://reference.aspose.com/cells/javascript-cpp/chart/#plotArea--)属性。以下代码示例演示了如何使用[**Chart.plotArea**](https://reference.aspose.com/cells/javascript-cpp/chart/#plotArea--)属性在图表中将图片设置为背景填充。

## 使用JavaScript在图表中设置图片为背景填充的代码

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Aspose.Cells Column Chart Example</h1>
        <p>
            Select an Excel file (sample.xlsx) and an optional image (aspose.png) for chart fill:
        </p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <input type="file" id="imageInput" accept="image/*" />
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
            const imageInput = document.getElementById('imageInput');
            const resultDiv = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            // Read Excel file
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet and set its name to "Data"
            let sheet = workbook.worksheets.get(0);
            sheet.name = "Data";

            // Get the cells collection in the sheet.
            const cells = workbook.worksheets.get(0).cells;

            // Put some values into cells of the Data sheet.
            let cell;
            cell = cells.get("A1"); cell.value = "Region";
            cell = cells.get("A2"); cell.value = "France";
            cell = cells.get("A3"); cell.value = "Germany";
            cell = cells.get("A4"); cell.value = "England";
            cell = cells.get("A5"); cell.value = "Sweden";
            cell = cells.get("A6"); cell.value = "Italy";
            cell = cells.get("A7"); cell.value = "Spain";
            cell = cells.get("A8"); cell.value = "Portugal";
            cell = cells.get("B1"); cell.value = "Sale";
            cell = cells.get("B2"); cell.value = 70000;
            cell = cells.get("B3"); cell.value = 55000;
            cell = cells.get("B4"); cell.value = 30000;
            cell = cells.get("B5"); cell.value = 40000;
            cell = cells.get("B6"); cell.value = 35000;
            cell = cells.get("B7"); cell.value = 32000;
            cell = cells.get("B8"); cell.value = 10000;

            // Add a chart sheet.
            let sheetIndex = workbook.worksheets.add(AsposeCells.SheetType.Chart);
            sheet = workbook.worksheets.get(sheetIndex);

            // Set the name of worksheet
            sheet.name = "Chart";

            // Create chart
            let chartIndex = sheet.charts.add(AsposeCells.ChartType.Column, 1, 1, 25, 10);
            const chart = sheet.charts.get(chartIndex);

            // Set some properties of chart plot area.
            // If an image was provided, set it as fill format and make the border invisible.
            if (imageInput.files.length) {
                const imgFile = imageInput.files[0];
                const imgBuffer = await imgFile.arrayBuffer();
                const imgBytes = new Uint8Array(imgBuffer);
                chart.plotArea.area.fillFormat.imageData = imgBytes;
            }
            chart.plotArea.border.isVisible = false;

            // Set properties of chart title
            chart.title.text = "Sales By Region";
            chart.title.font.color = AsposeCells.Color.Blue;
            chart.title.font.isBold = true;
            chart.title.font.size = 12;

            // Set properties of nseries
            chart.nSeries.add("Data!B2:B8", true);
            chart.nSeries.categoryData = "Data!A2:A8";
            chart.nSeries.isColorVaried = true;

            // Set the Legend.
            const legend = chart.legend;
            legend.position = AsposeCells.LegendPositionType.Top;

            // Save the excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'column_chart_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

---
title: 通过JavaScript和C++管理Excel图表的数据标签
description: 学习如何有效管理Excel图表中的数据标签，使用Aspose.Cells for Java脚本通过C++。本指南涵盖添加、删除和修改标签等多种管理任务，以提升图表的可读性和实用性。
keywords: Aspose.Cells for Java脚本、Excel图表、数据标签、管理、可读性、实用性、添加、删除、修改。
linktitle: 数据标签
type: docs
weight: 50
url: /zh/javascript-cpp/insert-datalabels-to-chart/
---

{{% alert color="primary" %}}  

数据标签是图表的重要组成部分。  
我们可以轻松地了解每个系列的值、百分比等。  

{{% /alert %}}  

## **数据标签选项**  
Aspose.Cells for Java脚本通过C++还允许在运行时管理图表的数据标签，借助[DataLabels](https://reference.aspose.com/cells/javascript-cpp/datalabels/)对象，轻松移动、更新和格式化图表的数据标签。  

|![todo:image_alt_text](chart_datalabels.png)|  

## **管理图表的数据标签**  
使用Aspose.Cells的[DataLabels](https://reference.aspose.com/cells/javascript-cpp/datalabels/)轻松管理图表的数据标签。  

以下代码片段演示了如何管理DataLabels：  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Chart Data Labels Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        let asposeReady = false;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            asposeReady = true;
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const resultDiv = document.getElementById('result');
            if (!asposeReady) {
                resultDiv.innerHTML = '<p style="color: red;">Aspose.Cells is not initialized yet. Please wait and try again.</p>';
                return;
            }

            // Instantiate a new Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").putValue(50);
            worksheet.cells.get("A2").putValue(100);
            worksheet.cells.get("A3").putValue(150);
            worksheet.cells.get("B1").putValue(60);
            worksheet.cells.get("B2").putValue(32);
            worksheet.cells.get("B3").putValue(50);

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
            chart.nSeries.add("A1:B3", true);

            // Show value labels
            chart.nSeries.get(0).dataLabels.showValue = true;
            // Show series name labels
            chart.nSeries.get(1).dataLabels.showSeriesName = true;
            // Move labels to center
            chart.nSeries.get(1).dataLabels.position = AsposeCells.LabelPositionType.Center;

            // Save the file and prepare download
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'chart_datalabels.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  

## **高级主题**  
- [向图表系列的数据点添加自定义标签](/cells/zh/javascript-cpp/adding-custom-labels-to-data-points-in-the-series-of-the-chart/)  
- [禁用图表的数据标签文本换行](/cells/zh/javascript-cpp/disable-text-wrapping-for-data-labels-of-the-chart/)  
- [调整图表数据标签形状以适应文本](/cells/zh/javascript-cpp/resize-chart-s-data-label-shape-to-fit-text/)  
- [图表点的富文本自定义数据标签](/cells/zh/javascript-cpp/rich-text-custom-data-label-of-chart-point/)  
- [设置图表数据标签的形状类型](/cells/zh/javascript-cpp/set-the-shape-type-of-data-labels-of-chart/)  
- [将单元格范围显示为数据标签](/cells/zh/javascript-cpp/showing-cell-range-as-the-data-labels/)

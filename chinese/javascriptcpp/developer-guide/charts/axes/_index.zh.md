---
title: 用 C++ 通过 JavaScript 管理 Excel 图表的轴线
description: 学习如何在 Aspose.Cells for JavaScript 通过 C++ 中配置图表轴线。我们的指南将展示如何调整主轴和副轴，设置它们的范围，以及修改它们的属性，以增强你的图表。
keywords: Aspose.Cells for Java脚本通过C++，图表轴，配置，主轴，辅轴，范围，属性。
linktitle: 轴
type: docs
weight: 50
url: /zh/javascript-cpp/chart-axes/
---

{{% alert color="primary" %}}  

在Excel图表中，有3种类型的轴：  
1. 横轴（类别轴）: X轴  
1. 垂直（值）轴：Y轴  
1. 深度（系列）轴：Z轴  

{{% /alert %}}  

## **轴选项**  
Aspose.Cells for Java脚本通过C++还允许你在运行时管理图表的轴。使用[轴](https://reference.aspose.com/cells/javascript-cpp/axis/)对象，你可以像在Excel中一样更改轴的所有选项。  

|![todo:image_alt_text](chart_axes.png)|  

## **管理X和Y轴**  
在Excel图表中，横轴和纵轴是最常用的两种轴。  

 以下代码片段演示了如何设置X轴和Y轴的选项。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Chart Axes</title>
    </head>
    <body>
        <h1>Chart Axes Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType } = AsposeCells;

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

            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").value = "Series1";
            worksheet.cells.get("A2").value = 50;
            worksheet.cells.get("A3").value = 100;
            worksheet.cells.get("A4").value = 150;
            worksheet.cells.get("B1").value = "Series2";
            worksheet.cells.get("B2").value = 60;
            worksheet.cells.get("B3").value = 32;
            worksheet.cells.get("B4").value = 50;

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
            chart.chartDataRange = ["A1:B4", true];

            // Hiding X axis
            chart.categoryAxis.isVisible = false;

            // Setting max value of Y axis
            chart.valueAxis.maxValue = 200;
            // Setting major unit
            chart.valueAxis.majorUnit = 50;

            // Save the file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'chart_axes.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully. Click the download link to download the file.</p>';
        });
    </script>
</html>
```  

## **高级主题**  
- [更改刻度标签方向](/cells/zh/javascript-cpp/change-tick-label-direction/)  
- [确定图表中存在哪些轴](/cells/zh/javascript-cpp/determine-which-axis-exists-in-the-chart/)  
- [处理Microsoft Excel的图表轴的自动单位](/cells/zh/javascript-cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/)  
- [计算图表后读取轴标签](/cells/zh/javascript-cpp/read-axis-labels-after-calculating-the-chart/)  
- [如何在Excel图表中设置类别轴](/cells/zh/javascript-cpp/how-to-set-category-axis/)

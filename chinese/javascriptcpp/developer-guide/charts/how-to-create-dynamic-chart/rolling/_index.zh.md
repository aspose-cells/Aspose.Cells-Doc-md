---
title: 如何使用C++通过JavaScript创建动态滚动图表
linktitle: 如何创建动态滚动图表
description: 了解如何使用Aspose.Cells for JavaScript通过C++创建动态滚动图表。我们的指南将演示如何在图表中实现平滑数据过渡和滚动平均，确保连续更新的显示效果。
keywords: Aspose.Cells for JavaScript通过C++、动态滚动图表、数据过渡、平滑平均、连续显示、更新可视化。
type: docs
weight: 74
url: /zh/javascript-cpp/create-dynamic-rolling-chart/
---

## **可能的使用场景**
动态滚动图表是指显示数据点不断变化和更新的图形表示。这是一种图表类型，会不断更新自己，展示最近数据点的滚动窗口，同时丢弃旧的数据点，因为新的数据点出现。

动态滚动图表通常用于可视化实时或流数据中的趋势和模式。在临时方面和随时间的变化至关重要的场景中特别有用，如股票市场分析、天气监测或实时性能跟踪。

这些图表通常采用动画或自动滚动机制，以确保始终呈现最新的信息。滚动窗口的长度可以自定义，以显示特定的时间段，如最近一小时、一天或一周。

总之，动态滚动图表是不断更新的图形表示，显示最新数据点，丢弃旧数据点，使用户能够观察实时趋势和模式。

## **使用Aspose Cells创建动态滚动图表**
在接下来的段落中，我们将向您展示如何使用Aspose.Cells创建动态滚动图表。我们将向您展示示例的代码以及使用该代码创建的Excel文件。

## **示例代码**
以下示例代码将生成[动态滚动图表文件](DynamicRollingChart.xlsx)。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Dynamic Rolling Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType, Utils } = AsposeCells;

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
            // Create a new workbook and access the first worksheet.
            const workbook = new Workbook();
            const sheets = workbook.worksheets;
            const sheet = sheets.get(0);

            // Populate the data for the chart. Add values to cells and set series names.
            sheet.cells.get("A1").value = "Month";
            sheet.cells.get("A2").value = 1;
            sheet.cells.get("A3").value = 2;
            sheet.cells.get("A4").value = 3;
            sheet.cells.get("A5").value = 4;
            sheet.cells.get("A6").value = 5;
            sheet.cells.get("A7").value = 6;
            sheet.cells.get("A8").value = 7;

            sheet.cells.get("B1").value = "Sales";
            sheet.cells.get("B2").value = 50;
            sheet.cells.get("B3").value = 45;
            sheet.cells.get("B4").value = 55;
            sheet.cells.get("B5").value = 60;
            sheet.cells.get("B6").value = 55;
            sheet.cells.get("B7").value = 65;
            sheet.cells.get("B8").value = 70;

            // Set the dynamic range for the chart's data source.
            let index = sheets.names.add("Sheet1!ChtData");
            sheets.names.get(index).refersTo = "=OFFSET(Sheet1!$B$1,COUNT(Sheet1!$B:$B),0,-5,1)";

            // Set the dynamic range for the chart's data labels.
            index = sheets.names.add("Sheet1!ChtLabels");
            sheets.names.get(index).refersTo = "=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)";

            // Create a chart object and set its data source.
            const chartIndex = sheet.charts.add(ChartType.Line, 10, 3, 25, 10);
            const chart = sheet.charts.get(chartIndex);
            chart.nSeries.add("Sales", true);
            chart.nSeries.get(0).values = "Sheet1!ChtData";
            chart.nSeries.get(0).xValues = "Sheet1!ChtLabels";

            // Save the workbook as an Excel file.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'DynamicRollingChart.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **备注**
在生成的文件中，您可以继续在A列和B列中添加数据，同时图表动态计算最新的 5 组数据。这是通过示例代码中的“OFFSET”公式完成的：

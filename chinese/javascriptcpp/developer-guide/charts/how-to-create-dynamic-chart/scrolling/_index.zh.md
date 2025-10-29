---
title: 如何在C++中使用JavaScript创建动态滚动图表
linktitle: 如何创建动态滚动图表
description: 了解如何使用Aspose.Cells for JavaScript通过C++创建动态滚动图表。我们的逐步指南将演示如何实现平滑的数据过渡和自动滚动，保持图表连续更新。
keywords: Aspose.Cells for JavaScript通过C++、动态滚动图表、数据过渡、平滑滚动、连续显示、更新可视化。
type: docs
weight: 75
url: /zh/javascript-cpp/create-dynamic-scrolling-chart/
---

## **可能的使用场景**
动态滚动图表是一种用于显示随时间变化的数据的图形表示类型。它旨在实时显示数据，使用户能够追踪连续的更新和趋势。随着新增数据的加入，图表将持续更新并自动滚动，以显示最新的信息。

动态滚动图表通常在各个行业中被广泛使用，如金融、股市分析、天气跟踪和社交媒体分析。它们使用户能够可视化和分析数据模式，并基于实时信息做出明智的决策。

这些图表通常是交互式的，允许用户放大或缩小、滚动历史数据和调整时间间隔。它们通常支持多个数据系列，提供不同指标及其相关性的综合视图。

总的来说，动态滚动图表是用于监控和分析时间序列数据的有价值的工具，有助于实时决策和增强数据可视化能力。

## **使用Aspose.Cells创建动态滚动图表**
在接下来的段落中，我们将展示如何使用Aspose.Cells for JavaScript通过C++创建动态滚动图表。我们会提供示例代码和所生成的Excel文件。

## **示例代码**
以下示例代码将生成[动态滚动图表文件](DynamicScrollingChart.xlsx)。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Dynamic Scrolling Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils, ChartType } = AsposeCells;

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
            sheet.cells.get("A1").value = "Day";
            sheet.cells.get("B1").value = "Sales";
            // In this example, we will add 30 days of data
            const allDays = 30;
            const showDays = 10;
            let currentDay = 1;

            for (let i = 0; i < allDays; i++) {
                const cellA = `A${i + 2}`;
                const cellB = `B${i + 2}`;
                sheet.cells.get(cellA).value = i + 1;
                sheet.cells.get(cellB).value = 50 * (i % 2) + 20 * (i % 3) + 10 * Math.floor(i / 3);
            }

            // This is the Dynamic Scrolling Control Data
            sheet.cells.get("G19").value = "Start Day";
            sheet.cells.get("G20").value = currentDay;
            sheet.cells.get("H19").value = "Show Days";
            sheet.cells.get("H20").value = showDays;

            // Set the dynamic range for the chart's data source. 
            let index = sheets.names.add("Sheet1!ChtScrollData");
            sheets.names.get(index).refersTo = "=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)";

            // Set the dynamic range for the chart's data labels. 
            index = sheets.names.add("Sheet1!ChtScrollLabels");
            sheets.names.get(index).refersTo = "=OFFSET(Sheet1!$A$2,Sheet1!$G$20,0,Sheet1!$H$20,1)";

            // Add a ScrollBar for the Dynamic Scrolling Chart
            const bar = sheet.shapes.addScrollBar(2, 0, 3, 0, 200, 30);
            bar.min = 0;
            bar.max = allDays - showDays;
            bar.currentValue = currentDay;
            bar.linkedCell = "$G$20";

            // Create a chart object and set its data source.
            const chartIndex = sheet.charts.add(ChartType.Line, 2, 4, 15, 10);
            const chart = sheet.charts.get(chartIndex);
            chart.nSeries.add("Sales", true);
            chart.nSeries.get(0).values = "Sheet1!ChtScrollData";
            chart.nSeries.get(0).xValues = "Sheet1!ChtScrollLabels";

            // Save the workbook as an Excel file.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'DynamicScrollingChart.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **备注**
在生成的文件中，您可以操作滚动条，而图表会动态计算最新的10组数据。这是在示例代码中使用“OFFSET”公式完成的：

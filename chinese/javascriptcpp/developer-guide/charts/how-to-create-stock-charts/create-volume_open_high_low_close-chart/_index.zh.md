---
title: 通过 C++ 使用 JavaScript 创建 Volume Open High Low Close（VOHLC）股票图表
description: 学习如何使用 Aspose.Cells for JavaScript 通过 C++ 创建带有成交量、开盘价、最高价、最低价、收盘价的股票图表。我们的指南将演示如何将股票市场数据绘制到图表上以便更好地分析和可视化。
keywords: 使用 C++ 通过 Aspose.Cells for JavaScript ，创建 Volume Open High Low Close 股票图表、股票市场数据、分析、可视化。
type: docs
weight: 184
url: /zh/javascript-cpp/create-volume-open-high-low-close-stock-chart/
---

## **可能的使用场景**
我们要看的第四个股票图表是成交量开盘最高最低收盘图表。同样，数据顺序必须正确。若需重新整理数据，应在设置图表前完成。该图表包括在第一（类别）列后立即的一列成交量，图表上有一个主轴显示成交量，价格移动到副轴。

![todo:image_alt_text](data.png)
## **成交量-开盘-最高-最低-收盘（VHLC）股票图表**

![todo:image_alt_text](sample.png)
## **示例代码**
以下示例代码加载了【示例Excel文件】(Volume-Open-High-Low-Close.xlsx)，并生成了【输出Excel文件】(out.xlsx)。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Volume-Open-High-Low-Close Stock Chart Example</h1>
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

            // Create an instance of Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            // Access the first worksheet.
            const worksheet = workbook.worksheets.get(0);
            // Create High-Low-Close-Stock Chart
            const pieIdx = worksheet.charts.add(AsposeCells.ChartType.StockVolumeOpenHighLowClose, 5, 6, 20, 12);
            // Retrieve the Chart object
            const chart = worksheet.charts.get(pieIdx);
            // Set the legend can be showed
            chart.showLegend = true;
            // Set the chart title name 
            chart.title.text = "Volume-Open-High-Low-Close Stock";
            // Set the Legend at the bottom of the chart area
            chart.legend.position = AsposeCells.LegendPositionType.Bottom;
            // Set data range (preserve both arguments as an array)
            chart.chartDataRange = ["A1:F9", true];
            // Set category data 
            chart.nSeries.categoryData = "A2:A9";
            // Set Color for the first series (Volume) data 
            chart.nSeries.get(0).area.foregroundColor = new AsposeCells.Color(79, 129, 189);
            // Fill the PlotArea area with nothing 
            chart.plotArea.area.fillFormat.fillType = AsposeCells.FillType.None;
            // Save the Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

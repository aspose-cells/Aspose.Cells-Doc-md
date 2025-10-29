---
title: 用JavaScript通过C++设置主轴和副轴
description: 学习如何理解和使用Aspose.Cells for JavaScript通过C++中的主轴和副轴。我们的指南将帮助您理解主轴与副轴的区别，以及如何有效配置和使用它们。
keywords: Aspose.Cells for JavaScript via C++，主轴，副轴，理解，区别，配置，使用
type: docs
weight: 190
url: /zh/javascript-cpp/primary-and-second-axis/
---

## **可能的使用场景**
当图表中的数据系列之间的数值差异很大，或者当您有多种类型的数据（价格和成交量）时，请在次垂直（值）轴上绘制一个或多个数据系列。次垂直轴的刻度显示了相关数据系列的值。在显示柱形图和折线图的组合图中，次要轴效果很好。

## **处理主轴和第二轴，就像处理Microsoft Excel一样**
请参阅以下示例代码，此代码创建一个新的Excel文件并将图表的值放在第一个工作表中。 
然后我们添加一个图表并显示第二轴。

![todo:image_alt_text](excel.png)

## **示例代码**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Primary and Secondary Axis Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType, LegendPositionType, FillType, Utils } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Put the sample values used in a chart
            worksheet.cells.get("A1").value = "Region";
            worksheet.cells.get("A2").value = "Peking";
            worksheet.cells.get("A3").value = "New York";
            worksheet.cells.get("A4").value = "Paris";
            worksheet.cells.get("B1").value = "Sales Volume";
            worksheet.cells.get("C1").value = "Growth Rate";
            worksheet.cells.get("B2").value = 100;
            worksheet.cells.get("B3").value = 80;
            worksheet.cells.get("B4").value = 140;
            worksheet.cells.get("C2").value = 0.7;
            worksheet.cells.get("C3").value = 0.8;
            worksheet.cells.get("C4").value = 1.0;

            // Create a Scatter chart
            const pieIdx = worksheet.charts.add(ChartType.Scatter, 6, 6, 15, 11);
            // Retrieve the Chart object
            const chart = worksheet.charts.get(pieIdx);
            // Add Series
            chart.nSeries.add("B2:C4", true);
            // Set the category data
            chart.nSeries.categoryData = "=Sheet1!$A$2:$A$4";
            // Set the Second-Axis
            chart.nSeries.get(1).plotOnSecondAxis = true;
            // Show the Second-Axis
            chart.secondValueAxis.isVisible = true;
            // Set the second series ChartType to line
            chart.nSeries.get(1).type = ChartType.Line;
            // Set the series name
            chart.nSeries.get(0).name = "Sales Volume";
            chart.nSeries.get(1).name = "Growth Rate";
            // Set the Legend at the bottom of the chart area
            chart.legend.position = LegendPositionType.Bottom;
            // Fill the PlotArea area with nothing
            chart.plotArea.area.fillFormat.fillType = FillType.None;
            // Save the file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'PrimaryandSecondaryAxis.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

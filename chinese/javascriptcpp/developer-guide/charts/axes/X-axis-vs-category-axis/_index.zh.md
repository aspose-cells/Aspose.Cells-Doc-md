---
title: JavaScript与C++中的X轴与类别轴对比
linktitle: X轴与分类轴的区别
description: 学习如何区分Aspose.Cells for Java脚本通过C++中的X轴和类别轴。我们的指南将帮助您理解它们的使用和属性差异，以及如何根据需求进行配置。
keywords: Aspose.Cells for Java脚本通过C++实现的脚本，X轴，类别轴，区别，使用，属性，配置。
type: docs
weight: 180
url: /zh/javascript-cpp/X-axis-vs-category-axis/
---

## **可能的使用场景**
X轴有不同类型。而Y轴是一个值类型轴，X轴可以是分类类型轴或值类型轴。使用值轴，数据被视为连续变化的数值数据，并且标记位于沿轴的变动点，其位置根据其数值而变化。使用分类轴，数据被视为一系列非数值文本标签，并且标记位于沿轴的一个位置，其位置根据其在序列中的位置而变化。下面的示例说明了值轴和分类轴之间的区别。
我们的示例数据如下图中的[示例表文件](sample.png)所示。第一列包含我们的X轴数据，可以视为分类或值。请注意，数字不是等间距的，也不按照数字顺序出现。

![todo:image_alt_text](sample.png)
## **处理X轴和分类轴，就像处理Microsoft Excel一样**
我们将在两种类型的图表上显示这些数据，第一种是XY（散点）图，X作为值轴，第二种是折线图，X作为类别轴。

![todo:image_alt_text](compare.png)
## **示例代码**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Charts and X Axis</h1>
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

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            // Access the first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Put the sample values used in charts
            worksheet.cells.get("A2").putValue(1);
            worksheet.cells.get("A3").putValue(3);
            worksheet.cells.get("A4").putValue(2.5);
            worksheet.cells.get("A5").putValue(3.5);
            worksheet.cells.get("B1").putValue("Cats");
            worksheet.cells.get("C1").putValue("Dogs");
            worksheet.cells.get("D1").putValue("Fishes");
            worksheet.cells.get("B2").putValue(7);
            worksheet.cells.get("B3").putValue(6);
            worksheet.cells.get("B4").putValue(5);
            worksheet.cells.get("B5").putValue(4);
            worksheet.cells.get("C2").putValue(7);
            worksheet.cells.get("C3").putValue(5);
            worksheet.cells.get("C4").putValue(4);
            worksheet.cells.get("C5").putValue(3);
            worksheet.cells.get("D2").putValue(8);
            worksheet.cells.get("D3").putValue(7);
            worksheet.cells.get("D4").putValue(3);
            worksheet.cells.get("D5").putValue(2);

            // Create Line Chart: X as Category Axis
            let pieIdx = worksheet.charts.add(ChartType.LineWithDataMarkers, 6, 15, 20, 21);
            // Retrieve the Chart object
            let chart = worksheet.charts.get(pieIdx);
            // Add Series
            chart.nSeries.add("B2:D5", true);
            // Set the category data
            chart.nSeries.categoryData = "=Sheet1!$A$2:$A$5";
            // Set the first series name
            chart.nSeries.get(0).name = "Cats";
            // Set the second series name
            chart.nSeries.get(1).name = "Dogs";
            // Set the third series name
            chart.nSeries.get(2).name = "Fishes";
            // Set the Legend at the bottom of the chart area
            chart.legend.position = LegendPositionType.Bottom;
            // Fill the PlotArea area with nothing 
            chart.plotArea.area.fillFormat.fillType = FillType.None;

            // Create XY (Scatter) Chart: X as Value Axis
            pieIdx = worksheet.charts.add(ChartType.ScatterConnectedByLinesWithDataMarker, 6, 6, 20, 12);
            // Retrieve the Chart object
            chart = worksheet.charts.get(pieIdx);
            // Add Series
            chart.nSeries.add("B2:D5", true);
            // Set X values for series 
            chart.nSeries.get(0).xValues = "{1,3,2.5,3.5}";
            chart.nSeries.get(1).xValues = "{1,3,2.5,3.5}";
            chart.nSeries.get(2).xValues = "{1,3,2.5,3.5}";
            // Set the first series name
            chart.nSeries.get(0).name = "Cats";
            // Set the second series name
            chart.nSeries.get(1).name = "Dogs";
            // Set the third series name
            chart.nSeries.get(2).name = "Fishes";
            // Set the Legend at the bottom of the chart area
            chart.legend.position = LegendPositionType.Bottom;
            // Fill the PlotArea area with nothing 
            chart.plotArea.area.fillFormat.fillType = FillType.None;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'XAxis.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

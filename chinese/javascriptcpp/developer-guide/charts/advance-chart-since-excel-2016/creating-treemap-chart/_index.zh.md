---
title: 如何在 JavaScript 结合 C++ 中创建 TreeMap 图表
linktitle: 如何创建树状图表
description: 学习如何在 Aspose.Cells for JavaScript 通过 C++ 中创建树形图。我们的指南将帮助你了解树形图的各种属性和格式设置选项，包括颜色、标签和数据表示。
keywords: Aspose.Cells for JavaScript 通过 C++，树形图，创建、属性、格式设置、颜色、标签、数据表示、环形图、分层图表。
type: docs
weight: 161
url: /zh/javascript-cpp/creating-treemap-chart/
---

## **可能的使用场景**  
树状图表提供了数据的分级视图，可轻松找出模式，比如哪些项目是商店的畅销品。树的分支由矩形代表，每个子分支显示为较小的矩形。树状图表通过颜色和临近性显示类别，并且可以轻松显示大量数据，这在其他图表类型中可能会很困难。  

![todo:image_alt_text](sample.png)  
## **树状图表**  
运行下面的代码后，您将会看到如下所示的树状图表。  

![todo:image_alt_text](result.png)  
## **示例代码**  
以下示例代码加载 [样本 Excel 文件](treemap.xlsx) 并生成 [输出 Excel 文件](out.xlsx)。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Treemap Chart Example</title>
    </head>
    <body>
        <h1>Treemap Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType, FillType } = AsposeCells;

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

            // Instantiate Workbook with uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);
            // Add a Treemap chart at row 5, column 6 with height 20 and width 12
            const pieIdx = worksheet.charts.add(ChartType.Treemap, 5, 6, 20, 12);
            // Retrieve the Chart object
            const chart = worksheet.charts.get(pieIdx);
            // Set the legend to be shown
            chart.showLegend = true;
            // Set the chart title text
            chart.title.text = "TreeMap Chart";
            // Add series data range (D2:F13)
            chart.nSeries.add("D2:F13", true);
            // Set category data (A2:C13)
            chart.nSeries.setCategoryData("A2:C13");
            // Show the DataLabels with category names for first series
            chart.nSeries.get(0).dataLabels.showCategoryName = true;
            // Fill the PlotArea area with nothing
            chart.plotArea.area.fillFormat.fillType = FillType.None;

            // Save the modified Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Treemap chart created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

---
title: 如何使用 JavaScript 结合 C++ 创建 Sunburst 图表
linktitle: 如何创建旭日图表
description: 学习如何在 Aspose.Cells for JavaScript 通过 C++ 中创建环形图，该图以圆形方式展示数据。我们的指南将帮助你设置图表的各种属性和格式，包括数据标签、图例、颜色等。
keywords: 在 Aspose.Cells for JavaScript 通过 C++ 中创建环形图，创建、设置属性、数据标签、图例、格式、颜色、圆形、数据渲染。
type: docs
weight: 162
url: /zh/javascript-cpp/creating-sunburst-chart/
---

## **可能的使用场景**
树状图非常适合比较层级内的比例；然而，树状图不擅长显示最大类别与每个数据点之间的层级关系。太阳放射图是更好的视觉图表，用于显示这些关系。太阳放射图理想于显示层级数据。每一层由一个环或圆圈表示，最内层代表层级顶部。没有层级数据（只有一层类别）的太阳放射图类似于甜甜圈图，但具有多个层级的太阳放射图展示了外环与内环的关系。太阳放射图最有效的用途是展示一环如何分解为其贡献部分，而另一种层级图表，树状图，则适合比较相对大小。

![todo:image_alt_text](sample.png)
## **旭日图表**
运行下面的代码后，您将会看到如下所示的旭日图表。

![todo:image_alt_text](result.png)
## **示例代码**
以下示例代码加载 [样本 Excel 文件](sunburst.xlsx) 并生成 [输出 Excel 文件](out.xlsx)。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Sunburst Chart Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Sunburst Chart Example</h1>
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

            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const worksheet = workbook.worksheets.get(0);

            const pieIdx = worksheet.charts.add(AsposeCells.ChartType.Sunburst, 5, 6, 25, 12);
            const chart = worksheet.charts.get(pieIdx);

            chart.showLegend = true;
            chart.title.text = "Sunburst Chart";
            chart.nSeries.add("D2:D16", true);
            chart.nSeries.categoryData = "A2:C16";
            chart.nSeries.get(0).dataLabels.showCategoryName = true;
            chart.plotArea.area.fillFormat.fillType = AsposeCells.FillType.None;

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Sunburst chart created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

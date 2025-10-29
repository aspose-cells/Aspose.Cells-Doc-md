---
title: 如何通过 C++ 使用 JavaScript 创建甘特图
linktitle: 如何创建甘特图
type: docs
weight: 72
url: /zh/javascript-cpp/how-to-create-gantt-chart/
description: 学习如何通过 C++ API 使用 Aspose.Cells for JavaScript 创建甘特图。
keywords: JavaScript 创建甘特图，添加甘特图，插入甘特图
---

## **什么是甘特图**

甘特图是一种条形图，显示项目时间表。它显示项目各个元素的开始和结束日期。每个任务或活动由一条条形表示，其长度对应持续时间。甘特图还显示任务之间的依赖关系，使项目管理者可以直观地看到任务的执行顺序。它在项目管理中广泛用于规划、排程和跟踪项目。

## **如何在Excel中创建甘特图**

你可以按照以下步骤在Excel中创建甘特图：
1. 添加一些用于甘特图的数据。 
<br>
<img src="00.png" width=50% />
1. 选择数据，依次点击插入 --> 图表 --> 插入柱状图或条形图 --> 堆积条形图。在示例中，是B1:B7，然后插入**堆积条**图表。
<br>
<img src="1.png" width=50% />

1. 选择图表，**选择数据** -> **添加**，设置 **系列名称** 和 **系列值** 如下。
<br>
<img src="2.png" width=50% />

1. 选择图表，编辑**横（类别）轴标签**。
<br>
<img src="3.png" width=50% />

1. **格式轴**，选择**类别逆序**以格式化Y轴。
1. 选择 **蓝色系列** 并设置 **填充 -> 无填充**。
1. **格式化轴** 设置 X 轴，设置 **最小值和最大值**（2019/1/5:43470，2019/1/30:43494）。
<br>
<img src="4.png" width=50% />

1. **为图表添加数据标签**，现在你将获得一个甘特图。
<br>
<img src="0.png" width=50% />


## **在Aspose.Cells中添加甘特图的方法。**
请查看以下示例代码。它加载包含一些示例数据的[示例Excel文件](sample.xlsx)，然后基于初始数据创建堆积柱状图，并设置相关属性。最后将工作簿保存为[输出XLSX](result.xlsx)。下方截图显示了由Aspose.Cells在输出Excel文件中创建的甘特图。
<br>
<img src="5.png" width=60% />

### **示例代码**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Chart Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Create BarStacked Chart
            const i = worksheet.charts.add(AsposeCells.ChartType.BarStacked, 5, 6, 20, 15);

            // Retrieve the Chart object
            const chart = worksheet.charts.get(i);

            // Set the chart title name 
            chart.title.text = "Gantt Chart";

            // Set the chart title is Visible
            chart.title.isVisible = true;

            // Set data range
            chart.chartDataRange = "B1:B6";

            // Add series data range
            chart.nSeries.add("C2:C6", true);

            // No fill for one serie
            chart.nSeries.get(0).area.fillFormat.fillType = AsposeCells.FillType.None;

            // Set the Horizontal(Category) Axis
            chart.nSeries.setCategoryData("A2:A6");

            // Reverse the Horizontal(Category) Axis
            chart.categoryAxis.isPlotOrderReversed = true;

            // Set the value axis's MinValue and MaxValue
            const minValue = parseFloat(worksheet.cells.get("B2").value);
            const maxValue = parseFloat(worksheet.cells.get("D6").value);
            chart.valueAxis.minValue = isNaN(minValue) ? 0 : minValue;
            chart.valueAxis.maxValue = isNaN(maxValue) ? 0 : maxValue;

            chart.plotArea.area.fillFormat.fillType = AsposeCells.FillType.None;

            // Show the DataLabels
            chart.nSeries.get(1).dataLabels.showValue = true;

            // Disable the Legend
            chart.showLegend = false;

            // Save the result
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'result.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

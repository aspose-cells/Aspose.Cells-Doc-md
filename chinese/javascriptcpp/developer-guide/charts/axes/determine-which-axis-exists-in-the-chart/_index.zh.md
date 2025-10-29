---
title: 用JavaScript通过C++确定图表中存在的轴线
linktitle: 确定图表中存在哪个轴
description: 学习如何在使用Aspose.Cells for JavaScript通过C++创建的图表中确定存在的轴线。我们的指南将帮助你识别和访问图表中的不同轴线，包括类别轴、数值轴和次轴。
keywords: Aspose.Cells for JavaScript via C++，图表，轴线，存在性，类别，数值，次轴。
type: docs
weight: 140
url: /zh/javascript-cpp/determine-which-axis-exists-in-the-chart/
---

{{% alert color="primary" %}}  
 有时，用户需要知道某个特定轴是否存在于图表中。例如，他们想知道图表中是否存在次数值轴。有些图表，如饼图、爆炸饼图、饼果图、饼条图、3D饼图、3D爆炸饼图、圆环图、爆炸圆环等，没有轴。  

Aspose.Cells提供了[**Chart.hasAxis(axisType, isPrimary)**](https://reference.aspose.com/cells/javascript-cpp/chart/#hasAxis-AxisType-boolean-)方法来判断图表是否具有特定的轴。  
{{% /alert %}}  

以下示例代码演示了如何使用[**Chart.hasAxis(axisType, isPrimary)**](https://reference.aspose.com/cells/javascript-cpp/chart/#hasAxis-AxisType-boolean-)判断样本图表是否具有主类别和数值轴以及次类别和数值轴。  

## 用JavaScript确定图表中存在的轴线的代码

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Check Chart Axes Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Check if there are any charts before accessing
            const charts = worksheet.charts;
            if (charts.count === 0) {
                resultDiv.innerHTML = '<p>No charts found in the worksheet.</p>';
                return;
            }

            // Access the chart
            const chart = charts.get(0);

            // Determine which axis exists in chart
            let outputs = [];
            let ret = chart.hasAxis(AsposeCells.AxisType.Category, true);
            outputs.push("Has Primary Category Axis: " + ret);

            ret = chart.hasAxis(AsposeCells.AxisType.Category, false);
            outputs.push("Has Secondary Category Axis: " + ret);

            ret = chart.hasAxis(AsposeCells.AxisType.Value, true);
            outputs.push("Has Primary Value Axis: " + ret);

            ret = chart.hasAxis(AsposeCells.AxisType.Value, false);
            outputs.push("Has Secondary Value Axis: " + ret);

            resultDiv.innerHTML = '<p>' + outputs.join('</p><p>') + '</p>';
        });
    </script>
</html>
```

## 示例代码生成的控制台输出

代码的控制台输出如下，显示主类别轴和数值轴为true，次类别轴和数值轴为false。  

{{< highlight java >}}  
Has Primary Category Axis: True  
Has Secondary Category Axis: False  
Has Primary Value Axis: True  
Has Secondary Value Axis: False  
{{< /highlight >}}

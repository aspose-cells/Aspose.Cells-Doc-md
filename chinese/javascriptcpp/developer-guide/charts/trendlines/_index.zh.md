---
title: 通过 C++ 使用 JavaScript 获取图表趋势线的方程文本
description: 学习如何使用 C++ 通过脚本获取在 Microsoft Excel 中创建的图表中趋势线的方程文本。我们的指南将演示如何访问和提取趋势线的方程以供进一步分析或显示。
keywords: 通过 C++ 采用脚本实现图表趋势线、方程文本、Microsoft Excel、数据分析、显示。
linktitle: 趋势线
type: docs
weight: 110
url: /zh/javascript-cpp/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

您可以使用 C++ 通过脚本获取图表趋势线的方程文本。Aspose.Cells 提供了 [**DataLabels.text**](https://reference.aspose.com/cells/javascript-cpp/datalabels/#text--) 属性，用于返回图表趋势线的方程文本。要使用此属性，首先需要调用 [**Chart.calculate()**](https://reference.aspose.com/cells/javascript-cpp/chart/#calculate--) 方法。

{{% /alert %}}

以下截图显示带有趋势线的图表及其方程文本（红色显示）。我们将在下面的示例代码中使用 [**DataLabels.text**](https://reference.aspose.com/cells/javascript-cpp/datalabels/#text--) 属性检索这段文本。

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

## 用于获取图表趋势线方程文本的 JavaScript 代码

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Read Trendline Equation Example</h1>
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the first chart inside the worksheet
            const chart = worksheet.charts.get(0);

            // Calculate the Chart to get the Equation Text of Trendline
            chart.calculate();

            // Access the Trendline
            const trendLine = chart.nSeries.get(0).trendLines.get(0);

            // Read the Equation Text of Trendline
            const equationText = trendLine.dataLabels.text;

            document.getElementById('result').innerHTML = `<p>Equation Text: ${equationText}</p>`;
        });
    </script>
</html>
```

## 示例代码生成的输出

这是上述示例代码的控制台输出。

{{< highlight javascript >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}

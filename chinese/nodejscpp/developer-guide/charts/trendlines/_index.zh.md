---
title: 获取趋势线方程文本的Node.js示例代码
description: 学习如何使用Aspose.Cells for Node.js via C++获取Microsoft Excel中创建的图表趋势线的方程文本。我们的指南演示如何访问和提取趋势线的方程以供进一步分析或显示。
keywords: Aspose.Cells for Node.js via C++，图表趋势线，方程文本，Microsoft Excel，数据分析，显示。
linktitle: 趋势线
type: docs
weight: 110
url: /zh/nodejs-cpp/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

你可以使用Aspose.Cells for Node.js via C++检索图表趋势线的方程文本。Aspose.Cells提供了[**DataLabels.getText()**](https://reference.aspose.com/cells/nodejs-cpp/datalabels/#getText--)属性，用于返回趋势线的方程文本，要使用这个属性，首先需要调用[**Chart.calculate()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#calculate--)方法。

{{% /alert %}}

以下截图显示带有趋势线的图表及其方程文本（红色显示）。我们将在下面的示例代码中使用 [**DataLabels.getText()**](https://reference.aspose.com/cells/nodejs-cpp/datalabels/#getText--) 属性检索这段文本。

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

## 使用Node.js获取图表趋势线的方程文本的代码示例

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create workbook object from source Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "source.xlsx"));

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the first chart inside the worksheet
const chart = worksheet.getCharts().get(0);

// Calculate the Chart first to get the Equation Text of Trendline
chart.calculate();

// Access the Trendline
const trendLine = chart.getNSeries().get(0).getTrendLines().get(0);

// Read the Equation Text of Trendline
console.log("Equation Text: " + trendLine.getDataLabels().getText());
```

## 示例代码生成的输出

这是上述示例代码的控制台输出。

{{< highlight javascript >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}

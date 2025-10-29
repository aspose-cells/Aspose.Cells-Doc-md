---  
title: 确定图表中存在的轴类型，使用Node.js通过C++  
linktitle: 确定图表中存在哪个轴  
description: 学习如何识别Aspose.Cells for Node.js via C++中创建的图表中存在的轴。我们的指南将帮助你识别和访问图表中的不同轴，包括类别轴、数值轴和次轴。  
keywords: Aspose.Cells for Node.js，图表，轴，存在性，类别，数值，次轴。  
type: docs  
weight: 140  
url: /zh/nodejs-cpp/determine-which-axis-exists-in-the-chart/  
---  

{{% alert color="primary" %}}  
 有时，用户需要知道某个特定轴是否存在于图表中。例如，他们想知道图表中是否存在次数值轴。有些图表，如饼图、爆炸饼图、饼果图、饼条图、3D饼图、3D爆炸饼图、圆环图、爆炸圆环等，没有轴。  

Aspose.Cells提供了[**Chart.hasAxis(axisType, isPrimary)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#hasAxis-AxisType-boolean-)方法来判断图表是否具有特定的轴。  
{{% /alert %}}  

以下示例代码演示了如何使用[**Chart.hasAxis(axisType, isPrimary)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#hasAxis-AxisType-boolean-)判断样本图表是否具有主类别和数值轴以及次类别和数值轴。  

## Node.js代码判断图表中是否存在轴  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "source.xlsx");
// Create workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Check if there are any charts before accessing
const charts = worksheet.getCharts();
if (charts.getCount() === 0) {
console.log("No charts found in the worksheet.");
return;
}

// Access the chart
const chart = charts.get(0);

// Determine which axis exists in chart
let ret = chart.hasAxis(AsposeCells.AxisType.Category, true);
console.log("Has Primary Category Axis: " + ret);

ret = chart.hasAxis(AsposeCells.AxisType.Category, false);
console.log("Has Secondary Category Axis: " + ret);

ret = chart.hasAxis(AsposeCells.AxisType.Value, true);
console.log("Has Primary Value Axis: " + ret);

ret = chart.hasAxis(AsposeCells.AxisType.Value, false);
console.log("Has Secondary Value Axis: " + ret);
```  

## 示例代码生成的控制台输出  

代码的控制台输出如下，显示主类别轴和数值轴为true，次类别轴和数值轴为false。  

{{< highlight java >}}  
Has Primary Category Axis: True  
Has Secondary Category Axis: False  
Has Primary Value Axis: True  
Has Secondary Value Axis: False  
{{< /highlight >}}  
{{< app/cells/assistant language="nodejs-cpp" >}}

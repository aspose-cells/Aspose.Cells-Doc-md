---
title: 使用Node.js通过C++更改刻度标签方向
linktitle: 更改刻度标签方向
description: 学习如何在Aspose.Cells for Node.js中更改刻度标签的方向。我们的指南将帮助你理解如何调整轴上刻度标签的方向，包括水平、垂直和角度方向。
keywords: Aspose.Cells for Node.js，刻度标签，方向，朝向，轴，水平，垂直，有角度。
type: docs
weight: 170
url: /zh/nodejs-cpp/change-tick-label-direction/
---

## **更改刻度标签方向**

Aspose.Cells 通过使用 [**TickLabels.getDirectionType()**](https://reference.aspose.com/cells/nodejs-cpp/ticklabels/#getDirectionType--) 属性提供更改图表刻度标签方向的能力。 [**TickLabels.getDirectionType()**](https://reference.aspose.com/cells/nodejs-cpp/ticklabels/#getDirectionType--) 属性接受 [**ChartTextDirectionType**](https://reference.aspose.com/cells/nodejs-cpp/charttextdirectiontype) 枚举值。 [**ChartTextDirectionType**](https://reference.aspose.com/cells/nodejs-cpp/charttextdirectiontype) 枚举包含以下成员：

- 水平
- 垂直
- 旋转90度
- 旋转270度
- 堆叠

以下图像比较了源文件和输出文件

### **源文件图像**

![todo:image_alt_text](change-tick-label-direction_1.jpg)

### **输出文件图像**

![todo:image_alt_text](change-tick-label-direction_2.jpg)

以下代码片段将刻度标签方向从Rotate90更改为水平方向

## **示例代码**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");
const filePath = path.join(sourceDir, "SampleChangeTickLabelDirection.xlsx");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const worksheet = workbook.getWorksheets().get(0);

// Load the chart from source worksheet
const chart = worksheet.getCharts().get(0);

chart.getCategoryAxis().getTickLabels().setDirectionType(AsposeCells.ChartTextDirectionType.Horizontal);

// Output the file
workbook.save(path.join(outputDir, "outputChangeChartDataLableDirection.xlsx"));
```

可以从以下链接下载源文件和输出文件。

[源文件](105480221.xlsx)

[输出文件](105480223.xlsx)
{{< app/cells/assistant language="nodejs-cpp" >}}

---
title: 使用 Node.js via C++ 为图表点添加富文本自定义数据标签
description: 学习如何在 Aspose.Cells for Node.js via C++ 中为图表点添加富文本自定义数据标签。我们的指南将向您展示如何用不同字体、颜色和对齐方式格式化标签，以增强图表的外观和可读性。
keywords: Aspose.Cells for Node.js via C++，制图，富文本，自定义数据标签，字体，颜色，对齐，外观，可读性。
type: docs
weight: 10
url: /zh/nodejs-cpp/rich-text-custom-data-label-of-chart-point/
---

{{% alert color="primary" %}}

您可以使用 Aspose.Cells 创建图表点的富文本自定义数据标签。Aspose.Cells 提供 [**ChartTextFrame.characters(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/charttextframe/#characters-number-number-) 方法返回 [**FontSetting**](https://reference.aspose.com/cells/nodejs-cpp/fontsetting) 对象，可用于设置文本的字体属性，如颜色、粗细等。

{{% /alert %}}

## 数据点的图表富文本自定义数据标签

以下代码访问第一个系列的第一个图表点，设置其文本，然后设置前十个字符的字体，将其颜色设为红色，粗体设为**true**。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create a workbook from source Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample_custom_datalabel.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the first chart inside the sheet
const chart = worksheet.getCharts().get(0);

// Access the data label of first series first point
const dlbls = chart.getNSeries().get(0).getPoints().get(0).getDataLabels();

// Set data label text
dlbls.setText("Rich Text Label");

// Set the font setting of the first 10 characters
const fntSetting = dlbls.characters(0, 10);
fntSetting.getFont().setColor(AsposeCells.Color.Red);
fntSetting.getFont().setIsBold(true);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```

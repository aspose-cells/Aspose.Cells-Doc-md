---
title: 使用Node.js通过C++在饼图中自定义切片或扇区颜色
linktitle: 在饼图中自定义切片或扇区的颜色
description: 学习如何使用Aspose.Cells for Node.js via C++自定义饼图中的切片和扇区颜色。我们的指南将展示如何为每个切片、扇区或扇团分配独特的颜色，以改善视觉效果和数据表现。
keywords: Aspose.Cells for Node.js via C++，饼图，自定义切片颜色，自定义扇区颜色，视觉吸引力，数据表现。
type: docs
weight: 60
url: /zh/nodejs-cpp/custom-slice-or-sector-colors-in-pie-chart/
---

{{% alert color="primary" %}}

本文解释了如何向饼图切片/扇区添加自定义颜色。默认情况下，饼图使用Microsoft Excel的默认模板。要使用其他颜色，需要重新定义图表中的颜色。

{{% /alert %}}

要为饼图的单独切片或扇区设置自定义颜色：

1. 访问[**Series**](https://reference.aspose.com/cells/nodejs-cpp/series)对象的[**ChartPoint**](https://reference.aspose.com/cells/nodejs-cpp/chartpoint)。
1. 使用[**ChartPoint.getForegroundColor()**](https://reference.aspose.com/cells/nodejs-cpp/area/#getForegroundColor--)属性分配你选择的颜色。

本文还解释了如何：

- 图表的类别数据。
- 与单元格相关联的图表标题。
- 图表标题字体设置。
- 图例的位置。

{{% alert color="primary" %}}

[**ChartPoint.getForegroundColor()**](https://reference.aspose.com/cells/nodejs-cpp/area/#getForegroundColor--) 不仅适用于饼图，还可用于所有类型的图表。

{{% /alert %}}

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Put the sample values used in a pie chart
worksheet.getCells().get("C3").putValue("India");
worksheet.getCells().get("C4").putValue("China");
worksheet.getCells().get("C5").putValue("United States");
worksheet.getCells().get("C6").putValue("Russia");
worksheet.getCells().get("C7").putValue("United Kingdom");
worksheet.getCells().get("C8").putValue("Others");

// Put the sample values used in a pie chart
worksheet.getCells().get("D2").putValue("% of world population");
worksheet.getCells().get("D3").putValue(25);
worksheet.getCells().get("D4").putValue(30);
worksheet.getCells().get("D5").putValue(10);
worksheet.getCells().get("D6").putValue(13);
worksheet.getCells().get("D7").putValue(9);
worksheet.getCells().get("D8").putValue(13);

// Create a pie chart with desired length and width
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.Pie, 1, 6, 15, 14);

// Access the pie chart
const pie = worksheet.getCharts().get(pieIdx);

// Set the pie chart series
pie.getNSeries().add("D3:D8", true);

// Set the category data
pie.getNSeries().setCategoryData("=Sheet1!$C$3:$C$8");

// Set the chart title that is linked to cell D2
pie.getTitle().setLinkedSource("D2");

// Set the legend position at the bottom.
pie.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);

// Set the chart title's font name and color
pie.getTitle().getFont().setName("Calibri");
pie.getTitle().getFont().setSize(18);

// Access the chart series
const srs = pie.getNSeries().get(0);

// Color the individual points with custom colors
srs.getPoints().get(0).getArea().setForegroundColor(new AsposeCells.Color(0, 246, 22, 219));
srs.getPoints().get(1).getArea().setForegroundColor(new AsposeCells.Color(0, 51, 34, 84));
srs.getPoints().get(2).getArea().setForegroundColor(new AsposeCells.Color(0, 46, 74, 44));
srs.getPoints().get(3).getArea().setForegroundColor(new AsposeCells.Color(0, 19, 99, 44));
srs.getPoints().get(4).getArea().setForegroundColor(new AsposeCells.Color(0, 208, 223, 7));
srs.getPoints().get(5).getArea().setForegroundColor(new AsposeCells.Color(0, 222, 69, 8));

// Autofit all columns
worksheet.autoFitColumns();

const outputPath = path.join(dataDir, "output.out.xlsx");
// Save the workbook
workbook.save(outputPath, AsposeCells.SaveFormat.Xlsx);
```

---
title: 如何通过 C++ 使用 Node.js 创建甘特图
linktitle: 如何创建甘特图
type: docs
weight: 72
url: /zh/nodejs-cpp/how-to-create-gantt-chart/
description: 学习如何使用 Aspose.Cells for Node.js via C++ API 创建甘特图。
keywords: Node.js 创建甘特图，添加甘特图，插入甘特图
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

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Create BarStacked Chart
const i = worksheet.getCharts().add(AsposeCells.ChartType.BarStacked, 5, 6, 20, 15);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(i);
// Set the chart title name 
chart.getTitle().setText("Gantt Chart");
// Set the chart title is Visible
chart.getTitle().setIsVisible(true);
// Set data range
chart.setChartDataRange("B1:B6", true);
// Add series data range
chart.getNSeries().add("C2:C6", true);
// No fill for one serie
chart.getNSeries().get(0).getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Set the Horizontal(Category) Axis
chart.getNSeries().setCategoryData("A2:A6");
// Reverse the Horizontal(Category) Axis
chart.getCategoryAxis().setIsPlotOrderReversed(true);
// Set the value axis's MinValue and MaxValue
const minValue = parseFloat(worksheet.getCells().get("B2").getValue());
const maxValue = parseFloat(worksheet.getCells().get("D6").getValue());
chart.getValueAxis().setMinValue(isNaN(minValue) ? 0 : minValue);
chart.getValueAxis().setMaxValue(isNaN(maxValue) ? 0 : maxValue);
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Show the DataLabels
chart.getNSeries().get(1).getDataLabels().setShowValue(true);
// Disable the Legend
chart.setShowLegend(false);
// Save the result
workbook.save("result.xlsx");
```

{{< app/cells/assistant language="nodejs-cpp" >}}

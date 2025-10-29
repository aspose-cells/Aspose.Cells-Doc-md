---  
title: 如何通过C++在Node.js中创建TreeMap图表  
linktitle: 如何创建树状图表  
description: 学习如何在Aspose.Cells for Node.js via C++中创建树状图。我们的指南将帮助你理解树状图的各种属性和格式选项，包括颜色、标签和数据表示。  
keywords: Aspose.Cells for Node.js，树状图，创建，属性，格式，颜色，标签，数据表示，环形图，层级图。  
type: docs  
weight: 161  
url: /zh/nodejs-cpp/creating-treemap-chart/  
---  

## **可能的使用场景**  
树状图表提供了数据的分级视图，可轻松找出模式，比如哪些项目是商店的畅销品。树的分支由矩形代表，每个子分支显示为较小的矩形。树状图表通过颜色和临近性显示类别，并且可以轻松显示大量数据，这在其他图表类型中可能会很困难。  

![todo:image_alt_text](sample.png)  
## **树状图表**  
运行下面的代码后，您将会看到如下所示的树状图表。  

![todo:image_alt_text](result.png)  
## **示例代码**  
以下示例代码加载 [样本 Excel 文件](treemap.xlsx) 并生成 [输出 Excel 文件](out.xlsx)。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "treemap.xlsx");
// Create an instance of Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Add a Treemap chart
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.Treemap, 5, 6, 20, 12);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Set the legend can be showed
chart.setShowLegend(true);
// Set the chart title name 
chart.getTitle().setText("TreeMap Chart");
// Add series data range(D2:D13,actually)
chart.getNSeries().add("D2:F13", true);
// Set category data(A2:A13 is incorrect )
chart.getNSeries().setCategoryData("A2:C13");
// Show the DataLabels with category names
chart.getNSeries().get(0).getDataLabels().setShowCategoryName(true);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the Excel file
workbook.save("out.xlsx");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}

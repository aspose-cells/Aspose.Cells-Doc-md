---  
title: 通过C++在Node.js中设置数据源  
description: 了解Aspose.Cells for Node.js via C++支持的各种数据源。我们的指南将引导您了解不同类型的数据源，演示如何连接和检索数据以填充工作表。  
keywords: Aspose.Cells for Node.js via C++，图表，数据格式化，标签，颜色，字体，外观，可用性。  
linktitle: 数据源  
type: docs  
weight: 10  
url: /zh/nodejs-cpp/data-formatting-in-charts/  
---  

在之前的主题中，我们已提供许多示例来演示如何为图表设置数据源，但在本主题中，我们将提供更多关于可以为图表设置的数据类型的详细信息。

## **设置图表数据**

使用Aspose.Cells处理图表时，有以下两种数据类型需要处理：

 - 图表数据。
 - 类别数据。

### **图表数据**

 图表数据是我们用作数据源来构建图表的数据。我们可以通过调用[**SeriesCollection**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection)对象的[**add(string, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection/#add-string-boolean-)方法添加包含图表数据的单元格范围。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(170);
worksheet.getCells().get("A4").putValue(300);
worksheet.getCells().get("B1").putValue(160);
worksheet.getCells().get("B2").putValue(32);
worksheet.getCells().get("B3").putValue(50);
worksheet.getCells().get("B4").putValue(40);

// Adding sample values to cells as category data
worksheet.getCells().get("C1").putValue("Q1");
worksheet.getCells().get("C2").putValue("Q2");
worksheet.getCells().get("C3").putValue("Y1");
worksheet.getCells().get("C4").putValue("Y2");

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
chart.getNSeries().add("A1:B4", true);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

### **分类数据**

 类别数据用于标签化图表数据，可以使用其[**getCategoryData()**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection/#getCategoryData--)属性添加到[**SeriesCollection**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection)。下面给出一个完整示例，演示如何使用图表和类别数据。执行上述示例代码后，工作表中将添加一个柱状图，如下所示。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(10);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(170);
worksheet.getCells().get("A4").putValue(200);
worksheet.getCells().get("B1").putValue(120);
worksheet.getCells().get("B2").putValue(320);
worksheet.getCells().get("B3").putValue(50);
worksheet.getCells().get("B4").putValue(40);

// Adding sample values to cells as category data
worksheet.getCells().get("C1").putValue("Q1");
worksheet.getCells().get("C2").putValue("Q2");
worksheet.getCells().get("C3").putValue("Y1");
worksheet.getCells().get("C4").putValue("Y2");

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
chart.getNSeries().add("A1:B4", true);

// Setting the data source for the category data of SeriesCollection
chart.getNSeries().setCategoryData("C1:C4");

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **高级主题**  
- [复制行或区域时更改图表的数据源到目标工作表](/cells/zh/nodejs-cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)  
- [创建动态图表](/cells/zh/nodejs-cpp/create-dynamic-charts/)  
- [使用 Chart.SetChartDataRange 方法设置图表的简单方法](/cells/zh/nodejs-cpp/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)  
- [查找图表系列中点的X和Y值类型](/cells/zh/nodejs-cpp/find-type-of-x-and-y-values-of-points-in-chart-series/)  

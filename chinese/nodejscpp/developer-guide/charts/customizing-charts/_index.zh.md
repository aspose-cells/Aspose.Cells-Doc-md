---  
title: 通过Node.js与C++自定义图表  
linktitle: 自定义图表  
description: 了解如何在Aspose.Cells for Node.js via C++中自定义图表。我们的指南将指导您如何修改图表布局、添加和格式化数据系列、调整轴线以及应用各种格式化选项，以改善图表的外观和实用性。  
keywords: Aspose.Cells for Node.js via C++，图表，自定义，布局，数据系列，轴线，格式化，外观，可用性。  
type: docs  
weight: 40  
url: /zh/nodejs-cpp/customizing-charts/  
---  


## **创建自定义图表**  

到目前为止，我们在讨论图表时，常常关注具有标准格式设置的标准图表。我们只定义数据源，设置一些属性，图表便会以默认格式创建。但Aspose.Cells API还支持创建自定义图表，允许开发者使用自定义格式设置来创建图表。  

开发人员可以使用Aspose.Cells在运行时创建自定义图表。  

图表由数据系列组成。Aspose.Cells中的每个数据系列由[**Series**](https://reference.aspose.com/cells/nodejs-cpp/series)对象表示，而[**SeriesCollection**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection)对象作为[**Series**](https://reference.aspose.com/cells/nodejs-cpp/series)对象的集合。当创建定制图表时，开发者可以自由地为不同的数据系列（收集在[**SeriesCollection**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection)对象中）使用不同类型的图表。  

下面的示例代码演示了如何创建自定义图表。在此示例中，我们将为第一个数据系列使用柱形图，为第二个系列使用折线图。结果是，我们在工作表中添加了一个柱形图，结合了一条折线图。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("A4").putValue(110);
worksheet.getCells().get("B1").putValue(260);
worksheet.getCells().get("B2").putValue(12);
worksheet.getCells().get("B3").putValue(50);
worksheet.getCells().get("B4").putValue(100);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding NSeries (chart data source) to the chart ranging from "A1" cell to "B4"
chart.getNSeries().add("A1:B4", true);

// Setting the chart type of 2nd NSeries to display as line chart
chart.getNSeries().get(1).setType(AsposeCells.ChartType.Line);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

{{% alert color="primary" %}}  

目前，Aspose.Cells仅支持结合饼图、折线图、柱状图和堆积柱状图的自定义图表，但未来版本将支持更多图表类型。  

{{% /alert %}}  

{{< app/cells/assistant language="nodejs-cpp" >}}

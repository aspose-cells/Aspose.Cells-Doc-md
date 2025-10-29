---  
title: 通过C++使用Node.js读取和操作Excel 2016图表  
linktitle: 读取和操作Excel 2016图表  
description: 学习如何使用Aspose.Cells for Node.js via C++读取和操作Excel 2016图表。本指南将展示如何访问和修改各种图表属性。  
keywords: Aspose.Cells for Node.js、Excel 2016图表、读取、操作、数据标签、系列颜色、布局、层级图表、圆形图表  
type: docs  
weight: 48  
url: /zh/nodejs-cpp/read-and-manipulate-excel-2016-charts/  
---  

## **可能的使用场景**  
Aspose.Cells 现在支持读取和操作 Microsoft Excel 2016 图表，而这些图表在 Microsoft Excel 2013 或早期版本中是不存在的。  
## **读取和操作Excel 2016图表**  
以下示例代码加载包含Excel 2016图表的[源Excel文件](22774101.xlsx)，该文件在第一个工作表中。它逐个读取所有图表并根据其图表类型更改标题。以下截图显示代码执行前的源Excel文件。如您所见，所有图表的标题都是相同的。

![todo:image_alt_text](read-and-manipulate-excel-2016-charts_1.png)

下面的屏幕截图显示了代码执行后的 [输出 Excel 文件](22774104.xlsx)。正如您所见，图表标题已根据其图表类型进行了更改。

![todo:image_alt_text](read-and-manipulate-excel-2016-charts_2.png)  
## **示例代码**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "excel2016Charts.xlsx");

// Load source excel file containing excel 2016 charts
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet which contains the charts
const sheet = workbook.getWorksheets().get(0);

// Access all charts one by one and read their types
for (let i = 0; i < sheet.getCharts().getCount(); i++) {
// Access the chart
const ch = sheet.getCharts().get(i);

// Print chart type
console.log(ch.getType());

// Change the title of the charts as per their types
ch.getTitle().setText("Chart Type is " + ch.getType().toString());
}

// Save the workbook
workbook.save(path.join(dataDir, "out_excel2016Charts.xlsx"));
```  
## **控制台输出**  
以下是使用所提供的 [源 Excel 文件](22774101.xlsx) 执行上述示例代码时的控制台输出。

{{< highlight javascript >}}  

 Waterfall  

Treemap  

Sunburst  

Histogram  

BoxWhisker  

{{< /highlight >}}  

## **高级主题**  
- [创建瀑布图](/cells/zh/nodejs-cpp/creating-waterfall-chart/)  
- [创建树状图表](/cells/zh/nodejs-cpp/creating-treemap-chart/)  
- [创建旭日图](/cells/zh/nodejs-cpp/creating-sunburst-chart/)  

{{< app/cells/assistant language="nodejs-cpp" >}}

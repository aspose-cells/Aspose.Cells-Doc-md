---  
title: 使用 Node.js via C++ 显示单元格范围作为数据标签  
linktitle: 将单元格范围显示为数据标签  
description: 学习如何在图表中显示单元格范围作为数据标签，支持 Aspose.Cells for Node.js via C++。我们的指南将演示如何将标签链接到数据源，并进行格式化，以在图表中提供准确且有意义的信息。  
keywords: Aspose.Cells for Node.js via C++，制图，数据标签，单元格范围，数据源，格式化，准确性，有意义的信息。  
type: docs  
weight: 130  
url: /zh/nodejs-cpp/showing-cell-range-as-the-data-labels/  
---  

{{% alert color="primary" %}}  
在 Microsoft Excel 2013 中，您可以显示单元格范围作为数据标签。 Aspose.Cells for Node.js 支持此功能。  
{{% /alert %}}  

## **复选框显示单元格范围作为数据标签**  

在Microsoft Excel中显示单元格范围作为数据标签：  

1. 选择系列数据标签，右键单击以打开上下文菜单。  
1. 选择**格式数据标签**。标签选项会显示。  
1. 选择或清除选项 **标签包含 - 来自单元格的值**。  

以下示例代码访问图表系列数据标签并将 [**DataLabels.getShowCellRange()**](https://reference.aspose.com/cells/nodejs-cpp/datalabels/#getShowCellRange--) 属性设置为 **true** ，以选择 **标签包含-来自单元格的值** 选项。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "source_show_range.xlsx");

// Create workbook from the source Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the chart inside the worksheet
const chart = worksheet.getCharts().get(0);

// Check the "Label Contains - Value From Cells"
const dataLabels = chart.getNSeries().get(0).getDataLabels();
dataLabels.setShowCellRange(true);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}

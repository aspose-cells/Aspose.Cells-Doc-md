---  
title: 通过 C++ 使用 Node.js 在计算完图表后读取轴标签  
linktitle: 在计算图表后读取轴标签  
description: 学习如何在计算完图表后读取 Aspose.Cells for Node.js via C++ 的轴标签。我们的指南将向您展示如何访问和检索轴标签，包括其格式和位置。  
keywords: Aspose.Cells for Node.js，制图，轴标签，计算，读取，访问，检索，格式，位置，Node.js via C++  
type: docs  
weight: 90  
url: /zh/nodejs-cpp/read-axis-labels-after-calculating-the-chart/  
---  

## **可能的使用场景**

您可以在使用 [**Chart.calculate()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#calculate--) 方法计算完值后读取图表的轴标签。请使用 [**Axis.getAxisTexts()**](https://reference.aspose.com/cells/nodejs-cpp/axis/#getAxisTexts--) 方法实现此目的，它将返回轴标签的列表。

## **计算图表后读取轴标签**

请参阅以下示例代码，加载[sample Excel file]（ReadAxisLabels.xlsx）并读取第一个工作表中图表的类别轴标签。然后在控制台上打印轴标签的值。请参阅下面的示例代码的控制台输出进行参考。

## **示例代码**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "ReadAxisLabels_new.xlsx");

// Load the Excel file containing chart
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the chart
const chart = worksheet.getCharts().get(0);

// Calculate the chart
chart.calculate();

// Read axis labels of category axis
const lstLabels = chart.getCategoryAxis().getAxisTexts();

// Print axis labels on console
console.log("Category Axis Labels: ");
console.log("---------------------");

// Iterate axis labels and print them one by one
for (let i = 0; i < lstLabels.length; i++) {
console.log(lstLabels[i]);
}
```

## **控制台输出**

{{< highlight javascript >}}  
 Category Axis Labels:  

\---------------------  

Iran  

China  

USA  

Brazil  

England  
{{< /highlight >}}  


---  
title: 如何用 Node.js 通过 C++ 设置点为总计  
linktitle: 设置点为总数的方法。  
description: 学习如何用 Aspose.Cells for Node.js via C++ 设置瀑布图中的点为总计。  
keywords: 瀑布图，点，设置为总计，Node.js 通过 C++  
type: docs  
weight: 72  
url: /zh/nodejs-cpp/how-to-set-point-as-total/  
---  

## Excel图表中的"设为总和"是什么意思

在某些 Excel 图表中，例如瀑布图，一些点数据是前面点的总和，你可能需要“设置点为总计”。我们将展示示例代码和下面的说明。

## 瀑布图需要 "设置点为总计" 

![todo:image_alt_text](set-as-total1.png)

这张图片显示了 Excel 中的瀑布图。可以看到有四个起始于“总计”的数据点，它们用来汇总所有前面的数据。在这张图片中，设置并不完全正确。当我们选择“总计 2024”这个点时，可以看到在 Excel 中“设置为总计”选项未勾选。下面附上需要修改的[示例 Excel 文件](SampleSheet.xlsx)，我们将使用 Aspose.Cells for Node.js via C++ 正确设置它。

## 使用 Aspose.Cells for Node.js via C++ 设置点为总计 

我们使用以下代码来正确设置文件：

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleSheet.xlsx");

const workbook = new AsposeCells.Workbook(filePath);
const worksheet = workbook.getWorksheets().get(0);
const chart = worksheet.getCharts().get("Graphiq5");

// set some points as total column 
// In this example, we set points 0, 4, 8, 12 as total
chart.getNSeries().get(0).getLayoutProperties().setSubtotals([0, 4, 8, 12]);
workbook.save(path.join(dataDir, "output.xlsx"));
```

你可以得到以下正确的[输出文件](output.xlsx)

如下图所示，四个"总和"数据点已正确设置，你可以看到与之前图表的区别。

![todo:image_alt_text](set-as-total2.png)  
{{< app/cells/assistant language="nodejs-cpp" >}}

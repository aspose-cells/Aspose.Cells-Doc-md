---  
title: 通过 C++ 使用 Node.js 将图表转换为 SVG 格式的图像  
linktitle: 将图表转换为SVG格式的图像  
type: docs  
weight: 240  
url: /zh/nodejs-cpp/converting-chart-to-image-in-svg-format/  
description: 学习如何使用 Aspose.Cells for Node.js via C++ 将图表转换为 SVG 格式的图像。  
---  

{{% alert color="primary" %}}  

可缩放矢量图形（SVG）是一种基于XML的二维图形格式，还支持交互和动画。SVG规范是由万维网联盟（W3C）自1999年以来制定的开放标准。  

SVG图像及其行为是在XML文本文件中定义的。这意味着它们可以被搜索、索引、编写脚本和压缩。作为XML文件，SVG图像可以使用任何文本编辑器创建和编辑，但更常见的是使用绘图软件创建。  

Aspose.Cells 可以将图表保存为 BMP、JPEG、PNG、GIF、SVG 等多种格式的图像。本文介绍了如何将图表保存为 SVG 格式。  

{{% /alert %}}  

以下示例代码解释了如何使用Aspose.Cells将图表转换为SVG格式图像。该代码加载源Microsoft Excel文件，然后将第一个工作表上找到的第一个图表保存为SVG。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object from source file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "SampleChartBook.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart inside the worksheet
const chart = worksheet.getCharts().get(0);

// Set image or print options
const opts = new AsposeCells.ImageOrPrintOptions();
opts.setImageType(AsposeCells.ImageType.Svg);

// Save the chart to svg format
chart.toImage(path.join(dataDir, "Image_out.svg"), opts);
```  


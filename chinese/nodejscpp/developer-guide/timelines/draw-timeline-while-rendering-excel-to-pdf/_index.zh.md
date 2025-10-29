---  
title: 在通过 C++ 将 Excel 渲染为 PDF 时绘制时间线  
linktitle: 将Excel渲染为PDF时绘制时间轴  
type: docs  
weight: 60  
url: /zh/nodejs-cpp/draw-timeline-while-rendering-excel-to-pdf/  
description: 使用Aspose.Cells for Node.js via C++管理Excel文件的时间线。  
keywords: 在没有 Office 2013、Office 2016、Office 2019 和 Office 365 的情况下，将时间线渲染为 PDF，使用 Node.js 通过 C++  
---  

## **将Excel文件应用时间轴并导出为PDF。Aspose.Cells for Java现在默认支持此功能。只需将带有时间轴的Excel文件导出为PDF，生成的PDF将显示应用的时间轴。**  
如果你有一个应用了时间线的Excel文件，并且想用时间线设置将Excel导出为PDF，Aspose.Cells for Node.js via C++现在支持此功能。只需将带有时间线的Excel文件导出为PDF，生成的PDF将显示时间线。  

以下示例代码加载包含现有时间轴的[样本Excel文件](input.xlsx)，然后将工作簿另存为[输出PDF文件](out.pdf)。以下屏幕截图比较了源Excel文件和生成的PDF文件。  

<img src="out.png" width="60%">  

## **示例代码**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");
// Load sample Excel file
const workbook = new AsposeCells.Workbook(filePath);
// Save file to pdf
workbook.save("out.pdf", AsposeCells.SaveFormat.Pdf);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}

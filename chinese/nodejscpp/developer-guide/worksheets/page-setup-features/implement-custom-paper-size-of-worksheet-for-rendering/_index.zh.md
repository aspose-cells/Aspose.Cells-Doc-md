---  
title: 用 Node.js 和 C++ 实现自定义纸张大小以便渲染  
linktitle: 实现工作表的自定义纸张大小以进行渲染  
type: docs  
weight: 70  
url: /zh/nodejs-cpp/implement-custom-paper-size-of-worksheet-for-rendering/  
description: 本文说明如何通过 Node.js API 和 C++ 设置自定义纸张大小，以便在将 Excel 文件渲染为 PDF 时使用。  
keywords: 用 Node.js 和 C++ 在渲染 Excel 为 PDF 时设置自定义纸张大小  
---  

## **可能的使用场景**  

MS Excel 没有直接创建自定义纸张大小的选项，但在将 Excel 文件渲染为 PDF 时，可以设置自定义纸张大小。本文介绍如何使用 Aspose.Cells API 设置工作表的自定义纸张大小。  

## **实现工作表的自定义纸张大小以进行渲染**  

Aspose.Cells允许您实现工作表的自定义纸张大小。您可以使用[**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/)类的[**PageSetup.customPaperSize(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#customPaperSize-number-number-)方法指定自定义页面大小。以下示例代码演示了如何为工作簿中的第一个工作表指定自定义纸张大小。请同时参考用以下代码生成的[输出PDF](45056028.pdf)。  

## **屏幕截图**  

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)  

## **示例代码**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Set custom paper size in unit of inches
ws.getPageSetup().customPaperSize(6, 4);

// Access cell B4
const b4 = ws.getCells().get("B4");

// Add the message in cell B4
b4.putValue("Pdf Page Dimensions: 6.00 x 4.00 in");

// Save the workbook in pdf format
wb.save(path.join(dataDir, "outputCustomPaperSize.pdf"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}

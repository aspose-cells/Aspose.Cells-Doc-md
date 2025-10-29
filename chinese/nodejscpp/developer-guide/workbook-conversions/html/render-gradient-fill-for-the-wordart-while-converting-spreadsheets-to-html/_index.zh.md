---  
title: 在将电子表格转换为HTML时为WordArt渲染渐变填充  
linktitle: 在将电子表格转换为HTML格式时渲染文字艺术的渐变填充  
type: docs  
weight: 90  
url: /zh/nodejs-cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/  
description: 学习如何在转换电子表格为HTML时为WordArt渲染渐变填充，使用Aspose.Cells for Node.js via C++。  
---  

## **可能的使用场景**  
在Aspose.Cells 17.1之前，转换为HTML格式时不支持WordArt的渐变填充。从Aspose.Cells 17.1版本开始，支持WordArt渐变填充。以下截图比较了使用Aspose.Cells 17.1和旧版本转换Excel文件时渐变填充的效果。  

![todo:image_alt_text](render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to-html_1.png)  

## **在将电子表格转换为HTML时渲染WordArt的渐变填充**  
以下示例代码将[源Excel文件](22774111.xlsx)转换成[输出HTML格式](22774109.zip)。源Excel文件中包含带有渐变填充的WordArt对象，如上截图所示。  

## **示例代码**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sourceGradientFill.xlsx");

// Read the source excel file having text with gradient fill
const workbook = new AsposeCells.Workbook(filePath);

// Save workbook to html format
workbook.save(path.join(dataDir, "out_sourceGradientFill.html"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}

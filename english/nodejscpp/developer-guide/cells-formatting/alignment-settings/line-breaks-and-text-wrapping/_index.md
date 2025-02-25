---  
title: Line Breaks and Text Wrapping with Node.js via C++  
linktitle: Line Breaks and Text Wrapping  
description: How to implement text wrapping and word wrap using the Aspose.Cells library in Node.js via C++. By using the Aspose.Cells library, you can easily insert text in cells and set the text wrapping method, such as manual word wrap, word wrap, etc. This document details how to implement these features and provides sample code for your reference.  
keywords: Aspose.Cells, line breaks, text wraps, text layout Node.js via C++  
type: docs  
weight: 60  
url: /nodejs-cpp/line-breaks-and-text-wrapping/  
---  

{{% alert color="primary" %}}  
To ensure that text in a cell can be read, explicit line breaks and text wrapping can be applied. Text wrapping turns one line into several in a cell, which explicit line breaks put in breaks exactly where you want them.  
{{% /alert %}}  

## **To Wrap Text in a Cell**  
To wrap text in a cell, use the [**Aspose.Cells.Style.isTextWrapped**](https://reference.aspose.com/cells/nodejs-cpp/style/#isTextWrapped) property.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create Workbook Object
const wb = new AsposeCells.Workbook();

// Open first Worksheet in the workbook
const ws = wb.getWorksheets().get(0);

// Get Worksheet Cells Collection
const cell = ws.getCells();

// Increase the width of First Column Width
cell.setColumnWidth(0, 35);

// Increase the height of first row
cell.setRowHeight(0, 36);

// Add Text to the First Cell
cell.checkCell(0, 0).putValue("I am using the latest version of Aspose.Cells to test this functionality");

// Make Cell's Text wrap
const style = cell.checkCell(0, 0).getStyle();
style.setIsTextWrapped(true);
cell.checkCell(0, 0).setStyle(style);

// Save Excel File
wb.save(path.join(dataDir, "WrappingText.out.xlsx"));
```  

## **To Use Explicit Line Breaks**  
You can use ‘\n’ in JavaScript to insert explicit line breaks in a cell.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create Workbook Object
const wb = new AsposeCells.Workbook();

// Open first Worksheet in the workbook
const ws = wb.getWorksheets().get(0);

// Get Worksheet Cells Collection
const cell = ws.getCells();

// Increase the width of First Column Width
cell.setColumnWidth(0, 35);

// Increase the height of first row
cell.setRowHeight(0, 65);

// Add Text to the First Cell with Explicit Line Breaks
cell.checkCell(0, 0).putValue("I am using\nthe latest version of \nAspose.Cells to \ntest this functionality");

// Make Cell's Text wrap
const style = cell.checkCell(0, 0).getStyle();
style.setIsTextWrapped(true);
cell.checkCell(0, 0).setStyle(style);

// Save Excel File
wb.save(path.join(dataDir, "WrappingText.out.xlsx"));
```  
  
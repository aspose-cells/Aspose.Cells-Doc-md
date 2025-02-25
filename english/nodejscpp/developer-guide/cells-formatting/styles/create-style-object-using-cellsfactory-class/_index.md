---
title: Create Style object using CellsFactory class with Node.js via C++
linktitle: Create Style object using CellsFactory class
description: Learn how to create a cell style object using the CellsFactory class in Aspose.Cells for Node.js via C++. Customize the appearance of spreadsheet cells as needed.
keywords: Aspose.Cells, Node.js via C++, electronic spreadsheet, style object, cell style, customization
type: docs
weight: 70
url: /nodejs-cpp/create-style-object-using-cellsfactory-class/
---

## **Create Style object using CellsFactory class**
The following sample code creates [Style](https://reference.aspose.com/cells/nodejs-cpp/style) object using [CellsFactory](https://reference.aspose.com/cells/nodejs-cpp/cellsfactory) class and then sets the Default Style of the workbook. Please download the [output excel file](5115153.xlsx) to see the results of this code for your reference.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a Style object using CellsFactory class
const cf = new AsposeCells.CellsFactory();
const st = cf.createStyle();

// Set the Style fill color to Yellow
st.setPattern(AsposeCells.BackgroundType.Solid);
st.setForegroundColor(AsposeCells.Color.Yellow);

// Create a workbook and set its default style using the created Style object
const wb = new AsposeCells.Workbook();
wb.setDefaultStyle(st);

// Save the workbook
wb.save(path.join(dataDir, "output_out.xlsx"));
```

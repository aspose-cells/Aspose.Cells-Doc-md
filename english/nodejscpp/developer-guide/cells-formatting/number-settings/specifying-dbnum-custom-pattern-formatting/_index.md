---
title: Specifying DBNum Custom Pattern Formatting with Node.js via C++
linktitle: Specifying DBNum Custom Pattern Formatting
description: Aspose.Cells is a library for Node.js via C++ that supports formatting dates and numbers using custom formatting patterns. This article shows how to specify the 'dbnum' custom format pattern for better control over number display.
keywords: Aspose.Cells, Node.js via C++, electronic spreadsheet, custom format pattern, formatting, 'dbnum', control display
type: docs
weight: 110
url: /nodejs-cpp/specifying-dbnum-custom-pattern-formatting/
---

## **Possible Usage Scenarios**

Aspose.Cells for Node.js via C++ supports the *DBNum* custom pattern formatting. For example, if your cell value is 123 and you specify its custom formatting as [DBNum2][$-804]General then it will be displayed like 壹佰贰拾叁. You can specify your custom formatting of the cell using [**Cell.getStyle()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle) method and [**Style.custom**](https://reference.aspose.com/cells/nodejs-cpp/style/properties/#custom) property.

## **Sample Code**

The following sample code illustrates how to specify *DBNum* custom pattern formatting. Please check its [output PDF](43352081.pdf) for more help.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create a workbook.
const wb = new AsposeCells.Workbook();

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Access cell A1 and put value 123.
const cell = ws.getCells().get("A1");
cell.putValue(123);

// Access cell style.
const st = cell.getStyle();

// Specifying DBNum custom pattern formatting.
st.setCustom("[DBNum2][$-804]General");

// Set the cell style.
cell.setStyle(st);

// Set the first column width.
ws.getCells().setColumnWidth(0, 30);

// Save the workbook in output pdf format.
wb.save(path.join(dataDir, "outputDBNumCustomFormatting.pdf"), AsposeCells.SaveFormat.Pdf);
```  

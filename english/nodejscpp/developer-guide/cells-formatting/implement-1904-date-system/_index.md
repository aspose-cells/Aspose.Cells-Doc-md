---
title: Implement 1904 Date System with Node.js via C++
description: Aspose.Cells is a Node.js library for working with spreadsheet files. It supports the implementation of the 1904 date system, allowing users to calculate and format based on the January 1, 1904 date system. This article describes how to implement the 1904 date system using the Aspose.Cells library.
keywords: Aspose.Cells, 1904 date system, spreadsheet, calculation, formatting, Node.js via C++
type: docs
weight: 7000
url: /nodejs-cpp/implement-1904-date-system/
---

{{% alert color="primary" %}} 

Microsoft Excel supports two date systems: 1900 date system (the default date system implemented in Excel for Windows) and 1904 date system. The 1904 date system is normally used to provide compatibility with Macintosh Excel files and is the default system if you are using Excel for Macintosh. You can set the 1904 date system for Excel files using Aspose.Cells for Node.js via C++. 

{{% /alert %}} 

To implement the 1904 date system in Microsoft Excel (for example, Microsoft Excel 2003):

1. From the **Tools** menu, select **Options**, and select the **Calculation** tab.
1. Select the **1904 date system** option.
1. Click **OK**.

|**Selecting 1904 date system in Microsoft Excel**|
| :- |
|![todo:image_alt_text](implement-1904-date-system_1.png)|

See the following sample code on how to achieve this using Aspose.Cells APIs.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xlsx");
// Initialize a new Workbook
// Open an excel file
const workbook = new AsposeCells.Workbook(filePath);

// Implement 1904 date system
workbook.getSettings().setDate1904(true);

// Save the excel file
workbook.save(path.join(dataDir, "Mybook.out.xlsx"));
```

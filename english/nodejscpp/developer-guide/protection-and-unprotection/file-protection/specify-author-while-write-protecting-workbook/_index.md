---  
title: Specify Author while Write Protecting Workbook with Node.js via C++  
linktitle: Specify Author while Write Protecting Workbook  
type: docs  
weight: 40  
url: /nodejs-cpp/specify-author-while-write-protecting-workbook/  
description: Specify an author name while write protecting a workbook using Aspose.Cells for Node.js via C++.  
---  

## **Possible Usage Scenarios**

You can specify an author name while write protecting your workbook using Aspose.Cells API. Please use [**Workbook.settings.writeProtection.author**](https://reference.aspose.com/cells/nodejs-cpp/writeprotection/properties/author) property for this purpose.

## **Specify Author while Write Protecting Workbook**

The following sample code explains the usage of [**Workbook.settings.writeProtection.author**](https://reference.aspose.com/cells/nodejs-cpp/writeprotection/properties/author) property. The code creates an empty workbook, write protects it with a password, specifies the author name, and saves it as [output Excel file](67338582.xlsx). The following screenshot illustrates the effect of the sample code on the output Excel file for your reference.

![todo:image_alt_text](specify-author-while-write-protecting-workbook_1.png)

## **Sample Code**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Create empty workbook.
const workbook = new AsposeCells.Workbook();

// Write protect workbook with password.
workbook.getSettings().getWriteProtection().setPassword("1234");

// Specify author while write protecting workbook.
workbook.getSettings().getWriteProtection().setAuthor("SimonAspose");

// Save the workbook in XLSX format.
const outputDir = path.join(__dirname, "output");
workbook.save(path.join(outputDir, "outputSpecifyAuthorWhileWriteProtectingWorkbook.xlsx"));
```  
  
---  
title: Specify Author while Write Protecting Workbook with Node.js via C++  
linktitle: Specify Author while Write Protecting Workbook  
type: docs  
weight: 40  
url: /nodejs-cpp/specify-author-while-write-protecting-workbook/  
description: Specify an author name while write-protecting a workbook using Aspose.Cells for Node.js via C++.  
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

## **Possible Usage Scenarios**

You can specify an author name while write-protecting your workbook using the Aspose.Cells API. Please use [**Workbook.getAuthor()**](https://reference.aspose.com/cells/nodejs-cpp/writeprotection/#getAuthor--) property for this purpose.

## **Specify Author while Write Protecting Workbook**

The following sample code demonstrates the usage of [**Workbook.getAuthor()**](https://reference.aspose.com/cells/nodejs-cpp/writeprotection/#getAuthor--) property. The code creates an empty workbook, write-protects it with a password, specifies the author name, and saves it as an [output Excel file](67338582.xlsx). The following screenshot illustrates the effect of the sample code on the output Excel file for your reference.

![todo:image_alt_text](specify-author-while-write-protecting-workbook_1.png)

## **Sample Code**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Create an empty workbook.
const workbook = new AsposeCells.Workbook();

// Write-protect the workbook with a password.
workbook.getSettings().getWriteProtection().setPassword("1234");

// Specify the author while write-protecting the workbook.
workbook.getSettings().getWriteProtection().setAuthor("SimonAspose");

// Save the workbook in XLSX format.
const outputDir = path.join(__dirname, "output");
workbook.save(path.join(outputDir, "outputSpecifyAuthorWhileWriteProtectingWorkbook.xlsx"));
```  
  
{{< app/cells/assistant language="nodejs-cpp" >}}

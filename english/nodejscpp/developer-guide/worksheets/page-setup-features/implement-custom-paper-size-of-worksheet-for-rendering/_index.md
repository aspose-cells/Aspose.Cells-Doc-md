---  
title: Implement Custom Paper Size of Worksheet for Rendering with Node.js via C++  
linktitle: Implement Custom Paper Size of Worksheet for Rendering  
type: docs  
weight: 70  
url: /nodejs-cpp/implement-custom-paper-size-of-worksheet-for-rendering/  
description: This article explains how to use the Node.js API via C++ to set a custom paper size for your desired worksheets when rendering an Excel file to PDF format programmatically.  
keywords: set custom paper size while rendering excel to pdf Node.js via C++  
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

## **Possible Usage Scenarios**  

There is no direct option available to create custom paper sizes in MS Excel, however, you can set a custom paper size of your desired worksheets when rendering an Excel file to PDF format. This document explains how to set a custom paper size of a worksheet using Aspose.Cells APIs.  

## **Implement Custom Paper Size of Worksheet for Rendering**  

Aspose.Cells allows you to implement your desired paper size of the worksheet. You may use the [**PageSetup.customPaperSize(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#customPaperSize-number-number-) method of the [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/) class to specify a custom page size. The following sample code illustrates how to specify a custom paper size for the first worksheet in the workbook. Please also see the [output PDF](45056028.pdf) generated with the following code for reference.  

## **Screenshot**  

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)  

## **Sample Code**  

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

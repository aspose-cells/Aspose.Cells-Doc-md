---  
title: Reusing Style Objects with Node.js via C++  
linktitle: Reusing Style Objects  
description: In Aspose.Cells for Node.js via C++, by creating and using reusable style objects, you can simplify style management and improve code efficiency. Our guide will help you leverage the advantages of reusable style objects and implement them in your application.  
keywords: Aspose.Cells for Node.js via C++, Reusing Style Objects, Style Management, Code Efficiency, Reusable Styles, Application Development, API Reference, Example Code, Download, Support.  
type: docs  
weight: 3000  
url: /nodejs-cpp/reusing-style-objects/  
---  

{{% alert color="primary" %}}  
Reusing style objects can save memory and make a program faster.  
{{% /alert %}}  

To apply some formatting to a large range of cells in a worksheet:

1. Create a style object.
1. Specify the attributes.
1. Apply the style to the cells in the range.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const workbook = new AsposeCells.Workbook();

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access cells
const cell1 = worksheet.getCells().get("A1");
const cell2 = worksheet.getCells().get("B1");

// Set the styles of both cells to Times New Roman
const styleObject = workbook.createStyle();
styleObject.getFont().setColor(AsposeCells.Color.Red);
styleObject.getFont().setName("Times New Roman");
cell1.setStyle(styleObject);
cell2.setStyle(styleObject);

// Put the values inside the cell
cell1.putValue("Hello World!");
cell2.putValue("Hello World!!");

// Save to Pdf without setting PdfSaveOptions.IsFontSubstitutionCharGranularity
workbook.save(path.join(dataDir, "SampleOutput_out.xlsx"));
```  

{{% alert color="primary" %}}  
Because the [**Cell.getStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle) / [**Cell.setStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle) approach uses a lot less memory, and is efficient, the older Cell.style property which consumed a lot of unnecessary memory was removed with the release of Aspose.Cells 7.1.0.  
{{% /alert %}}  
  
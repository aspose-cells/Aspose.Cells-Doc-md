---  
title: Render Gradient Fill for the WordArt while Converting Spreadsheets to HTML with Node.js via C++  
linktitle: Render Gradient Fill for the WordArt while Converting Spreadsheets to HTML  
type: docs  
weight: 90  
url: /nodejs-cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/  
description: Learn how to render gradient fill for WordArt when converting spreadsheets to HTML using Aspose.Cells for Node.js via C++.  
---  

## **Possible Usage Scenarios**  
Before Aspose.Cells 17.1, Aspose.Cells did not render gradient fill of the WordArt when the Excel file was converted to HTML format. Since the release of Aspose.Cells 17.1, WordArt gradient fill is supported. The following screenshot compares the effect on the gradient fill by converting the Excel file using Aspose.Cells 17.1 and the older version.  

![todo:image_alt_text](render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to-html_1.png)  

## **Render Gradient Fill for the WordArt while converting spreadsheets to HTML**  
The following sample code converts the [source excel file](22774111.xlsx) into [output HTML format](22774109.zip). The source excel file contains a WordArt object with gradient fill as shown in the above screenshot.  

## **Sample Code**  
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
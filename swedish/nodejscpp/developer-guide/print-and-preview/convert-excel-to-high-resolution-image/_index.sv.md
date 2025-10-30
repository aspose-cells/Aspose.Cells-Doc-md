---  
title: Konvertera Excel till högupplöst bild med Node.js via C++  
linktitle: Konvertera Excel till högupplöst bild  
type: docs  
weight: 100  
url: /sv/nodejs-cpp/convert-excel-to-high-resolution-image/  
description: Lär dig hur du konverterar Excel filer till högupplösta bilder med Aspose.Cells for Node.js via C++.  
---  

 Med ökad förekomst av högupplösta skärmar verkar bilder som genereras vid standard 96 DPI ofta suddiga och otydliga. För att säkerställa klarhet på högupplösta skärmar är det viktigt att generera bilder vid högre DPI. Aspose.Cells for Node.js via C++ erbjuder funktionalitet att ställa in [**ImageOrPrintOptions.getHorizontalResolution()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getHorizontalResolution--) och [**ImageOrPrintOptions.getVerticalResolution()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getVerticalResolution--), vilket gör att du kan skapa högkvalitativa bilder från Excel-filer som ser skarpa ut på högupplösta displayer.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");

// Load the Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Create an instance of ImageOrPrintOptions
const options = new AsposeCells.ImageOrPrintOptions();
options.setHorizontalResolution(300);
options.setVerticalResolution(300);
options.setImageType(AsposeCells.ImageType.Png);

// Get the worksheet
const sheet = workbook.getWorksheets().get(0);

// Create a SheetRender instance
const render = new AsposeCells.SheetRender(sheet, options);

// Generate and save the image
render.toImage(0, "output.png");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}

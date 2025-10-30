---  
title: Excel in hochauflösendes Bild mit Node.js über C++ konvertieren  
linktitle: Excel in hochauflösendes Bild umwandeln  
type: docs  
weight: 100  
url: /de/nodejs-cpp/convert-excel-to-high-resolution-image/  
description: Erfahren Sie, wie Sie Excel Dateien mit Aspose.Cells for Node.js via C++ in hochauflösende Bilder umwandeln.  
---  

Mit der zunehmenden Verbreitung hochauflösender Bildschirme erscheinen bei der Standardauflösung von 96 DPI erzeugte Bilder oft unscharf und unklar. Um auf hochauflösenden Bildschirmen Klarheit zu gewährleisten, ist es notwendig, Bilder bei höherer DPI zu erstellen. Aspose.Cells for Node.js via C++ bietet die Funktion, [**ImageOrPrintOptions.getHorizontalResolution()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getHorizontalResolution--) und [**ImageOrPrintOptions.getVerticalResolution()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getVerticalResolution--) zu setzen, um hochwertige Bilder aus Excel-Dateien zu erzeugen, die auf hochauflösenden Bildschirmen scharf aussehen.  

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

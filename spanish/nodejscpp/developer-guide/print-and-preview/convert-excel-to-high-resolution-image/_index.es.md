---  
title: Convertir Excel a Imagen de Alta Resolución con Node.js a través de C++  
linktitle: Convertir Excel en Imagen de Alta Resolución  
type: docs  
weight: 100  
url: /es/nodejs-cpp/convert-excel-to-high-resolution-image/  
description: Aprende cómo convertir archivos Excel en imágenes de alta resolución utilizando Aspose.Cells for Node.js via C++.  
---  

Con la creciente prevalencia de pantallas de alta resolución, las imágenes generadas en la resolución predeterminada de 96 DPI suelen aparecer borrosas y poco claras. Para garantizar la claridad en pantallas de alta resolución, es fundamental generar imágenes a mayor DPI. Aspose.Cells for Node.js via C++ ofrece la funcionalidad de establecer [**ImageOrPrintOptions.getHorizontalResolution()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getHorizontalResolution--) y [**ImageOrPrintOptions.getVerticalResolution()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getVerticalResolution--), permitiéndote crear imágenes de alta calidad a partir de archivos de Excel que se ven nítidas en pantallas de alta resolución.  

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


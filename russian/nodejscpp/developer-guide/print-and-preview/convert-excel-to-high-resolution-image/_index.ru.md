---  
title: Конвертация Excel в изображение высокого разрешения с помощью Node.js через C++  
linktitle: Конвертация Excel в изображение высокого разрешения  
type: docs  
weight: 100  
url: /ru/nodejs-cpp/convert-excel-to-high-resolution-image/  
description: Узнайте, как преобразовать файлы Excel в изображения высокого разрешения с помощью Aspose.Cells for Node.js via C++.  
---  

С увеличением популярности дисплеев высокого разрешения изображения, созданные по умолчанию с 96 DPI, выглядят размытыми и неясными. Чтобы обеспечить четкость на дисплеях высокого разрешения, важно создавать изображения с большим DPI. Aspose.Cells for Node.js via C++ позволяет задавать [**ImageOrPrintOptions.getHorizontalResolution()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getHorizontalResolution--) и [**ImageOrPrintOptions.getVerticalResolution()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getVerticalResolution--), что позволяет создавать изображения высокого качества из файлов Excel, которые выглядят острыми на дисплеях с высоким разрешением.  

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

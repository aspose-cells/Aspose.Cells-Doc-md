---  
title: تحويل إكسل إلى صورة عالية الدقة باستخدام Node.js عبر C++  
linktitle: تحويل إكسل إلى صورة عالية الدقة  
type: docs  
weight: 100  
url: /ar/nodejs-cpp/convert-excel-to-high-resolution-image/  
description: تعرف على كيفية تحويل ملفات إكسل إلى صور عالية الدقة باستخدام Aspose.Cells for Node.js via C++.  
---  

نظرًا لانتشار الشاشات عالية الدقة، غالبًا ما تظهر الصور المولدة عند 96 DPI الافتراضية مشوشة وغير واضحة. لضمان الوضوح على الشاشات عالية الدقة، من الضروري توليد الصور بدقة أعلى. يوفر Aspose.Cells for Node.js via C++ وظيفة لضبط [**ImageOrPrintOptions.getHorizontalResolution()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getHorizontalResolution--) و [**ImageOrPrintOptions.getVerticalResolution()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getVerticalResolution--)، مما يتيح لك إنشاء صور عالية الجودة من ملفات إكسل تظهر حادة على شاشات عالية الدقة.  

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

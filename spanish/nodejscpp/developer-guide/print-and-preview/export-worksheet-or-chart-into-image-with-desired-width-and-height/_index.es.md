---  
title: Exportar hoja de trabajo o gráfico en una imagen con ancho y alto deseados vía Node.js  
linktitle: Exportar hoja de cálculo o gráfico a imagen con ancho y alto deseados  
type: docs  
weight: 290  
url: /es/nodejs-cpp/export-worksheet-or-chart-into-image-with-desired-width-and-height/  
description: Aprenda cómo exportar una hoja de trabajo o gráfico a una imagen con ancho y alto especificados usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Puede usar Aspose.Cells for Node.js via C++ para exportar su hoja de trabajo o gráfico a una imagen con el ancho y alto deseados. Proporciona el método [**ImageOrPrintOptions.setDesiredSize(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#setDesiredSize-number-number-boolean-) para establecer el ancho y alto deseados de la imagen exportada. El ancho y alto se especifican en la unidad de píxeles.  
{{% /alert %}}  

El siguiente código exporta la hoja de cálculo a una imagen con tamaño de 400x400.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Create workbook object from source file
const filePath = path.join(sourceDir, "sampleWorksheetToImageDesiredSize.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Set image or print options we want one page per sheet. The image format is in png and desired dimensions are 400x400
const opts = new AsposeCells.ImageOrPrintOptions();
opts.setOnePagePerSheet(true);
opts.setImageType(AsposeCells.ImageType.Png);
opts.setDesiredSize(400, 400, false);

// Render sheet into image
const sr = new AsposeCells.SheetRender(worksheet, opts);
sr.toImage(0, path.join(outputDir, "outputWorksheetToImageDesiredSize.png"));
```  


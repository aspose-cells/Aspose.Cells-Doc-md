---
title: Generar miniatura de la hoja de trabajo con Node.js vía C++
linktitle: Generar miniatura de la hoja de cálculo
type: docs
weight: 110
url: /es/nodejs-cpp/generate-thumbnail-of-the-worksheet/
description: Aprenda cómo generar una imagen miniatura de una hoja de trabajo usando Aspose.Cells for Node.js via C++. Cree imágenes pequeñas para vistas previas en documentos y presentaciones.
---

{{% alert color="primary" %}} 

Puede ser útil generar miniaturas de hojas de cálculo. Una miniatura es una imagen pequeña que se puede pegar en un documento de Word o en una presentación de PowerPoint para dar una vista previa de lo que hay en la hoja de cálculo. Se puede agregar a una página web con un enlace para descargar el documento original y tiene una serie de otros usos.

{{% /alert %}} 

Aspose.Cells for Node.js via C++ le permite exportar hojas de trabajo a archivos de imagen, por lo que crear una miniatura es fácil. El código de ejemplo a continuación muestra cómo exportar hojas de trabajo a archivos de imagen.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Instantiate and open an Excel file
const filePath = path.join(sourceDir, "sampleGenerateThumbnailOfWorksheet.xlsx");
const book = new AsposeCells.Workbook(filePath);

// Define ImageOrPrintOptions
const imgOptions = new AsposeCells.ImageOrPrintOptions();

// Specify the image format
imgOptions.setImageType(AsposeCells.ImageType.Jpeg);

// Set the vertical and horizontal resolution
imgOptions.setVerticalResolution(200);
imgOptions.setHorizontalResolution(200);

// One page per sheet is enabled
imgOptions.setOnePagePerSheet(true);

// Set desired thumbnail dimensions
imgOptions.setDesiredSize(600, 600, true);

// Get the first worksheet
const sheet = book.getWorksheets().get(0);

// Render the sheet with respect to specified image/print options
const sr = new AsposeCells.SheetRender(sheet, imgOptions);

// Save the thumbnail directly
sr.toImage(0, path.join(outputDir, "outputGenerateThumbnailOfWorksheet.jpg"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}

---
title: Extraer imágenes de hojas de trabajo usando ImageOrPrintOptions con Node.js vía C++
linktitle: Extraer imágenes de hojas de cálculo utilizando ImageOrPrintOptions
type: docs
weight: 140
url: /es/nodejs-cpp/extract-images-from-worksheets-using-imageorprintoptions/
description: Aprenda cómo extraer imágenes de hojas de Excel y guardarlas usando Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}} 

Los usuarios de Microsoft Excel pueden agregar imágenes a hojas de cálculo. Con Aspose.Cells for Node.js via C++, es posible leer imágenes de archivos de Microsoft Excel y guardarlas en una unidad local. Este artículo muestra cómo.

{{% /alert %}} 

El código de muestra a continuación muestra cómo extraer imágenes de un archivo de Excel y guardarlas.



```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Open a template Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleExtractImagesFromWorksheets.xlsx"));

// Get the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Get the first Picture in the first worksheet
const pic = worksheet.getPictures().get(0);

// Set the output image file path
const picformat = pic.getImageType().toString();

// Note: you may evaluate the image format before specifying the image path
// Define ImageOrPrintOptions
const printoption = new AsposeCells.ImageOrPrintOptions();

// Specify the image format
printoption.setImageType(AsposeCells.ImageType.Jpeg);

// Save the image
pic.toImage(path.join(outputDir, "outputExtractImagesFromWorksheets.jpg"), printoption);
```
{{< app/cells/assistant language="nodejs-cpp" >}}

---
title: Convertir Hoja de Cálculo en Imagen  Eliminar espacio en blanco alrededor de los datos con Node.js a través de C++
linktitle: Convertir hoja de cálculo a imagen  Eliminar espacios en blanco alrededor de los datos
type: docs
weight: 40
url: /es/nodejs-cpp/convert-worksheet-to-image-remove-whitespace-around-data/
description: Aprende cómo convertir hojas de cálculo de Microsoft Excel en imágenes y eliminar espacios en blanco alrededor de los datos usando Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

A veces, es necesario presentar imágenes de hojas de cálculo en aplicaciones o páginas web. Por ejemplo, puede que necesites insertar imágenes en un documento de Word, un archivo PDF, una presentación de PowerPoint, u otro documento. Básicamente, quieres renderizar una hoja de cálculo como una imagen para poder pegarla en otras aplicaciones. Aspose.Cells te permite convertir hojas de cálculo de Excel en imágenes.

{{% /alert %}}

## **Eliminar espacios en blanco alrededor de los datos**

El API [**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender) convierte una hoja de cálculo en un archivo de imagen con atributos especificados, por ejemplo, formato de imagen, hojas paginadas, etc. Se admiten varios formatos de imagen, incluyendo BMP, GIF, JPG, TIFF y EMF.

Cuando utilizas la función de hoja a imagen, la imagen de salida tiene espacios en blanco, es decir, un borde, alrededor de ella de forma predeterminada. Puedes eliminar esto configurando los márgenes de configuración de página superior, inferior, izquierda y derecha de la hoja de origen en 0 y especificar los atributos [**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions) en consecuencia.

El siguiente fragmento de código elimina los espacios en blanco alrededor de los datos en la imagen de salida.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Open the template file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));

// Get the first worksheet
const sheet = workbook.getWorksheets().get(0);
const options = new AsposeCells.LoadOptions();
options.setLoadFilter(new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.All));
// Specify your print area if you want
// sheet.getPageSetup().setPrintArea("A1:H8");

// To remove the white border around the image.
sheet.getPageSetup().setLeftMargin(0);
sheet.getPageSetup().setRightMargin(0);
sheet.getPageSetup().setBottomMargin(0);
sheet.getPageSetup().setTopMargin(0);

// Define ImageOrPrintOptions
const imgOptions = new AsposeCells.ImageOrPrintOptions();
imgOptions.setImageType(AsposeCells.ImageType.Emf);

// Set only one page would be rendered for the image
imgOptions.setOnePagePerSheet(true);
imgOptions.setPrintingPage(AsposeCells.PrintingPageType.IgnoreBlank);

// Create the SheetRender object based on the sheet with its ImageOrPrintOptions attributes
const sr = new AsposeCells.SheetRender(sheet, imgOptions);

// Convert the image
sr.toImage(0, path.join(outputDir, "outputRemoveWhitespaceAroundData.emf"));
```

---  
title: Especificar cómo cruzar cadenas en el PDF de salida e imágenes con Node.js mediante C++  
linktitle: Especificar cómo cruzar cadenas en PDF de salida e imagen  
type: docs  
weight: 120  
url: /es/nodejs-cpp/specify-how-to-cross-string-in-output-pdf-and-image/  
description: Aprenda a controlar el desbordamiento de texto en PDF/Imagen de salida especificando el tipo de cruce usando Aspose.Cells for Node.js via C++.  
---  

## **Escenarios de uso posibles**

Cuando una celda contiene texto o una cadena, pero es más grande que el ancho de la celda, entonces la cadena desborda si la siguiente celda en la siguiente columna es nula o está vacía. Cuando guarda su archivo Excel en formato PDF/Imagen, puede controlar este desbordamiento especificando el tipo de cruce usando la enumeración [**TextCrossType**](https://reference.aspose.com/cells/nodejs-cpp/textcrosstype). Tiene los siguientes valores:

- **TextCrossType.Default**: Muestra el texto como MS Excel, lo que depende de la siguiente celda. Si la siguiente celda es nula, la cadena cruzará o se truncará.

- **TextCrossType.CrossKeep**: Mostrar la cadena como MS Excel exportando a PDF/Imagen.

- **TextCrossType.CrossOverride**: Mostrar todo el texto cruzando otras celdas y sobrescribir el texto de las celdas cruzadas.

- **TextCrossType.StrictInCell**: Solo muestra la cadena dentro del ancho de la celda.

## **Especifica cómo cruzar la cadena en el PDF/Imagen de salida utilizando TextCrossType**

El siguiente código de ejemplo carga el archivo de Excel de muestra y lo guarda en formato PDF/Imagen especificando diferentes [**TextCrossType**](https://reference.aspose.com/cells/nodejs-cpp/textcrosstype). El archivo de Excel de muestra y los archivos de salida se pueden descargar desde los siguientes enlaces:

[sampleCrossType.xlsx](81920905.xlsx)  

[outputCrossType.pdf](81920903.pdf)  

[outputCrossType.png](81920904.png)  

### Código de Ejemplo

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load template Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleCrosssType.xlsx"));

// Initialize PDF save options
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();

// Set text cross type
pdfSaveOptions.setTextCrossType(AsposeCells.TextCrossType.StrictInCell);

// Save PDF file
workbook.save(outputDir + "outputCrosssType.pdf", pdfSaveOptions);

// Initialize image or print options
const imageSaveOptions = new AsposeCells.ImageOrPrintOptions();

// Set text cross type
imageSaveOptions.setTextCrossType(AsposeCells.TextCrossType.StrictInCell);

// Initialize sheet renderer object
const sheetRenderer = new AsposeCells.SheetRender(workbook.getWorksheets().get(0), imageSaveOptions);

sheetRenderer.toImage(0, outputDir + "outputCrosssType.png");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}

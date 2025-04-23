---  
title: Imagen con Node.js a través de C++  
linktitle: Imagen  
type: docs  
weight: 300  
url: /es/nodejs-cpp/convert-excel-to-image/  
---  

{{% alert color="primary" %}}  
Aspose.Cells le permite exportar una hoja de cálculo del libro y convertirla a diferentes formatos. Este artículo explica cómo convertir una hoja de cálculo a diferentes formatos.  
{{% /alert %}}  

## Convirtiendo el libro a TIFF  

Un archivo de Excel puede contener varias hojas con varias páginas. [**WorkbookRender**](https://reference.aspose.com/cells/nodejs-cpp/workbookrender) permite convertir Excel a TIFF con múltiples páginas. Además, puedes controlar varias opciones para TIFF, como [ImageOrPrintOptions.getTiffCompression()](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getTiffCompression--), [ImageOrPrintOptions.getTiffColorDepth()](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getTiffColorDepth--), Resolución ([ImageOrPrintOptions.getHorizontalResolution()](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getHorizontalResolution--), [ImageOrPrintOptions.getVerticalResolution()](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getVerticalResolution--)).  

El siguiente fragmento de código muestra cómo convertir Excel a TIFF con múltiples páginas. Se adjuntan el [archivo de Excel de origen](workbook-to-tiff-with-mulitiple-pages.xlsx) y la [imagen TIFF generada](workbook-to-tiff-with-mulitiple-pages.tiff) para tu referencia.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "workbook-to-tiff-with-mulitiple-pages.xlsx");

// Load the workbook
const wb = new AsposeCells.Workbook(filePath);

const imgOptions = new AsposeCells.ImageOrPrintOptions();
imgOptions.setImageType(AsposeCells.ImageType.Tiff);

// Set resolution to 200
imgOptions.setHorizontalResolution(200);
imgOptions.setVerticalResolution(200);

// Set TIFF compression to LZW
imgOptions.setTiffCompression(AsposeCells.TiffCompression.CompressionLZW);

const workbookRender = new AsposeCells.WorkbookRender(wb, imgOptions);
workbookRender.toImage("workbook-to-tiff-with-mulitiple-pages.tiff");
```  

## **Conversión de hoja de cálculo a imagen**  

Las hojas de cálculo contienen datos que quieres analizar. Por ejemplo, una hoja de cálculo puede contener parámetros, totales, porcentajes, excepciones y cálculos.  

Como desarrollador, es posible que necesites presentar hojas de cálculo como imágenes. Por ejemplo, es posible que necesites utilizar una imagen de una hoja de cálculo en una aplicación o página web. Es posible que desees insertar una imagen en un documento de Microsoft Word, un archivo PDF, una presentación de PowerPoint u otro tipo de documento. En resumen, querrás una hoja de cálculo renderizada como una imagen para poder utilizarla en otro lugar.  

[**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender)
[**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions)
[**WorkbookRender**](https://reference.aspose.com/cells/nodejs-cpp/workbookrender)

La clase [**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender) representa una hoja de cálculo para renderizar como imágenes. Tiene un método sobrecargado, [**SheetRender.toImage(number, string)**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#toImage-number-string-), que puede convertir una hoja de cálculo en archivos de imagen con diferentes atributos u opciones. Devuelve un objeto Buffer y puedes guardar un archivo de imagen en disco o en streaming. Se soportan varios formatos de imagen, por ejemplo BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.  

El siguiente fragmento de código muestra cómo convertir una hoja de cálculo en un archivo de Excel a un archivo de imagen.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "sampleConvertWorksheetToImageByPage.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const sheet = workbook.getWorksheets().get(0);

const options = new AsposeCells.ImageOrPrintOptions();
options.setHorizontalResolution(200);
options.setVerticalResolution(200);
options.setImageType(AsposeCells.ImageType.Tiff);

// Sheet2Image By Page conversion
const sr = new AsposeCells.SheetRender(sheet, options);
for (let j = 0; j < sr.getPageCount(); j++) 
{
let path = "outputConvertWorksheetToImageByPage_" + (j + 1) + ".tif";
sr.toImage(j, path);
}
```  

{{% alert color="primary" %}}  
Actualmente, la API para convertir hojas de cálculo en imágenes no admite gráficos de burbujas 3D.  
{{% /alert %}}  

## **Conversión de hoja de cálculo a SVG**  

SVG significa Gráficos Vectoriales Escalables. SVG es una especificación basada en estándares XML para gráficos vectoriales bidimensionales. Es un estándar abierto que ha estado en desarrollo por el Consorcio World Wide Web (W3C) desde 1999.  

Aspose.Cells for Node.js via C++ ha podido convertir hojas de cálculo a imágenes SVG desde la versión 7.1.0. El siguiente fragmento de código muestra cómo convertir una hoja de cálculo en un archivo de imagen SVG.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(dataDir, "output");

// Instantiate a workbook
const workbook = new AsposeCells.Workbook();

// Put sample text in the first cell of the first worksheet in the newly created workbook
workbook.getWorksheets().get(0).getCells().get("A1").putValue("DEMO TEXT ON SHEET1");

// Add second worksheet in the workbook
workbook.getWorksheets().add(AsposeCells.SheetType.Worksheet);

// Set text in the first cell of the second sheet
workbook.getWorksheets().get(1).getCells().get("A1").putValue("DEMO TEXT ON SHEET2");

// Set currently active sheet index to 1 i.e. Sheet2
workbook.getWorksheets().setActiveSheetIndex(1);

// Save workbook to SVG. It shall render the active sheet only to SVG
workbook.save(path.join(outputDir, "ConvertWorksheetToSVG_out.svg"));
```  

## **Temas avanzados**  
- [Convertir un gráfico de Excel a imagen](/cells/es/nodejs-cpp/convert-an-excel-chart-to-image/)  
- [Convertir Gráfico a Imagen en Formato SVG](/cells/es/nodejs-cpp/converting-chart-to-image-in-svg-format/)  
- [Exportar gráfico a SVG con atributo viewBox](/cells/es/nodejs-cpp/export-chart-to-svg-with-viewbox-attribute/)  
- [Seguir el progreso de conversión de Excel a TIFF](/cells/es/nodejs-cpp/track-conversion-progress-of-excel-to-tiff/)  


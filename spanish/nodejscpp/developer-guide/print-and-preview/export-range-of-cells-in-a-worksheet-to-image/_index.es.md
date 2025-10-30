---  
title: Exportar rango de celdas en una hoja de trabajo a imagen con Node.js vía C++  
linktitle: Exportar rango de celdas en una hoja de cálculo a imagen  
type: docs  
weight: 60  
url: /es/nodejs-cpp/export-range-of-cells-in-a-worksheet-to-image/  
---  

## **Escenarios de uso posibles**  

Puede hacer una imagen de una hoja de trabajo usando Aspose.Cells for Node.js via C++. Sin embargo, a veces necesita exportar solo un rango de celdas en una hoja de trabajo a una imagen. Este artículo explica cómo lograrlo.  

## **Exportar un rango de celdas en una hoja de cálculo a una imagen**  

Para tomar una imagen de un rango, configure el área de impresión al rango deseado y luego configure todos los márgenes en 0. También configure [**ImageOrPrintOptions.getOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getOnePagePerSheet--) en **true**. El siguiente código toma una imagen del rango D8:G16. A continuación, una captura de pantalla del [archivo de ejemplo de Excel](47153160.xlsx) utilizado en el código. Puede probar el código con cualquier archivo de Excel.  

## **Captura de pantalla del archivo de Excel de muestra y su imagen exportada**  

**![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)**  

Al ejecutar el código se crea una imagen del rango D8:G16 solamente.  

**![todo:image_alt_text](Output-Image.png)**  

## **Código de muestra**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Create workbook from source file.
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleExportRangeOfCellsInWorksheetToImage.xlsx"));

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Set the print area with your desired range
worksheet.getPageSetup().setPrintArea("D8:G16");

// Set all margins as 0
worksheet.getPageSetup().setLeftMargin(0);
worksheet.getPageSetup().setRightMargin(0);
worksheet.getPageSetup().setTopMargin(0);
worksheet.getPageSetup().setBottomMargin(0);

// Set OnePagePerSheet option as true
const options = new AsposeCells.ImageOrPrintOptions();
options.setOnePagePerSheet(true);
options.setImageType(AsposeCells.ImageType.Jpeg);
options.setHorizontalResolution(200);
options.setVerticalResolution(200);

// Take the image of your worksheet
const sr = new AsposeCells.SheetRender(worksheet, options);
sr.toImage(0, path.join(outputDir, "outputExportRangeOfCellsInWorksheetToImage.jpg"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}

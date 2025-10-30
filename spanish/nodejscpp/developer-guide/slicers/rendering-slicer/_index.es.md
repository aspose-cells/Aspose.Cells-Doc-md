---  
title: Renderizar Segmentador con Node.js a través de C++  
linktitle: Renderizado de Slicer  
type: docs  
weight: 40  
url: /es/nodejs-cpp/rendering-slicer/  
---  

## **Escenarios de uso posibles**  
Aspose.Cells for Node.js via C++ soporta la renderización de formas de segmentador. Si conviertes tu hoja de cálculo en una imagen o guardas tu libro como PDF o HTML, verás que los segmentadores se renderizan correctamente.  

## **Renderización de rebanador**  
El siguiente código de ejemplo carga el [archivo Excel de muestra](67338479.xlsx) que contiene un segmentador existente. Convierte la hoja en una imagen estableciendo el área de impresión que solo cubre el segmentador. La imagen resultante es la [imagen de salida](67338480.png) que muestra el segmentador renderizado. Como puedes ver, el segmentador ha sido renderizado correctamente y se ve igual que en el archivo Excel de ejemplo.  

![todo:image_alt_text](rendering-slicer_1)  
## **Código de muestra**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleRenderingSlicer.xlsx");

// Load sample Excel file containing slicer.
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Set the print area because we want to render slicer only.
ws.getPageSetup().setPrintArea("B15:E25");

// Specify image or print options, set one page per sheet and only area to true.
const imgOpts = new AsposeCells.ImageOrPrintOptions();
imgOpts.setHorizontalResolution(200);
imgOpts.setVerticalResolution(200);
imgOpts.setImageType(AsposeCells.ImageType.Png);
imgOpts.setOnePagePerSheet(true);
imgOpts.setOnlyArea(true);

// Create sheet render object and render worksheet to image.
const sr = new AsposeCells.SheetRender(ws, imgOpts);
sr.toImage(0, "outputRenderingSlicer.png");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}

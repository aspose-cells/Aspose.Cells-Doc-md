---  
title: Copiar alturas de filas de un rango fuente a un rango de destino con Node.js a través de C++  
linktitle: Copiar alturas de fila del rango de origen al rango de destino  
type: docs  
weight: 590  
url: /es/nodejs-cpp/copy-row-heights-of-source-range-to-destination-range/  
---  

{{% alert color="primary" %}}  

A veces, los usuarios necesitan copiar las alturas de fila de un rango fuente a un rango de destino. Aspose.Cells for Node.js via C++ proporciona el enum [**PasteType.RowHeights**](https://reference.aspose.com/cells/nodejs-cpp/pastetype/) para este propósito. Cuando configures la propiedad [**PasteOptions.getPasteType()**](https://reference.aspose.com/cells/nodejs-cpp/pasteoptions/#getPasteType--) con [**PasteType.RowHeights**](https://reference.aspose.com/cells/nodejs-cpp/pastetype/), las alturas de todas las filas dentro del rango fuente se copiarán al rango de destino.  

{{% /alert %}}  

El siguiente código de ejemplo explica cómo usar el enum [**PasteType.RowHeights**](https://reference.aspose.com/cells/nodejs-cpp/pastetype/) para copiar las alturas de filas del rango fuente al rango de destino. Una vez que abras el archivo Excel generado con esta código en Microsoft Excel, verás que las alturas de fila del rango de destino son exactamente iguales a las del rango fuente.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const workbook = new AsposeCells.Workbook();

// Source worksheet
const srcSheet = workbook.getWorksheets().get(0);

// Add destination worksheet
const dstSheet = workbook.getWorksheets().add("Destination Sheet");

// Set the row height of the 4th row. This row height will be copied to destination range
srcSheet.getCells().setRowHeight(3, 50);

// Create source range to be copied
const srcRange = srcSheet.getCells().createRange("A1:D10");

// Create destination range in destination worksheet
const dstRange = dstSheet.getCells().createRange("A1:D10");

// PasteOptions, we want to copy row heights of source range to destination range
const opts = new AsposeCells.PasteOptions();
opts.setPasteType(AsposeCells.PasteType.RowHeights);

// Copy source range to destination range with paste options
dstRange.copy(srcRange, opts);

// Write informative message in cell D4 of destination worksheet
dstSheet.getCells().get("D4").putValue("Row heights of source range copied to destination range");

// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "output_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  


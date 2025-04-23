---  
title: Copier la hauteur des lignes de la plage source vers la plage de destination avec Node.js via C++  
linktitle: Copier la hauteur des lignes de la plage source vers la plage de destination  
type: docs  
weight: 590  
url: /fr/nodejs-cpp/copy-row-heights-of-source-range-to-destination-range/  
---  

{{% alert color="primary" %}}  

Parfois, les utilisateurs doivent copier la hauteur des lignes d'une plage source vers une plage de destination. Aspose.Cells for Node.js via C++ fournit un énumérateur [**PasteType.RowHeights**](https://reference.aspose.com/cells/nodejs-cpp/pastetype/) pour cette tâche. Lorsque vous définissez la propriété [**PasteOptions.getPasteType()**](https://reference.aspose.com/cells/nodejs-cpp/pasteoptions/#getPasteType--) avec [**PasteType.RowHeights**](https://reference.aspose.com/cells/nodejs-cpp/pastetype/), la hauteur de toutes les lignes dans la plage source sera copiée vers la plage de destination.  

{{% /alert %}}  

 Le code d'exemple suivant explique comment utiliser l'énumérator [**PasteType.RowHeights**](https://reference.aspose.com/cells/nodejs-cpp/pastetype/) pour copier la hauteur des lignes de la plage source vers la plage de destination. Une fois que vous ouvrez le fichier Excel généré par ce code dans Microsoft Excel, vous verrez que la hauteur des lignes de la plage de destination est exactement la même que celle de la plage source.  

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


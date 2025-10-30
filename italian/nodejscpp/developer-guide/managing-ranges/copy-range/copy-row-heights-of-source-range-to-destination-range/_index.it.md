---  
title: Copia altezza righe dall intervallo di origine all intervallo di destinazione con Node.js tramite C++  
linktitle: Copia l altezza delle righe dell intervallo di origine nell intervallo di destinazione  
type: docs  
weight: 590  
url: /it/nodejs-cpp/copy-row-heights-of-source-range-to-destination-range/  
---  

{{% alert color="primary" %}}  

A volte gli utenti devono copiare l'altezza delle righe di un intervallo di origine in un intervallo di destinazione. Aspose.Cells for Node.js via C++ fornisce l'enumerazione [**PasteType.RowHeights**](https://reference.aspose.com/cells/nodejs-cpp/pastetype/) per questo scopo. Quando imposti la proprietà [**PasteOptions.getPasteType()**](https://reference.aspose.com/cells/nodejs-cpp/pasteoptions/#getPasteType--) con [**PasteType.RowHeights**](https://reference.aspose.com/cells/nodejs-cpp/pastetype/), le altezze di tutte le righe all'interno dell'intervallo di origine saranno copiate nell'intervallo di destinazione.  

{{% /alert %}}  

Il seguente esempio di codice spiega come usare l'enumerazione [**PasteType.RowHeights**](https://reference.aspose.com/cells/nodejs-cpp/pastetype/) per copiare le altezze delle righe dall'intervallo di origine a quello di destinazione. Quando apri il file Excel generato da questo codice in Microsoft Excel, vedrai che le altezze delle righe dell'intervallo di destinazione sono esattamente uguali a quelle dell'intervallo di origine.  

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

{{< app/cells/assistant language="nodejs-cpp" >}}

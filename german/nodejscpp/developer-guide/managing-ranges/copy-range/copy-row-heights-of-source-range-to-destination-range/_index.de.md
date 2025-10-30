---  
title: Zeilenhöhen des Quellbereichs in Zielbereich mit Node.js über C++ kopieren  
linktitle: Quellenbereichszeilenhöhen in Zielbereich kopieren  
type: docs  
weight: 590  
url: /de/nodejs-cpp/copy-row-heights-of-source-range-to-destination-range/  
---  

{{% alert color="primary" %}}  

Manchmal müssen Benutzer die Zeilenhöhen eines Quellbereichs in einen Zielbereich kopieren. Aspose.Cells for Node.js via C++ bietet für diesen Zweck das [**PasteType.RowHeights**](https://reference.aspose.com/cells/nodejs-cpp/pastetype/) Enum. Wenn Sie die Eigenschaft [**PasteOptions.getPasteType()**](https://reference.aspose.com/cells/nodejs-cpp/pasteoptions/#getPasteType--) mit [**PasteType.RowHeights**](https://reference.aspose.com/cells/nodejs-cpp/pastetype/) setzen, werden die Höhen aller Zeilen im Quellbereich in den Zielbereich kopiert.  

{{% /alert %}}  

Das folgende Beispiel erklärt, wie man das [**PasteType.RowHeights**](https://reference.aspose.com/cells/nodejs-cpp/pastetype/) Enum verwendet, um die Zeilenhöhen des Quellbereichs in den Zielbereich zu kopieren. Sobald Sie die von diesem Code generierte Excel-Ausgabedatei in Microsoft Excel öffnen, werden Sie sehen, dass die Zeilenhöhen im Zielbereich genau die gleichen sind wie im Quellbereich.  

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

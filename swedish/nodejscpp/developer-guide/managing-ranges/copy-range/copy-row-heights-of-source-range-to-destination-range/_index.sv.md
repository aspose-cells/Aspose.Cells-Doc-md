---  
title: Kopiera radhöjder från källområde till destinationsområde med Node.js via C++  
linktitle: Kopiera radhöjderna i källområdet till destinationsområdet  
type: docs  
weight: 590  
url: /sv/nodejs-cpp/copy-row-heights-of-source-range-to-destination-range/  
---  

{{% alert color="primary" %}}  

Ibland behöver användare kopiera radhöjder från ett källområde till ett målområde. Aspose.Cells for Node.js via C++ tillhandahåller [**PasteType.RowHeights**](https://reference.aspose.com/cells/nodejs-cpp/pastetype/) enum för detta ändamål. När du ställer in egenskapen [**PasteOptions.getPasteType()**](https://reference.aspose.com/cells/nodejs-cpp/pasteoptions/#getPasteType--) med [**PasteType.RowHeights**](https://reference.aspose.com/cells/nodejs-cpp/pastetype/),, kommer höjderna för alla rader inom källområdet att kopieras till målområdet.  

{{% /alert %}}  

Följande exempel kod förklarar hur man använder [**PasteType.RowHeights**](https://reference.aspose.com/cells/nodejs-cpp/pastetype/) enum för att kopiera radhöjder från källområdet till målområdet. När du öppnar den genererade Excel-filen i Microsoft Excel, kommer du att se att radhöjderna i målområdet är exakt samma som i källområdet.  

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

---  
title: Formatera slicer med Node.js via C++  
linktitle: Formatering av Slicer  
type: docs  
weight: 20  
url: /sv/nodejs-cpp/formatting-slicer/  
---  

## **Möjliga användningsscenario**  

Du kan formatera slicern i Microsoft Excel genom att sätta antalet kolumner eller genom att ställa in dess stil osv. Aspose.Cells for Node.js via C++ låter dig också göra detta med hjälp av [**Slicer.getNumberOfColumns()**](https://reference.aspose.com/cells/nodejs-cpp/slicer/#getNumberOfColumns--) och [**Slicer.getStyleType()**](https://reference.aspose.com/cells/nodejs-cpp/slicer/#getStyleType--) egenskaper.  

## **Formatera skärva**  

Se följande kod, den laddar in [exempel Excel-filen](67338473.xlsx) som innehåller en slicer. Den kommer åt slicern och ställer in dess antal kolumner och stiltyp och sparar den som [utmatnings Excel-filen](67338474.xlsx). Skärmdumpen visar hur slicern ser ut efter exekveringen.  

![todo:image_alt_text](formatting-slicer_1.png)  

## **Exempelkod**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleFormattingSlicer.xlsx");
// Load sample Excel file containing slicer.
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Access the first slicer inside the slicer collection.
const slicer = ws.getSlicers().get(0);

// Set the number of columns of the slicer.
slicer.setNumberOfColumns(2);

// Set the type of slicer style.
slicer.setStyleType(AsposeCells.SlicerStyleType.SlicerStyleLight6);

// Save the workbook in output XLSX format.
wb.save("outputFormattingSlicer.xlsx", AsposeCells.SaveFormat.Xlsx);
```  


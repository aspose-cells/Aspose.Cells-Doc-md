---  
title: Skapa Union Range med Node.js via C++  
linktitle: Skapa Union Range  
type: docs  
weight: 360  
url: /sv/nodejs-cpp/create-union-range/  
description: Lär dig hur man skapar en Union Range med Aspose.Cells for Node.js via C++.  
keywords: Skapa Union Range Node.js via C++, Union Range Aspose.Cells Node.js, WorksheetCollection skapa union range Node.js  
---  

## **Skapa unionsspann**  
Aspose.Cells ger möjlighet att skapa en Union Range med hjälp av [WorksheetCollection.createUnionRange](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#createUnionRange-string-number-). Metoden [WorksheetCollection.createUnionRange](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#createUnionRange-string-number-) accepterar två parametrar, adressen för att skapa unionen och indexet för arbetsbladet. Metoden returnerar ett [UnionRange](https://reference.aspose.com/cells/nodejs-cpp/unionrange) objekt.  

Följande kodavsnitt visar hur man skapar ett unionintervall med hjälp av [WorksheetCollection.createUnionRange](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#createUnionRange-string-number-). Det genererade utdatafilen för referens är bifogad.  

- [Utdatafil](106364952.xlsx)  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Create union range
const unionRange = workbook.getWorksheets().createUnionRange("sheet1!A1:A10,sheet1!C1:C10", 0);

// Put value "ABCD" in the range
unionRange.setValue("ABCD");

// Save the output workbook.
workbook.save("CreateUnionRange_out.xlsx");
```  


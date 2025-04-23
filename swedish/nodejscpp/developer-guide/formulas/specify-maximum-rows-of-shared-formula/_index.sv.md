---  
title: Ange max antal rader för delad formel med Node.js via C++  
linktitle: Ange maximala rader för delad formel  
type: docs  
weight: 40  
url: /sv/nodejs-cpp/specify-maximum-rows-of-shared-formula/  
description: Lär dig hur du specificerar maximalt antal rader för delade formler med Aspose.Cells for Node.js via C++.  
---  

## **Möjliga användningsscenario**  

Standardmaximalt antal rader för delad formel är 64. Det kan vara vilket tal som helst, t.ex. 1000. Prestandan för delad formel förändras med ett annat antal rader. Därför ger Aspose.Cells egenskapen [**WorkbookSettings.getMaxRowsOfSharedFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxRowsOfSharedFormula--) som kan användas för att specificera det maximala antalet rader för den delade formeln. Den delade formeln delas upp i flera delade formler om det totala antalet rader för den delade formeln överstiger detta värde, vilket visas i följande skärmbild.  

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)  

## **Ange maximala rader för delad formel**  

Följande exempel förklarar användningen av egenskapen [**WorkbookSettings.getMaxRowsOfSharedFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxRowsOfSharedFormula--). Den sätter det maximala antalet rader för den delade formeln till 5 och lägger till den delade formeln i cell D1 för 100 rader och sparar till [utgångs-Excel fil](61767856.xlsx). Om du extraherar innehållet i utgångs-Excel-filen och kontrollerar *sheet1.xml*, kommer du att se att den delade formeln delas efter varje 5 rader som markerats i skärmbilden ovan.  

## **Exempelkod**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create a new workbook
const wb = new AsposeCells.Workbook();

// Set the max rows of shared formula to 5
wb.getSettings().setMaxRowsOfSharedFormula(5);

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access cell D1
const cell = ws.getCells().get("D1");

// Set the shared formula in 100 rows
cell.setSharedFormula("=Sum(A1:A2)", 100, 1);

// Save the output Excel file
wb.save("outputSpecifyMaximumRowsOfSharedFormula.xlsx");
```  


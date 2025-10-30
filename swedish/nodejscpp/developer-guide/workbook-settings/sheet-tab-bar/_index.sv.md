---  
title: Hur man styr bladflikens vagn med Node.js via C++  
linktitle: Hur man kontrollerar flikfält för arkhuvuden  
type: docs  
weight: 600  
url: /sv/nodejs-cpp/how-to-control-sheet-tab-bar/  
description: Lär dig hur man styr bladflikens vagn med Aspose.Cells for Node.js via C++.  
keywords: Hur man styr bladflikens vagn med Node.js via C++, hantera bladflikens vagn med Node.js via C++, ställ in bladflikens vagn med Node.js via C++, styr bladflikens vagn med Node.js via C++.  
---  

## **Möjliga användningsscenario**  
När du behöver justera visningen av Excel-bladets bar, måste du veta hur du styr bladflikens vagn, till exempel att dölja eller visa bladflikens vagn, ändra bredden på bladflikens vagn, ange det första synliga fliken och så vidare. Aspose.Cells for Node.js via C++ stöder dessa funktioner. Aspose.Cells tillhandahåller följande egenskaper och metoder för att hjälpa dig att uppnå dina mål.

- [**WorkbookSettings.getShowTabs()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShowTabs--)
- [**WorkbookSettings.getSheetTabBarWidth()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getSheetTabBarWidth--)
- [**WorkbookSettings.getFirstVisibleTab()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getFirstVisibleTab--)

## **Hur man styr bladflikens vagn med Aspose.Cells for Node.js via C++**  
Detta exempel visar hur man:

1. Skapa en arbetsbok.
1. Lägga till data till celler i den första arbetsboken.
1. Visa flikfältet och ange bredden på flikfältet.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the newly added worksheet
const ws = workbook.getWorksheets().get(0);
const cells = ws.getCells();

// Setting the value to the cells
let cell = cells.get("A1");
cell.putValue("Fruit");
cell = cells.get("B1");
cell.putValue("Count");
cell = cells.get("C1");
cell.putValue("Price");

cell = cells.get("A2");
cell.putValue("Apple");
cell = cells.get("A3");
cell.putValue("Mango");
cell = cells.get("A4");
cell.putValue("Blackberry");
cell = cells.get("A5");
cell.putValue("Cherry");

// Display the sheet tab and set the width of the tab bar
workbook.getSettings().setShowTabs(true);
workbook.getSettings().setSheetTabBarWidth(150);

workbook.save("out.xlsx");
```

Förhandsgranskning av resultatfil:  
<br>  
<image src="result.png" width="70%" />  


{{< app/cells/assistant language="nodejs-cpp" >}}

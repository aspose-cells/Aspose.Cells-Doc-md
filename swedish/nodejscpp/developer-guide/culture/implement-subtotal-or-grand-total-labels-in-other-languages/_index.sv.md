---  
title: Implementera subtotal eller totalsummor etiketter på andra språk med Node.js via C++  
linktitle: Implementera subtotal eller totalmärken på andra språk  
type: docs  
weight: 50  
url: /sv/nodejs-cpp/implement-subtotal-or-grand-total-labels-in-other-languages/  
---  

## **Möjliga användningsscenario**  

Ibland vill du visa subtotal- och totalsummoretiketter på icke-engelska språk som kinesiska, japanska, arabiska, hindi etc. Aspose.Cells for Node.js via C++ tillåter detta med hjälp av [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings)-klassen och [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/)-egenskapen. Se denna artikel för hur man använder [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings)-klassen.  

- [Användning av klassen GlobalizationSettings för anpassade subtotalmärken och andra märken för cirkeldiagram](/cells/sv/nodejs-cpp/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/)  

## **Implementera subtotal eller totalmärken på andra språk**  

Följande kodexempel laddar [exempel-Excel](5115151.xlsx) filen och implementerar subtotal- och totalsummonamn på kinesiska. Kontrollera det genererade [Excel-utdata](5115152.xlsx) för referens. Först skapar vi en klass av [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) och använder den därefter i vår kod.  

```javascript
const AsposeCells = require("aspose.cells.node");

class GlobalizationSettingsImp extends AsposeCells.GlobalizationSettings {
// This function will return the sub total name
getTotalName(functionType) {
return "Chinese Total - 可能的用法";
}

// This function will return the grand total name
getGrandTotalName(functionType) {
return "Chinese Grand Total - 可能的用法";
}
}
```  

Använd nu den skapade klassen i koden som nedan:  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load your source workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Set the globalization setting to change subtotal and grand total names
const globalizationSettings = new AsposeCells.GlobalizationSettings();
workbook.getSettings().setGlobalizationSettings(globalizationSettings);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Apply subtotal on A1:B10
const cellArea = AsposeCells.CellArea.createCellArea("A1", "B10");
worksheet.getCells().subtotal(cellArea, 0, AsposeCells.ConsolidationFunction.Sum, [2, 3, 4]);

// Set the width of the first column
worksheet.getCells().setColumnWidth(0, 40);

// Save the output excel file
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  


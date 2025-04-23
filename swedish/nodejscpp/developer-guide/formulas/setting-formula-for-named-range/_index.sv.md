---
title: Ställa in formel för namngiven rad med Node.js via C++
linktitle: Ange formel för namngivet område
type: docs
weight: 20
url: /sv/nodejs-cpp/setting-formula-for-named-range/
description: Lär dig hur du ställer in formler för namngivna rader i kalkylblad med hjälp av Aspose.Cells for Node.js via C++.
---

## **Ange formel för namngivet område**
Precis som Excel-appen erbjuder Aspose.Cells API möjligheten att specificera en formel för en namngiven rad medan du använder dess [Range.getRefersTo()](https://reference.aspose.com/cells/nodejs-cpp/range/#getRefersTo--) egenskap. Det kan finnas många användningsscenarier för denna funktion, några av vilka är tydligt beskrivna nedan.

### **Ange enkel formel för namngivet område**
Enkel formel skulle kunna vara en hänvisning till en annan cell i samma (eller annan) kalkylblad. Följande exempel skapar ett namngivet område i en ny kalkyl och anger dess hänvisning till en annan cell.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create an instance of Workbook
const book = new AsposeCells.Workbook();

// Get the WorksheetCollection
const worksheets = book.getWorksheets();

// Add a new Named Range with name "NewNamedRange"
const index = worksheets.getNames().add("NewNamedRange");

// Access the newly created Named Range
const name = worksheets.getNames().get(index);

// Set RefersTo property of the Named Range to a formula. Formula references another cell in the same worksheet
name.setRefersTo("=Sheet1!$A$3");

// Set the formula in the cell A1 to the newly created Named Range
worksheets.get(0).getCells().get("A1").setFormula("NewNamedRange");

// Insert the value in cell A3 which is being referenced in the Named Range
worksheets.get(0).getCells().get("A3").putValue("This is the value of A3");

// Calculate formulas
book.calculateFormula();

// Save the result in XLSX format
book.save(path.join(dataDir, "output_out.xlsx"));
```

### **Ange komplex formel för namngivet område**
En komplex formel kan vara vad som helst, till exempel en dynamiskt område eller en formel som sträcker sig över flera celler i olika kalkylblad. Följande exempel skapar ett dynamiskt område med hjälp av INDEX-funktionen för att hämta värdet från en lista baserat på dess plats.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const book = new AsposeCells.Workbook();

// Get the WorksheetCollection
const worksheets = book.getWorksheets();

// Add a new Named Range with name "data"
let index = worksheets.getNames().getCount();
worksheets.getNames().add("data");

// Access the newly created Named Range from the collection
const data = worksheets.getNames().get(index);

// Set RefersTo property of the Named Range to a cell range in same worksheet
data.setRefersTo("=Sheet1!$A$1:$A$10");

// Add another Named Range with name "range"
index = worksheets.getNames().getCount();
worksheets.getNames().add("range");

// Access the newly created Named Range from the collection
const range = worksheets.getNames().get(index);

// Set RefersTo property to a formula using the Named Range data
range.setRefersTo("=INDEX(data,Sheet1!$A$1,1):INDEX(data,Sheet1!$A$1,9)");

// Save the workbook
book.save(path.join(dataDir, "output_out.xlsx"));
```

Här är ytterligare ett exempel som använder ett namngivet område för att summera värden från 2 celler i olika kalkylblad.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create an instance of Workbook
const book = new AsposeCells.Workbook();

// Get the WorksheetCollection
const worksheets = book.getWorksheets();

// Insert some data in cell A1 of Sheet1
worksheets.get("Sheet1").getCells().get("A1").putValue(10);

// Add a new Worksheet and insert a value to cell A1
worksheets.get(worksheets.add()).getCells().get("A1").putValue(10);

// Add a new Named Range with name "range"
const index = worksheets.getNames().add("range");

// Access the newly created Named Range from the collection
const range = worksheets.getNames().get(index);

// Set RefersTo property of the Named Range to a SUM function
range.setRefersTo("=SUM(Sheet1!$A$1,Sheet2!$A$1)");

// Insert the Named Range as formula to 3rd worksheet
worksheets.get(worksheets.add()).getCells().get("A1").setFormula("range");

// Calculate formulas
book.calculateFormula();

// Save the result in XLSX format
book.save(path.join(dataDir, "output_out.xlsx"));
```

---
title: Formel für benannten Bereich mit Node.js über C++ festlegen
linktitle: Formel für benanntes Bereich setzen
type: docs
weight: 20
url: /de/nodejs-cpp/setting-formula-for-named-range/
description: Lernen Sie, wie Sie Formeln für benannte Bereiche in Tabellen mit Aspose.Cells for Node.js via C++ festlegen.
---

## **Formel für benanntes Bereich setzen**
Wie die Excel-Anwendung bieten die Aspose.Cells APIs die Möglichkeit, eine Formel für einen benannten Bereich anzugeben, während Sie seine [Range.getRefersTo()](https://reference.aspose.com/cells/nodejs-cpp/range/#getRefersTo--) Eigenschaft verwenden. Für diese Funktion gibt es zahlreiche Nutzungsszenarien, von denen einige im Folgenden erläutert werden.

### **Eine einfache Formel für benannten Bereich setzen**
Eine einfache Formel könnte eine Referenz auf eine andere Zelle im gleichen (oder anderen) Arbeitsblatt sein. Das folgende Beispiel erstellt einen benannten Bereich in einem neuen Tabellenblatt und setzt seine Referenz auf eine andere Zelle.

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

### **Eine komplexe Formel für benannten Bereich setzen**
Eine komplexe Formel könnte alles Mögliche sein, zum Beispiel ein dynamischer Bereich oder eine Formel über mehrere Zellen in verschiedenen Arbeitsblättern. Das folgende Beispiel erstellt einen dynamischen Bereich mit der INDEX-Funktion, um den Wert aus einer Liste basierend auf seiner Position zu erhalten.

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

Hier ist ein weiteres Beispiel, das einen benannten Bereich verwendet, um Werte aus 2 Zellen in verschiedenen Arbeitsblättern zu summieren.

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

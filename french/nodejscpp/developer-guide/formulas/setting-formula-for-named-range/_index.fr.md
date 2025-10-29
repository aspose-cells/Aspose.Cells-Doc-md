---
title: Définir une formule pour une plage nommée avec Node.js via C++
linktitle: Définition de la formule pour une plage nommée
type: docs
weight: 20
url: /fr/nodejs-cpp/setting-formula-for-named-range/
description: Apprenez comment définir des formules pour des plages nommées dans des feuilles de calcul à l aide de Aspose.Cells for Node.js via C++.
---

## **Définition de la formule pour une plage nommée**
Comme l'application Excel, les API Aspose.Cells offrent la possibilité de spécifier une formule pour une plage nommée en utilisant la propriété [Range.getRefersTo()](https://reference.aspose.com/cells/nodejs-cpp/range/#getRefersTo--). Plusieurs scénarios d'utilisation sont possibles pour cette fonctionnalité, quelques-uns sont détaillés ci-dessous.

### **Définir une formule simple pour une plage nommée**
Une formule simple pourrait être une référence à une autre cellule dans la même feuille de calcul (ou dans une feuille de calcul différente). L'exemple suivant crée une plage nommée dans une nouvelle feuille et défini sa référence à une autre cellule.

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

### **Définir une formule complexe pour une plage nommée**
Une formule complexe pourrait être n'importe quoi, comme une plage dynamique ou une formule s'étalant sur plusieurs cellules dans différentes feuilles de calcul. L'exemple suivant crée une plage dynamique en utilisant la fonction INDEX pour obtenir la valeur d'une liste en fonction de son emplacement.

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

Voici un autre exemple qui utilise une plage nommée pour additionner les valeurs de 2 cellules dans différentes feuilles de calcul.

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
{{< app/cells/assistant language="nodejs-cpp" >}}

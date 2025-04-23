---
title: Usare la funzione FormulaText in Aspose.Cells for Node.js via C++
linktitle: Utilizzo della funzione FormulaText in Aspose.Cells
description: Questo articolo introduce come usare la funzione FormulaText nella libreria Aspose.Cells per elaborare le formule in Microsoft Excel. Imparare a ottenere e impostare il testo della formula delle celle e salvare i file Excel modificati con Node.js via C++.
keywords: Aspose.Cells, Excel, funzioni FormulaText Node.js via C++
type: docs
weight: 60
url: /it/nodejs-cpp/using-formulatext-function-in-aspose-cells/
---

{{% alert color="primary" %}} 

FormulaText è una funzione introdotta in Excel 2013 e versioni successive. Non è supportata da versioni precedenti come Excel 2010 o 2007. Come suggerisce il nome, essa stampa il testo della formula presente in una cella data. Questo articolo mostrerà come utilizzare questa funzione con Aspose.Cells for Node.js via C++.

{{% /alert %}} 

Il seguente esempio di codice mostra l'uso di FormulaText con Aspose.Cells for Node.js via C++. Il codice scrive prima una formula nella cella A1 e poi stampa il testo della formula usando FormulaText in A2.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Create a workbook object
// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Put some formula in cell A1
const cellA1 = worksheet.getCells().get("A1");
cellA1.setFormula("=Sum(B1:B10)");

// Get the text of the formula in cell A2 using FORMULATEXT function
const cellA2 = worksheet.getCells().get("A2");
cellA2.setFormula("=FormulaText(A1)");

// Calculate the workbook
workbook.calculateFormula();

// Print the results of A2, It will now print the text of the formula inside cell A1
console.log(cellA2.getStringValue());
```
## **Output della console**
Ecco l'output della console del codice di esempio sopra.

{{< highlight java >}}

 =SUM(B1:B10)

{{< /highlight >}}

---
title: Verwendung der Funktion FormulaText in Aspose.Cells for Node.js via C++
linktitle: Verwendung der FormulaText Funktion in Aspose.Cells
description: Dieser Artikel zeigt, wie die Function FormulaText in der Aspose.Cells Bibliothek verwendet werden kann, um Formeln in Microsoft Excel zu verarbeiten. Lernen Sie, die Formeltext der Zellen zu holen und zu setzen sowie modifizierte Excel Dateien mit Node.js über C++ zu speichern.
keywords: Aspose.Cells, Excel, FormulaText Funktionen Node.js über C++
type: docs
weight: 60
url: /de/nodejs-cpp/using-formulatext-function-in-aspose-cells/
---

{{% alert color="primary" %}} 

FormulaText ist eine Funktion in Excel 2013 und neueren Versionen. Sie wird von älteren Versionen wie Excel 2010 oder 2007 nicht unterstützt. Wie der Name schon sagt, gibt sie den Text der Formel aus, die in einer bestimmten Zelle vorhanden ist. Dieser Artikel zeigt Ihnen, wie Sie diese Funktion mit Aspose.Cells for Node.js via C++ verwenden können.

{{% /alert %}} 

Der folgende Beispiels code zeigt die Verwendung von FormulaText mit Aspose.Cells for Node.js via C++. Der Code schreibt zuerst eine Formel in Zelle A1 und gibt dann den Text der Formel mit FormulaText in Zelle A2 aus.

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
## **Konsolenausgabe**
Hier ist die Konsolenausgabe des obigen Beispielcodes.

{{< highlight java >}}

 =SUM(B1:B10)

{{< /highlight >}}

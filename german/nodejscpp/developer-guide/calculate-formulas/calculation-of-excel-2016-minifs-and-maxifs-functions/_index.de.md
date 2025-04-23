---
title: Berechnung der MINIFS und MAXIFS Funktionen in Excel 2016 mit Node.js via C++
description: Dieser Artikel zeigt, wie man die Aspose.Cells Bibliothek verwendet, um MINIFS und MAXIFS Funktionen in Microsoft Excel 2016 mit Node.js via C++ zu berechnen. Laden Sie eine bestehende Excel Datei oder erstellen Sie eine neue, verwenden Sie die Methoden von Aspose.Cells, um diese Funktionen zu berechnen, und speichern Sie die Ergebnisse auf der Festplatte.
keywords: Aspose.Cells, Excel, 2016, MINIFS Funktion, MAXIFS Funktion, Berechnung Node.js via C++
type: docs
weight: 300
url: /de/nodejs-cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/
---

## **Mögliche Verwendungsszenarien**
Microsoft Excel 2016 unterstützt MINIFS- und MAXIFS-Funktionen. Diese Funktionen werden in Excel 2013 oder früheren Versionen nicht unterstützt. Aspose.Cells for Node.js via C++ unterstützt ebenfalls die Berechnung dieser Funktionen. Der folgende Screenshot zeigt die Verwendung dieser Funktionen. Lesen Sie die roten Kommentare im Screenshot, um zu erfahren, wie diese Funktionen funktionieren.

![todo:image_alt_text](calculation-of-excel-2016-minifs-and-maxifs-functions_1.png)

## **Berechnung der Excel 2016 MINIFS- und MAXIFS-Funktionen**
Der folgende Beispielcode lädt die [Beispieldatei Excel](5115149.xlsx) und ruft die [Workbook.calculateFormula()](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) Methode auf, um die Formeleingabe über Aspose.Cells for Node.js via C++ durchzuführen, und speichert dann die Ergebnisse in der [Ausgabedatei PDF](5115154.pdf).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleMINIFSAndMAXIFS.xlsx");

// Load your source workbook containing MINIFS and MAXIFS functions
const workbook = new AsposeCells.Workbook(sourceFilePath);

// Perform Aspose.Cells formula calculation
workbook.calculateFormula();

// Save the calculations result in pdf format
const options = new AsposeCells.PdfSaveOptions();
options.setOnePagePerSheet(true);
const outputFilePath = path.join(dataDir, "outputMINIFSAndMAXIFS.pdf");
workbook.save(outputFilePath, options);
```

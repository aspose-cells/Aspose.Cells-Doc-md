---
title: Berechnung von Array Formeln für Datentabellen mit Node.js via C++
linktitle: Berechnung der Array Formel von DatenTabellen
description: So verwenden Sie die Aspose.Cells Bibliothek, um Array Formeln für eine Datentabelle in Microsoft Excel mit Node.js via C++ zu berechnen. Laden oder erstellen Sie eine Excel Datei, berechnen Sie die Array Formel und speichern Sie die geänderte Datei.
keywords: Aspose.Cells, Excel, Datentabellen, Array Formeln, Berechnungen Node.js via C++
type: docs
weight: 70
url: /de/nodejs-cpp/calculation-of-array-formula-of-data-tables/
---

{{% alert color="primary" %}}

Sie können eine Datentabelle in Microsoft Excel mit Data > What-If Analysis > Data Table... erstellen. Aspose.Cells ermöglicht jetzt die Berechnung der Array-Formel einer Datentabelle. Verwenden Sie [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) wie gewohnt zur Berechnung aller Arten von Formeln.

{{% /alert %}}

Im folgenden Beispiellcode haben wir die [Quellexceldatei](5115535.xlsx) verwendet. Wenn Sie den Wert von Zelle B1 auf 100 ändern, werden die Werte der Datentabelle, die mit Gelb gefüllt sind, wie in den folgenden Bildern gezeigt, zu 120. Der Beispiellcode generiert die [Ausgabepdf](5115538.pdf).

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

Hier ist der Beispiellcode, der verwendet wurde, um das [Ausgabepdf](5115538.pdf) von der [Quellexceldatei](5115535.xlsx) zu generieren. Bitte lesen Sie die Kommentare für weitere Informationen.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create workbook from source excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "DataTable.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// When you will put 100 in B1, then all Data Table values formatted as Yellow will become 120
worksheet.getCells().get("B1").putValue(100);

// Calculate formula, now it also calculates Data Table array formula
workbook.calculateFormula();

// Save the workbook in pdf format
workbook.save(path.join(dataDir, "output_out.pdf"));
```

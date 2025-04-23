---
title: Formeln statt Werte in einem Arbeitsblatt mit Node.js über C++ anzeigen
linktitle: Statt Werte in einem Arbeitsblatt Formeln anzeigen
type: docs
weight: 20
url: /de/nodejs-cpp/show-formulas-instead-of-values-in-a-worksheet/
description: Dieser Artikel bietet Beispielcode für die Verwendung der Node.js API über C++, um programmgesteuert Formeln anzuzeigen, anstatt Werte in einem Excel Arbeitsblatt oder einer Tabelle.
---

{{% alert color="primary" %}}

Es ist möglich, Formeln anstelle berechneter Werte in Microsoft Excel mit der Option **Formeln anzeigen** auf der Registerkarte **Formeln** anzuzeigen. Wenn Formeln angezeigt werden, zeigt Microsoft Excel die Formeln im Arbeitsblatt an. Sie können dasselbe Ergebnis mit Aspose.Cells for Node.js via C++ erzielen.

{{% /alert %}}

Aspose.Cells bietet eine Eigenschaft [**Worksheet.getShowFormulas()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getShowFormulas--). Stellen Sie sie auf **true** ein, um Microsoft Excel anzuweisen, Formeln anzuzeigen.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "source.xlsx");

// Load the source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Show formulas of the worksheet
worksheet.setShowFormulas(true);

// Save the workbook
workbook.save(path.join(dataDir, ".out.xlsx"));
```

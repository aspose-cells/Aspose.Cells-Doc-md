---
title: Combinar o descombinar un rango de celdas con Node.js via C++
linktitle: Combinar o dividir rango de celdas
type: docs
weight: 190
url: /es/nodejs-cpp/merge-or-unmerge-range-of-cells/
description: Combinar y descombinar celdas en un rango en Excel con código Node.js via C++.
keywords: Node.js combina y descombina celdas en un rango, Node.js combina y descombina celdas en rango, combina y descombina celdas en rango con Node.js, combina y descombina celdas en rango usando Node.js, combina y descombina celdas en excel usando Node.js, combina y descombina celdas en excel con Node.js, Node.js combina y descombina celdas en excel, Node.js combina celdas en excel, Node.js descombina celdas en excel, combina celdas en rango con Node.js
---

{{% alert color="primary" %}}

Puede utilizar Aspose.Cells para combinar o dividir un rango de celdas. Aspose.Cells ofrece los métodos [**Range.merge()**](https://reference.aspose.com/cells/nodejs-cpp/range/#merge--) y [**Range.unMerge()**](https://reference.aspose.com/cells/nodejs-cpp/range/#unMerge--) para este propósito. Este artículo explica cómo combinar un rango de celdas en una sola celda.

{{% /alert %}}

## **Ejemplo**

El siguiente código de ejemplo primero crea un rango - A1:D4 - luego combina las celdas del rango en una sola usando el método [**Range.merge()**](https://reference.aspose.com/cells/nodejs-cpp/range/#merge--). De manera similar, puedes dividir celdas creando un rango y llamando al método [**Range.unMerge()**](https://reference.aspose.com/cells/nodejs-cpp/range/#unMerge--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create a workbook
const workbook = new AsposeCells.Workbook();

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Create a range
const range = worksheet.getCells().createRange("A1:D4");

// Merge range into a single cell
range.merge();

// Save the workbook
workbook.save(path.join(dataDir, "output.out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}

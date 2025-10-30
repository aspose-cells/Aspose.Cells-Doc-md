---
title: Trovare la posizione assoluta di una forma all interno del foglio di lavoro con Node.js tramite C++
linktitle: Trova la posizione assoluta della forma all interno del foglio di lavoro
type: docs
weight: 8000
url: /it/nodejs-cpp/finding-absolute-position-of-shape-inside-the-worksheet/
description: Scopri come trovare la posizione assoluta di una forma all’interno di un foglio di lavoro usando Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

A volte, hai bisogno di conoscere la posizione assoluta di una forma in un foglio di lavoro. Aspose.Cells for Node.js via C++ fornisce le proprietà [**Shape.getLeftToCorner()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getLeftToCorner--) e [**Shape.getTopToCorner()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTopToCorner--) a questo scopo. Queste proprietà restituiscono la posizione assoluta della forma all’interno del foglio di lavoro in pixel.

{{% /alert %}}

Il codice di esempio seguente visualizza la posizione assoluta della prima forma nel foglio di lavoro in pixel. Il codice di esempio visualizza l'output della console seguente:

{{< highlight java >}}

Absolute Position of this Shape is (320 , 183)

{{< /highlight >}}

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load the sample Excel file inside the workbook object
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the first shape inside the worksheet
const shape = worksheet.getShapes().get(0);

// Displays the absolute position of the shape
console.log(`Absolute Position of this Shape is (${shape.getLeftToCorner()} , ${shape.getTopToCorner()})`);
```
{{< app/cells/assistant language="nodejs-cpp" >}}

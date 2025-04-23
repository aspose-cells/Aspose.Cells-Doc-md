---
title: Finden Sie die absolute Position einer Form innerhalb des Arbeitsblatts mit Node.js via C++
linktitle: Ermittlung der absoluten Position einer Form innerhalb des Arbeitsblatts
type: docs
weight: 8000
url: /de/nodejs-cpp/finding-absolute-position-of-shape-inside-the-worksheet/
description: Lernen Sie, wie Sie die absolute Position einer Form innerhalb eines Arbeitsblatts mit Aspose.Cells for Node.js via C++ ermitteln. 
---

{{% alert color="primary" %}}

Manchmal müssen Sie die absolute Position einer Form in einem Arbeitsblatt kennen. Aspose.Cells for Node.js via C++ stellt die Eigenschaften [**Shape.getLeftToCorner()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getLeftToCorner--) und [**Shape.getTopToCorner()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTopToCorner--) dafür bereit. Diese Eigenschaften geben die absolute Position der Form im Arbeitsblatt in Pixeln zurück.

{{% /alert %}}

Der folgende Beispielcode zeigt die absolute Position der ersten Form im Arbeitsblatt in Pixeln an. Der Beispielcode zeigt die folgende Konsolenausgabe:

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

---
title: Encontrar posición absoluta de la forma dentro de la hoja de cálculo con Node.js vía C++
linktitle: Encontrar la posición absoluta de la forma dentro de la hoja de cálculo
type: docs
weight: 8000
url: /es/nodejs-cpp/finding-absolute-position-of-shape-inside-the-worksheet/
description: Aprende cómo encontrar la posición absoluta de una forma dentro de una hoja de cálculo usando Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

A veces, necesitas conocer la posición absoluta de una forma en una hoja de cálculo. Aspose.Cells for Node.js via C++ proporciona las propiedades [**Shape.getLeftToCorner()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getLeftToCorner--) y [**Shape.getTopToCorner()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTopToCorner--) para este propósito. Estas propiedades devuelven la posición absoluta de la forma dentro de la hoja en píxeles.

{{% /alert %}}

El siguiente código de ejemplo muestra la posición absoluta de la primera forma en la hoja de cálculo en píxeles. El código de ejemplo muestra la siguiente salida en la consola:

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

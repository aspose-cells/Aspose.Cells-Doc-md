---
title: Trouver la position absolue d une forme dans la feuille de calcul avec Node.js via C++
linktitle: Trouver la position absolue de la forme dans la feuille de calcul
type: docs
weight: 8000
url: /fr/nodejs-cpp/finding-absolute-position-of-shape-inside-the-worksheet/
description: Apprenez comment trouver la position absolue d’une forme dans une feuille de calcul en utilisant Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Parfois, vous devez connaître la position absolue d’une forme dans une feuille de calcul. Aspose.Cells for Node.js via C++ fournit les propriétés [**Shape.getLeftToCorner()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getLeftToCorner--) et [**Shape.getTopToCorner()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTopToCorner--) à cette fin. Ces propriétés retournent la position absolue de la forme dans la feuille de calcul en pixels.

{{% /alert %}}

Le code d'exemple suivant affiche la position absolue de la première forme dans la feuille de calcul en pixels. Le code d'exemple affiche la sortie console suivante :

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

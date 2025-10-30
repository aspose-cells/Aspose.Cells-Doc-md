---
title: Att hitta absolut position för forma i kalkylbladet med Node.js via C++
linktitle: Hitta absolut position av formen innanför arbetsbladet
type: docs
weight: 8000
url: /sv/nodejs-cpp/finding-absolute-position-of-shape-inside-the-worksheet/
description: Lär dig hur man hittar den absoluta positionen för en figur i ett kalkylblad med Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Ibland behöver du veta den absoluta positionen för en figur i ett kalkylblad. Aspose.Cells for Node.js via C++ tillhandahåller egenskaperna [**Shape.getLeftToCorner()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getLeftToCorner--) och [**Shape.getTopToCorner()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTopToCorner--) för detta ändamål. Dessa egenskaper returnerar den absoluta positionen för figuren inuti kalkylbladet i pixlar.

{{% /alert %}}

Följande exempel på kod visar den absoluta positionen för den första formen i arbetsbladet i pixlar. Exempelkoden visar följande konsolresultat:

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

---
title: Finding Absolute Position of Shape inside the Worksheet with Node.js via C++
linktitle: Finding Absolute Position of Shape inside the Worksheet
type: docs
weight: 8000
url: /nodejs-cpp/finding-absolute-position-of-shape-inside-the-worksheet/
description: Learn how to find the absolute position of a shape inside a worksheet using Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Sometimes, you need to know the absolute position of a shape in a worksheet. Aspose.Cells for Node.js via C++ provides the [**Shape.getLeftToCorner()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getLeftToCorner--) and [**Shape.getTopToCorner()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTopToCorner--) properties for this purpose. These properties return the absolute position of the shape inside the worksheet in pixels.

{{% /alert %}}

The following sample code displays the absolute position of the first shape in the worksheet in pixels. The sample code displays the following console output:

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
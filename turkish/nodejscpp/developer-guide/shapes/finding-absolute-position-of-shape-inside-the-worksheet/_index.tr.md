---
title: Node.js ile C++ kullanarak Çalışma Sayfası İçinde Şeklin Kesin Konumunu Bulma
linktitle: Çalışma sayfasının içindeki Şeklin Mutlak Konumunu Bulma
type: docs
weight: 8000
url: /tr/nodejs-cpp/finding-absolute-position-of-shape-inside-the-worksheet/
description: Aspose.Cells for Node.js via C++ kullanarak bir şeklin çalışma sayfası içindeki kesin konumunu nasıl bulacağınızı öğrenin. 
---

{{% alert color="primary" %}}

Bazen, bir şeklin çalışma sayfasındaki kesin konumunu bilmeniz gerekir. Aspose.Cells for Node.js via C++ bu amaçla [**Shape.getLeftToCorner()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getLeftToCorner--) ve [**Shape.getTopToCorner()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTopToCorner--) özelliklerini sağlar. Bu özellikler, şeklin çalışma sayfası içindeki kesin konumunu piksel cinsinden döner.

{{% /alert %}}

Aşağıdaki örnek kod çalışsayfadaki ilk şeklin mutlak konumunu pikseller cinsinden gösterir. Örnek kod aşağıdaki konsol çıktısını görüntüler:

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

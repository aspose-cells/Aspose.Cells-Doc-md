---
title: Нахождение абсолютной позиции фигуры внутри листа с помощью Node.js через C++
linktitle: Нахождение абсолютной позиции формы внутри Листа книги Excel
type: docs
weight: 8000
url: /ru/nodejs-cpp/finding-absolute-position-of-shape-inside-the-worksheet/
description: Узнайте, как определить абсолютную позицию фигуры внутри листа, используя Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Иногда необходимо знать абсолютную позицию фигуры в листе. Aspose.Cells for Node.js via C++ предоставляет свойства [**Shape.getLeftToCorner()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getLeftToCorner--) и [**Shape.getTopToCorner()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTopToCorner--) для этой цели. Эти свойства возвращают абсолютную позицию фигуры внутри листа в пикселях.

{{% /alert %}}

Следующий образец кода отображает абсолютное положение первой формы на листе в пикселях. Образец кода отображает следующий вывод в консоли:

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

---
title: Node.jsをC++で使用してActiveXコントロールを削除
linktitle: ActiveXコントロールを削除
type: docs
weight: 1000
url: /ja/nodejs-cpp/remove-activex-control/
description: Aspose.Cells for Node.js via C++を使用してワークブックからActiveXコントロールを削除する方法を学びます。
---

## **ActiveXコントロールを削除**

Aspose.Cellsは、ワークブックからActiveXコントロールを削除する機能を提供します。これにはAPIが [**Shape.removeActiveXControl()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#removeActiveXControl--) メソッドを提供します。次のコードスニペットは、ActiveXコントロールを削除するために [**Shape.removeActiveXControl()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#removeActiveXControl--) メソッドの使用例を示しています。

## **サンプルコード**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Create a workbook
const wb = new AsposeCells.Workbook(path.join(sourceDir, "sampleUpdateActiveXComboBoxControl.xlsx"));

// Access first shape from first worksheet
const shape = wb.getWorksheets().get(0).getShapes().get(0);

// Access ActiveX ComboBox Control and update its value
if (shape.getActiveXControl() != null) {
// Remove Shape ActiveX Control
shape.removeActiveXControl();
}

// Save the workbook
wb.save(path.join(outputDir, "RemoveActiveXControl_our.xlsx"));
``` 


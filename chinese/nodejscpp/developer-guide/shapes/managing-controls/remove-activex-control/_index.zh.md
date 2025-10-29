---
title: 通过C++在Node.js中移除ActiveX控件
linktitle: 移除ActiveX控件
type: docs
weight: 1000
url: /zh/nodejs-cpp/remove-activex-control/
description: 学习如何使用Aspose.Cells for Node.js via C++从工作簿中移除ActiveX控件。
---

## **移除ActiveX控件**

Aspose.Cells 提供了从工作簿中移除 ActiveX 控件的功能。为此，API 提供了 [**Shape.removeActiveXControl()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#removeActiveXControl--) 方法。以下代码片段演示了如何使用 [**Shape.removeActiveXControl()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#removeActiveXControl--) 方法移除 ActiveX 控件。

## **示例代码**

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

{{< app/cells/assistant language="nodejs-cpp" >}}

---
title: Remove ActiveX Control with Node.js via C++
linktitle: Remove ActiveX Control
type: docs
weight: 1000
url: /nodejs-cpp/remove-activex-control/
description: Learn how to remove ActiveX controls from workbooks using Aspose.Cells for Node.js via C++.
---

## **Remove ActiveX Control**

Aspose.Cells provides the ability to remove ActiveX Control from workbooks. For this, the API provides the [**Shape.removeActiveXControl()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#removeActiveXControl--) method. The following code snippet demonstrates the use of the [**Shape.removeActiveXControl()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#removeActiveXControl--) method to remove ActiveX Control.

## **Sample Code**

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
 
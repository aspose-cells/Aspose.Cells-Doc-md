---
title: إزالة عنصر تحكم ActiveX باستخدام Node.js عبر C++
linktitle: إزالة عنصر تحكم ActiveX
type: docs
weight: 1000
url: /ar/nodejs-cpp/remove-activex-control/
description: تعلم كيفية إزالة عناصر تحكم ActiveX من دفاتر العمل باستخدام Aspose.Cells for Node.js via C++.
---

## **إزالة عنصر تحكم ActiveX**

توفر Aspose.Cells القدرة على إزالة عنصر تحكم ActiveX من دفاتر العمل. لهذا، يوفر API الطريقة [**Shape.removeActiveXControl()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#removeActiveXControl--). يوضح مقتطف التعليمات البرمجية التالي استخدام طريقة [**Shape.removeActiveXControl()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#removeActiveXControl--) لإزالة عنصر تحكم ActiveX.

## **الكود المثالي**

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


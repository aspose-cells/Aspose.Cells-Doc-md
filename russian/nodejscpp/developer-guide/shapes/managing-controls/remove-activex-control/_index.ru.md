---
title: Удаление элемента ActiveX с помощью Node.js через C++
linktitle: Удалить элемент управления ActiveX
type: docs
weight: 1000
url: /ru/nodejs-cpp/remove-activex-control/
description: Узнайте, как удалять элементы ActiveX из рабочих книг с помощью Aspose.Cells for Node.js via C++.
---

## **Удалить элемент управления ActiveX**

Aspose.Cells предоставляет возможность удалять элементы ActiveX из рабочих книг. Для этого API имеет метод [**Shape.removeActiveXControl()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#removeActiveXControl--). Следующий код демонстрирует использование метода [**Shape.removeActiveXControl()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#removeActiveXControl--) для удаления элемента ActiveX.

## **Образец кода**

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


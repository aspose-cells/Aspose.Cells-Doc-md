---
title: Eliminar control ActiveX con Node.js vía C++
linktitle: Eliminar Control ActiveX
type: docs
weight: 1000
url: /es/nodejs-cpp/remove-activex-control/
description: Aprenda cómo eliminar controles ActiveX de libros de trabajo usando Aspose.Cells for Node.js via C++.
---

## **Eliminar control ActiveX**

Aspose.Cells proporciona la capacidad de eliminar controles ActiveX de libros de trabajo. Para ello, la API ofrece el método [**Shape.removeActiveXControl()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#removeActiveXControl--). El siguiente fragmento de código demuestra el uso del método [**Shape.removeActiveXControl()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#removeActiveXControl--) para eliminar un control ActiveX.

## **Código de muestra**

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


---
title: ActiveX Steuerelement mit Node.js via C++ entfernen
linktitle: AktiveX Steuerung entfernen
type: docs
weight: 1000
url: /de/nodejs-cpp/remove-activex-control/
description: Lernen, wie man ActiveX Steuerelemente aus Arbeitsmappen mit Aspose.Cells for Node.js via C++ entfernt.
---

## **AktiveX-Steuerung entfernen**

Aspose.Cells bietet die Möglichkeit, ActiveX-Steuerelemente aus Arbeitsmappen zu entfernen. Für diese Funktion bietet die API die Methode [**Shape.removeActiveXControl()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#removeActiveXControl--). Das folgende Codebeispiel demonstriert die Verwendung der Methode [**Shape.removeActiveXControl()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#removeActiveXControl--), um ein ActiveX-Steuerelement zu entfernen.

## **Beispielcode**

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


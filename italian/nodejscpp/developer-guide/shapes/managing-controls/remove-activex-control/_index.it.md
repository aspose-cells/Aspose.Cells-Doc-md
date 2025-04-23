---
title: Rimuovi controllo ActiveX con Node.js tramite C++
linktitle: Rimuovi controllo ActiveX
type: docs
weight: 1000
url: /it/nodejs-cpp/remove-activex-control/
description: Impara come rimuovere controlli ActiveX dai workbook usando Aspose.Cells for Node.js via C++.
---

## **Rimuovi controllo ActiveX**

Aspose.Cells fornisce la possibilità di rimuovere il controllo ActiveX dai workbook. Per farlo, l'API offre il metodo [**Shape.removeActiveXControl()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#removeActiveXControl--). Il seguente esempio di codice dimostra l'uso del metodo [**Shape.removeActiveXControl()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#removeActiveXControl--) per rimuovere il controllo ActiveX.

## **Codice di Esempio**

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


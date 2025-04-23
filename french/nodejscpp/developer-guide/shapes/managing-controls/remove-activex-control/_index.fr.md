---
title: Supprimer le contrôle ActiveX avec Node.js via C++
linktitle: Supprimer le contrôle ActiveX
type: docs
weight: 1000
url: /fr/nodejs-cpp/remove-activex-control/
description: Apprenez comment supprimer des contrôles ActiveX des classeurs en utilisant Aspose.Cells for Node.js via C++.
---

## **Supprimer le contrôle ActiveX**

Aspose.Cells offre la possibilité de supprimer un contrôle ActiveX des classeurs. Pour cela, l'API fournit la méthode [**Shape.removeActiveXControl()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#removeActiveXControl--). L'extrait de code suivant démontre l'utilisation de la méthode [**Shape.removeActiveXControl()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#removeActiveXControl--) pour supprimer un contrôle ActiveX.

## **Code d'exemple**

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


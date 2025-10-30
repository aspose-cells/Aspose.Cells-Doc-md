---
title: Ta bort ActiveX kontroll med Node.js via C++
linktitle: Ta bort ActiveX kontroll
type: docs
weight: 1000
url: /sv/nodejs-cpp/remove-activex-control/
description: Lär dig hur du tar bort ActiveX kontroller från arbetsböcker med Aspose.Cells for Node.js via C++.
---

## **Ta bort ActiveX-kontroll**

Aspose.Cells ger möjlighet att ta bort ActiveX-kontroll från arbetsböcker. För detta tillhandahåller API:n [**Shape.removeActiveXControl()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#removeActiveXControl--)-metoden. Följande kodsnutt demonstrerar användningen av [**Shape.removeActiveXControl()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#removeActiveXControl--)-metoden för att ta bort ActiveX-kontroll.

## **Exempelkod**

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

---
title: Lägg till ActiveX kontroller med Aspose.Cells for Node.js via C++
linktitle: Lägg till ActiveX kontroller med hjälp av Aspose.Cells
type: docs
weight: 260
url: /sv/nodejs-cpp/add-activex-controls-using-aspose-cells/
description: Lär dig hur du lägger till ActiveX kontroller i ett kalkylblad med Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Du kan lägga till ActiveX-kontroller med Aspose.Cells med metoden [**ShapeCollection.addActiveXControl(ControlType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addActiveXControl-controltype-number-number-number-number-number-number-). Denna metod tar en parameter [**ControlType**](https://reference.aspose.com/cells/nodejs-cpp/controltype/) som berättar vilken typ av ActiveX-kontroll som ska läggas till i ett kalkylblad. Den har följande värden.

- ControlType.CheckBox
- ControlType.ComboBox
- ControlType.CommandButton
- ControlType.Image
- ControlType.Label
- ControlType.ListBox
- ControlType.RadioButton
- ControlType.ScrollBar
- ControlType.SpinButton
- ControlType.TextBox
- ControlType.ToggleButton
- ControlType.Unknown

När du har lagt till ActiveX-kontrollen i formgruppen kan du sedan komma åt ActiveX-kontrollobjektet via [**Shape.getActiveXControl()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getActiveXControl--) egenskapen och sedan ställa in dess olika egenskaper.

{{% /alert %}}

Följande exempelkod lägger till Toggle-knappen ActiveX-kontroll med hjälp av Aspose.Cells.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const wb = new AsposeCells.Workbook();

// Access first worksheet
const sheet = wb.getWorksheets().get(0);

// Add Toggle Button ActiveX Control inside the Shape Collection
const s = sheet.getShapes().addActiveXControl(AsposeCells.ControlType.ToggleButton, 4, 0, 4, 0, 100, 30);

// Access the ActiveX control object and set its linked cell property
const c = s.getActiveXControl();
c.setLinkedCell("A1");

// Save the workbook in xlsx format
wb.save(path.join(dataDir, "AddActiveXControls_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
{{< app/cells/assistant language="nodejs-cpp" >}}

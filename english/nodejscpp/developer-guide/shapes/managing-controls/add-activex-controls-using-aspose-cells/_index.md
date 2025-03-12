---
title: Add ActiveX Controls using Aspose.Cells for Node.js via C++
linktitle: Add ActiveX Controls using Aspose.Cells
type: docs
weight: 260
url: /nodejs-cpp/add-activex-controls-using-aspose-cells/
description: Learn how to add ActiveX controls in a worksheet using Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

You can add ActiveX controls with Aspose.Cells using the [**ShapeCollection.addActiveXControl(ControlType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addActiveXControl-controltype-number-number-number-number-number-number-) method. This method takes a parameter [**ControlType**](https://reference.aspose.com/cells/nodejs-cpp/controltype/) which tells what type of ActiveX control needs to be added inside a worksheet. It has the following values.

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

Once you have added the ActiveX control inside the shape collection, you can then access the ActiveX control object via [**Shape.getActiveXControl()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getActiveXControl--) property and then set its various properties.

{{% /alert %}}

The following sample code adds Toggle Button ActiveX Control using Aspose.Cells.

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

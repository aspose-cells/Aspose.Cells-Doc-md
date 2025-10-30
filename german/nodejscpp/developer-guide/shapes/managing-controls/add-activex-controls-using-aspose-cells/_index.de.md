---
title: ActiveX Steuerelemente mithilfe von Aspose.Cells for Node.js via C++ hinzufügen
linktitle: AktiveX Steuerelemente mit Aspose.Cells hinzufügen
type: docs
weight: 260
url: /de/nodejs-cpp/add-activex-controls-using-aspose-cells/
description: Lernen, wie man ActiveX Steuerelemente in einem Arbeitsblatt mit Aspose.Cells for Node.js via C++ hinzufügt. 
---

{{% alert color="primary" %}}

Sie können ActiveX-Steuerelemente mit Aspose.Cells mit der Methode [**ShapeCollection.addActiveXControl(ControlType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addActiveXControl-controltype-number-number-number-number-number-number-) hinzufügen. Diese Methode nimmt einen Parameter [**ControlType**](https://reference.aspose.com/cells/nodejs-cpp/controltype/), der angibt, welchen Typ von ActiveX-Steuerelement in einem Arbeitsblatt hinzugefügt werden soll. Sie hat folgende Werte.

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

Nachdem Sie das ActiveX-Steuerelement im Shape-Container hinzugefügt haben, können Sie dann auf das ActiveX-Steuerelement-Objekt über die Eigenschaft [**Shape.getActiveXControl()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getActiveXControl--) zugreifen und seine verschiedenen Eigenschaften einstellen.

{{% /alert %}}

Der folgende Beispielcode fügt eine Umschaltfläche für ActiveX-Steuerungen mithilfe von Aspose.Cells hinzu.

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

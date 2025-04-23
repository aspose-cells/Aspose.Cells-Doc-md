---
title: Agregar controles ActiveX usando Aspose.Cells for Node.js via C++
linktitle: Agregar controles ActiveX usando Aspose.Cells
type: docs
weight: 260
url: /es/nodejs-cpp/add-activex-controls-using-aspose-cells/
description: Aprenda cómo agregar controles ActiveX en una hoja de cálculo usando Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Puede agregar controles ActiveX con Aspose.Cells usando el método [**ShapeCollection.addActiveXControl(ControlType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addActiveXControl-controltype-number-number-number-number-number-number-). Este método toma un parámetro [**ControlType**](https://reference.aspose.com/cells/nodejs-cpp/controltype/) que indica qué tipo de control ActiveX debe agregarse dentro de una hoja. Tiene los siguientes valores.

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

Una vez que haya agregado el control ActiveX dentro de la colección de formas, puede acceder al objeto control ActiveX a través de la propiedad [**Shape.getActiveXControl()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getActiveXControl--) y luego establecer sus varias propiedades.

{{% /alert %}}

El siguiente código de ejemplo agrega el control de botón de alternancia ActiveX utilizando Aspose.Cells.

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

---
title: Aggiungi controlli ActiveX usando Aspose.Cells for Node.js via C++
linktitle: Aggiungi controlli ActiveX usando Aspose.Cells
type: docs
weight: 260
url: /it/nodejs-cpp/add-activex-controls-using-aspose-cells/
description: Impara come aggiungere controlli ActiveX in un foglio di lavoro usando Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Puoi aggiungere controlli ActiveX con Aspose.Cells usando il metodo [**ShapeCollection.addActiveXControl(ControlType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addActiveXControl-controltype-number-number-number-number-number-number-). Questo metodo prende un parametro [**ControlType**](https://reference.aspose.com/cells/nodejs-cpp/controltype/) che indica quale tipo di controllo ActiveX deve essere aggiunto all'interno di un foglio di lavoro. I valori sono i seguenti.

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

Una volta aggiunto il controllo ActiveX all'interno della raccolta shape, puoi quindi accedere all'oggetto controllo ActiveX tramite la proprietà [**Shape.getActiveXControl()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getActiveXControl--) e impostarne le varie proprietà.

{{% /alert %}}

Il seguente codice di esempio aggiunge il pulsante di controllo ActiveX utilizzando Aspose.Cells.

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

---
title: Ajouter des contrôles ActiveX en utilisant Aspose.Cells for Node.js via C++
linktitle: Ajouter des contrôles ActiveX à l aide d Aspose.Cells
type: docs
weight: 260
url: /fr/nodejs-cpp/add-activex-controls-using-aspose-cells/
description: Apprenez comment ajouter des contrôles ActiveX dans une feuille de calcul en utilisant Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Vous pouvez ajouter des contrôles ActiveX avec Aspose.Cells en utilisant la méthode [**ShapeCollection.addActiveXControl(ControlType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addActiveXControl-controltype-number-number-number-number-number-number-). Cette méthode prend un paramètre [**ControlType**](https://reference.aspose.com/cells/nodejs-cpp/controltype/) qui indique quel type de contrôle ActiveX doit être ajouté dans une feuille de calcul. Elle a les valeurs suivantes.

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

Une fois que vous avez ajouté le contrôle ActiveX dans la collection de formes, vous pouvez accéder à l'objet contrôle ActiveX via la propriété [**Shape.getActiveXControl()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getActiveXControl--) puis définir ses diverses propriétés.

{{% /alert %}}

Le code d'exemple suivant ajoute le contrôle ActiveX du bouton bascule à l'aide d'Aspose.Cells.

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

---
title: Добавьте элементы ActiveX с помощью Aspose.Cells for Node.js via C++
linktitle: Добавление элементов ActiveX с помощью Aspose.Cells
type: docs
weight: 260
url: /ru/nodejs-cpp/add-activex-controls-using-aspose-cells/
description: Узнайте, как добавлять элементы ActiveX в лист с помощью Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Вы можете добавлять элементы ActiveX с Aspose.Cells, используя метод [**ShapeCollection.addActiveXControl(ControlType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addActiveXControl-controltype-number-number-number-number-number-number-). Этот метод принимает параметр [**ControlType**](https://reference.aspose.com/cells/nodejs-cpp/controltype/), который определяет тип элемента ActiveX, который необходимо добавить в лист. Он имеет следующие значения.

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

После добавления элемента ActiveX в коллекцию фигур, вы можете получить доступ к объекту ActiveX через свойство [**Shape.getActiveXControl()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getActiveXControl--), а затем установить его свойства.

{{% /alert %}}

В следующем примере кода добавляется элемент Управления переключением с помощью элемента ActiveX Toggle Button, используя Aspose.Cells.

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

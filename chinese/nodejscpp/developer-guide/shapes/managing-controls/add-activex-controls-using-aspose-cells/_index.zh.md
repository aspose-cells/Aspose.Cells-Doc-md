---
title: 使用Aspose.Cells for Node.js via C++添加ActiveX控件
linktitle: 使用 Aspose.Cells 添加 ActiveX 控件
type: docs
weight: 260
url: /zh/nodejs-cpp/add-activex-controls-using-aspose-cells/
description: 学习如何在工作表中使用Aspose.Cells for Node.js via C++添加ActiveX控件。 
---

{{% alert color="primary" %}}

可以使用[**ShapeCollection.addActiveXControl(ControlType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addActiveXControl-controltype-number-number-number-number-number-number-)方法添加ActiveX控件。该方法接受参数[**ControlType**](https://reference.aspose.com/cells/nodejs-cpp/controltype/)，告诉需要在工作表中添加哪种类型的ActiveX控件，具体取值如下。

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

将ActiveX控件添加到形状集合中后，可以通过[**Shape.getActiveXControl()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getActiveXControl--)属性访问ActiveX控件对象，然后设置其各种属性。

{{% /alert %}}

以下示例代码使用 Aspose.Cells 添加 Toggle Button ActiveX 控件。

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

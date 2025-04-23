---
title: إضافة عناصر تحكم ActiveX باستخدام Aspose.Cells for Node.js via C++
linktitle: إضافة عناصر التحكم ActiveX باستخدام Aspose.Cells
type: docs
weight: 260
url: /ar/nodejs-cpp/add-activex-controls-using-aspose-cells/
description: تعلم كيفية إضافة عناصر تحكم ActiveX في ورقة عمل باستخدام Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

يمكنك إضافة عناصر تحكم ActiveX باستخدام Aspose.Cells باستخدام طريقة [**ShapeCollection.addActiveXControl(ControlType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addActiveXControl-controltype-number-number-number-number-number-number-). تأخذ هذه الطريقة معلمة [**ControlType**](https://reference.aspose.com/cells/nodejs-cpp/controltype/) التي تخبر عن نوع عنصر تحكم ActiveX الذي يحتاج إلى إضافته داخل ورقة العمل. لديها القيم التالية.

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

بمجرد إضافة عنصر تحكم ActiveX داخل مجموعة الأشكال، يمكنك الوصول إلى كائن عنصر التحكم ActiveX عبر الخاصية [**Shape.getActiveXControl()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getActiveXControl--) ثم تعيين خصائصه المختلفة.

{{% /alert %}}

يقومالكودالمصدرالتاليبإضافةزرتبديلتحكمActiveXباستخدامAspose.Cells.

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

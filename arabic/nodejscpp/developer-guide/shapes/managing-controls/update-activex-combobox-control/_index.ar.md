---
title: تحديث عنصر تحكم ComboBox الخاص بـ ActiveX باستخدام Node.js عبر C++
linktitle: تحديث عنصر التحكم ActiveX ComboBox
type: docs
weight: 170
url: /ar/nodejs-cpp/update-activex-combobox-control/
description: تعلم كيفية قراءة وكتابة قيم عنصر تحكم ComboBox الخاص بـ ActiveX باستخدام Aspose.Cells for Node.js via C++. 
---

## **سيناريوهات الاستخدام المحتملة**
يمكنك قراءة أو كتابة قيم عنصر تحكم ComboBox الخاص بـ ActiveX باستخدام Aspose.Cells for Node.js via C++. يرجى الوصول إلى عنصر التحكم ActiveX عبر الخاصية [Shape.getActiveXControl()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getActiveXControl--) والتحقق من نوعه عبر [ActiveXControlBase.getType()](https://reference.aspose.com/cells/nodejs-cpp/activexcontrolbase/#getType--)، والتي يجب أن تُرجع قيمة [ControlType.ComboBox](https://reference.aspose.com/cells/nodejs-cpp/controltype/)، ثم تحويل نوعه إلى كائن [ComboBoxActiveXControl](https://reference.aspose.com/cells/nodejs-cpp/comboboxactivexcontrol/) وقراءة أو تعديل خصائصه المختلفة.

يرجىتنزيل[ملف الإكسل العيني](5115124.xlsx) المستخدمفيالكود العينيالتالي.
## **تحديث عنصر تحكم ActiveX ComboBox**
الصورة التي تلي تظهر تأثير كود العينة على [ملف الإكسل عينة](5115124.xlsx). كما يمكنك رؤية أن قيمة عنصر التحكم ComboBox في ActiveX تم تحديثها إلى "هذا عنصر التحكم في مربع القائمة"

|![todo:image_alt_text](update-activex-combobox-control_1.png)|
| :- |
## **الكود المثالي**
تحديث قيمة عنصر التحكم في مربع القائمة ActiveX داخل [ملف الإكسل عينة](5115124.xlsx).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SourceFile_activex.xlsx");
// Create a workbook
const wb = new AsposeCells.Workbook(filePath);

// Access first shape from first worksheet
const shape = wb.getWorksheets().get(0).getShapes().get(0);

// Access ActiveX ComboBox Control and update its value
if (shape.getActiveXControl() != null)
{
// Access Shape ActiveX Control
const c = shape.getActiveXControl();

if (c instanceof AsposeCells.ComboBoxActiveXControl)
{
// Type cast ActiveXControl into ComboBoxActiveXControl and change its value
const comboBoxActiveX = new AsposeCells.ComboBoxActiveXControl(c);
comboBoxActiveX.setValue("This is combo box control with updated value.");

}

}

// Save the workbook
const outputFilePath = path.join(dataDir, "OutputFile_out.xlsx");
wb.save(outputFilePath);
```

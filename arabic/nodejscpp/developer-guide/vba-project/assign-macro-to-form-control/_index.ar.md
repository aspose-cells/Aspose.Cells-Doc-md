---
title: تعيين ماكرو إلى عنصر تحكم النموذج باستخدام Node.js عبر C++
linktitle: تعيين ماكرو إلى عنصر تحكم النموذج
type: docs
weight: 60
url: /ar/nodejs-cpp/assign-macro-to-form-control/
description: تعلم كيفية تعيين رمز الماكرو لعنصر تحكم النموذج مثل زر باستخدام Aspose.Cells for Node.js via C++. 
keywords: تعيين الماكرو إلى عنصر تحكم النموذج Node.js عبر C++، رمز الماكرو لعنصر تحكم النموذج عبر Node.js باستخدام C++، الماكرو المدمج في XLSM عبر Node.js باستخدام C++
---

{{% alert color="primary" %}}

تسمح Aspose.Cells لك بتعيين شيفر آلي إلى عنصر تحكم النموذج مثل زر. يرجى استخدام الخاصية [**Shape.getMacroName()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getMacroName--) لتعيين شيفر آلي جديد إلى عنصر تحكم النموذج داخل سجل العمل.

{{% /alert %}}

الكود النموذجي التالي ينشئ دفتر عمل جديد، يعين رمز الماكرو لزر النموذج، ويحفظ الناتج بتنسيق XLSM. عند فتح ملف XLSM الناتج في Microsoft Excel، ستشاهد رمز الماكرو التالي.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **تعيين الماكرو لعنصر تحكم النموذج في Node.js**

إليك رمز العينة لإنشاء ملف XLSM الناتج مع رمز الماكرو.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().get(0);

const moduleIdx = workbook.getVbaProject().getModules().add(sheet);
const module = workbook.getVbaProject().getModules().get(moduleIdx);
module.setCodes(
"Sub ShowMessage()" + "\r\n" +
"    MsgBox \"Welcome to Aspose!\"" + "\r\n" +
"End Sub"
);

const button = sheet.getShapes().addButton(2, 0, 2, 0, 28, 80);
button.setPlacement(AsposeCells.PlacementType.FreeFloating);
button.getFont().setName("Tahoma");
button.getFont().setIsBold(true);
button.getFont().setColor(AsposeCells.Color.Blue);
button.setText("Aspose");

button.setMacroName(sheet.getName() + ".ShowMessage");

const outputFilePath = path.join(dataDir, "Output.out.xlsm");
workbook.save(outputFilePath);
```
{{< app/cells/assistant language="nodejs-cpp" >}}

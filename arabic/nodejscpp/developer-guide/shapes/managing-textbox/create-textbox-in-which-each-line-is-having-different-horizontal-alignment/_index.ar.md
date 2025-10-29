---
title: إنشاء مربع نص حيث يحتوي كل سطر على محاذاة أفقية مختلفة باستخدام Node.js عبر C++
linktitle: إنشاء مربع نص يحتوي كل سطر على محاذاة أفقية مختلفة
type: docs
weight: 310
url: /ar/nodejs-cpp/create-textbox-in-which-each-line-is-having-different-horizontal-alignment/
description: تعلم كيفية إنشاء مربع نص يمكن لكل سطر أن يحتوي على محاذاة أفقية مختلفة باستخدام Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}
يمكنك تحديد محاذاة النص الأفقية لنص فقرتك باستخدام خاصية [**TextParagraph.getAlignmentType()**](https://reference.aspose.com/cells/nodejs-cpp/textparagraph/#getAlignmentType--).
{{% /alert %}}

الكود النموذجي التالي ينشئ ثلاثة أسطر ويحدد محاذاة كل منها.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a workbook.
const wb = new AsposeCells.Workbook();

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Add text box inside the sheet.
ws.getShapes().addTextBox(2, 0, 2, 0, 80, 400);

// Access first shape which is a text box and set its text.
const shape = ws.getShapes().get(0);
shape.setText("Sign up for your free phone number.\nCall and text online for free.\nCall your friends and family.");

// Access the first paragraph and set its horizontal alignment to left.
let p = shape.getTextBody().getTextParagraphs().get(0);
p.setAlignmentType(AsposeCells.TextAlignmentType.Left);

// Access the second paragraph and set its horizontal alignment to center.
p = shape.getTextBody().getTextParagraphs().get(1);
p.setAlignmentType(AsposeCells.TextAlignmentType.Center);

// Access the third paragraph and set its horizontal alignment to right.
p = shape.getTextBody().getTextParagraphs().get(2);
p.setAlignmentType(AsposeCells.TextAlignmentType.Right);

// Save the workbook in xlsx format.
wb.save(path.join(dataDir, "output_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
{{< app/cells/assistant language="nodejs-cpp" >}}

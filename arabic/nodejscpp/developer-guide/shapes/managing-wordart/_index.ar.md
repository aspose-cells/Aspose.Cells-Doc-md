---
title: أضف علامة مائية WordArt إلى ورقة العمل باستخدام Node.js عبر C++
linktitle: إدارة كلمة اللهن
type: docs
weight: 180
url: /ar/nodejs-cpp/add-wordart-watermark-to-worksheet/
description: تعلم كيفية إضافة WordArt كعلامة مائية خلفية إلى ورقة العمل باستخدام Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}} 

استخدام كلمة الفن لإضافة تأثيرات نص خاصة إلى جداول البيانات، على سبيل المثال، تمدد عنوان عبر الجزء العلوي من الملف، زينة النص، وجعل النص يتناسب مع شكل محدد مسبقًا، أو تطبيق النص إلى ورقة Excel كعلامة مائية خلفية. تصبح كلمة الفن كائنًا يمكنك نقله أو تحديد موقعه في جداول البيانات لإضافة زخرفة.

{{% /alert %}} 

المثال التالي يوضح كيفية إضافة شكل WordArt لتعيين علامة مائية في الخلفية لورقة العمل.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook
const workbook = new AsposeCells.Workbook();

// Get the first default sheet
const sheet = workbook.getWorksheets().get(0);

// Add Watermark
const wordart = sheet.getShapes().addTextEffect(AsposeCells.MsoPresetTextEffect.TextEffect1,
"CONFIDENTIAL", "Arial Black", 50, false, true, 18, 8, 1, 1, 130, 800);

// Get the fill format of the word art
const wordArtFormat = wordart.getFill();            

// Set the transparency
wordArtFormat.setTransparency(0.9);

// Make the line invisible
const lineFormat = wordart.getLine();          

const outputFilePath = path.join(dataDir, "Watermark_Test.out.xls");
// Save the file
workbook.save(outputFilePath);
```

## **مواضيع متقدمة**
- [إضافة نص Word Art بأنماط مدمجة](/cells/ar/nodejs-cpp/add-word-art-text-with-built-in-styles/)
- [تأمين علامة مائية WordArt](/cells/ar/nodejs-cpp/locking-wordart-watermark/)
- [تعيين نمط WordArt المحدد مسبقًا لنص الشكل](/cells/ar/nodejs-cpp/set-preset-wordart-style-to-the-text-of-the-shape/)

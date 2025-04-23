---
title: أضف نص الفن الكلمة باستخدام أنماط مدمجة باستخدام Node.js عبر C++
linktitle: إضافة نص فني بأنماط مضمنة
type: docs
weight: 270
url: /ar/nodejs-cpp/add-word-art-text-with-built-in-styles/
description: تعلم كيف تضيف نص الفن الكلمة باستخدام Aspose.Cells for Node.js via C++. أنشئ نصًا جذابًا بصريًا في Excel باستخدام الأنماط المدمجة.
---

## **سيناريوهات الاستخدام المحتملة**
يمكنك إضافة نص الفن الكلمة باستخدام الأنماط المدمجة باستخدام Aspose.Cells for Node.js via C++. يرجى استخدام الطريقة [ShapeCollection.addWordArt()](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addWordArt-presetwordartstyle-string-number-number-number-number-number-number-) لهذا الغرض.

## **إضافة نص Word Art بأنماط مدمجة**
يقوم الكود النموذجي التالي بإضافة نصوص فنية بأنماط مدمجة مختلفة. يُرجى التحقق من [ملف الإكسل الناتج](5115470.xlsx) الذي تم إنشاؤه بهذا الكود. هكذا يبدو [ملف الإكسل الناتج](5115470.xlsx) في Microsoft Excel.

![todo:image_alt_text](add-word-art-text-with-built-in-styles_1.png)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Add Word Art Text with Built-in Styles
ws.getShapes().addWordArt(AsposeCells.PresetWordArtStyle.WordArtStyle1, "Aspose File Format APIs", 0, 0, 0, 0, 100, 800);
ws.getShapes().addWordArt(AsposeCells.PresetWordArtStyle.WordArtStyle2, "Aspose File Format APIs", 10, 0, 0, 0, 100, 800);
ws.getShapes().addWordArt(AsposeCells.PresetWordArtStyle.WordArtStyle3, "Aspose File Format APIs", 20, 0, 0, 0, 100, 800);
ws.getShapes().addWordArt(AsposeCells.PresetWordArtStyle.WordArtStyle4, "Aspose File Format APIs", 30, 0, 0, 0, 100, 800);
ws.getShapes().addWordArt(AsposeCells.PresetWordArtStyle.WordArtStyle5, "Aspose File Format APIs", 40, 0, 0, 0, 100, 800);

// Save the workbook in xlsx format
wb.save(path.join(dataDir, "output_out.xlsx"));
```

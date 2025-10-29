---
title: استخراج النص من شكل فن ذكي من نوع Gear باستخدام Node.js عبر C++
linktitle: استخراج النص من شكل SmartArt نوع الحركة
type: docs
weight: 500
url: /ar/nodejs-cpp/extract-text-from-the-gear-type-smartart-shape/
description: تعلم كيفية استخراج النص من شكل فن ذكي من نوع Gear باستخدام Aspose.Cells for Node.js via C++.
---

## **سيناريوهات الاستخدام المحتملة**

يمكن لـ Aspose.Cells استخراج النص من شكل فن ذكي من نوع Gear. للقيام بذلك، يجب أولاً تحويل شكل الفن الذكي إلى شكل جماعي باستخدام طريقة [**Shape.getResultOfSmartArt()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getResultOfSmartArt--). ثم يجب الحصول على مصفوفة كل الأشكال الفردية التي تكون ضمن الشكل الجماعي باستخدام طريقة [**GroupShape.getGroupedShapes()**](https://reference.aspose.com/cells/nodejs-cpp/groupshape/#getGroupedShapes--). أخيراً، يمكنك التكرار عبر جميع الأشكال الفردية واحدًا تلو الآخر في حلقة واستخراج نصها باستخدام الخاصية [**Shape.getText()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getText--).

## **استخراج النص من شكل SmartArt نوع الحركة**

يحمل الكود العيني التالي [ملف Excel العيني](67338483.xlsx) الذي يحتوي على شكل Smart Art Shape من نوع العتاد. ثم يستخرج النص من الأشكال الفردية له كما هو موضح أعلاه. يرجى الاطلاع على مخرجات الوحدة المعطاة أدناه كمرجع.

## **الكود المثالي**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleExtractTextFromGearTypeSmartArtShape.xlsx");

// Load sample Excel file containing gear type smart art shape.
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Access first shape.
const shape = worksheet.getShapes().get(0);

// Get the result of gear type smart art shape in the form of group shape.
const groupShape = shape.getResultOfSmartArt();

// Get the list of individual shapes consisting of group shape.
const shapes = groupShape.getGroupedShapes();

// Extract the text of gear type shapes and print them on console.
for (let i = 0; i < shapes.length; i++) {
const s = shapes[i];

if (s.getType() === AsposeCells.AutoShapeType.Gear9 || s.getType() === AsposeCells.AutoShapeType.Gear6) {
console.log("Gear Type Shape Text: " + s.getText());
}
}
```

## **مخرجات الوحدة**

{{< highlight javascript >}}

Gear Type Shape Text: Nice

Gear Type Shape Text: Good

Gear Type Shape Text: Excellent

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}

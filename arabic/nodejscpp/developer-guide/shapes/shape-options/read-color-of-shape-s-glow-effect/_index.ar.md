---
title: قراءة لون تأثير التوهج للشكل باستخدام Node.js عبر C++
linktitle: قراءة لون تأثير إضاءة الشكل
type: docs
weight: 330
url: /ar/nodejs-cpp/read-color-of-shape-s-glow-effect/
description: تعلم كيفية قراءة لون تأثير التوهج لشكل باستخدام Aspose.Cells for Node.js via C++. 
---

## سيناريوات الاستخدام المحتملة

 إذا كنت تريد قراءة لون تأثير التوهج لأي شكل، يرجى استخدام خاصية [**Shape.getColor()**](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/#getColor--). ستساعدك على العثور على الخصائص المختلفة المتعلقة بلون تأثير التوهج للشكل.

## قراءة لون تأثير الإضاءة للشكل

يرجى الاطلاع على الكود النموذجي التالي و[ملف الإكسل الأصلي](22774108.xlsx) وإخراج الكونسول للرجوع إلى. تظهر اللقطة الشاشة التالية تأثير الاضاءة للشكل داخل ملف الإكسل الأصلي عند عرضه في Microsoft Excel.

![todo:image_alt_text](read-color-of-shape-s-glow-effect_1.png)

## كود Node.js لقراءة لون تأثير التوهج للشكل

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Read the source excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sourceGlowEffectColor.xlsx"));

// Access the first worksheet
const sheet = workbook.getWorksheets().get(0);

// Access the shape
const shape = sheet.getShapes().get(0);

// Read the glow effect color and its various properties
const effect = shape.getGlow();
const color = effect.getColor();
console.log("Color: " + color.getColor());
console.log("ColorIndex: " + color.getColorIndex());
console.log("IsShapeColor: " + color.isShapeColor());
console.log("Transparency: " + color.getTransparency());
console.log("Type: " + color.getType());
```

## مخرج الكونسول

إليك إخراج الكونسول للرمز النموذجي أعلاه عند تنفيذه مع [ملف الإكسل الأصلي](22774108.xlsx) المقدم.

{{< highlight javascript >}}

Color: Color [A=222, R=255, G=0, B=0]

ColorIndex: 16711672

IsShapeColor: True

Transparency: 0.13

Type: RGB

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}

---
title: العمل مع تأثير الانعكاس للشكل أو المخطط مع Node.js عبر C++
linktitle: العمل مع تأثير الانعكاس الداخلي للشكل أو الرسم البياني
type: docs
weight: 210
url: /ar/nodejs-cpp/working-with-the-reflection-effect-of-shape-or-chart/
description: تعلم كيفية العمل مع تأثير الانعكاس للأشكال أو المخططات باستخدام Aspose.Cells for Node.js via C++. قم بضبط خصائص الانعكاس المختلفة لتحقيق النتائج المرغوبة.
---

## **سيناريوهات الاستخدام المحتملة**
يوفر Aspose.Cells for Node.js via C++ الخاصية [Shape.getReflection()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getReflection--) بالإضافة إلى فئة [ReflectionEffect](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect) للعمل مع تأثير الانعكاس للشكل أو المخطط. تحتوي فئة [ReflectionEffect](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect) على الخصائص التالية والتي يمكن ضبطها لتحقيق نتائج مختلفة حسب متطلبات التطبيق.

- [ReflectionEffect.getBlur()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getBlur--)
- [ReflectionEffect.getDirection()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getDirection--)
- [ReflectionEffect.getDistance()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getDistance--)
- [ReflectionEffect.getFadeDirection()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getFadeDirection--)
- [ReflectionEffect.getRotWithShape()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getRotWithShape--)
- [ReflectionEffect.getSize()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getSize--)
- [ReflectionEffect.getTransparency()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getTransparency--)
- [ReflectionEffect.getType()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getType--)

## **العمل مع تأثير الانعكاس للشكل أو الرسم البياني**
يقوم الرمز النموذجي التالي بتحميل ملف إكسل المصدر (5115424.xlsx) والوصول إلى الشكل الأول في ورقة العمل الافتراضية. يضبط خصائص مختلفة من فئة [Shape.getReflection()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getReflection--) ثم يحفظ دفتر العمل في ملف إكسل الإخراج (5115423.xlsx).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first shape
const shape = worksheet.getShapes().get(0);

// Set the reflection effect of the shape, set its Blur, Size, Transparency and Distance properties
const reflectionEffect = shape.getReflection();
reflectionEffect.setBlur(30);
reflectionEffect.setSize(90);
reflectionEffect.setTransparency(0);
reflectionEffect.setDistance(80);

// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "output_out.xlsx"));
```

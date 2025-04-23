---
title: تحويل الشكل الذكي إلى شكل جماعي باستخدام Node.js عبر C++
linktitle: تحويل الرسوم البيانية الذكية إلى شكل مجموعة
type: docs
weight: 200
url: /ar/nodejs-cpp/convert-the-smart-art-to-group-shape/
---

## **سيناريوهات الاستخدام المحتملة**

يمكنك تحويل شكل الفن الذكي إلى شكل جماعي باستخدام طريقة [**Shape.getResultOfSmartArt()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getResultOfSmartArt--). ستتمكن من التعامل مع شكل الفن الذكي ككائن مجموعة. بالتالي، سيكون لديك الوصول إلى الأجزاء أو الأشكال الفردية الخاصة بمجموعة الأشكال.

## **تحويل الرسوم البيانية الذكية إلى شكل مجموعة**

الرمز المساعد التالي يقوم بتحميل ملف إكسل (sample.xlsx) يحتوي على شكل فن ذكي كما هو موضح في هذه الصورة. ثم يتم تحويل شكل الفن الذكي إلى شكل جماعي ويطبع خاصية Shape.isGroup. يرجى الاطلاع على ناتج الكونسول للرمز المساعد المقدم أدناه.

![todo:image_alt_text](convert-the-smart-art-to-group-shape_1.png)

## **الكود المثالي**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Load the sample smart art shape - Excel file
const filePath = path.join(__dirname, "data", "sampleSmartArtShape_GetResultOfSmartArt.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first shape
const shape = worksheet.getShapes().get(0);

// Determine if shape is smart art
console.log("Is Smart Art Shape: " + shape.isSmartArt());

// Determine if shape is group shape
console.log("Is Group Shape: " + shape.isGroup());

// Convert smart art shape into group shape
console.log("Is Group Shape: " + shape.getResultOfSmartArt().isGroup());
```

## **مخرجات الوحدة**

{{< highlight javascript >}}

Is Smart Art Shape: True

Is Group Shape: False

Is Group Shape: True

{{< /highlight >}}

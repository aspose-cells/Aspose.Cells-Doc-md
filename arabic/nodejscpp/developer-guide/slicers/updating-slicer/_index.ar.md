---
title: تحديث المقسم باستخدام Node.js عبر C++
linktitle: تحديث المقسم
type: docs
weight: 50
url: /ar/nodejs-cpp/updating-slicer/
description: يوضح هذا المقال كيفية تحديث الجداول المحورية المرتبطة من خلال تحديث المقسم باستخدام Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells Node.js عبر C++، تحديث المقسم Node.js، كيفية تغيير المقسم Node.js، كيفية ضبط المقسم في Node.js، كيفية اختيار أو إلغاء اختيار عناصر المقسم Node.js عبر C++.
---

## **سيناريوهات الاستخدام المحتملة**

 إذا كنت تريد تحديث مقسم في Microsoft Excel، قم باختيار أو إلغاء اختيار عناصره، وسيتحدث المقسم وفقًا لذلك. يرجى استخدام [**Slicer.getSlicerCacheItems()**](https://reference.aspose.com/cells/nodejs-cpp/slicercache/#getSlicerCacheItems--) لاختيار أو إلغاء اختيار عناصر المقسم مع Aspose.Cells ثم استدعاء [**Slicer.refresh()**](https://reference.aspose.com/cells/nodejs-cpp/slicer/#refresh--) لتحديث جدول المقسم أو الجدول المحوري.

## **كيفية تحديث العارض**

يحمل الكود العيني التالي الملف اكسل العيني الذي يحتوي على عارض موجود. يلغي تحديد العناصر الثانية والثالثة من العارض ويحدث العارض. ثم يحفظ الدفتر كملف أكسل بإسم ملف الأكسل العيني الناتج. تظهر الصورة العينية التالية تأثير الكود العيني على ملف الأكسل العيني العيني. كما ترون في الصورة العينية، تم تحديث العارض بالعناصر المحددة وكذلك تم تحديث الجدول المحوري وفقًا لذلك.

![todo:image_alt_text](updating-slicer_1.png)

## **الكود المثالي**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleUpdatingSlicer.xlsx");
// Load sample Excel file containing slicer.
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Access the first slicer inside the slicer collection.
const slicer = ws.getSlicers().get(0);

// Access the slicer items.
const scItems = slicer.getSlicerCache().getSlicerCacheItems();

const items = slicer.getSlicerCache().getSlicerCacheItems();

for (let i = 0; i < items.getCount(); i++) {
const item = items.get(i);
if (item.getValue() === "Pink" || item.getValue() === "Green") {
item.setSelected(false);
}
}
slicer.refresh();
wb.save("out.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}

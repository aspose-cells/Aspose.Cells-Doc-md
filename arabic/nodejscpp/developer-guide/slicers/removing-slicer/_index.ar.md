---
title: إزالة المقسم باستخدام Node.js عبر C++
linktitle: إزالة قالب التصفية
type: docs
weight: 30
url: /ar/nodejs-cpp/removing-slicer/
---

## **سيناريوهات الاستخدام المحتملة**

 إذا كنت تريد إزالة مقسم في Excel، فقط حدد المقسم واضغط على زر *حذف*. بالمثل، إذا كنت تريد إزالته باستخدام API الخاص بـ Aspose.Cells برمجيًا، يرجى استخدام [**SlicerCollection.remove(Slicer)**](https://reference.aspose.com/cells/nodejs-cpp/slicercollection/#remove-slicer-). وسيتم إزالة المقسم من الورقة.

## **إزالة قالب التصفية**

 الكود النموذجي التالي يحمل [ملف Excel النموذجي](67338478.xlsx) الذي يحتوي على مقسم موجود. يصل إلى المقسم ثم يزيله. أخيرًا، يحفظ المصنف كـ [ملف Excel المخرجي](67338477.xlsx). تبرز الصورة التالية المقسم الذي سيتم إزالته بعد تنفيذ الكود النموذجي.

![todo:image_alt_text](removing-slicer_1.png)

## **الكود المثالي**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleRemovingSlicer.xlsx");

// Load sample Excel file containing slicer.
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Access the first slicer inside the slicer collection.
const slicer = worksheet.getSlicers().get(0);

// Remove slicer.
worksheet.getSlicers().remove(slicer);

// Save the workbook in output XLSX format.
workbook.save("outputRemovingSlicer.xlsx", AsposeCells.SaveFormat.Xlsx);
```
{{< app/cells/assistant language="nodejs-cpp" >}}

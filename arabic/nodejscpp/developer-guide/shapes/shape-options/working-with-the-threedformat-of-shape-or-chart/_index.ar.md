---
title: العمل مع شكل أو مخطط ثلاثي الأبعاد مع Node.js عبر C++
linktitle: العمل مع ثلاثة الأبعاد من الشكل أو الرسم البياني
type: docs
weight: 250
url: /ar/nodejs-cpp/working-with-the-threedformat-of-shape-or-chart/
---

## **سيناريوهات الاستخدام المحتملة**
يوفر Aspose.Cells for Node.js via C++ الخاصية [Shape.getThreeDFormat()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getThreeDFormat--) بالإضافة إلى فئة [ThreeDFormat](https://reference.aspose.com/cells/nodejs-cpp/threedformat) للعمل مع تنسيق 3D للشكل أو المخطط. تحتوي فئة [ThreeDFormat](https://reference.aspose.com/cells/nodejs-cpp/threedformat) على خصائص مختلفة يمكن ضبطها لتحقيق نتائج مختلفة حسب متطلبات التطبيق.

## **العمل مع ثلاثة الأبعاد من الشكل أو الرسم البياني**
يعتمد الرمز النموذجي التالي على تحميل ملف إكسل المصدر (5115419.xlsx) والوصول إلى الشكل الأول في ورقة العمل الأولى وضبط الخصائص الفرعية من الخاصية [Shape.getThreeDFormat()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getThreeDFormat--) ثم يحفظ دفتر العمل في ملف إكسل الإخراج (5115410.xlsx).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load excel file containing a shape
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access first shape
const sh = ws.getShapes().get(0);

// Apply different three dimensional settings
const n3df = sh.getThreeDFormat();
n3df.setContourWidth(17);
n3df.setExtrusionHeight(32);

// Save the output excel file in xlsx format
wb.save(path.join(dataDir, "output_out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}

---
title: تحديث عنصر صيغة Power Query باستخدام Node.js عبر C++
linktitle: تحديث عنصر صيغة Power Query
type: docs
weight: 120
url: /ar/nodejs-cpp/update-power-query-formula-item/
description: تعلم كيفية تحديث مصدر بيانات عنصر صيغة Power Query في ملف إكسل باستخدام Aspose.Cells for Node.js via C++.
---

## **سيناريو الاستخدام**

قد توجد حالات يتم فيها نقل ملفات مصدر البيانات ويكون ملف إكسل غير قادر على تحديد موقع الملف. في مثل هذه الحالات، توفر واجهة برمجة التطبيقات Aspose.Cells خيار تحديث عنصر صيغة Power Query باستخدام فئة [*PowerQueryFormulaItem*](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformulaitem) لتحديث موقع ملف المصدر.

## **تحديث عنصر صيغة Power Query**

توفر API لـ Aspose.Cells القدرة على تحديث عناصر صيغة Power Query. يعرض المقطع التالي تحديث موقع ملف مصدر البيانات في ملف Excel باستخدام خاصية [**PowerQueryFormulaItem.getValue()**](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformulaitem/#getValue--). المرفقات من الملفات المصدر والمخرج لمراجعتك.

- [ملف المصدر 1](106364953.xlsx)
- [ملف المصدر 2](106364954.xlsx)
- [ملف الناتج](106364955.xlsx)

## **الكود المثالي**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Working directories
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

const workbook = new AsposeCells.Workbook(path.join(sourceDir, "SamplePowerQueryFormula.xlsx"));
const mashupData = workbook.getDataMashup();

const powerQueryFormulas = mashupData.getPowerQueryFormulas();
const count = powerQueryFormulas.getCount();
for (let i = 0; i < count; i++) 
{
const formula = powerQueryFormulas.get(i);
const items = formula.getPowerQueryFormulaItems();
const itemsCount = items.getCount();
for (let j = 0; j < itemsCount; j++) 
{
const item = items.get(j);
if (item.getName() === "Source") 
{
item.setValue(`Excel.Workbook(File.Contents("${path.join(sourceDir, "SamplePowerQueryFormulaSource.xlsx")}", null, true)`);
}
}
}

// Save the output workbook.
workbook.save(outputDir + "SamplePowerQueryFormula_out.xlsx");
```

---
title: دمج أوراق عمل متعددة في ورقة عمل واحدة باستخدام Node.js عبر C++
linktitle: دمج الأوراق العمل المتعددة في ورقة عمل واحدة
type: docs
weight: 160
url: /ar/nodejs-cpp/combine-multiple-worksheets-into-a-single-worksheet/
description: تعلم كيفية دمج عدة أوراق عمل إلى ورقة عمل واحدة باستخدام Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}} 

في بعض الأحيان، قد تحتاج إلى دمج أوراق العمل المتعددة في ورقة عمل واحدة. يمكن بسهولة تحقيق ذلك باستخدام واجهة برمجة التطبيقات Aspose.Cells. سيوضح لك هذا المقال مثالًا على الكود الذي يقوم بقراءة دفتر عمل المصدر ويدمج البيانات من جميع أوراق العمل المصدر في ورقة عمل واحدة داخل دفتر عمل الوجهة.

{{% /alert %}} 

يُظهر مقطع الكود التالي لك كيفية دمج أوراق عمل متعددة في ورقة عمل واحدة.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleInput.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const destWorkbook = new AsposeCells.Workbook();
const destSheet = destWorkbook.getWorksheets().get(0);

let TotalRowCount = 0;

for (let i = 0; i < workbook.getWorksheets().getCount(); i++) {
const sourceSheet = workbook.getWorksheets().get(i);

const sourceRange = sourceSheet.getCells().getMaxDisplayRange();
const destRange = destSheet.getCells().createRange(
sourceRange.getFirstRow() + TotalRowCount,
sourceRange.getFirstColumn(),
sourceRange.getRowCount(),
sourceRange.getColumnCount()
);

destRange.copy(sourceRange);
TotalRowCount += sourceRange.getRowCount();
}

const outputFilePath = path.join(dataDir, "Output.out.xlsx");
destWorkbook.save(outputFilePath);
``` 

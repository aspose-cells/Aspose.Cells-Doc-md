---
title: كشف الخلايا المدمجة في ورقة عمل باستخدام Node.js عبر C++
linktitle: الكشف عن الخلايا المدمجة في ورقة البيانات
description: تعلم كيفية كشف الخلايا المدمجة في ورقة عمل باستخدام Aspose.Cells for Node.js via C++. ستوضح لك هذه المقالة كيفية استخدام المكتبة لتحديد والتلاعب بالخلايا المدمجة.
keywords: Aspose.Cells، ورقة عمل، دمج الخلايا، اكتشاف، تحديد، التشغيل باستخدام Node.js عبر C++
type: docs
weight: 80
url: /ar/nodejs-cpp/detect-merged-cells-in-a-worksheet/
---

{{% alert color="primary" %}}

يوفر هذا المقال معلومات حول كيفية الحصول على مناطق الخلايا المدمجة في ورقة العمل.

يسمح لك Aspose.Cells for Node.js via C++ بالحصول على مناطق الخلايا المدمجة في ورقة عمل. ويمكنك إلغاء الدمج (تقسيمها) أيضًا. تظهر هذه المقالة أبسط رمز باستخدام واجهة برمجة تطبيقات **Aspose.Cells** لأداء المهمة.

{{% /alert %}}

يوفر المكون metodologia [**Cells.getMergedAreas()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMergedAreas--) التي يمكنها الحصول على جميع الخلايا المدمجة. يعرض لك نموذج الشفرة التالي كيفية اكتشاف الخلايا المدمجة في ورقة العمل.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleInput.xlsx");

// Instantiate a new Workbook
// Open an existing excel file
const wkBook = new AsposeCells.Workbook(filePath);
// Get a worksheet in the workbook
const wkSheet = wkBook.getWorksheets().get("Sheet2");
// Clear its contents
wkSheet.getCells().clear();

// Get merged areas
const areas = wkSheet.getCells().getMergedAreas();

// Check if areas is null or not
if (!areas || areas.length === 0) {
console.warn("No merged areas to unmerge.");
return;
}

// Define some variables
let frow, fcol, erow, ecol, trows, tcols;
// Loop through the arraylist and get each cellarea
// To unmerge it
for (let i = 0; i < areas.length; i++) {
frow = areas[i].startRow;
fcol = areas[i].startColumn;
erow = areas[i].endRow;
ecol = areas[i].endColumn;

trows = erow - frow + 1;
tcols = ecol - fcol + 1;
wkSheet.getCells().unMerge(frow, fcol, trows, tcols);
}

const outputFilePath = path.join(dataDir, "MergeTrial.out.xlsx");
// Save the excel file
wkBook.save(outputFilePath);
```
{{< app/cells/assistant language="nodejs-cpp" >}}

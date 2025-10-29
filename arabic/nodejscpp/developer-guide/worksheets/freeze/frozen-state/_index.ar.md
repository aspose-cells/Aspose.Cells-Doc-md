---
title: كيفية التحقق من حالة التجمد بدون إكسل باستخدام Node.js عبر C++
linktitle: الحالة المجمدة
type: docs
weight: 190
url: /ar/nodejs-cpp/how-to-check-frozen-state-of-excel-worksheet
description: في هذا المقال، ستتعلم كيفية التحقق برمجيًا من حالة تجميد ورقة عمل إكسل باستخدام Node.js ومكتبة C++.

---

## **مقدمة**

في هذا المقال، سنتعلم كيفية التحقق برمجيًا من حالة تجميد ورقة عمل إكسل. يمكننا ببساطة معرفة ما إذا كانت ورقة العمل مجمدة أو مقسمة في MS Excel. لكن هل هناك طريقة لمعرفة ما إذا كانت مجمدة أو مقسمة باستخدام Node.js؟ يمكننا ببساطة فعل ذلك باستخدام Aspose.Cells for Node.js via C++.

## **هل النوافذ مجمدة**
باستخدام Aspose.Cells for Node.js via C++، يمكننا التحقق مما إذا كانت النافذة مجمدة وكم عدد الصفوف والأعمدة المقفلة.

يرجى استخدام خاصية [**Worksheet.getPaneState()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPaneState--) للتحقق من حالة ألواح النافذة والحصول على الصفوف والأعمدة المقفلة باستخدام طريقة [**Worksheet.getFreezedPanes()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getFreezedPanes--).
1. إنشاء سجل العمل لفتح الملف.
2. التحقق ما إذا كانت ورقة العمل مجمدة.
3. احصل على الصفوف والأعمدة المقفلة.

```javascript
try {
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Frozen.xlsx");

// Loads the workbook which contains frozen panes
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

// Check whether worksheet is frozen.
if (sheet.getPaneState() === AsposeCells.PaneStateType.Frozen || sheet.getPaneState() === AsposeCells.PaneStateType.FrozenSplit) {
let row, column, rows, columns;
// Gets locked rows and columns.
sheet.getFreezedPanes().forEach((value) => {
row = value[0];
column = value[1];
rows = value[2];
columns = value[3];
```  
{{< app/cells/assistant language="nodejs-cpp" >}}

---
title: الحصول على عنوان، عدد الخلايا، والانحراف عن كامل العمود والصف في النطاق باستخدام Node.js عبر C++
linktitle: الحصول على عنوان خلية، عدد الخلايا، الإزاحة، العمود الكامل والصف الكامل للنطاق
type: docs
weight: 330
url: /ar/nodejs-cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/
---

## **سيناريوهات الاستخدام المحتملة**
يوفر Aspose.Cells for Node.js via C++ كائن النطاق الذي يحتوي على طرق مساعدة تسهل على المستخدم العمل مع نطاقات Excel بسهولة. توضح هذه المقالة استخدام الطرق أو الخصائص التالية لكائن النطاق.

- **العنوان**

الحصول على عنوان النطاق.

- **عدد الخلايا**

الحصول على جميع عدد الخلايا في النطاق.

- **الإزاحة**

الحصول على النطاق بواسطة الإزاحة.

- **العمود الكامل**

الحصول على كائن نطاق يمثل العمود الكامل (أو الأعمدة) الذي يحتوي على النطاق المحدد.

- **الصف الكامل**

الحصول على كائن نطاق يمثل الصف الكامل (أو الصفوف) التي تحتوي على النطاق المحدد.

## **الحصول على العنوان، عدد الخلايا، الإزاحة، العمود الكامل والصف الكامل للنطاق**
يشرح الكود العيني التالي استخدام الطرق والخصائص كما تم مناقشتها أعلاه. يُرجى الرجوع إلى الانتاج على وحدة التحكم للكود الوارد أدناه للرجوع.

## **الكود المثالي**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create empty workbook.
const wb = new AsposeCells.Workbook();

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Create range A1:B3.
console.log("Creating Range A1:B3\n");
let rng = ws.getCells().createRange("A1:B3");

// Print range address and cell count.
console.log("Range Address: " + rng.getAddress());
console.log("Range row Count: " + rng.getRowCount());
console.log("Range column Count: " + rng.getColumnCount());

// Formatting console output.
console.log("----------------------");
console.log("");

// Create range A1.
console.log("Creating Range A1\n");
rng = ws.getCells().createRange("A1");

// Print range offset, entire column and entire row.
console.log("Offset: " + rng.getOffset(2, 2).getAddress());
console.log("Entire Column: " + rng.getEntireColumn().getAddress());
console.log("Entire Row: " + rng.getEntireRow().getAddress());

// Formatting console output.
console.log("----------------------");
console.log("");
```

## **مخرجات الوحدة**
{{< highlight javascript >}}
 Creating Range A1:B3

Range Address: A1:B3

Cell Count: 6

\----------------------

Creating Range A1

Offset: C3

Entire Column: A:A

Entire Row: 1:1

\----------------------

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}

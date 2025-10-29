---
title: حساب دالة IFNA باستخدام Aspose.Cells for Node.js via C++
description: كيفية حساب دوال IFNA باستخدام مكتبة Aspose.Cells في Node.js عبر C++. قم بتحميل ملف Excel موجود أو إنشائه، ثم حساب دالة IFNA للحصول على النتيجة. أخيرًا، نحفظ ملف Excel المعدل على القرص.
keywords: Aspose.Cells، Excel، دوال IFNA، الحسابات، Node.js عبر C++
type: docs
weight: 40
url: /ar/nodejs-cpp/calculating-ifna-function-using-aspose-cells/
---

{{% alert color="primary" %}} 

يدعم Aspose.Cells حساب دالة Excel المعروفة بـ IFNA. ترجع دالة IFNA القيمة التي تحددها إذا كانت الصيغة تُرجع خطأ قيمة #N/A؛ وإلا، فهي تُرجع نتيجة الصيغة.

{{% /alert %}} 
## **حساب دالة IFNA باستخدام Aspose.Cells for Node.js via C++**
يوضح الكود النموذجي التالي حساب دالة IFNA باستخدام Aspose.Cells for Node.js via C++.


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Create new workbook
// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Add data for VLOOKUP
worksheet.getCells().get("A1").putValue("Apple");
worksheet.getCells().get("A2").putValue("Orange");
worksheet.getCells().get("A3").putValue("Banana");

// Access cell A5 and A6
const cellA5 = worksheet.getCells().get("A5");
const cellA6 = worksheet.getCells().get("A6");

// Assign IFNA formula to A5 and A6
cellA5.setFormula('=IFNA(VLOOKUP("Pear",$A$1:$A$3,1,0),"Not found")');
cellA6.setFormula('=IFNA(VLOOKUP("Orange",$A$1:$A$3,1,0),"Not found")');

// Calculate the formula of workbook
workbook.calculateFormula();

// Print the values of A5 and A6
console.log(cellA5.getStringValue());
console.log(cellA6.getStringValue());
```
## **مخرجات الوحدة**
فيما يلي مخرجات وحدة الإدخال الخاصة بالكود المصدري أعلاه.

{{< highlight javascript >}}
 Not found

Orange
{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}

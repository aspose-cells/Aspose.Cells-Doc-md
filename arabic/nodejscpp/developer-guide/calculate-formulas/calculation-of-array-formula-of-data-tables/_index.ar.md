---
title: حساب صيغة المصفوفة للجداول البيانات باستخدام Node.js عبر C++
linktitle: حساب الصيغة الصفيفية لجداول البيانات
description: كيفية استخدام مكتبة Aspose.Cells لحساب صيغ المصفوفة لجدول بيانات في Microsoft Excel باستخدام Node.js عبر C++. تحميل ملف Excel أو إنشاؤه، حساب صيغة المصفوفة، وحفظ الملف المعدل.
keywords: Aspose.Cells، Excel، جداول البيانات، صيغ المصفوفة، الحسابات، Node.js عبر C++
type: docs
weight: 70
url: /ar/nodejs-cpp/calculation-of-array-formula-of-data-tables/
---

{{% alert color="primary" %}}

يمكنك إنشاء جدول بيانات في Microsoft Excel باستخدام البيانات > تحليل ماذا-لو > جدول البيانات.... يتيح لك Aspose.Cells الآن حساب صيغة المصفوفة الخاصة بجدول البيانات. يرجى استخدام [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) كالمعتاد لحساب أي نوع من الصيغ.

{{% /alert %}}

في الكود النموذجي التالي، استخدمنا الملف المصدر (ملف Excel مصدر)5115535.xlsx. إذا قمت بتغيير قيمة الخلية B1 إلى 100، ستصبح قيم جدول البيانات المحددة باللون الأصفر 120 كما هو موضح في الصور التالية. يولد الكود النموذجي الملف [PDF الناتج](5115538.pdf).

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

هنا الكود النموذجي المستخدم لإنشاء الملف [PDF الناتج](5115538.pdf) من الملف المصدر (ملف Excel مصدر)5115535.xlsx. يرجى قراءة التعليقات للحصول على مزيد من المعلومات.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create workbook from source excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "DataTable.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// When you will put 100 in B1, then all Data Table values formatted as Yellow will become 120
worksheet.getCells().get("B1").putValue(100);

// Calculate formula, now it also calculates Data Table array formula
workbook.calculateFormula();

// Save the workbook in pdf format
workbook.save(path.join(dataDir, "output_out.pdf"));
```

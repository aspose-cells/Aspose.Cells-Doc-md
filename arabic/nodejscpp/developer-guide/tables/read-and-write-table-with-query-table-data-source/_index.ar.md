---
title: قراءة وكتابة الجدول مع مصدر بيانات جدول الاستعلام عبر Node.js
linktitle: قراءة وكتابة الجدول مع مصدر بيانات جدول الاستعلام
type: docs
weight: 30
url: /ar/nodejs-cpp/read-and-write-table-with-query-table-data-source/
description: تعلم كيفية قراءة وكتابة جدول باستخدام مصدر بيانات QueryTable باستخدام Aspose.Cells for Node.js via C++. 
---

## **قراءة وكتابة الجدول مع مصدر بيانات جدول الاستعلام**
مع Aspose.Cells for Node.js via C++، يمكنك قراءة وكتابة جدول يحتوي على QueryTable كمصدر للبيانات. الدعم لهذه الميزة موجود أيضًا لملفات XLS. يُظهر مقتطف الكود التالي قراءة وكتابة جدول من هذا النوع من خلال قراءة الجدول أولًا ثم تعديله لإضافة صف الإجماليات.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the source directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load workbook object
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "SampleTableWithQueryTable.xls"));

const worksheet = workbook.getWorksheets().get(0);

const table = worksheet.getListObjects().get(0);

// Check the data source type if it is query table
if (table.getDataSourceType() === AsposeCells.TableDataSourceType.QueryTable) {
table.setShowTotals(true);
}

// Save the file
workbook.save(path.join(outputDir, "SampleTableWithQueryTable_out.xls"));
```

الملفات الإكسل المصدر والناتج مرفقة للرجوع إليها.

[ملف المصدر](96928091.xls)

[ملف الناتج](96928092.xls)

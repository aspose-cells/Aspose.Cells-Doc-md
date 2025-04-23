---
title: نشر الصيغة تلقائيًا في جدول أو كائن قائمة أثناء إدخال البيانات في صفوف جديدة باستخدام Node.js عبر C++
linktitle: يحدد صيغة الجدول
type: docs
weight: 260
url: /ar/nodejs-cpp/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
description: تعلم كيف تقوم بنشر الصيغ تلقائيًا في الجداول أو كائنات القائمة أثناء إدخال البيانات في الصفوف الجديدة باستخدام Aspose.Cells for Node.js via C++.
---

## **سيناريوهات الاستخدام المحتملة**
أحيانًا، ترغب في أن تنتشر صيغة في جدولك أو كائن القائمة تلقائيًا إلى الصفوف الجديدة أثناء إدخال بيانات جديدة. هذا هو السلوك الافتراضي لمايكروسوفت إكسل. لتحقيق نفس الوظيفة مع Aspose.Cells for Node.js via C++، يرجى استخدام خاصية [ListColumn.getFormula()](https://reference.aspose.com/cells/nodejs-cpp/listcolumn/#getFormula--) .

## **نشر الصيغة تلقائيًا في جدول أو كائن قائمة أثناء إدخال البيانات في الصفوف الجديدة**
يخلق رمز المثال التالي جدول أو كائن قائمة بحيث تنتشر الصيغة في العمود ب تلقائيًا إلى الصفوف الجديدة عند إدخال بيانات جديدة. يرجى التحقق من [ملف إكسل الناتج](5115469.xlsx) الذي تم توليده بهذا الرمز. إذا أدخلت أي رقم في الخلية A3، سترى أن الصيغة في الخلية B2 تنتشر تلقائيًا إلى الخلية B3.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const book = new AsposeCells.Workbook();

// Access first worksheet
const sheet = book.getWorksheets().get(0);

// Add column headings in cell A1 and B1
sheet.getCells().get(0, 0).putValue("Column A");
sheet.getCells().get(0, 1).putValue("Column B");

// Add list object, set its name and style
const listObject = sheet.getListObjects().get(sheet.getListObjects().add(0, 0, 1, sheet.getCells().getMaxColumn(), true));
listObject.setTableStyleType(AsposeCells.TableStyleType.TableStyleMedium2);
listObject.setDisplayName("Table");

// Set the formula of second column so that it propagates to new rows automatically while entering data
listObject.getListColumns().get(1).setFormula("=[Column A] + 1");

// Save the workbook in xlsx format
book.save(path.join(dataDir, "output_out.xlsx"));
```

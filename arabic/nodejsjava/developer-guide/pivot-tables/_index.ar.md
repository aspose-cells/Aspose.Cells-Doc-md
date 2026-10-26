---
title: إدراج جدول محوري
linktitle: إدراج جدول محوري
description: إنشاء وتنسيق الجداول المحورية في ملفات جداول بيانات Excel باستخدام Aspose.Cells for Node.js via Java.
keywords: إنشاء جدول محوري, إدراج جدول محوري, تنسيق جدول محوري, Aspose.Cells for Node.js via Java.
type: docs
weight: 160
url: /ar/nodejs-java/create-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **ما هو الجدول المحوري؟**
الجدول المحوري تقرير ملخص تفاعلي: فهو يجمع كتلة كبيرة من البيانات الخام المرتبة صفًا بصف في مصفوفة موجزة، من دون استخدام أي صيغة. وتحدّد أنت الأعمدة التي تصبح تسميات للصفوف، وتلك التي تصبح تسميات للأعمدة، والأعمدة التي يتم تجميعها كقيم؛ ويتولى الجدول المحوري عملية التجميع والحساب:
- **تلخيص** — إجمالي المبيعات لكل منتج أو منطقة أو ربع، بدلاً من سلاسل الصيغ الطويلة.
- **مقارنة** — وضع الفئات في الصفوف والفترات في الأعمدة يحوّل قائمة مسطحة إلى تقرير متقاطع تظهر فيه الاتجاهات بوضوح.
- **الانتقال إلى التفاصيل** — انقر نقرًا مزدوجًا على أي قيمة ملخص لفحص الصفوف المصدر المرتبطة بها.
- **تحديث** — عند تغير بيانات المصدر، تكفي عملية تحديث واحدة لإعادة حساب التقرير بالكامل.
تشمل السيناريوهات الشائعة لوحات معلومات المبيعات، وتحليلات توزيع المصروفات، وتحليلات المخزون — أي سؤال من قبيل «كيف تتوزع هذه الأرقام حسب الفئة والوقت؟». ويتيح Aspose.Cells for Node.js via Java إنشاء الجداول المحورية برمجيًا، بحيث يمكن للمصنفات التي ينشئها تطبيقك أن تتضمن تقارير جاهزة بدلاً من البيانات الخام فقط.

### **نموذج كائن الجدول المحوري**
يوفر Aspose.Cells مجموعة من الفئات المستخدمة لإنشاء الجداول المحورية والتحكم فيها. وتتمثل لبنات البناء في:
- `PivotField` يمثل حقلًا في `PivotTable`.
- `PivotFieldCollection` يمثل مجموعة جميع كائنات `PivotField` في `PivotTable`.
- `PivotTable` يمثل جدولًا محوريًا على ورقة عمل.
- `PivotTableCollection` يمثل مجموعة جميع كائنات `PivotTable` على ورقة عمل.

### **إنشاء جدول محوري بسيط باستخدام Aspose.Cells**
تتمثل عملية إنشاء جدول محوري في ثلاث خطوات: كتابة بيانات المصدر في خلايا ورقة العمل، وإضافة الجدول المحوري إلى موضع الوجهة، ثم وضع حقول الجدول المحوري في مناطق الصفوف والأعمدة والبيانات.
1. أضف البيانات إلى ورقة العمل باستخدام طريقة `putValue` الخاصة بالخلية. ستُستخدم هذه البيانات كمصدر بيانات للجدول المحوري.
2. أضف جدولًا محوريًا إلى ورقة العمل عن طريق استدعاء طريقة `add` في مجموعة `PivotTables`: `add(sourceData, row, column)`. يمثل `sourceData` نطاق المصدر (مثل "A1:C8")؛ ويمثل `row` و`column` إحداثي خلية الوجهة (بدءًا من 0) في الركن العلوي الأيسر للجدول المحوري (تعني الخلية E3 الصف 2 والعمود 4). وتعيد الطريقة كائن `PivotTable` الجديد مباشرة.
3. ضع حقول الجدول المحوري باستخدام طريقة `addFieldToArea` في كائن `PivotTable`: يوضع اسم الحقل في منطقة الصفوف (`PivotFieldType.ROW`)، أو منطقة الأعمدة (`PivotFieldType.COLUMN`)، أو منطقة البيانات (`PivotFieldType.DATA`).
4. احفظ المصنف — يُكتب الجدول المحوري في الملف المحفوظ.
بعد تنفيذ رمز المثال، يضاف جدول محوري إلى ورقة العمل.

```javascript
const AsposeCells = require("aspose.cells");

// إنشاء مصنف عمل جديد والحصول على ورقة العمل الأولى
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// كتابة بيانات المصدر: المبيعات حسب الرياضة والربع
sheet.getCells().get("A1").putValue("Sport");
sheet.getCells().get("B1").putValue("Quarter");
sheet.getCells().get("C1").putValue("Sales");
sheet.getCells().get("A2").putValue("Golf");
sheet.getCells().get("B2").putValue("Qtr3");
sheet.getCells().get("C2").putValue(1500);
sheet.getCells().get("A3").putValue("Golf");
sheet.getCells().get("B3").putValue("Qtr4");
sheet.getCells().get("C3").putValue(2000);
sheet.getCells().get("A4").putValue("Tennis");
sheet.getCells().get("B4").putValue("Qtr3");
sheet.getCells().get("C4").putValue(600);
sheet.getCells().get("A5").putValue("Tennis");
sheet.getCells().get("B5").putValue("Qtr4");
sheet.getCells().get("C5").putValue(1500);
sheet.getCells().get("A6").putValue("Tennis");
sheet.getCells().get("B6").putValue("Qtr3");
sheet.getCells().get("C6").putValue(4070);
sheet.getCells().get("A7").putValue("Tennis");
sheet.getCells().get("B7").putValue("Qtr4");
sheet.getCells().get("C7").putValue(5000);
sheet.getCells().get("A8").putValue("Golf");
sheet.getCells().get("B8").putValue("Qtr3");
sheet.getCells().get("C8").putValue(6430);

// إضافة جدول محوري في خلية الوجهة E3، بمصدر A1:C8
let pivotTable = sheet.getPivotTables().add("A1:C8", 2, 4);

// تعيين حقول الجدول المحوري: الرياضة إلى الصفوف، الربع إلى الأعمدة، المبيعات إلى البيانات
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Quarter");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Sales");

// حفظ المصنف
workbook.save("pivotTable_test_out.xlsx");
```

{{% alert color="primary" %}}
عند تعيين نطاق من الخلايا كمصدر للبيانات، يجب أن يمتد النطاق من أعلى اليسار إلى أسفل اليمين. على سبيل المثال، النطاق "A1:C3" صالح، بينما النطاق "C3:A1" غير صالح.
{{% /alert %}}

## مقالات ذات صلة
- [إضافة حقول التصفية إلى جدول محوري في Aspose.Cells for Node.js via Java](/cells/ar/nodejs-java/add-page-field-in-pivot-table/)
- [تطبيق الأنماط على الجداول المحورية في Aspose.Cells for Node.js via Java](/cells/ar/nodejs-java/apply-style-to-pivot-table/)
- [تعديل تخطيط حقل الصفحة في الجدول المحوري](/cells/ar/nodejs-java/change-page-field-layout/)
- [تصفية الجداول المحورية حسب التسمية أو القيمة](/cells/ar/nodejs-java/filter-by-label-or-value-of-pivot-table/)
- [إدارة حقول قيم الجدول المحوري في Aspose.Cells for Node.js via Java](/cells/ar/nodejs-java/manage-value-fields/)

{{< app/cells/assistant language="nodejs-java" >}}
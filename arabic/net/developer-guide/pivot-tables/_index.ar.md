---
title: إدراج جدول محوري
linktitle: إدراج جدول محوري
description: إنشاء الجداول المحورية وتنسيقها لملفات جداول بيانات Excel.
keywords: إنشاء جدول محوري, إدراج جدول محوري, تنسيق جدول محوري.
type: docs
weight: 160
url: /ar/net/create-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **ما هو الجدول المحوري؟**
الجدول المحوري هو تقرير ملخص تفاعلي: يختصر مجموعة كبيرة من البيانات الخام، المدرجة صفًا بصف، في مصفوفة موجزة من دون أي صيغة. تحدد أنت أي الأعمدة ستُستخدم كتسميات صفوف، وأيها كتسميات أعمدة، وأيها سيُجمَّع في القيم؛ يتولى الجدول المحوري عملية التجميع والحساب:
- **تلخيص** — إجمالي المبيعات لكل منتج أو منطقة أو ربع، بدلاً من سلاسل الصيغ الطويلة.
- **مقارنة** — تحوّل قائمة مسطحة إلى تقرير متقاطع، من خلال وضع الفئات في الصفوف والفترات في الأعمدة، لتظهر الاتجاهات بلمحة.
- **الانتقال إلى التفاصيل** — انقر نقرًا مزدوجًا على أي قيمة ملخص لفحص الصفوف المصدر الكامنة خلفها.
- **تحديث** — عند تغيّر بيانات المصدر، تكفي عملية تحديث واحدة لإعادة حساب التقرير بالكامل.
تشمل السيناريوهات النموذجية لوحات معلومات المبيعات وتفصيلات المصروفات وتحليل المخزون، أي أي سؤال من النوع «كيف تتفصل هذه الأرقام حسب الفئة والوقت؟». يتيح Aspose.Cells for .NET إنشاء الجداول المحورية برمجيًا، لذا يمكن للمصنفات التي ينشئها تطبيقك أن تحمل تقارير جاهزة بدلًا من البيانات الخام وحدها.

### **نموذج كائنات الجدول المحوري**
يوفر Aspose.Cells مجموعة خاصة من الفئات في مساحة الأسماء [**Aspose.Cells.Pivot**](https://reference.aspose.com/cells/net/aspose.cells.pivot) تُستخدم لإنشاء الجداول المحورية والتحكم بها. وتُستخدم هذه الفئات لإنشاء كائنات [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) وضبطها، وهي المكوّنات الأساسية للجدول المحوري. وتتمثل هذه الكائنات في:
- [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) يمثل حقلًا في [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) يمثل مجموعة جميع كائنات [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) في [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) يمثل كائن PivotTable على ورقة عمل.
- [**PivotTableCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) يمثل مجموعة جميع كائنات [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) على ورقة عمل.

### **إنشاء جدول محوري بسيط باستخدام Aspose.Cells**
تتم عملية إنشاء الجدول المحوري عبر الخطوات التالية: كتابة بيانات المصدر في خلايا ورقة العمل، وإضافة الجدول المحوري في موضع الوجهة، ووضع حقوله في مناطق الصفوف والأعمدة والبيانات.
1. أضف البيانات إلى ورقة عمل باستخدام طريقة [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) الخاصة بكائن [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell). ستُستخدم هذه البيانات كمصدر بيانات للجدول المحوري.
2. أضف جدولًا محوريًا إلى ورقة العمل عن طريق استدعاء طريقة [**Add**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/add/index) في مجموعة [**PivotTables**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection): `Add(sourceData, row, column)`. و`sourceData` هو نطاق المصدر (مثل "A1:C8")؛ و`row` و`column` هما إحداثيات الصف والعمود لخلية الوجهة، وتبدأ من الصفر عند الركن العلوي الأيسر للجدول المحوري (فخلية E3 تعني الصف 2 والعمود 4). تُعيد الطريقة كائن [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) الجديد مباشرة.
3. ضع حقول الجدول المحوري باستخدام طريقة `AddFieldToArea` الخاصة بكائن [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable): يوضع اسم الحقل في منطقة الصفوف (`PivotFieldType.Row`)، أو منطقة الأعمدة (`PivotFieldType.Column`)، أو منطقة البيانات (`PivotFieldType.Data`).
4. احفظ المصنف — يُكتب الجدول المحوري في الملف المحفوظ.
بعد تنفيذ رمز المثال، تتم إضافة جدول محوري إلى ورقة العمل.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;

// إنشاء مصنف جديد والحصول على ورقة العمل الأولى
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];

// كتابة البيانات المصدرية: المبيعات لكل رياضة وربع
sheet.Cells["A1"].PutValue("Sport");
sheet.Cells["B1"].PutValue("Quarter");
sheet.Cells["C1"].PutValue("Sales");
sheet.Cells["A2"].PutValue("Golf");
sheet.Cells["B2"].PutValue("Qtr3");
sheet.Cells["C2"].PutValue(1500);
sheet.Cells["A3"].PutValue("Golf");
sheet.Cells["B3"].PutValue("Qtr4");
sheet.Cells["C3"].PutValue(2000);
sheet.Cells["A4"].PutValue("Tennis");
sheet.Cells["B4"].PutValue("Qtr3");
sheet.Cells["C4"].PutValue(600);
sheet.Cells["A5"].PutValue("Tennis");
sheet.Cells["B5"].PutValue("Qtr4");
sheet.Cells["C5"].PutValue(1500);
sheet.Cells["A6"].PutValue("Tennis");
sheet.Cells["B6"].PutValue("Qtr3");
sheet.Cells["C6"].PutValue(4070);
sheet.Cells["A7"].PutValue("Tennis");
sheet.Cells["B7"].PutValue("Qtr4");
sheet.Cells["C7"].PutValue(5000);
sheet.Cells["A8"].PutValue("Golf");
sheet.Cells["B8"].PutValue("Qtr3");
sheet.Cells["C8"].PutValue(6430);

// إضافة جدول محوري في خلية الوجهة E3، مصدره A1:C8
PivotTable pivotTable = sheet.PivotTables.Add("A1:C8", 2, 4);

// تعيين حقول الجدول المحوري: Sport إلى الصفوف، Quarter إلى الأعمدة، Sales إلى البيانات
pivotTable.AddFieldToArea(PivotFieldType.Row, "Sport");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Quarter");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Sales");

// حفظ المصنف
workbook.Save("pivotTable_test_out.xlsx");
```

{{% alert color="primary" %}}
عند تعيين نطاق من الخلايا كمصدر للبيانات، يجب أن يمتد النطاق من أعلى اليسار إلى أسفل اليمين. على سبيل المثال، "A1:C3" صالحة، لكن "C3:A1" غير صالحة.
{{% /alert %}}

## مقالات ذات صلة
- [إضافة حقول التصفية إلى جدول محوري في Aspose.Cells for .NET](/cells/ar/net/add-page-field-in-pivot-table/)
- [تطبيق الأنماط على الجداول المحورية في Aspose.Cells for .NET](/cells/ar/net/apply-style-to-pivot-table/)
- [تعديل تخطيط حقل الصفحة في الجدول المحوري](/cells/ar/net/change-page-field-layout/)
- [تصفية الجداول المحورية حسب التسمية أو القيمة](/cells/ar/net/filter-by-label-or-value-of-pivot-table/)
- [إدارة حقول قيم الجدول المحوري في Aspose.Cells for .NET](/cells/ar/net/manage-value-fields/)

{{< app/cells/assistant language="csharp" >}}
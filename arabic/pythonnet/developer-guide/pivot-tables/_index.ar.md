---
title: إدراج جدول محوري
linktitle: إدراج جدول محوري
description: إنشاء وتنسيق الجداول المحورية باستخدام Aspose.Cells for Python عبر .NET.
keywords: إنشاء جدول محوري, إدراج جدول محوري, تنسيق جدول محوري.
type: docs
weight: 160
url: /ar/python-net/create-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **ما هو الجدول المحوري؟**
الجدول المحوري هو تقرير ملخص تفاعلي يختصر حجمًا كبيرًا من البيانات الخام المُدرجة صفًا بصف في مصفوفة موجزة، دون الحاجة إلى أي صيغة. أنت تحدد الأعمدة التي ستُستخدم كتسميات للصفوف، والأعمدة التي ستُستخدم كتسميات للأعمدة، والأعمدة التي ستُجمع كقيم، بينما يتولى الجدول المحوري عملية التجميع والحساب:
- **تلخيص** — إجمالي المبيعات لكل منتج أو منطقة أو ربع، بدلاً من سلاسل الصيغ الطويلة.
- **مقارنة** — وضع الفئات في الصفوف والفترات في الأعمدة يحوّل قائمة مسطحة إلى تقرير متقاطع تكشف فيه الاتجاهات بنظرة سريعة.
- **الانتقال إلى التفاصيل** — انقر نقرًا مزدوجًا على أي قيمة ملخصة لفحص صفوف المصدر التي تتكون منها.
- **إعادة التحديث** — عند تغيير بيانات المصدر، تكفي عملية تحديث واحدة لإعادة حساب التقرير بالكامل.
تشمل السيناريوهات النموذجية لوحات معلومات المبيعات، وتحليلات المصروفات، وتحليلات المخزون، وأي سؤال من نوع «كيف تُفصَّل هذه الأرقام حسب الفئة والزمن؟». يتيح Aspose.Cells for Python عبر .NET إنشاء جداول محورية مماثلة برمجيًا، بحيث يمكن للمصنفات التي يولّدها تطبيقك أن تحمل تقارير جاهزة بدلًا من البيانات الخام فحسب.

### **نموذج كائن الجدول المحوري**
يوفر Aspose.Cells for Python عبر .NET مجموعة خاصة من الفئات في namespace [**aspose.cells.pivot**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/) تُستخدم لإنشاء الجداول المحورية والتحكم فيها. وتُستخدم هذه الفئات لإنشاء كائنات [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/) وضبطها، وهي الكتل البنائية الأساسية للجدول المحوري. وتتمثل هذه الكائنات فيما يلي:
- [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/) يمثل حقلًا في [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection) يمثل مجموعة جميع كائنات [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/) الموجودة في [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) يمثل كائن PivotTable على ورقة عمل.
- [**PivotTableCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection) يمثل مجموعة جميع كائنات [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) الموجودة على ورقة عمل.

### **إنشاء جدول محوري بسيط باستخدام Aspose.Cells**
تتمثل عملية إنشاء جدول محوري في ثلاث خطوات: كتابة بيانات المصدر في خلايا ورقة العمل، وإضافة الجدول المحوري في موضع الوجهة، ثم وضع حقول الجدول المحوري في مناطق الصفوف والأعمدة والبيانات.
1. أضف البيانات إلى ورقة العمل باستخدام كائن [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) وطريقة [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#str) الخاصة به. ستُستخدم هذه البيانات كمصدر بيانات للجدول المحوري.
2. أضف جدولًا محوريًا إلى ورقة العمل عن طريق استدعاء طريقة [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/add/#str-str-str) الخاصة بمجموعة [**PivotTables**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection): `add(source_data, row, column)`. يمثل `source_data` نطاق المصدر (مثل "A1:C8")، بينما تمثل `row` و`column` الإحداثيات ذات الأساس الصفري لخلية الوجهة عند الركن العلوي الأيسر للجدول المحوري (الخلية E3 تعني الصف 2 والعمود 4). وتعيد الطريقة كائن [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) الجديد مباشرة.
3. ضع حقول الجدول المحوري في مناطقها باستخدام طريقة `add_field_to_area` الخاصة بكائن [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable): يوضع اسم الحقل في منطقة الصفوف (`PivotFieldType.ROW`)، أو منطقة الأعمدة (`PivotFieldType.COLUMN`)، أو منطقة البيانات (`PivotFieldType.DATA`).
4. احفظ المصنف؛ إذ يُكتب الجدول المحوري في الملف المحفوظ.
بعد تنفيذ مثال التعليمات البرمجية، تتم إضافة جدول محوري إلى ورقة العمل.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType

# إنشاء مصنف جديد والحصول على ورقة العمل الأولى
workbook = ac.Workbook()
sheet = workbook.worksheets[0]

# كتابة بيانات المصدر: المبيعات لكل رياضة وربع سنة
sheet.cells.get("A1").put_value("Sport")
sheet.cells.get("B1").put_value("Quarter")
sheet.cells.get("C1").put_value("Sales")
sheet.cells.get("A2").put_value("Golf")
sheet.cells.get("B2").put_value("Qtr3")
sheet.cells.get("C2").put_value(1500)
sheet.cells.get("A3").put_value("Golf")
sheet.cells.get("B3").put_value("Qtr4")
sheet.cells.get("C3").put_value(2000)
sheet.cells.get("A4").put_value("Tennis")
sheet.cells.get("B4").put_value("Qtr3")
sheet.cells.get("C4").put_value(600)
sheet.cells.get("A5").put_value("Tennis")
sheet.cells.get("B5").put_value("Qtr4")
sheet.cells.get("C5").put_value(1500)
sheet.cells.get("A6").put_value("Tennis")
sheet.cells.get("B6").put_value("Qtr3")
sheet.cells.get("C6").put_value(4070)
sheet.cells.get("A7").put_value("Tennis")
sheet.cells.get("B7").put_value("Qtr4")
sheet.cells.get("C7").put_value(5000)
sheet.cells.get("A8").put_value("Golf")
sheet.cells.get("B8").put_value("Qtr3")
sheet.cells.get("C8").put_value(6430)

# إضافة جدول محوري في خلية الوجهة E3، باستخدام A1:C8 كمصدر
pivot_table = sheet.pivot_tables.add("A1:C8", 2, 4)

# تعيين حقول الجدول المحوري: Sport إلى الصفوف، Quarter إلى الأعمدة، Sales إلى البيانات
pivot_table.add_field_to_area(PivotFieldType.ROW, "Sport")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Quarter")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Sales")

# حفظ المصنف
workbook.save("pivotTable_test_out.xlsx")
```

{{% alert color="primary" %}}
عند تعيين نطاق من الخلايا كمصدر بيانات، يجب أن يمتد النطاق من أعلى اليسار إلى أسفل اليمين. على سبيل المثال، يكون النطاق "A1:C3" صالحًا، بينما يكون النطاق "C3:A1" غير صالح.
{{% /alert %}}

## مقالات ذات صلة
- [إضافة حقول التصفية إلى جدول محوري في Aspose.Cells for Python عبر .NET](/cells/ar/python-net/add-page-field-in-pivot-table/)
- [تطبيق الأنماط على الجداول المحورية في Aspose.Cells for Python عبر .NET](/cells/ar/python-net/apply-style-to-pivot-table/)
- [تعديل تخطيط حقل الصفحة في الجدول المحوري](/cells/ar/python-net/change-page-field-layout/)
- [تصفية الجداول المحورية حسب التسمية أو القيمة](/cells/ar/python-net/filter-by-label-or-value-of-pivot-table/)
- [إدارة حقول قيم الجدول المحوري في Aspose.Cells for Python عبر .NET](/cells/ar/python-net/manage-value-fields/)

{{< app/cells/assistant language="python-net" >}}
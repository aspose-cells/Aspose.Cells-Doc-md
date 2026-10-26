---
title: الجداول المحورية
linktitle: الجداول المحورية
description: إنشاء وتنسيق الجداول المحورية باستخدام Aspose.Cells for Python via Java.
keywords: إنشاء جدول محوري, إدراج جدول محوري, تنسيق جدول محوري.
type: docs
weight: 160
url: /ar/python-java/create-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **ما هو الجدول المحوري؟**
الجدول المحوري هو تقرير ملخص تفاعلي: يختصر مجموعة كبيرة من البيانات الخام المرتبة صفًا بصف في مصفوفة موجزة دون الحاجة إلى استخدام أي صيغة. تحدد أنت الأعمدة التي ستُستخدم كتسميات للصفوف، وتلك التي ستُستخدم كتسميات للأعمدة، وتلك التي ستُجمَّع كقيم — يتولى الجدول المحوري عملية التجميع والحساب:
- **تلخيص** — إجمالي المبيعات لكل منتج أو منطقة أو ربع بدلًا من سلاسل الصيغ الطويلة.
- **مقارنة** — وضع الفئات في الصفوف والفترات في الأعمدة يحوّل قائمة مسطحة إلى تقرير متقاطع تظهر فيه الاتجاهات بنظرة سريعة.
- **الانتقال إلى التفاصيل** — انقر نقرًا مزدوجًا على أي قيمة ملخصة لفحص الصفوف المصدرية المرتبطة بها.
- **تحديث** — عند تغيّر بيانات المصدر، تؤدي عملية تحديث واحدة إلى إعادة حساب التقرير بالكامل.
تشمل السيناريوهات النموذجية لوحات معلومات المبيعات وتفصيل المصروفات وتحليل المخزون — أي سؤال من الشكل «كيف تُفصَّل هذه الأرقام حسب الفئة والوقت؟». يبني Aspose.Cells for Python via Java الجداول المحورية ذاتها برمجيًا، لذا يمكن أن تحمل المصنفات التي ينشئها تطبيقك تقارير جاهزة بدلاً من البيانات الخام فقط.

### **نموذج كائن الجدول المحوري**
يوفر Aspose.Cells مجموعة من الفئات المستخدمة لإنشاء الجداول المحورية والتحكم فيها. العناصر الأساسية هي:
- `PivotField` يمثل حقلًا في `PivotTable`.
- `PivotFieldCollection` يمثل مجموعة جميع كائنات `PivotField` الموجودة في `PivotTable`.
- `PivotTable` يمثل جدولًا محوريًا على ورقة عمل.
- `PivotTableCollection` يمثل مجموعة جميع كائنات `PivotTable` الموجودة على ورقة عمل.

### **إنشاء جدول محوري بسيط باستخدام Aspose.Cells**
يتطلب إنشاء جدول محوري ثلاث خطوات: كتابة بيانات المصدر في خلايا ورقة العمل، وإضافة الجدول المحوري في موضع الوجهة، ووضع حقول الجدول المحوري في مناطق الصفوف والأعمدة والبيانات.
1. أضف البيانات إلى ورقة العمل باستخدام طريقة `putValue` الخاصة بالخلية. ستُستخدم هذه البيانات بوصفها مصدر بيانات الجدول المحوري.
2. أضف الجدول المحوري إلى ورقة العمل عن طريق استدعاء طريقة `add` الخاصة بمجموعة `PivotTables`: `add(sourceData, row, column)`. يمثل `sourceData` نطاق المصدر (على سبيل المثال، "A1:C8")، وتحدد `row` و`column` إحداثيات خلية الوجهة، بدءًا من الصفر، عند الركن العلوي الأيسر للجدول المحوري (الخلية E3 تعني الصف 2 والعمود 4). تُرجع الطريقة كائن `PivotTable` الجديد مباشرة.
3. ضع حقول الجدول المحوري باستخدام طريقة `addFieldToArea` الخاصة بكائن `PivotTable`: يوضع اسم الحقل في منطقة الصفوف (`PivotFieldType.ROW`) أو منطقة الأعمدة (`PivotFieldType.COLUMN`) أو منطقة البيانات (`PivotFieldType.DATA`).
4. احفظ المصنف — إذ يُكتب الجدول المحوري في الملف المحفوظ.
بعد تنفيذ رمز المثال، تتم إضافة جدول محوري إلى ورقة العمل.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType

# إنشاء مصنف جديد والحصول على ورقة العمل الأولى
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()

# كتابة بيانات المصدر: المبيعات لكل رياضة وربع سنة
cells.get("A1").putValue("Sport")
cells.get("B1").putValue("Quarter")
cells.get("C1").putValue("Sales")
cells.get("A2").putValue("Golf")
cells.get("B2").putValue("Qtr3")
cells.get("C2").putValue(1500)
cells.get("A3").putValue("Golf")
cells.get("B3").putValue("Qtr4")
cells.get("C3").putValue(2000)
cells.get("A4").putValue("Tennis")
cells.get("B4").putValue("Qtr3")
cells.get("C4").putValue(600)
cells.get("A5").putValue("Tennis")
cells.get("B5").putValue("Qtr4")
cells.get("C5").putValue(1500)
cells.get("A6").putValue("Tennis")
cells.get("B6").putValue("Qtr3")
cells.get("C6").putValue(4070)
cells.get("A7").putValue("Tennis")
cells.get("B7").putValue("Qtr4")
cells.get("C7").putValue(5000)
cells.get("A8").putValue("Golf")
cells.get("B8").putValue("Qtr3")
cells.get("C8").putValue(6430)

# إضافة جدول محوري في خلية الوجهة E3، مصدره A1:C8
pivotTable = sheet.getPivotTables().add("A1:C8", 2, 4)

# تعيين حقول الجدول المحوري: Sport إلى الصفوف، Quarter إلى الأعمدة، Sales إلى البيانات
pivotTable.addFieldToArea(PivotFieldType.ROW, "Sport")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Quarter")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Sales")

# حفظ المصنف
workbook.save("pivotTable_test_out.xlsx")
```

{{% alert color="primary" %}}
عند تعيين نطاق من الخلايا كمصدر للبيانات، يجب أن يمتد النطاق من أعلى اليسار إلى أسفل اليمين. على سبيل المثال، تُعد "A1:C3" صالحة، بينما تُعد "C3:A1" غير صالحة.
{{% /alert %}}

## مقالات ذات صلة
- [إضافة حقول تصفية إلى جدول محوري في Aspose.Cells for Python via Java](/cells/ar/python-java/add-page-field-in-pivot-table/)
- [تطبيق الأنماط على الجداول المحورية في Aspose.Cells for Python via Java](/cells/ar/python-java/apply-style-to-pivot-table/)
- [تعديل تخطيط حقل الصفحة في الجدول المحوري](/cells/ar/python-java/change-page-field-layout/)
- [تصفية الجداول المحورية حسب التسمية أو القيمة](/cells/ar/python-java/filter-by-label-or-value-of-pivot-table/)
- [إدارة حقول قيم الجدول المحوري في Aspose.Cells for Python via Java](/cells/ar/python-java/manage-value-fields/)

{{< app/cells/assistant language="python" >}}
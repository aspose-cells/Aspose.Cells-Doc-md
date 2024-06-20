---
title: إنشاء جداول محورية ورسوم بيانية محورية
type: docs
weight: 20
url: /ar/python-net/create-pivot-tables-and-pivot-charts/
description: كيفية إضافة جداول الإحاطة والرسوم البيانية الدائرية باستخدام Aspose.Cells لـ Python via .NET.
keywords: Aspose.Cells for Python Excel، مكتبة Excel Python، إضافة جداول الإحاطة والرسوم البيانية باستخدام مكتبة Aspose.Cells لـ Python Excel.
---

{{% alert color="primary" %}}

الجدول المحوري هو ملخص تفاعلي للسجلات. على سبيل المثال، قد تحتوي على مئات الإدخالات الخاصة بالفواتير في قائمة داخل صفحة العمل. يمكن للجدول المحوري إجمالي الفواتير حسب العميل، المنتج أو التاريخ. باستخدام مايكروسوفت إكسل يمكن بسرعة إعادة ترتيب المعلومات في الجدول المحوري عن طريق سحب الأزرار إلى موقع جديد.

الرسم البياني المحوري هو تمثيل رسومي تفاعلي للبيانات في الجدول المحوري. تم إدخال الرسوم البيانية المحورية في إكسل 2000. باستخدام الرسم البياني المحوري يصبح أسهل فهم البيانات نظرًا لأن الجدول المحوري يقوم تلقائيًا بإنشاء المجاميع الفرعية والمجاميع.

تدعم Aspose.Cells for Python via .NET [جداول الإحاطة](/cells/ar/python-net/create-pivot-tables-and-pivot-charts/) و [رسومات الإحاطة](/cells/ar/python-net/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}

## **إضافة جداول الإحاطة والرسوم البيانية باستخدام مكتبة Aspose.Cells لـ Python Excel.**

توفر Aspose.Cells for Python via .NET مجموعة خاصة من الفصول المستخدمة لإنشاء جداول الإحاطة. تُستخدم هذه الفصول لإنشاء وتعيين كائنات PivotTable، التي تعمل كبنى أساسية لكائن PivotTable: 

- PivotField، حقل في تقرير جدول محوري.
- PivotFields، مجموعة من جميع كائنات PivotField في جدول محوري.
- PivotTable، تقرير PivotTable على صفحة العمل.
- PivotTables، مجموعة من جميع كائنات PivotTable على صفحة العمل.

### **الاستعداد لاستخدام Aspose.Cells for Python via .NET**
1. قم بتثبيت Aspose.Cells for Python via .NET من [pypi](https://pypi.org/project/aspose-cells-python/) باستخدام الأمر التالي: $ pip install aspose-cells-python.
1. يمكنك أيضًا اتباع التعليمات خطوة بخطوة حول كيفية تثبيت "Aspose.Cells for Python via .NET" في بيئة التطوير الخاصة بك.


### **كيفية إضافة جدول محوري باستخدام مكتبة Aspose.Cells for Python Excel**

لإنشاء جدول محوري باستخدام Aspose.Cells for Python via .NET:

1. أضف بعض البيانات إلى خلايا ورق العمل باستخدام طريقة put_value لكائن الخلية. يمكنك أيضًا استخدام ملف قالب مملوء بالفعل بالبيانات. ستُستخدم البيانات كمصدر بيانات الجدول المحوري.
1. أضف جدول محوري إلى ورقة العمل عن طريق استدعاء طريقة add في مجموعة PivotTables (مغلّفة في كائن الورقة).
1. الوصول إلى كائن PivotTable الجديد من مجموعة PivotTables عن طريق تمرير الفهرس الخاص به. ثم استخدم أي من كائنات جدول الجدول المحوري المحتوية في كائن PivotTable لإدارة الجدول.

تم إعطاء أمثلة الكود أدناه.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotTable-1.py" >}}

### **كيفية إضافة رسم بياني محوري باستخدام مكتبة Aspsoe.Cells for Python Excel**

لإنشاء PivotChart باستخدام Aspose.Cells for Python via .NET:

1. أضف رسم بياني.
1. قم بتعيين PivotSource للرسم البياني للإشارة إلى جدول محوري موجود في جدول البيانات.
1. قم بتعيين سمات أخرى.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotChart-1.py" >}}


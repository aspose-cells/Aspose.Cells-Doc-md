---
title: إنشاء الجداول المحورية والمخططات المحورية
type: docs
weight: 20
url: /ar/python-net/create-pivot-tables-and-pivot-charts/
description: كيفية إضافة الجداول المحورية والمخططات المحورية مع Aspose.Cells for Python via .NET.
keywords: Add Pivot Tables and Pivot Charts.
---
{{% alert color="primary" %}}

الجدول المحوري هو ملخص تفاعلي للسجلات. على سبيل المثال، قد يكون لديك مئات من إدخالات الفاتورة في قائمة في ورقة العمل. يمكن للجدول المحوري تجميع الفواتير حسب العميل أو المنتج أو التاريخ. باستخدام برنامج Excel Microsoft، من الممكن إعادة ترتيب المعلومات في الجدول المحوري بسرعة عن طريق سحب الأزرار إلى موضع جديد.

المخطط المحوري هو تمثيل رسومي تفاعلي للبيانات الموجودة في جدول محوري. تم تقديم المخططات المحورية في Excel 2000. يؤدي استخدام المخطط المحوري إلى تسهيل فهم البيانات حيث يقوم الجدول المحوري بإنشاء الإجماليات الفرعية والإجماليات تلقائيًا.

 Aspose.Cells for Python via .NET يدعم[الجداول المحورية](/cells/ar/python-net/create-pivot-tables-and-pivot-charts/) و[المخططات المحورية](/cells/ar/python-net/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}

##  **إضافة الجداول المحورية والرسوم البيانية**

Aspose.Cells for Python via .NET يوفر مجموعة خاصة من الفئات المستخدمة لإنشاء الجداول المحورية. يتم استخدام هذه الفئات لإنشاء كائنات PivotTable وتعيينها، والتي تعمل بمثابة العناصر الأساسية لكائن PivotTable:

- PivotField، حقل في تقرير الجدول المحوري.
- PivotFields، مجموعة من كافة كائنات PivotField الموجودة في جدول محوري.
- PivotTable، تقرير PivotTable على ورقة العمل.
- PivotTables، مجموعة من كافة كائنات PivotTable الموجودة في ورقة العمل.

###  **التحضير للاستخدام Aspose.Cells for Python via .NET**
1.  تثبيت Aspose.Cells for Python via .NET من[pypi](https://pypi.org/project/aspose-cells-python/)استخدم الأمر كـ: $ pip install aspose-cells-python.
1. يمكنك أيضًا اتباع الإرشادات خطوة بخطوة حول كيفية تثبيت "Aspose.Cells for Python via .NET" في بيئة المطور لديك.


###  **إضافة جدول محوري**

لإنشاء جدول محوري باستخدام Aspose.Cells for Python via .NET:

1. أضف بعض البيانات إلى خلايا ورقة العمل باستخدام طريقة put_value للكائن Cell. يمكنك أيضًا استخدام ملف قالب مملوء بالفعل بالبيانات. سيتم استخدام البيانات كمصدر بيانات الجدول المحوري.
1. قم بإضافة جدول محوري إلى ورقة العمل عن طريق استدعاء أسلوب الإضافة الخاص بمجموعة PivotTables (المغلفة في كائن ورقة العمل).
1. قم بالوصول إلى كائن PivotTable الجديد من مجموعة PivotTables عن طريق تمرير الفهرس الخاص به. # استخدم أيًا من كائنات الجدول المحوري المغلفة في كائن PivotTable لإدارة الجدول.

يتم إعطاء أمثلة التعليمات البرمجية أدناه.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotTable-1.py" >}}

###  **إضافة مخطط محوري**

لإنشاء PivotChart باستخدام Aspose.Cells for Python via .NET:

1. أضف مخططًا.
1. قم بتعيين PivotSource للمخطط للإشارة إلى جدول محوري موجود في جدول البيانات.
1. تعيين سمات أخرى.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotChart-1.py" >}}


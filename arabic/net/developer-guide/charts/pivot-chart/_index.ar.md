---
title: كيفية إضافة جدول محوري باستخدام Aspose.Cells
linktitle: مخطط محوري
type: docs
weight: 100
url: /ar/net/how-to-add-pivot-chart/
description: كيفية إضافة جدول محوري باستخدام Aspose.Cells.
keywords: PivotChart
---
## ما هو PivotChart

PivotChart في Excel هو تمثيل رسومي للبيانات تم إنشاؤه من PivotTable. يتيح للمستخدمين تصور البيانات وتحليلها ديناميكيًا من خلال تلخيص وعرض المعلومات في شكل رسوم بيانية. تكون PivotCharts تفاعلية ويمكن تعديلها بسهولة لعرض وجهات نظر مختلفة للبيانات، مما يجعلها أداة قوية لتحليل البيانات والعرض في Excel.

## كيفية إضافة جدول محوري باستخدام Aspose.Cells

### **إضافة جدول محوري**

لإنشاء جدول محوري باستخدام Aspose.Cells:

1. أضف بعض البيانات إلى خلايا ورق العمل باستخدام أسلوب PutValue/setValue لكائن الخلية. يمكنك أيضًا استخدام ملف قالب مملوء بالفعل بالبيانات. سيتم استخدام البيانات كمصدر بيانات الجدول الدوري.
1. أضف جدول محوري إلى ورقة العمل عن طريق استدعاء طريقة add في مجموعة PivotTables (مغلّفة في كائن الورقة).
1. الوصول إلى كائن PivotTable الجديد من مجموعة PivotTables عن طريق تمرير الفهرس الخاص به. ثم استخدم أي من كائنات جدول الجدول المحوري المحتوية في كائن PivotTable لإدارة الجدول.

تم إعطاء أمثلة الكود أدناه.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotTable-1.cs" >}}

### **إضافة رسم بياني دوراني**

لإنشاء PivotChart باستخدام Aspose.Cells:

1. أضف رسم بياني.
1. قم بتعيين PivotSource للرسم البياني للإشارة إلى جدول محوري موجود في جدول البيانات.
1. قم بتعيين سمات أخرى.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotChart-1.cs" >}}


---
title: كيفية إضافة PivotChart باستخدام Aspose.Cells
linktitle: مخطط بياني محوري
type: docs
weight: 100
url: /ar/net/how-to-add-pivot-chart/
description: كيفية إضافة PivotChart باستخدام Aspose.Cells.
keywords: PivotChart
---
##  ما هو التخطيط المحوري

يعد PivotChart في Excel تمثيلاً رسوميًا للبيانات التي تم إنشاؤها من PivotTable. فهو يسمح للمستخدمين بتصور البيانات وتحليلها ديناميكيًا من خلال تلخيص المعلومات وعرضها في شكل مخطط. تعتبر PivotCharts تفاعلية ويمكن تعديلها بسهولة لإظهار وجهات نظر مختلفة للبيانات، مما يجعلها أداة قوية لتحليل البيانات وعرضها في Excel.

##  كيفية إضافة PivotChart باستخدام Aspose.Cells

###  **إضافة جدول محوري**

لإنشاء جدول محوري باستخدام Aspose.Cells:

1. أضف بعض البيانات إلى خلايا ورقة العمل باستخدام أسلوب PutValue/setValue للكائن Cell. يمكنك أيضًا استخدام ملف قالب مملوء بالفعل بالبيانات. سيتم استخدام البيانات كمصدر بيانات الجدول المحوري.
1. قم بإضافة جدول محوري إلى ورقة العمل عن طريق استدعاء أسلوب الإضافة الخاص بمجموعة PivotTables (المغلفة في كائن ورقة العمل).
1. قم بالوصول إلى كائن PivotTable الجديد من مجموعة PivotTables عن طريق تمرير الفهرس الخاص به. # استخدم أيًا من كائنات الجدول المحوري المغلفة في كائن PivotTable لإدارة الجدول.

يتم إعطاء أمثلة التعليمات البرمجية أدناه.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotTable-1.cs" >}}

###  **إضافة مخطط محوري**

لإنشاء PivotChart باستخدام Aspose.Cells:

1. أضف مخططًا.
1. قم بتعيين PivotSource للمخطط للإشارة إلى جدول محوري موجود في جدول البيانات.
1. تعيين سمات أخرى.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotChart-1.cs" >}}


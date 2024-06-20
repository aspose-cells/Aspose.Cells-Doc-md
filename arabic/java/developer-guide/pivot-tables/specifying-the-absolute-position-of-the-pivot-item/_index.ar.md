---
title: تحديد الموقع المطلق لبند جدول الإحصائيات المحورية
type: docs
weight: 40
url: /ar/java/specifying-the-absolute-position-of-the-pivot-item/
---

{{% alert color="primary" %}}

أحيانًا ، يحتاج المستخدم إلى تحديد الموقع المطلق لعناصر جدول الإحصائيات المحورية ، API لـ Aspose.Cells قد فتحت خصائص وطريقة جديدة لتحقيق هذه الاحتياجات.

- تمت إضافة [**PivotItem.setPosition()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#Position) الخاصية التي يمكن استخدامها لتحديد مؤشر الموقع في كافة PivotItems بغض النظر عن العقدة الأم. تمت إضافة [**PivotItem.setPositionInSameParentNode()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#PositionInSameParentNode) للخاصية التي يمكن استخدامها لتحديد مؤشر الموقع في PivotItems تحت نفس العقدة الأم.
- تمت إضافة الطريقة [**PivotItem.move(int count, boolean isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move(int,%20boolean)) من أجل نقل العنصر لأعلى أو لأسفل استنادًا إلى قيمة العدد، حيث يكون العدد هو عدد المواقف التي يجب نقل عنصر الجدول المحوري لأعلى أو لأسفل. إذا كانت قيمة العدد أقل من الصفر، فسيتم نقل العنصر لأعلى بينما إذا كانت قيمة العدد أكبر من الصفر، فسيتم نقل عنصر الجدول المحوري لأسفل، طراز البيانات المنطقية هو الباراميتر الذي يحدد ما إذا كان يجب تنفيذ عملية النقل في نفس عقد الأصل أم لا.
- تم إهمال الطريقة *PivotItem.move(int count)*، لذا يُقترح استخدام الطريقة المضافة حديثًا [**PivotItem.move(int count, boolean isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move(int,%20boolean)) بدلاً من ذلك.

يرجى ملاحظة أنه من الضروري استدعاء الطريقة [**PivotTable.refreshData**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#refreshData--) و [**PivotTable.calculateData**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#calculateData--) قبل استخدام [**PivotItem.setPosition()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#Position)، خصائص [**PivotItem.setPositionInSameParentNode()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#PositionInSameParentNode) و [**PivotItem.move(int count, boolean isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move(int,%20boolean)).

{{% /alert %}}

## كود عينة

يقوم الكود العينة التالي بإنشاء جدول إحصائيات محوري ومن ثم يُحدد مواقع عناصر الجدول المحوري في نفس العقدة الأم.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SpecifyAbsolutePositionOfPivotItem-SpecifyAbsolutePositionOfPivotItem.java" >}}

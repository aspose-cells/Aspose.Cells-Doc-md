---
title: البحث عن البيانات باستخدام القيم الأصلية
type: docs
weight: 540
url: /ar/java/search-data-using-original-values/
---

{{% alert color="primary" %}} 

في بعض الأحيان يتم إخفاء قيمة البيانات لأنها مكتوبة بشكل معين. على سبيل المثال، لنفترض أن خلية D4 بها صيغة =Sum(A1:A2) وقيمتها هي 20 ولكنها مكتوبة على شكل ---، في هذه الحالة، تم إخفاء القيمة 20 ولا يمكن العثور عليها باستخدام خيارات البحث في Microsoft Excel. ومع ذلك، يمكنك العثور عليها باستخدام Aspose.Cells باستخدام [LookInType.ORIGINAL_VALUES](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#ORIGINAL_VALUES)

{{% /alert %}} 
## **البحث عن البيانات باستخدام القيم الأصلية**
الكود العيني التالي يوضح النقطة المذكورة أعلاه. يعثر على الخلية D4 التي لا يمكن العثور عليها باستخدام خيارات البحث في Microsoft Excel ولكن Aspose.Cells يمكنها أن تعثر عليها باستخدام [LookInType.ORIGINAL_VALUES](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#ORIGINAL_VALUES). يرجى قراءة التعليقات داخل الكود لمزيد من المعلومات.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SearchDataUsingOriginalValues-SearchDataUsingOriginalValues.java" >}}
## **مخرجات الوحدة**
فيما يلي مخرجات وحدة الإدخال الخاصة بالكود المصدري أعلاه.

{{< highlight java >}}

 Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]

{{< /highlight >}}

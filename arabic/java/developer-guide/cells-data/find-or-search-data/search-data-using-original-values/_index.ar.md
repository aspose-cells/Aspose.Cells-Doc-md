---
title: البحث عن البيانات باستخدام القيم الأصلية
type: docs
weight: 540
url: /ar/java/search-data-using-original-values/
---

{{% alert color="primary" %}} 

أحيانًا يكون قيمة البيانات مخفية لأنها مُنسقة بطريقة ما. على سبيل المثال، افترض أن الخلية D4 تحتوي على الصيغة =Sum(A1:A2) وقيمتها 20 لكنها منسقة كـ ---، إذًا، القيمة 20 مخفية ولا يمكن العثور عليها باستخدام خيارات البحث في Microsoft Excel. ومع ذلك، يمكنك إيجادها باستخدام Aspose.Cells باستخدام [LookInType.ORIGINAL_VALUES](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#ORIGINAL-VALUES)

{{% /alert %}} 
## **البحث عن البيانات باستخدام القيم الأصلية**
يوضح الكود النموذجي التالي النقطة أعلاه. يجد الخلية D4 التي لا يمكن العثور عليها باستخدام خيارات البحث في Microsoft Excel ولكن يمكن لـ Aspose.Cells العثور عليها باستخدام [LookInType.ORIGINAL_VALUES](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#ORIGINAL-VALUES). يرجى قراءة التعليقات داخل الكود للمزيد من المعلومات.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SearchDataUsingOriginalValues-SearchDataUsingOriginalValues.java" >}}
## **مخرجات الوحدة**
فيما يلي مخرجات وحدة الإدخال الخاصة بالكود المصدري أعلاه.

{{< highlight java >}}

 Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}

---
title: البحث في البيانات باستخدام القيم الأصلية
type: docs
weight: 540
url: /ar/java/search-data-using-original-values/
---
{{% alert color="primary" %}} 

 في بعض الأحيان تكون قيمة البيانات مخفية لأنها منسقة بطريقة ما. على سبيل المثال ، افترض أن الخلية D4 تحتوي على الصيغة = Sum (A1: A2) وقيمتها 20 ولكن تم تنسيقها كـ --- ، ثم القيمة 20 مخفية ولا يمكن العثور عليها باستخدام خيارات البحث عن Excel Microsoft. ومع ذلك ، يمكنك العثور عليه باستخدام Aspose.Cells باستخدام[LookInType.ORIGINAL_VALUES](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#ORIGINAL_VALUES)

{{% /alert %}} 
## **البحث في البيانات باستخدام القيم الأصلية**
 يوضح نموذج التعليمات البرمجية التالي النقطة أعلاه. يعثر على الخلية D4 التي لا يمكن العثور عليها باستخدام Microsoft خيارات البحث عن Excel ولكن يمكن لـ Aspose.Cells العثور عليها باستخدام[LookInType.ORIGINAL_VALUES](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#ORIGINAL_VALUES). يرجى قراءة التعليقات داخل الكود لمزيد من المعلومات.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SearchDataUsingOriginalValues-SearchDataUsingOriginalValues.java" >}}
## **إخراج وحدة التحكم**
هنا هو إخراج وحدة التحكم من نموذج التعليمات البرمجية أعلاه.

{{< highlight "java" >}}

 Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]{{< /highlight >}}

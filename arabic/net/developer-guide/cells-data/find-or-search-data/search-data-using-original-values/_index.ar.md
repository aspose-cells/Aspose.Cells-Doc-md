---
title: البحث في البيانات باستخدام القيم الأصلية
type: docs
weight: 380
url: /ar/net/search-data-using-original-values/
---
{{% alert color="primary" %}}

 في بعض الأحيان تكون قيمة البيانات مخفية لأنها منسقة بطريقة ما. على سبيل المثال ، افترض أن الخلية D4 تحتوي على الصيغة = Sum (A1: A2) وقيمتها 20 ولكن تم تنسيقها كـ --- ، ثم القيمة 20 مخفية ولا يمكن العثور عليها باستخدام خيارات البحث عن Excel Microsoft. ومع ذلك ، يمكنك العثور عليه باستخدام Aspose.Cells باستخدام[**LookInType.OriginalValues**](https://reference.aspose.com/cells/net/aspose.cells/lookintype)

{{% /alert %}}

 يوضح نموذج التعليمات البرمجية التالي النقطة أعلاه. يعثر على الخلية D4 التي لا يمكن العثور عليها باستخدام Microsoft خيارات البحث عن Excel ولكن يمكن لـ Aspose.Cells العثور عليها باستخدام[**LookInType.OriginalValues**](https://reference.aspose.com/cells/net/aspose.cells/lookintype). يرجى قراءة التعليقات داخل الكود لمزيد من المعلومات.

## C# كود للبحث عن البيانات باستخدام القيم الأصلية

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-SearchDataUsingOriginalValues-SearchDataUsingOriginalValues.cs" >}}

## ناتج وحدة التحكم التي تم إنشاؤها بواسطة نموذج التعليمات البرمجية

هنا هو إخراج وحدة التحكم من نموذج التعليمات البرمجية أعلاه.

{{< highlight "java" >}}

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]{{< /highlight >}}

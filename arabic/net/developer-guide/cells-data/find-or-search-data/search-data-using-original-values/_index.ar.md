---
title: البحث عن البيانات باستخدام القيم الأصلية
type: docs
weight: 380
url: /ar/net/search-data-using-original-values/
description: تعرف على كيفية البحث عن البيانات باستخدام القيم الأصلية من خلال Aspose.Cells for .NET API.
keywords: Search Data using Original Values, Find Data using Original Values, Search Data by Original Values, Find Data by Original Values
---
{{% alert color="primary" %}}

 في بعض الأحيان تكون قيمة البيانات مخفية لأنها منسقة بطريقة ما. على سبيل المثال، لنفترض أن الخلية D4 تحتوي على الصيغة =Sum(A1:A2) وقيمتها هي 20 ولكن تم تنسيقها كـ ---، فإن القيمة 20 مخفية ولا يمكن العثور عليها باستخدام خيارات البحث في Excel Microsoft. ومع ذلك، يمكنك العثور عليه باستخدام Aspose.Cells باستخدام[**LookInType.OriginalValues**](https://reference.aspose.com/cells/net/aspose.cells/lookintype)

{{% /alert %}}

 يوضح نموذج التعليمات البرمجية التالي النقطة المذكورة أعلاه. يعثر على الخلية D4 التي لا يمكن العثور عليها باستخدام Microsoft خيارات البحث في Excel ولكن Aspose.Cells يمكنه العثور عليها باستخدام[**LookInType.OriginalValues**](https://reference.aspose.com/cells/net/aspose.cells/lookintype). يرجى قراءة التعليقات داخل الكود لمزيد من المعلومات.

##  C# كود للبحث عن البيانات باستخدام القيم الأصلية

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-SearchDataUsingOriginalValues-SearchDataUsingOriginalValues.cs" >}}

## إخراج وحدة التحكم التي تم إنشاؤها بواسطة نموذج التعليمات البرمجية

هنا هو إخراج وحدة التحكم لنموذج التعليمات البرمجية أعلاه.

{{< highlight "java" >}}

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]

{{< /highlight >}}

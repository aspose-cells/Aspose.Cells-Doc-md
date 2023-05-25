---
title: احذف الصفوف والأعمدة الفارغة في ورقة عمل
type: docs
weight: 300
url: /ar/net/delete-blank-rows-and-columns-in-a-worksheet/
---
{{% alert color="primary" %}}

من الممكن حذف جميع الصفوف والأعمدة الفارغة من ورقة العمل. يكون هذا مفيدًا ، على سبيل المثال ، عند إنشاء ملف PDF من ملف Excel Microsoft وتريد تحويل الصفوف والأعمدة التي تحتوي على بيانات أو كائن مرتبط فقط.

استخدم الطرق Aspose.Cells التالية لحذف الصفوف والأعمدة الفارغة:

1.  لحذف الصفوف الفارغة ، استخدم ملف[**Cells.DeleteBlankRows ()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleteblankrows) طريقة. يرجى ملاحظة أنه بالنسبة للصفوف الفارغة التي سيتم حذفها ، لا يلزم ذلك فقط[**صف ، بلانك**](https://reference.aspose.com/cells/net/aspose.cells/row/isblank/) يجب أن تكون صحيحة ، ولكن يجب أيضًا ألا يكون هناك تعليق مرئي محدد لأي خلية في تلك الصفوف ، ولا يوجد جدول محوري يتقاطع نطاقها معها.
1.  لحذف الأعمدة الفارغة ، استخدم ملف[**Cells.DeleteBlankColumns ()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleteblankcolumns) طريقة.

{{% /alert %}}

##  C# كود لحذف الصفوف الفارغة

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DeleteBlankRowsColumns-DeletingBlankRows-1.cs" >}}

##  C# كود لحذف الأعمدة الفارغة

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DeleteBlankRowsColumns-DeletingBlankColumns-1.cs" >}}

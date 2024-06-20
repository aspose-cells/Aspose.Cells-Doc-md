---
title: حذف الصفوف والأعمدة الفارغة في ورقة العمل
type: docs
weight: 300
url: /ar/net/delete-blank-rows-and-columns-in-a-worksheet/
---

{{% alert color="primary" %}}

من الممكن حذف جميع الصفوف والأعمدة الفارغة من ورقة العمل. هذا مفيد عندما ترغب في إنشاء ملف PDF من ملف Microsoft Excel وترغب في تحويل الصفوف والأعمدة التي تحتوي على بيانات أو كائن مرتبط فقط.

استخدم وسائل Aspose.Cells التالية لحذف الصفوف والأعمدة الفارغة:

1. لحذف الصفوف الفارغة، استخدم الطريقة [**Cells.DeleteBlankRows()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleteblankrows). يرجى ملاحظة أنه من الضروري للصفوف الفارغة التي سيتم حذفها أن يكون [**Row.IsBlank**](https://reference.aspose.com/cells/net/aspose.cells/row/isblank/) صحيحًا، وأيضًا يجب ألا يكون هناك تعليق مرئي معرف لأي خلية في تلك الصفوف، ولا جدول محوري يتقاطع نطاقه معها.
1. لحذف الأعمدة الفارغة، استخدم الطريقة [**Cells.DeleteBlankColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleteblankcolumns).

{{% /alert %}}

## كود C# لحذف الصفوف الفارغة

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DeleteBlankRowsColumns-DeletingBlankRows-1.cs" >}}

## كود C# لحذف الأعمدة الفارغة

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DeleteBlankRowsColumns-DeletingBlankColumns-1.cs" >}}

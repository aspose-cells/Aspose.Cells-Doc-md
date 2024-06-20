---
title: حذف الصفوف والأعمدة الفارغة في ورقة العمل
type: docs
weight: 300
url: /ar/python-net/delete-blank-rows-and-columns-in-a-worksheet/
description: يصف هذا المقال كيفية حذف الصفوف والأعمدة الفارغة في ورقة العمل باستخدام Aspose.Cells لمكتبة Python via .NET.
keywords: مكتبة Python Excel, حذف الصفوف الفارغة بواسطة Python, إزالة الصفوف الفارغة بواسطة Python, حذف الأعمدة الفارغة بواسطة Python, إزالة الأعمدة الفارغة بواسطة Python, حذف أو إزالة الصفوف والأعمدة الفارغة بواسطة Python.
---

{{% alert color="primary" %}}

من الممكن حذف جميع الصفوف والأعمدة الفارغة من ورقة العمل. هذا مفيد عندما ترغب في إنشاء ملف PDF من ملف Microsoft Excel وترغب في تحويل الصفوف والأعمدة التي تحتوي على بيانات أو كائن مرتبط فقط.

استخدم وسائل Aspose.Cells التالية لحذف الصفوف والأعمدة الفارغة:

1. لحذف الصفوف الفارغة، استخدم الطريقة [**Cells.delete_blank_rows()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_blank_rows). يرجى ملاحظة أنه من الضروري للصفوف الفارغة التي سيتم حذفها أن يكون [**Row.is_blank**](https://reference.aspose.com/cells/python-net/aspose.cells/row/is_blank/) صحيحًا، وأيضًا يجب ألا يكون هناك تعليق مرئي معرف لأي خلية في تلك الصفوف، ولا جدول محوري يتقاطع نطاقه معها.
1. لحذف الأعمدة الفارغة، استخدم الطريقة [**Cells.delete_blank_columns()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_blank_columns).

{{% /alert %}}

## كود C# لحذف الصفوف الفارغة

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-DeletingBlankRows-1.py" >}}

## كود C# لحذف الأعمدة الفارغة

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-DeletingBlankColumns-1.py" >}}

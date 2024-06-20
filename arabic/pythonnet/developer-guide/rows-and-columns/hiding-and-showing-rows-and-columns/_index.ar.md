---
title: إخفاء وعرض الصفوف والأعمدة
type: docs
weight: 60
url: /ar/python-net/hiding-and-showing-rows-and-columns/
description: توضح هذه المقالة كيفية إخفاء وإظهار الصفوف والأعمدة باستخدام Aspose.Cells for Python via .NET API.
keywords: مكتبة Excel Python، Aspose.Cells Python إخفاء وإظهار الصفوف، Python إخفاء وإظهار الأعمدة، Python إخفاء الصفوف والأعمدة، Python إظهار الصفوف والأعمدة.
---

{{% alert color="primary" %}}

في بعض الأحيان، من المنطق إخفاء صفوف أو أعمدة معينة في ورقة عمل وعرضها لاحقًا. يوفر Microsoft Excel هذه الميزة وكذلك Aspose.Cells for Python via .NET.

{{% /alert %}}

## **التحكم في رؤية الصفوف والأعمدة**

يوفر Aspose.Cells for Python via .NET فئة، [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)، التي تمثل ملف Microsoft Excel. تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) على [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) يسمح للمطورين بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بالفئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) مجموعة [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) تمثل جميع الخلايا في ورقة العمل. توفر مجموعة [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) عدة أساليب لإدارة الصفوف أو الأعمدة في ورقة عمل. يتم مناقشة بعض هذه الأساليب أدناه.

## **كيفية إخفاء الصفوف والأعمدة**

يمكن للمطورين إخفاء صف أو عمود عن طريق استدعاء طرق [**hide_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_row/) و[**hide_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_column/) من مجموعة [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) على التوالي. تأخذ كلا الطريقين فهم فهرس الصف والعمود كمعلمة لإخفاء الصف أو العمود المحدد.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Hiding-HidingRowsAndColumns-1.py" >}}

{{% alert color="primary" %}}

من الممكن أيضًا إخفاء صف أو عمود عن طريق تعيين ارتفاع الصف أو عرض العمود إلى 0 على التوالي.

{{% /alert %}}

## **كيفية إظهار الصفوف والأعمدة**

يمكن للمطورين عرض أي صف أو عمود مخفي عن طريق استدعاء طرق [**unhide_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_row/) و[**unhide_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_column/) من مجموعة [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) على التوالي. تأخذ كلا الطريقين معلمتين:

- **فهرس الصف أو العمود** - فهرس الصف أو العمود المستخدم لعرض الصف أو العمود المحدد.
- **ارتفاع الصف أو عرض العمود** - ارتفاع الصف أو عرض العمود المعين للصف أو العمود بعد عرضه.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Hiding-UnhidingRowsAndColumns-1.py" >}}

{{% alert color="primary" %}}

أثناء جعل العمود المخفي مرئيًا، إذا كنت بحاجة إلى استعادته إلى العرض المعين سابقًا أو إلى عرضه الأصلي، يرجى عرض العمود بعرض سلبي. على سبيل المثال: worksheet.Cells.UnhideColumn(5, -1)

{{% /alert %}}

## **كيفية إخفاء صفوف وأعمدة متعددة**

يمكن للمطورين إخفاء عدة صفوف أو أعمدة دفعة واحدة عن طريق استدعاء طرق [**hide_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_rows/) و[**hide_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_columns/) من مجموعة [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) على التوالي. تأخذ كلا الطريقين فهرس الصف أو العمود البدء وعدد الصفوف أو الأعمدة التي يجب إخفاؤها كمعلمات.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.py" >}}

{{% alert color="primary" %}}

من الممكن أيضًا استخدام طرق [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) و[**unhide_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_rows/) فئة [**unhide_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_columns/) لجعل عدة صفوف وأعمدة مرئية.

{{% /alert %}}

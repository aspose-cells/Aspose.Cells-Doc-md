---
title: إدارة فواصل الصفحات
type: docs
weight: 30
url: /ar/python-net/managing-page-breaks/
description: يوفر هذا المقال رمز العينة ويشرح كيفية إضافة استراحات الصفحات، ومسح استراحات الصفحات، أو حذف استراحات الصفحات المحددة في ورقات العمل في Excel برمجيًا باستخدام Aspose.Cells for Python via .NET API.
keywords: مكتبة بايثون لإكسل، فواصل صفحات بايثون، فواصل صفحات إكسل باستخدام بايثون، حذف فاصل صفحة بـ Python.
---

{{% alert color="primary" %}}

وفقًا للتعريف، فإن فاصل الصفحة هو المكان في تدفق النص حيث تنتهي صفحة وتبدأ الصفحة التالية. يتيح Microsoft Excel للمستخدمين إضافة فواصل صفحات في أي خلية محددة من ورقة العمل.

مكان الخلية التي يتم فيها إضافة استراحة الصفحة، ينتهي الصفحة ويتم طباعة بقية البيانات بعد استراحة الصفحة على الصفحة التالية أثناء الطباعة. ببساطة، تقسم استراحات الصفحات ورقة العمل الخاصة بك إلى عدة صفحات وفقًا لمواصفاتك. يمكنك أيضًا إضافة استراحات الصفحات إلى ورقات العمل الخاصة بك أثناء التشغيل باستخدام Aspose.Cells for Python via .NET. يسمح Aspose.Cells for Python via .NET للمطورين بإضافة نوعين من استراحات الصفحات:

- فاصل صفحات أفقي
- فاصل صفحات عمودي

في بقية النقاش، سنصف كيف يمكنك إضافة استراحات صفحة أفقية أو رأسية إلى ورقات العمل الخاصة بك باستخدام Aspose.Cells for Python via .NET.

{{% /alert %}}

## **كسرات الصفحة**

Aspose.Cells for Python via .NET يوفر [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) فئة تمثل ملف إكسل. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) التي تسمح بالوصول إلى كل ورقة في ملف Excel.

يتم تمثيل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) مجموعة واسعة من الخصائص والأساليب المستخدمة لإدارة ورقة العمل.

لإضافة كسر الصفحة، استخدم خصائص [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) للفئة والخصائص [**horizontal_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/horizontal_page_breaks).

الخصائص [**horizontal_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/horizontal_page_breaks) و [**vertical_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/vertical_page_breaks) هي مجموعات قد تحتوي على العديد من كسر الصفحة. تحتوي كل مجموعة على العديد من الطرق لإدارة كسر الصفحة الأفقي والعمودي.

## **كيفية إضافة فواصل الصفحات**

لإضافة فاصل صفحة في ورقة عمل، أدخل فواصل الصفحات الرأسية والأفقية في الخلية المحددة عند استدعاء الطرق [**HorizontalPageBreakCollection.add()**](https://reference.aspose.com/cells/python-net/aspose.cells/horizontalpagebreakcollection/add/#str) و [**VerticalPageBreakCollection.add()**](https://reference.aspose.com/cells/python-net/aspose.cells/verticalpagebreakcollection/add/#str). تأخذ كل طريقة **إضافة** اسم الخلية التي يجب إضافة الفاصل فيها.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-AddingPageBreaks-1.py" >}}

{{% alert color="primary" %}}

في وضع معاينة كسر الصفحة أو معاينة الطباعة، يمكنك رؤية كيف تعمل هذه الكسور.

{{% /alert %}}


## **مهم معرفته**

عند ضبط خصائص **تناسب الصفحات** (أي [**fit_to_pages_tall**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/fit_to_pages_tall) و [**fit_to_pages_wide**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/fit_to_pages_wide)) في إعدادات تكوين الصفحة، يتأثر إعدادات كسر الصفحة، لذلك، إذا قمت بطباعة ورقة العمل، فإن إعدادات كسر الصفحة لا تعتبر على الرغم من أنها ما زالت مضبوطة.

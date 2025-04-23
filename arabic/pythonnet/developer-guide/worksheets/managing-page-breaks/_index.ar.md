---
title: إدارة فواصل الصفحات
type: docs
weight: 30
url: /ar/python-net/managing-page-breaks/
description: يوضح هذا المقال رمزاً نمذجياً ويشرح كيفية إضافة فواصل صفحات، مسح فواصل الصفحات، أو حذف فواصل صفحات محددة في أوراق عمل إكسل برمجياً باستخدام API لـ Aspose.Cells لبايثون via .NET.
keywords: مكتبة إكسل بايثون، فواصل صفحات، فواصل الصفحات في إكسل، مسح فاصل صفحة في بايثون.
---

{{% alert color="primary" %}}

وفقًا للتعريف، فإن فاصل الصفحة هو المكان في تدفق النص حيث تنتهي صفحة وتبدأ الصفحة التالية. يتيح Microsoft Excel للمستخدمين إضافة فواصل صفحات في أي خلية محددة من ورقة العمل.

يقع فاصل الصفحة الذي تتم إضافته على الخلية، حيث ينتهي الصفحة ويُطبع باقي البيانات التي بعد فاصل الصفحة في الصفحة التالية أثناء الطباعة. ببساطة، فواصل الصفحات تقسم ورقة العمل إلى صفحات متعددة وفقًا لمواصفاتك. يمكنك أيضاً إضافة فواصل صفحات لورقة العمل الخاصة بك أثناء التشغيل باستخدام Aspose.Cells لبايثون via .NET. تتيح Aspose.Cells لبايثون via .NET للمطورين إضافة نوعين من فواصل الصفحات:

- فاصل صفحات أفقي
- فاصل صفحات عمودي

في بقية المناقشة، سنشرح كيف يمكنك إضافة فواصل صفحات أفقية أو عمودية إلى أوراق العمل الخاصة بك باستخدام Aspose.Cells لبايثون via .NET.

{{% /alert %}}

## **كسرات الصفحة**

توفر Aspose.Cells لبايثون via .NET فئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) التي تمثل ملف إكسل. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) التي تتيح الوصول إلى كل ورقة عمل داخل ملف الإكسل.

يتم تمثيل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) مجموعة واسعة من الخصائص والأساليب المستخدمة لإدارة ورقة العمل.

لإضافة كسر الصفحة، استخدم خصائص [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) للفئة والخصائص [**horizontal_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/horizontal_page_breaks).

الخصائص [**horizontal_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/horizontal_page_breaks) و [**vertical_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/vertical_page_breaks) هي مجموعات قد تحتوي على العديد من كسر الصفحة. تحتوي كل مجموعة على العديد من الطرق لإدارة كسر الصفحة الأفقي والعمودي.

## **كيفية إضافة فواصل صفحات**

لإضافة فاصل صفحة في ورقة عمل، قم بإدراج فواصل صفحة أفقية وعمودية عند الخلية المحددة باستخدام استدعاء طريقتي [**HorizontalPageBreakCollection.add()**](https://reference.aspose.com/cells/python-net/aspose.cells/horizontalpagebreakcollection/add/#str) و [**VerticalPageBreakCollection.add()**](https://reference.aspose.com/cells/python-net/aspose.cells/verticalpagebreakcollection/add/#str). كل طريقة **إضافة** تأخذ اسم الخلية التي يجب إضافة الفاصل إليها.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-AddingPageBreaks-1.py" >}}

{{% alert color="primary" %}}

في وضع معاينة كسر الصفحة أو معاينة الطباعة، يمكنك رؤية كيف تعمل هذه الكسور.

{{% /alert %}}


## **مهم معرفته**

عند ضبط خصائص **تناسب الصفحات** (أي [**fit_to_pages_tall**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/fit_to_pages_tall) و [**fit_to_pages_wide**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/fit_to_pages_wide)) في إعدادات تكوين الصفحة، يتأثر إعدادات كسر الصفحة، لذلك، إذا قمت بطباعة ورقة العمل، فإن إعدادات كسر الصفحة لا تعتبر على الرغم من أنها ما زالت مضبوطة.

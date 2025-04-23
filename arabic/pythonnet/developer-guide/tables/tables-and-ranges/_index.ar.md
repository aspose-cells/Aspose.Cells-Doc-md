---
title: الجداول والنطاقات
type: docs
weight: 50
url: /ar/python-net/tables-and-ranges/
---

## **مقدمة**

أحيانًا تقوم بإنشاء جدول في برنامج Microsoft Excel ولا ترغب في الاستمرار في استخدام وظائف الجدول الخاصة به. بدلاً من ذلك، ترغب في شيء يبدو وكأنه جدول. للحفاظ على البيانات في جدول دون فقدان التنسيق، قم بتحويل الجدول إلى نطاق عادي من البيانات.
يدعم Aspose.Cells لبايثون via .NET هذه الميزة من ميكروسوفت إكسل للجداول والكائنات القائمة.

## **استخدام Microsoft Excel**

استخدم ميزة **تحويل إلى نطاق** لتحويل الجدول إلى نطاق بسرعة دون فقدان التنسيق. في Microsoft Excel 2007/2010:

1. انقر في أي مكان في الجدول للتأكد من أن الخلية النشطة في عمود الجدول.
1. في علامة التبويب **التصميم**، في مجموعة **الأدوات**، انقر فوق **تحويل إلى نطاق**.

## **باستخدام Aspose.Cells لبايثون via .NET**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Tables-ConvertTableToRange-1.py" >}}

{{% alert color="primary" %}}

لا تعود ميزات الجداول متاحة بعد تحويل الجدول إلى نطاق. على سبيل المثال، لم تعد رؤوس الصفوف تحتوي على السهام للفرز والتصفية، والإشارات المنظمة (المشار إليها باستخدام أسماء الجدول) التي تم استخدامها في الصيغ تتحول إلى مراجع خلية عادية.

{{% /alert %}}

## **تحويل الجدول إلى نطاق بخيارات**

يوفر Aspose.Cells لبايثون via .NET خيارات إضافية أثناء تحويل جدول إلى نطاق عبر فئة [**TableToRangeOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/tabletorangeoptions). تقدم فئة [**TableToRangeOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/tabletorangeoptions) خاصية [**last_row**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/tabletorangeoptions/last_row/) التي تتيح لك ضبط الفهرس النهائي لصف الجدول. سيتم الاحتفاظ بتنسيق الجدول حتى الفهرس المحدد وسُيُزال باقي التنسيق.

يظهر الشيفرة المثالية أدناه كيفية استخدام الفئة [**TableToRangeOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/tabletorangeoptions).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Tables-ConvertTableToRangeWithOptions-1.py" >}}


---
title: الجداول والنطاقات
type: docs
weight: 50
url: /ar/net/tables-and-ranges/
---

## **مقدمة**

أحيانًا تقوم بإنشاء جدول في برنامج Microsoft Excel ولا ترغب في الاستمرار في استخدام وظائف الجدول الخاصة به. بدلاً من ذلك، ترغب في شيء يبدو وكأنه جدول. للحفاظ على البيانات في جدول دون فقدان التنسيق، قم بتحويل الجدول إلى نطاق عادي من البيانات.
يدعم Aspose.Cells هذه الميزة في برنامج Microsoft Excel للجداول وكائنات القوائم.

## **استخدام Microsoft Excel**

استخدم ميزة **تحويل إلى نطاق** لتحويل الجدول إلى نطاق بسرعة دون فقدان التنسيق. في Microsoft Excel 2007/2010:

1. انقر في أي مكان في الجدول للتأكد من أن الخلية النشطة في عمود الجدول.
1. في علامة التبويب **التصميم**، في مجموعة **الأدوات**، انقر فوق **تحويل إلى نطاق**.

## **استخدام Aspose.Cells**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-ConvertTableToRange-1.cs" >}}

{{% alert color="primary" %}}

لا تعود ميزات الجداول متاحة بعد تحويل الجدول إلى نطاق. على سبيل المثال، لم تعد رؤوس الصفوف تحتوي على السهام للفرز والتصفية، والإشارات المنظمة (المشار إليها باستخدام أسماء الجدول) التي تم استخدامها في الصيغ تتحول إلى مراجع خلية عادية.

{{% /alert %}}

## **تحويل الجدول إلى نطاق بخيارات**

يوفر Aspose.Cells خيارات إضافية أثناء تحويل الجدول إلى نطاق من خلال فئة [**TableToRangeOptions**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions). توفر الفئة [**TableToRangeOptions**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions) خاصية [**LastRow**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions/properties/lastrow) التي تتيح لك تعيين الفهرس الأخير لصف الجدول. سيتم الاحتفاظ بتنسيق الجدول حتى الفهرس المحدد لصف، وسيتم إزالة بقية التنسيق.

يظهر الشيفرة المثالية أدناه كيفية استخدام الفئة [**TableToRangeOptions**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-ConvertTableToRangeWithOptions-1.cs" >}}

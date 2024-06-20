---
title: تحويل جدول Excel إلى مجموعة من البيانات
type: docs
weight: 10
url: /ar/java/convert-an-excel-table-to-a-range-of-data/
---

{{% alert color="primary" %}}

أحيانًا تقوم بإنشاء جدول في برنامج Microsoft Excel ولا ترغب في الاستمرار في استخدام وظائف الجدول الخاصة به. بدلاً من ذلك، ترغب في شيء يبدو وكأنه جدول. للحفاظ على البيانات في جدول دون فقدان التنسيق، قم بتحويل الجدول إلى نطاق عادي من البيانات.

تدعم Aspose.Cells هذه الميزة في Microsoft Excel للجداول وكائنات القوائم.

{{% /alert %}}

## **استخدام Microsoft Excel**

استخدم ميزة **تحويل إلى نطاق** لتحويل الجدول إلى نطاق بسرعة دون فقدان التنسيق. في Microsoft Excel 2007/2010:

1. انقر في أي مكان في الجدول للتأكد من أن الخلية النشطة في عمود الجدول.

![todo:image_alt_text](convert-an-excel-table-to-a-range-of-data_1.gif)

1. في علامة التبويب **التصميم**، في مجموعة **الأدوات**، انقر فوق **تحويل إلى نطاق**.

![todo:image_alt_text](convert-an-excel-table-to-a-range-of-data_2.gif)

{{% alert color="primary" %}}

لا تعود ميزات الجداول متاحة بعد تحويل الجدول إلى نطاق. على سبيل المثال، لم تعد رؤوس الصفوف تحتوي على السهام للفرز والتصفية، والإشارات المنظمة (المشار إليها باستخدام أسماء الجدول) التي تم استخدامها في الصيغ تتحول إلى مراجع خلية عادية.

{{% /alert %}}

## **استخدام Aspose.Cells**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-ConvertTableToRange-ConvertTableToRange.java" >}}

## **تحويل الجدول إلى نطاق بخيارات**

يوفر Aspose.Cells خيارات إضافية أثناء تحويل الجدول إلى نطاق من خلال الفئة [**TableToRangeOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions). توفر الفئة [**TableToRangeOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions) خاصية [**LastRow**](https://reference.aspose.com/cells/java/com.aspose.cells/tabletorangeoptions#LastRow) التي تسمح لك بتعيين الفهرس الأخير لصف الجدول. سيتم الاحتفاظ بتنسيق الجدول حتى الفهرس المحدد لصف الجدول وسيتم إزالة بقية التنسيق.

يظهر الشيفرة المثالية أدناه كيفية استخدام الفئة [**TableToRangeOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Tables-ConvertTableToRangeWithOptions-1.java" >}}

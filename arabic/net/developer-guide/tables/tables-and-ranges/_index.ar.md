---
title: الجداول والنطاقات
type: docs
weight: 50
url: /ar/net/tables-and-ranges/
---
## **مقدمة**

في بعض الأحيان تقوم بإنشاء جدول في Microsoft Excel ولا ترغب في الاستمرار في العمل مع وظائف الجدول التي تأتي معها. بدلاً من ذلك ، تريد شيئًا يشبه الطاولة. للاحتفاظ بالبيانات في جدول دون فقد التنسيق ، قم بتحويل الجدول إلى نطاق منتظم من البيانات.
يدعم Aspose.Cells هذه الميزة من Microsoft Excel للجداول وكائنات القائمة.

## **باستخدام Microsoft إكسل**

 استخدم ال**تحويل إلى المدى** ميزة لتحويل الجدول بسرعة إلى نطاق دون فقدان التنسيق. في Microsoft Excel 2007/2010:

1. انقر في أي مكان في الجدول للتأكد من أن الخلية النشطة موجودة في عمود جدول.
1.  على ال**تصميم** علامة التبويب في**أدوات** المجموعة ، انقر فوق**تحويل إلى المدى**.

## **باستخدام Aspose.Cells**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-ConvertTableToRange-1.cs" >}}

{{% alert color="primary" %}}

لم تعد ميزات الجدول متاحة بعد تحويل الجدول إلى نطاق. على سبيل المثال ، لم تعد رؤوس الصفوف تتضمن أسهم الفرز والتصفية ، وتتحول المراجع المصنفة (المراجع التي تستخدم أسماء الجداول) التي تم استخدامها في الصيغ إلى مراجع خلايا عادية.

{{% /alert %}}

## **تحويل الجدول إلى نطاق مع خيارات**

يوفر Aspose.Cells خيارات إضافية أثناء تحويل جدول إلى نطاق عبر[**TableToRangeOptions**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions) صف دراسي. ال[**TableToRangeOptions**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions)فئة تقدم[**الصف الأخير**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions/properties/lastrow)الخاصية التي تسمح لك بتعيين الفهرس الأخير لصف الجدول. سيتم الاحتفاظ بتنسيق الجدول حتى فهرس الصف المحدد وستتم إزالة باقي التنسيق.

يوضح نموذج التعليمات البرمجية الوارد أدناه استخدام[**TableToRangeOptions**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions)صف دراسي.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-ConvertTableToRangeWithOptions-1.cs" >}}

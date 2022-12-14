---
title: تحويل جدول Excel إلى نطاق من البيانات
type: docs
weight: 10
url: /ar/java/convert-an-excel-table-to-a-range-of-data/
---
{{% alert color="primary" %}}

في بعض الأحيان تقوم بإنشاء جدول في Microsoft Excel ولا ترغب في الاستمرار في العمل مع وظائف الجدول التي تأتي معها. بدلاً من ذلك ، تريد شيئًا يشبه الطاولة. للاحتفاظ بالبيانات في جدول دون فقد التنسيق ، قم بتحويل الجدول إلى نطاق منتظم من البيانات.

يدعم Aspose.Cells هذه الميزة من Microsoft Excel للجداول وكائنات القائمة.

{{% /alert %}}

## **باستخدام Microsoft إكسل**

 استخدم ال**تحويل إلى المدى** ميزة لتحويل الجدول بسرعة إلى نطاق دون فقدان التنسيق. في Microsoft Excel 2007/2010:

1. انقر في أي مكان في الجدول للتأكد من أن الخلية النشطة موجودة في عمود جدول.

![ما يجب القيام به: image_بديل_نص](convert-an-excel-table-to-a-range-of-data_1.gif)

1.  على ال**تصميم** علامة التبويب في**أدوات** المجموعة ، انقر فوق**تحويل إلى المدى**.

![ما يجب القيام به: image_بديل_نص](convert-an-excel-table-to-a-range-of-data_2.gif)

{{% alert color="primary" %}}

لم تعد ميزات الجدول متاحة بعد تحويل الجدول إلى نطاق. على سبيل المثال ، لم تعد رؤوس الصفوف تتضمن أسهم الفرز والتصفية ، وتتحول المراجع المصنفة (المراجع التي تستخدم أسماء الجداول) التي تم استخدامها في الصيغ إلى مراجع خلايا عادية.

{{% /alert %}}

## **باستخدام Aspose.Cells**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-ConvertTableToRange-ConvertTableToRange.java" >}}

## **تحويل الجدول إلى نطاق مع خيارات**

يوفر Aspose.Cells خيارات إضافية أثناء تحويل جدول إلى نطاق عبر[**TableToRangeOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions)صف دراسي. ال[**TableToRangeOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions)فئة تقدم[**الصف الأخير**](https://reference.aspose.com/cells/java/com.aspose.cells/tabletorangeoptions#LastRow)الخاصية التي تسمح لك بتعيين الفهرس الأخير لصف الجدول. سيتم الاحتفاظ بتنسيق الجدول حتى فهرس الصف المحدد وستتم إزالة باقي التنسيق.

يوضح نموذج التعليمات البرمجية الوارد أدناه استخدام[**TableToRangeOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions)صف دراسي.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Tables-ConvertTableToRangeWithOptions-1.java" >}}

---
title: إدارة التعليقات والملاحظات
linktitle: التعليقات والملاحظات
type: docs
weight: 128
url: /ar/java/comments-and-notes/
description: إدخال وإدارة التعليقات أو الملاحظات باستخدام Aspose.Cells لجافا.
keywords: إدراج تعليقات، إدراج ملاحظات
---

## **مقدمة**

يتم استخدام التعليقات لإضافة معلومات إضافية إلى الخلايا. يوفر Aspose.Cells طريقتين لإضافة تعليقات إلى الخلايا. الأولى هي إنشاء التعليقات في ملف مصمم يدويًا. يتم استيراد هذه التعليقات بعد ذلك باستخدام Aspose.Cells. الثانية هي إضافة التعليقات باستخدام واجهة برمجة التطبيقات Aspose.Cells أثناء التشغيل. يتناول هذا الموضوع إضافة التعليقات إلى الخلايا باستخدام واجهة برمجة التطبيقات Aspose.Cells. سيتم أيضًا شرح تنسيق التعليقات.

## **إضافة تعليق**

إضافة تعليق إلى خلية عن طريق استدعاء طريقة **إضافة** لمجموعة [**Comments**](https://reference.aspose.com/cells/java/com.aspose.cells/CommentCollection) (المغلفة في [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)). يمكن الوصول إلى الكائن [**Comment**](https://reference.aspose.com/cells/java/com.aspose.cells/Comment) الجديد من مجموعة [**Comments**](https://reference.aspose.com/cells/java/com.aspose.cells/CommentCollection) عن طريق تمرير مؤشر التعليق. بعد الوصول إلى الكائن [**Comment**](https://reference.aspose.com/cells/java/com.aspose.cells/Comment)، قم بتخصيص ملاحظة التعليق باستخدام خاصية [**Note**](https://reference.aspose.com/cells/java/com.aspose.cells/comment#Note) لكائن [**Comment**](https://reference.aspose.com/cells/java/com.aspose.cells/Comment).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "AddingComment-1.java" >}}

## **تنسيق التعليق**

من الممكن أيضًا تنسيق مظهر التعليقات عن طريق تكوين ارتفاعها، وعرضها وإعدادات الخط.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "CommentFormatting-1.java" >}}

## **إضافة صورة إلى التعليق**

مع Microsoft Excel 2007، من الممكن أيضًا وضع صورة كخلفية لتعليق الخلية. في Excel 2007، يمكن القيام بذلك من خلال الخطوات التالية. (يلزم أن يكون قد تم بالفعل إضافة تعليق للخلية.)

1. انقر بزر الماوس الأيمن فوق الخلية التي تحتوي على التعليق.
1. حدد **إظهار/إخفاء التعليقات**، وامسح أي نص من التعليق.
1. انقر على الحد للتعليق لتحديده.
1. حدد **تنسيق**، ثم **تعليق**.
1. على علامة تبويب **الألوان والخطوط**، قم بتوسيع قائمة **اللون**.
1. انقر على **ملء الآثار**.
1. على علامة تبويب **الصورة**، انقر على **تحديد صورة**.
1. العثور على الصورة وتحديدها.
1. انقر على **موافق** حتى يتم إغلاق جميع الحوارات.

توفر Aspose.Cells أيضًا هذه الميزة. فيما يلي عينة من الشفرة التي تنشئ ملف XLSX من البداية، مع إضافة تعليق إلى الخلية "A1" وتعيين صورة كخلفية لها.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "AddImageToComment-1.java" >}}

## **مواضيع متقدمة**
- [تغيير اتجاه النص للتعليق](/cells/ar/java/change-text-direction-of-the-comment/)
- [كيفية تغيير لون خط التعليق](/cells/ar/java/how-to-change-the-comment-font-color/)
- [كيفية تعيين خلفية التعليق](/cells/ar/java/how-to-set-comment-background/)
- [تعليقات متداخلة](/cells/ar/java/threaded-comments/)


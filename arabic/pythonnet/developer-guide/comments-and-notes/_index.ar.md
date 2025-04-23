---
title: إدارة التعليقات والملاحظات
linktitle: التعليقات والملاحظات
type: docs
weight: 128
url: /ar/python-net/comments-and-notes/
description: إدراج وإدارة التعليقات أو الملاحظات باستخدام Aspose.Cells لـ .Net.
keywords: إدراج تعليقات، إدراج ملاحظات
---

## **مقدمة**

يتم استخدام التعليقات لإضافة معلومات إضافية إلى الخلايا. يوفر Aspose.Cells طريقتين لإضافة تعليقات إلى الخلايا. الأولى هي إنشاء التعليقات في ملف مصمم يدويًا. يتم استيراد هذه التعليقات بعد ذلك باستخدام Aspose.Cells. الثانية هي إضافة التعليقات باستخدام واجهة برمجة التطبيقات Aspose.Cells أثناء التشغيل. يتناول هذا الموضوع إضافة التعليقات إلى الخلايا باستخدام واجهة برمجة التطبيقات Aspose.Cells. سيتم أيضًا شرح تنسيق التعليقات.

## **إضافة تعليق**

أضف تعليقًا إلى خلية عن طريق استدعاء الطريقة [**add**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/add) في تجميعة [**Comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection) (المغلفة في الكائن [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)). يمكن الوصول إلى الكائن [**Comment**](https://reference.aspose.com/cells/python-net/aspose.cells/comment) الجديد من تجميعة [**Comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection) عن طريق تمرير مؤشر التعليق. بعد الوصول إلى الكائن [**Comment**](https://reference.aspose.com/cells/python-net/aspose.cells/comment)، يمكن تخصيص ملاحظة التعليق باستخدام خاصية [**note**](https://reference.aspose.com/cells/python-net/aspose.cells/comment/note) لكائن [**Comment**](https://reference.aspose.com/cells/python-net/aspose.cells/comment).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Comments-AddingComment-1.cs" >}}

## **تنسيق التعليق**

من الممكن أيضًا تنسيق مظهر التعليقات عن طريق تكوين ارتفاعها، وعرضها وإعدادات الخط.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Comments-CommentFormatting-1.cs" >}}

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

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Comments-AddImageToComment-1.cs" >}}

## **مواضيع متقدمة**
- [تغيير اتجاه النص للتعليق](/cells/ar/python-net/change-text-direction-of-the-comment/)
- [كيفية تغيير لون خط التعليق](/cells/ar/python-net/how-to-change-the-comment-font-color/)
- [كيفية تعيين خلفية التعليق](/cells/ar/python-net/how-to-set-comment-background/)
- [تعليقات متداخلة](/cells/ar/python-net/threaded-comments/)


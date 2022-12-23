---
title: إدارة التعليقات والملاحظات
linktitle: التعليقات والملاحظات
type: docs
weight: 128
url: /ar/java/comments-and-notes/
description: قم بإدراج وإدارة التعليقات أو الملاحظات باستخدام Aspose.Cells لجافا.
keywords: insert comments, insert notes
---
## **مقدمة**

تستخدم التعليقات لإضافة معلومات إضافية إلى الخلايا. يوفر Aspose.Cells طريقتين لإضافة التعقيبات إلى الخانات. الأول هو إنشاء تعليقات في ملف المصمم يدويًا. ثم يتم استيراد هذه التعليقات باستخدام Aspose.Cells. والثاني هو إضافة تعليقات باستخدام Aspose.Cells API في وقت التشغيل. يناقش هذا الموضوع إضافة التعليقات إلى الخلايا باستخدام Aspose.Cells API. سيتم أيضًا شرح تنسيق التعليقات.

## **إضافة تعليق**

 أضف تعليقًا إلى خلية عن طريق استدعاء[**تعليقات**](https://reference.aspose.com/cells/java/com.aspose.cells/CommentCollection) المجموعة**يضيف** طريقة (مغلفة في[**ورقة عمل**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) موضوع). الجديد[**تعليق**](https://reference.aspose.com/cells/java/com.aspose.cells/Comment) يمكن الوصول إلى الكائن من خلال[**تعليقات**](https://reference.aspose.com/cells/java/com.aspose.cells/CommentCollection) المجموعة عن طريق تمرير فهرس التعليقات. بعد الوصول إلى ملف[**تعليق**](https://reference.aspose.com/cells/java/com.aspose.cells/Comment) ، قم بتخصيص ملاحظة التعليق باستخدام[**تعليق**](https://reference.aspose.com/cells/java/com.aspose.cells/Comment) أشياء[**ملحوظة**](https://reference.aspose.com/cells/java/com.aspose.cells/comment#Note)خاصية.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "AddingComment-1.java" >}}

## **تنسيق التعليق**

من الممكن أيضًا تنسيق مظهر التعليقات من خلال تكوين إعدادات الطول والعرض والخط.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "CommentFormatting-1.java" >}}

## **أضف صورة للتعليق**

باستخدام Microsoft Excel 2007 ، من الممكن أيضًا الحصول على صورة كخلفية لتعليق الخلية. يتم تحقيق ذلك في Excel 2007 عن طريق القيام بالخطوات التالية. (يفترضون أنك قمت بالفعل بإضافة تعليق خلية.)

1. انقر بزر الماوس الأيمن فوق الخلية التي تحتوي على التعليق.
1.  يختار**إظهار / إخفاء التعليقات**، وامسح أي نص من التعليق.
1. انقر فوق حد التعليق لتحديده.
1.  يختار**شكل** ، ومن بعد**تعليق**.
1.  على ال**الألوان والخطوط** علامة التبويب ، قم بتوسيع**اللون** قائمة.
1.  انقر**تأثيرات التعبئة**.
1.  على ال**صورة** علامة التبويب ، انقر فوق**حدد صورة**.
1. حدد موقع الصورة وحددها.
1.  انقر**نعم** حتى يتم إغلاق جميع الحوارات.

يوفر Aspose.Cells أيضًا هذه الميزة. يوجد أدناه نموذج رمز يقوم بإنشاء ملف XLSX من البداية ، مضيفًا تعليقًا إلى الخلية "A1" مع تعيين صورة كخلفية لها.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "AddImageToComment-1.java" >}}

## **موضوعات مسبقة**
- [تغيير اتجاه النص للتعليق](/cells/ar/java/change-text-direction-of-the-comment/)
- [كيفية تغيير لون خط التعليق](/cells/ar/java/how-to-change-the-comment-font-color/)
- [كيفية تعيين خلفية التعليق](/cells/ar/java/how-to-set-comment-background/)
- [تعليقات مترابطة](/cells/ar/java/threaded-comments/)


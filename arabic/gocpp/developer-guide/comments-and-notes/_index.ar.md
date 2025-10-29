---
title: إدارة التعليقات والملاحظات باستخدام Golang عبر C++
linktitle: التعليقات والملاحظات
type: docs
weight: 128
url: /ar/go-cpp/comments-and-notes/
description: إدراج وإدارة التعليقات أو الملاحظات مع Aspose.Cells for C++.
keywords: إدراج تعليقات، إدراج ملاحظات
---

## **مقدمة**

يتم استخدام التعليقات لإضافة معلومات إضافية إلى الخلايا. يوفر Aspose.Cells طريقتين لإضافة تعليقات إلى الخلايا. الأولى هي إنشاء التعليقات في ملف مصمم يدويًا. يتم استيراد هذه التعليقات بعد ذلك باستخدام Aspose.Cells. الثانية هي إضافة التعليقات باستخدام واجهة برمجة التطبيقات Aspose.Cells أثناء التشغيل. يتناول هذا الموضوع إضافة التعليقات إلى الخلايا باستخدام واجهة برمجة التطبيقات Aspose.Cells. سيتم أيضًا شرح تنسيق التعليقات.

## **إضافة تعليق**

أضف تعليقًا إلى خلية عن طريق استدعاء الطريقة [**Add**](https://reference.aspose.com/cells/go-cpp/commentcollection/add/) في تجميعة [**Comments**](https://reference.aspose.com/cells/go-cpp/commentcollection/) (المغلفة في الكائن [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)). يمكن الوصول إلى الكائن [**Comment**](https://reference.aspose.com/cells/cpp/aspose.cells/comment/) الجديد من تجميعة [**Comments**](https://reference.aspose.com/cells/go-cpp/commentcollection/) عن طريق تمرير مؤشر التعليق. بعد الوصول إلى الكائن [**Comment**](https://reference.aspose.com/cells/cpp/aspose.cells/comment/)، يمكن تخصيص ملاحظة التعليق باستخدام خاصية [**GetNote()**](https://reference.aspose.com/cells/cpp/aspose.cells/comment/getnote/) لكائن [**Comment**](https://reference.aspose.com/cells/cpp/aspose.cells/comment/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CommentsAndNotes.go" >}}
## **تنسيق التعليق**

من الممكن أيضًا تنسيق مظهر التعليقات عن طريق تكوين ارتفاعها، وعرضها وإعدادات الخط.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CommentsAndNotes-1.go" >}}
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

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CommentsAndNotes-2.go" >}}
## **مواضيع متقدمة**
- [تغيير اتجاه النص للتعليق](/cells/ar/cpp/change-text-direction-of-the-comment/)
- [كيفية تغيير لون خط التعليق](/cells/ar/cpp/how-to-change-the-comment-font-color/)
- [كيفية تعيين خلفية التعليق](/cells/ar/cpp/how-to-set-comment-background/)
- [تعليقات متداخلة](/cells/ar/cpp/threaded-comments/)

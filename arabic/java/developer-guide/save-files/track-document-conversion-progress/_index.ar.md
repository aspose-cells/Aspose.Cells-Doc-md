---
title: تتبع تقدم تحويل المستند
type: docs
weight: 120
url: /ar/java/track-document-conversion-progress/
---
## **سيناريوهات الاستخدام الممكنة**

في بعض الأحيان ، قد يستغرق تحويل ملفات Excel الكبيرة بعض الوقت. خلال هذا الوقت ، قد ترغب في إظهار تقدم تحويل المستند بدلاً من مجرد شاشة تحميل لتحسين إمكانية استخدام التطبيق الخاص بك. Aspose.Cells يدعم تتبع عملية تحويل الوثيقة من خلال توفير**[IPageSavingCallback] (https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback)**واجهه المستخدم. ال**[IPageSavingCallback] (https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback)**يوفر واجهة**[PageStartSaving] (https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageStartSaving (com.aspose.cells.PageStartSavingArgs))**و**[PageEndSaving] (https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageEndSaving (com.aspose.cells.PageEndSavingArgs))** الطرق التي يمكنك تنفيذها في فئتك المخصصة. يمكنك أيضًا التحكم في الصفحات التي يتم عرضها كما هو موضح في ملف*TestPageSavingCallback*فئة مخصصة.

## **تتبع تقدم تحويل المستند**

نموذج التعليمات البرمجية التالي بتحميل[ملف اكسل المصدر](PagesBook1.xlsx)ويطبع تقدم التحويل في وحدة التحكم باستخدام ملف*TestPageSavingCallback*فئة مخصصة تنفذ**[IPageSavingCallback] (https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback)**واجهه المستخدم.

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgress-1.java" >}}

ما يلي هو رمز*TestPageSavingCallback*فئة مخصصة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgress-2.java" >}}

## **إخراج وحدة التحكم**

ابدأ بحفظ فهرس الصفحة 0 من الصفحات 11</br>
نهاية فهرس صفحة الحفظ 0 من الصفحات 11</br>
ابدأ بحفظ فهرس الصفحة 1 من الصفحات 11</br>
نهاية فهرس صفحة الحفظ 1 من الصفحات 11</br>
ابدأ بحفظ فهرس الصفحة 2 من الصفحات 11</br>
نهاية فهرس صفحة الحفظ 2 من الصفحات 11</br>
ابدأ بحفظ فهرس الصفحة 3 من الصفحات 11</br>
نهاية فهرس صفحة الحفظ 3 من الصفحات 11</br>
ابدأ بحفظ فهرس الصفحة 4 من الصفحات 11</br>
نهاية فهرس صفحة الحفظ 4 من الصفحات 11</br>
ابدأ بحفظ فهرس الصفحة 5 من الصفحات 11</br>
نهاية فهرس صفحة الحفظ 5 من الصفحات 11</br>
ابدأ بحفظ فهرس الصفحة 6 من الصفحات 11</br>
نهاية فهرس صفحة الحفظ 6 من الصفحات 11</br>
ابدأ بحفظ فهرس الصفحة 7 من الصفحات 11</br>
نهاية فهرس صفحة الحفظ 7 من الصفحات 11</br>
ابدأ بحفظ فهرس الصفحة 8 من الصفحات 11</br>
نهاية فهرس صفحة الحفظ 8 من الصفحات 11

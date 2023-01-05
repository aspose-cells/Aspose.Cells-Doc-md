---
title: تتبع تقدم تحويل المستند
type: docs
weight: 970
url: /ar/net/track-document-conversion-progress/
---
## **سيناريوهات الاستخدام الممكنة**

 في بعض الأحيان ، قد يستغرق تحويل ملفات Excel الكبيرة بعض الوقت. خلال هذا الوقت ، قد ترغب في إظهار تقدم تحويل المستند بدلاً من مجرد شاشة تحميل لتحسين إمكانية استخدام التطبيق الخاص بك. Aspose.Cells يدعم تتبع عملية تحويل الوثيقة من خلال توفير**[IPageSavingCallback] (https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback)** واجهه المستخدم. ال**[IPageSavingCallback] (https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback)**يوفر واجهة**[PageStartSaving] (https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback/methods/pagestartsaving)**و**[PageEndSaving] (https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback/methods/pageendsaving)**الطرق التي يمكنك تنفيذها في فئتك المخصصة. يمكنك أيضًا التحكم في الصفحات التي يتم عرضها كما هو موضح في حرف T.*estPageSavingCallback*فئة مخصصة.

## **تتبع تقدم تحويل المستند**

 نموذج التعليمات البرمجية التالي بتحميل[ملف اكسل المصدر](94896151.xlsx) ويطبع تقدم التحويل في وحدة التحكم باستخدام ملف*TestPageSavingCallback* فئة مخصصة تنفذ**[IPageSavingCallback] (https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback)**واجهه المستخدم.

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgress-1.cs" >}}

ما يلي هو رمز*TestPageSavingCallback*فئة مخصصة.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgress-2.cs" >}}

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

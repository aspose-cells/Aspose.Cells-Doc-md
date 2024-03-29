﻿---
title: فتح ملف Excel بدون فتح مربع الحوار "حفظ إلغاء"
type: docs
weight: 150
url: /ar/net/opening-excel-file-without-open-save-cancel-dialog-box/
---
{{% alert color="primary" %}} 

يشرح هذا المستند كيفية فتح ملف Excel Microsoft في مستعرض بدون إظهار مربع الحوار فتح-حفظ-إلغاء.

 وتجدر الإشارة هنا إلى أن التقييد الأمني الذي لا يسمح بالتحميل المباشر لملف يتم فرضه بواسطة Microsoft (أو بائعي المستعرضات الآخرين) ، وليس بواسطة Aspose. يتم فرض حظر وتقييد تنزيل الملفات التي يحتمل أن تكون ضارة على الأجهزة المحلية .

من الخطورة أن يسمح النظام المحلي للعميل بالتنزيل دون إظهار مربع الحوار "فتح - حفظ - إلغاء" للمطالبة بالتنزيل. لا يوجد خيار أو حل بديل متاح من Aspose لأنه سيكون مخاطرة أمنية كبيرة جدًا.

{{% /alert %}} 
## **لماذا يمثل مخاطرة أمنية؟**
تُظهر الصورة التالية مربع الحوار فتح-حفظ-إلغاء الذي يظهره Internet Explorer عند محاولة تنزيل ملف.

|**مربع الحوار فتح - حفظ - إلغاء**|
|:- |
|![ما يجب القيام به: image_بديل_نص](opening-excel-file-without-open-save-cancel-dialog-box_1.png)|
كما هو موضح أعلاه ، فإن السماح لملف بالفتح أو التشغيل على نظامك دون تأكيد أنك تريده حقًا يمثل مخاطرة أمنية. تحتوي بعض الملفات على فيروسات ، وسيحاول بعض المواقع تنزيل ملفات ضارة على جهازك دون مطالبتك. لذلك لا يوصى بالسماح بتنزيل الملف بدون مطالبة التنزيل بحيث يتعين على المستخدمين التحقق من الملف ويمكن التحقق من مصدره قبل تنزيله أو تشغيله. يؤدي تعطيل مربع حوار التنزيل إلى جعل النظام عرضة للفيروسات وأحصنة طروادة والمتسللين الذين قد يؤثرون بصمت على نظامك.
## **فتح ملف بدون مربع الحوار فتح حفظ وإلغاء**
 على الرغم من كونه مصدر قلق أمني كبير ، لا يزال Microsoft يوفر إعدادات Internet Explorer التي تسمح للمستخدمين بتعطيل موجه Open-Save-Cancel لتنزيل الملف.

في مستكشف Windows:

1.  على ال**أدوات** القائمة ، حدد**خيارات المجلد**.
1. انقر فوق علامة التبويب "أنواع الملفات" في مربع الحوار "خيارات المجلد".
1. حدد نوع ملف الامتداد XLS.
1.  انقر**متقدم**. 
يتم عرض مربع حوار. لديها ثلاثة خيارات في الأسفل.
1.  قم بإلغاء التحديد**قم بتأكيد الفتح بعد التنزيل**.
1.  حدد الخيار الثالث -**تصفح في نفس النافذة** - لعرض ملف Excel في برنامج Internet Explorer دون بدء تشغيل Microsoft Excel بشكل مستقل.

|**تحرير خيارات نوع الملف**|
|:- |
|![ما يجب القيام به: image_بديل_نص](opening-excel-file-without-open-save-cancel-dialog-box_2.png)|
يسمح هذا الإعداد بتشغيل الملفات مباشرة في مستعرض الويب ، بدون ظهور مربع الحوار فتح-حفظ-إلغاء عند تنزيل الملف أو فتحه.

---
title: تغيير حجم GridWeb في نافذة المتصفح
type: docs
weight: 40
url: /ar/net/aspose-cells-gridweb/resize-gridweb-in-the-browser-window/
keywords: GridWeb,resize
description: يقدم هذا المقال كيفية تغيير الحجم في GridWeb.
---

## **سيناريوهات الاستخدام المحتملة**
أحيانًا ترغب في أن يقوم Aspose.Cells.GridWeb بتغيير حجم نفسه وفقًا لنافذة المتصفح. قد تحتاج أن يقوم GridWeb بضبط حجمه (الارتفاع ، العرض) دائمًا ويكون متوافقًا مع حجم نافذة المتصفح. يوفر Aspose.Cells.GridWeb دالة *resize()* في الجانب العميل لهذا الغرض. علاوة على ذلك ، يمكنك حتى جعل التحكم في GridWeb قابلاً للتغيير في نافذة المتصفح. على سبيل المثال ، يمكنك استخدام المقبض الأيمن السفلي (عبر الماوس) لتخصيص عرضه / ارتفاعه في النافذة. عليك أيضًا تضمين / تحديد ملفات الجافا سكريبت jquery لجعله يعمل في مصدر الصفحة في مشروعك.
## **استخدام طريقة تغيير حجم GridWeb**
سيتحقق الكود العيني التالي مما إذا كان هناك عملية تغيير حجم تمت كل 100 ميللي ثانية. عندما لا تكون هناك عملية تغيير حجم أخرى ، فإنه يعتقد أن عملية التغيير في الحجم انتهت الآن. نحن نستخدم ملف قالب عيني يتم استيراده إلى GridWeb. نستخدم الكود الجانب العميل لتغيير حجم GridWeb. تظهر الصورة العينية أن GridWeb يقوم بتغيير حجمه وفقًا لذلك عند تغيير حجم نافذة المتصفح.

![todo:image_alt_text](resize-gridweb-in-the-browser-window_1.png)
### **الكود المثالي**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-WorkingWithGridWebClientSideScript-ResizeGridWebUsingResizeMethod" >}}


## **جعل GridWeb قابلاً للتغيير في الحجم باستخدام ميزة resizable jquery ui**
الكود العيني التالي سيجعل التحكم في GridWeb قابلاً للتغيير في نافذة المتصفح. على سبيل المثال ، يمكنك استخدام المقبض الأيمن السفلي لتخصيص حجم GridWeb في النافذة. نحن نستخدم نفس ملف القالب الذي يتم استيراده إلى GridWeb أولاً. نحن نستخدم نصوص jquery لجعل GridWeb قابلاً للتغيير في الحجم. تظهر الصورة العينية أن GridWeb قد تم تغيير حجمه باستخدام المقبض الأيمن السفلي في نافذة المتصفح.

![todo:image_alt_text](resize-gridweb-in-the-browser-window_2.png)
### **الكود المثالي**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-WorkingWithGridWebClientSideScript-MakingGridWebResizableUsingResizablejQueryUiFeature" >}}

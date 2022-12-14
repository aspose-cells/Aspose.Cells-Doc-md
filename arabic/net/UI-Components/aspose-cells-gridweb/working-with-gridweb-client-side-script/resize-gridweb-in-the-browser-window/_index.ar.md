---
title: تغيير حجم GridWeb في نافذة المتصفح
type: docs
weight: 40
url: /ar/net/resize-gridweb-in-the-browser-window/
---
## **سيناريوهات الاستخدام الممكنة**
في بعض الأحيان تريد أن يقوم Aspose.Cells.GridWeb بتغيير حجم نفسه وفقًا لنافذة المتصفح. قد تحتاج إلى أن تقوم GridWeb دائمًا بضبط حجمها (الارتفاع والعرض) ومتوافقة مع حجم نافذة المتصفح. Aspose.Cells.GridWeb يوفر جانب العميل*تغيير الحجم()* وظيفة لهذا الغرض. علاوة على ذلك ، يمكنك حتى جعل التحكم في GridWeb قابلًا لتغيير حجمه في نافذة المتصفح. على سبيل المثال ، يمكنك استخدام المقبض الأيمن السفلي (عبر الماوس) لتخصيص عرضه / ارتفاعه في النافذة. تحتاج أيضًا إلى تضمين / تحديد ملفات Javascript jquery لجعلها تعمل في مصدر الصفحة في مشروعك.
## **استخدام طريقة تغيير حجم GridWeb**
سيتحقق الكود التالي من إجراء تغيير الحجم كل 100 مللي ثانية. عندما لا يكون هناك المزيد من إجراء تغيير الحجم ، فإنه يعتقد أن عملية تغيير الحجم قد انتهت الآن. نستخدم نموذج ملف تم استيراده إلى GridWeb. نستخدم رمز جانب العميل لتغيير حجم GridWeb. تُظهر لقطة الشاشة أن GridWeb يغير حجم نفسه وفقًا لذلك عند تغيير حجم نافذة المتصفح.

![ما يجب القيام به: image_بديل_نص](resize-gridweb-in-the-browser-window_1.png)
### **عينة من الرموز**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-WorkingWithGridWebClientSideScript-ResizeGridWebUsingResizeMethod" >}}


## **جعل GridWeb قابل لتغيير الحجم باستخدام ميزة jquery ui القابلة لتغيير الحجم**
الكود التالي سيجعل التحكم في GridWeb قابلاً لتغيير حجمه في نافذة المتصفح. على سبيل المثال ، يمكنك استخدام المقبض الأيمن السفلي لتخصيص حجم GridWeb في النافذة. نستخدم ملف القالب نفسه الذي تم استيراده إلى GridWeb أولاً. نحن نستخدم نصوص jquery لجعل GridWeb قابلة لتغيير الحجم. تُظهر لقطة الشاشة أنه تم تغيير حجم GridWeb باستخدام المقبض الأيمن السفلي في نافذة المتصفح.

![ما يجب القيام به: image_بديل_نص](resize-gridweb-in-the-browser-window_2.png)
### **عينة من الرموز**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-WorkingWithGridWebClientSideScript-MakingGridWebResizableUsingResizablejQueryUiFeature" >}}

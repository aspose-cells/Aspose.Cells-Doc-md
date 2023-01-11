﻿---
title: استخدام زر عام لإرسال بيانات الشبكة
type: docs
weight: 20
url: /ar/net/using-a-common-button-to-submit-grid-data/
---
{{% alert color="primary" %}} 

 Aspose.Cells.GridWeb يوفر بعض أزرار الأوامر المضمنة مثل**يُقدِّم** و**يحفظ**. استخدم هذه الأزرار لأداء المهام ذات الصلة.

توضح هذه المقالة كيفية إرسال البيانات إلى خادم ليس فقط عن طريق النقر فوق GridWeb المدمج**يحفظ** زر الأمر ، ولكن عن طريق النقر فوق زر ASP.NET شائع (التحكم في الويب). الغرض من هذه المقالة هو إظهار مرونة Aspose.Cells.GridWeb. علاوة على ذلك ، تستخدم هذه المقالة أيضًا وظائف خاصة تم الكشف عنها بواسطة Aspose.Cells.GridWeb لاستخدامها في البرنامج النصي من جانب العميل.

{{% /alert %}} 
## **إرسال بيانات الشبكة باستخدام زر ASP.NET**
Aspose.Cells.GridWeb يوفر ثلاثة أزرار مدمجة (**يُقدِّم**, **يحفظ** و**الغاء التحميل** ). بعد التحرير في GridWeb ، يمكن للمستخدم النقر فوق ملف**يُقدِّم** أو**يحفظ** الزر في شريط علامات التبويب للسماح لـ GridWeb بإرسال البيانات إلى الخادم. إذا قام المستخدم بالنقر فوق علامة تبويب الورقة ، فإن عنصر التحكم GridWeb يؤدي نفس المهمة مثل تلك الخاصة بأزرار الأوامر المضمنة. Aspose.Cells.GridWeb يدعم أيضًا إضافة هذه الوظيفة إلى عنصر تحكم زر ASP.NET شائع ، لكنك تحتاج إلى إضافة بعض التعليمات البرمجية الإضافية إلى التطبيق.
### **1. إنشاء تطبيق اختبار**
افتح Visual Studio.NET IDE الخاص بك وقم بإنشاء مشروع تطبيق ويب ASP.NET جديد. بمجرد إنشاء التطبيق ، ستتم إضافة صفحة WebForm1.aspx افتراضية إلى مشروعك. قم بسحب وإسقاط التحكم في GridWeb من Toolbox إلى نموذج الويب. إذا لم تتمكن من العثور على عنصر تحكم GridWeb في Toolbox الخاص بك ، فارجع إلى هذه الصفحة:[دمج Aspose.Cells شبكة التحكم مع Visual Studio.NET](/cells/ar/net/integrate-aspose-cells-grid-controls-with-visual-studio-net/) لمعرفة المزيد حول هذا الموضوع: بعد إضافة عنصر تحكم GridWeb إلى نموذج الويب الخاص بك ، قم أيضًا بإضافة عنصر تحكم ويب Button من Toolbox إلى نموذج الويب الخاص بك.
### **2. إضافة رمز إلى Page_Load Event**
حان الوقت الآن لإضافة بعض التعليمات البرمجية إلى الصفحة_حدث التحميل من نموذج الويب. يمكنك النقر نقرًا مزدوجًا فوق نموذج الويب في طريقة عرض التصميم وسيقوم VS.NET IDE بنقلك تلقائيًا إلى الصفحة_تحميل معالج الحدث حيث ستحتاج إلى استخدام مجموعة السمات الخاصة بالزر لتجاوز حدث OnClick الخاص به.

{{% alert color="primary" %}} 

ASP.NET زر التحكم هو عنصر تحكم من جانب الخادم. عندما يتم النقر عليه ، يتم تشغيل حدث جانب الخادم ولكن إذا كنت تريد استخدام عنصر التحكم في الزر هذا لتنفيذ بعض التعليمات البرمجية على جانب العميل (عادةً باستخدام جافا سكريبت) ، فأنت بحاجة إلى تعديل سمة onclick الخاصة به ضمن حدث Page_Load. Aspose.Cells.GridWeb يوفر بعض الوظائف التي يمكن استدعاؤها في جافا سكريبت للتعامل مع تحكم GridWeb من جانب العميل. في المثال أدناه ، استخدمنا وظائف updateData & validateAll (وهي وظائف من جانب العميل) من GridWeb لتحديث بيانات الشبكة والتحقق منها.

{{% /alert %}} 
#### **مثال رمز**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-UsingCommonSubmitButton.aspx-UsingCommonSubmitButton.cs" >}}
### **3. تشغيل التطبيق**
الآن ، يمكنك ترجمة التطبيق وتشغيله بالضغط على Ctrl + F5 وسيتم فتح الصفحة في نافذة متصفح جديدة. دعنا نضيف بعض القيم إلى GridWeb ونضغط على زر إرسال بيانات الشبكة إلى الخادم وسترى حدوث إعادة النشر لتحديث بيانات GridWeb والتحقق من صحتها.
## **استنتاج**
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb يوفر مرونة كبيرة للعمل مع ضوابط GridWeb من الخادم أو العميل. يمتلك المطورون عددًا كبيرًا من الخيارات لاستخدام التحكم في GridWeb في أنواع مختلفة من السيناريوهات لتقديم حلول أفضل لعملائهم.

{{% /alert %}}
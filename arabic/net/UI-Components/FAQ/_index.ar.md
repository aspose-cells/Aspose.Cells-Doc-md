---
title: التعليمات
type: docs
weight: 400
url: /ar/net/grid-faq/
---
## **هل هناك أي قيود في إصدار التقييم لـ Aspose.Cells Grid Controls؟**
 لا ، لا توجد قيود على الميزات في إصدار التقييم لـ Aspose.Cells Grid Controls. يوفر الإصدار التقييمي ميزات كاملة للإصدار المرخص باستثناء أنه يضيف ورقة عمل إضافية (تحتوي على**تحذير حقوق النشر الخاصة بالتقييم** ) إلى ملفات الإخراج.
## **هناك الكثير من ضوابط الشبكة المتاحة في السوق. لماذا يجب علي شراء Aspose.Cells Grid Controls؟**
 حسنًا ، أسعار Aspose.Cells Grid Controls جيدة جدًا لتكون في متناول جميع أنواع المستخدمين. بسعر معقول جدًا ، فإنه يوفر لك مجموعة من عنصري تحكم للعمل على Windows وتطبيقات الويب. علاوة على ذلك ، إنها ليست مجرد شبكة بسيطة ، إنها شبكة**عارض جداول البيانات والمحرر والمبدع** في نفس الوقت. لا يمكنك ربطه فقط بأي نوع من مصادر البيانات (مثل عناصر تحكم الشبكة العادية) ولكن يمكنك أيضًا إنشاء ملفات Excel وإدارتها. كما يوفر قويًا وغنيًا**محرك حساب الصيغة** لحساب ليس فقط الوظائف المضمنة (المدعومة بواسطة عناصر تحكم الشبكة Aspose.Cells) ولكن أيضًا الصيغ المخصصة التي تحددها أنت. هناك ميزات أكثر بكثير لمجموعة Aspose.Cells Grid التي لا يمكن تغطيتها هنا ، يرجى الرجوع إلى صفحة أنواع الإصدارات للحصول على قائمة ميزات أكثر تفصيلاً.
## **لقد اشتريت مؤخرًا ترخيصي لـ Aspose.Cells Grid Controls. كيف يمكنني استخدام هذا الترخيص في تطبيقي مع Aspose.Cells Grid Control؟**
يرجى الرجوع إلى[الترخيص](/cells/ar/net/licensing/) صفحة Aspose.Cells Grid Controls. يوفر تفاصيل كاملة حول كيفية استخدام الترخيص مع Aspose.Cells Grid Controls في تطبيقاتك.
## **هل Aspose.Cells Grid Controls مدعومة في Visual Studio.NET 2005؟**
نعم ، Aspose.Cells Grid Controls مدعومة بالكامل في Visual Studio.NET 2005 والإصدارات الأحدث.
## **أنا أستخدم Aspose.Cells.GridWeb control في موقع الويب الخاص بي باستخدام Visual Studio.NET 2005. ولكنه لا يعمل على الإطلاق. ما هي المشكلة؟**
 Aspose.Cells.GridWeb يدعم كليهما**نظام الملفات** و**HTTP** أوضاع Visual Studio.NET 2005. إذا كنت لا تزال مرتبكًا ، فيرجى إلقاء نظرة على دليل خطوة بخطوة للعمل مع Aspose.Cells.GridWeb باستخدام Visual Studio.NET 2005.
## **كيف يمكنني نشر مشروع / حل ويب Aspose.Cells.GridWeb الخاص بي على الخادم؟**
إذا كنت بحاجة إلى نشر تطبيق الويب الذي يحتوي على تحكم GridWeb ، فيمكنك نسخ "acw_client "إلى مجلد المشروع الخاص بك على الأقل لم يتمكن تطبيق الويب الخاص بك (المنشور عبر الخادم) من العثور عليه. يمكنك دائمًا تحديد مسار البرمجة النصية عن طريق إضافة سطور التعليمات البرمجية التالية في قسم التكوين (على سبيل المثال في ملف web.config في مشروع VS.NET)_client "هو مجلد يحتوي على ملفات و Aspose.Cells.GridWeb يستخدم هذا المجلد لإدارة تكوينه الداخلي ، ويحتوي على ملفات نصية وملفات صور وملفات أخرى لتحديد سلوك GridWeb وتعيين عمليات أخرى. يتم استخدام ملف التكوين لمنع التحكم من باستخدام موارد العميل المضمنة (الصور والنصوص وما إلى ذلك) والتي تكون مفيدة في بعض الحالات / السيناريوهات.

**XML**

{{< highlight "csharp" >}}

 <appSettings>

  <add key="aspose.cells.gridweb.acw_client_path" value="/grid/acw_client/"/>

  <add key="aspose.cells.gridweb.force_script_path" value="true"/>

  <add key="aspose.cells.gridweb.forcepath" value="true"/>

 </appSettings>

{{< /highlight >}}

{{% alert color="primary" %}} 

يرتبط المسار دائمًا بدليل المشروع. يجب ألا تستخدم أي دليل خارج دليل المشروع. لذلك من الضروري نسخ دليل "acw_client" (@ مجلد تثبيت GridWeb الخاص بك) في دليل المشروع.

{{% /alert %}} 
## **تشغيل Aspose.Cell.GridWeb في Internet Explorer 10 أو 11**
 حاليًا Aspose.Cells.GridWeb لا يعمل جيدًا على Internet Explorer 10 أو 11 ، لذلك عليك استخدام وضع التوافق لـ IE8 / 9 للعمل معه على نوع متصفح IE10 / 11. يجب عليك إضافة السطر التالي من**<meta>** علامة في قسم الرأس بتنسيق**.aspx** صفحة:



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-FAQ-RunGridWebInIE-RunGridWebIE.aspx" >}}


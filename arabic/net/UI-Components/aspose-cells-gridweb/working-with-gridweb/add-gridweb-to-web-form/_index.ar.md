---
title: إضافة GridWeb إلى نموذج الويب
type: docs
weight: 10
url: /ar/net/aspose-cells-gridweb/add-gridweb-to-web-form/
keywords: GridWeb,webform,form
description: يقدم هذا المقال كيفية العمل مع نموذج الويب في GridWeb.
---

{{% alert color="primary" %}} 

يوفر هذا الموضوع دليلًا تدريجيًا أساسيًا للمبتدئين لمساعدتهم في إنشاء واستخدام عنصر التحكم Aspose.Cells.GridWeb في تطبيقات الويب.

{{% /alert %}} 
## **إنشاء واستخدام عنصر تحكم Aspose.Cells.GridWeb**
### **الخطوة 1: إنشاء مشروع تطبيق ويب**
أولاً، قم بإنشاء مشروع تطبيق ويب تستخدم فيه عنصر التحكم Aspose.Cells.GridWeb:

1. افتح Visual Studio.
1. من قائمة **الملف**, حدد **جديد** ثم **مشروع**. 

![todo:image_alt_text](add-gridweb-to-web-form_1.png)



يظهر مربع حوار مشروع جديد.

1. حدد **ASP.NET Web Application** لغة الرغبة. 

![todo:image_alt_text](add-gridweb-to-web-form_2.png)

1. حدد النموذج **Web Forms**. 

![todo:image_alt_text](add-gridweb-to-web-form_3.png)

1. أضف نموذج ويب جديد إلى المشروع.
### **الخطوة 2: تضمين التحكم في النموذج الويب**
اسحب وأسقط تحكم Aspose.Cells.GridWeb من مربع الأدوات في Visual Studio إلى النموذج الويب. 

![todo:image_alt_text](add-gridweb-to-web-form_4.png)

{{% alert color="primary" %}} 

لمعرفة كيفية إضافة تحكمات شبكة Aspose.Cells إلى مربع أدوات Visual Studio، يرجى قراءة [دمج تحكمات Aspose.Cells.Grid مع Visual Studio.NET](/cells/as/asp/asp.net/integrate-aspose-cells-grid-controls-with-visual-studio-net/).

{{% /alert %}} 

عندما يتم إضافة التحكم إلى النموذج، يتم عرضه على النحو التالي: 

![todo:image_alt_text](add-gridweb-to-web-form_5.png)
### **الخطوة 3: تغيير حجم التحكم**
يتم عرض النموذج بحجم افتراضي. قم بضبط الحجم عن طريق سحب الحدود أو الزوايا. 

![todo:image_alt_text](add-gridweb-to-web-form_6.png)
### **الخطوة 4: ضبط خصائص التحكم**
يمكن أيضًا تكوين تحكم Aspose.Cells.GridWeb باستخدام العديد من الخصائص. 

![todo:image_alt_text](add-gridweb-to-web-form_7.png)

من الممكن ضبط العديد من خصائص التحكم باستخدام مربع الخصائص. تشمل الخصائص الأساسية الارتفاع والعرض، واللون والأنماط البصرية. تشمل الخصائص المتقدمة وضع التحرير ووضع الجلسة ووضع النقر المزدوج. علاوة على ذلك، من الممكن ضبط معالجات الأحداث المخصصة في مربع الخصائص.

هناك أيضا بعض أدوات التكوين الإضافية لتحكم Aspose.Cells.GridWeb التي يمكن رؤيتها في أسفل مربع الخصائص كروابط نصية، أو بالنقر بزر الفأرة الأيمن على تحكم GridWeb للعثور عليها. تشمل هذه الأدوات تكوين:

- الأزرار الخاصة بالأوامر المخصصة
#### **الأزرار الخاصة بالأوامر المخصصة**
لفتح محرر الأزرار الخاصة بالأوامر المخصصة:
انقر بزر الفأرة الأيمن على تحكم GridWeb وحدد **Custom Command Buttons**. 

![todo:image_alt_text](add-gridweb-to-web-form_8.png)



يتم عرض مربع حوار محرر CustomCommandButton Collection. 

![todo:image_alt_text](add-gridweb-to-web-form_9.png)

يتيح المحرر للمطورين إضافة وإزالة الأزرار المخصصة في تحكم GridWeb.


### **مهم**
يوفر Aspose.Cells.GridWeb أيضًا ملفات موارده مع العنصر التحكم. يحتوي "acw_client" على مجلد (@دليل التثبيت الخاص بك) الذي يحتوي على ملفات ويستخدم Aspose.Cells.GridWeb هذا المجلد لإدارة تكوينه الداخلي والوظائف الأخرى، ويحتوي على ملفات نصية وملفات صور وملفات أخرى لتحديد سلوك GridWeb وتعيين العمليات الأخرى. يتم استخدام ملف التكوين لإدارة موارد العميل المضمنة (الصور والنصوص، إلخ). علاوة على ذلك، عندما تحتاج إلى نشر تطبيق الويب الذي يحتوي على عنصر تحكم GridWeb، يجب عليك نسخ أيضًا دليل "acw_client" إلى مجلد المشروع الخاص بك على الأقل، ثم لن يتمكن تطبيق الويب الخاص بك (الذي يتم نشره على الخادم) من العثور عليه. يمكنك دائمًا تحديد مجلد الموارد عن طريق إضافة السطور التالية من الكود في القسم التكويني (مثل ملف web.config في مشروع VS.NET الخاص بك):



|<p>{{< highlight java >}}</p><p> <appSettings></p><p>  <add key="aspose.cells.gridweb.acw_client_path" value="/grid/acw_client/"/> </p><p></appSettings></p><p>{{< /highlight >}}</p>|
| :- |


{{% alert color="primary" %}}

المسار مرتبط دائمًا بدليل المشروع. يجب عليك عدم استخدام أي دليل خارج دليل المشروع. لذا من الضروري نسخ دليل "acw_client" (@دليل تثبيت GridWeb الخاص بك) إلى دليل المشروع/المجلد الفرعي.

{{% /alert %}}
### **الخطوة 5: تشغيل تطبيق الويب**
قم بتشغيل التطبيق عن طريق الضغط على Ctrl+F5 أو النقر فوق الزر **بدء**. 

عند تشغيل التطبيق في متصفح، سيتم عرض صفحة WebForm1.aspx، التي تحتوي الآن على عنصر تحكم Aspose.Cells.GridWeb فارغًا. أضف القيم إلى الخلايا عن طريق النقر عليها. من الممكن أيضًا القيام بمهام أخرى مثل تغيير ارتفاع الصف أو عرض العمود، نسخ (Ctrl+C) أو قص (Ctrl+X) بيانات الخلية إلى الحافظة، ولصق (Ctrl+V) البيانات في الخلية. للقيام بمزيد من العمليات، قم بالنقر بزر الماوس الأيمن على العنصر التحكم لرؤية القائمة الكاملة للخيارات. 

**قائمة سياق Aspose.Cells.GridWeb** 

![todo:image_alt_text](add-gridweb-to-web-form_10.png)

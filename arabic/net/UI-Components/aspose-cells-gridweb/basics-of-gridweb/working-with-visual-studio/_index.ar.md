---
title: العمل مع فيجوال ستوديو
type: docs
weight: 20
url: /ar/net/aspose-cells-gridweb/work-with-visual-studio/
keywords: GridWeb,visualstudio
description: يقدم هذا المقال كيفية استخدام GridWeb في فيجوال ستوديو.
---

{{% alert color="primary" %}} 

يشرح هذا الموضوع كيفية استخدام Aspose.Cells.GridWeb في تطبيقات ASP.NET باستخدام Visual Studio.NET 2005. هذا الموضوع مفيد للمطورين على مستوى المبتدئين الذين يعملون مع Aspose.Cells.GridWeb.

{{% /alert %}} 
## **العمل مع Aspose.Cells.GridWeb باستخدام فيجوال ستوديو 2013**
يوضح هذا الموضوع كيفية استخدام Aspose.Cells.GridWeb من خلال إنشاء موقع ويب تجريبي في فيجوال ستوديو 2013. تم تقسيم العملية إلى خطوات.
### **الخطوة 1: إنشاء موقع ويب جديد**
1. افتح فيجوال ستوديو 2013.
1. من قائمة **File**، حدد **New Menu**، ثم **Web Site**. 

![todo:image_alt_text](working-with-visual-studio_1.png)


يتم فتح مربع الحوار New Web Site. 

1. حدد **ASP.NET Web Forms Site** من القوالب المثبتة في فيجوال ستوديو.
1. اختر نمط HTTP كموقع لموقع الويب. 

![todo:image_alt_text](working-with-visual-studio_2.png)




1. حدد الموقع الذي ستتم فيه إنشاء ملفات موقع الويب وتخزينها. 
   1. انقر **Browse** في مربع الحوار New Web Site. 

![todo:image_alt_text](working-with-visual-studio_3.png)



يتم عرض مربع الحوار Choose Location. 

1. انقر على علامة التبويب **Local IIS**.
   يتم عرض جميع المجلدات وتطبيقات الويب المخزنة في مجلد الجذر الخاص بـ IIS الخاص بك (على سبيل المثال: C:\Inetpub\wwwroot). 

![todo:image_alt_text](working-with-visual-studio_4.png)




1. أنشئ تطبيق ويب جديد في IIS المحلي حيث ستتم تخزين ملفات الموقع الإلكتروني.
   يتيح لك مربع حوار اختيار الموقع إنشاء وحذف التطبيقات الويب أو الدلائل الظاهرية في IIS المحلي. لإنشاء تطبيق ويب، انقر فوق زر كما هو موضح في الشكل أدناه. 

![todo:image_alt_text](working-with-visual-studio_5.png)



يتم إنشاء تطبيق ويب جديد بالاسم الافتراضي WebSite. 

1. إعادة تسمية تطبيق الويب. لقد أعدنا تسميته إلى GridWebOn2013.
1. انقر فوق **فتح**. 

![todo:image_alt_text](working-with-visual-studio_6.png)



You return to the New Web Site dialog. The path of web site location is set to <http://localhost/GridWebOn2013>. 

1. انقر فوق **موافق** للسماح لـ Visual Studio بإنشاء موقع ويب. 

![todo:image_alt_text](working-with-visual-studio_7.png)
### **الخطوة 2: التحقق من عروض النص والتصميم لصفحة الويب**
سيكون قد تم إنشاء موقع ويب افتراضي بواسطة Visual Studio 2013. يحتوي على صفحة ويب Default.aspx افتراضية مع بعض النصوص والعلامات الدمية. 

**عرض المصدر لصفحة default.aspx** 

![todo:image_alt_text](working-with-visual-studio_8.png)



يمكن فتح جميع صفحات الويب (بما في ذلك ASP.NET) في وضعين. يعتبر الأول عرض المصدر الذي يتيح للمطورين الوصول إلى الشيفرة المصدرية وتعديلها. يعتبر الوضع الثاني عرض التصميم الذي يمكن استخدامه لتصميم صفحات الويب بطريقة WYSIWYG. يعرض اللقطة الشاشة أعلاه عرض المصدر لصفحة ويب default.aspx. لعرض عرض التصميم، انقر فوق **تصميم**. 

**عرض التصميم لصفحة default.aspx** 

![todo:image_alt_text](working-with-visual-studio_9.png)




حذف الصفحة Default.aspx التي تمت إضافتها بواسطة Visual Studio وإضافة صفحة Default.aspx فارغة جديدة.

![todo:image_alt_text](working-with-visual-studio_10.png)
### **الخطوة 3: إضافة Aspose.Cells.GridWeb إلى صفحة الويب**
يمكنك ببساطة إضافة تحكم Aspose.Cells.GridWeb (أو GridWeb) إلى صفحة ويب عن طريق سحبه من مربع الأدوات. 

![todo:image_alt_text](working-with-visual-studio_11.png)




{{% alert color="primary" %}} 

إذا كنت لا تعرف كيفية إضافة Aspose.Cells.GridWeb إلى مربع الأدوات، راجع [دمج تحكم Aspose.Cells Grid مع Visual Studio.NET](/cells/ar/net/aspose-cells-gridweb/integrate-aspose-cells-grid-controls-with-visual-studio-net/). 

{{% /alert %}} 

بمجرد أن يتم إسقاط تحكم GridWeb إلى صفحة ويب، سيتم عرضه على النحو التالي: 

![todo:image_alt_text](working-with-visual-studio_12.png)



### **Step 4: Change the <!DOCTYPE> tag**
1. Switch to source view and find the following **<!DOCTYPE>** tag in the source code: 

**ASP.NET**

{{< highlight csharp >}}



<!DOCTYPE html>



{{< /highlight >}}

1. حدد العلامة الكاملة. 

![todo:image_alt_text](working-with-visual-studio_13.png)




1. Retain, change or delete the <!DOCTYPE> tag.
1. Or modify the <!DOCTYPE> tag with the following one: 

{{< highlight csharp >}}



<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">



{{< /highlight >}}
### **الخطوة 5: تغيير حجم التحكم Aspose.Cells.GridWeb**
يمكنك تغيير عرض وارتفاع تحكم GridWeb بعد سحبه إلى الموقع الإلكتروني. 

يمكنك في وضع التصميم تغيير عرض وارتفاع GridWeb. 

![todo:image_alt_text](working-with-visual-studio_14.png)



### **الخطوة 6: تكوين خصائص Aspose.Cells.GridWeb**
قم بتكوين خصائص Aspose.Cells.GridWeb في WYSIWYG عن طريق النقر على زر **الخصائص** على الجانب الأيمن من محرر الرسوميات Visual Studio 2013. 
يتم عرض مربع الحواصل. 

![todo:image_alt_text](working-with-visual-studio_15.png)



يجعل الحاوية الخصائص من الممكن تكوين مظهر GridWeb وبعض خصائص أخرى للتحكم في سلوك GridWeb.
### **الخطوة 7: تشغيل موقع الويب الخاص بك الأول الذي يحتوي على Aspose.Cells.GridWeb**
بناء وتشغيل موقع الويب. 

1. قم بتشغيل موقع الويب مباشرة من Visual Studio عن طريق الضغط على Ctrl+F5 أو النقر على **بدء التصحيح**. 

![todo:image_alt_text](working-with-visual-studio_16.png)

الآن، يمكنك البدء في التعامل مع عنصر تحكم GridWeb. 

**عنصر تحكم GridWeb في العمل** 

![todo:image_alt_text](working-with-visual-studio_17.png)

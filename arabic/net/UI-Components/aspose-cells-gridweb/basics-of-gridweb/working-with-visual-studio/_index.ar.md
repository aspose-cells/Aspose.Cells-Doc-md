---
title: العمل مع Visual Studio
type: docs
weight: 20
url: /ar/net/working-with-visual-studio/
---
{{% alert color="primary" %}} 

يشرح هذا الموضوع كيفية استخدام Aspose.Cells.GridWeb في تطبيقات ASP.NET باستخدام Visual Studio.NET 2005. هذا الموضوع مفيد للمطورين على مستوى المبتدئين الذين يعملون مع Aspose.Cells.GridWeb.

{{% /alert %}} 
## **العمل مع Aspose.Cells.GridWeb باستخدام Visual Studio 2013**
يوضح هذا الموضوع كيفية استخدام Aspose.Cells.GridWeb من خلال إنشاء نموذج لموقع ويب في Visual Studio 2013. وقد تم تقسيم العملية إلى خطوات.
### **الخطوة 1: إنشاء موقع ويب جديد**
1. افتح Visual Studio 2013.
1.  من**ملف** القائمة ، حدد**قائمة جديدة** ، ومن بعد**موقع الكتروني**. 

![ما يجب القيام به: image_بديل_نص](working-with-visual-studio_1.png)


 يتم فتح مربع حوار New Web Site.

1.  يختار**ASP.NET موقع نماذج ويب** من قوالب Visual Studio المثبتة.
1.  اختر وضع HTTP لموقع موقع الويب.

![ما يجب القيام به: image_بديل_نص](working-with-visual-studio_2.png)




1.  حدد موقعًا حيث سيتم إنشاء ملفات موقع الويب وتخزينها.
 1. انقر فوق**تصفح** في مربع الحوار New Web Site.

![ما يجب القيام به: image_بديل_نص](working-with-visual-studio_3.png)



 يتم عرض مربع حوار اختيار الموقع.

1.  انقر على**IIS المحلية** التبويب.
يتم عرض كافة المجلدات وتطبيقات الويب المخزنة في مجلد IIS الجذر (على سبيل المثال: C: \ Inetpub \ wwwroot).

![ما يجب القيام به: image_بديل_نص](working-with-visual-studio_4.png)




1. الآن قم بإنشاء تطبيق ويب جديد في IIS المحلي الخاص بك حيث سيتم تخزين ملفات موقع الويب.
 يتيح لك مربع حوار اختيار الموقع إنشاء وحذف تطبيقات الويب أو الدلائل الظاهرية في IIS المحلي. لإنشاء تطبيق ويب ، انقر فوق الزر كما هو موضح أدناه في الشكل.

![ما يجب القيام به: image_بديل_نص](working-with-visual-studio_5.png)



 يتم إنشاء تطبيق ويب جديد بالاسم الافتراضي WebSite.

1. أعد تسمية تطبيق الويب. قمنا بإعادة تسميتها GridWebOn2013.
1.  انقر**فتح**. 

![ما يجب القيام به: image_بديل_نص](working-with-visual-studio_6.png)



 ترجع إلى مربع حوار موقع ويب جديد. تم تعيين مسار موقع موقع الويب على<http://localhost/GridWebOn2013>. 

1.  انقر**نعم** للسماح لبرنامج Visual Studio بإنشاء موقع ويب.

![ما يجب القيام به: image_بديل_نص](working-with-visual-studio_7.png)
### **الخطوة 2: التحقق من طرق عرض المصدر والتصميم لصفحة الويب**
 سيتم إنشاء موقع ويب افتراضي بواسطة Visual Studio 2013. يحتوي على صفحة ويب default.aspx مع بعض النص الوهمي والترميز.

**طريقة العرض المصدر لصفحة default.aspx** 

![ما يجب القيام به: image_بديل_نص](working-with-visual-studio_8.png)



يمكن فتح جميع صفحات الويب (بما في ذلك ASP.NET) في وضعين. أحدهما هو عرض المصدر الذي يتيح للمطورين الوصول إلى التعليمات البرمجية المصدر وتعديلها. الوضع الثاني هو عرض التصميم الذي يمكن استخدامه لتصميم صفحات الويب بطريقة WYSIWYG. تُظهر لقطة الشاشة أعلاه طريقة عرض مصدر لصفحة الويب default.aspx. لعرض عرض التصميم ، انقر فوق**تصميم**. 

**طريقة عرض تصميم صفحة default.aspx** 

![ما يجب القيام به: image_بديل_نص](working-with-visual-studio_9.png)




احذف صفحة Default.aspx المضافة بواسطة Visual Studio وأضف صفحة Default.aspx فارغة جديدة.

![ما يجب القيام به: image_بديل_نص](working-with-visual-studio_10.png)
### **الخطوة 3: إضافة Aspose.Cells.GridWeb إلى صفحة الويب**
 يمكنك ببساطة إضافة عنصر تحكم Aspose.Cells.GridWeb (أو GridWeb) إلى صفحة ويب عن طريق سحبه من صندوق الأدوات.

![ما يجب القيام به: image_بديل_نص](working-with-visual-studio_11.png)




{{% alert color="primary" %}} 

 إذا كنت لا تعرف كيفية إضافة Aspose.Cells.GridWeb إلى مربع الأدوات ، فارجع إلى[دمج Aspose.Cells شبكة التحكم مع Visual Studio.NET](/cells/ar/net/integrate-aspose-cells-grid-controls-with-visual-studio-net/). 

{{% /alert %}} 

 بمجرد إسقاط عنصر تحكم GridWeb في صفحة الويب ، فسيتم عرضه على النحو التالي:

![ما يجب القيام به: image_بديل_نص](working-with-visual-studio_12.png)



### **الخطوة 4: قم بتغيير علامة <! DOCTYPE>**
1.  قم بالتبديل إلى عرض المصدر وابحث عن ما يلي**<! DOCTYPE>** علامة في شفرة المصدر:

**ASP.NET**

{{< highlight "csharp" >}}



<!DOCTYPE html>



{{< /highlight >}}

1.  حدد العلامة الكاملة.

![ما يجب القيام به: image_بديل_نص](working-with-visual-studio_13.png)




1.  الاحتفاظ أو تغيير أو حذف<!DOCTYPE> بطاقة شعار.
1.  أو قم بتعديل ملف<!DOCTYPE> علامة بالعلامة التالية:

{{< highlight "csharp" >}}



<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">



{{< /highlight >}}
### **الخطوة الخامسة: تغيير الحجم Aspose.Cells.GridWeb Control**
 يمكنك تغيير عرض وارتفاع عنصر التحكم GridWeb بعد سحبه إلى موقع الويب.

 في عرض التصميم ، يمكنك تغيير حجم عرض GridWeb وارتفاعه.

![ما يجب القيام به: image_بديل_نص](working-with-visual-studio_14.png)



### **الخطوة 6: تكوين خصائص Aspose.Cells.GridWeb**
 قم بتكوين خصائص Aspose.Cells.GridWeb في WYSIWYG بالنقر فوق ملف**ملكيات** على الجانب الأيمن من Visual Studio 2013 IDE.
 يتم عرض مربع حوار الخصائص.

![ما يجب القيام به: image_بديل_نص](working-with-visual-studio_15.png)



يتيح جزء الخصائص تكوين شكل وأسلوب عرض GridWeb وبعض الخصائص الأخرى للتحكم في سلوك GridWeb.
### **الخطوة 7: تشغيل موقع الويب الأول الخاص بك الذي يحتوي على Aspose.Cells.GridWeb**
 بناء وتشغيل موقع الويب.

1.  قم بتشغيل موقع الويب مباشرة من Visual Studio بالضغط على Ctrl + F5 أو النقر**ابدأ التصحيح**. 

![ما يجب القيام به: image_بديل_نص](working-with-visual-studio_16.png)

 الآن ، يمكنك بدء اللعب باستخدام التحكم في GridWeb.

**التحكم في الشبكة في العمل** 

![ما يجب القيام به: image_بديل_نص](working-with-visual-studio_17.png)

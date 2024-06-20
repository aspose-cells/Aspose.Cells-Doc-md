---
title: تصدير مستخدمي Sitefinity إلى إكسل
type: docs
weight: 20
url: /ar/net/sitefinity-export-users-to-excel/
---

ملخص المحتويات

- [مقدمة](#SitefinityExportUserstoExcel-Introduction)
- [متطلبات النظام والمنصات المدعومة](#SitefinityExportUserstoExcel-SystemRequirementsandSupportedPlatforms) 
  - [متطلبات النظام](#SitefinityExportUserstoExcel-SystemRequirements)
  - [المنصات المدعومة](#SitefinityExportUserstoExcel-SupportedPlatforms)
- [رمز المصدر](#SitefinityExportUserstoExcel-SourceCode) 
  - [كيفية تكوين كود المصدر](#SitefinityExportUserstoExcel-Howtoconfigurethesourcecode)
- [التثبيت والاستخدام](#SitefinityExportUserstoExcel-InstallationandUsage) 
  - [التحميل](#SitefinityExportUserstoExcel-Downloading)
  - [التثبيت](#SitefinityExportUserstoExcel-Installing)
- [استخدام وفيديو ديمو](#SitefinityExportUserstoExcel-UsingandVideoDemo) 
  - [استخدام](#SitefinityExportUserstoExcel-Using)
  - [فيديو توضيحي](#SitefinityExportUserstoExcel-VideoDemo)
- [الدعم](#SitefinityExportUserstoExcel-Support)
- [تمديد والمساهمة](#SitefinityExportUserstoExcel-ExtendandContribute)
## **مقدمة**
يسمح وحدة التصدير من Aspose .NET لمستخدمي Excel لوحدة SiteFinity للمطورين بتصدير مستخدمي SiteFinity إلى Microsoft Excel أو جدول بيانات OpenOffice. توضح هذه الوحدة ميزة بناء جدول البيانات القوية التي يوفرها Aspose.Cells.

## **متطلبات النظام والمنصات المدعومة**
### **متطلبات النظام**
لإعداد إضافات Aspose.Cells .NET لـ Sitefinity ، يجب أن تتوفر لديك الشروط التالية:

- تعمل نظام Sitefinity CMS على ASP.NET 4.0

يرجى عدم التردد في الاتصال بنا إذا كان لديك أي مشاكل في إعداد هذه إضافة Sitefinity.
### **المنصات المدعومة**
تدعم الإضافة على جميع الإصدارات

- تعمل نظام Sitefinity CMS على ASP.NET 4.0
## **رمز المصدر**
يمكنك الحصول على آخر رمز مصدري من أحد المواقع التالية

- [جيتهاب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/SiteFinity)
### **كيفية تكوين كود المصدر**
عليك أن تكون قد قمت بتثبيت ما يلي لفتح وتوسيع كود المصدر

- Visual Studio 2010 أو أحدث

يرجى اتباع هذه الخطوات البسيطة للبدء

1. قم بتنزيل/نسخ كود المصدر.
1. افتح فيجوال ستوديو 2010 واختر **ملف** > **فتح مشروع**
1. تصفح إلى أحدث شفرة مصدرية قمت بتنزيلها وافتح ملف **.sln**.
## **التثبيت والاستخدام**
### **التحميل**
يمكنك تنزيل وحدة تصدير Aspose .NET Content Exporter for Sitefinity من إحدى المواقع التالية

- [جيتهاب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases)
### **التثبيت**
بمجرد تنزيله، يرجى اتباع هذه الخطوات لتثبيت الإضافة في موقع الويب Sitefinity الخاص بك:

**الخطوة 1: انسخ الملفات إلى تثبيت Sitefinity الخاص بك**

يرجى استخراج ملف ZIP الذي تم تنزيله. ستحتاج إلى FTP أو إمكانية الوصول المباشر إلى مجلد تثبيت Sitefinity على الخادم لأداء ما يلي:

1. انسخ Aspose.Cells.dll و Aspose.SiteFinity.ExportUsersToExcel.dll إلى مجلد **bin** في تثبيت Sitefinity.
1. انسخ مجلد **Addons** في الجذر من تثبيت Sitefinity حيث يتواجد مجلد **bin**.

**الخطوة 2: قم بتسجيل إضافة Aspose Sitefinity Content Export في Sitefinity**

1. Log into your Sitefinity CMS with an ‘**Administrator**’ account. The login page can be reached by <http://www.mywebsite.com/sitefinity>
1. انقر **الإدارة** ثم **الإعدادات**.
   يظهر صفحة الإعدادات الأساسية.
1. انقر فوق الرابط **Advanced**.
   يظهر صفحة الإعدادات.
1. في اللوحة اليسارية، انقر على **Toolboxes** تليها **Toolboxes**, **PageControls**, **Sections** و **ContentToolboxSection**, ثم **Tools.**
1. انقر على **إنشاء جديد**.
   يظهر نموذج تسجيل المربع.
1. ملء حقول النموذج على النحو التالي: 
   1. تأكد من اختيار **تمكين**.
   1. أضف ~/Addons/Aspose.SiteFinity.ExportUsersToExcel/AsposeExportUsersToExcel.ascx

   1. في حقل **نوع CLR للتحكم أو المسار الظاهري**.
   1. أضف **الاسم**، **العنوان** و **الوصف** على النحو التالي:
      Aspose.SiteFinity.ExportUsersToExcel
      Aspose Export SiteFinity Users to Excel
      تصدير مستخدمي SiteFinity إلى Excel
   1. يمكنك ترك كافة الحقول الأخرى كما هي.
1. عند الانتهاء، انقر على **حفظ التغييرات**.
   يتم تسجيل العنصر النائب في لوحة الأدوات ويمكن استخدامه في Sitefinity.
## **استخدام وفيديو ديمو**
### **استخدام**
بعد تثبيت وتكوين إضافة Aspose Sitefinity Export Users to Excel، فمن السهل حقًا البدء في استخدامه على موقع الويب الخاص بك. يرجى اتباع هذه الخطوات البسيطة للبدء:

1. تأكد من تسجيل الدخول إلى Sitefinity باستخدام حساب مستوى مسؤول.
1. انتقل إلى الصفحة التي ترغب في إضافة الوظيفة الإضافية لتصديرها. تأكد من فتح الصفحة في وضع التحرير.
1. من القائمة **سحب عناصر واجهة المستخدم** على اليمين، حدد تصدير مستخدمي SiteFinity إلى Excel واسحبه إلى الموضع المناسب.


لقد قمت بإضافة Aspose Sitefinity Export Users to Excel بنجاح.
### **فيديو توضيحي**
يرجى التحقق [من الفيديو](https://www.youtube.com/watch?v=O1524u-Pom4) أدناه لرؤية الوحدة في العمل.
## **الدعم**
منذ الأيام الأولى لـ Aspose ، كنا نعلم أن مجرد منح عملائنا منتجات جيدة لن يكون كافيًا. كنا بحاجة أيضًا إلى تقديم خدمة جيدة. نحن أنفسنا مطورين ونفهم مدى إزعاج القضايا التقنية أو العيوب في البرمجيات التي توقفك عن القيام بما تحتاج إلى القيام به. نحن هنا لحل المشاكل ، وليس لخلقها.

هذا هو السبب في أننا نقدم الدعم المجاني. يستحق أي شخص يستخدم منتجاتنا ، سواء اشتروها أو كانوا يستخدمون تقييمًا ، كامل انتباهنا واحترامنا.

يمكنك تسجيل أي مشاكل أو اقتراحات تتعلق بوحدات Aspose.Cells .NET for Sitefinity باستخدام أي من المنصات التالية

- [جيتهاب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)
## **تمديد والمساهمة**
Aspose Sitefinity Widgets/Modules مفتوحة المصدر وكودها متاح على المواقع الرئيسية لتشفير الشبكات الاجتماعية المدرجة أدناه. يشجع المطورون على تنزيل كود المصدر وتوسيع الوظائف وفقًا لمتطلباتهم الخاصة.

---
title: Sitefinity تصدير المستخدمين إلى Excel
type: docs
weight: 20
url: /ar/net/sitefinity-export-users-to-excel/
---
**ملخص المحتويات**

- [مقدمة](#SitefinityExportUserstoExcel-Introduction)
- [متطلبات النظام والأنظمة الأساسية المدعومة](#SitefinityExportUserstoExcel-SystemRequirementsandSupportedPlatforms) 
  - [متطلبات النظام](#SitefinityExportUserstoExcel-SystemRequirements)
  - [المنصات المدعومة](#SitefinityExportUserstoExcel-SupportedPlatforms)
- [مصدر الرمز](#SitefinityExportUserstoExcel-SourceCode) 
  - [كيفية تكوين شفرة المصدر](#SitefinityExportUserstoExcel-Howtoconfigurethesourcecode)
- [التثبيت والاستخدام](#SitefinityExportUserstoExcel-InstallationandUsage) 
  - [جارى التحميل](#SitefinityExportUserstoExcel-Downloading)
  - [التثبيت](#SitefinityExportUserstoExcel-Installing)
- [استخدام وعرض الفيديو](#SitefinityExportUserstoExcel-UsingandVideoDemo) 
  - [استخدام](#SitefinityExportUserstoExcel-Using)
  - [فيديو تجريبي](#SitefinityExportUserstoExcel-VideoDemo)
- [الدعم](#SitefinityExportUserstoExcel-Support)
- [تمديد والمساهمة](#SitefinityExportUserstoExcel-ExtendandContribute)
## **مقدمة**
Aspose .NET تصدير المستخدمين إلى Excel لـ SiteFinity Module يسمح للمطورين بتصدير مستخدمي SiteFinity إلى Microsoft Excel أو OpenOffice Spreadsheet. توضح هذه الوحدة ميزة إنشاء جداول البيانات القوية التي يوفرها Aspose.Cells.

## **متطلبات النظام والأنظمة الأساسية المدعومة**
### **متطلبات النظام**
من أجل إعداد Aspose.Cells .NET لوظائف Sitefinity الإضافية ، يجب أن يكون لديك المتطلبات التالية:

- يعمل Sitefinity CMS على ASP.NET 4.0

لا تتردد في الاتصال بنا إذا كانت لديك أية مشكلات في إعداد الوظيفة الإضافية لـ Sitefinity.
### **المنصات المدعومة**
الوظيفة الإضافية مدعومة في جميع إصدارات

- يعمل Sitefinity CMS على ASP.NET 4.0
## **مصدر الرمز**
يمكنك الحصول على أحدث كود مصدر من أحد المواقع التالية

- [ جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/SiteFinity)
### **كيفية تكوين شفرة المصدر**
يجب أن يكون لديك ما يلي مثبتًا لفتح كود المصدر وتوسيعه

- Visual Studio 2010 أو أعلى

يرجى اتباع هذه الخطوات البسيطة للبدء

1. تنزيل / استنساخ الكود المصدري.
1.  افتح Visual Studio 2010 واختر**ملف** > **مشروع مفتوح**
1.  استعرض للوصول إلى أحدث كود مصدر قمت بتنزيله وافتح ملف**.sln** ملف.
## **التثبيت والاستخدام**
### **جارى التحميل**
يمكنك تنزيل Aspose .NET Content Exporter لوحدة Sitefinity من أحد المواقع التالية

- [ جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases)
### **التثبيت**
بمجرد التنزيل ، يرجى اتباع هذه الخطوات لتثبيت الوظيفة الإضافية في موقع الويب Sitefinity الخاص بك:

**الخطوة 1: انسخ الملفات إلى تثبيت Sitefinity الخاص بك**

يرجى استخراج ملف ZIP الذي تم تنزيله. ستحتاج إلى FTP أو وصول مباشر إلى مجلد تثبيت Sitefinity على الخادم لإجراء ما يلي:

1.  انسخ Aspose.Cells.dll و Aspose.SiteFinity.ExportUsersToExcel.dll في**سلة مهملات** مجلد تثبيت Sitefinity.
1.  انسخ ال**الإضافات** مجلد على جذر تثبيت Sitefinity حيث يكون ملف**سلة مهملات** يقع المجلد.

**الخطوة 2: قم بتسجيل الوظيفة الإضافية Aspose Sitefinity Content Export في Sitefinity**

1. قم بتسجيل الدخول إلى Sitefinity CMS الخاص بك باستخدام "**مدير** ' الحساب. يمكن الوصول إلى صفحة تسجيل الدخول عن طريق<http://www.mywebsite.com/sitefinity>
1.  انقر**الادارة** وثم**إعدادات**.
تظهر صفحة الإعدادات الأساسية.
1.  انقر على**متقدم** حلقة الوصل.
 تظهر صفحة الإعدادات.
1.  في الجزء الأيمن ، انقر فوق "نعم"**صناديق الأدوات** تليها**صناديق الأدوات** ، ومن بعد**PageControls**, **الأقسام** و**ContentToolboxSection** ، ومن بعد**أدوات.**
1.  انقر**خلق جديد إبداع جديد**.
 يظهر نموذج تسجيل القطعة.
1.  املأ حقول النموذج على النحو التالي:
 1. تأكد**ممكن** تم الإختيار.
 1. أضف ~ / Addons / Aspose.SiteFinity.ExportUsersToExcel / AsposeExportUsersToExcel.ascx

 1. ` `in**التحكم في نوع CLR أو المسار الظاهري** مجال.
 1. أضف**اسم**, **عنوان** و**وصف** كالآتي:
 Aspose.SiteFinity.ExportUsersToExcel
 Aspose تصدير مستخدمي SiteFinity إلى Excel
 تصدير مستخدمي SiteFinity إلى Excel
 1. يمكنك ترك جميع الحقول الأخرى كما هي.
1.  عند الانتهاء ، انقر فوق**احفظ التغييرات**.
 يتم تسجيل عنصر واجهة المستخدم في صندوق الأدوات ويمكن استخدامه في Sitefinity.
## **استخدام وعرض الفيديو**
### **استخدام**
بعد تثبيت وتكوين الوظيفة الإضافية Aspose Sitefinity Export Users to Excel ، من السهل حقًا البدء في استخدامها على موقع الويب الخاص بك. يرجى اتباع هذه الخطوات البسيطة للبدء:

1. تأكد من تسجيل الدخول إلى Sitefinity بحساب مستوى المسؤول.
1. انتقل إلى الصفحة حيث تريد إضافة وظيفة التصدير الإضافية. تأكد من فتح الصفحة في وضع التحرير.
1.  من**أدوات السحب** القائمة على اليمين ، حدد Aspose تصدير المستخدمين إلى Excel واسحبه إلى الموضع.


لقد نجحت في إضافة Aspose Sitefinity Export Users إلى Excel.
### **فيديو تجريبي**
 يرجى المراجعة[الفيديو](https://www.youtube.com/watch?v=O1524u-Pom4) أدناه للاطلاع على الوحدة قيد التنفيذ.
## **الدعم**
منذ الأيام الأولى من Aspose ، علمنا أن مجرد تقديم منتجات جيدة لعملائنا لن يكون كافيًا. كنا بحاجة أيضًا إلى تقديم خدمة جيدة. نحن مطورون بأنفسنا ونفهم مدى الإحباط عندما تمنعك مشكلة فنية أو غرابة في البرنامج من القيام بما تحتاج إلى القيام به. نحن هنا لحل المشاكل وليس خلقها.

هذا هو السبب في أننا نقدم الدعم المجاني. أي شخص يستخدم منتجاتنا ، سواء اشتراها أو استخدم تقييمًا ، يستحق كامل اهتمامنا واحترامنا.

يمكنك تسجيل أي مشكلات أو اقتراحات تتعلق بـ Aspose.Cells .NET لوحدات Sitefinity النمطية باستخدام أي من الأنظمة الأساسية التالية

- [ جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)
## **تمديد والمساهمة**
Aspose Sitefinity Widgets / Modules مفتوحة المصدر وكودها المصدر متاح على مواقع الترميز الاجتماعي الرئيسية المدرجة أدناه. يتم تشجيع المطورين على تنزيل الكود المصدري وتوسيع الوظائف وفقًا لمتطلباتهم الخاصة.

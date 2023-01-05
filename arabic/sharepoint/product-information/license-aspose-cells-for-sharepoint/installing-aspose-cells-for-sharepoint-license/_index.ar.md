---
title: تثبيت ترخيص Aspose.Cells for SharePoint
type: docs
weight: 10
url: /ar/sharepoint/installing-aspose-cells-for-sharepoint-license/
---
{{% alert color="primary" %}}

 بمجرد أن تصبح سعيدًا بملف[تقييم](/cells/ar/sharepoint/evaluate-aspose-cells/), [شراء رخصة](https://purchase.aspose.com/buy).

قبل الشراء ، تأكد من أنك تفهم وتوافق على شروط اشتراك الترخيص.

{{% /alert %}}

يتم إرسال الترخيص إليك عبر البريد الإلكتروني عند دفع الطلب. الترخيص عبارة عن أرشيف مضغوط يحتوي على حزمة حلول SharePoint عادية.

يحتوي الترخيص ZIP على:

- **Aspose.Cells.SharePoint.License.wsp** - ملف حزمة حلول SharePoint. يتم حزم ترخيص Aspose.Cells for SharePoint كحل SharePoint لتسهيل النشر والسحب عبر مزرعة الخوادم.
- **readme.txt** تعليمات تثبيت الترخيص. يتم إجراء تثبيت الترخيص من وحدة تحكم الخادم عبر ملف**stsadm.exe**. فيما يلي الخطوات المطلوبة لتثبيت الترخيص.

#### **تثبيت الترخيص**

{{% alert color="primary" %}}

 تم حذف المسارات من أجل الوضوح. أضف المسار الفعلي إلى**stsadm.exe** و / أو ملف الحل عند تنفيذ الخطوات أدناه.

{{% /alert %}}

1. قم بتشغيل stsadm لإضافة الحل إلى متجر حلول SharePoint:
 stsadm.exe -o addolution -filename Aspose.Cells.SharePoint.License.wsp
1. انشر الحل على جميع الخوادم في المزرعة:
 stsadm.exe -o نشر الحل -الاسم Aspose.Cells.SharePoint.License.wsp - فوري - القوة
1. قم بتنفيذ وظائف المؤقت الإداري لإكمال النشر على الفور:
 stsadm.exe -o execadmsvcjobs

{{% alert color="primary" %}}

 ستتلقى تحذيرًا عند تشغيل خطوة النشر إذا لم تبدأ خدمة إدارة SharePoint Services Windows.**Stsadm.exe**يعتمد على هذه الخدمة و Windows SharePoint Timer Service لنسخ بيانات الحل عبر المزرعة. إذا لم تكن هذه الخدمات قيد التشغيل في مزرعة الخوادم الخاصة بك ، فقد تحتاج إلى نشر الترخيص بشكل منفصل لكل خادم.

{{% /alert %}}

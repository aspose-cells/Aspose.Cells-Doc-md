---
title: تثبيت ترخيص Aspose.Cells for SharePoint
type: docs
weight: 10
url: /ar/sharepoint/installing-aspose-cells-for-sharepoint-license/
---

{{% alert color="primary" %}}

بمجرد أن تكون راضيًا عن [التقييم الخاص بك](/cells/ar/sharepoint/evaluate-aspose-cells/)، [اشترِ ترخيصًا](https://purchase.aspose.com/buy).

قبل الشراء، تأكد من أنك تفهم وتوافق على شروط الاشتراك في الترخيص.

{{% /alert %}}

يتم ارسال الترخيص إليك عبر البريد الإلكتروني عندما يتم دفع الطلب. الترخيص هو ملف ZIP يحتوي على حزمة حلول SharePoint العادية.

ZIP الترخيص يحتوي على:

- **Aspose.Cells.SharePoint.License.wsp** – ملف حزمة حل SharePoint. يتم تعبئة الترخيص Aspose.Cells for SharePoint كحل SharePoint لتسهيل النشر والانحسار عبر مزرعة الخادم.
- **readme.txt** – تعليمات تثبيت الترخيص. يتم أداء تثبيت الترخيص من وحدة التحكم للخادم عبر **stsadm.exe**. الخطوات المطلوبة لتثبيت الترخيص مذكورة أدناه.

#### **تثبيت الترخيص**

{{% alert color="primary" %}}

تم حذف المسارات لأسباب وضوح. أضف المسار الفعلي لـ **stsadm.exe** و/أو ملف الحل عند تنفيذ الخطوات أدناه.

{{% /alert %}}

1. تشغيل stsadm لإضافة الحل إلى مخزن حلول SharePoint:
   stsadm.exe -o addsolution -filename Aspose.Cells.SharePoint.License.wsp
2. نشر الحل على جميع الخوادم في المزرعة:
   stsadm.exe -o deploysolution -name Aspose.Cells.SharePoint.License.wsp -immediate -force
3. تنفيذ أعمال توقيت إدارية لإكمال النشر على الفور:
   stsadm.exe -o execadmsvcjobs

{{% alert color="primary" %}}

سوف تتلقى تحذير عند تشغيل خطوة النشر إذا لم يتم بدء خدمة إدارة خدمات Windows SharePoint. يعتمد **Stsadm.exe** على هذه الخدمة وخدمة Windows SharePoint Timer لتكرير بيانات الحل عبر المزرعة. إذا لم تكن هذه الخدمات قيد التشغيل في مزرعة الخوادم الخاصة بك، فقد تحتاج إلى نشر الترخيص على كل خادم على حدة.

{{% /alert %}}

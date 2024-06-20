---
title: إلغاء تثبيت الترخيص Aspose.Cells for SharePoint
type: docs
weight: 30
url: /ar/sharepoint/uninstalling-aspose-cells-for-sharepoint-license/
---

{{% alert color="primary" %}} 

لإلغاء ترخيص Aspose.Cells for SharePoint، يرجى استخدام الخطوات أدناه من وحدة التحكم للخادم. 

{{% /alert %}} 

1. سحب حل الترخيص من المزرعة:
   stsadm.exe -o retractsolution -name Aspose.Cells.SharePoint.License.wsp -immediate
1. تنفيذ وظائف الموقت الإدارية لإكمال الانحسار على الفور:
   stsadm.exe -o execadmsvcjobs
1. انتظر حتى يكتمل السحب.
   يمكنك استخدام الإدارة المركزية للتحقق مما إذا كانت عملية السحب قد اكتملت من خلال الانتقال إلى **الإدارة المركزية**, ثم **العمليات** و **إدارة الحلول**.
1. قم بإزالة الحل من مستودع حلول SharePoint:
   stsadm.exe -o deletesolution -name Aspose.Cells.SharePoint.License.wsp

---
title: إلغاء تثبيت ترخيص Aspose.Cells for SharePoint
type: docs
weight: 30
url: /ar/sharepoint/uninstalling-aspose-cells-for-sharepoint-license/
---
{{% alert color="primary" %}} 

 لإلغاء تثبيت ترخيص Aspose.Cells for SharePoint ، يرجى استخدام الخطوات أدناه من وحدة تحكم الخادم.

{{% /alert %}} 

1. سحب حل الترخيص من المزرعة:
 stsadm.exe -o retractsolution -name Aspose.Cells.SharePoint.License.wsp - فوري
1. قم بتنفيذ وظائف المؤقت الإداري لإكمال التراجع على الفور:
 stsadm.exe -o execadmsvcjobs
1. انتظر حتى يكتمل التراجع.
 يمكنك استخدام الإدارة المركزية للتحقق مما إذا كان التراجع قد اكتمل بالذهاب إلى**الإدارة المركزية** ، ومن بعد**عمليات** و**إدارة الحلول**.
1. قم بإزالة الحل من متجر حلول SharePoint:
 stsadm.exe -o حذف الحل -اسم Aspose.Cells.SharePoint.License.wsp

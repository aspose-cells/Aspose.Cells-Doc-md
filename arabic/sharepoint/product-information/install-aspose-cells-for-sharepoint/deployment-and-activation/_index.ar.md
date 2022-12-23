---
title: النشر والتفعيل
type: docs
weight: 20
url: /ar/sharepoint/deployment-and-activation/
---
{{% alert color="primary" %}} 

[تركيب Aspose.Cells for SharePoint](/cells/ar/sharepoint/installing-aspose-cells-for-sharepoint/) يرشدك خلال عملية التثبيت. تشرح هذه المقالة ما يتم نشر عملية التثبيت وتنشيطها.

{{% /alert %}} 
### **تعيين**
Aspose.Cells for SharePoint يقوم بتنفيذ الإجراءات التالية أثناء النشر:

1.  التثبيتات**Aspose.Cells.SharePoint.dll** في Global Assembly Cache ويضيف إدخال SafeControl إلى**web.config** ملف.
1. تثبيت بيان الميزة والملفات الضرورية الأخرى في الدلائل المناسبة.
1. يسجل الميزة في قاعدة بيانات SharePoint ويجعلها متاحة للتنشيط في نطاق الميزة.
### **التنشيط**
 يتم حزم Aspose.Cells for SharePoint كميزة مستوى مستوى الموقع (مجموعة المواقع المشتركة) ويمكن تنشيطها وإلغاء تنشيطها في مجموعات الموقع.

أثناء التنشيط ، تقوم الميزة بإجراء بعض التغييرات على الدليل الظاهري لتطبيق الويب الأصل لمجموعة المواقع المشتركة:

1. يضيف صفحة إعدادات التحويل إلى ملف خريطة الموقع.
1. نسخ ملفات الموارد الضرورية إلى مجلد App_GlobalResources في الدليل الظاهري.

---
title: النشر والتنشيط
type: docs
weight: 20
url: /ar/sharepoint/deployment-and-activation/
---

{{% alert color="primary" %}} 

[تثبيت Aspose.Cells for SharePoint](/cells/ar/sharepoint/installing-aspose-cells-for-sharepoint/) يرشدك خلال عملية التثبيت. يشرح هذا المقال ما هي عملية التثبيت والتنشيط.

{{% /alert %}} 
### **النشر**
يؤدي Aspose.Cells for SharePoint إلى الإجراءات التالية أثناء النشر:

1. يقوم بتثبيت **Aspose.Cells.SharePoint.dll** في ذاكرة التخزين المؤقت العامة ويضيف إدخال SafeControl إلى ملف **web.config**.
2. يثبت تصريح الميزة والملفات الأخرى اللازمة في الدلائل المناسبة.
3. يسجل الميزة في قاعدة البيانات SharePoint ويجعلها متاحة للتنشيط على نطاق الميزة.
### **التنشيط**
Aspose.Cells for SharePoint محزم كميزة على مستوى الموقع (المجموعة الرئيسية) ويمكن تفعيله وإلغاء تنشيطه على مجموعات المواقع. 

خلال التفعيل، تقوم الخاصية بإجراء بعض التغييرات على الدليل الظاهري لتطبيق الويب الأصلي لمجموعة المواقع:

1. يضيف صفحة إعدادات التحويل إلى ملف خريطة الموقع.
1. ينسخ الملفات الموارد الضرورية إلى مجلد App_GlobalResources في الدليل الظاهري.

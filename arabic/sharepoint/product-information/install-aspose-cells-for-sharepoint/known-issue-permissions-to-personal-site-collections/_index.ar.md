﻿---
title: المشكلة المعروفة - أذونات مجموعات الموقع الشخصية
type: docs
weight: 40
url: /ar/sharepoint/known-issue-permissions-to-personal-site-collections/
---
{{% alert color="primary" %}} 

لا يمنح SharePoint افتراضيًا أذونات كاملة لإدارة المواقع الشخصية لمسؤولي البوابة. لهذا السبب قد يفشل التنشيط وإلغاء التنشيط على مجموعة مواقع مشتركة عندما يتم تنفيذها بواسطة مسؤولي المدخل. يتضمن هذا التنشيط وإلغاء التنشيط أثناء الإعداد.

{{% /alert %}} 
### **منح الإذن للمواقع الشخصية**
عند حدوث هذه المشكلة أثناء التثبيت ، يتم تسجيل UnauthorizedAccessException على Microsoft.SharePoint.SPFeature.Activate () إلى سجل تتبع SharePoint. عندما يفشل إلغاء التنشيط كجزء من إلغاء التثبيت ، يتم عرض UnauthorizedAccessException على شاشة الإعداد الأخيرة لإلغاء التنشيط (عمليات) الفاشلة.

لمنع هذه المشكلة ، امنح مسؤولي البوابة الإذن لإدارة تطبيق MySite Web:

1.  اذهب إلى**إدارة SharePoint المركزية**وحدد ملف**الإدارة التطبيقية** التبويب.
1.  أختر**سياسة تطبيق الويب** تحت**أمان التطبيق** مجموعة.
1.  تأكد من تحديد تطبيق الويب الصحيح لـ "My Site" في**تطبيق الويب** قائمة على اليمين.
1.  يختار**أضف مستخدمين** أعلى اليسار.
1.  أختر**كل المناطق** بشكل افتراضي على**أضف مستخدمين** الشاشة والنقر**التالي**.
1. أضف المستخدم (المستخدمين) المناسب أو مجموعة الدليل النشط التي تريد التحكم فيها في تطبيق الويب "My Site".
1.  حدد مستوى التحكم.

   **إضافة المستخدمين وضبط مستوى التحكم** 

![ما يجب القيام به: image_بديل_نص](known-issue-permissions-to-personal-site-collections_1.png)




1.  انقر**ينهي**.

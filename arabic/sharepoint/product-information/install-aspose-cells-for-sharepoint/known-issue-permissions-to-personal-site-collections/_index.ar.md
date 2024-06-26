---
title: مشكلة معروفة  الأذونات لمجموعات المواقع الشخصية
type: docs
weight: 40
url: /ar/sharepoint/known-issue-permissions-to-personal-site-collections/
---

{{% alert color="primary" %}} 

بشكل افتراضي، لا تمنح SharePoint أذونات كاملة لإدارة المواقع الشخصية إلى مسؤولي البوابة. لهذا السبب قد يفشل التنشيط والإلغاء على مجموعة مواقع شخصية عند قيام المسؤولين بالبوابة بها. وهذا يشمل التنشيط والإلغاء خلال عملية الإعداد.

{{% /alert %}} 
### **منح الأذونات للمواقع الشخصية**
عند حدوث هذه المشكلة أثناء التثبيت، يتم تسجيل UnauthorizedAccessException في سجل تتبع SharePoint SPFeature.Activate(). عند فشل الإلغاء كجزء من إزالة التثبيت، يتم عرض UnauthorizedAccessException على الشاشة الأخيرة للإعداد للإلغاء. الفشل.

لمنع هذه المشكلة، قم بمنح مسؤولي بوابة الإذن بإدارة تطبيق الويب الخاص بـ MySite:

1. انتقل إلى **إدارة SharePoint المركزية** وحدد علامة تبويب **إدارة التطبيقات**.
1. اختر **سياسة تطبيق الويب** تحت مجموعة **أمان التطبيق**.
1. تأكد من اختيار تطبيق الويب الصحيح لـ "My Site" في قائمة **تطبيق الويب** على اليمين.
1. حدد **إضافة مستخدمين** في الأعلى على اليسار.
1. اختر **جميع المناطق** افتراضيًا على شاشة **إضافة المستخدمين** وانقر على **التالي**.
1. أضف المستخدم(ين) المناسب(ين) أو مجموعة الدليل النشط التي ترغب في السيطرة على تطبيق الويب "My Site" الخاص بك.
1. حدد مستوى السيطرة. 

   **إضافة المستخدمين وضبط مستوى السيطرة** 

![todo:image_alt_text](known-issue-permissions-to-personal-site-collections_1.png)




1. انقر على **إنهاء**.

---
title: تشفير وفك تشفير ملفات Excel
type: docs
weight: 10
url: /ar/net/encrypt-and-decrypt-excel-files/
description: كيفية تشفير وفك تشفير ملفات Excel باستخدام C#. قفل وفتح ملفات Excel.
---

{{% alert color="primary" %}}

Microsoft Excel (97 - 365) يتيح لك تشفير وحماية كلمة مرور جداول البيانات الخاصة بك. تستخدم خوارزميات المزود الخدمي الكريبتوجرافي، أو CSP، مجموعة من الخوارزميات الكريبتوجرافية ذات خصائص مختلفة. CSP الافتراضي هو 'Office 97/2000 Compatible' أو 'Weak Encryption (XOR)'. من المهم اختيار طول مفتاح التشفير المناسب. بعض CSPs لا تدعم أكثر من 40 أو 56 بت. يعتبر ذلك تشفير ضعيف. للحصول على تشفير قوي، يتطلب طول مفتاح أدنى لـ 128 بت. تحتوي نوافذ Microsoft على CSPs تقدم أنواع تشفير قوية أيضًا، على سبيل المثال 'مزود تشفير قوي من Microsoft'. لإعطائك فكرة، تشفير 128 بت هو ما تستخدمه البنوك لتشفير الاتصال مع أنظمة الخدمات المصرفية عبر الإنترنت الخاصة بهم.

تسمح Aspose.Cells لك بتشفير وحماية ملفات Microsoft Excel بنوع التشفير الذي ترغب فيه.

{{% /alert %}}

## **استخدام Microsoft Excel**

لضبط إعدادات تشفير الملف في Microsoft Excel (هنا Microsoft Excel 2003):

1. من قائمة **الأدوات**، حدد **الخيارات**. ستظهر نافذة حوارية.
١. حدد علامة التبويب **الأمان**.
1. أدخل كلمة مرور وانقر **متقدم**
١. اختر نوع التشفير وقم بتأكيد كلمة المرور.

## **تشفير ملف Excel باستخدام Aspose.Cells**

المثال التالي يوضح كيفية تشفير وحماية ملف Excel بكلمة مرور باستخدام واجهة برمجة التطبيقات Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-1.cs" >}}

### **تحديد كلمة المرور لخيار تعديل**

المثال التالي يوضح كيفية ضبط خيار Microsoft Excel **كلمة المرور للتعديل** لملف موجود باستخدام واجهة برمجة التطبيقات Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-SpecifyPasswordToModifyOption.cs" >}}


## **فك تشفير ملف Excel باستخدام Aspose.Cells**
من السهل جداً فتح ملف Excel المحمي بكلمة مرور وفك تشفيره باستخدام واجهة برمجة التطبيقات Aspose.Cells كما يلي:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Decrypt-Excel-File.cs" >}}


## **مواضيع متقدمة**
- [تشفير وفك تشفير ملفات ODS](/cells/ar/net/encrypt-and-decrypt-ods-files/)
- [ضبط نوع التشفير القوي](/cells/ar/net/setting-strong-encryption-type/)
- [تحديد المؤلف أثناء حماية كتاب العمل](/cells/ar/net/specify-author-while-write-protecting-workbook/)
- [التحقق من كلمة مرور الملفات المشفرة](/cells/ar/net/verify-password-of-encrypted-excel-and-ods-files/)


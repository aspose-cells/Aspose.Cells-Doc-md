---
title: تشفير وفك تشفير ملفات Excel
type: docs
weight: 10
url: /ar/python-net/encrypt-and-decrypt-excel-files/
description: كيفية تشفير وفك تشفير ملفات Excel باستخدام Python. قفل وفتح ملفات Excel.
---

{{% alert color="primary" %}}

Microsoft Excel (97 - 365) يتيح لك تشفير وحماية كلمة مرور جداول البيانات الخاصة بك. تستخدم خوارزميات المزود الخدمي الكريبتوجرافي، أو CSP، مجموعة من الخوارزميات الكريبتوجرافية ذات خصائص مختلفة. CSP الافتراضي هو 'Office 97/2000 Compatible' أو 'Weak Encryption (XOR)'. من المهم اختيار طول مفتاح التشفير المناسب. بعض CSPs لا تدعم أكثر من 40 أو 56 بت. يعتبر ذلك تشفير ضعيف. للحصول على تشفير قوي، يتطلب طول مفتاح أدنى لـ 128 بت. تحتوي نوافذ Microsoft على CSPs تقدم أنواع تشفير قوية أيضًا، على سبيل المثال 'مزود تشفير قوي من Microsoft'. لإعطائك فكرة، تشفير 128 بت هو ما تستخدمه البنوك لتشفير الاتصال مع أنظمة الخدمات المصرفية عبر الإنترنت الخاصة بهم.

يسمح Aspose.Cells للبايثون via .NET بتشفير وحماية ملفات Microsoft Excel بكلمة مرور ونوع التشفير الذي تريده.

{{% /alert %}}

## **استخدام Microsoft Excel**

لضبط إعدادات تشفير الملف في Microsoft Excel (هنا Microsoft Excel 2003):

1. من قائمة **الأدوات**، حدد **الخيارات**. ستظهر نافذة حوارية.
١. حدد علامة التبويب **الأمان**.
1. أدخل كلمة مرور وانقر **متقدم**
١. اختر نوع التشفير وقم بتأكيد كلمة المرور.

## **تشفير ملف Excel باستخدام Aspose.Cells**

يعرض المثال التالي كيفية تشفير وحماية كلمة مرور لملف إكسل باستخدام واجهة برمجة التطبيقات Aspose.Cells لبايثون via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-EncryptingFiles-1.py" >}}

### **تحديد كلمة المرور لخيار تعديل**

يعرض المثال التالي كيفية تعيين خيار **كلمة المرور للتعديل** لملف إكسل Microsoft Excel لملف موجود باستخدام واجهة برمجة التطبيقات Aspose.Cells لبايثون via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-SpecifyPasswordToModifyOption.py" >}}


## **فك تشفير ملف Excel باستخدام Aspose.Cells**
من السهل جدًا فتح ملف إكسل محمي بكلمة مرور وفك تشفيره باستخدام واجهة برمجة التطبيقات Aspose.Cells لبايثون via .NET كما في الرموز التالية:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-Decrypt-Excel-File.py" >}}


## **مواضيع متقدمة**
- [تشفير وفك تشفير ملفات ODS](/cells/ar/python-net/encrypt-and-decrypt-ods-files/)
- [ضبط نوع التشفير القوي](/cells/ar/python-net/setting-strong-encryption-type/)
- [تحديد المؤلف أثناء حماية كتاب العمل](/cells/ar/python-net/specify-author-while-write-protecting-workbook/)
- [التحقق من كلمة مرور الملفات المشفرة](/cells/ar/python-net/verify-password-of-encrypted-excel-and-ods-files/)

{{< app/cells/assistant language="python-net" >}}

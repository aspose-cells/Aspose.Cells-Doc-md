---
title: تشفير وفك تشفير ملفات Excel
type: docs
weight: 10
url: /ar/net/encrypt-and-decrypt-excel-files/
description: كيفية تشفير وفك تشفير ملفات Excel باستخدام C#. قفل وفتح ملفات Excel.
---
{{% alert color="primary" %}}

يمكّنك Microsoft Excel (97 - 365) من تشفير جداول البيانات وحمايتها بكلمة مرور. يستخدم الخوارزميات التي يوفرها مزود خدمة التشفير ، أو CSP ، وهي مجموعة من خوارزميات التشفير ذات الخصائص المختلفة. CSP الافتراضي هو "متوافق مع Office 97/2000" أو "تشفير ضعيف (XOR)". من المهم اختيار طول مفتاح التشفير المناسب. لا يدعم بعض CSPs أكثر من 40 أو 56 بت. يعتبر هذا تشفير ضعيف. للتشفير القوي ، يجب ألا يقل طول المفتاح عن 128 بت. يحتوي Microsoft Windows على CSPs الذين يقدمون أنواع تشفير قوية أيضًا ، على سبيل المثال "موفر التشفير القوي Microsoft". لإعطائك فكرة ، تشفير 128 بت هو ما تستخدمه البنوك لتشفير الاتصال بأنظمتها المصرفية عبر الإنترنت.

يسمح لك Aspose.Cells بتشفير وحماية كلمة مرور Microsoft ملفات Excel بنوع التشفير المطلوب.

{{% /alert %}}

## **باستخدام Microsoft إكسل**

لتعيين إعدادات تشفير الملفات في Microsoft Excel (هنا Microsoft Excel 2003):

1.  من**أدوات** القائمة ، حدد**خيارات**سيظهر مربع حوار.
1.  حدد ملف**حماية** التبويب.
1.  أدخل كلمة مرور وانقر**متقدم**
1. اختر نوع التشفير وقم بتأكيد كلمة المرور.

## **تشفير ملف إكسل باستخدام Aspose.Cells**

يوضح المثال التالي كيفية تشفير وحماية كلمة المرور لملف excel باستخدام Aspose.Cells API.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-1.cs" >}}

### **تحديد كلمة المرور لتعديل الخيار**

 يوضح المثال التالي كيفية تعيين ملف**كلمة مرور للتعديل** خيار Microsoft Excel لملف موجود باستخدام Aspose.Cells API.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-SpecifyPasswordToModifyOption.cs" >}}


## **فك تشفير ملف Excel باستخدام Aspose.Cells**
من السهل جدًا فتح ملف Excel للحماية بكلمة مرور وفك تشفير باستخدام Aspose.Cells API على النحو التالي:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Decrypt-Excel-File.cs" >}}


## **موضوعات مسبقة**
- [تشفير وفك تشفير ملفات ODS](/cells/ar/net/encrypt-and-decrypt-ods-files/)
- [تحديد نوع التشفير القوي](/cells/ar/net/setting-strong-encryption-type/)
- [حدد المؤلف أثناء كتابة حماية المصنف](/cells/ar/net/specify-author-while-write-protecting-workbook/)
- [تحقق من كلمة المرور للملفات المشفرة](/cells/ar/net/verify-password-of-encrypted-excel-and-ods-files/)


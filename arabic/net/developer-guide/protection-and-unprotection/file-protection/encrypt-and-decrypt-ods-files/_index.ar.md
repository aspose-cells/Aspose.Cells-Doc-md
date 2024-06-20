---
title: تشفير وفك تشفير ملفات ODS
type: docs
weight: 10
url: /ar/net/encrypt-and-decrypt-ods-files/
description: حماية كلمة المرور وتشفير ملفات ODS باستخدام Aspose.Cells لـ .Net وهي مكتبة نقية .Net.
---

{{% alert color="primary" %}}
OpenOffice.org هو حزمة مكتبية كاملة الميزات تدعم حماية كلمة المرور وتشفير الملفات. ومع ذلك، يمكن فتح ملف ODS المُشفر فقط بواسطة OpenOffice بعد تقديم كلمة المرور. لا يمكن لإكسيل فتح ملف ODS المُشفر وقد يُعرِض رسالة تحذير. خيارات التشفير غير قابلة للتطبيق على ملفات ODS على عكس أنواع الملفات الأخرى. 
يسمح Aspose.Cells بتشفير وفك تشفير ملف ODS. يمكن فتح ملف ODS المفكك في كل من إكسيل وOpenOffice. 
{{% /alert %}}

## **التشفير باستخدام OpenOffice Calc**
1. حدد **حفظ ك** وانقر على مربع **حفظ بكلمة مرور**.
1. انقر على زر **حفظ**.
1. اكتب كلمة المرور المطلوبة في حقلي **أدخل كلمة المرور للفتح** و **تأكيد كلمة المرور** في نافذة تعيين كلمة المرور التي تفتح. 
1. انقر على زر **موافق** لحفظ الملف.

## **تشفير ملف ODS باستخدام Aspose.Cells لـ .Net**
لتشفير ملف ODS، قم بتحميل الملف وتعيين القيمة [**WorkbookSettings.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) إلى كلمة المرور الفعلية قبل حفظه. يمكن فتح ملف ODS المشفر الناتج في OpenOffice فقط.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingODSFiles-1.cs" >}}

## **فك تشفير ملف ODS باستخدام Aspose.Cells لـ .Net**

لفك تشفير ملف ODS، قم بتحميل الملف عن طريق تقديم كلمة مرور في [**LoadOptions.Password**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/password). بمجرد تحميل الملف، ضبط السلسلة [**WorkbookSettings.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) على القيمة الخالية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-DecryptingODSFiles-1.cs" >}}

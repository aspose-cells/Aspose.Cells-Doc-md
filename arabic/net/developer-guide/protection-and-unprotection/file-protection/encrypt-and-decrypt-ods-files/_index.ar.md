---
title: تشفير وفك تشفير ملفات ODS
type: docs
weight: 10
url: /ar/net/encrypt-and-decrypt-ods-files/
description: حماية كلمة المرور وتشفير ملفات ODS باستخدام Aspose.Cells لـ .Net وهي مكتبة شبكية خالصة.
---
{{% alert color="primary" %}}
 OpenOffice.org عبارة عن مجموعة مكتبية كاملة الميزات تدعم حماية كلمة المرور وتشفير الملفات. ومع ذلك ، لا يمكن فتح ملف ODS المشفر إلا بواسطة OpenOffice بعد توفير كلمة المرور. لا يمكن لبرنامج Excel فتح ملف ODS المشفر وقد يرفع رسالة تحذير. لا تنطبق خيارات التشفير على ملف ODS بخلاف أنواع الملفات الأخرى.
 Aspose.Cells يسمح بتشفير وفك تشفير ملف ODS. يمكن فتح ملف ODS الذي تم فك تشفيره في كل من Excel و OpenOffice ،
{{% /alert %}}

## **تشفير باستخدام OpenOffice Calc**
1.  يختار**حفظ باسم** وانقر فوق ملف**حفظ بكلمة مرور** علبة.
1.  انقر على**يحفظ** زر.
1.  اكتب كلمة المرور التي تريدها في كلا الملفين**أدخل كلمة المرور للفتح** و**تأكيد كلمة المرور** الحقول في نافذة تعيين كلمة المرور التي تفتح.
1.  انقر على**نعم** زر لحفظ الملف.

## **قم بتشفير ملف ODS باستخدام Aspose.Cells لـ .Net**
 لتشفير ملف ODS ، قم بتحميل الملف واضبط الامتداد[**إعدادات المصنف**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) قيمة كلمة المرور الفعلية قبل حفظها. يمكن فتح ملف ODS المشفر الناتج في OpenOffice فقط.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingODSFiles-1.cs" >}}

## **فك تشفير ملف ODS باستخدام Aspose.Cells لـ .Net**

 لفك تشفير ملف ODS ، قم بتحميل الملف عن طريق توفير كلمة مرور في ملف[**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/password) . بمجرد تحميل الملف ، اضبط ملف[**إعدادات المصنف**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) سلسلة لاغية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-DecryptingODSFiles-1.cs" >}}

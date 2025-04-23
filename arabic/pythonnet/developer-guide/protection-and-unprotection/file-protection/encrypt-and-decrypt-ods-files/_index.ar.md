---
title: تشفير وفك تشفير ملفات ODS
type: docs
weight: 10
url: /ar/python-net/encrypt-and-decrypt-ods-files/
description: حماية بكلمة مرور وتشفير ملفات ODS باستخدام Aspose.Cells for Python via .NET والذي هو مكتبة NET خالصة.
---

{{% alert color="primary" %}}
OpenOffice.org هو حزمة مكتبية كاملة الميزات تدعم حماية كلمة المرور وتشفير الملفات. ومع ذلك، يمكن فتح ملف ODS المُشفر فقط بواسطة OpenOffice بعد تقديم كلمة المرور. لا يمكن لإكسيل فتح ملف ODS المُشفر وقد يُعرِض رسالة تحذير. خيارات التشفير غير قابلة للتطبيق على ملفات ODS على عكس أنواع الملفات الأخرى. 
ASPose.Cells for Python via .NET يسمح بالتشفير وفك التشفير لملف ODS. يمكن فتح ملف ODS المفكوك التشفير في Excel و OpenOffice، 
{{% /alert %}}

## **التشفير باستخدام OpenOffice Calc**
1. حدد **حفظ ك** وانقر على مربع **حفظ بكلمة مرور**.
1. انقر على زر **حفظ**.
1. اكتب كلمة المرور المطلوبة في حقلي **أدخل كلمة المرور للفتح** و **تأكيد كلمة المرور** في نافذة تعيين كلمة المرور التي تفتح. 
1. انقر على زر **موافق** لحفظ الملف.

## **تشفير ملف ODS باستخدام Aspose.Cells for Python via .NET**
لتشفير ملف ODS، قم بتحميل الملف وتعيين القيمة [**WorkbookSettings.password**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/password) إلى كلمة المرور الفعلية قبل حفظه. يمكن فتح ملف ODS المشفر الناتج في OpenOffice فقط.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-EncryptingODSFiles-1.py" >}}

## **فك تشفير ملف ODS باستخدام Aspose.Cells for Python via .NET**

لفك تشفير ملف ODS، قم بتحميل الملف عن طريق تقديم كلمة مرور في [**LoadOptions.password**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/password). بمجرد تحميل الملف، ضبط السلسلة [**WorkbookSettings.password**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/password) على القيمة الخالية.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-DecryptingODSFiles-1.py" >}}


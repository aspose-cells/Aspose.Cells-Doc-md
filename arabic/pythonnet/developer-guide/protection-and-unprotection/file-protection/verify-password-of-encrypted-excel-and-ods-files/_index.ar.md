---
title: التحقق من كلمة مرور الملفات المشفرة
type: docs
weight: 10
url: /ar/python-net/verify-password-of-encrypted-excel-and-ods-files/
description: التحقق من كلمة المرور لملفات إكسل (xlsx، xlsb، xls، xlsm) وملفات Open office (ODS) المشفرة باستخدام كود CShape.
---

{{% alert color="primary" %}}
إذا كانت ملفات إكسل (xlsx، xlsb، xls، xlsm) وملفات Open office (ODS) مقفلة بكلمة مرور، تدعم Aspose التحقق البسيط من كلمة المرور دون معالجة بيانات محددة للملفات.
{{% /alert %}}

## **تحقق من كلمة المرور للملف المُشفر**

للتحقق من كلمة مرور الملف المشفر، يوفر Aspose.Cells for Python via .NET طريقة [**verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformatutil/verify_password). تقبل هذه الطرق معامليْن، تيار الملف وكلمة المرور التي تحتاج للتحقق.
يوضح مقتطف الشيفرة التالي استخدام الطريقة [**verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformatutil/verify_password) للتحقق مما إذا كانت كلمة المرور المقدمة صالحة أم لا.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-VerifyPassword-1.py" >}}


{{< app/cells/assistant language="python-net" >}}

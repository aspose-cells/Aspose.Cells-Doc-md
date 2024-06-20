---
title: مستندات PDF الآمنة
type: docs
weight: 120
url: /ar/python-net/secure-pdf-documents/
description: تعلم كيفية تمرير خيارات الأمان في PDF عند حفظ جداول البيانات إلى ملفات PDF باستخدام Aspose.Cells for Python via .NET API.
keywords: كتابة خيارات الأمان إلى ملف PDF، تشفير مستند PDF باستخدام Python 
---

{{% alert color="primary" %}}

في بعض الأحيان، يحتاج المطورون إلى العمل مع ملفات PDF المُشفرة. على سبيل المثال:

- تأمين المستندات بكلمات مرور للمالك والمستخدم حتى لا يمكن لأي شخص فتحه.
- تعيين قيود أو أذونات للمستند بعد فتحه، على سبيل المثال: تقييد ما إذا كان بإمكان محتوى المستند أن يُطبع أو يستخرج.

يشرح هذا المقال كيفية تمرير خيارات أمان PDF عند حفظ الجداول الإلكترونية إلى PDF.

{{% /alert %}}

توفر Aspose.Cells for Python via .NET [**PdfSecurityOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/) للعمل مع الأمان. يمكنك تعيين كلمات سر المالك والمستخدم أثناء الحفظ إلى صيغة PDF. سيتعين الرقم السري للمالك أو الرقم السري للمستخدم لفتح المستند المشفر بصيغة PDF للعرض.

- يمكن أن تكون كلمة المرور للمستخدم فارغة أو سلسلة فارغة، في هذه الحالة لن يكون هناك حاجة إلى كلمة مرور من المستخدم عند فتح مستند PDF.
- فتح مستند PDF بكلمة مرور المالك الصحيحة يسمح بالوصول الكامل (دون تحديد أي قيود وصول) إلى المستند.
- فتح مستند PDF بكلمة مرور المستخدم الصحيحة (أو فتح مستند لا يحتوي على كلمة مرور للمستخدم) يسمح بوصول محدود حيث تم تحديد الأذونات.

يصف الكود النموذجي أدناه كيفية تأمين ملفات PDF باستخدام Aspose.Cells for Python via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-Articles-SecurePDFDocuments-1.py" >}}

{{% alert color="primary" %}}

إذا كانت جداول البيانات تحتوي على صيغ، فمن الأفضل استدعاء [**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) قبل عرضها إلى PDF. يضمن هذا إعادة حساب القيم المعتمدة على الصيغ وعرض القيم الصحيحة في PDF.

{{% /alert %}}

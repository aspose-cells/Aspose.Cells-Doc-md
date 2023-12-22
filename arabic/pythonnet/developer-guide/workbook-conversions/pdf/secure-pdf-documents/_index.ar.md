---
title: تأمين PDF الوثائق
type: docs
weight: 120
url: /ar/python-net/secure-pdf-documents/
description: تعرف على كيفية تمرير خيارات الأمان PDF عند حفظ جداول البيانات إلى PDF مع Aspose.Cells for Python via .NET API.
keywords: Python write security options to pdf, encrypt PDF document 
---
{{% alert color="primary" %}}

في بعض الأحيان، يحتاج المطورون إلى العمل مع الملفات المشفرة PDF. على سبيل المثال:

- قم بتأمين المستندات باستخدام كلمات مرور المالك والمستخدم حتى لا يتمكن أي شخص من فتحها.
- قم بتعيين القيود أو الأذونات للمستند بعد فتح المستند. على سبيل المثال، تقييد ما إذا كان يمكن طباعة محتوى المستند أو استخراجه.

تشرح هذه المقالة كيفية تمرير خيارات الأمان PDF عند حفظ جداول البيانات إلى PDF.

{{% /alert %}}

 Aspose.Cells for Python via .NET يوفر[**خيارات PDF الأمنية**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/)للعمل مع الأمن. يمكنك تعيين كلمات مرور المالك والمستخدم أثناء الحفظ في PDF. ستكون كلمة مرور المالك أو كلمة مرور المستخدم مطلوبة لفتح مستند PDF المشفر للعرض.

- يمكن أن تكون كلمة مرور المستخدم فارغة أو سلسلة فارغة، وفي هذه الحالة لن تكون كلمة المرور مطلوبة من المستخدم عند فتح مستند PDF.
- يتيح فتح المستند PDF باستخدام كلمة مرور المالك الصحيحة الوصول الكامل (دون تحديد أي قيود وصول) إلى المستند.
- فتح مستند PDF بكلمة مرور المستخدم الصحيحة (أو فتح مستند لا يحتوي على كلمة مرور مستخدم) يسمح بوصول محدود حسب الأذونات المحددة.

يصف نموذج التعليمات البرمجية أدناه كيفية تأمين ملفات PDF باستخدام Aspose.Cells for Python via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-Articles-SecurePDFDocuments-1.py" >}}

{{% alert color="primary" %}}

 إذا كان جدول البيانات يحتوي على صيغ، فمن الأفضل الاتصال به[**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) مباشرة قبل تقديمه إلى PDF. وهذا يضمن إعادة حساب القيم التابعة للصيغة وتقديم القيم الصحيحة في PDF.

{{% /alert %}}

---
title: إعادة تشكيل الصور المضافة - تحويل Excel إلى PDF
type: docs
weight: 150
url: /ar/python-net/resample-added-images-excel-to-pdf-conversion/
description: تعرف على كيفية إعادة تشكيل الصور المضافة عند تحويل Excel إلى pdf باستخدام Aspose.Cells for Python via .NET API.
keywords: Python Resample Added Images when Convert Excel to PDF
---
{{% alert color="primary" %}}

أثناء العمل مع ملفات Excel الكبيرة التي تحتوي على الكثير من الصور، قد تحتاج إلى ضغط الصور التي تمت إضافتها لتقليل حجم الملف الناتج PDF وتحسين أداء التحويل الإجمالي. Aspose.Cells for Python via .NET يدعم إعادة تشكيل الصور المضافة لتقليل حجم الملف الناتج PDF وتحسين الأداء إلى حد ما.

{{% /alert %}}

يرجى الاطلاع على نموذج التعليمات البرمجية التالي الذي يصف كيفية تنفيذ المهمة باستخدام Aspose.Cells for Python via .NET API. يقوم المثال بتحويل ملف Excel Microsoft إلى ملف PDF أثناء ضغط الصور في الملف.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ResamplingAddedImages-1.py" >}}

{{% alert color="primary" %}}

 باستخدام[**PdfSaveOptions.set_image_resample**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/set_image_resample/#int-int)يعمل هذا الخيار على تقليل حجم الإخراج PDF ولكنه قد يؤثر على جودة الصورة قليلاً.

{{% /alert %}} {{% alert color="primary" %}}

 إذا كان جدول البيانات الخاص بك يحتوي على صيغ، فمن الأفضل الاتصال به[**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) مباشرة قبل تقديم جدول البيانات إلى تنسيق PDF. سيؤدي القيام بذلك إلى ضمان إعادة حساب القيم التابعة للصيغة، وتقديم القيم الصحيحة في PDF.

{{% /alert %}}

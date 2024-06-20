---
title: تحويل صور محددة إلى PDF  العين اكسل الى PDF
type: docs
weight: 150
url: /ar/python-net/resample-added-images-excel-to-pdf-conversion/
description: تعلم كيفية تحويل صور محددة عند تحويل اكسل الى PDF مع Aspose.Cells لبرنامجPython via .NET
keywords: Python تحويل صور محددة عند تحويل اكسل الىPDF
---

{{% alert color="primary" %}}

أثناء العمل مع ملفات Microsoft Excel الكبيرة التي تحتوي على الكثير من الصور، قد تحتاج إلى ضغط الصور التي تمت إضافتها لتقليل حجم ملف PDF الناتج وتحسين أداء التحويل العام.  Aspose.Cells لبرنامجPython via .NET يدعم تحويل الصور المضافة لتقليل حجم ملف PDF الناتج وتحسين الأداء إلى حدٍ ما.

{{% /alert %}}

يرجى الاطلاع على الشيفرة المصدرية التالية التي تصف كيفية أداء المهمة باستخدام Aspose.Cells لبرنامجPython via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ResamplingAddedImages-1.py" >}}

{{% alert color="primary" %}}

استخدام ال [**PdfSaveOptions.set_image_resample**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/set_image_resample/#int-int) تقلل حجم ملف ال PDF الناتج لكن قد تؤثر على جودة الصور قليلاً.

{{% /alert %}} {{% alert color="primary" %}}

إذا كانت جداول البيانات الخاصة بك تحتوي على صيغ، من الأفضل استدعاء [**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) قبل تحويل جدول البيانات إلى تنسيق PDF. وذلك سيضمن إعادة حساب قيم الصيغ الخاصة وتقديم القيم الصحيحة في الملف الناتج PDF.

{{% /alert %}}

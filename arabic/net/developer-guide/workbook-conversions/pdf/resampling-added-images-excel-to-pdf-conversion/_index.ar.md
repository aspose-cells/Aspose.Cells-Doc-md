---
title: إعادة تشكيل الصور المضافة - تحويل Excel إلى PDF
type: docs
weight: 150
url: /ar/net/resampling-added-images-excel-to-pdf-conversion/
---
{{% alert color="primary" %}}

أثناء العمل مع ملفات Excel Microsoft الكبيرة التي تحتوي على الكثير من الصور ، قد تحتاج إلى ضغط الصور التي تمت إضافتها لتقليل حجم ملف PDF الناتج وتحسين أداء التحويل الكلي. يدعم Aspose.Cells إعادة تشكيل الصور المضافة لتقليل حجم ملف PDF الناتج وتحسين الأداء إلى حد ما.

{{% /alert %}}

يرجى الاطلاع على نموذج التعليمات البرمجية التالي الذي يصف كيفية تنفيذ المهمة باستخدام Aspose.Cells API. يقوم المثال بتحويل ملف Excel Microsoft إلى ملف PDF أثناء ضغط الصور في الملف.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ResamplingAddedImages-1.cs" >}}

{{% alert color="primary" %}}

 باستخدام ملف[**SetImageResample**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/methods/setimageresample)يقلل الخيار من حجم ملف PDF الناتج ولكنه قد يؤثر على جودة الصورة قليلاً.

{{% /alert %}} {{% alert color="primary" %}}

 إذا كان جدول البيانات الخاص بك يحتوي على صيغ ، فمن الأفضل الاتصال[**المصنف .CalculateFormula ()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) مباشرة قبل تحويل جدول البيانات إلى تنسيق PDF. سيؤدي القيام بذلك إلى ضمان إعادة حساب القيم التابعة للصيغة ، وتقديم القيم الصحيحة في ملف PDF.

{{% /alert %}}

---
title: إعادة عينات الصور المضافة  تحويل Excel إلى PDF
type: docs
weight: 150
url: /ar/net/resampling-added-images-excel-to-pdf-conversion/
---

{{% alert color="primary" %}}

أثناء العمل مع ملفات Microsoft Excel الكبيرة مع الكثير من الصور، قد تحتاج إلى ضغط الصور التي تمت إضافتها لتقليل حجم ملف PDF الناتج وتحسين أداء التحويل الكلي. Aspose.Cells تدعم إعادة عينات الصور المضافة لتقليل حجم ملف PDF الناتج وتحسين الأداء بشكل ملحوظ.

{{% /alert %}}

يرجى الاطلاع على الكود النموذجي التالي الذي يصف كيفية إجراء المهمة باستخدام واجهة برمجة التطبيقات Aspose.Cells. النموذج يحول ملف Microsoft Excel إلى ملف PDF مع ضغط الصور في الملف.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ResamplingAddedImages-1.cs" >}}

{{% alert color="primary" %}}

استخدام ال [**SetImageResample**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/methods/setimageresample) تقلل حجم ملف ال PDF الناتج لكن قد تؤثر على جودة الصور قليلاً.

{{% /alert %}} {{% alert color="primary" %}}

إذا كانت جداول البيانات الخاصة بك تحتوي على صيغ، من الأفضل استدعاء [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) قبل تحويل جدول البيانات إلى تنسيق PDF. وذلك سيضمن إعادة حساب قيم الصيغ الخاصة وتقديم القيم الصحيحة في الملف الناتج PDF.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}

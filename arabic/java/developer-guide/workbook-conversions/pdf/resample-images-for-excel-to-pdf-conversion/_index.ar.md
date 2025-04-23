---
title: إعادة عينات الصور لتحويل ملفات Excel إلى PDF
type: docs
weight: 250
url: /ar/java/resample-images-for-excel-to-pdf-conversion/
description: يوضح هذا المقال تقليل أحجام الصور أثناء تحويل ملفات Excel إلى PDF
keywords: إكسيل إلى PDF، إعادة عينات الصور أثناء تحويل إكسيل إلى PDF، ضغط الصور أثناء تحويل إكسيل إلى PDF، تقليل أحجام الصور أثناء تحويل إكسيل إلى PDF، تحويل إكسيل إلى PDF بحجم أصغر، تحويل إكسيل إلى PDF مع إعادة عينات الصور، تحويل إكسيل إلى PDF مع ضغط الصور، إعادة عينات الصور أثناء تحويل إكسيل إلى PDF بلغة جافا
---

{{% alert color="primary" %}}

أثناء العمل مع ملفات Microsoft Excel الكبيرة التي تحتوي على الكثير من الصور، قد تحتاج إلى ضغط الصور التي تمت إضافتها لتقليل حجم ملف PDF الناتج وتحسين أداء التحويل بشكل عام. Aspose.Cells يدعم إعادة عينات الصور المضافة لتقليل حجم ملف PDF الناتج وتحسين الأداء.

{{% /alert %}}

## **إعادة عينات الصور لتحويل ملفات Excel إلى PDF**

يرجى الاطلاع على الكود النموذجي التالي الذي يصف كيفية إجراء المهمة باستخدام واجهة برمجة التطبيقات Aspose.Cells. النموذج يحول ملف Microsoft Excel إلى ملف PDF مع ضغط الصور في الملف.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ResampleImagesforExceltoPDFConversion-ResampleImagesforExceltoPDFConversion.java" >}}

{{% alert color="primary" %}}

باستخدام الخيار [**PdfSaveOptions.setImageResample**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#setImageResample-int-int-) يُقلل من حجم ملف PDF الناتج ولكن قد يؤثر ذلك قليلاً على جودة الصورة.

{{% /alert %}} {{% alert color="primary" %}}

إذا كانت جداول البيانات الخاصة بك تحتوي على صيغ، من الأفضل استدعاء [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) قبل تحويل جدول البيانات إلى تنسيق PDF. وذلك سيضمن إعادة حساب قيم الصيغ الخاصة وتقديم القيم الصحيحة في الملف الناتج PDF.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}

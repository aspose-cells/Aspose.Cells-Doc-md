---
title: إعادة عينة الصور لبرنامج Excel لتحويل PDF
type: docs
weight: 250
url: /ar/java/resample-images-for-excel-to-pdf-conversion/
description: توضح هذه المقالة تقليل أحجام الصور أثناء تحويل ملفات Excel إلى PDF
keywords: excel to pdf, resample images during excel to pdf conversion, compress images during excel to pdf conversion, reduce image sizes during excel to pdf conversion, convert excel to pdf with smaller size, excel to pdf conversion with image resampling, excel to pdf conversion with image compression, resample images during excel to pdf conversion java
---
{{% alert color="primary" %}}

أثناء العمل مع ملفات Excel Microsoft الكبيرة التي تحتوي على الكثير من الصور ، قد تحتاج إلى ضغط الصور التي تمت إضافتها لتقليل حجم ملف الإخراج PDF وتحسين أداء التحويل الكلي. يدعم Aspose.Cells إعادة أخذ عينات الصور المضافة لتقليل حجم الملف الناتج PDF وتحسين الأداء.

{{% /alert %}}

## **إعادة عينة الصور لبرنامج Excel لتحويل PDF**

يرجى الاطلاع على نموذج التعليمات البرمجية التالي الذي يصف كيفية تنفيذ المهمة باستخدام Aspose.Cells API. يقوم المثال بتحويل ملف Excel Microsoft إلى ملف PDF أثناء ضغط الصور في الملف.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ResampleImagesforExceltoPDFConversion-ResampleImagesforExceltoPDFConversion.java" >}}

{{% alert color="primary" %}}

 باستخدام[**PdfSaveOptions.setImageResample**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#setImageResample(int,%20int)) يقلل حجم الإخراج PDF ولكنه قد يؤثر على جودة الصورة قليلاً.

{{% /alert %}} {{% alert color="primary" %}}

إذا كان جدول البيانات الخاص بك يحتوي على صيغ ، فمن الأفضل الاتصال[**Workbook.calculateFormula ()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()قبل تحويل جدول البيانات إلى تنسيق PDF. سيؤدي القيام بذلك إلى ضمان إعادة حساب القيم التابعة للصيغة ، وتقديم القيم الصحيحة في PDF.

{{% /alert %}}

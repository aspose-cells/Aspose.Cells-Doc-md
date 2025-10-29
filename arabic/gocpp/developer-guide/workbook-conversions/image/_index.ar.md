---
title: تحويل إكسل إلى صورة مع Golang عبر C++
linktitle: تحويل ملف إكسل إلى صورة
type: docs
weight: 300
url: /ar/go-cpp/convert-excel-to-image/
description: تعرّف على كيفية تحويل أوراق عمل إكسل إلى صور، بما في ذلك تنسيقات TIFF و SVG، باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}}

تتيح Aspose.Cells لك تصدير ورقة عمل من دفتر عمل وتحويلها إلى تنسيقات مختلفة. يشرح هذا المقال كيفية تحويل ورقة عمل إلى تنسيقات مختلفة.

{{% /alert %}}

## تحويل دفتر العمل إلى TIFF

قد يحتوي ملف إكسل على عدة أوراق مع صفحات متعددة. يسمح [**WorkbookRender**](https://reference.aspose.com/cells/go-cpp/workbookrender/) لك بتحويل إكسل إلى TIFF بعدة صفحات. كما يمكنك التحكم في خيارات متعددة لـ TIFF، مثل [الضغط](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/tiffcompression/)، [GetTiffColorDepth()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gettiffcolordepth/)، الدقة ([GetHorizontalResolution()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gethorizontalresolution/)، [GetVerticalResolution()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getverticalresolution/)).

يوضح مقتطف الكود التالي كيفية تحويل Excel إلى TIFF مع عدة صفحات. المرفقات تشمل [ملف الإكسل المصدر](workbook-to-tiff-with-mulitiple-pages.xlsx) و [صورة TIFF المولدة](workbook-to-tiff-with-mulitiple-pages.tiff) للرجوع اليها.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Image.go" >}}
## **تحويل ورقة عمل إلى صورة**

تحتوي الأوراق العمل على البيانات التي ترغب في تحليلها. على سبيل المثال، يمكن أن تحتوي ورقة العمل على معلمات وإجماليات ونسب واستثناءات وحسابات.

كمطور، قد تحتاج إلى عرض الأوراق العمل كصور. على سبيل المثال، قد تحتاج إلى استخدام صورة لورقة عمل في تطبيق أو صفحة ويب. قد ترغب في إدراج صورة في مستند Microsoft Word أو ملف PDF أو عرض PowerPoint أو نوع مستند آخر. ببساطة، ترغب في عرض ورقة عمل كصورة حتى تتمكن من استخدامها في مكان آخر.

يدعم Aspose.Cells تحويل أوراق عمل إكسل إلى صور. لاستخدام هذه الميزة، تحتاج إلى استيراد مساحة الاسم [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/go-cpp/) إلى برنامجك أو مشروعك. يوجد العديد من الفئات القيمة للرسم والطباعة، على سبيل المثال [**SheetRender**](https://reference.aspose.com/cells/go-cpp/sheetrender/)، [**ImageOrPrintOptions**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/)، [**WorkbookRender**](https://reference.aspose.com/cells/go-cpp/workbookrender/)، وغيرها.

تمثل فئة [**SheetRender**](https://reference.aspose.com/cells/go-cpp/sheetrender/) ورقة عمل يمكن تصييرها كصور. لديها طريقة محملة، [**ToImage**](https://reference.aspose.com/cells/go-cpp/sheetrender/toimage/)، التي يمكنها تحويل ورقة العمل إلى ملف أو ملفات صورة مع سمات أو خيارات مختلفة. تعيد كائن `System.Drawing.Bitmap` ويمكنك حفظ ملف صورة على القرص أو التدفق. يدعم عدة تنسيقات صور، على سبيل المثال BMP، PNG، GIF، JPG، JPEG، TIFF، EMF.

يوضح مقتطف الكود التالي كيفية تحويل ورقة عمل في ملف Excel إلى ملف صورة.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Image-1.go" >}}
{{% alert color="primary" %}}

حاليًا، لا يدعم الواجهة البرمجية لتحويل ورقة عمل إلى صور دعم مخططات الفقاعات ثلاثية الأبعاد.

{{% /alert %}}

## **تحويل ورقة عمل إلى SVG**

تعني SVG Scalable Vector Graphics. SVG هو مواصفة تعتمد على معايير XML للرسومات الناقلة ثنائية الأبعاد. إنها معيار مفتوح تحت تطوير من قبل الجمعية العالمية للويب (W3C) منذ عام 1999.

تمكن Aspose.Cells for C++ من تحويل أوراق العمل إلى صورة SVG منذ النسخة 7.1.0. يُظهر مقتطف الكود التالي كيفية تحويل ورقة عمل في ملف إكسل إلى ملف صورة SVG.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Image-2.go" >}}
## **مواضيع متقدمة**
- [تحويل مخطط Excel إلى صورة](/cells/ar/cpp/convert-an-excel-chart-to-image/)
- [تحويل مخطط إلى صورة بتنسيق SVG](/cells/ar/cpp/converting-chart-to-image-in-svg-format/)
- [تصدير مخطط إلى SVG باستخدام سمة viewBox](/cells/ar/cpp/export-chart-to-svg-with-viewbox-attribute/)
- [تتبع تقدّم تحويل Excel إلى TIFF](/cells/ar/cpp/track-conversion-progress-of-excel-to-tiff/)

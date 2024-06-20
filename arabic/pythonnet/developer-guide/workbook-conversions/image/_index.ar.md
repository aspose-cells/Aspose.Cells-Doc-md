---
title: صورة
type: docs
weight: 300
url: /ar/python-net/convert-excel-to-image/
description: تحويل الرسم البياني إلى صورة باستخدام واجهة برمجة التطبيقات Aspose.Cells for Python via .NET.
keywords: تحويل الرسم البياني إلى صورة باستخدام Python، تصدير الرسم البياني إلى صورة في Python via NET، حفظ الرسم البياني إلى صورة في Python.
---


{{% alert color="primary" %}}

تسمح Aspose.Cells for Python via .NET لك بتصدير ورق العمل من المصنف وتحويله إلى تنسيقات مختلفة. يشرح هذا المقال كيفية تحويل ورق العمل إلى تنسيقات مختلفة.

{{% /alert %}}

## تحويل دفتر العمل إلى TIFF

يمكن أن يحتوي ملف Excel على عدة صفحات مع عدة صفحات. [**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender) تتيح لك تحويل Excel إلى TIFF مع عدة صفحات. كما يمكنك التحكم في العديد من الخيارات لـ TIFF ، مثل [الضغط](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/tiff_compression/) ، [عمق الألوان](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/tiff_color_depth/) ، الدقة ([الدقة الأفقية](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/horizontal_resolution/) ، [الدقة العمودية](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/vertical_resolution/)).

يوضح مقتطف الكود التالي كيفية تحويل Excel إلى TIFF مع عدة صفحات. المرفقات تشمل [ملف الإكسل المصدر](workbook-to-tiff-with-mulitiple-pages.xlsx) و [صورة TIFF المولدة](workbook-to-tiff-with-mulitiple-pages.tiff) للرجوع اليها.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Workbook-To-Tiff-With-Mulitiple-Pages.py" >}}

## **تحويل ورقة عمل إلى صورة**

تحتوي الأوراق العمل على البيانات التي ترغب في تحليلها. على سبيل المثال، يمكن أن تحتوي ورقة العمل على معلمات وإجماليات ونسب واستثناءات وحسابات.

كمطور، قد تحتاج إلى عرض الأوراق العمل كصور. على سبيل المثال، قد تحتاج إلى استخدام صورة لورقة عمل في تطبيق أو صفحة ويب. قد ترغب في إدراج صورة في مستند Microsoft Word أو ملف PDF أو عرض PowerPoint أو نوع مستند آخر. ببساطة، ترغب في عرض ورقة عمل كصورة حتى تتمكن من استخدامها في مكان آخر.

تدعم Aspose.Cells for Python via .NET تحويل ورقات عمل Excel إلى صور. لاستخدام هذه الميزة ، تحتاج إلى استيراد مساحة الاسم [**aspose.cells.rendering**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/) إلى برنامجك أو مشروعك. لديها عدة فئات قيمة للتقديم والطباعة ، على سبيل المثال [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/) ، [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/) ، [**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender/) ، وغيرها.

تمثل الفئة [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/) ورقة عمل يتم تحويلها إلى صور. تحتوي على طريقة محملة، [**to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_image/#int-str) التي يمكن تحويل ورقة عمل إلى ملف صورة (صور) بخصائص أو خيارات مختلفة. تقوم بإرجاع كائن System.Drawing.Bitmap ويمكنك حفظ ملف صورة إلى القرص أو التسلسل. تدعم عدة تنسيقات صور، على سبيل المثال BMP، PNG، GIF، JPG، JPEG، TIFF، EMF.

يوضح مقتطف الكود التالي كيفية تحويل ورقة عمل في ملف Excel إلى ملف صورة.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheet-ConvertWorksheetToImageByPage-1.py" >}}

{{% alert color="primary" %}}

حاليًا، لا يدعم الواجهة البرمجية لتحويل ورقة عمل إلى صور دعم مخططات الفقاعات ثلاثية الأبعاد.

{{% /alert %}}

## **تحويل ورقة عمل إلى SVG**

تعني SVG Scalable Vector Graphics. SVG هو مواصفة تعتمد على معايير XML للرسومات الناقلة ثنائية الأبعاد. إنها معيار مفتوح تحت تطوير من قبل الجمعية العالمية للويب (W3C) منذ عام 1999.

Aspose.Cells for Python via .NET كان قادرًا على تحويل أوراق عمل إلى صور SVG منذ الإصدار 7.1.0. يُظهر مقتطف الكود التالي كيفية تحويل ورقة عمل في ملف Excel إلى ملف صورة SVG.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheet-ConvertWorksheetToSVG-1.py" >}}

## **مواضيع متقدمة**
- [تحويل مخطط Excel إلى صورة](/cells/ar/python-net/convert-an-excel-chart-to-image/)
- [تحويل مخطط إلى صورة بتنسيق SVG](/cells/ar/python-net/converting-chart-to-image-in-svg-format/)
- [تصدير مخطط إلى SVG باستخدام سمة viewBox](/cells/ar/python-net/export-chart-to-svg-with-viewbox-attribute/)

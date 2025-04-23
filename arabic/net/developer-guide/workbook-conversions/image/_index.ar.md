---
title: صورة
type: docs
weight: 300
url: /ar/net/convert-excel-to-image/
---


{{% alert color="primary" %}}

تتيح Aspose.Cells لك تصدير ورقة عمل من دفتر عمل وتحويلها إلى تنسيقات مختلفة. يشرح هذا المقال كيفية تحويل ورقة عمل إلى تنسيقات مختلفة.

{{% /alert %}}

## تحويل دفتر العمل إلى TIFF

يمكن لملف Excel أن يحتوي على عدة أوراق ببضع صفحات. تسمح [**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender) لك بتحويل Excel إلى TIFF بصفحات متعددة. كما يمكنك التحكم في خيارات متعددة لـ TIFF، مثل [الضغط](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/tiffcompression)، [عمق اللون](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/tiffcolordepth)، الدقة ([الدقة الأفقية](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/horizontalresolution)، [الدقة العمودية](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/verticalresolution)).

يوضح مقتطف الكود التالي كيفية تحويل Excel إلى TIFF مع عدة صفحات. المرفقات تشمل [ملف الإكسل المصدر](workbook-to-tiff-with-mulitiple-pages.xlsx) و [صورة TIFF المولدة](workbook-to-tiff-with-mulitiple-pages.tiff) للرجوع اليها.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Workbook-To-Tiff-With-Mulitiple-Pages.cs" >}}

## **تحويل ورقة عمل إلى صورة**

تحتوي الأوراق العمل على البيانات التي ترغب في تحليلها. على سبيل المثال، يمكن أن تحتوي ورقة العمل على معلمات وإجماليات ونسب واستثناءات وحسابات.

كمطور، قد تحتاج إلى عرض الأوراق العمل كصور. على سبيل المثال، قد تحتاج إلى استخدام صورة لورقة عمل في تطبيق أو صفحة ويب. قد ترغب في إدراج صورة في مستند Microsoft Word أو ملف PDF أو عرض PowerPoint أو نوع مستند آخر. ببساطة، ترغب في عرض ورقة عمل كصورة حتى تتمكن من استخدامها في مكان آخر.

تدعم Aspose.Cells تحويل أوراق العمل في Excel إلى صور. لاستخدام هذه الميزة، يجب عليك استيراد فضاء الأسماء [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/net/aspose.cells.rendering) إلى برنامجك أو مشروعك. تحتوي على عدة فئات قيمة لعمليات العرض والطباعة، على سبيل المثال [**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)، [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)، [**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender)، وغيرها.

تمثل الفئة [**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) ورقة عمل يتم تحويلها إلى صور. تحتوي على طريقة محملة، [**ToImage**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index) التي يمكن تحويل ورقة عمل إلى ملف صورة (صور) بخصائص أو خيارات مختلفة. تقوم بإرجاع كائن System.Drawing.Bitmap ويمكنك حفظ ملف صورة إلى القرص أو التسلسل. تدعم عدة تنسيقات صور، على سبيل المثال BMP، PNG، GIF، JPG، JPEG، TIFF، EMF.

يوضح مقتطف الكود التالي كيفية تحويل ورقة عمل في ملف Excel إلى ملف صورة.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheetToImageByPage-1.cs" >}}

{{% alert color="primary" %}}

حاليًا، لا يدعم الواجهة البرمجية لتحويل ورقة عمل إلى صور دعم مخططات الفقاعات ثلاثية الأبعاد.

{{% /alert %}}

## **تحويل ورقة عمل إلى SVG**

تعني SVG Scalable Vector Graphics. SVG هو مواصفة تعتمد على معايير XML للرسومات الناقلة ثنائية الأبعاد. إنها معيار مفتوح تحت تطوير من قبل الجمعية العالمية للويب (W3C) منذ عام 1999.

Aspose.Cells for .NET تمكن من تحويل ورقات العمل إلى صور SVG منذ الإصدار 7.1.0. يوضح مقتطف الكود التالي كيفية تحويل ورقة عمل في ملف Excel إلى ملف صورة SVG.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheetToSVG-1.cs" >}}

## **مواضيع متقدمة**
- [تحويل مخطط Excel إلى صورة](/cells/ar/net/convert-an-excel-chart-to-image/)
- [تحويل مخطط إلى صورة بتنسيق SVG](/cells/ar/net/converting-chart-to-image-in-svg-format/)
- [تصدير مخطط إلى SVG باستخدام سمة viewBox](/cells/ar/net/export-chart-to-svg-with-viewbox-attribute/)
- [تتبع تقدّم تحويل Excel إلى TIFF](/cells/ar/net/track-conversion-progress-of-excel-to-tiff/)
{{< app/cells/assistant language="csharp" >}}

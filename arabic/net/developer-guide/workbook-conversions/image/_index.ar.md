---
title: صورة
type: docs
weight: 300
url: /ar/net/convert-excel-to-image/
---
{{% alert color="primary" %}}

يسمح لك Aspose.Cells بتصدير ورقة عمل من المصنف وتحويلها إلى تنسيقات مختلفة. تشرح هذه المقالة كيفية تحويل ورقة عمل إلى تنسيقات مختلفة.

{{% /alert %}}

## تحويل المصنف إلى TIFF

 يمكن أن يحتوي ملف Excel على أوراق متعددة بصفحات متعددة.[عرض المصنف](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender) يسمح لك بتحويل Excel إلى TIFF بصفحات متعددة. أيضًا ، يمكنك التحكم في خيارات متعددة لـ TIFF ، مثل[ضغط](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/tiffcompression), [عمق اللون](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/tiffcolordepth)، الدقة([الدقة الأفقية](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/horizontalresolution), [دقة رأسية](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/verticalresolution)).

 يوضح مقتطف الشفرة التالي كيفية تحويل Excel إلى TIFF بصفحات متعددة. ال[ملف Excel المصدر](workbook-to-tiff-with-mulitiple-pages.xlsx) و[تم إنشاء صورة TIFF](workbook-to-tiff-with-mulitiple-pages.tiff) المرفقة للرجوع اليها.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Workbook-To-Tiff-With-Mulitiple-Pages.cs" >}}

## **تحويل ورقة العمل إلى صورة**

تحتوي أوراق العمل على بيانات تريد تحليلها. على سبيل المثال ، يمكن أن تحتوي ورقة العمل على معلمات وإجماليات ونسب مئوية واستثناءات وحسابات.

بصفتك مطورًا ، قد تحتاج إلى تقديم أوراق العمل كصور. على سبيل المثال ، قد تحتاج إلى استخدام صورة ورقة عمل في تطبيق أو صفحة ويب. قد ترغب في إدراج صورة في مستند Word Microsoft أو ملف PDF أو عرض تقديمي PowerPoint أو أي نوع مستند آخر. ببساطة ، تريد عرض ورقة العمل كصورة بحيث يمكنك استخدامها في مكان آخر.

يدعم Aspose.Cells تحويل أوراق عمل Excel إلى صور. لاستخدام هذه الميزة ، تحتاج إلى استيراد ملف**[Aspose.Cells.Rendering] (https://reference.aspose.com/cells/net/aspose.cells.rendering)** إلى برنامجك أو مشروعك. لديها العديد من الفئات القيمة للتصيير والطباعة ، على سبيل المثال**[SheetRender] (https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)**, **[ImageOrPrintOptions] (https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)**, **[WorkbookRender] (https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender)**، و اخرين.

 ال**[SheetRender] (https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)** فئة تمثل ورقة عمل يتم عرضها كصور. لديها طريقة محملة فوق طاقتها ،**[ToImage] (https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index)**، يمكنها تحويل ورقة عمل إلى ملف (ملفات) صور بسمات أو خيارات مختلفة. تقوم بإرجاع كائن System.Drawing.Bitmap ويمكنك حفظ ملف صورة على القرص أو التدفق. يتم دعم العديد من تنسيقات الصور ، على سبيل المثال BMP ، PNG ، GIF ، JPG ، JPEG ، TIFF ، EMF.

يوضح مقتطف التعليمات البرمجية التالي كيفية تحويل ورقة عمل في ملف Excel إلى ملف صورة.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheetToImageByPage-1.cs" >}}

{{% alert color="primary" %}}

في الوقت الحالي ، لا يدعم API لتحويل أوراق العمل إلى صور المخططات الفقاعية ثلاثية الأبعاد.

{{% /alert %}}

## **تحويل ورقة العمل إلى SVG**

SVG لتقف على Scalable Vector Graphics. SVG هي مواصفة تستند إلى معايير XML للرسومات المتجهة ثنائية الأبعاد. إنه معيار مفتوح قيد التطوير من قبل World Wide Web Consortium (W3C) منذ 1999.

Aspose.Cells for .NET تمكن من تحويل أوراق العمل إلى صورة SVG منذ الإصدار 7.1.0. يوضح مقتطف التعليمات البرمجية التالي كيفية تحويل ورقة عمل في ملف Excel إلى ملف صورة SVG.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheetToSVG-1.cs" >}}

## **موضوعات مسبقة**
- [تحويل مخطط Excel إلى صورة](/cells/ar/net/convert-an-excel-chart-to-image/)
- [تحويل الرسم البياني إلى صورة بتنسيق SVG](/cells/ar/net/converting-chart-to-image-in-svg-format/)
- [تصدير المخطط إلى SVG مع سمة viewBox](/cells/ar/net/export-chart-to-svg-with-viewbox-attribute/)
- [تتبع تقدم تحويل Excel إلى TIFF](/cells/ar/net/track-conversion-progress-of-excel-to-tiff/)

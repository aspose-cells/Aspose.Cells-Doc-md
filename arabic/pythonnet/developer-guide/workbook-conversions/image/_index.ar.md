---
title: Image
type: docs
weight: 300
url: /ar/python-net/convert-excel-to-image/
description: تحويل الرسم البياني إلى Image باستخدام Aspose.Cells for Python via .NET API.
keywords: Python Convert Chart to Image, Export Chart to Image in Python via NET, Python Save Chart to Image.
---
{{% alert color="primary" %}}

Aspose.Cells for Python via .NET يتيح لك تصدير ورقة عمل من المصنف وتحويلها إلى تنسيقات مختلفة. يشرح هذا المقال كيفية تحويل ورقة العمل إلى تنسيقات مختلفة.

{{% /alert %}}

##  تحويل المصنف إلى TIFF

 يمكن أن يحتوي ملف Excel على أوراق متعددة تحتوي على صفحات متعددة.[WorkbookRender](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender) يسمح لك بتحويل Excel إلى TIFF بصفحات متعددة. كما يمكنك التحكم في خيارات متعددة للرقم TIFF مثل[ضغط](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/tiff_compression/), [عمق اللون](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/tiff_color_depth/)، دقة([القرار الأفقي](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/horizontal_resolution/), [القرار العمودي](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/vertical_resolution/)).

 يوضح مقتطف التعليمات البرمجية التالي كيفية تحويل Excel إلى TIFF بصفحات متعددة. ال[ملف اكسيل المصدر](workbook-to-tiff-with-mulitiple-pages.xlsx) و[تم إنشاء صورة TIFF](workbook-to-tiff-with-mulitiple-pages.tiff) يتم إرفاقها للرجوع إليها.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Workbook-To-Tiff-With-Mulitiple-Pages.py" >}}

##  **تحويل ورقة العمل إلى Image**

تحتوي أوراق العمل على البيانات التي تريد تحليلها. على سبيل المثال، يمكن أن تحتوي ورقة العمل على معلمات وإجماليات ونسب مئوية واستثناءات وحسابات.

كمطور، قد تحتاج إلى تقديم أوراق العمل كصور. على سبيل المثال، قد تحتاج إلى استخدام صورة ورقة عمل في تطبيق أو صفحة ويب. قد ترغب في إدراج صورة في مستند Word Microsoft أو ملف PDF أو عرض تقديمي PowerPoint أو أي نوع آخر من المستندات. ببساطة، أنت تريد عرض ورقة العمل كصورة بحيث يمكنك استخدامها في مكان آخر.

Aspose.Cells for Python via .NET يدعم تحويل أوراق عمل Excel إلى صور. لاستخدام هذه الميزة، تحتاج إلى استيراد ملف**[aspose.cells.rendering](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/)**مساحة الاسم لبرنامجك أو مشروعك. وله عدة فئات قيمة للعرض والطباعة، على سبيل المثال *[SheetRender](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/)**, *[خيارات الصورة أو الطباعة](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/)**, *[WorkbookRender](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender/)**، و اخرين.

 ال**[SheetRender](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/)**يمثل الفصل ورقة عمل لعرضها كصور. لديها طريقة مثقلة، *[to_image](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_image/#int-str)**، يمكنه تحويل ورقة العمل إلى ملف (ملفات) صورة بسمات أو خيارات مختلفة. تقوم بإرجاع كائن System.Drawing.Bitmap ويمكنك حفظ ملف صورة على القرص أو الدفق. يتم دعم العديد من صيغ الصور، على سبيل المثال BMP، PNG، GIF، JPG، JPEG، TIFF، EMF.

يوضح مقتطف التعليمات البرمجية التالي كيفية تحويل ورقة عمل في ملف Excel إلى ملف صورة.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheet-ConvertWorksheetToImageByPage-1.py" >}}

{{% alert color="primary" %}}

في الوقت الحاضر، API لتحويل أوراق العمل إلى صور لا يدعم المخططات الفقاعية ثلاثية الأبعاد.

{{% /alert %}}

##  **تحويل ورقة العمل إلى SVG**

SVG يرمز إلى رسومات المتجهات القابلة للتطوير. SVG هي مواصفات تعتمد على معايير XML للرسومات المتجهة ثنائية الأبعاد. وهو معيار مفتوح قيد التطوير بواسطة اتحاد شبكة الويب العالمية (W3C) منذ عام 1999.

Aspose.Cells for Python via .NET تمكن من تحويل أوراق العمل إلى صورة SVG منذ الإصدار 7.1.0. يوضح مقتطف التعليمات البرمجية التالي كيفية تحويل ورقة عمل في ملف Excel إلى ملف صورة SVG.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheet-ConvertWorksheetToSVG-1.py" >}}

##  **مواضيع متقدمة**
- [تحويل مخطط Excel إلى Image](/cells/ar/python-net/convert-an-excel-chart-to-image/)
- [تحويل المخطط إلى Image بتنسيق SVG](/cells/ar/python-net/converting-chart-to-image-in-svg-format/)
- [تصدير الرسم البياني إلى SVG مع سمة viewBox](/cells/ar/python-net/export-chart-to-svg-with-viewbox-attribute/)

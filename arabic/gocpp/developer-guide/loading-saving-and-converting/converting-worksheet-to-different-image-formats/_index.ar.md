---
title: تحويل ورقة العمل إلى تنسيقات صور مختلفة
type: docs
weight: 90
url: /ar/go-cpp/converting-worksheet-to-different-image-formats/
---

{{% alert color="primary" %}}

Aspose.Cells  يسمح لك بتصدير ورقة البيانات من جدول بيانات وتحويلها إلى تنسيقات صور مختلفة. يشرح هذا المقال كيفية تحويل ورقة البيانات إلى تنسيقات صور مختلفة.

{{% /alert %}}

## **تحويل ورقة عمل إلى صورة**

تحتوي الأوراق العمل على البيانات التي ترغب في تحليلها. على سبيل المثال، يمكن أن تحتوي ورقة العمل على معلمات وإجماليات ونسب واستثناءات وحسابات.

كمطور، قد تحتاج إلى عرض أوراق العمل كصور. على سبيل المثال، قد تحتاج إلى استخدام صورة لورقة عمل في تطبيق أو صفحة ويب. ربما تريد إدراج صورة في مستند Microsoft Word، أو ملف PDF، أو عرض PowerPoint، أو نوع مستند آخر. ببساطة، أنت تريد أن يتم عرض ورقة العمل كصورة بحيث يمكنك استخدامها في مكان آخر.

يدعم Aspose.Cells تحويل أوراق عمل Excel إلى صور. لاستخدام هذه الميزة، تحتاج إلى استيراد مساحة الأسماء [Aspose.Cells.Rendering](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/) إلى برنامجك أو مشروعك. تحتوي على عدة فئات قيمة للعرض والطباعة، على سبيل المثال، [SheetRender](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/)، [ImageOrPrintOptions](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/)، وغيرها.

تمثل فئة [Aspose.Cells.Rendering.ISheetRender](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/) ورقة العمل التي يتم عرضها كصور. تحتوي على طريقة محملة، [ToImage](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/)، والتي يمكنها تحويل ورقة عمل إلى ملف صورة أو أكثر بسمات أو خيارات مختلفة. تدعم عدة تنسيقات صور، على سبيل المثال، BMP، PNG، GIF، JPG، JPEG، TIFF، و EMF.

يوضح مقتطف الكود التالي كيفية تحويل ورقة عمل في ملف Excel إلى ملف صورة.

### **تحويل Excel / جدول البيانات إلى PNG باستخدام GoLang**

يرجى رؤية الكود عينة التالي، ملف الإكسل [عينة](67338402.xlsx) و [صور PNG النتج](67338401.zip).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertWorksheetToImage_Png.go" >}}

### **تحويل Excel / جدول البيانات إلى TIFF باستخدام GoLang**

يرجى رؤية الكود عينة التالي، ملف الإكسل [عينة](67338402.xlsx) و [صورة TIFF الناتجة](67338419.zip).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertWorksheetToImage_Tiff.go" >}}

## **تحويل Excel / جدول البيانات إلى SVG باستخدام GoLang**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertWorksheetToImage_Svg.go" >}}

تعني SVG Scalable Vector Graphics. SVG هو مواصفة تعتمد على معايير XML للرسومات الناقلة ثنائية الأبعاد. إنها معيار مفتوح تحت تطوير من قبل الجمعية العالمية للويب (W3C) منذ عام 1999.

تمكن Aspose.Cells for Go via C++ من تحويل أوراق العمل إلى صور SVG منذ الإصدار 24.12.0.

للاستفادة من هذه الميزة، استيراد فضاء الاسم `Aspose.Cells.Rendering` إلى برنامجك أو مشروعك. يوجد فيه عدة فئات قيمة للتقديم والطباعة، على سبيل المثال، `ISheetRender`، `IImageOrPrintOptions` وغيرها.

تحدد فئة `Aspose.Cells.Rendering.IImageOrPrintOptions` أنه سيتم حفظ ورقة العمل بتنسيق SVG. الكود المصغر التالي يظهر كيفية تحويل ورقة عمل في ملف Excel إلى ملف صورة SVG

يرجى رؤية الكود عينة التالي، ملف الإكسل [عينة](67338402.xlsx) و [صور SVG الناتجة](67338403.zip).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertWorksheetToImage_SVG.go" >}}

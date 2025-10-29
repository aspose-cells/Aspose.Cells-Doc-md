---
title: تحويل ورقة العمل إلى تنسيقات صور مختلفة
type: docs
weight: 90
url: /ar/cpp/converting-worksheet-to-different-image-formats/
---

{{% alert color="primary" %}} 

Aspose.Cells  يسمح لك بتصدير ورقة البيانات من جدول بيانات وتحويلها إلى تنسيقات صور مختلفة. يشرح هذا المقال كيفية تحويل ورقة البيانات إلى تنسيقات صور مختلفة.

{{% /alert %}} 
## **تحويل ورقة عمل إلى صورة**
تحتوي الأوراق العمل على البيانات التي ترغب في تحليلها. على سبيل المثال، يمكن أن تحتوي ورقة العمل على معلمات وإجماليات ونسب واستثناءات وحسابات.

كمطور، قد تحتاج إلى عرض الأوراق العمل كصور. على سبيل المثال، قد تحتاج إلى استخدام صورة لورقة عمل في تطبيق أو صفحة ويب. قد ترغب في إدراج صورة في مستند Microsoft Word أو ملف PDF أو عرض PowerPoint أو نوع مستند آخر. ببساطة، ترغب في عرض ورقة عمل كصورة حتى تتمكن من استخدامها في مكان آخر.

Aspose.Cells يدعم تحويل ورقات العمل في Excel إلى صور. لاستخدام هذه الميزة، تحتاج إلى استيراد فضاء الاسم [Aspose.Cells.Rendering](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/) إلى برنامجك أو مشروعك. يوجد فيه عدة فئات قيمة للتقديم والطباعة، على سبيل المثال، [SheetRender](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/)، [ImageOrPrintOptions](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) وغيرها.

تمثل فئة `Aspose.Cells.Rendering.ISheetRender` ورقة عمل يتم تقديمها كصور. لديها أسلوب مفرط، [ToImage](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/)، الذي يمكن أن يحول ورقة عمل إلى ملف صورة (صور) بخصائص أو خيارات مختلفة. يتم دعم عدة تنسيقات صور، على سبيل المثال، BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.

يوضح مقتطف الكود التالي كيفية تحويل ورقة عمل في ملف Excel إلى ملف صورة.
### **تنسيق PNG**
يرجى رؤية الكود عينة التالي، ملف الإكسل [عينة](67338402.xlsx) و [صور PNG النتج](67338401.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_PNG-new.cpp" >}}

### **تنسيق TIFF**
يرجى رؤية الكود عينة التالي، ملف الإكسل [عينة](67338402.xlsx) و [صورة TIFF الناتجة](67338419.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_TIFF-new.cpp" >}}

## **تحويل ورقة عمل إلى SVG**
تعني SVG Scalable Vector Graphics. SVG هو مواصفة تعتمد على معايير XML للرسومات الناقلة ثنائية الأبعاد. إنها معيار مفتوح تحت تطوير من قبل الجمعية العالمية للويب (W3C) منذ عام 1999.

Aspose.Cells for C++ تمكن من تحويل ورقات العمل إلى صور SVG منذ الإصدار 18.5.0.

للاستفادة من هذه الميزة، استيراد فضاء الاسم `Aspose.Cells.Rendering` إلى برنامجك أو مشروعك. يوجد فيه عدة فئات قيمة للتقديم والطباعة، على سبيل المثال، `ISheetRender`، `IImageOrPrintOptions` وغيرها.

تحدد فئة `Aspose.Cells.Rendering.IImageOrPrintOptions` أنه سيتم حفظ ورقة العمل بتنسيق SVG. الكود المصغر التالي يظهر كيفية تحويل ورقة عمل في ملف Excel إلى ملف صورة SVG

يرجى رؤية الكود عينة التالي، ملف الإكسل [عينة](67338402.xlsx) و [صور SVG الناتجة](67338403.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_SVG-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}

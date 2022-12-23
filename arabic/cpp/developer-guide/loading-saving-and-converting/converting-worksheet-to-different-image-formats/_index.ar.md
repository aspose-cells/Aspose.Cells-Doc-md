---
title: تحويل ورقة العمل إلى تنسيقات صور مختلفة
type: docs
weight: 90
url: /ar/cpp/converting-worksheet-to-different-image-formats/
---
{{% alert color="primary" %}} 

يسمح لك Aspose.Cells بتصدير ورقة عمل من مصنف وتحويلها إلى تنسيقات صور مختلفة. تشرح هذه المقالة كيفية تحويل ورقة عمل إلى تنسيقات صور مختلفة.

{{% /alert %}} 
## **تحويل ورقة العمل إلى صورة**
تحتوي أوراق العمل على بيانات تريد تحليلها. على سبيل المثال ، يمكن أن تحتوي ورقة العمل على معلمات وإجماليات ونسب مئوية واستثناءات وحسابات.

بصفتك مطورًا ، قد تحتاج إلى تقديم أوراق العمل كصور. على سبيل المثال ، قد تحتاج إلى استخدام صورة ورقة عمل في تطبيق أو صفحة ويب. قد ترغب في إدراج صورة في مستند Word Microsoft أو ملف PDF أو عرض تقديمي PowerPoint أو أي نوع مستند آخر. ببساطة ، تريد عرض ورقة العمل كصورة بحيث يمكنك استخدامها في مكان آخر.

يدعم Aspose.Cells تحويل أوراق عمل Excel إلى صور. لاستخدام هذه الميزة ، تحتاج إلى استيراد ملف[Aspose.Cells.Rendering](https://reference.aspose.com/cells/cpp/namespace/aspose.cells.rendering)إلى برنامجك أو مشروعك. لديها العديد من الفئات القيمة للتصيير والطباعة ، على سبيل المثال ،[ISheetRender](https://reference.aspose.com/cells/cpp/class/aspose.cells.rendering.i_sheet_render), [IImageOrPrintOptions](https://reference.aspose.com/cells/cpp/class/aspose.cells.rendering.i_image_or_print_options)و اخرين.

الفئة `Aspose.Cells.Rendering.ISheetRender` تمثل ورقة عمل ليتم عرضها كصور. لديها طريقة محملة فوق طاقتها ،[ToImage](https://reference.aspose.com/cells/cpp/class/aspose.cells.rendering.i_sheet_render#ae508827a76d0c353ab0890024ec363c5)، يمكنها تحويل ورقة عمل إلى ملف (ملفات) صور بسمات أو خيارات مختلفة. يتم دعم العديد من تنسيقات الصور ، على سبيل المثال ، BMP ، PNG ، GIF ، JPG ، JPEG ، TIFF ، EMF.

يوضح مقتطف التعليمات البرمجية التالي كيفية تحويل ورقة عمل في ملف Excel إلى ملف صورة.
### **تنسيق PNG**
 يرجى الاطلاع على نموذج التعليمات البرمجية التالي ، الخاص به[نموذج لملف Excel](67338402.xlsx) ، و ال[الإخراج PNG صور](67338401.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_PNG.cpp" >}}
### **تنسيق TIFF**
 يرجى الاطلاع على نموذج التعليمات البرمجية التالي ، الخاص به[نموذج لملف Excel](67338402.xlsx) ، و ال[الإخراج TIFF صورة](67338419.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_TIFF.cpp" >}}
## **تحويل ورقة العمل إلى SVG**
SVG لتقف على Scalable Vector Graphics. SVG هي مواصفة تستند إلى معايير XML للرسومات المتجهة ثنائية الأبعاد. إنه معيار مفتوح قيد التطوير من قبل World Wide Web Consortium (W3C) منذ 1999.

Aspose.Cells for C++ تمكن من تحويل أوراق العمل إلى صورة SVG منذ الإصدار 18.5.0.

لاستخدام هذه الميزة ، قم باستيراد مساحة الاسم `Aspose.Cells.Rendering` إلى البرنامج أو المشروع الخاص بك. لديها العديد من الفئات القيمة للتصيير والطباعة ، على سبيل المثال ، `ISheetRender` ، `IImageOrPrintOptions` ، وغيرها.

تحدد الفئة `Aspose.Cells.Rendering.IImageOrPrintOptions` أنه سيتم حفظ ورقة العمل بتنسيق SVG. يوضح مقتطف التعليمات البرمجية التالي كيفية تحويل ورقة عمل في ملف Excel إلى ملف صورة SVG

 يرجى الاطلاع على نموذج التعليمات البرمجية التالي ، الخاص به[نموذج لملف Excel](67338402.xlsx) ، و ال[الإخراج SVG صور](67338403.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_SVG.cpp" >}}

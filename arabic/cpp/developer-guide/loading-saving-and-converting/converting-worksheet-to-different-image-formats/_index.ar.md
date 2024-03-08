---
title: تحويل ورقة العمل إلى تنسيقات الصور المختلفة
type: docs
weight: 90
url: /ar/cpp/converting-worksheet-to-different-image-formats/
---
{{% alert color="primary" %}} 

Aspose.Cells يسمح لك بتصدير ورقة عمل من مصنف وتحويلها إلى تنسيقات صور مختلفة. يشرح هذا المقال كيفية تحويل ورقة عمل إلى تنسيقات صور مختلفة.

{{% /alert %}} 
##  **تحويل ورقة العمل إلى صورة**
تحتوي أوراق العمل على البيانات التي تريد تحليلها. على سبيل المثال، يمكن أن تحتوي ورقة العمل على معلمات وإجماليات ونسب مئوية واستثناءات وحسابات.

كمطور، قد تحتاج إلى تقديم أوراق العمل كصور. على سبيل المثال، قد تحتاج إلى استخدام صورة ورقة عمل في تطبيق أو صفحة ويب. قد ترغب في إدراج صورة في مستند Word Microsoft أو ملف PDF أو عرض تقديمي PowerPoint أو أي نوع آخر من المستندات. ببساطة، أنت تريد عرض ورقة العمل كصورة بحيث يمكنك استخدامها في مكان آخر.

Aspose.Cells يدعم تحويل أوراق عمل Excel إلى صور. لاستخدام هذه الميزة، تحتاج إلى استيراد ملف[Aspose.Cells.Rendering](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/)مساحة الاسم لبرنامجك أو مشروعك. لديها عدة فئات قيمة للعرض والطباعة، على سبيل المثال،[SheetRender](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/), [خيارات الصورة أو الطباعة](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/)و اخرين.

تمثل الفئة `Aspose.Cells.Rendering.ISheetRender` ورقة عمل لعرضها كصور. لديها طريقة مثقلة ،[ToImage](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/)، يمكنه تحويل ورقة العمل إلى ملف (ملفات) صورة بسمات أو خيارات مختلفة. يتم دعم العديد من صيغ الصور، على سبيل المثال، BMP، PNG، GIF، JPG، JPEG، TIFF، EMF.

يوضح مقتطف التعليمات البرمجية التالي كيفية تحويل ورقة عمل في ملف Excel إلى ملف صورة.
###  **PNG تنسيق**
 الرجاء مراجعة نموذج التعليمات البرمجية التالي، الخاص به[عينة من ملف إكسل](67338402.xlsx) ، و ال[إخراج PNG الصور](67338401.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_PNG-new.cpp" >}}

###  **TIFF تنسيق**
 الرجاء مراجعة نموذج التعليمات البرمجية التالي، الخاص به[عينة من ملف إكسل](67338402.xlsx) ، و ال[إخراج TIFF صورة](67338419.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_TIFF-new.cpp" >}}

##  **تحويل ورقة العمل إلى SVG**
SVG يرمز إلى رسومات المتجهات القابلة للتطوير. SVG هي مواصفات تعتمد على معايير XML للرسومات المتجهة ثنائية الأبعاد. وهو معيار مفتوح قيد التطوير بواسطة اتحاد شبكة الويب العالمية (W3C) منذ عام 1999.

تمكن Aspose.Cells for C++ من تحويل أوراق العمل إلى صورة SVG منذ الإصدار 18.5.0.

لاستخدام هذه الميزة، قم باستيراد مساحة الاسم `Aspose.Cells.Rendering` إلى برنامجك أو مشروعك. وله عدة فئات قيمة للعرض والطباعة، على سبيل المثال، `ISheetRender`، `IImageOrPrintOptions`، وغيرها.

تحدد الفئة `Aspose.Cells.Rendering.IImageOrPrintOptions` أنه سيتم حفظ ورقة العمل بتنسيق SVG. يوضح مقتطف التعليمات البرمجية التالي كيفية تحويل ورقة عمل في ملف Excel إلى ملف صورة SVG

 الرجاء مراجعة نموذج التعليمات البرمجية التالي، الخاص به[عينة من ملف إكسل](67338402.xlsx) ، و ال[إخراج SVG الصور](67338403.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_SVG-new.cpp" >}}

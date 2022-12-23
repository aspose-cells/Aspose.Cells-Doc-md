---
title: تكوين الخطوط لتقديم جداول البيانات
type: docs
weight: 10
url: /ar/net/configuring-fonts-for-rendering-spreadsheets/
---
## **سيناريوهات الاستخدام الممكنة**

توفر واجهات برمجة التطبيقات Aspose.Cells إمكانية عرض جداول البيانات بتنسيقات صور بالإضافة إلى تحويلها إلى تنسيقات PDF و XPS. لتحقيق أقصى قدر من دقة التحويل ، من الضروري أن تكون الخطوط المستخدمة في جدول البيانات متاحة في دليل الخطوط الافتراضي لنظام التشغيل. في حالة عدم وجود الخطوط المطلوبة ، ستحاول واجهات برمجة تطبيقات Aspose.Cells استبدال الخطوط المطلوبة بالخطوط المتاحة.

## **اختيار الخطوط**

فيما يلي العملية التي تتبعها واجهات برمجة التطبيقات Aspose.Cells خلف الكواليس.

1. يحاول API العثور على الخطوط في نظام الملفات المطابقة لاسم الخط الدقيق المستخدم في جدول البيانات.
1.  إذا لم يتمكن API من العثور على الخطوط التي لها نفس الاسم بالضبط ، فإنه يحاول استخدام الخط الافتراضي المحدد ضمن المصنف**[DefaultStyle.Font] (https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)** خاصية.
1.  إذا كان API لا يمكنه تحديد مكان الخط المعرف ضمن المصنف**[DefaultStyle.Font] (https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)** الخاصية ، يحاول استخدام الخط المحدد ضمن**[PdfSaveOptions.DefaultFont] (https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont)** أو**[ImageOrPrintOptions.DefaultFont] (https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont)** خاصية.
1.  إذا كان API لا يمكنه تحديد مكان الخط المعرف أسفل**[PdfSaveOptions.DefaultFont] (https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont)** أو**[ImageOrPrintOptions.DefaultFont] (https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont)** الخاصية ، يحاول استخدام الخط المحدد ضمن**[FontConfigs.DefaultFontName] (https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/properties/defaultfontname)** خاصية.
1.  إذا كان API لا يمكنه تحديد مكان الخط المعرف أسفل**[FontConfigs.DefaultFontName] (https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/properties/defaultfontname)** الخاصية ، فهو يحاول تحديد أنسب الخطوط من جميع الخطوط المتاحة.
1. أخيرًا ، إذا لم يتمكن API من العثور على أي خطوط في نظام الملفات ، فسيتم عرض جدول البيانات باستخدام Arial.

## **تعيين مجلدات الخطوط المخصصة**

 Aspose.Cells تقوم واجهات برمجة التطبيقات (API) بالبحث في دليل الخط الافتراضي لنظام التشغيل عن الخطوط المطلوبة. في حالة عدم توفر الخطوط المطلوبة في دليل خطوط النظام ، تقوم واجهات برمجة التطبيقات بالبحث من خلال الدلائل المخصصة (المعرفة من قبل المستخدم). ال**[FontConfigs] (https://reference.aspose.com/cells/net/aspose.cells/fontconfigs)**كشفت class عن عدد من الطرق لتعيين أدلة الخطوط المخصصة كما هو مفصل أدناه.

1. **[FontConfigs.SetFontFolder] (https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolder)**: هذه الطريقة مفيدة إذا كان هناك مجلد واحد فقط ليتم تعيينه.
1. **[FontConfigs.SetFontFolders] (https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolders)**: هذه الطريقة مفيدة عندما تكون الخطوط موجودة في مجلدات متعددة ويرغب المستخدم في تعيين جميع المجلدات بشكل منفصل بدلاً من دمج كل الخطوط في مجلد واحد.
1. **[FontConfigs.SetFontSources] (https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontsources)**: هذه الآلية مفيدة عندما يرغب المستخدم في تحميل الخطوط من مجلدات متعددة أو ملف خط واحد أو بيانات الخط من مجموعة من البايتات.

{{% alert color="primary" %}}

 كلاهما**[FontConfigs.SetFontFolder] (https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolder)** & **[FontConfigs.SetFontFolders] (https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolders)** الأساليب تقبل معلمة ثانية من النوع المنطقي. تمرير**حقيقي** حيث أن المعلمة الثانية ستوجه Aspose.Cells APIs للبحث في المجلدات الفرعية عن ملفات الخطوط.

{{% /alert %}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetCustomFontFolders-1.cs" >}}

{{% alert color="primary" %}}

يرجى استخدام أي من الطرق المذكورة أعلاه في بداية التطبيق ، أي ؛ قبل استدعاء أي كائنات أخرى من Aspose.Cells APIs.

{{% /alert %}} {{% alert color="primary" %}}

إذا تم استخدام جميع الطرق المذكورة أعلاه لتعيين مصادر الخطوط ، فسيتم تفعيل الإعدادات الأخيرة فقط.

{{% /alert %}}

## **آلية استبدال الخط**

 توفر واجهات برمجة التطبيقات Aspose.Cells أيضًا القدرة على تحديد طاقم الطباعة البديل لأغراض التصيير. هذه الآلية مفيدة عندما لا يكون الخط المطلوب متاحًا على الجهاز حيث يجب إجراء التحويل. يمكن للمستخدمين توفير قائمة بأسماء الخطوط كبديل للخط المطلوب في الأصل. من أجل تحقيق ذلك ، كشفت واجهات برمجة التطبيقات Aspose.Cells ملف**[FontConfigs.SetFontSubstitutes] (https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontsubstitutes)** الطريقة التي تقبل معلمتين. المعلمة الأولى من النوع**سلسلة** ، والذي يجب أن يكون اسم الخط الذي يجب استبداله. المعلمة الثانية هي مصفوفة من النوع**سلسلة**يمكن للمستخدمين توفير قائمة بأسماء الخطوط كبديل لاسم الخط الأصلي (المحدد في المعلمة الأولى).

هنا سيناريو استخدام بسيط.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetCustomFontFolders-FontSubstitution.cs" >}}

## **جمع المعلومات**

بالإضافة إلى الأساليب المذكورة أعلاه ، قدمت واجهات برمجة التطبيقات Aspose.Cells أيضًا وسائل لجمع المعلومات حول المصادر والبدائل التي تم تعيينها.

1. **[FontConfigs.GetFontSources] (https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsources)** طريقة إرجاع مصفوفة من النوع**[FontSourceBase] (https://reference.aspose.com/cells/net/aspose.cells/fontsourcebase)**تحتوي على قائمة بمصادر الخطوط المحددة. في حالة عدم وجود مصادر محددة ، فإن**[FontConfigs.GetFontSources] (https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsources)**سيعود التابع مصفوفة فارغة.
1. **[FontConfigs.GetFontSubstitutes] (https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsubstitutes)** الأسلوب يقبل معلمة من النوع**سلسلة** السماح بتحديد اسم الخط الذي تم استبداله. في حالة عدم تعيين أي استبدال لاسم الخط المحدد ثم ملف**[FontConfigs.GetFontSubstitutes] (https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsubstitutes)**سيعود الأسلوب فارغًا.

## **موضوعات مسبقة**
- [قم بتعيين الخط الافتراضي أثناء عرض جدول البيانات على الصور](/cells/ar/net/set-default-font-while-rendering-spreadsheet-to-images/)
- [قم بتعيين خاصية DefaultFont لـ PdfSaveOptions و ImageOrPrintOptions ليكون لها الأولوية](/cells/ar/net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [تنسيقات الخطوط المدعومة](/cells/ar/net/supported-font-formats/)
- [ورقة العمل على الصورة - اضبط تنسيق البكسل للصورة المعروضة](/cells/ar/net/worksheet-to-image-set-pixel-format-for-the-rendered-image/)

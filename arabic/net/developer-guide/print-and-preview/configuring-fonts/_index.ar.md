---
title: تكوين الخطوط لرسم الجداول الخليوية
type: docs
weight: 10
url: /ar/net/configuring-fonts-for-rendering-spreadsheets/
---

## **سيناريوهات الاستخدام المحتملة**

توفر Aspose.Cells APIs مرفق تقديم الجداول الخليوية بتنسيق الصور وتحويلها إلى تنسيقات PDF و XPS. من أجل زيادة دقة التحويل، من الضروري أن تكون الخطوط المستخدمة في الجدول الخليوي متوفرة في مجلد الخط الافتراضي لنظام التشغيل. في حالة عدم توفر الخطوط المطلوبة، ستحاول Aspose.Cells APIs استبدال الخطوط المطلوبة بتلك المتاحة.

## **اختيار الخطوط**

أدناه هو العملية التي تتبعها Aspose.Cells APIs خلف الكواليس.

1. تحاول الواجهة البرمجية الخارجية العثور على الخطوط في نظام الملفات تطابق اسم الخط المستخدم في الجدول الخليوي.
1. إذا لم تتمكن الواجهة البرمجية الخارجية من العثور على الخطوط بنفس الاسم الدقيق، فإنها تحاول استخدام الخط الافتراضي المحدد في خصائص الدفتر.
1. إذا لم تتمكن الواجهة البرمجية الخارجية من تحديد الخط المحدد تحت خصائص الدفتر، فإنها تحاول استخدام الخط المحدد تحت خصائص [**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont) أو [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont).
1. إذا لم تتمكن الواجهة البرمجية الخارجية من تحديد الخط المحدد تحت خصائص [**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont) أو [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont)، فإنها تحاول استخدام الخط المحدد تحت خصائص [**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/properties/defaultfontname).
1. إذا لم تتمكن الواجهة البرمجية الخارجية من تحديد الخط المحدد تحت خصائص [**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/properties/defaultfontname)، فإنها تحاول اختيار أنسب الخطوط من جميع الخطوط المتاحة.
1. وأخيرًا، إذا لم تتمكن الواجهة البرمجية الخارجية من العثور على أي خطوط في نظام الملفات، تقوم بتقديم الجدول الخليوي باستخدام Arial.

{{% alert color="primary" %}}

بشكل عام، تقوم APIs من Aspose.Cells بمسح الدلائل الافتراضية للخطوط على نظام التشغيل Windows و Linux و MacOS بشكل افتراضي. بدءًا من [Aspose.Cells for .NET 24.7](https://releases.aspose.com/cells/net/release-notes/2024/aspose-cells-for-net-24-7-release-notes/)، تقوم الواجهة البرمجية بمسح دلائل الخطوط السحابية المُخزنة مؤقتًا في Office بشكل إضافي بشكل افتراضي.

{{% /alert %}}

## **تعيين مجلدات الخط المخصصة**

تبحث واجهات برمجة تطبيقات Aspose.Cells في دليل الخطوط الافتراضية لنظام التشغيل للخطوط المطلوبة. في حالة عدم توفر الخطوط المطلوبة في دليل خطوط النظام، تبحث الواجهات عبر الدلائل المخصصة (المعرفة للمستخدم). فئة [**FontConfigs**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs) قد عرضت العديد من الطرق لتعيين الدلائل المخصصة كما هو مفصل أدناه.

1. [**FontConfigs.SetFontFolder**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolder): تُفيد هذه الطريقة إذا كان هناك مجلد واحد فقط يجب تعيينه.
1. [**FontConfigs.SetFontFolders**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolders): تَكون هذه الطريقة مفيدةً عندما تتواجد الخطوط في مجلدات متعددة ويرغب المستخدم في تعيين كافة المجلدات بشكل منفصل بدلاً من دمج كل الخطوط في مجلد واحد.
1. [**FontConfigs.SetFontSources**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontsources): يكون هذا الآلية مفيدًا عندما يرغب المستخدم في تحميل الخطوط من مجلدين أو ملف خط واحد أو بيانات الخط من مصفوفة بايت.

{{% alert color="primary" %}}

كلاً من طريقتي [**FontConfigs.SetFontFolder**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolder) و [**FontConfigs.SetFontFolders**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolders) تقبلان معامل ثانوي من نوع Boolean. تمرير **true** كمعامل ثانوي سيوجه واجهات برمجة التطبيقات لـ Aspose.Cells للبحث في الأنظمة الفرعية عن ملفات الخطوط.

{{% /alert %}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetCustomFontFolders-1.cs" >}}

{{% alert color="primary" %}}

يرجى استخدام أي من الطرق المذكورة أعلاه في بدء التطبيق، أي قبل استدعاء أي كائنات أخرى من APIs Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

إذا تم استخدام جميع الطرق المذكورة أعلاه لتحديد مصادر الخطوط، فسيتم اعتماد إعدادات آخرى فقط.

{{% /alert %}}

## **آلية الاستبدال للخطوط**

توفر واجهات برمجة التطبيقات لـ Aspose.Cells أيضًا القدرة على تحديد الخط البديل لأغراض العرض. يكون هذا الآلية مفيدًا عندما لا يكون الخط المطلوب متاحًا على الجهاز الذي يجب أن تحدث فيه التحويل. يمكن للمستخدمين تقديم قائمة بأسماء الخطوط كبديل للخط المطلوب بشكل أصلي. ومن أجل تحقيق هذا، فقد قدمت واجهات برمجة التطبيقات لـ Aspose.Cells الطريقة [**FontConfigs.SetFontSubstitutes**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontsubstitutes) التي تقبل 2 معامل. المعامل الأول من نوع **string**، يجب أن يكون اسم الخط الذي يجب أن يتم استبداله. المعامل الثاني هو مصفوفة من نوع **string**. يمكن للمستخدمين تقديم قائمة بأسماء الخطوط كاستبدال لاسم الخط الأصلي (المحدد في المعامل الأول).

فيما يلي سيناريو استخدام بسيط.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetCustomFontFolders-FontSubstitution.cs" >}}

## **تجميع المعلومات**

بالإضافة إلى الطرق المذكورة أعلاه، قدمت واجهات برمجة التطبيقات Aspose.Cells وسيلة لجمع المعلومات حول المصادر والاستبدالات التي تم تعيينها.

1. تقوم الطريقة [**FontConfigs.GetFontSources**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsources) بإرجاع مصفوفة من نوع [**FontSourceBase**](https://reference.aspose.com/cells/net/aspose.cells/fontsourcebase) التي تحتوي على قائمة مصادر الخط المحددة. في حالة عدم تعيين مصادر، ستقوم الطريقة [**FontConfigs.GetFontSources**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsources) بإرجاع مصفوفة فارغة.
1. تقوم الطريقة [**FontConfigs.GetFontSubstitutes**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsubstitutes) بقبول معامل من نوع **string** يسمح بتحديد اسم الخط الذي تم تعيين الاستبدال له. في حالة عدم تعيين الاستبدال لاسم الخط المحدد، ستقوم الطريقة [**FontConfigs.GetFontSubstitutes**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsubstitutes) بإرجاع قيمة خالية.

## **مواضيع متقدمة**
- [تعيين الخط الافتراضي أثناء تقديم جدول البيانات إلى الصور](/cells/ar/net/set-default-font-while-rendering-spreadsheet-to-images/)
- [تعيين خاصية DefaultFont من PdfSaveOptions و ImageOrPrintOptions لتكون لها الأولوية](/cells/ar/net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [صيغ الخط المدعمة](/cells/ar/net/supported-font-formats/)
- [ورقة العمل إلى صورة - تعيين تنسيق البكسل للصورة المقدمة](/cells/ar/net/worksheet-to-image-set-pixel-format-for-the-rendered-image/)
{{< app/cells/assistant language="csharp" >}}

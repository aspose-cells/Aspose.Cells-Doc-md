---
title: تكوين الخطوط لرسم الجداول الخليوية
type: docs
weight: 10
url: /ar/python-net/configuring-fonts-for-rendering-spreadsheets/
---

## **سيناريوهات الاستخدام المحتملة**

توفر APIs الخاصة بـ Aspose.Cells لـ Python via .NET إمكانية عرض جداول البيانات بصيغ صور، وكذلك تحويلها إلى صيغ PDF وXPS. من أجل تحقيق أعلى دقة في التحويل، من الضروري أن تكون الخطوط المستخدمة في جدول البيانات متاحة في مجلد الخطوط الافتراضي لنظام التشغيل. في حال عدم وجود الخطوط المطلوبة، ستقوم APIs الخاصة بـ Aspose.Cells لـ Python via .NET بمحاولة استبدال الخطوط المطلوبة بالخطوط المتاحة.

## **اختيار الخطوط**

بالأسفل هو العملية التي تتبعها APIs الخاصة بـ Aspose.Cells لـ Python via .NET وراء الكواليس.

1. تحاول الواجهة البرمجية الخارجية العثور على الخطوط في نظام الملفات تطابق اسم الخط المستخدم في الجدول الخليوي.
1. إذا لم تتمكن الواجهة البرمجية الخارجية من العثور على الخطوط بنفس الاسم الدقيق، فإنها تحاول استخدام الخط الافتراضي المحدد في خصائص الدفتر.
1. إذا لم تتمكن الواجهة البرمجية الخارجية من تحديد الخط المحدد تحت خصائص الدفتر، فإنها تحاول استخدام الخط المحدد تحت خصائص [**PdfSaveOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/default_font/) أو [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font).
1. إذا لم تتمكن الواجهة البرمجية الخارجية من تحديد الخط المحدد تحت خصائص [**PdfSaveOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/default_font/) أو [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font)، فإنها تحاول استخدام الخط المحدد تحت خصائص [**FontConfigs.default_font_name**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/default_font_name).
1. إذا لم تتمكن الواجهة البرمجية الخارجية من تحديد الخط المحدد تحت خصائص [**FontConfigs.default_font_name**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/default_font_name)، فإنها تحاول اختيار أنسب الخطوط من جميع الخطوط المتاحة.
1. وأخيرًا، إذا لم تتمكن الواجهة البرمجية الخارجية من العثور على أي خطوط في نظام الملفات، تقوم بتقديم الجدول الخليوي باستخدام Arial.

## **تعيين مجلدات الخط المخصصة**

تبحث APIs الخاصة بـ Aspose.Cells لـ Python via .NET في دليل الخطوط الافتراضي لنظام التشغيل عن الخطوط المطلوبة. في حال عدم توافر الخطوط المطلوبة في دليل الخطوط، تبحث الـ APIs في الأدلة المخصصة (المعرفَة من قبل المستخدم). لقد كشفت فئة [**FontConfigs**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs) عن العديد من الطرق لتعيين أدلة الخطوط المخصصة كما هو موضح أدناه.

1. [**FontConfigs.set_font_folder**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_folder/): تُفيد هذه الطريقة إذا كان هناك مجلد واحد فقط يجب تعيينه.
1. [**FontConfigs.set_font_folders**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_folders/): تَكون هذه الطريقة مفيدةً عندما تتواجد الخطوط في مجلدات متعددة ويرغب المستخدم في تعيين كافة المجلدات بشكل منفصل بدلاً من دمج كل الخطوط في مجلد واحد.
1. [**FontConfigs.set_font_sources**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_sources/#list): يكون هذا الآلية مفيدًا عندما يرغب المستخدم في تحميل الخطوط من مجلدين أو ملف خط واحد أو بيانات الخط من مصفوفة بايت.

{{% alert color="primary" %}}

 كل من [**FontConfigs.set_font_folder**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_folder/) و [**FontConfigs.set_font_folders**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_folders/) يقبلان معاملًا ثانيًا من نوع Boolean. تمرير **true** كمعامل ثانٍ سيؤدي إلى توجيه APIs الخاصة بـ Aspose.Cells لـ Python via .NET للبحث في المجلدات الفرعية عن ملفات الخطوط.

{{% /alert %}}

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SetCustomFontFolders-1.py" >}}

{{% alert color="primary" %}}

يرجى استخدام أي من الطرق المذكورة أعلاه في بداية التطبيق، أي قبل استدعاء أي كائن آخر من APIs الخاصة بـ Aspose.Cells لـ Python via .NET.

{{% /alert %}} {{% alert color="primary" %}}

إذا تم استخدام جميع الطرق المذكورة أعلاه لتحديد مصادر الخطوط، فسيتم اعتماد إعدادات آخرى فقط.

{{% /alert %}}

## **آلية الاستبدال للخطوط**

توفر APIs الخاصة بـ Aspose.Cells لـ Python via .NET أيضًا إمكانية تحديد الخط البديل لأغراض التصيير. تساعد هذه الآلية عندما لا يتوفر الخط المطلوب على الجهاز الذي تتم فيه التحويل. يمكن للمستخدمين توفير قائمة بأسماء الخطوط كبديل للخط المطلوب أصلاً. لتحقيق ذلك، كشفت APIs عن طريقة [**FontConfigs.set_font_substitutes**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_substitutes/#str-list) التي تقبل معلمين: الأول هو من نوع **string**، وهو اسم الخط الذي يحتاج إلى الاستبدال، والثاني هو مصفوفة من نوع **string**، ويمكن للمستخدمين تقديم قائمة بأسماء الخطوط كبديل للخط الأصلي (المحدد في المعامل الأول).

فيما يلي سيناريو استخدام بسيط.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SetCustomFontFolders-FontSubstitution.py" >}}

## **تجميع المعلومات**

بالإضافة إلى الطرق المذكورة أعلاه، توفر APIs الخاصة بـ Aspose.Cells لـ Python via .NET أيضًا وسائل لجمع المعلومات حول المصادر والاستبدالات التي تم ضبطها.

1. تقوم الطريقة [**FontConfigs.get_font_sources**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/get_font_sources/#) بإرجاع مصفوفة من نوع [**FontSourceBase**](https://reference.aspose.com/cells/python-net/aspose.cells/fontsourcebase) التي تحتوي على قائمة مصادر الخط المحددة. في حالة عدم تعيين مصادر، ستقوم الطريقة [**FontConfigs.get_font_sources**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/get_font_sources/#) بإرجاع مصفوفة فارغة.
1. تقوم الطريقة [**FontConfigs.get_font_substitutes**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/get_font_substitutes/#str) بقبول معامل من نوع **string** يسمح بتحديد اسم الخط الذي تم تعيين الاستبدال له. في حالة عدم تعيين الاستبدال لاسم الخط المحدد، ستقوم الطريقة [**FontConfigs.get_font_substitutes**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/get_font_substitutes/#str) بإرجاع قيمة خالية.

## **مواضيع متقدمة**
- [تعيين الخط الافتراضي أثناء تقديم جدول البيانات إلى الصور](/cells/ar/python-net/set-default-font-while-rendering-spreadsheet-to-images/)
- [تعيين خاصية DefaultFont من PdfSaveOptions و ImageOrPrintOptions لتكون لها الأولوية](/cells/ar/python-net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [صيغ الخط المدعمة](/cells/ar/python-net/supported-font-formats/)
- [ورقة العمل إلى صورة - تعيين تنسيق البكسل للصورة المقدمة](/cells/ar/python-net/worksheet-to-image-set-pixel-format-for-the-rendered-image/)


---
title: تكوين الخطوط لتقديم جداول البيانات
type: docs
weight: 10
url: /ar/java/configuring-fonts-for-rendering-spreadsheets/
---
## **سيناريوهات الاستخدام الممكنة**

توفر واجهات برمجة التطبيقات Aspose.Cells إمكانية عرض جداول البيانات بتنسيقات صور بالإضافة إلى تحويلها إلى تنسيقات PDF و XPS. لتحقيق أقصى قدر من دقة التحويل ، من الضروري أن تكون الخطوط المستخدمة في جدول البيانات متاحة في دليل الخطوط الافتراضي لنظام التشغيل. في حالة عدم وجود الخطوط المطلوبة ، ستحاول واجهات برمجة تطبيقات Aspose.Cells استبدال الخطوط المطلوبة بالخطوط المتاحة.

## **اختيار الخطوط**

فيما يلي العملية التي تتبعها واجهات برمجة التطبيقات Aspose.Cells خلف الكواليس.

1. يحاول API العثور على الخطوط في نظام الملفات المطابقة لاسم الخط الدقيق المستخدم في جدول البيانات.
1.  إذا لم يتمكن API من العثور على الخطوط التي لها نفس الاسم بالضبط ، فإنه يحاول استخدام الخط الافتراضي المحدد ضمن المصنف[**DefaultStyle.Font**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font) خاصية.
1.  إذا كان API لا يمكنه تحديد مكان الخط المعرف ضمن المصنف[**DefaultStyle.Font**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font) الخاصية ، يحاول استخدام الخط المحدد ضمن[**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveoptions#DefaultFont) أو[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions#DefaultFont) خاصية.
1.  إذا كان API لا يمكنه تحديد مكان الخط المعرف أسفل[**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveoptions#DefaultFont) أو[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions#DefaultFont) الخاصية ، يحاول استخدام الخط المحدد ضمن[**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs#DefaultFontName) خاصية.
1.  إذا كان API لا يمكنه تحديد مكان الخط المعرف أسفل[**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs#DefaultFontName) الخاصية ، فهو يحاول تحديد أنسب الخطوط من جميع الخطوط المتاحة.
1. أخيرًا ، إذا لم يتمكن API من العثور على أي خطوط في نظام الملفات ، فسيتم عرض جدول البيانات باستخدام Arial.

{{% alert color="primary" %}}

 تقوم واجهات برمجة التطبيقات Aspose.Cells دائمًا بمسح دليل الخطوط الافتراضي لنظام التشغيل مع استثناء واحد ، وهو ؛ عندما الحجج JVM**-DAspose.Cells.FontDirExc = "YourFontDir"**تم تعيينها. في هذه الحالة ، ستتخطى واجهات برمجة التطبيقات Aspose.Cells فحص دليل الخطوط الافتراضية لنظام التشغيل وستبحث فقط في المسار كما هو محدد في وسيطات JVM المذكورة أعلاه.

{{% /alert %}}

## **تعيين مجلدات الخطوط المخصصة**

 Aspose.Cells تقوم واجهات برمجة التطبيقات (API) بالبحث في دليل الخط الافتراضي لنظام التشغيل عن الخطوط المطلوبة. في حالة عدم توفر الخطوط المطلوبة في دليل خطوط النظام ، تقوم واجهات برمجة التطبيقات بالبحث من خلال الدلائل المخصصة (المعرفة من قبل المستخدم). ال[**FontConfigs**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs)كشفت class عن عدد من الطرق لتعيين أدلة الخطوط المخصصة كما هو مفصل أدناه.

1. [**FontConfigs.setFontFolder**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolder(java.lang.String,%20boolean)): هذه الطريقة مفيدة إذا كان هناك مجلد واحد فقط ليتم تعيينه.
1. [**FontConfigs.setFontFolders**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolders(java.lang.String[],%20boolean)): هذه الطريقة مفيدة عندما تكون الخطوط موجودة في مجلدات متعددة ويريد المستخدم تعيين جميع المجلدات بشكل منفصل بدلاً من دمج كل الخطوط في مجلد واحد.
1. [**FontConfigs.setFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontSources(com.aspose.cells.FontSourceBase[])): هذه الآلية مفيدة عندما يرغب المستخدم في تحميل خطوط من مجلدات متعددة أو ملف خط واحد أو بيانات خط من مصفوفة من البايت.

{{% alert color="primary" %}}

 كلاهما[**FontConfigs.setFontFolder**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolder(java.lang.String,%20boolean)) & [**FontConfigs.setFontFolders**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolders(java.lang.String[],%20boolean) ) تقبل أساليب المعامل الثاني من النوع المنطقي. تمرير**حقيقي**كمعامل ثانٍ سيوجه Aspose.Cells APIs للبحث في المجلدات الفرعية عن ملفات الخطوط.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetCustomFontFolders-SetCustomFontFolders.java" >}}

{{% alert color="primary" %}}

يرجى استخدام أي من الطرق المذكورة أعلاه في بداية التطبيق ، أي ؛ قبل استدعاء أي كائنات أخرى من Aspose.Cells APIs.

{{% /alert %}} {{% alert color="primary" %}}

إذا تم استخدام أكثر من طريقة من الطرق المذكورة أعلاه لتعيين مصادر الخطوط ، فسيتم تفعيل الإعدادات الأخيرة فقط.

{{% /alert %}}

## **آلية استبدال الخط**

توفر واجهات برمجة التطبيقات Aspose.Cells أيضًا القدرة على تحديد طاقم الطباعة البديل لأغراض التصيير. هذه الآلية مفيدة عندما لا يكون الخط المطلوب متاحًا على الجهاز حيث يجب إجراء التحويل. يمكن للمستخدمين توفير قائمة بأسماء الخطوط كبديل للخط المطلوب في الأصل. من أجل تحقيق ذلك ، كشفت واجهات برمجة التطبيقات Aspose.Cells طريقة FontConfigs.setFontSubstitutes التي تقبل معلمتين. المعلمة الأولى من النوع**سلسلة** ، والذي يجب أن يكون اسم الخط الذي يجب استبداله. المعلمة الثانية هي مصفوفة من النوع**سلسلة**. يمكن للمستخدمين توفير قائمة بأسماء الخطوط كبدائل للخط الأصلي (المحدد في المعلمة الأولى).

هنا سيناريو استخدام بسيط.

{{< highlight "java" >}}

 //Substituting the Arial font with Times New Roman & Calibri

FontConfigs.setFontSubstitutes("Arial", new String[]{ "Times New Roman", "Calibri" });

{{< /highlight >}}

## **جمع المعلومات**

بالإضافة إلى الأساليب المذكورة أعلاه ، قدمت واجهات برمجة التطبيقات Aspose.Cells أيضًا وسائل لجمع المعلومات حول المصادر والبدائل التي تم تعيينها.

1. [**FontConfigs.getFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSources() ): ترجع هذه الطريقة مصفوفة من النوع[**FontSourceBase**](https://reference.aspose.com/cells/java/com.aspose.cells/FileFontSource)تحتوي على قائمة بمصادر الخطوط المحددة. في حالة عدم وجود مصادر محددة ، فإن[**FontConfigs.getFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSources()) سيعيد التابع مصفوفة فارغة.
1. [**FontConfigs.getFontSubstitutes**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSubstitutes(java.lang.String) ): تقبل هذه الطريقة معلمة من النوع**سلسلة** السماح بتحديد اسم الخط الذي تم استبداله. في حالة عدم تعيين أي استبدال لاسم الخط المحدد ثم ملف[**FontConfigs.getFontSubstitutes**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSubstitutes(java.lang.String)) ستعيد الطريقة فارغة.

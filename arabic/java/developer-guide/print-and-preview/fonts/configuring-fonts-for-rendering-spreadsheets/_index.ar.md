---
title: تكوين الخطوط لرسم الجداول الخليوية
type: docs
weight: 10
url: /ar/java/configuring-fonts-for-rendering-spreadsheets/
---

## **سيناريوهات الاستخدام المحتملة**

توفر Aspose.Cells APIs مرفق تقديم الجداول الخليوية بتنسيق الصور وتحويلها إلى تنسيقات PDF و XPS. من أجل زيادة دقة التحويل، من الضروري أن تكون الخطوط المستخدمة في الجدول الخليوي متوفرة في مجلد الخط الافتراضي لنظام التشغيل. في حالة عدم توفر الخطوط المطلوبة، ستحاول Aspose.Cells APIs استبدال الخطوط المطلوبة بتلك المتاحة.

## **اختيار الخطوط**

أدناه هو العملية التي تتبعها Aspose.Cells APIs خلف الكواليس.

1. تحاول الواجهة البرمجية الخارجية العثور على الخطوط في نظام الملفات تطابق اسم الخط المستخدم في الجدول الخليوي.
1. إذا لم تتمكن الواجهة البرمجية الخارجية من العثور على الخطوط بنفس الاسم الدقيق، فإنها تحاول استخدام الخط الافتراضي المحدد في خصائص الدفتر.
1. إذا لم تتمكن الواجهة البرمجية الخارجية من تحديد الخط المحدد تحت خصائص الدفتر، فإنها تحاول استخدام الخط المحدد تحت خصائص [**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveoptions#DefaultFont) أو [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions#DefaultFont).
1. إذا لم تتمكن الواجهة البرمجية الخارجية من تحديد الخط المحدد تحت خصائص [**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveoptions#DefaultFont) أو [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions#DefaultFont)، فإنها تحاول استخدام الخط المحدد تحت خصائص [**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs#DefaultFontName).
1. إذا لم تتمكن الواجهة البرمجية الخارجية من تحديد الخط المحدد تحت خصائص [**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs#DefaultFontName)، فإنها تحاول اختيار أنسب الخطوط من جميع الخطوط المتاحة.
1. وأخيرًا، إذا لم تتمكن الواجهة البرمجية الخارجية من العثور على أي خطوط في نظام الملفات، تقوم بتقديم الجدول الخليوي باستخدام Arial.

{{% alert color="primary" %}}

تقوم دائمًا Aspose.Cells APIs بفحص مجلد الخط الافتراضي لنظام التشغيل باستثناء واحد، وهو عندما يتم تعيين وسائط JVM **-DAspose.Cells.FontDirExc="YourFontDir"**. في هذه الحالة، تقوم Aspose.Cells APIs بتخطي فحص مجلد الخط الافتراضي لنظام التشغيل والبحث فقط في المسار كما هو محدد في الوسائط JVM المذكورة سابقًا.

{{% /alert %}}

## **تعيين مجلدات الخط المخصصة**

تقوم Aspose.Cells APIs بالبحث في مجلد الخط الافتراضي لنظام التشغيل عن الخطوط المطلوبة. في حالة عدم توفر الخطوط المطلوبة في مجلد الخط الخاص بالنظام، تقوم الواجهة البرمجية الخارجية بالبحث من خلال المجلدات المخصصة (المحددة من قبل المستخدم). كما يوضح الفئة [**FontConfigs**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs) عددًا من الطرق لتعيين مجلدات الخط المخصصة كما هو مفصل أدناه.

1. [**FontConfigs.setFontFolder**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolder(java.lang.String,%20boolean)): تُفيد هذه الطريقة إذا كان هناك مجلد واحد فقط يجب تعيينه.
1. [**FontConfigs.setFontFolders**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolders(java.lang.String[],%20boolean)): تَكون هذه الطريقة مفيدةً عندما تتواجد الخطوط في مجلدات متعددة ويرغب المستخدم في تعيين كافة المجلدات بشكل منفصل بدلاً من دمج كل الخطوط في مجلد واحد.
1. [**FontConfigs.setFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontSources(com.aspose.cells.FontSourceBase[])): يكون هذا الآلية مفيدًا عندما يرغب المستخدم في تحميل الخطوط من مجلدين أو ملف خط واحد أو بيانات الخط من مصفوفة بايت.

{{% alert color="primary" %}}

كلتا الطريقتين [**FontConfigs.setFontFolder**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolder(java.lang.String,%20boolean)) و [**FontConfigs.setFontFolders**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolders(java.lang.String[],%20boolean)) تقبلان معلمة ثانية من النوع **Boolean**. يوجه تمرير **صحيح** كمعلمة ثانية سيوجه واجهات برمجة التطبيقات لـ Aspose.Cells للبحث في المجلدات الفرعية لملفات الخطوط.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetCustomFontFolders-SetCustomFontFolders.java" >}}

{{% alert color="primary" %}}

يرجى استخدام أيًا من الطرق المذكورة أعلاه في بداية التطبيق، أي قبل استدعاء أي كائنات أخرى من واجهات برمجة التطبيقات Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

إذا تم استخدام أكثر من واحدة من الطرق المذكورة أعلاه لتعيين مصادر الخطوط، فإن الإعدادات الأخيرة فقط ستكون سارية المفعول.

{{% /alert %}}

## **آلية الاستبدال للخطوط**

توفر واجهات برمجة التطبيقات Aspose.Cells أيضًا القدرة على تحديد الخط البديل لأغراض التقديم. تكون هذه الآلية مفيدة عندما لا يكون الخط المطلوب متوفرًا على الجهاز الذي يجب أن تتم فيه التحويل. يمكن للمستخدمين توفير قائمة أسماء الخطوط كبديل للخط المطلوب أصلاً. ومن أجل تحقيق ذلك، فقد عرضت واجهات برمجة التطبيقاتAspose.Cells الطريقة FontConfigs.setFontSubstitutes التي تقبل 2 معلمة. المعلمة الأولى هي من النوع **String**، التي يجب أن تكون اسم الخط الذي يجب أن يكون بديلًا. المعلمة الثانية هي مصفوفة من النوع **String**. يمكن للمستخدمين تقديم قائمة من أسماء الخطوط كبدائل للخط الأصلي (المحدد في المعلمة الأولى).

فيما يلي سيناريو استخدام بسيط.

{{< highlight java >}}

 //Substituting the Arial font with Times New Roman & Calibri

FontConfigs.setFontSubstitutes("Arial", new String[] { "Times New Roman", "Calibri" });

{{< /highlight >}}

## **تجميع المعلومات**

بالإضافة إلى الطرق المذكورة أعلاه، قدمت واجهات برمجة التطبيقات Aspose.Cells وسيلة لجمع المعلومات حول المصادر والاستبدالات التي تم تعيينها.

1. [**FontConfigs.getFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSources--): تُخرج هذه الطريقة مصفوفة من النوع [**FontSourceBase**](https://reference.aspose.com/cells/java/com.aspose.cells/FileFontSource) تحتوي على قائمة المصادر النوعية للخطوط المحددة. في حالة عدم تعيين أي مصادر، فإن الطريقة [**FontConfigs.getFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSources--) ستُرجع مصفوفة فارغة.
1. [**FontConfigs.getFontSubstitutes**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSubstitutes(java.lang.String)): تقبل هذه الطريقة معلمة من نوع **String** تمكن من تحديد اسم الخط الذي تم تعيين الاستبدال له. في حالة عدم تم تعيين استبدال لاسم الخط المحدد ستُعيد الطريقة [**FontConfigs.getFontSubstitutes**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSubstitutes(java.lang.String)) قيمة فارغة.

---
title: ضبط الخطوط لعرض أوراق العمل باستخدام Node.js عبر C++
linktitle: تكوين الخطوط لرسم الجداول الخليوية
type: docs
weight: 10
url: /ar/nodejs-cpp/configuring-fonts-for-rendering-spreadsheets/
description: تعرف على كيفية تكوين الخطوط لعرض أوراق العمل باستخدام Aspose.Cells for Node.js via C++. تأكد من توفر الخطوط للتحويل الأمثل للجودة.
---

## **سيناريوهات الاستخدام المحتملة**

توفر واجهات برمجة التطبيقات Aspose.Cells إمكانية عرض أوراق العمل بصيغ الصور بالإضافة إلى تحويلها إلى صيغ PDF و XPS. لتحقيق أعلى قدر من دقة التحويل، من الضروري أن تتوفر الخطوط المستخدمة في ورقة العمل في مجلد الخطوط الافتراضي لنظام التشغيل. في حالة عدم وجود الخطوط المطلوبة، ستحاول واجهات برمجة التطبيقات Aspose.Cells استبدال الخطوط المطلوبة بأخرى متاحة.

## **اختيار الخطوط**

أدناه هو العملية التي تتبعها Aspose.Cells APIs خلف الكواليس.

1. تحاول الواجهة البرمجية الخارجية العثور على الخطوط في نظام الملفات تطابق اسم الخط المستخدم في الجدول الخليوي.
1. إذا لم تتمكن الواجهة البرمجية الخارجية من العثور على الخطوط بنفس الاسم الدقيق، فإنها تحاول استخدام الخط الافتراضي المحدد في خصائص الدفتر.
1. إذا لم تتمكن الواجهة البرمجية الخارجية من تحديد الخط المحدد تحت خصائص الدفتر، فإنها تحاول استخدام الخط المحدد تحت خصائص [**PdfSaveOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getDefaultFont--) أو [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--).
1. إذا لم تتمكن الواجهة البرمجية الخارجية من تحديد الخط المحدد تحت خصائص [**PdfSaveOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getDefaultFont--) أو [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--)، فإنها تحاول استخدام الخط المحدد تحت خصائص [**FontConfigs.getDefaultFontName()**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getDefaultFontName--).
1. إذا لم تتمكن الواجهة البرمجية الخارجية من تحديد الخط المحدد تحت خصائص [**FontConfigs.getDefaultFontName()**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getDefaultFontName--)، فإنها تحاول اختيار أنسب الخطوط من جميع الخطوط المتاحة.
1. وأخيرًا، إذا لم تتمكن الواجهة البرمجية الخارجية من العثور على أي خطوط في نظام الملفات، تقوم بتقديم الجدول الخليوي باستخدام Arial.

## **تعيين مجلدات الخط المخصصة**

تبحث واجهات برمجة التطبيقات Aspose.Cells في مجلد الخطوط الافتراضي لنظام التشغيل عن الخطوط المطلوبة. في حال عدم توفر الخطوط المطلوبة في مجلد الخطوط، تبحث الواجهات عبر المجلدات المخصصة (المعرفة من قبل المستخدم). exposes [**FontConfigs**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs) العديد من الطرق لضبط مجلدات الخطوط المخصصة كما هو موضح أدناه.

1. [**FontConfigs.setFontFolder(string, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontFolder-string-boolean-): تُفيد هذه الطريقة إذا كان هناك مجلد واحد فقط يجب تعيينه.
1. [**FontConfigs.setFontFolders(string[], boolean)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontFolders-stringarray-boolean-): تَكون هذه الطريقة مفيدةً عندما تتواجد الخطوط في مجلدات متعددة ويرغب المستخدم في تعيين كافة المجلدات بشكل منفصل بدلاً من دمج كل الخطوط في مجلد واحد.
1. [**FontConfigs.setFontSources(FontSourceBase[])**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontSources-fontsourcebasearray-): يكون هذا الآلية مفيدًا عندما يرغب المستخدم في تحميل الخطوط من مجلدين أو ملف خط واحد أو بيانات الخط من مصفوفة بايت.

{{% alert color="primary" %}}

كلاً من طريقتي [**FontConfigs.setFontFolder(string, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontFolder-string-boolean-) و [**FontConfigs.setFontFolders(string[], boolean)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontFolders-stringarray-boolean-) تقبلان معامل ثانوي من نوع Boolean. تمرير **true** كمعامل ثانوي سيوجه واجهات برمجة التطبيقات لـ Aspose.Cells للبحث في الأنظمة الفرعية عن ملفات الخطوط.

{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Defining string variables to store paths to font folders & font file
const fontFolder1 = path.join(dataDir, "Arial");
const fontFolder2 = path.join(dataDir, "Calibri");
const fontFile = path.join(dataDir, "arial.ttf"); 

// Setting first font folder with SetFontFolder method
// Second parameter directs the API to search the subfolders for font files
AsposeCells.FontConfigs.setFontFolder(fontFolder1, true);

// Setting both font folders with SetFontFolders method
// Second parameter prohibits the API to search the subfolders for font files
AsposeCells.FontConfigs.setFontFolders([fontFolder1, fontFolder2], false);

// Defining FolderFontSource
const sourceFolder = new AsposeCells.FolderFontSource(fontFolder1, false);

// Defining FileFontSource
const sourceFile = new AsposeCells.FileFontSource(fontFile);

// Defining MemoryFontSource
const sourceMemory = new AsposeCells.MemoryFontSource(require("fs").readFileSync(fontFile));

// Setting font sources
AsposeCells.FontConfigs.setFontSources([sourceFolder, sourceFile, sourceMemory]);
```

{{% alert color="primary" %}}

يرجى استخدام أي من الطرق المذكورة أعلاه في بدء التطبيق، أي قبل استدعاء أي كائنات أخرى من APIs Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

إذا تم استخدام جميع الطرق المذكورة أعلاه لتحديد مصادر الخطوط، فسيتم اعتماد إعدادات آخرى فقط.

{{% /alert %}}

## **آلية الاستبدال للخطوط**

توفر واجهات برمجة التطبيقات Aspose.Cells أيضًا القدرة على تحديد الخط البديل لأغراض العرض. هذه الآلية مفيدة عندما لا تتوفر الخطوط المطلوبة على الجهاز الذي يتم عليه التحويل. يمكن للمستخدمين تقديم قائمة بأسماء الخطوط كبديل للخطوط الأصلية. لتحقيق ذلك، توفر الواجهات Aspose.Cells الأسلوب [**FontConfigs.setFontSubstitutes(string, string[])**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontSubstitutes-string-stringarray-) الذي يقبل معاملين. المعامل الأول هو من نوع **string**، ويجب أن يكون اسم الخط الذي يحتاج إلى استبداله. المعامل الثاني هو مصفوفة من نوع **string**، ويمكن للمستخدمين تقديم قائمة بأسماء الخطوط كبديل لاسم الخط الأصلي (المحدد في المعامل الأول).

فيما يلي سيناريو استخدام بسيط.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Substituting the Arial font with Times New Roman & Calibri
AsposeCells.FontConfigs.setFontSubstitutes("Arial", ["Times New Roman", "Calibri"]);
```

## **تجميع المعلومات**

بالإضافة إلى الطرق المذكورة أعلاه، قامت واجهات برمجة التطبيقات Aspose.Cells أيضًا بتوفير وسائل لجمع المعلومات حول المصادر والاستبدالات التي تم تعيينها.

1. ترجع طريقة [**FontConfigs.getFontSources()**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getFontSources--) مصفوفة من نوع [**FontSourceBase**](https://reference.aspose.com/cells/nodejs-cpp/fontsourcebase) تحتوي على قائمة مصادر الخطوط المحددة. في حال عدم تعيين أي مصادر، ستعيد طريقة [**FontConfigs.getFontSources()**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getFontSources--) مصفوفة فارغة.
1. تقبل طريقة [**FontConfigs.getFontSubstitutes(string)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getFontSubstitutes-string-) وسيط من نوع **string** يحدد اسم الخط الذي تم تعيين استبداله. في حال عدم تعيين استبدال للخط المحدد، ستعيد طريقة [**FontConfigs.getFontSubstitutes(string)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getFontSubstitutes-string-) قيمة null.

## **مواضيع متقدمة**
- [تعيين الخط الافتراضي أثناء تقديم جدول البيانات إلى الصور](/cells/ar/nodejs-cpp/set-default-font-while-rendering-spreadsheet-to-images/)
- [تعيين خاصية DefaultFont من PdfSaveOptions و ImageOrPrintOptions لتكون لها الأولوية](/cells/ar/nodejs-cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [صيغ الخط المدعمة](/cells/ar/nodejs-cpp/supported-font-formats/)
- [ورقة العمل إلى صورة - تعيين تنسيق البكسل للصورة المقدمة](/cells/ar/nodejs-cpp/worksheet-to-image-set-pixel-format-for-the-rendered-image/)
{{< app/cells/assistant language="nodejs-cpp" >}}

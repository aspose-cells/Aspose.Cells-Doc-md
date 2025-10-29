---
title: تكوين الخطوط لعرض الجداول الإلكترونية باستخدام JavaScript عبر C++
linktitle: تكوين الخطوط لرسم الجداول الخليوية
type: docs
weight: 10
url: /ar/javascript-cpp/configuring-fonts-for-rendering-spreadsheets/
description: تعلم كيفية تكوين الخطوط لعرض الجداول الإلكترونية باستخدام Aspose.Cells for JavaScript عبر C++. تأكد من توفر الخطوط لزيادة دقة التحويل.
---

## **سيناريوهات الاستخدام المحتملة**

توفر واجهات برمجة التطبيقات Aspose.Cells إمكانية عرض أوراق العمل بصيغ الصور بالإضافة إلى تحويلها إلى صيغ PDF و XPS. لتحقيق أعلى قدر من دقة التحويل، من الضروري أن تتوفر الخطوط المستخدمة في ورقة العمل في مجلد الخطوط الافتراضي لنظام التشغيل. في حالة عدم وجود الخطوط المطلوبة، ستحاول واجهات برمجة التطبيقات Aspose.Cells استبدال الخطوط المطلوبة بأخرى متاحة.

## **اختيار الخطوط**

أدناه هو العملية التي تتبعها Aspose.Cells APIs خلف الكواليس.

1. تحاول الواجهة البرمجية الخارجية العثور على الخطوط في نظام الملفات تطابق اسم الخط المستخدم في الجدول الخليوي.
1. إذا لم تتمكن الواجهة البرمجية الخارجية من العثور على الخطوط بنفس الاسم الدقيق، فإنها تحاول استخدام الخط الافتراضي المحدد في خصائص الدفتر.
1. إذا لم تتمكن الواجهة البرمجية الخارجية من تحديد الخط المحدد تحت خصائص الدفتر، فإنها تحاول استخدام الخط المحدد تحت خصائص [**PdfSaveOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#defaultFont--) أو [**ImageOrPrintOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#defaultFont--).
1. إذا لم تتمكن الواجهة البرمجية الخارجية من تحديد الخط المحدد تحت خصائص [**PdfSaveOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#defaultFont--) أو [**ImageOrPrintOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#defaultFont--)، فإنها تحاول استخدام الخط المحدد تحت خصائص [**FontConfigs.defaultFontName**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#defaultFontName--).
1. إذا لم تتمكن الواجهة البرمجية الخارجية من تحديد الخط المحدد تحت خصائص [**FontConfigs.defaultFontName**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#defaultFontName--)، فإنها تحاول اختيار أنسب الخطوط من جميع الخطوط المتاحة.
1. وأخيرًا، إذا لم تتمكن الواجهة البرمجية الخارجية من العثور على أي خطوط في نظام الملفات، تقوم بتقديم الجدول الخليوي باستخدام Arial.

## **تعيين مجلدات الخط المخصصة**

تبحث واجهات برمجة التطبيقات Aspose.Cells في مجلد الخطوط الافتراضي لنظام التشغيل عن الخطوط المطلوبة. في حال عدم توفر الخطوط المطلوبة في مجلد الخطوط، تبحث الواجهات عبر المجلدات المخصصة (المعرفة من قبل المستخدم). exposes [**FontConfigs**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs) العديد من الطرق لضبط مجلدات الخطوط المخصصة كما هو موضح أدناه.

1. [**FontConfigs.fontFolder(string, boolean)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontFolder-string-boolean-): تُفيد هذه الطريقة إذا كان هناك مجلد واحد فقط يجب تعيينه.
1. [**FontConfigs.fontFolders(string[], boolean)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontFolders-stringarray-boolean-): تَكون هذه الطريقة مفيدةً عندما تتواجد الخطوط في مجلدات متعددة ويرغب المستخدم في تعيين كافة المجلدات بشكل منفصل بدلاً من دمج كل الخطوط في مجلد واحد.
1. [**FontConfigs.fontSources(FontSourceBase[])**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSources-fontsourcebasearray-): يكون هذا الآلية مفيدًا عندما يرغب المستخدم في تحميل الخطوط من مجلدين أو ملف خط واحد أو بيانات الخط من مصفوفة بايت.

{{% alert color="primary" %}}

كلاً من طريقتي [**FontConfigs.fontFolder(string, boolean)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontFolder-string-boolean-) و [**FontConfigs.fontFolders(string[], boolean)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontFolders-stringarray-boolean-) تقبلان معامل ثانوي من نوع Boolean. تمرير **true** كمعامل ثانوي سيوجه واجهات برمجة التطبيقات لـ Aspose.Cells للبحث في الأنظمة الفرعية عن ملفات الخطوط.

{{% /alert %}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Font Configuration Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Font Configuration Example</h1>
        <p>Select an Excel file (optional) and font resources to configure Aspose.Cells font sources in the browser.</p>

        <label>Excel File (optional):</label>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <br/><br/>

        <label>Font File (.ttf/.otf) (optional):</label>
        <input type="file" id="fontFileInput" accept=".ttf,.otf" />
        <br/><br/>

        <label>Font Folder (optional, select a folder):</label>
        <input type="file" id="fontFolderInput" webkitdirectory directory multiple />
        <br/><br/>

        <button id="runExample">Configure Fonts</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const fontFileInput = document.getElementById('fontFileInput');
            const fontFolderInput = document.getElementById('fontFolderInput');
            const resultDiv = document.getElementById('result');

            // Basic validation: ensure at least one font resource is provided (file or folder)
            if (!fontFileInput.files.length && !fontFolderInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select at least one font file or a font folder.</p>';
                return;
            }

            // Defining string variables to store paths/names to font folders & font file
            // (In browser environment we use simple names or uploaded file names)
            const fontFolder1 = "Arial";
            const fontFolder2 = "Calibri";
            const fontFile = "arial.ttf";

            // Setting first font folder (converted from setFontFolder)
            AsposeCells.FontConfigs.fontFolder = fontFolder1;
            // Preserve the subfolder-search flag from original API call as a separate property
            AsposeCells.FontConfigs.fontFolderSearchSubFolders = true;

            // Setting both font folders (converted from setFontFolders)
            AsposeCells.FontConfigs.fontFolders = [fontFolder1, fontFolder2];
            // Preserve the subfolder-search flag as a separate property
            AsposeCells.FontConfigs.fontFoldersSearchSubFolders = false;

            // Defining FolderFontSource
            const sourceFolder = new AsposeCells.FolderFontSource(fontFolder1, false);

            // Defining FileFontSource
            const sourceFile = new AsposeCells.FileFontSource(fontFile);

            // Defining MemoryFontSource
            let memoryFontBytes = new Uint8Array([]);
            if (fontFileInput.files.length) {
                const ff = fontFileInput.files[0];
                const arrayBuffer = await ff.arrayBuffer();
                memoryFontBytes = new Uint8Array(arrayBuffer);
            } else if (fontFolderInput.files.length) {
                // If a folder was provided, try to find a .ttf/.otf inside it and use the first found
                const files = Array.from(fontFolderInput.files);
                const fontCandidate = files.find(f => f.name.toLowerCase().endsWith('.ttf') || f.name.toLowerCase().endsWith('.otf'));
                if (fontCandidate) {
                    const arrayBuffer = await fontCandidate.arrayBuffer();
                    memoryFontBytes = new Uint8Array(arrayBuffer);
                }
            }
            const sourceMemory = new AsposeCells.MemoryFontSource(memoryFontBytes);

            // Setting font sources (converted from setFontSources)
            AsposeCells.FontConfigs.fontSources = [sourceFolder, sourceFile, sourceMemory];

            // Provide feedback to the user
            resultDiv.innerHTML = '<p style="color: green;">Font configuration applied successfully.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

يرجى استخدام أي من الطرق المذكورة أعلاه في بدء التطبيق، أي قبل استدعاء أي كائنات أخرى من APIs Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

إذا تم استخدام جميع الطرق المذكورة أعلاه لتحديد مصادر الخطوط، فسيتم اعتماد إعدادات آخرى فقط.

{{% /alert %}}

## **آلية الاستبدال للخطوط**

توفر واجهات برمجة التطبيقات Aspose.Cells أيضًا القدرة على تحديد الخط البديل لأغراض العرض. هذه الآلية مفيدة عندما لا تتوفر الخطوط المطلوبة على الجهاز الذي يتم عليه التحويل. يمكن للمستخدمين تقديم قائمة بأسماء الخطوط كبديل للخطوط الأصلية. لتحقيق ذلك، توفر الواجهات Aspose.Cells الأسلوب [**FontConfigs.fontSubstitutes(string, string[])**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSubstitutes-string-stringarray-) الذي يقبل معاملين. المعامل الأول هو من نوع **string**، ويجب أن يكون اسم الخط الذي يحتاج إلى استبداله. المعامل الثاني هو مصفوفة من نوع **string**، ويمكن للمستخدمين تقديم قائمة بأسماء الخطوط كبديل لاسم الخط الأصلي (المحدد في المعامل الأول).

فيما يلي سيناريو استخدام بسيط.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Substituting the Arial font with Times New Roman & Calibri
            // Converted from: AsposeCells.FontConfigs.setFontSubstitutes("Arial", ["Times New Roman", "Calibri"]);
            AsposeCells.FontConfigs.fontSubstitutes = { "Arial": ["Times New Roman", "Calibri"] };

            // Saving the (possibly modified) workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the processed file.</p>';
        });
    </script>
</html>
```

## **تجميع المعلومات**

بالإضافة إلى الطرق المذكورة أعلاه، قامت واجهات برمجة التطبيقات Aspose.Cells أيضًا بتوفير وسائل لجمع المعلومات حول المصادر والاستبدالات التي تم تعيينها.

1. ترجع طريقة [**FontConfigs.fontSources**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSources--) مصفوفة من نوع [**FontSourceBase**](https://reference.aspose.com/cells/javascript-cpp/fontsourcebase) تحتوي على قائمة مصادر الخطوط المحددة. في حال عدم تعيين أي مصادر، ستعيد طريقة [**FontConfigs.fontSources**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSources--) مصفوفة فارغة.
1. تقبل طريقة [**FontConfigs.fontSubstitutes(string)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSubstitutes-string-) وسيط من نوع **string** يحدد اسم الخط الذي تم تعيين استبداله. في حال عدم تعيين استبدال للخط المحدد، ستعيد طريقة [**FontConfigs.fontSubstitutes(string)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSubstitutes-string-) قيمة null.

## **مواضيع متقدمة**
- [تعيين الخط الافتراضي أثناء تقديم جدول البيانات إلى الصور](/cells/ar/javascript-cpp/set-default-font-while-rendering-spreadsheet-to-images/)
- [تعيين خاصية DefaultFont من PdfSaveOptions و ImageOrPrintOptions لتكون لها الأولوية](/cells/ar/javascript-cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [صيغ الخط المدعمة](/cells/ar/javascript-cpp/supported-font-formats/)
- [ورقة العمل إلى صورة - تعيين تنسيق البكسل للصورة المقدمة](/cells/ar/javascript-cpp/worksheet-to-image-set-pixel-format-for-the-rendered-image/)

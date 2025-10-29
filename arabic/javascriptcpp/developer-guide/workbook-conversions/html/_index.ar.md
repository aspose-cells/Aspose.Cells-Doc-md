---
title: HTML مع جافا سكريبت عبر ++C
linktitle: HTML
type: docs
weight: 230
url: /ar/javascript-cpp/convert-excel-to-html/
---

## **تحويل دفتر العمل في إكسل إلى HTML**
يوفر API Aspose.Cells دعمًا للتصدير إلى تنسيق HTML. لهذا الغرض، يستخدم Aspose.Cells فئة [**HtmlSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions) لتوفير المرونة للتحكم في عدة جوانب من مخرجات HTML.

يعرض مثال الكود أدناه كيفية حفظ مصنف كملف HTML باستخدام جافا سكريبت عبر ++C

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Convert Excel to HTML</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to HTML</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Saving the workbook to HTML format
            const outputData = workbook.save(SaveFormat.Html);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```


## **تحويل دفتر العمل في إكسل إلى ملفات MHTML**
يجمع MHTML بين HTML العادي والموارد الخارجية (أي المحتوى المرتبط عادة، مثل الصور والرسوم المتحركة والصوت، وغيرها) في ملف واحد. يُستخدم للبريد الإلكتروني بامتداد ملف .mht. يدعم Aspose.Cells قراءة وكتابة ملفات MHTML.

يعرض مثال الكود أدناه كيفية حفظ مصنف كملف MHTML باستخدام جافا سكريبت عبر ++C

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Save as MHT</title>
    </head>
    <body>
        <h1>Save Excel as MHT Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load your source workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save file to MHT format
            const outputData = workbook.save(SaveFormat.MHtml);
            const blob = new Blob([outputData], { type: 'application/octet-stream' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.mht';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download MHT File';

            resultDiv.innerHTML = '<p style="color: green;">File converted to MHT successfully! Click the download link to get the result.</p>';
        });
    </script>
</html>
```

## **مواضيع متقدمة**
- [تلائم الأعمدة والصفوف تلقائيًا أثناء تحميل HTML في دفتر العمل](/cells/ar/javascript-cpp/autofit-columns-and-rows-while-loading-html-in-workbook/)
- [تجنب العلامة العلمية للأرقام الكبيرة أثناء الاستيراد من HTML](/cells/ar/javascript-cpp/avoid-exponential-notation-of-large-numbers-while-importing/)
- [تغيير نوع الوصلة HTML المستهدفة](/cells/ar/javascript-cpp/change-the-html-link-target-type/)
- [تحويل Excel إلى HTML مع تلميحة](/cells/ar/javascript-cpp/convert-excel-to-html-with-tooltip/)
- [Create Transparent Image of Excel Worksheet](/cells/ar/javascript-cpp/create-transparent-image-of-excel-worksheet/)
- [حذف المسافات الزائدة بعد فاصلة السطر أثناء استيراد HTML](/cells/ar/javascript-cpp/delete-redundant-spaces-after-line-break-while-importing/)
- [تعطيل كشف التعليقات عند الاستخدام التسلسلي لأسفل عند الحفظ في HTML](/cells/ar/javascript-cpp/disable-downlevel-revealed-comments-while-saving-to/)
- [تعطيل تصدير النصوص الإطار وخصائص المستند](/cells/ar/javascript-cpp/disable-exporting-frame-scripts-and-document-properties/)
- [Excel إلى HTML - استخدام خيار PresentationPreference لتحسين التخطيط](/cells/ar/javascript-cpp/excel-to-html-use-presentationpreference-option-for-better-layout/)
- [استبعاد الأنماط غير المستخدمة أثناء تحويل Excel إلى HTML](/cells/ar/javascript-cpp/exclude-unused-styles-during-excel-to-html-conversion/)
- [توسيع النص من اليمين إلى اليسار أثناء تصدير ملف Excel إلى HTML](/cells/ar/javascript-cpp/expanding-text-from-right-to-left-while-exporting-excel-file-to/)
- [تصدير DataBar، ColorScale و IconSet لتنسيق الشروط أثناء تحويل Excel إلى HTML](/cells/ar/javascript-cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/)
- [تصدير التعليقات أثناء حفظ ملف Excel إلى HTML](/cells/ar/javascript-cpp/export-comments-while-saving-excel-file-to/)
- [تصدير خصائص المصنف والصفحة العمل في Excel إلى تحويل HTML](/cells/ar/javascript-cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/)
- [تصدير Excel إلى HTML مع خطوط الشبكة](/cells/ar/javascript-cpp/export-excel-to-html-with-gridlines/)
- [تصدير نطاق المنطقة المطبوعة إلى HTML](/cells/ar/javascript-cpp/export-print-area-range-to/)
- [تصدير نمط الحدود المماثل عند عدم دعم نمط الحدود من قبل متصفحات الويب](/cells/ar/javascript-cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/)
- [تصدير ورق العمل CSS بشكل منفصل في ملف HTML الناتج](/cells/ar/javascript-cpp/export-worksheet-css-separately-in-output/)
- [إخفاء المحتوى المتداخل باستخدام CrossHideRight أثناء الحفظ إلى HTML](/cells/ar/javascript-cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/)
- [بادئة أنماط عناصر الجدول باستخدام خاصية HtmlSaveOptions.TableCssId](/cells/ar/javascript-cpp/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/)
- [منع تصدير محتويات ورقة العمل المخفية عند الحفظ في HTML](/cells/ar/javascript-cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/)
- [توفير مسار ملف HTML الخاص بورقة العمل المصدرة عبر واجهة IFilePathProvider](/cells/ar/javascript-cpp/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/)
- [الاعتراف بالعلامات مغلقة ذاتياً](/cells/ar/javascript-cpp/recognise-self-closing-tags/)
- [إظهار تعبئة التدرج لـ WordArt أثناء تحويل جداول البيانات إلى HTML](/cells/ar/javascript-cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/)
- [تعيين عرض العمود إلى وحدة قابلة للتطويل مثل em أو النسبة المئوية](/cells/ar/javascript-cpp/set-column-width-to-scalable-unit-like-em-or-percent/)
- [تعيين الخط الافتراضي أثناء تقديم جدول بيانات إلى HTML](/cells/ar/javascript-cpp/set-default-font-while-rendering-spreadsheet-to/)
- [تحديد كيفية تقاطع السلسلة في HTML الناتج باستخدام HtmlCrossType](/cells/ar/javascript-cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/)
- [دعم تخطيط علامات DIV أثناء تحميل HTML إلى دفتر عمل Excel](/cells/ar/javascript-cpp/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/)

- [تمكين خصائص CSS المخصصة أثناء الحفظ إلى HTML](/cells/ar/javascript-cpp/enable-css-custom-properties-while-saving-to-html/)

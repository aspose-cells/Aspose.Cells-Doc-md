---
title: Pdf مع JavaScript عبر C++
linktitle: Pdf
type: docs
weight: 220
url: /ar/javascript-cpp/convert-excel-to-pdf/
description: تعلم كيفية تحويل مصنف Excel إلى PDF باستخدام Script Aspose.Cells for Java عبر C++. 
---

{{% alert color="primary" %}}
تدعم Aspose.Cells تحويل سجل العمل في Excel إلى PDF. في هذا المثال، سنرى التحويل الكامل لسجل عمل Excel إلى PDF.
{{% /alert %}}

## **تحويل سجل عمل Excel إلى PDF**

تستخدم ملفات PDF على نطاق واسع لتبادل المستندات بين المؤسسات والقطاعات الحكومية والأفراد. إنها صيغة مستند قياسية وغالبًا ما يُطلب من مطوري البرامج أن يجدوا طريقة لتحويل ملفات Microsoft Excel إلى مستندات PDF.

تدعم Aspose.Cells تحويل ملفات Excel إلى PDF وتحافظ على دقة الرؤية العالية في التحويل.

{{% alert color="primary" %}}
يسجل Script عبر C++ Aspose.Cells for Java مباشرة المعلومات عن API ورقم الإصدار في مستندات الإخراج. على سبيل المثال، عند تحويل المستند إلى PDF، يملأ Script عبر C++ حقل **مولد PDF** بالقيمة، مثل 'Aspose.Cells v23.2'.

يرجى ملاحظة أنه يمكنك تغيير هذه المعلومات في مستندات الإخراج عن طريق خاصية [**PdfSaveOptions.producer**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#producer--).
{{% /alert %}}

### **التحويل المباشر**

يدعم Script عبر C++ Aspose.Cells for Java التحويل من جداول البيانات إلى PDF بشكل مستقل عن البرامج الأخرى. ببساطة، احفظ ملف Excel كملف PDF باستخدام طريقة [**save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-) من فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook). توفر طريقة [**save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-) العضو [**SaveFormat.Pdf**](https://reference.aspose.com/cells/javascript-cpp/saveformat) الذي يحول ملفات Excel الأصلية إلى تنسيق PDF.

اتبع الخطوات التالية لتحويل الجداول الحسابية في Excel مباشرة إلى تنسيق PDF:

1. قم بإنشاء كائن من فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) بالاتصال ببنائه الفارغ.
1. يمكنك فتح/تحميل ملف قالب موجود أو تخطي هذه الخطوة إذا كنت تقوم بإنشاء السجل العمل من البداية.
1. أدخل أي عمل (البيانات الدخلية، تطبيق التنسيق، ضبط الصيغ، إدراج الصور أو كائنات الرسم الأخرى، وما إلى ذلك) على ورق العمل باستخدام واجهات برمجة التطبيقات Aspose.Cells.
1. عندما يكتمل كود الجدول، استدعِ طريقة [**save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-) من فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) لحفظ الجدول.

يجب أن يكون تنسيق الملف PDF، لذا حدد *Pdf* (قيمة محددة مسبقًا) من تعداد [**SaveFormat**](https://reference.aspose.com/cells/javascript-cpp/saveformat) لتوليد مستند PDF النهائي.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
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

            // Instantiate the Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save the document in PDF format
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion to PDF completed! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

### **التحويل المتقدم**

يمكنك أيضًا استخدام الفصيلة [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) لتعيين خصائص مختلفة للتحويل. تعيين خصائص مختلفة للفصيلة [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) يمنحك السيطرة على إعدادات الطباعة، الخط، الأمان، والضغط لمخرج PDF. 

أهم خاصية هي [**PdfSaveOptions.compliance**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#compliance--) التي تمكّنك من تعيين مستوى الامتثال لمعايير PDF. حاليًا، يمكنك حفظ إلى صيغ PDF 1.4، PDF 1.5، PDF 1.6، PDF 1.7، PDF/A-1a، PDF/A-1b، PDF/A-2a، PDF/A-2b، PDF/A-2u، PDF/A-3a، PDF/A-2ab، وصيغ PDF/A-3u. يرجى ملاحظة أنه مع صيغة PDF/A، يكون حجم الملف الناتج أكبر من حجم ملف PDF عادي.

#### **حفظ جدول البيانات إلى ملف PDF/A المتوافق**

مقطع الرمز المقدم أدناه يوضح كيفية استخدام فئة [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) لحفظ ملفات Excel إلى تنسيق PDF/A متوافق مع PDF.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create PDF/A from Workbook</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, PdfCompliance } = AsposeCells;

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
            // Instantiate new workbook
            const workbook = new Workbook();

            // Insert a value into the A1 cell in the first worksheet
            workbook.worksheets.get(0).cells.get(0, 0).value = "Testing PDF/A";

            // Define PdfSaveOptions
            const pdfSaveOptions = new PdfSaveOptions();

            // Set the compliance type
            pdfSaveOptions.compliance = PdfCompliance.PdfA1b;

            // Save the file to PDF with options
            const outputData = workbook.save(SaveFormat.Pdf, pdfSaveOptions);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF/A File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF/A created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}
يرجى ملاحظة، تمت إضافة الخاصية [**PdfSaveOptions.compliance**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#compliance--) مع إصدار Script عبر C++ 5.3.0.
{{% /alert %}}

#### **تعيين وقت إنشاء ملف PDF**

مع فئة [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions)، يمكنك الحصول على أو تعيين وقت إنشاء PDF. يوضح الرمز التالي استخدام الخاصية [**PdfSaveOptions.createdTime**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#createdTime--) لتعيين وقت إنشاء ملف PDF.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, PdfSaveOptions, SaveFormat, Utils } = AsposeCells;

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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create an instance of PdfSaveOptions
            const options = new PdfSaveOptions();
            options.createdTime = new Date();

            // Save the workbook to PDF format while passing the object of PdfSaveOptions
            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

#### **تعيين خيار ContentCopyForAccessibility**

مع فئة [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions)، يمكنك الحصول على أو تعيين خيار [**PdfSecurityOptions.accessibilityExtractContent**](https://reference.aspose.com/cells/javascript-cpp/pdfsecurityoptions/#accessibilityExtractContent--) للتحكم في وصول المحتوى في ملف PDF المحول.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Aspose.Cells Example - Convert to PDF with Security Options</title>
    </head>
    <body>
        <h1>Convert Excel to PDF with Security Options</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
        <a id="downloadLink" style="display: none;"></a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, PdfSecurityOptions, Utils } = AsposeCells;

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

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create an instance of PdfSaveOptions
            const pdfSaveOpt = new PdfSaveOptions();

            // Create an instance of PdfSecurityOptions
            const securityOptions = new PdfSecurityOptions();

            // Set AccessibilityExtractContent to false (converted from setAccessibilityExtractContent(false))
            securityOptions.accessibilityExtractContent = false;

            // Set the security option in the PdfSaveOptions (converted from setSecurityOptions)
            pdfSaveOpt.securityOptions = securityOptions;

            // Save the workbook to PDF format while passing the PdfSaveOptions
            const outputData = workbook.save(SaveFormat.Pdf, pdfSaveOpt);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outFile.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

#### **تصدير الخصائص المخصصة إلى ملف PDF**

مع فئة [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions)، يمكنك تصدير الخصائص المخصصة في دفتر العمل المصدر إلى PDF. وتوفر مُعدّلة [**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/javascript-cpp/pdfcustompropertiesexport/) لتحديد الطريقة التي يتم بها تصدير الخصائص. يمكن ملاحظة هذه الخصائص في Adobe Acrobat Reader بالنقر فوق ملف ثم الخصائص كما هو موضح في الصورة التالية. يمكن تنزيل ملف القالب "sourceWithCustProps.xlsx" من [هنا](sourceWithCustProps.xlsx) للفحص وملف PDF الناتج "outSourceWithCustProps" متاح [هنا](outSourceWithCustProps.pdf) للتحليل.

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to PDF with Custom Properties</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, PdfCustomPropertiesExport } = AsposeCells;

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

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create an instance of PdfSaveOptions
            const pdfSaveOptions = new PdfSaveOptions();

            // Set CustomPropertiesExport property to PdfCustomPropertiesExport.Standard
            pdfSaveOptions.customPropertiesExport = PdfCustomPropertiesExport.Standard;

            // Save the workbook to PDF format while passing the object of PdfSaveOptions
            const outputData = workbook.save(SaveFormat.Pdf, pdfSaveOptions);

            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outSourceWithCustProps.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

### **سمات التحويل**

نحن نعمل على تعزيز ميزات التحويل مع كل إصدار جديد. لا تزال عملية تحويل Excel إلى PDF من Aspose.Cells تحتوي على بعض القيود. لا يتم دعم MapChart عند التحويل إلى تنسيق PDF. أيضًا، بعض الكائنات الرسومية لا تتمتع بدعم جيد.

الجدول التالي يقوم بسرد جميع الميزات المدعومة جزئيًا أو بالكامل عند التصدير إلى PDF باستخدام Aspose.Cells. هذا الجدول ليس نهائيًا ولا يغطي جميع خصائص جدول البيانات ولكنه يحدد تلك الميزات التي لا تتم دعمها أو يتم دعمها جزئيًا للتحويل إلى PDF.

|**عنصر المستند**|**السمة**|**مدعوم**|**ملاحظات**|
| :- | :- | :- | :- |
|المحاذاة| |نعم| |
|إعدادات الخلفية| |نعم| |
|الحدود|لون|نعم| |
|الحدود|نمط الخط|نعم| |
|الحدود|سمك الخط|نعم| |
|بيانات الخلية| |نعم| |
|التعليقات| |نعم| |
|تنسيق شرطي| |نعم| |
|خصائص المستند| |نعم| |
|كائنات الرسم| |جزئيا|لا يتم دعم الظل والتأثيرات ثلاثية الأبعاد لكائنات الرسم بشكل جيد؛ WordArt و SmartArt يتم دعمهما جزئيا.|
|الخط|الحجم|نعم| |
|الخط|اللون|نعم| |
|الخط|النمط|نعم| |
|الخط|التسطير|نعم| |
|الخط|التأثيرات|نعم||
|الصور| |نعم| |
|الارتباط| |نعم| |
|الرسوم البيانية| |جزئيا|لم يتم دعم MapChart.|
|الخلايا المدمجة| |نعم| |
|فاصل الصفحة| |نعم| |
|إعداد الصفحة|الرأس/التذييل|نعم| |
|إعداد الصفحة|الهوامش|نعم| |
|إعداد الصفحة|اتجاه الصفحة|نعم| |
|إعداد الصفحة|حجم الصفحة|نعم| |
|إعداد الصفحة|منطقة الطباعة|نعم| |
|إعداد الصفحة|عناوين الطباعة|نعم| |
|إعداد الصفحة|تحجيم|نعم| |
|ارتفاع الصف/عرض العمود| |نعم| |
|لغة من اليمين إلى اليسار| |نعم| |

{{% alert color="primary" %}}
إذا كانت جداول البيانات الخاصة بك تحتوي على صيغ، من الأفضل استدعاء [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) قبل تحويل جدول البيانات إلى تنسيق PDF. وذلك سيضمن إعادة حساب قيم الصيغ الخاصة وتقديم القيم الصحيحة في الملف الناتج PDF.
{{% /alert %}}

## **مواضيع متقدمة**
- [إضافة علامات مرجعية لملف PDF باستخدام وجهات مسماة](/cells/ar/javascript-cpp/add-pdf-bookmarks-with-named-destinations/)
- [تجنب الصفحة الفارغة في ملف PDF الناتج عندما لا يوجد شيء للطباعة](/cells/ar/javascript-cpp/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [تغيير الخط المستخدم للرموز اليونيكود الخاصة عند حفظ الملف إلى PDF](/cells/ar/javascript-cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/)
- [تحويل ملف XLSX إلى تنسيق PDF](/cells/ar/javascript-cpp/convert-xlsx-file-to-pdf-format/)
- [تحويل ملف Excel إلى تنسيق PDF متوافق مع PDFA-1a](/cells/ar/javascript-cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [تحويل ملف XLS مع صور أو رسوم بيانية إلى تنسيق PDF](/cells/ar/javascript-cpp/convert-xls-file-with-images-or-charts-to-pdf/)
- [إنشاء PdfBookmarkEntry لورقة الرسم البياني](/cells/ar/javascript-cpp/create-pdfbookmarkentry-for-chart-sheet/)
- [تناسب جميع أعمدة ورقة العمل على صفحة PDF واحدة](/cells/ar/javascript-cpp/fit-all-worksheet-columns-on-single-pdf-page/)
- [الحصول على DrawObject والحدود أثناء تقديمها إلى PDF باستخدام فئة DrawObjectEventHandler](/cells/ar/javascript-cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/)
- [الحصول على تحذيرات بديلة للخط أثناء تحويل ملف Excel إلى PDF](/cells/ar/javascript-cpp/get-warnings-for-font-substitution-while-rendering-excel-file/)
- [تجاهل الأخطاء أثناء تحويل Excel إلى PDF](/cells/ar/javascript-cpp/ignore-errors-while-rendering-excel-to-pdf/)
- [تحديد عدد الصفحات التي يتم إنشاؤها – تحويل من Excel إلى PDF](/cells/ar/javascript-cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [طباعة التعليقات عند الحفظ إلى PDF](/cells/ar/javascript-cpp/print-comments-while-saving-to-pdf/)
- [تقديم الإضافات المكتبية أثناء تحويل Excel إلى PDF](/cells/ar/javascript-cpp/render-office-add-ins-while-converting-excel-to-pdf/)
- [تقديم صفحة PDF واحدة لكل ورقة عمل إكسل - تحويل إكسل إلى PDF](/cells/ar/javascript-cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [عرض الحروف اليونيكود الإضافية في ملف PDF الناتج باستخدام Aspose.Cells](/cells/ar/javascript-cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [إعادة عينات الصور المضافة - تحويل إكسل إلى PDF](/cells/ar/javascript-cpp/resampling-added-images-excel-to-pdf-conversion/)
- [حفظ كل ورقة عمل في ملف PDF مختلف](/cells/ar/javascript-cpp/save-each-worksheet-to-a-different-pdf-file/)
- [حفظ إكسل في ملف PDF بحجم قياسي أو حد أدنى](/cells/ar/javascript-cpp/save-excel-into-pdf-with-standard-or-minimum-size/)
- [حفظ ورقات العمل المحددة في ملف PDF](/cells/ar/javascript-cpp/save-specified-worksheets-to-pdf/)
- [مستندات PDF آمنة](/cells/ar/javascript-cpp/secure-pdf-documents/)
- [تحديد كيفية عبور السلسلة في ملف PDF والصورة](/cells/ar/javascript-cpp/specify-how-to-cross-string-in-output-pdf-and-image/)

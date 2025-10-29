---
title: كيفية طباعة إكسل كصفحات مناسبة للعرض واسعة وطويلة باستخدام JavaScript عبر C++
linktitle: كيفية طباعة إكسل كصفحات مناسبة للعرض بشكل واسع ومرتفعة
type: docs
weight: 200
url: /ar/javascript-cpp/how-to-print-excel-as-fitted-pages-wide-and-tall/
description: يعرض هذا المقال رمزًا يشرح كيفية ضبط FitToPagesWide و FitToPagesTall باستخدام Aspose.Cells for JavaScript عبر C++.
keywords: JavaScript عبر C++ كيفية تعيين FitToPagesWide و FitToPagesTall، كيفية إضافة FitToPagesWide و FitToPagesTall في JavaScript، كيفية تعيين FitToPagesWide و FitToPagesTall في إكسل، كيفية مسح FitToPagesWide و FitToPagesTall في إكسل، كيف تطبع إكسل كصفحات مناسبة للعرض واسعة وطويلة، كيفية طباعة ورقة عمل كصفحة واحدة، طباعة جميع أعمدة ورقة العمل في صفحة واحدة.
---

## **مقدمة**

يتم استخدام إعدادات FitToPagesWide و FitToPagesTall في تطبيقات جداول البيانات (مثل مايكروسوفت إكسل) للتحكم في كيفية تكبير الجدول عند الطباعة. تساعد هذه الإعدادات على ضمان أن المخرجات المطبوعة تتوافق مع عدد معين من الصفحات، أفقياً وعمودياً. إليك شرح لكل إعداد:

1. FitToPagesWide: يحدد هذا الإعداد عدد الصفحات عرضه يجب أن تتناسب مع المخرجات المطبوعة. على سبيل المثال، ضبطه إلى 1 يعني أن المحتوى سيتم تكبيره ليتلاءم مع عرض صفحة واحدة بغض النظر عن عرض الجدول.
 2. FitToPagesTall: يحدد هذا الإعداد عدد الصفحات ارتفاعًا الذي يجب أن يتناسب معه الناتج المطبوع. على سبيل المثال، تعيين FitToPagesTall إلى 1 يعني أن المحتوى سيتم تكبيره ليتناسب مع ارتفاع صفحة واحدة، بغض النظر عن عدد الصفوف.

## **لماذا نستخدم FitToPagesWide و FitToPagesTall**
وفيما يلي بعض الأسباب لضبط هذا الإعداد:
1. التحكم في التنسيق المطبوع: من خلال تحديد عدد الصفحات عرضاً وارتفاعاً، يمكنك ضمان أن يكون المستند المطبوع سهل القراءة ومنظم بشكل جيد، دون تقسيم الأعمدة أو الصفوف بشكل غير مناسب عبر الصفحات.
 2. الاتساق: إذا كنت تطبع عدة أوراق أو تقارير، فإن استخدام هذه الإعدادات يساعد على الحفاظ على تنسيق موحد، مما يسهل مقارنة وتحليل المستندات المطبوعة.
 3. عرض تقديمي احترافي: يمكن أن يؤدي تكبير المحتوى وتكييفه بشكل صحيح لعدد معين من الصفحات إلى عرض تقديمي أكثر احترافية واحترافية لبياناتك.

## **كيفية طباعة الملف كصفحات مناسبة عريضة وطويلة في Excel**

لتعيين إعدادات FitToPagesWide و FitToPagesTall في Microsoft Excel، اتبع الخطوات التالية:

1. افتح مصنف Excel الخاص بك وانتقل إلى الورقة التي تريد طباعةها.
 2. انتقل إلى علامة التبويب تخطيط الصفحة على الشريط.
 3. في مجموعة إعداد الصفحة، انقر على السهم الصغير في الزاوية اليمنى السفلى لفتح مربع حوار إعداد الصفحة.
 4. في مربع حوار إعداد الصفحة، انتقل إلى علامة التبويب الصفحة.
 5. تحت مقياس، اختر خيار "تتناسب مع" ثم حدد عدد الصفحات عريضة ومرتفعة التي تريدها: أدخل عدد الصفحات العريضة في المربع الأول (تتناسب مع x صفحات عريضة). أدخل عدد الصفحات المرتفعة في المربع الثاني (تتناسب مع y صفحات عالية).
<br>
<img src="2.png" width=60% />

 6. انقر على موافق لتطبيق الإعدادات.

## **كيفية طباعة إكسل كصفحات مناسبة للعرض واسعة وطويلة باستخدام Aspose.Cells for JavaScript عبر C++**

لتعيين FitToPagesWide و FitToPagesTall في ورقة عمل محددة: أولاً، قم بتحميل [ملف العينة](input.xlsx)، ثم تحتاج إلى تعديل خاصيتي [**PageSetup.fitToPagesTall**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#fitToPagesTall--) و [**PageSetup.fitToPagesWide**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#fitToPagesWide--) من الكائن [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/) للورقة المطلوبة. إليك مثالاً في JavaScript:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set Worksheet Fit To Pages and Save as PDF</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Setting the number of pages to which the length of the worksheet will be spanned
            worksheet.pageSetup.fitToPagesTall = 1;

            // Setting the number of pages to which the width of the worksheet will be spanned
            worksheet.pageSetup.fitToPagesWide = 1;

            // Saving the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_net.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

نتيجة الإخراج:
<br>
<img src="1.png" width=60% />

## **كيفية طباعة ورقة العمل كصفحة واحدة باستخدام Aspose.Cells for JavaScript عبر C++**

لطباعة ورقة عمل كصفحة واحدة: أولاً، قم بتحميل [ملف العينة](sample.xlsx)، ثم تحتاج إلى تعيين الخاصية [**PdfSaveOptions.onePagePerSheet**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#onePagePerSheet--) من الكائن [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/). إليك مثالاً في JavaScript:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>One Page Per Sheet to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, Utils } = AsposeCells;

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

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const options = new PdfSaveOptions();
            options.onePagePerSheet = true;

            // Save the workbook to PDF format and provide download link
            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OnePagePerSheet.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

نتيجة الإخراج:
<br>
<img src="3.png" width=60% />

## **كيفية طباعة جميع أعمدة ورقة العمل على صفحة واحدة باستخدام Aspose.Cells for JavaScript عبر C++**

لطباعة جميع أعمدة ورقة العمل على صفحة واحدة: أولاً، قم بتحميل [ملف العينة](sample.xlsx)، ثم تحتاج إلى تعيين خاصية [**PdfSaveOptions.allColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#allColumnsInOnePagePerSheet--) من كائن [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/). إليك مثال في JavaScript:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>All Columns In One Page Per Sheet Example</h1>
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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create PdfSaveOptions and set allColumnsInOnePagePerSheet property
            const options = new AsposeCells.PdfSaveOptions();
            options.allColumnsInOnePagePerSheet = true;

            // Save the workbook to PDF format with the options
            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData], { type: 'application/pdf' });

            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'AllColumnsInOnePagePerSheet.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

نتيجة الإخراج:
<br>
<img src="4.png" width=60% />

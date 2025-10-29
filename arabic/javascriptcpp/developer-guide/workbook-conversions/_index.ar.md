---
title: تحويل Excel إلى Pdf، صورة وصيغ أخرى
linktitle: تحويل المصنفات
type: docs
weight: 65
url: /ar/javascript-cpp/convert-workbook-to-different-formats/
description: تحويل ملفات إكسل إلى Word، Excel، PowerPoint، PDF، CSV، JPG، HTML، MHT، ODS، BMP، PNG، SVG، TIFF، XPS، JSON، SQL، XML والمزيد باستخدام جافا سكريبت عبر C++.
---

{{% alert color="primary" %}}
Aspose.Cells تدعم تحويل بين العديد من الصيغ. من الناحية التقنية، التحويل يعني تحميل جدول عمل في تنسيق ملف معين وحفظه في تنسيق آخر.
{{% /alert %}}

## **تحويل مصنف Excel إلى PDF**
تستخدم ملفات PDF على نطاق واسع لتبادل المستندات بين المؤسسات والقطاعات الحكومية والأفراد. إنها صيغة مستند قياسية وغالبًا ما يُطلب من مطوري البرامج أن يجدوا طريقة لتحويل ملفات Microsoft Excel إلى مستندات PDF.

تدعم Aspose.Cells تحويل ملفات Excel إلى PDF وتحافظ على دقة الرؤية العالية في التحويل.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Save As PDF Example</title>
    </head>
    <body>
        <h1>Save Excel as PDF Example</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save the document in PDF format
            const outputData = workbook.save(SaveFormat.Pdf);

            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

## **تحويل مصنف Excel إلى JPG**
يدعم Aspose.Cells تحويل ملفات Excel إلى JPG. يوضح مثال الكود أدناه كيفية حفظ مصنف كصورة JPG.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Convert Workbook to JPG Example</title>
    </head>
    <body>
        <h1>Convert Workbook to JPG Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to JPG</button>
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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Convert workbook to JPG image
            const outputData = workbook.save(SaveFormat.Jpeg);
            const blob = new Blob([outputData], { type: 'image/jpeg' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Image1.jpg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download JPG Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed. Click the download link to get the JPG image.</p>';
        });
    </script>
</html>
```

## **تحويل مصنف Excel إلى صورة**
يدعم Aspose.Cells تحويل ملفات Excel إلى صور. يوضح مثال الكود أدناه كيفية حفظ مصنف كصور.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells: Convert Workbook to Images</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to Images</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
        <div id="downloads"></div>
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

            document.getElementById('result').innerHTML = '<p>Converting workbook to images...</p>';
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Define desired image formats
            const formats = [
                { fmt: SaveFormat.Bmp, name: 'Image1.bmp', mime: 'image/bmp' },
                { fmt: SaveFormat.Jpeg, name: 'Image1.jpg', mime: 'image/jpeg' },
                { fmt: SaveFormat.Png, name: 'Image1.png', mime: 'image/png' },
                { fmt: SaveFormat.Emf, name: 'Image1.emf', mime: 'image/emf' },
                { fmt: SaveFormat.Gif, name: 'Image1.gif', mime: 'image/gif' }
            ];

            const downloadsDiv = document.getElementById('downloads');
            downloadsDiv.innerHTML = '';

            // Convert and create download links for each image format
            for (const f of formats) {
                const outputData = workbook.save(f.fmt);
                const blob = new Blob([outputData], { type: f.mime });
                const url = URL.createObjectURL(blob);

                const a = document.createElement('a');
                a.href = url;
                a.download = f.name;
                a.textContent = 'Download ' + f.name;
                a.style.display = 'block';
                downloadsDiv.appendChild(a);
            }

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed. Click the links below to download the images.</p>';
        });
    </script>
</html>
```

## **تحويل دفتر العمل في Excel إلى XPS**
تتكون صيغة مستند XPS من ترميز XML منظم يحدد تخطيط المستند والمظهر البصري لكل صفحة، جنبًا إلى جنب مع قواعد العرض لتوزيع المستندات وأرشفتها وعرضها ومعالجتها وطباعتها.

لغة الوسوم لـ XPS هي جزء من XAML مما يسمح لها بدمج عناصر الرسومات الناقلة في المستندات، باستخدام XAML لتسمية عناصر Windows Presentation Foundation (WPF) البدائية. يتم وصف العناصر المستخدمة من حيث المسارات والبدائيات الهندسية الأخرى.

ملف XPS هو في الواقع أرشيف ZIP يستخدم ترميز Unicode باستخدام الاتفاقات الخاصة بالتغليف المفتوح، يحتوي على الملفات التي تشكل المستند. تشمل هذه ملف ترميز XML لكل صفحة، ونصوص، وخطوط مضمنة، وصور بترا، ورسومات ناقلة 2D، بالإضافة إلى معلومات إدارة الحقوق الرقمية. يمكن فحص محتويات ملف XPS ببساطة عن طريق فتحه في تطبيق يدعم ملفات ZIP.

ابتداءً من Aspose.Cells 6.0.0، يتم دعم تحويل ملفات Microsoft Excel إلى XPS.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Render to XPS</title>
    </head>
    <body>
        <h1>Render Worksheet / Workbook to XPS</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <div>
            <a id="downloadLinkSheet" style="display: none; margin-right: 10px;">Download Sheet XPS</a>
            <a id="downloadLinkWorkbook" style="display: none;">Download Workbook XPS</a>
        </div>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, XpsSaveOptions, SheetSet } = AsposeCells;

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
            const downloadLinkSheet = document.getElementById('downloadLinkSheet');
            const downloadLinkWorkbook = document.getElementById('downloadLinkWorkbook');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            // Read file from input
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Open workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Render the sheet to XPS
            const options = new XpsSaveOptions();
            const sheetSet = new SheetSet([sheet.index]);
            options.sheetSet = sheetSet;
            const outputDataSheet = workbook.save(SaveFormat.Xps, options);
            const blobSheet = new Blob([outputDataSheet], { type: 'application/vnd.ms-xps' });
            downloadLinkSheet.href = URL.createObjectURL(blobSheet);
            downloadLinkSheet.download = 'out_printingxps.out.xps';
            downloadLinkSheet.style.display = 'inline-block';
            downloadLinkSheet.textContent = 'Download Sheet XPS';

            // Export the whole workbook to XPS
            const outputDataWorkbook = workbook.save(SaveFormat.Xps, new XpsSaveOptions());
            const blobWorkbook = new Blob([outputDataWorkbook], { type: 'application/vnd.ms-xps' });
            downloadLinkWorkbook.href = URL.createObjectURL(blobWorkbook);
            downloadLinkWorkbook.download = 'out_whole_printingxps.out.xps';
            downloadLinkWorkbook.style.display = 'inline-block';
            downloadLinkWorkbook.textContent = 'Download Workbook XPS';

            resultDiv.innerHTML = '<p style="color: green;">XPS files generated. Use the links above to download the sheet and workbook XPS files.</p>';
        });
    </script>
</html>
```

## **تحويل Excel إلى Ods و Sxc و Fods (OpenOffice / LibreOffice Calc)**
يدعم Aspose.Cells تحويل ملفات Excel إلى ملفات Ods و Sxc و Fods. يوضح مثال الكود أدناه كيفية تحويل [القالب](book1.xlsx) إلى ملفات Ods و Sxc و Fods.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Save As Multiple Formats Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Save As ODS / SXC / FODS Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert and Download</button>
        <div style="margin-top: 10px;">
            <a id="downloadLinkOds" style="display: none; margin-right: 10px;">Download ODS</a>
            <a id="downloadLinkSxc" style="display: none; margin-right: 10px;">Download SXC</a>
            <a id="downloadLinkFods" style="display: none; margin-right: 10px;">Download FODS</a>
        </div>
        <div id="result" style="margin-top: 10px;"></div>

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
            const result = document.getElementById('result');
            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save as ods file
            const outputOds = workbook.save(SaveFormat.Ods);
            const blobOds = new Blob([outputOds]);
            const downloadLinkOds = document.getElementById('downloadLinkOds');
            downloadLinkOds.href = URL.createObjectURL(blobOds);
            downloadLinkOds.download = 'Out.ods';
            downloadLinkOds.style.display = 'inline-block';
            downloadLinkOds.textContent = 'Download ODS File';

            // Save as sxc file
            const outputSxc = workbook.save(SaveFormat.Sxc);
            const blobSxc = new Blob([outputSxc]);
            const downloadLinkSxc = document.getElementById('downloadLinkSxc');
            downloadLinkSxc.href = URL.createObjectURL(blobSxc);
            downloadLinkSxc.download = 'Out.sxc';
            downloadLinkSxc.style.display = 'inline-block';
            downloadLinkSxc.textContent = 'Download SXC File';

            // Save as fods file
            const outputFods = workbook.save(SaveFormat.Fods);
            const blobFods = new Blob([outputFods]);
            const downloadLinkFods = document.getElementById('downloadLinkFods');
            downloadLinkFods.href = URL.createObjectURL(blobFods);
            downloadLinkFods.download = 'Out.fods';
            downloadLinkFods.style.display = 'inline-block';
            downloadLinkFods.textContent = 'Download FODS File';

            result.innerHTML = '<p style="color: green;">Files converted successfully! Click the download links to get the converted files.</p>';
        });
    </script>
</html>
```

## **تحويل دفتر العمل في إكسل إلى ملفات MHTML**
تجمع MHTML بين HTML العادي مع الموارد الخارجية (أي المحتوى الذي يتم عادةً الربط به، مثل الصور والرسوم المتحركة والصوت وما إلى ذلك) في ملف واحد. يُستخدمون في الرسائل البريدية بامتداد ملف .mht.

Aspose.Cells تدعم قراءة وكتابة ملفات MHTML.

يوضح المثال البرمجي أدناه كيفية حفظ دفتر العمل كملف MHTML.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to MHT Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
            window.asposeCellsReady = true;
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            if (!window.asposeCellsReady) {
                resultDiv.innerHTML = '<p style="color: red;">Aspose.Cells is not initialized yet. Please wait and try again.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a workbook and open the uploaded XLSX file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify the HTML Saving Options
            const sv = new HtmlSaveOptions(SaveFormat.MHtml);

            // Save the MHT file (returns binary data)
            const outputData = workbook.save(SaveFormat.MHtml, sv);

            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = `${file.name}.out.mht`;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download MHT File';

            resultDiv.innerHTML = '<p style="color: green;">MHT file generated successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **تحويل دفتر العمل في إكسل إلى HTML**
يوفر API Aspose.Cells دعمًا للتصدير إلى تنسيق HTML. لهذا الغرض، يستخدم Aspose.Cells فئة [**HtmlSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions) لتوفير المرونة للتحكم في عدة جوانب من مخرجات HTML.

يوضح المثال البرمجي أدناه كيفية حفظ دفتر العمل كملف HTML.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Converting Excel to HTML</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load your sample excel file in a workbook object
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save it in HTML format
            const outputData = workbook.save(SaveFormat.Html);

            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ConvertingToHTMLFiles_out.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            resultDiv.innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```

## **تعيين تفضيلات الصور لتنسيق HTML**
ابتداءً من الإصدار 8.0.2، كشفت Aspose.Cells عن [**imageOptions**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#imageOptions--) لفئة [**HtmlSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions)، مما يسمح للمطورين بتحديد تفضيلات الصور عند حفظ جداول البيانات بصيغة HTML.

أدناه تفاصيل بعض إعدادات الصور التي يمكن تطبيقها،

- [**ImageType**](https://reference.aspose.com/cells/javascript-cpp/imagetype/): يحدد نوع الصورة. يرجى ملاحظة أن جميع الأشكال ، بما في ذلك الرسوم البيانية ، يتحولون إلى صور في تنسيق HTML الناتج.
- [**quality**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#quality--): يحدد جودة الصورة بين 0 و 100، عندما يتم تحديد [**ImageType**](https://reference.aspose.com/cells/javascript-cpp/imagetype/) كـ Jpeg.
- [**verticalResolution**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#verticalResolution--): يحصل أو يحدد الدقة الرأسية للصورة بدقة بالنقاط في البوصة.
- [**horizontalResolution**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#horizontalResolution--): يحصل أو يحدد الدقة الأفقية للصورة بدقة بالنقاط في البوصة.
- [**TiffCompression**](https://reference.aspose.com/cells/javascript-cpp/tiffcompression/): يحصل أو يضبط نوع الضغط للصور عند تحديد [**ImageType**](https://reference.aspose.com/cells/javascript-cpp/imagetype/) كـ Tiff.
- [**transparent**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#transparent--): يشير إذا كان خلفية الصورة يجب أن تكون شفافة عندما يتم تحديد ImageFormat على أنها PNG.

## **تحويل دفتر العمل إكسل إلى Markdown**
توفر واجهة برمجة تطبيقات Aspose.Cells دعمًا لتصدير جداول البيانات إلى صيغة Markdown. لتصدير ورقة العمل النشطة إلى Markdown، مرر [**SaveFormat.Markdown**](https://reference.aspose.com/cells/javascript-cpp/saveformat) كوسيط ثاني لطريقة [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveoptions-). يمكنك أيضًا استخدام فئة [**MarkdownSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/markdownsaveoptions) لتحديد إعدادات إضافية لتصدير ورقة العمل إلى Markdown.

يُوضح مثال الكود التالي تصدير ورقة العمل النشطة إلى Markdown باستخدام عضو تعداد [**SaveFormat.Markdown**](https://reference.aspose.com/cells/javascript-cpp/saveformat). يرجى مراجعة [ملف Markdown الناتج](md_sample.txt) الذي تم إنشاؤه بواسطة الكود للمرجعية.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Save as Markdown</title>
    </head>
    <body>
        <h1>Save Excel as Markdown Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to Markdown</button>
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

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Saving as Markdown
            const outputData = workbook.save(SaveFormat.Markdown);
            const blob = new Blob([outputData], { type: 'text/markdown' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book1.md';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Markdown File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the Markdown file.</p>';
        });
    </script>
</html>
```

## **تحويل دفتر العمل Excel إلى JSON**
يدعم Aspose.Cells تحويل مصنف إلى ملف Json (ترميز كائن JavaScript).

يُوضح مثال الكود التالي تصدير ورقة العمل النشطة إلى Json باستخدام عضو تعداد [**SaveFormat.Json**](https://reference.aspose.com/cells/javascript-cpp/saveformat). يرجى مراجعة الكود لتحويل [ملف المصدر](Book1.xlsx) إلى [ملف Json الناتج](Book1.Json) الذي تم إنشاؤه بواسطة الكود للمرجعية.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Convert Workbook to JSON</title>
    </head>
    <body>
        <h1>Convert Workbook to JSON</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to JSON</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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

            // Convert the workbook to JSON format
            const outputData = workbook.save(SaveFormat.Json);

            // Create a downloadable blob for the JSON result
            const blob = new Blob([outputData], { type: 'application/json' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.json';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download JSON File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook converted to JSON successfully! Click the download link to get the JSON file.</p>';
        });
    </script>
</html>
```

## **تحويل دفتر العمل إكسل إلى XML**
Aspose.Cells تدعم تحويل جدول العمل إلى ملف Excel 2003 Spreadsheet XML وبيانات XML نقية.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Workbook to XML Examples</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <br/><br/>
        <a id="downloadLink1" style="display: none; margin-right: 10px;">Download Spreadsheet XML</a>
        <a id="downloadLink2" style="display: none;">Download Data XML</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, XmlSaveOptions } = AsposeCells;

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

            // Save as Excel 2003 Spreadsheet XML
            const spreadsheetData = workbook.save(SaveFormat.Excel2003Xml);
            const blob1 = new Blob([spreadsheetData]);
            const downloadLink1 = document.getElementById('downloadLink1');
            downloadLink1.href = URL.createObjectURL(blob1);
            downloadLink1.download = 'Spreadsheet.xml';
            downloadLink1.style.display = 'inline-block';
            downloadLink1.textContent = 'Download Spreadsheet XML';

            // Save as plain XML data with XmlSaveOptions
            const xmlSaveOptions = new XmlSaveOptions();
            const dataXml = workbook.save(SaveFormat.SpreadsheetML, xmlSaveOptions);
            const blob2 = new Blob([dataXml]);
            const downloadLink2 = document.getElementById('downloadLink2');
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'data.xml';
            downloadLink2.style.display = 'inline-block';
            downloadLink2.textContent = 'Download Data XML';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Use the links above to download the generated XML files.</p>';
        });
    </script>
</html>
```

## **تحويل دفتر العمل إكسل إلى TIFF**
Aspose.Cells تدعم تحويل جدول العمل إلى ملف TIFF.

الكود المصغر أدناه يوضّح كيفية تحويل إكسل إلى TIFF:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to TIFF</h1>
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

            // Instantiating a Workbook object by opening the Excel file from the file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save workbook to TIFF format
            const outputData = workbook.save(SaveFormat.Tiff);
            const blob = new Blob([outputData], { type: 'image/tiff' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.tiff';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download TIFF File';

            resultDiv.innerHTML = '<p style="color: green;">File converted to TIFF successfully! Click the download link to get the TIFF file.</p>';
        });
    </script>
</html>
```

## **تحويل دفتر العمل إكسل إلى DOCX**
توفر واجهة برمجة تطبيقات Aspose.Cells دعمًا لتحويل جداول البيانات إلى صيغة DOCX. لتصدير المصنف إلى DOCX، مرر [**SaveFormat.Docx**](https://reference.aspose.com/cells/javascript-cpp/saveformat) كوسيط ثاني لطريقة [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveoptions-). يمكنك أيضًا استخدام فئة [**DocxSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/docxsaveoptions) لتحديد إعدادات إضافية لتصدير ورقة العمل إلى DOCX.

يُوضح مثال الكود التالي تصدير ورقة العمل النشطة إلى DOCX باستخدام عضو تعداد [**SaveFormat.Docx**](https://reference.aspose.com/cells/javascript-cpp/saveformat). يرجى مراجعة [ملف DOCX الناتج](Book1.docx) الذي تم إنشاؤه بواسطة الكود للمرجعية.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save as DOCX (Markdown/Docx conversion per original code)
            const outputData = workbook.save(SaveFormat.Docx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book1.docx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Docx File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File converted successfully! Click the download link to get the DOCX file.</p>';
        });
    </script>
</html>
```

## **تحويل دفتر العمل إكسل إلى PPTX**
توفر واجهة برمجة تطبيقات Aspose.Cells دعمًا لتحويل جداول البيانات إلى صيغة PPTX. لتصدير المصنف إلى PPTX، مرر [**SaveFormat.Pptx**](https://reference.aspose.com/cells/javascript-cpp/saveformat) كوسيط ثاني لطريقة [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveoptions-). يمكنك أيضًا استخدام فئة [**PptxSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pptxsaveoptions) لتحديد إعدادات إضافية لتصدير ورقة العمل إلى PPTX.

يُوضح مثال الكود التالي تصدير ورقة العمل النشطة إلى PPTX باستخدام عضو تعداد [**SaveFormat.Pptx**](https://reference.aspose.com/cells/javascript-cpp/saveformat). يرجى مراجعة [ملف PPTX الناتج](Book1.pptx) الذي تم إنشاؤه بواسطة الكود للمرجعية.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Save as PPTX Example</title>
    </head>
    <body>
        <h1>Save Excel as PPTX Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PPTX</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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

            // Save as PPTX
            const outputData = workbook.save(SaveFormat.Pptx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            const baseName = file.name.replace(/\.[^/.]+$/, "");
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = baseName + '.pptx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Converted PPTX File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File converted successfully! Click the download link to get the PPTX file.</p>';
        });
    </script>
</html>
```

## **تحويل ملف عمل Excel إلى EPUB**
توفر واجهة برمجة تطبيقات Aspose.Cells دعمًا لتحويل جداول البيانات إلى صيغة EPUB. لتصدير المصنف إلى EPUB، مرر [**SaveFormat.Epub**](https://reference.aspose.com/cells/javascript-cpp/saveformat) كوسيط ثاني لطريقة [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveoptions-). يمكنك أيضًا استخدام فئة [**EBookSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/ebooksaveoptions) لتحديد إعدادات إضافية لتصدير ورقة العمل إلى Epub.

يُوضح مثال الكود التالي تصدير ورقة العمل النشطة إلى EPUB باستخدام عضو تعداد [**SaveFormat.Epub**](https://reference.aspose.com/cells/javascript-cpp/saveformat).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Converting To EPUB Files</title>
    </head>
    <body>
        <h1>Converting To EPUB Files</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to EPUB</button>
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
            const result = document.getElementById('result');

            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load your sample excel file in a workbook object
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save it in EPUB format
            const outputData = workbook.save(SaveFormat.Epub);

            const blob = new Blob([outputData], { type: 'application/epub+zip' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ConvertingToEPUBFiles_out.epub';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download EPUB File';

            result.innerHTML = '<p style="color: green;">File converted to EPUB successfully! Click the download link to get the EPUB file.</p>';
        });
    </script>
</html>
```

## **تحويل ملف عمل Excel إلى AZW3**
توفر واجهة برمجة تطبيقات Aspose.Cells دعمًا لتحويل جداول البيانات إلى صيغة AZW3. لتصدير المصنف إلى AZW3، مرر [**SaveFormat.Azw3**](https://reference.aspose.com/cells/javascript-cpp/saveformat) كوسيط ثاني لطريقة [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveoptions-). يمكنك أيضًا استخدام فئة [**EBookSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/ebooksaveoptions) لتحديد إعدادات إضافية لتصدير ورقة العمل إلى AZW3.

يُوضح مثال الكود التالي تصدير ورقة العمل النشطة إلى AZW3 باستخدام عضو تعداد [**SaveFormat.Azw3**](https://reference.aspose.com/cells/javascript-cpp/saveformat).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Convert to AZW3 Example</title>
    </head>
    <body>
        <h1>Convert Excel to AZW3 (EPUB) Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Convert to AZW3</button>
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

            // Load your sample excel file in a workbook object
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Save it in AZW3 format
            const outputData = wb.save(SaveFormat.Azw3);
            const blob = new Blob([outputData]);

            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ConvertingToEPUBFiles_out.azw3';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download AZW3 File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the AZW3 file.</p>';
        });
    </script>
</html>
```

## **مواضيع متقدمة**
- [تحويل مراجعة XLSB إلى XLSM](/cells/ar/javascript-cpp/convert-revision-of-xlsb-to-xlsm/)
- [HTML](/cells/ar/javascript-cpp/convert-excel-to-html/)
- [صورة](/cells/ar/javascript-cpp/convert-excel-to-image/)
- [Json](/cells/ar/javascript-cpp/convert-workbook-to-json/)
- [تحويل مصنف Excel إلى Ods و Sxc و Fods (OpenOffice / LibreOffice calc).](/cells/ar/javascript-cpp/convert-excel-to-ods/)
- [Pdf](/cells/ar/javascript-cpp/convert-excel-workbook-to-pdf/)
- [تحويل Excel إلى CSV و TSV و Txt](/cells/ar/javascript-cpp/convert-excel-to-csv-tsv-and-txt/)
- [تتبع تقدم تحويل الوثائق](/cells/ar/javascript-cpp/track-document-conversion-progress/)
- [تحويل CSV، TSV و TXT إلى Excel](/cells/ar/javascript-cpp/convert-csv-tsv-and-txt-to-excel/)

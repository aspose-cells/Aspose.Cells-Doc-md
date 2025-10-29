---
title: طرق مختلفة لحفظ الملفات باستخدام JavaScript عبر C++
linktitle: حفظ الملفات
type: docs
weight: 40
url: /ar/javascript-cpp/different-ways-to-save-files/
description: يمكن لـ Aspose.Cells for JavaScript عبر C++ حفظ الملفات بصيغ مختلفة بما في ذلك PDF، HTML، DOCX، PPTX، JSON، و MHTML.
keywords: Aspose.Cells يحفظ إكسل إلى PDF، HTML، JSON، CSV، TXT، XML، DOCX، PPTX، MHT، MHTML وغيرها باستخدام JavaScript عبر C++.
---

{{% alert color="primary" %}}

‏تجعل Aspose.Cells من الممكن إنشاء الملفات وحفظها. يشرح هذا المقال الطرق المختلفة التي يمكن بها حفظ الملفات.

{{% /alert %}}

## **طرق مختلفة لحفظ الملفات**

توفر Aspose.Cells [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) الذي يمثل ملف Microsoft Excel ويقدم الخصائص والطرق اللازمة للعمل مع ملفات Excel. توفر فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) الطريقة [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-) المستخدمة لحفظ ملفات Excel. تحتوي الطريقة [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-) على العديد من التحميلات المفرطة التي تُستخدم لحفظ الملفات بطرق مختلفة.

يتم تحديد تنسيق الملف الذي يتم حفظ الملف به بواسطة التعداد [**SaveFormat**](https://reference.aspose.com/cells/javascript-cpp/saveformat)

|**أنواع تنسيق الملفات**|**الوصف**|
| :- | :- |
|CSV|يمثل ملف CSV|
|Excel97To2003| يمثل ملف Excel 97-2003|
||Xlsx| يمثل ملف Excel 2007 XLSX|
||Xlsm| يمثل ملف Excel 2007 XLSM|
||Xltx| يمثل قالب Excel 2007 XLTX|
||Xltm| يمثل ملف Excel 2007 الممكن للتشغيل الآلي XLTM|
|Xlsb| يمثل ملف XLSB بتنسيق Excel 2007 الثنائي
|SpreadsheetML| يمثل ملف XML لجدول بيانات
|TSV|يمثل ملف قيم مفصولة بعلامة التبويب|
|TabDelimited|يمثل ملف نصي بقيم مفصولة بواسطة علامة التبويب|
|ODS|يمثل ملف ODS|
|Html| يمثل ملف HTML
|MHtml| يمثل ملف MHTML
|Pdf| يمثل ملف PDF
|XPS| يمثل مستند XPS
|TIFF| يمثل ملف TIFF

## **كيفية حفظ الملف بتنسيقات مختلفة**

لحفظ الملفات في موقع تخزين، حدد اسم الملف (بالشامل مع مسار التخزين) والتنسيق المطلوب للملف (من تعداد [**SaveFormat**](https://reference.aspose.com/cells/javascript-cpp/saveformat)) عند استدعاء طريقة [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-) في كائن [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook).

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Aspose.Cells Save Formats Example</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            #downloadLinks a { display: block; margin: 6px 0; }
        </style>
    </head>
    <body>
        <h1>Aspose.Cells Save Formats Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsb,.ods" />
        <button id="runExample">Save in Multiple Formats</button>
        <div id="result"></div>
        <div id="downloadLinks"></div>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, XlsSaveOptions } = AsposeCells;

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
            const downloadLinks = document.getElementById('downloadLinks');
            downloadLinks.innerHTML = '';
            result.innerHTML = '';

            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load your source workbook
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Prepare format list to save
            const formats = [
                { format: SaveFormat.Excel97To2003, name: 'output.xls', options: new XlsSaveOptions() },
                { format: SaveFormat.Xlsx, name: 'output.xlsx' },
                { format: SaveFormat.Xlsb, name: 'output.xlsb' },
                { format: SaveFormat.Ods, name: 'output.ods' },
                { format: SaveFormat.Pdf, name: 'output.pdf' },
                { format: SaveFormat.Html, name: 'output.html' },
                { format: SaveFormat.SpreadsheetML, name: 'output.xml' }
            ];

            // Save in each format and create download link
            for (let i = 0; i < formats.length; i++) {
                const f = formats[i];
                let outputData;
                if (f.options) {
                    outputData = workbook.save(f.format, f.options);
                } else {
                    outputData = workbook.save(f.format);
                }
                const blob = new Blob([outputData]);
                const link = document.createElement('a');
                link.href = URL.createObjectURL(blob);
                link.download = f.name;
                link.textContent = 'Download ' + f.name;
                downloadLinks.appendChild(link);
            }

            result.innerHTML = '<p style="color: green;">Files saved in memory. Click the download links below to download each format.</p>';
        });
    </script>
</html>
```

## **كيفية حفظ الكتاب الدراسي إلى صيغة PDF**
صيغة المستندات المحمولة (PDF) هي نوع من المستندات التي أنشأتها Adobe في التسعينيات. كان الهدف من هذا التنسيق تقديم معيار لعرض المستندات والمواد المرجعية الأخرى بشكل مستقل عن تطبيقات البرمجيات والأجهزة، بالإضافة إلى نظام التشغيل. يمتلك تنسيق ملف PDF القدرة الكاملة على احتواء معلومات مثل النصوص والصور والروابط التشعبية وحقول النموذج media الغني والتوقيعات الرقمية والمرفقات والبيانات الوصفية والخصائص الجغرافية والميزات ثلاثية الأبعاد الموجودة فيه والتي يمكن أن تصبح جزءًا من المستند المصدر.

يوضح الكود التالي كيفية حفظ دفتر العمل كملف PDF باستخدام Aspose.Cells:
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Save to PDF and PDF/A-1a</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <div>
            <a id="downloadLink1" style="display: none; margin-right: 10px;"></a>
            <a id="downloadLink2" style="display: none;"></a>
        </div>
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet and set value to A1
            const worksheet = workbook.worksheets.get(0);
            const cell = worksheet.cells.get("A1");
            cell.value = "Hello World!";

            // Save as PDF (first file)
            const outputData1 = workbook.save(SaveFormat.Pdf);
            const blob1 = new Blob([outputData1], { type: 'application/pdf' });
            const downloadLink1 = document.getElementById('downloadLink1');
            downloadLink1.href = URL.createObjectURL(blob1);
            downloadLink1.download = 'pdf1.pdf';
            downloadLink1.style.display = 'inline';
            downloadLink1.textContent = 'Download pdf1.pdf';

            // Save as PDF with PDF/A-1a compliance
            const saveOptions = new PdfSaveOptions();
            saveOptions.compliance = PdfCompliance.PdfA1a;

            const outputData2 = workbook.save(SaveFormat.Pdf, saveOptions);
            const blob2 = new Blob([outputData2], { type: 'application/pdf' });
            const downloadLink2 = document.getElementById('downloadLink2');
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'pdfa1a.pdf';
            downloadLink2.style.display = 'inline';
            downloadLink2.textContent = 'Download pdfa1a.pdf';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF files generated successfully. Use the download links above.</p>';
        });
    </script>
</html>
```

## **كيفية حفظ الكتاب الدراسي إلى تنسيق نصي أو CSV**

في بعض الأحيان ، تريد تحويل أو حفظ دفتر عمل بعدة ورقات عمل إلى تنسيق نصي. بالنسبة لتنسيقات النص (مثل TXT، TabDelim، CSV، إلخ) ، يحفظ كل من Microsoft Excel وAspose.Cells افتراضيًا محتويات الورقة العمل النشطة فقط.

يشرح المثال التالي كيفية حفظ دفتر عمل كامل بصيغة نصية. قم بتحميل دفتر العمل المصدر الذي يمكن أن يكون أي ملف جدول بيانات من Microsoft Excel أو OpenOffice (مثل XLS و XLSX و XLSM و XLSB و ODS وغيرها) مع أي عدد من أوراق العمل.

عند تنفيذ الكود ، يتم تحويل بيانات كافة الأوراق في دفتر العمل إلى تنسيق TXT.

يمكنك تعديل نفس المثال لحفظ ملفك بصيغة CSV. بشكل افتراضي، [**TxtSaveOptions.separator**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#separator--) هو فاصلة، لذا لا تحدد فاصلًا إذا كنت تحفظ بصيغة CSV. يرجى ملاحظة: إذا كنت تستخدم النسخة التقييمية وحتى إذا تم تعيين خاصية [**TxtSaveOptions.exportAllSheets**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#exportAllSheets--) إلى true، فإن البرنامج سيسمح فقط بتصدير ورقة عمل واحدة.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Export Workbook to Txt</title>
    </head>
    <body>
        <h1>Export Workbook to Txt Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Export to TXT</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TxtSaveOptions } = AsposeCells;

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

            // Load your source workbook
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Text save options. You can use any type of separator
            const opts = new TxtSaveOptions();
            opts.separator = '\t';
            opts.exportAllSheets = true;

            // Save entire workbook data into file (Tab delimited)
            const outputData = workbook.save(SaveFormat.TabDelimited, opts);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.txt';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Text File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook exported to TXT successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **كيفية حفظ ملف إلى ملفات نصية مع فاصل مخصص**

تحتوي ملفات النص على بيانات جداول بيانات دون تنسيق. الملف هو نوع ملف نصي عادي يمكن أن يحتوي على بعض الفواصل المخصصة بين بياناته.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to CSV (with custom separator)</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, TxtSaveOptions } = AsposeCells;

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

            // Create a Workbook object and open the file from the uploaded data
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Instantiate Text File's Save Options
            const options = new TxtSaveOptions();

            // Specify the separator
            options.separator = ";";

            // Save the file with the options (returns file data)
            const outputData = wb.save(options);

            const blob = new Blob([outputData], { type: 'text/csv' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.csv';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download CSV File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File converted successfully! Click the download link to get the CSV file.</p>';
        });
    </script>
</html>
```

## **كيفية حفظ ملف إلى تيار**

لحفظ الملفات إلى تيار، أنشئ كائن *MemoryStream* أو *FileStream* واحفظ الملف إلى ذلك التيار باستخدام استدعاء طريقة [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-) من الكائن [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook). حدد تنسيق الملف المطلوب باستخدام تعداد [**SaveFormat**](https://reference.aspose.com/cells/javascript-cpp/saveformat) عند استدعاء طريقة [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-).

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

            // Load the workbook from the selected file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save the workbook to a binary (xlsx) and provide it as a download
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **كيفية حفظ ملف إكسل إلى ملفات Html و Mht**
يمكن لـ Aspose.Cells حفظ ملف Excel ببساطة كملف HTML و MHTML و JSON و CSV والملفات الأخرى التي يمكن تحميلها بواسطة Aspose.Cells كمصادر ملفات .html و .mht.
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells MHTML Save Example</title>
    </head>
    <body>
        <h1>Save Workbook to MHTML Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Saving the workbook to MHTML format
            const outputData = workbook.save(SaveFormat.MHtml);
            const blob = new Blob([outputData], { type: 'application/octet-stream' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.mht';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download MHTML File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook saved to MHTML format successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```


## **كيفية حفظ ملف إكسل إلى OpenOffice (ODS, SXC, FODS, OTS)**
يمكننا حفظ الملفات بصيغة OpenOffice: ODS و SXC و FODS و OTS وغيرها.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Convert to ODS/SXC/FODS</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert and Save</button>
        <div>
            <a id="downloadOds" style="display: none; margin-right: 10px;">Download ODS File</a>
            <a id="downloadSxc" style="display: none; margin-right: 10px;">Download SXC File</a>
            <a id="downloadFods" style="display: none;">Download FODS File</a>
        </div>
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

            // Save as ODS
            const odsData = workbook.save(SaveFormat.Ods);
            const odsBlob = new Blob([odsData]);
            const downloadOds = document.getElementById('downloadOds');
            downloadOds.href = URL.createObjectURL(odsBlob);
            downloadOds.download = 'Out.ods';
            downloadOds.style.display = 'inline-block';
            downloadOds.textContent = 'Download ODS File';

            // Save as SXC
            const sxcData = workbook.save(SaveFormat.Sxc);
            const sxcBlob = new Blob([sxcData]);
            const downloadSxc = document.getElementById('downloadSxc');
            downloadSxc.href = URL.createObjectURL(sxcBlob);
            downloadSxc.download = 'Out.sxc';
            downloadSxc.style.display = 'inline-block';
            downloadSxc.textContent = 'Download SXC File';

            // Save as FODS
            const fodsData = workbook.save(SaveFormat.Fods);
            const fodsBlob = new Blob([fodsData]);
            const downloadFods = document.getElementById('downloadFods');
            downloadFods.href = URL.createObjectURL(fodsBlob);
            downloadFods.download = 'Out.fods';
            downloadFods.style.display = 'inline-block';
            downloadFods.textContent = 'Download FODS File';

            resultDiv.innerHTML = '<p style="color: green;">Files ready. Click the download links to save the converted files.</p>';
        });
    </script>
</html>
```

## **كيفية حفظ ملف إكسل إلى JSON أو XML**

JSON (JavaScript Object Notation) هو تنسيق ملف مفتوح المعايير لمشاركة البيانات التي تستخدم النص القابل للقراءة من قبل الإنسان لتخزين ونقل البيانات. يتم تخزين ملفات JSON باستخدام الامتداد .json. يتطلب JSON تنسيقًا أقل وهو بديل جيد لـ XML. يتم استخلاص JSON من JavaScript ولكنه تنسيق بيانات مستقل عن اللغة. تدعم العديد من لغات البرمجة الحديثة مولد وتجزئة JSON. application/json هو نوع الوسائط المستخدم لـ JSON.

تدعم Aspose.Cells حفظ الملفات في JSON أو XML.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells JSON Export Example</title>
    </head>
    <body>
        <h1>Convert Excel to JSON</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to JSON</button>
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

            // Save workbook as JSON
            const outputData = workbook.save(SaveFormat.Json);
            const blob = new Blob([outputData], { type: 'application/json' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.json';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download JSON File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the JSON file.</p>';
        });
    </script>
</html>
```


## **مواضيع متقدمة**
- [ضبط مستوى ضغط الورقة العمل](/cells/ar/javascript-cpp/adjust-workbook-compression-level/)
- [حفظ الدفتر إلى تنسيق جدول بيانات إكس الإكس إم الصارم](/cells/ar/javascript-cpp/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [حفظ الملف في كائن الاستجابة](/cells/ar/javascript-cpp/saving-file-to-response-object/)

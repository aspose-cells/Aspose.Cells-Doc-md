---
title: فتح ملفات إصدارات مختلفة من Microsoft Excel باستخدام JavaScript عبر C++
linktitle: فتح ملفات إكسل من إصدارات مايكروسوفت المختلفة
type: docs
weight: 20
url: /ar/javascript-cpp/opening-different-microsoft-excel-versions-files/
description: يشرح هذا المقال كيفية فتح ملفات إصدار مختلفة من Excel باستخدام Aspose.Cells for JavaScript عبر C++.
keywords: JavaScript فتح ملفات Microsoft Excel المختلفة عبر C++، كيف أفتح ملفات Excel المشفرة باستخدام JavaScript عبر C++
---

{{% alert color="primary" %}}

يمكن لـ Aspose.Cells فتح مجموعة متنوعة من ملفات إكسل المختلفة ، مثل إكسل 95/97 - 2003 ، SpreadsheetML ، فتح ملفات إكسل 2007/2010/2013/2016/2019 و Office 365 XLSX أو ملفات إكسل المشفرة.

{{% /alert %}}

## **كيفية فتح ملفات من إصدارات مايكروسوفت إكسل المختلفة**

غالبًا، يتوجب على التطبيق أن يكون قادرًا على فتح ملفات إكسل التي تم إنشاؤها بواسطة إصدارات مختلفة، على سبيل المثال، Microsoft Excel 95، 97، أو Microsoft Excel 2007/2010/2013/2016/2019 وOffice 365. قد تحتاج إلى تحميل ملف بصيغة من بين عدة تنسيقات، بما في ذلك XLS، XLSX، XLSM، XLSB، SpreadsheetML، TabDelimited أو TSV، CSV، ODS وغيرها. استخدم المنشئ، أو حدد سمة نوع [**fileFormat**](https://reference.aspose.com/cells/javascript-cpp/workbook/#fileFormat--) للفئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) التي تحدد الشكل باستخدام تعداد [**FileFormatType**](https://reference.aspose.com/cells/javascript-cpp/fileformattype).

تحتوي تعداد [**FileFormatType**](https://reference.aspose.com/cells/javascript-cpp/fileformattype) على العديد من صيغ الملفات المعرفة مسبقًا، وأحدها مذكور أدناه.

|**أنواع تنسيق الملفات**|**الوصف**|
| :- | :- |
|Csv| يمثل ملف CSV|
|Excel97To2003| يمثل ملف Excel 97-2003|
|Xlsx| يمثل ملف Excel 2007/2010/2013/2016/2019 و Office 365 XLSX|
|Xlsm| يمثل ملف Excel 2007/2010/2013/2016/2019 و Office 365 XLSM|
|Xltx|يمثل ملف XLTX قالب Excel 2007/2010/2013/2016/2019 و Office 365|
|Xltm|يمثل ملف XLTM Excel 2007/2010/2013/2016/2019 و Office 365 القادر على تشغيل الماكرو|
|Xlsb|يمثل ملف XLSB بتنسيق Excel 2007/2010/2013/2016/2019 و Office 365|
|SpreadsheetML|يمثل ملف SpreadsheetML|
|Tsv|يمثل ملف بقيم مفصولة بواسطة علامة التبويب|
|TabDelimited|يمثل ملف نصي بقيم مفصولة بواسطة علامة التبويب|
|Ods|يمثل ملف ODS|
|Html|يمثل ملف HTML|
|Mhtml|يمثل ملف MHTML|

### **فتح ملفات Microsoft Excel 95/5.0**

لفتح ملف Microsoft Excel 95/5.0، استخدم [**LoadOptions**](https://reference.aspose.com/cells/javascript-cpp/loadoptions) واضبط السمة ذات الصلة لفئة [**LoadOptions**](https://reference.aspose.com/cells/javascript-cpp/loadoptions) لملف النموذج ليتم تحميله. يمكنك تنزيل ملف اختبار هذه الميزة من الرابط التالي:

[ملف Excel95](Excel95.xls)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Open Excel95_5.0.xls Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Open Workbook</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Instantiate LoadOptions specified by the LoadFormat.
            const loadOptions1 = new LoadOptions(LoadFormat.Auto);

            // Create a Workbook object and opening the file from the stream
            const wbExcel95 = new Workbook(new Uint8Array(arrayBuffer), loadOptions1);
            console.log("Microsoft Excel 95/5.0 workbook opened successfully!");

            document.getElementById('result').innerHTML = '<p style="color: green;">Microsoft Excel 95/5.0 workbook opened successfully!</p>';
        });
    </script>
</html>
```

### **فتح ملفات Microsoft Excel 97 - 2003**

لفتح ملف Microsoft Excel 97 - 2003، استخدم [**LoadOptions**](https://reference.aspose.com/cells/javascript-cpp/loadoptions) واضبط السمة ذات الصلة لفئة [**LoadOptions**](https://reference.aspose.com/cells/javascript-cpp/loadoptions) لملف النموذج ليتم تحميله.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Open Excel 97-2003 Workbook Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, LoadFormat, SaveFormat, Utils } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel 97-2003 (.xls) file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            const loadOptions1 = new LoadOptions(LoadFormat.Excel97To2003);
            const wbExcel97 = new Workbook(new Uint8Array(arrayBuffer), loadOptions1);

            document.getElementById('result').innerHTML = '<p style="color: green;">Microsoft Excel 97 - 2003 workbook opened successfully!</p>';

            const outputData = wbExcel97.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: 'application/vnd.ms-excel' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';
        });
    </script>
</html>
```

### **فتح ملفات Microsoft Excel 2007/2010/2013/2016/2019 و Office 365 بصيغة XLSX**

لفتح صيغة Microsoft Excel 2007/2010/2013/2016/2019 و Office 365، وهي XLSX أو XLSB، حدد مسار الملف. يمكنك أيضًا استخدام [**LoadOptions**](https://reference.aspose.com/cells/javascript-cpp/loadoptions) وضبط السمة/الخيار ذات الصلة لفئة [**LoadOptions**](https://reference.aspose.com/cells/javascript-cpp/loadoptions) لملف النموذج ليتم تحميله.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Open Excel 2007 Xlsx Example</title>
    </head>
    <body>
        <h1>Open Excel 2007 Xlsx Example</h1>
        <input type="file" id="fileInput" accept=".xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, LoadFormat, SaveFormat, Utils } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel .xlsx file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate LoadOptions specified by the LoadFormat.
            const loadOptions = new LoadOptions(LoadFormat.Xlsx);

            // Create a Workbook object and open the file from the uploaded data
            const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            document.getElementById('result').innerHTML = '<p style="color: green;">Microsoft Excel 2007 - Office365 workbook opened successfully!</p>';

            // Save the workbook back to a downloadable file (unchanged content)
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book_Excel2007_output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Opened Workbook';
        });
    </script>
</html>
```

### **فتح ملفات Excel المشفرة**

من الممكن إنشاء ملفات Excel مشفرة باستخدام Microsoft Excel. لفتح ملف مشفر، استخدم [**LoadOptions**](https://reference.aspose.com/cells/javascript-cpp/loadoptions) وضبط سماته وخياراته (على سبيل المثال، إعطاء كلمة مرور) لملف النموذج ليتم تحميله.
يمكن تنزيل ملف نموذجي لاختبار هذه الميزة من الرابط التالي:

[Encrypted Excel](EncryptedExcel.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Open Encrypted Workbook Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Open Encrypted Workbook</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, Utils } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an encrypted Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate LoadOptions
            const loadOptions = new LoadOptions();

            // Specify the password (converted from setPassword to property assignment)
            loadOptions.password = "1234";

            // Create a Workbook object opening the file from the uploaded bytes with loadOptions
            const wbEncrypted = new Workbook(new Uint8Array(arrayBuffer), loadOptions);
            console.log("Encrypted excel file opened successfully!");

            // Save the workbook so user can download it (using Excel97To2003 format for .xls)
            const outputData = wbEncrypted.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            // Use original name with a prefix to indicate it's been opened
            const originalName = file.name || 'output.xls';
            downloadLink.download = 'opened_' + originalName;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Opened Workbook';

            document.getElementById('result').innerHTML = '<p style="color: green;">Encrypted Excel file opened successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

تدعم Aspose.Cells أيضًا فتح ملفات Microsoft Excel 2007، 2010، 2013، 2016، 2019، Office 365 المحمية بكلمة مرور.

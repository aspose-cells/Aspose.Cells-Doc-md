---
title: تحويل Excel إلى CSV و TSV و Txt مع JavaScript عبر C++
linktitle: حفظ كـ CSV و TSV و Txt
type: docs
weight: 40
url: /ar/javascript-cpp/convert-excel-to-csv-tsv-and-txt/
description: تعلم كيفية تحويل ملفات Excel إلى صيغ CSV، TSV و TXT باستخدام Script Aspose.Cells for Java عبر C++.
---

{{% alert color="primary" %}}

يجعل Aspose.Cells من الممكن تحويل ملفات Excel و ODS و JSON والتنسيقات الأخرى إلى CSV و TSV و TXT.

{{% /alert %}}

## **حفظ دفتر العمل إلى تنسيق نصي أو CSV**

في بعض الأحيان، تريد تحويل أو حفظ دفتر عمل يتضمن أوراق عمل متعددة إلى صيغة نصية. بالنسبة للتنسيقات النصية (على سبيل المثال TXT، TabDelim، CSV، إلخ)، يقوم كل من Microsoft Excel و Aspose.Cells بشكل افتراضي بحفظ محتوى ورقة العمل النشطة فقط.

يوضح المثال التالي كيف تحفظ مصنفًا بالكامل بصيغة نصية. قم بتحميل المصنف المصدر، الذي يمكن أن يكون أي ملف جدول بيانات من Microsoft Excel أو OpenOffice (بما في ذلك XLS، XLSX، XLSM، XLSB، ODS، وغيرها) بعدد أوراق عمل مختلف.

عند تنفيذ الكود ، يتم تحويل بيانات كافة الأوراق في دفتر العمل إلى تنسيق TXT.

يمكنك تعديل نفس المثال لحفظ ملفك بتنسيق CSV. بشكل افتراضي، [**TxtSaveOptions.separator**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#separator--) هو فاصلة، لذلك لا تحدد فاصل إذا كنت تريد الحفظ بتنسيق CSV.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Txt Save Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Txt Save Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TxtSaveOptions, Utils } = AsposeCells;

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

            // Text save options. You can use any type of separator
            const opts = new TxtSaveOptions();
            opts.separator = '\t';
            opts.exportAllSheets = true;

            // Save entire workbook data into file (as text)
            const outputData = workbook.save(SaveFormat.Txt, opts);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.txt';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Text File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook saved as text. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **حفظ ملفات النص بفاصل مخصص**

تحتوي ملفات النص على بيانات جداول بيانات دون تنسيق. الملف هو نوع ملف نصي عادي يمكن أن يحتوي على بعض الفواصل المخصصة بين بياناته.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Export Workbook to TXT/CSV Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, TxtSaveOptions, SaveFormat } = AsposeCells;

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

            // Create a Workbook object from the uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Instantiate Text File's Save Options
            const options = new TxtSaveOptions();

            // Specify the separator
            options.separator = ";";

            // Optionally specify CSV save format if required by the API
            options.saveFormat = SaveFormat.CSV;

            // Save the workbook to CSV/TXT using the options
            const outputData = wb.save(SaveFormat.CSV, options);
            const blob = new Blob([outputData], { type: 'text/csv' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.csv';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download CSV File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File converted successfully! Click the download link to get the result.</p>';
        });
    </script>
</html>
```


## **مواضيع متقدمة**
- [الاحتفاظ بالفواصل للصفوف الفارغة أثناء تصدير جداول البيانات إلى تنسيق CSV](/cells/ar/javascript-cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [تقليص الصفوف والأعمدة الخالية أثناء تصدير جداول البيانات إلى تنسيق CSV](/cells/ar/javascript-cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)

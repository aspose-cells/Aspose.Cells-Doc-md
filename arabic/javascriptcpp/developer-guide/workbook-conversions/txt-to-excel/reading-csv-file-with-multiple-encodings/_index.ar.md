---
title: قراءة ملف CSV بترميزات متعددة باستخدام جافا سكريبت عبر C++
linktitle: قراءة ملف CSV بترميزات متعددة
type: docs
weight: 200
url: /ar/javascript-cpp/reading-csv-file-with-multiple-encodings/
description: تعلم كيفية قراءة ملفات CSV ذات التشفيرات المتعددة باستخدام Aspose.Cells for JavaScript عبر C++.
---

{{% alert color="primary" %}}

أحيانًا، يحتوي ملف CSV الخاص بك على ترميزات متعددة (Unicode، ANSI، UTF8، UTF7، وغيرها). تتيح لك Aspose.Cells تحميل مثل هذه الملفات وتحويلها إلى تنسيقات أخرى، مثل PDF أو XLSX.

{{% /alert %}}

توفر Aspose.Cells الخاصية [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/javascript-cpp/txtloadoptions/#isMultiEncoded--)، والتي تحتاج إلى ضبطها على **true** لتحميل ملف CSV الخاص بك مع ترميزات متعددة بشكل صحيح.

يوضح اللقطة الشاشية التالية ملف CSV عينة يحتوي على سطرين. السطر الأول بترميز **ANSI** والسطر الثاني بترميز **Unicode**.

|**ملف الإدخال**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

 تظهر الصورة التالية ملف XLSX الذي تم تحويله من ملف CSV أعلاه دون ضبط الخاصية [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/javascript-cpp/txtloadoptions/#isMultiEncoded--) على **true**. كما ترى، لم يتم تحويل النص Unicode بشكل صحيح.

|**ملف الإخراج 1: لم يتم اتخاذ إجراءات للتعامل مع الترميز المتعدد**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

تظهر الصورة التالية ملف XLSX الذي تم تحويله من ملف CSV السابق بعد ضبط الخاصية [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/javascript-cpp/txtloadoptions/#isMultiEncoded--) على **true**. كما ترى، النص الداخلي Unicode الآن تم تحويله بشكل صحيح.

|**ملف الإخراج 2: تم تعيين IsMultiEncoded على true**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

أدناه الكود النموذجي الذي يحول ملف CSV أعلاه إلى صيغة XLSX بشكل صحيح.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Convert Multi-Encoded CSV to XLSX</h1>
        <input type="file" id="fileInput" accept=".csv" />
        <button id="runExample">Convert to XLSX</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TxtLoadOptions, Utils } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select a CSV file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create TxtLoadOptions and set isMultiEncoded property
            const options = new TxtLoadOptions();
            options.isMultiEncoded = true;

            // Load the CSV into a Workbook using the options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), options);

            // Save the workbook to XLSX format and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            const outName = file.name.replace(/(\.[^/.]+)$/, '$1.out.xlsx');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = outName;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Converted Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File converted successfully! Click the download link to save the XLSX file.</p>';
        });
    </script>
</html>
```

## مقالات ذات صلة

- [فتح ملفات CSV](/cells/ar/javascript-cpp/opening-files-with-different-formats/#opening-csv-files)

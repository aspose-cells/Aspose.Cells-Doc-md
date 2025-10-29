---
title: تطبيق نظام التاريخ 1904 باستخدام جافاسكريبت عبر C++
description: Aspose.Cells هي مكتبة جافاسكريبت للعمل مع ملفات جداول البيانات. تدعم تنفيذ نظام التاريخ 1904، مما يسمح للمستخدمين بالحساب والتنسيق استنادًا إلى نظام التاريخ 1904 الذي يبدأ من 1 يناير 1904. تصف هذه المقالة كيفية تنفيذ نظام التاريخ 1904 باستخدام مكتبة Aspose.Cells.
keywords: Aspose.Cells، نظام تاريخ 1904، جدول البيانات، الحساب، التنسيق، جافاسكريبت عبر C++
type: docs
weight: 7000
url: /ar/javascript-cpp/implement-1904-date-system/
---

{{% alert color="primary" %}} 

يدعم Microsoft Excel نظامي التاريخ: نظام تاريخ 1900 (نظام التاريخ الافتراضي في Excel لنظام Windows) ونظام التاريخ 1904. يستخدم نظام التاريخ 1904 عادةً لتوفير التوافق مع ملفات Excel لنظام Macintosh، وهو النظام الافتراضي إذا كنت تستخدم Excel لنظام Macintosh. يمكنك تعيين نظام التاريخ 1904 لملفات Excel باستخدام Aspose.Cells for JavaScript عبر C++. 

{{% /alert %}} 

لتنفيذ نظام التاريخ 1904 في Microsoft Excel (على سبيل المثال، Microsoft Excel 2003):

1. من القائمة **الأدوات**, حدد **الخيارات**, وحدد **الحساب**.
1. حدد خيار **نظام تاريخ 1904**.
1. انقر على **موافق**.

|**اختيار نظام تاريخ 1904 في Microsoft Excel**|
| :- |
|![todo:image_alt_text](implement-1904-date-system_1.png)|

انظر إلى الرمز البريدي العيني التالي حول كيفية تحقيق ذلك باستخدام واجهات برمجة التطبيقات Aspose.Cells.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Enable 1904 Date System</h1>
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

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Implement 1904 date system
            workbook.settings.date1904 = true;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Mybook.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">1904 date system enabled. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

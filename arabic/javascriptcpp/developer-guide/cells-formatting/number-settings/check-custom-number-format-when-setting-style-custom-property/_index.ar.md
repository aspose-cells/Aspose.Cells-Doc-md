---
title: تحقق من تنسيق الرقم المخصص عند ضبط خاصية Style.Custom
linktitle: تحقق من تنسيق الرقم المخصص عند ضبط خاصية Style.Custom
description: Aspose.Cells هي مكتبة جافا سكريبت للعمل مع ملفات الجدول الإلكتروني، وتدعم فحص تنسيقات الأرقام المخصصة عند التزيين. سيعرض لك هذا المقال كيفية استخدام مكتبة Aspose.Cells لفحص تنسيقات الأرقام المخصصة لضمان صحة التزيين.
keywords: مكتبات Aspose.Cells، جافاسكريبت، الجداول الإلكترونية، التزيين، تنسيق الأرقام المخصصة، الفحص، التحقق
type: docs
weight: 170
url: /ar/javascript-cpp/check-custom-number-format-when-setting-style-custom-property/
---

## **سيناريوهات الاستخدام المحتملة**

إذا قمت بتعيين تنسيق رقم مخصص غير صالح لخاصية [**Style.custom**](https://reference.aspose.com/cells/javascript-cpp/style/#custom-string-)، فلن يرمي Script عبر C++ أي استثناء. ولكن إذا أردت أن يتحقق Aspose.Cells من صلاحية تنسيق الرقم المخصص المعين أو لا، يرجى ضبط خاصية [**Workbook.settings.checkCustomNumberFormat**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#checkCustomNumberFormat-boolean-) على **true**.

## **التحقق من تنسيق الرقم المخصص عند تعيين خاصية Style.custom**

يعين الكود النموذجي التالي تنسيق رقم مخصص غير صالح لخاصية [**Style.custom**](https://reference.aspose.com/cells/javascript-cpp/style/#custom-string-). بما أننا قمنا سابقًا بضبط الخاصية [**Workbook.settings.checkCustomNumberFormat**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#checkCustomNumberFormat-boolean-) على **true**، فإنه يرمي استثناء، مثل تنسيق رقم غير صالح. يرجى قراءة التعليقات داخل الكود للمزيد من المساعدة.

## **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Check Custom Number Format</h1>
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
            let workbook;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new empty workbook if no file is provided
                workbook = new Workbook();
            }

            // Setting this property to true will make Aspose.Cells throw an exception
            // when invalid custom number format is assigned to Style.custom property
            workbook.settings.checkCustomNumberFormat = true;

            // Access first worksheet
            const sheet = workbook.worksheets.get(0);

            // Access cell A1 and put some number to it
            const cell = sheet.cells.get("A1");
            cell.value = 2347;

            // Access cell's style and set its Style.custom property
            const style = cell.style;

            // This line will throw exception if workbook.settings.checkCustomNumberFormat is set to true
            style.custom = "ggg @ fff"; // Invalid custom number format

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

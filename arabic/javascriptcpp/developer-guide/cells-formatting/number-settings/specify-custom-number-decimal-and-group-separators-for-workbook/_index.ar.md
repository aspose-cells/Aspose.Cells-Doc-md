---
title: تحديد فاصل عشري مخصص للأرقام وفاصلات مجموع للورقة العمل
linktitle: تحديد فاصل عشري مخصص للأرقام وفاصلات مجموع للورقة العمل
type: docs
weight: 110
url: /ar/javascript-cpp/specify-custom-number-decimal-and-group-separators-for-workbook/
description: تغيير فواصل الأرقام العشرية والمجمعة في إكسل باستخدام Aspose.Cells for JavaScript عبر C++.
keywords: تحديد فاصل عشري مخصص في إكسل باستخدام جافا سكريبت عبر C++، تحديد فاصل مجموعات مخصص في إكسل باستخدام جافا سكريبت عبر C++، تغيير فاصل عشري وفاصل مجموعات في إكسل باستخدام جافا سكريبت عبر C++
---

{{% alert color="primary" %}}

يمكنك في Microsoft Excel تحديد الفاصل العشري المخصص وفاصل الآلاف بدلاً من استخدام الفواصل النظامية من **خيارات Excel المتقدمة** كما هو موضح في اللقطة أدناه.

يوفر Aspose.Cells الطريقتين [**WorkbookSettings.numberDecimalSeparator**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#numberDecimalSeparator-string-) و [**WorkbookSettings.numberGroupSeparator**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#numberGroupSeparator-string-) لضبط الفواصل المخصصة لتنسيق / تحليل الأرقام.

{{% /alert %}}

## **تحديد الفواصل المخصصة باستخدام Microsoft Excel**

تُظهر اللقطة الشاشية التالية **خيارات Excel المتقدمة** وتبرز القسم الخاص بتحديد **الفواصل المخصصة**.

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **تحديد فواصل مخصصة باستخدام Aspose.Cells for JavaScript عبر C++**

يوضح الكود العينة التالي كيفية تحديد الفواصل المخصصة باستخدام واجهة برمجة التطبيقات Aspose.Cells. يحدد فاصل العدد المخصص وفاصل المجموعة المخصصين على أنهما نقطة ومسافة على التوالي.

### رمز جافا سكريبت لتحديد فواصل الأرقام العشرية والمجمعة المخصصة

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Custom Number Separator Example</h1>
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

            // Load workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify custom separators
            workbook.settings.numberDecimalSeparator = '.';
            workbook.settings.numberGroupSeparator = ' ';

            const worksheet = workbook.worksheets.get(0);

            // Set cell value
            const cell = worksheet.cells.get("A1");
            cell.value = 123456.789;

            // Set custom cell style
            const style = cell.style;
            style.custom = "#,##0.000;[Red]#,##0.000";
            cell.style = style;

            worksheet.autoFitColumns();

            // Save workbook as pdf
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CustomSeparator_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```

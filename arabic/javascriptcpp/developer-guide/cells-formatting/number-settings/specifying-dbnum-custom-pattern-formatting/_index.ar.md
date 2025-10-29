---
title: تحديد تنسيق نمط DBNum المخصص
linktitle: تحديد تنسيق نمط DBNum المخصص
description: Aspose.Cells هي مكتبة لجافا سكريبت عبر C++ تدعم تنسيق التواريخ والأرقام باستخدام أنماط تنسيق مخصصة. يوضح هذا المقال كيفية تحديد نمط التنسيق المخصص dbnum لمزيد من السيطرة على عرض الأرقام.
keywords: Aspose.Cells، جافا سكريبت عبر C++، جدول بيانات إلكتروني، نمط تنسيق مخصص، تنسيق، dbnum ، عرض التحكم
type: docs
weight: 110
url: /ar/javascript-cpp/specifying-dbnum-custom-pattern-formatting/
---

## **سيناريوهات الاستخدام المحتملة**

يدعم Aspose.Cells for JavaScript عبر C++ تنسيق النمط المخصص *DBNum*. على سبيل المثال، إذا كانت قيمة الخلية هي 123 وقمت بتحديد تنسيقها المخصص كـ [DBNum2][$-804]General، فستظهر كالكتابة 壹佰贰拾叁. يمكنك تحديد تنسيقك المخصص باستخدام طريقتي [**Cell.style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) و [**Style.custom(string)**](https://reference.aspose.com/cells/javascript-cpp/style/#custom-string-).

## **الكود المثالي**

يُظهر الكود النموذجي التالي كيفية تحديد تنسيق نمط مخصص *DBNum*. يرجى مراجعة [ملف PDF الناتج](43352081.pdf) للمزيد من المساعدة.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - DBNum Custom Formatting Example</h1>
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

            // Create or load workbook
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet.
            const ws = workbook.worksheets.get(0);

            // Access cell A1 and put value 123.
            const cell = ws.cells.get("A1");
            cell.value = 123;

            // Access cell style.
            const st = cell.style;

            // Specifying DBNum custom pattern formatting.
            st.custom = "[DBNum2][$-804]General";

            // Set the cell style.
            cell.style = st;

            // Set the first column width.
            ws.cells.columns.get(0).width = 30;

            // Save the workbook in output pdf format.
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: "application/pdf" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDBNumCustomFormatting.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```

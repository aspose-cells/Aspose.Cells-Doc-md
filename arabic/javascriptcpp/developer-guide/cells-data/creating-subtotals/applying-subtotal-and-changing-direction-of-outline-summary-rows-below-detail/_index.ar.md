---
title: تطبيق الإجمالي الجزئي وتغيير اتجاه الصفوف الجملية تحت البيانات الدقيقة
type: docs
weight: 100
url: /ar/javascript-cpp/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
description: تعلم كيفية تطبيق المجموع الفرعي وتغيير اتجاه خلايا ملخص التخطيط عند استخدام Aspose.Cells for JavaScript عبر API C++.
keywords: تطبيق الإجمالي الجزئي، إضافة الإجمالي الجزئي، تغيير اتجاه صفوف الملخص الإطاري أدناه، تغيير اتجاه أعمدة الملخص الإطاري إلى اليمين من التفاصيل، إنشاء الإجمالي الجزئي وتغيير اتجاه صفوف الملخص التفصيلي.
---

{{% alert color="primary" %}}

سيقوم هذا المقال بشرح كيفية تطبيق الإجمالي الجزئي على البيانات وتغيير اتجاه صفوف الملخص التفصيلي.

يمكنك تطبيق الإجمالي الجزئي على البيانات باستخدام الطريقة [**Worksheet.cells.subtotal()**](https://reference.aspose.com/cells/javascript-cpp/cells/#subtotal-cellarea-number-consolidationfunction-numberarray-boolean-boolean-boolean-). تأخذ المعلمات التالية.

- **منطقة الخلية** - النطاق الذي سيتم تطبيق الإجمالي عليه
- **التجميع حسب** - الحقل الذي يتم التجميع حسبه، كتعويض صفري مبني
- **الوظيفة** - الوظيفة الإجمالي
- **قائمة الإجمالي** - مصفوفة من الحقول المبنية على التعويض الصفري، تشير إلى الحقول التي يتم إضافة الإجمالي لها
- **تبديل** - يشير ما إذا كان يجب استبدال الإجمالي الحالي
- **PageBreaks** - يشير إلى ما إذا كان هناك فاصل صفحة بين المجموعات
- **ملخص أدنى البيانات** - يشير ما إذا كان يجب إضافة ملخص أدنى للبيانات.

بالإضافة إلى ذلك، يمكنك التحكم في اتجاه الصفوف المخططة أدناه للملخص كما هو موضح في اللقطة الشاشة التالية باستخدام خاصية Worksheet.Outline.SummaryRowBelow. يمكنك فتح هذا الإعداد في برنامج Microsoft Excel باستخدام Data > Outline > Settings

![todo:image_alt_text](1.png)

{{% /alert %}}

## صور ملفات المصدر والإخراج

تظهر اللقطة الشاشية التالية ملف Excel الأصلي المستخدم في الشفرة المثالية أدناه والذي يحتوي على بعض البيانات في الأعمدة A و B.

![todo:image_alt_text](2.png)

تظهر اللقطة الشاشة التالية ملف Excel الناتج الذي تم إنشاؤه بواسطة الكود النموذجي. كما ترون، تم تطبيق الإجمالي إلى النطاق A2:B11 واتجاه المخطط هو صفوف ملخص أدناه للتفاصيل.

![todo:image_alt_text](3.png)

## جافا سكريبت لتطبيق المجموع الفرعي وتغيير اتجاه خلايا ملخص التخطيط



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Subtotal Example</title>
    </head>
    <body>
        <h1>Apply Subtotal Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, ConsolidationFunction, Utils } = AsposeCells;

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

            // Create workbook from uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Get the Cells collection in the first worksheet
            const cells = worksheet.cells;

            // Create a cellarea i.e., A2:B11
            const ca = CellArea.createCellArea("A2", "B11");

            // Apply subtotal, the consolidation function is Sum and it will applied to Second column (B) in the list
            cells.subtotal(ca, 0, ConsolidationFunction.Sum, [1], true, false, true);

            // Set the direction of outline summary
            worksheet.outline.summaryRowBelow = true;

            // Save the excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Subtotal applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

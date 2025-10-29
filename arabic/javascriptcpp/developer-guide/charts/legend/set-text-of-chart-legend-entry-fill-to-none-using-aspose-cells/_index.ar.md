---
title: تعيين نص إدخال أسطورة المخطط ليكون بدون باستخدام Aspose.Cells for JavaScript عبر C++
linktitle: ضبط نص إدخال وسام الرسم البياني على لا شيء باستخدام Aspose.Cells
description: تعرف على كيفية استخدام Aspose.Cells for JavaScript عبر C++ لضبط تعبئة إدخال مفتاح أسطورة الرسم البياني إلى لا شيء. ستوضح هذه الدليل كيف تعدل لون التعبئة الخاص بنصوص الأسطورة في مخططات Microsoft Excel لتحسين التصور والتخصيص.
keywords: Aspose.Cells for JavaScript عبر C++، تعبئة إدخال أسطورة الرسم البياني، Microsoft Excel، التصور، التخصيص.
type: docs
weight: 320
url: /ar/javascript-cpp/set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells/
---

{{% alert color="primary" %}}

إذا كنت ترغب في تعيين نص مدخلات أسطورة المخطط إلى لا شيء حتى لا يتم عرضها داخل أسطورة المخطط، يرجى تعيين [**LegendEntry.isTextNoFill()**](https://reference.aspose.com/cells/javascript-cpp/legendentry/#isTextNoFill--) إلى **true**.

{{% /alert %}}

يقوم الكود العينة التالي بتعيين نص إدخال تسمية المخطط الثاني إلى لا شيء. يرجى تنزيل [ملف Excel عينة](5115219.xlsx) المستخدم في هذا الكود و[ملف Excel الخرج](5115217.xlsx) الذي تم إنشاؤه به للرجوع إليه.

 تبرز لقطة الشاشة التالية تأثير هذا الكود على [ملف Excel النموذجي](5115219.xlsx).

![todo:image_alt_text](set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells_1.png)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Chart Legend Entry Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Access the first chart inside the sheet
            const chart = sheet.charts.get(0);

            // Set text of second legend entry fill to none
            const legendEntry = chart.legend.legendEntries.get(1);
            legendEntry.isTextNoFill = true;

            // Save the workbook in xlsx format and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ChartLegendEntry_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

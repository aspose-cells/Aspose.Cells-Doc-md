---
title: عرض إضافات Office أثناء تحويل Excel إلى PDF باستخدام JavaScript عبر C++
linktitle: عرض إضافات Office أثناء تحويل Excel إلى صيغة PDF
type: docs
weight: 100
url: /ar/javascript-cpp/render-office-add-ins-while-converting-excel-to-pdf/
---

## **سيناريوهات الاستخدام المحتملة**

في السابق، لم تتمكن Aspose.Cells من عرض إضافات Office عند حفظ ملف إكسيل بصيغة PDF. الآن، تعرض Aspose.Cells الإضافة بشكل صحيح. لا يلزمك استخدام أي طريقة أو خاصية خاصة لعرض الإضافات Office في PDF الناتج. فقط احفظ ملف إكسيل بصيغة PDF، وسيتم عرض الإضافة.

## **تقديم الإضافات المكتبية أثناء تحويل Excel إلى PDF**

الكود التالي يحفظ [ملف Excel النموذجي](60489769.xlsx) الذي يحتوي على إضافات Office، يرجى الاطلاع على [ملف PDF الناتج مع الإصدار السابق 17.11](60489770.pdf) و[ملف PDF الناتج مع الإصدار الأحدث 17.12 وما بعد](60489771.pdf). الملف السابق يكون PDF الناتج فارغًا، لكن النسخة الأحدث تظهر الإضافة.

## **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Render Office Add-Ins to PDF Example</title>
    </head>
    <body>
        <h1>Render Office Add-Ins to PDF Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get Aspose.Cells version (converted from getVersion())
            const version = AsposeCells.CellsHelper.version;

            // Save workbook to PDF format
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = `output-${version}.pdf`;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Saved to PDF successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

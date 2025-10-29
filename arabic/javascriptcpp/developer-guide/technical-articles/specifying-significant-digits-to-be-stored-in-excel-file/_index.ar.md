---
title: تحديد الأرقام المهمة لتخزينها في ملف إكسل باستخدام جافا سكريبت عبر C++
linktitle: تحديد الأرقام البارزة التي يجب تخزينها في ملف Excel
type: docs
weight: 30
url: /ar/javascript-cpp/specifying-significant-digits-to-be-stored-in-excel-file/
description: تعلم كيفية تحديد الأرقام المهمة لتخزينها في ملف إكسل باستخدام Aspose.Cells for JavaScript عبر C++.
---

## **سيناريوهات الاستخدام المحتملة**  

 بشكل افتراضي، يخزن Aspose.Cells for JavaScript عبر C++ 17 رقمًا مهمًا لقيمات doubles داخل ملف إكسل، على عكس MS-Excel الذي يخزن فقط 15 رقمًا مهمًا. يمكنك تغيير السلوك الافتراضي لـ Aspose.Cells من 17 رقمًا مهمًا إلى 15 رقمًا مهمًا باستخدام الخاصية [**CellsHelper.significantDigits**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#significantDigits--).  

## **تحديد عدد الأرقام المعنوية التي سيتم تخزينها في ملف Excel**  

يعرض رمز النموذج التالي كيف يُجبر Aspose.Cells على استخدام 15 رقمًا مهمًا أثناء تخزين القيم المزدوجة داخل ملف Excel. تحقق من [ملف الإكسل الناتج](22774105.xlsx). غيّر امتداده إلى .zip وفك ضغطه، سترى أن 15 رقمًا مهمًا فقط مخزن داخل ملف الإكسل. يوضح لقطة الشاشة التالية تأثير خاصية [**CellsHelper.significantDigits**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#significantDigits--) على ملف الإكسل الناتج.  

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)  

## **الكود المثالي**  

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Aspose.Cells Example - Significant Digits</title>
    </head>
    <body>
        <h1>Significant Digits Example</h1>
        <p>This example sets CellsHelper.significantDigits to 15 and writes a double to cell A1.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellsHelper } = AsposeCells;

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

            // If a file is provided, open it; otherwise create a new workbook (matches original Node behavior)
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // By default, Aspose.Cells stores 17 significant digits unlike MS-Excel which stores only 15 significant digits
            CellsHelper.significantDigits = 15;

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cell A1
            const c = worksheet.cells.get("A1");

            // Put double value, only 15 significant digits as specified by CellsHelper.significantDigits above will be stored
            c.value = 1234567890.123451711;

            // Saving the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_SignificantDigits.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created/modified successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

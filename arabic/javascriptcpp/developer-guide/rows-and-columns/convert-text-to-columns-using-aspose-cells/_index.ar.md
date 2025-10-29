---
title: تحويل النص إلى أعمدة باستخدام Aspose.Cells for JavaScript عبر C++
linktitle: تحويل النص إلى أعمدة
type: docs
weight: 30
url: /ar/javascript-cpp/convert-text-to-columns-using-aspose-cells/
description: تعلم كيفية تحويل النص إلى أعمدة في Excel باستخدام Aspose.Cells for JavaScript عبر C++.
---

## **سيناريوهات الاستخدام المحتملة**  

 يمكنك تحويل النص إلى أعمدة باستخدام Microsoft Excel. تتوفر هذه الميزة ضمن *أدوات البيانات* تحت تبويب *البيانات*. من أجل تقسيم محتوى عمود إلى عدة أعمدة، يجب أن يحتوي البيانات على فاصل محدد مثل فاصلة (أو أي حرف آخر) حيث يقوم Microsoft Excel بفصل محتوى الخلية إلى خلايا متعددة. كما توفر Aspose.Cells for JavaScript عبر C++ هذه الميزة من خلال [**Cells.textToColumns(number, number, number, TxtLoadOptions)**](https://reference.aspose.com/cells/javascript-cpp/cells/#textToColumns-number-number-number-txtloadoptions-).  

## **تحويل النص إلى أعمدة باستخدام Aspose.Cells for JavaScript عبر C++**  

يوضح رمز العينة التالي استخدام أسلوب [**Cells.textToColumns(number, number, number, TxtLoadOptions)**](https://reference.aspose.com/cells/javascript-cpp/cells/#textToColumns-number-number-number-txtloadoptions-). يضيف الرمز أولاً بعض أسماء الأشخاص في العمود أ من ورقة العمل الأولى. يتم فصل الاسم الأول واسم العائلة بواسطة مسافة. ثم يطبق أسلوب [**Cells.textToColumns(number, number, number, TxtLoadOptions)**](https://reference.aspose.com/cells/javascript-cpp/cells/#textToColumns-number-number-number-txtloadoptions-) على العمود أ ويحفظه كملف إكسل للإخراج. إذا فتحت ملف إكسل الناتج [ملف الإكسل](25395213.xlsx)، سترى أن الأسماء الأولى موجودة في العمود أ بينما أسماء العائلة في العمود ب كما هو موضح في لقطة الشاشة هذه.  

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)  

## **الكود المثالي**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Text to Columns Example</h1>
        <p>Select an optional Excel file to start from, or leave empty to create a new workbook.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
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
            const resultDiv = document.getElementById('result');

            // Basic validation only: file is optional
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new workbook if no file is provided
                workbook = new Workbook();
            }

            // Access first worksheet.
            const ws = workbook.worksheets.get(0);

            // Add people name in column A. First name and last name are separated by space.
            ws.cells.get("A1").value = "John Teal";
            ws.cells.get("A2").value = "Peter Graham";
            ws.cells.get("A3").value = "Brady Cortez";
            ws.cells.get("A4").value = "Mack Nick";
            ws.cells.get("A5").value = "Hsu Lee";

            // Create text load options with space as separator.
            const opts = new TxtLoadOptions();
            opts.separator = ' ';

            // Split the column A into two columns using TextToColumns() method.
            // Now column A will have first name and column B will have second name.
            ws.cells.textToColumns(0, 0, 5, opts);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputTextToColumns.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

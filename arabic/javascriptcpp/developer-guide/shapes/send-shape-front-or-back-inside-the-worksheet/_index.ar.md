---
title: إرسال الشكل للأمام أو للخلف داخل ورقة العمل باستخدام جافا سكريبت عبر C++
linktitle: إرسال الشكل إلى الأمام أو الوراء داخل ورقة العمل
type: docs
weight: 3400
url: /ar/javascript-cpp/send-shape-front-or-back-inside-the-worksheet/
description: تعلم كيفية إرسال شكل إلى الأمام أو الخلف في ورقة العمل باستخدام Aspose.Cells for JavaScript عبر C++. 
---

## **سيناريوهات الاستخدام المحتملة**

عندما تتواجد أشكال متعددة في نفس الموقع، يتم تحديد رؤيتها حسب مواقع ترتيب z. توفر Aspose.Cells طريقة [**Shape.toFrontOrBack()**](https://reference.aspose.com/cells/javascript-cpp/shape/#toFrontOrBack-number-)، التي تغير موضع ترتيب z للشكل. لإرسال شكل إلى الخلف، ستستخدم رقمًا سالبًا مثل -1، -2، -3، وهكذا، ولإحضار شكل إلى الأمام، ستستخدم رقمًا موجبًا مثل 1، 2، 3، وهكذا.

## **إرسال الشكل إلى الأمام أو الوراء داخل ورقة العمل**

يوضح رمز العينة التالي استخدام طريقة [**Shape.toFrontOrBack()**](https://reference.aspose.com/cells/javascript-cpp/shape/#toFrontOrBack-number-). الرجاء مراجعة ملف Excel النموذجي (50528330.xlsx) المستخدم في الكود وملف Excel الناتج (50528331.xlsx) الذي تم إنشاؤه به. تُظهر لقطة الشاشة تأثير الكود على ملف Excel النموذجي عند التشغيل.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Send Shapes Front or Back</title>
    </head>
    <body>
        <h1>Send Shapes to Front or Back Example</h1>
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
            const resultDiv = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Access first and fourth shapes
            const shape1 = worksheet.shapes.get(0);
            const shape4 = worksheet.shapes.get(3);

            // Print the Z-Order position of shape1
            resultDiv.innerHTML = `<p>Z-Order Shape 1: ${shape1.zOrderPosition}</p>`;

            // Send this shape to front
            shape1.toFrontOrBack(2);

            // Print the Z-Order position of shape4
            resultDiv.innerHTML += `<p>Z-Order Shape 4: ${shape4.zOrderPosition}</p>`;

            // Send this shape to back
            shape4.toFrontOrBack(-2);

            // Saving the modified Excel file and preparing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputToFrontOrBack.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML += '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

---
title: تحويل بيانات النص الرقمي إلى رقم
type: docs
weight: 900
url: /ar/javascript-cpp/convert-text-numeric-data-to-number/
description: تعلم كيفية تحويل الأرقام المخزنة كنص في Excel إلى أرقام باستخدام واجهة برمجة تطبيقات Aspose.Cells for Javaسكريبت عبر C++.
keywords: تحويل النص إلى رقم في إكسل، شفرة جافا سكريبت لتحويل النص إلى رقم في إكسل، تحويل البيانات الرقمية النصية إلى رقم، رمز جافا سكريبت لتحويل البيانات النصية الرقمية إلى رقم، تحويل النص الرقمي إلى رقم في إكسل، رموز جافا سكريبت لتحويل النص الرقمي إلى رقم، تحويل النص الرقمي إلى رقم بواسطة جافا سكريبت، تحويل النص الرقمي إلى رقم في إكسل باستخدام جافا سكريبت، تحويل السلسلة الرقمية إلى رقم في إكسل باستخدام جافا سكريبت، رمز جافا سكريبت لتحويل البيانات الرقمية النصية إلى رقم، رمز جافا سكريبت لتحويل السلسلة الرقمية إلى رقم
---

## **سيناريوهات الاستخدام المحتملة**
أحيانًا، تريد تحويل البيانات الرقمية المُدخلة كنص إلى أرقام. يمكنك إدخال الأرقام كنص في Microsoft Excel بوضع فاصلة قبل الرقم، على سبيل المثال **'12345**. ثم تعتبر إكسل الرقم كابل نص. يتيح لك Aspose.Cells for Javaسكريبت عبر C++ تحويل السلاسل إلى أرقام.


## كيفية تحويل الأرقام المخزنة كنصوص إلى أرقام في Excel
يمكنك تحويل الأرقام المخزنة كنصوص إلى أرقام باتباع خطوات بسيطة قليلة.
1. حدد أي خلية واحدة أو مجموعة من الخلايا التي تحتوي على مؤشر خطأ في الزاوية العلوية اليسرى.
2. بجانب الخلية المحددة أو مجموعة الخلايا، انقر فوق زر الخطأ الذي يظهر. في القائمة، انقر على تحويل إلى رقم. 
<br>
<img src="4.png" width=70% />
3. إذا كان زر التنبيه غير متاح، حدد العمود الذي يوجد به المشكلة. إذا كنت لا ترغب في تحويل العمود كاملاً، يمكنك تحديد خلية واحدة أو أكثر بدلاً من ذلك. فقط تأكد من أن الخلايا التي تحددها في نفس العمود، وإلا فإن هذه العملية لن تعمل. زر النص إلى أعمدة عادة ما يستخدم لتقسيم عمود، ولكن يمكن أيضاً استخدامه لتحويل عمود واحد من النصوص إلى أرقام. في علامة البيانات، انقر فوق النص إلى أعمدة.
<br>
<img src="1.png" width=70% />
4. انقر فوق زر الانتهاء في صندوق البوب ​​آب.
<br>
<img src="2.png" width=70% />
5. يتم تحويل الأرقام المخزنة كنصوص إلى أرقام.
<br>
<img src="3.png" width=70% />

## كيفية تحويل الأرقام المخزنة كنص إلى أرقام باستخدام Aspose.Cells for Javaسكريبت عبر C++
يوفر Aspose.Cells for Javaسكريبت عبر C++ الطريقة [**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/javascript-cpp/cells/#convertStringToNumericValue--) التي يمكن استخدامها لتحويل جميع البيانات الرقمية النصية أو السلاسل إلى أرقام.

تظهر اللقطة الشاشية التالية أرقام سلسلة في الخلايا **A1:A17**. تم تحويل أرقام السلسلة إلى أرقام باستخدام {0} في اللقطة الشاشية التالية. كما يمكنك رؤيتها، فهي محاذاة الآن إلى اليمين.
<br>
<img src="5.png" width=70% />

تم تحويل هذه الأرقام النصية إلى أرقام باستخدام [**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/javascript-cpp/cells/#convertStringToNumericValue--) في اللقطة الشاشية التالية. كما يمكنك رؤيتها، فهي الآن محاذاة إلى اليمين.
<br>
<img src="6.png" width=70% />

## رمز جافا سكريبت لتحويل البيانات الرقمية النصية إلى أرقام فعلية

يوضح الكود العيني التالي كيفية تحويل جميع البيانات الرقمية النصية إلى أرقام فعلية في جميع أوراق العمل.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Strings to Numeric Values in All Sheets</h1>
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

            // Instantiate workbook object with the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access worksheets collection
            const sheets = workbook.worksheets;
            const sheetcount = sheets.count;

            // Iterate through all worksheets and convert strings to numeric values
            for (let i = 0; i < sheetcount; i++) {
                const sheet = sheets.get(i);
                sheet.cells.convertStringToNumericValue();
            }

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

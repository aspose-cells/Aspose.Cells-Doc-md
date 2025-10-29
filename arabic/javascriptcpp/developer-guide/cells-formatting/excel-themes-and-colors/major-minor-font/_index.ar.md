---
title: سمات العناوين والنص الأساسي للسمات
linktitle: سمات العناوين والنص الأساسي للسمات
description: Aspose.Cells هي مكتبة جافا سكريبت عبر C++ للعمل مع ملفات الجدول. تدعم تعيين خطوط سمة الرأس والجسم في مستندات إكسل، مما يتيح للمستخدمين تخصيص مظهر ونمط المستند. ستقدم هذه المقالة كيفية استخدام مكتبة Aspose.Cells للعمل مع خطوط سمة الرأس والجسم في مستندات إكسل.
keywords: Aspose.Cells، مستند إكسل، رأس، جسم، خط السمة، المظهر، النمط، جافا سكريبت عبر C++
type: docs
weight: 120
url: /ar/javascript-cpp/headings-and-body-theme-font/
---

{{% alert color="primary" %}}

سيتم تغيير الخط الافتراضي تلقائيًا عند تغيير إعداد المنطقة.

إذا تم تغيير الخط الافتراضي، ستتم أيضًا تغيير ارتفاع الصف وعرض العمود، وقد يؤدي ذلك إلى تخريب تخطيط الصفحة.

ما الذي تسبب تغيير الخط الافتراضي؟

إذا تم ضبط خط السمة في Excel، فإن Excel سيقوم تلقائيًا بالتبديل بين خطوط مختلفة استنادًا إلى بيئة اللغة الحالية.

{{% /alert %}}

## **سمات العناوين والنص الأساسي للسمات في Excel**

في Excel، حدد علامة التبويب الصفحة الرئيسية، انقر على مربع اختيار خطوط النص، سترى "خطوط النموذج" مع خطين: Calibri Light (عناوين) و Calibri (الجسم) على الأعلى مع إعداد المنطقة باللغة الإنجليزية.

**![سمات الخطوط](Theme-Fonts.png)**

إذا تم اختيار خط النموذج، فسيقع اسم الخط بشكل مختلف في مناطق مختلفة. إذا كنت لا تريد أن يتغير الخط تلقائيًا في المناطق المختلفة، لا تحدد خطي النموذج.

## **تغيير خطوط العناوين والجسد برمجياً**
مع Aspose.Cells for JavaScript عبر C++، يمكننا التحقق مما إذا كان الخط الافتراضي هو خط سمة أو تعيين خط السمة باستخدام [**Font.schemeType**](https://reference.aspose.com/cells/javascript-cpp/font/#schemeType-fontschemetype-) طريقة.

يعرض رمز النموذج التالي كيفية التلاعب بخط النموذج.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Change Theme Font Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FontSchemeType, Utils } = AsposeCells;

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

            // Accessing and modifying the default style and its font scheme
            let defaultStyle = workbook.defaultStyle;
            let font = defaultStyle.font;
            let schemeType = font.schemeType;

            if (schemeType === FontSchemeType.Major || schemeType === FontSchemeType.Minor) {
                console.log("It's theme font");
            }

            // Change theme font to normal font
            font.schemeType = FontSchemeType.None;

            // Assign the modified default style back to the workbook
            workbook.defaultStyle = defaultStyle;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book1.modified.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Theme font changed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```



## **الحصول ديناميكيًا على خط السمة المحلي برمجياً**
في بعض الأحيان، يكون خوادمنا وأجهزة المستخدمين غير في نفس الإقليم. كيف يمكننا الحصول على نفس الخط الذي يرغب المستخدمون فيه لمعالجة الملف؟

يجب تعيين إعدادات المنطقة الخاصة بالنظام قبل تحميل الملف باستخدام [**LoadOptions.region**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#region-countrycode-) طريقة.

يعرض الشيفرة النموذجية التالية كيفية الحصول على خط سمة محلي.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Get Default Style Local Font Example</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a new LoadOptions.
            const options = new AsposeCells.LoadOptions();
            // Sets the customer's region
            options.region = AsposeCells.CountryCode.Japan;

            // Instantiate a new Workbook using the uploaded file and load options.
            const workbook = new Workbook(new Uint8Array(arrayBuffer), options);

            // Get the default style
            const defaultStyle = workbook.defaultStyle;

            // Gets customer's local font.
            const localFontName = defaultStyle.font.name;

            resultDiv.innerHTML = `<p style="color: green;">Local font name: ${localFontName}</p>`;
        });
    </script>
</html>
```

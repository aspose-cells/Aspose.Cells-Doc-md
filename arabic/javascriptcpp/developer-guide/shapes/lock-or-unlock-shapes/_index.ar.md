---
title: قفل أو إلغاء قفل الأشكال باستخدام جافا سكريبت عبر ++C
linktitle: قفل أو فتح الشكل
type: docs
weight: 200
url: /ar/javascript-cpp/lock-or-unlock-shapes/
description: يعرض هذا المقال رمزًا يشرح كيفية قفل أو إلغاء قفل الأشكال لحمايتها باستخدام مكتبة Aspose.Cells لجافا سكريبت عبر ++C。
keywords: قفل الأشكال في جافا سكريبت عبر ++C لحمايتها، كيفية قفل أو إلغاء قفل الأشكال باستخدام جافا سكريبت عبر ++C، قفل أو إلغاء قفل الأشكال لحمايتها في جافا سكريبت عبر ++C.
---

## **سيناريوهات الاستخدام المحتملة**

أحيانًا، تحتاج إلى حماية جميع الأشكال في بعض الأوراق لمنع تدميرها من قبل مواقف غير مرغوب فيها. في هذه الحالة، تحتاج إلى قفل جميع الأشكال في الورقة المحددة. 

يمكن أن يكون قفل الأشكال في جدول بيانات أو مستند مفيدًا لأسباب عدة:
1. منع التغييرات العرضية: يضمن قفل الأشكال عدم تحريكها أو تغيير حجمها أو حذفها عن طريق المستخدمين عن غير قصد. هذا مهم بشكل خاص في المستندات المعقدة حيث قد تُستخدم الأشكال للملاحظات التوضيحية، أو الرسوم التوضيحية، أو كجزء من تصميم المستند.
1. الحفاظ على التخطيط والتصميم: غالبًا ما تلعب الأشكال دورًا حيويًا في تنظيم المستند والتصميم البصري. يضمن قفلها الحفاظ على المظهر المقصود، مما يضمن بقاء المستند احترافيًا وجذابًا بصريًا.
1. سلامة البيانات: في جداول البيانات، يمكن استخدام الأشكال لإبراز نقاط بيانات مهمة، أو إضافة ملاحظات، أو تقديم تفسيرات بصرية. يضمن قفل هذه الأشكال بقاء المعلومات السياقية التي تقدمها دقيقة وسليمة.
1. الاتساق في المستندات المشتركة: عند التعاون على المستندات، قد يكون لدى المستخدمين المختلفين مستويات متنوعة من الخبرة. يساعد قفل الأشكال على الحفاظ على الاتساق عبر المستند عن طريق منع التعديلات غير المقصودة.
1. الأمان: في المستندات الحساسة، يمكن أن يكون قفل الأشكال جزءًا من استراتيجية أوسع لحماية المعلومات. على سبيل المثال، في التقارير المالية أو المستندات القانونية، يمكن استخدام الأشكال المقفلة لحماية الملاحظات أو النقاط المميزة التي توفر سياقًا هامًا.

أحيانًا، تحتاج إلى القدرة على تعديل أشكال معينة في أوراق عمل معينة محمية، وفي هذه الحالة، تحتاج إلى إلغاء قفل هذه الأشكال. ستوضح هذه المقالة بالتفصيل كيف يمكن قفل وفتح الأشكال المحددة.

## **كيفية قفل الأشكال لحمايتها في إكسيل**

إليك كيفية قفل الخلايا في Microsoft Excel:

1. افتح ملف إكسل الخاص بك: افتح ملف إكسل الذي يحتوي على الأشكال التي تريد قفلها.

1. اختيار الشكل: انقر على الشكل الذي تريد قفله. يمكنك أيضًا اختيار عدة أشكال بالضغط مع الاستمرار على مفتاح Ctrl والنقر على كل شكل.

1. فتح لوحة تنسيق الشكل: انقر بزر الماوس الأيمن على الشكل (الأشكال) المختار واختر "الحجم والخصائص." بدلاً من ذلك، يمكنك الذهاب إلى علامة التبويب "التنسيق" على الشريط، وفي مجموعة "الحجم"، انقر على أيقونة الحوار (السهم الصغير) لفتح لوحة "تنسيق الشكل".
1. قفل الشكل: في لوحة "تنسيق الشكل"، انتقل إلى علامة التبويب "الحجم والخصائص" (الرمز يبدو كمربع بأسهم). تحت قسم "الخصائص"، ضع علامة في مربع "مقفول".
<br>
<img src="1.png" width=60% />
1. حماية ورقة العمل: انتقل إلى علامة التبويب "مراجعة" على الشريط. انقر على "حماية الورقة". ضع كلمة مرور (اختياري) واختر الأذونات التي ترغب في السماح بها (مثل اختيار الخلايا المقفلة، تنسيق الخلايا، وهلم جرا). انقر "موافق".
<br>
<img src="2.png" width=60% />

## **كيفية قفل جميع الأشكال في ورقة عمل محددة**

لحماية جميع الأشكال في ورقة عمل محددة، استخدم وظيفة `worksheet.protect(ProtectionType.Objects)`، كما هو موضح في الكود النموذجي التالي.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Lock Shapes Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ProtectionType } = AsposeCells;

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

            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const text = "This is a test";
            const worksheet = workbook.worksheets.get(0);

            let shape = worksheet.shapes.addTextBox(1, 0, 1, 0, 30, 100);
            shape.text = text;

            shape = worksheet.shapes.addRectangle(5, 0, 1, 0, 30, 100);
            shape.text = text;

            shape = worksheet.shapes.addButton(9, 0, 1, 0, 30, 100);
            shape.text = text;

            shape = worksheet.shapes.addOval(13, 0, 1, 0, 50, 100);
            shape.text = text;

            // Protect all shapes in the specified worksheet
            shape.worksheet.protect(ProtectionType.Objects);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Locked.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Locked.xlsx';

            document.getElementById('result').innerHTML = '<p style="color: green;">Shapes locked successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **كيفية إلغاء قفل الأشكال المحددة في ورقة عمل محمية**

لفتح قفل شكل معين في ورقة عمل محمية، استخدم `shape.isLocked`، كما هو موضح في الكود النموذجي التالي.

ملحوظة: `shape.isLocked` ذو معنى فقط عندما تكون ورقة العمل محمية.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Unlock Shape</title>
    </head>
    <body>
        <h1>Unlock Shape Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get protected worksheet
            const worksheet = workbook.worksheets.get(0);

            // Get the specified shape to be unlocked
            const shape = worksheet.shapes.get("TextBox 1");

            if (!shape) {
                resultDiv.innerHTML = '<p style="color: red;">Shape "TextBox 1" not found.</p>';
                return;
            }

            // Unlock the specified shape
            if (!worksheet.protection.allowEditingObject && shape.isLocked) {
                shape.isLocked = false;
            }

            // Save the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'UnLocked.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Shape unlocked successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

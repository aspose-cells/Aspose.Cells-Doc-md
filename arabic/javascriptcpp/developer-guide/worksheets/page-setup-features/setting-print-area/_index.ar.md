---
title: كيفية ضبط منطقة الطباعة باستخدام JavaScript عبر C++
linktitle: كيفية تعيين منطقة الطباعة
type: docs
weight: 200
url: /ar/javascript-cpp/how-to-set-print-area/
description: يعرض هذا المقال رمزًا يوضح كيفية ضبط منطقة الطباعة باستخدام مكتبة Aspose.Cells ل JavaScript عبر C++.
keywords: تحديد نطاق الطباعة، تعيين نطاق الطباعة، مسح نطاق الطباعة، ضبط ومسح نطاق الطباعة باستخدام JavaScript عبر C++, كيفية ضبط منطقة الطباعة، كيفية مسح منطقة الطباعة باستخدام JavaScript عبر C++, كيفية مسح منطقة الطباعة في JavaScript، كيفية إضافة منطقة طباعة باستخدام JavaScript، كيفية إزالة منطقة الطباعة باستخدام JavaScript، كيفية ضبط منطقة الطباعة في Excel، كيفية مسح منطقة الطباعة في Excel.
---

## **سيناريوهات الاستخدام المحتملة**

تساعدك إعداد منطقة الطباعة في مستند، مثل جدول بيانات Excel، على التحكم في المحتوى الذي يتم تضمينه عند الطباعة. إليك بعض الأسباب لتعيين منطقة طباعة:

1. التركيز على البيانات المحددة: يمكنك طباعة الأقسام الأكثر أهمية فقط، وتجنب المحتوى غير الضروري.
1. تحسين التنسيق: يساعد في تنظيم وتناسب المحتوى بشكل مرتب على الصفحات المطبوعة، وتجنب الانقسامات أو فواصل الصفحات غير المرغوب فيها.
1. توفير الموارد: من خلال تحديد منطقة الطباعة، يمكنك تقليل كمية الورق والحبر المستخدمين.
1. العرض الاحترافي: يضمن أن البيانات المطبوعة تكون مصقولة ونهائية، وهو أمر مهم بشكل خاص للتقارير أو العروض التقديمية.
1. الاتساق: عند طباعة نفس المستند مرات متعددة، فإن وجود منطقة طباعة محددة يضمن الاتساق في المخرجات.

<br>
يعد تعيين منطقة الطباعة مفيدًا بشكل خاص في المستندات الكبيرة حيث يحتاج جزء فقط للمشاركة أو المراجعة بشكل مطبوع.

## **كيفية تعيين منطقة الطباعة في Excel**

لتعيين منطقة طباعة في Excel، اتبع الخطوات التالية:

1. تحديد الخلايا: انقر السحب لتحديد نطاق الخلايا الذي تريد تعيينه كمنطقة طباعة.
1. فتح علامة التبويب تخطيط الصفحة: انتقل إلى علامة التبويب "تخطيط الصفحة" في الشريط أعلى نافذة Excel.
1. تعيين منطقة الطباعة: في مجموعة "إعداد الصفحة"، انقر على "منطقة الطباعة". من القائمة المنسدلة، اختر "تعيين منطقة الطباعة".
<br>
<img src="3.png" width=60% />

1. إضافة إلى منطقة الطباعة: إذا كنت تريد إضافة خلايا إضافية إلى منطقة الطباعة الحالية، حدد الخلايا الإضافية، وانتقل إلى "منطقة الطباعة" في علامة التبويب "تخطيط الصفحة"، واختر "إضافة إلى منطقة الطباعة".

<br>
سيعرف هذا الإجراء الخلايا المحددة كمجال للطباعة. عند طباعة ورقة العمل، سيتم طباعة هذا المجال المحدد فقط.

## **كيفية مسح مجال الطباعة في إكسل**

لمسح مجال الطباعة في إكسل، اتبع الخطوات التالية:

1. افتح علامة تبويب تخطيط الصفحة: انقر على علامة التبويب "تخطيط الصفحة" في الشريط أعلى نافذة إكسل.
1. مسح مجال الطباعة: في مجموعة "إعداد الصفحة"، انقر على "مجال الطباعة". من القائمة المنسدلة، حدد "مسح مجال الطباعة".
<br>
<img src="4.png" width=60% />

<br>
سيؤدي هذا الإجراء إلى إزالة أي مجال طباعة تم تحديده مسبقًا، مما يسمح لطباعة كامل ورقة العمل.

## **ماذا يحدث بعد مسح مجال الطباعة**

مسح مجال الطباعة في تطبيق جدول بيانات مثل إكسل باستخدام Aspose.Cells سيؤدي إلى تضمين كامل ورقة العمل عند طباعة المستند. إذا تم تعيين مجال طباعة، فسيتم طباعة النطاق المحدد فقط من الخلايا. بمسح مجال الطباعة، تضمن عدم تحديد نطاق معين وسيتحقق سلوك الطباعة الافتراضي، الذي يتضمن كامل الورقة.

1. السلوك الافتراضي للطباعة: ستعتبر كامل ورقة العمل للطباعة. هذا يعني أن جميع الخلايا ذات البيانات أو التنسيق ستُطبع.
1. لا حدود لمجال الطباعة: ستتم إزالة الحدود المحددة سابقًا لمجال الطباعة. إذا كانت هناك صفوف وأعمدة معينة مخصصة للطباعة، فلن تكون مقيدة بتلك الحدود.
1. طباعة المحتوى الكامل: سيتم تضمين كافة المحتويات، بما في ذلك العناوين، والتذييلات، وأي بيانات أخرى داخل ورقة العمل، في عملية الطباعة.

## **كيفية ضبط منطقة الطباعة باستخدام Aspose.Cells for JavaScript عبر C++**

لتعيين منطقة الطباعة في ورقة عمل محددة: أولاً، قم بتحميل [الملف النموذجي](input.xlsx)، ثم تحتاج إلى تعديل خاصية [**PageSetup.printArea**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printArea--) لكائن [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/) للورقة المطلوبة. تعيين هذه الخاصية إلى سلسلة نطاق سيؤدي إلى تعيين منطقة الطباعة.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Print Area</title>
    </head>
    <body>
        <h1>Set Print Area Example</h1>
        <input type="file" id="fileInput" accept=".xlsx,.xls" />
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load the workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the desired worksheet (first worksheet)
            const worksheet = workbook.worksheets.get(0);

            // Set the print area - specify the range you want to print
            worksheet.pageSetup.printArea = "A1:D10";

            // Save the workbook as PDF and provide a download link
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'set_print_area.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">Print area set successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```

نتيجة الإخراج:
<br>
<img src="1.png" width=60% />

## **كيفية مسح منطقة الطباعة باستخدام Aspose.Cells for JavaScript عبر C++**

لمسح مجال الطباعة في ورقة عمل محددة: أولاً، قم بتحميل [الملف النموذجي](input.xlsx)، ثم عليك تعديل خاصية [**PageSetup.printArea**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printArea--) من كائن [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/) لورقة العمل المرغوبة. تعيين هذه الخاصية إلى سلسلة فارغة سيمسح مجال الطباعة.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Clear Print Area</title>
    </head>
    <body>
        <h1>Clear Print Area Example</h1>
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
            const resultEl = document.getElementById('result');
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load the workbook
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the desired worksheet
            const worksheet = workbook.worksheets.get(0);

            // Clear the print area
            worksheet.pageSetup.printArea = "";

            // Save the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'clear_print_area.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultEl.innerHTML = '<p style="color: green;">Print area cleared successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```

نتيجة الإخراج:
<br>
<img src="2.png" width=60% />

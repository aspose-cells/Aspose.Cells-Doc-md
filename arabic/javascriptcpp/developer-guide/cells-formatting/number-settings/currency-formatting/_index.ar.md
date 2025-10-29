---
title: كيفية تنسيق الرقم كعملة
type: docs
weight: 10
url: /ar/javascript-cpp/format-number-to-currency/
description: سيقدم هذا المقال كيف يمكن تنسيق رقم إلى عملة باستخدام API Script عبر C++.
keywords: تنسيق الرقم كعملة، إعدادات رقم الخلية، تنسيق الرقم كعملة، إعدادات العملة، تنسيق العملة.
---

## **سيناريوهات الاستخدام المحتملة**
تنسيق الأرقام كعملة في إكسل مهم لعدة أسباب، خاصة عند العمل مع البيانات المالية. إليك سبب فائدته:

1. توضيح القيم المالية: يجعل تنسيق الرقم كعملة من الواضح أن القيمة تمثل مالًا. على سبيل المثال، بدلاً من رؤية 1000، والتي يمكن أن تعني أي شيء، يظهر $1,000 بوضوح أن القيمة مبلغ مالي.
1. يشمل رموز العملة: عند التعامل مع عملات دولية أو متعددة، يوضح تنسيق الأرقام برمز العملة المناسب (مثل $, €, £) نوع العملة المستخدمة، مما يقلل الالتباس في التقارير أو المعاملات المالية متعددة الجنسيات.
1. يعزز العرض المهني: تظهر القيم المالية بشكل منظم ومحترف، وهو مهم بشكل خاص للتقارير والعروض التقديمية والمستندات التجارية. يظهر $10,000.00 بشكل أكثر مصداقية وتنظيمًا من رقم 10000 بسيط.
1. يعزز قابلية القراءة: يضيف تنسيق العملة الفواصل الآلاف والأماكن العشرية، مما يجعل الأرقام الكبيرة أسهل في القراءة. على سبيل المثال، 1000000 يصبح $1,000,000.00، وهو أكثر وضوحًا وأسهل للفهم من لمحة.
1. يضمن الاتساق: من خلال تطبيق تنسيق العملة بشكل متسق، تضمن عرض جميع القيم المالية في مجموعة البيانات بنفس التنسيق. هذا الاتساق مهم للدقة المالية والتواصل المهني، خاصة في جداول بيانات كبيرة تحتوي على العديد من الأرقام.
1. يظهر الدقة: يتضمن تنسيق العملة عادةً مكانين عشريين، مما يسهل رؤية المبالغ المالية الدقيقة. على سبيل المثال، $100.50 يختلف بوضوح عن $100.00، وهو مهم في التقارير المالية حيث تكون الدقة مهمة.
1. يبسط الحسابات المالية: عند إجراء الحسابات المالية (مثل جمع الإجماليات أو حساب المتوسطات)، يساعد تنسيق العملة Excel والمستخدمين على فهم أن البيانات في مصطلحات مالية. يساعد Excel على تطبيق التنسيق المناسب في الصيغ والوظائف، مما يضمن بقاء النتائج متسقة.
1. يقلل من سوء التفسير: بدون تنسيق العملة، يمكن تفسير الأرقام بشكل خاطئ على أنها قيم رقمية عامة بدلاً من مبالغ مالية. على سبيل المثال، يمكن أن يُساء فهم 500 على أنه عدد العناصر أو الوحدات، في حين أن $500.00 تمثل مبلغًا ماليًا بشكل واضح.
1. يعمل مع ميزات المحاسبة: يتوافق تنسيق العملة بشكل جيد مع وظائف المحاسبة في Excel، مثل الميزانية العمومية أو تقارير التدفق النقدي. يجعل القيم أسهل في الاستخدام في البيانات المالية التي يركز فيها المال بشكل رئيسي.
<br>
باختصار، يساعد تنسيق الأرقام كعملة على تمييز القيم المالية عن الأنواع الأخرى من الأرقام، ويزيد من الوضوح، ويسهل تفسير البيانات، خاصة في السياقات المالية.

## **كيفية تنسيق الرقم إلى عملة في Excel**
ل تنسيق الأرقام كعملة في Excel، اتبع الخطوات التالية:

### **باستخدام خيار تنسيق العملة**
1. حدد الخلايا التي تريد تنسيقها كعملة.
1. انتقل إلى علامة التبويب الصفحة الرئيسية على الشريط.
1. في مجموعة الأرقام، انقر على السهم المنسدل بجانب مربع تنسيق الأرقام (قد يعرض "عام" بشكل افتراضي).
<br>
<img src="1.png" width=60% />
1. اختر العملة من القائمة.

### **استخدام مربع حوار تنسيق الخلايا**
1. حدد الخلايا التي تريد تنسيقها.
1. انقر بزر الماوس الأيمن على الخلايا المحددة واختر تنسيق الخلايا لفتح مربع الحوار تنسيق الخلايا.
1. في علامة التبويب الرقم، اختر العملة من القائمة على اليسار.
<br>
<img src="2.png" width=60% />
1. يمكنك تخصيص التالي: أماكن الفاصلة العشرية، الرمز، الأرقام السالبة.
1. انقر موافق لتطبيق التنسيق.

## **كيفية تنسيق الرقم إلى عملة في Aspose.Cells**

لتنسيق الأرقام كعملة في مكتبة Script عبر C++ للعمل مع ملفات إكسل، يمكنك تطبيق تنسيق العملة على الخلايا برمجياً. إليك كيفية القيام بذلك باستخدام Script عبر C++:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Currency Formatting Example</h1>
        <p>Optionally select an Excel file to modify. If no file is selected, a new workbook will be created.</p>
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
            let workbook;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the cell you want to format
            const a1 = worksheet.cells.get("A1");

            // Set a numeric value to the cell
            a1.value = 1234.56;

            // Create a style object to apply the currency format
            const a1Style = a1.style;
            // "7" is the currency format in Excel
            a1Style.number = 7;

            // Apply the style to the cell
            a1.style = a1Style;

            // Access the cell where you want to apply the currency format
            const a2 = worksheet.cells.get("A2");

            // Set a numeric value to the cell
            a2.value = 3456.78;

            // Create a style object to apply the currency format
            const a2Style = a2.style;
            // Custom format for dollar currency
            a2Style.custom = "$#,##0.00";

            // Apply the style to the cell
            a2.style = a2Style;

            // Saving the workbook and providing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CurrencyFormatted.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download CurrencyFormatted.xlsx';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook formatted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

---
title: كيفية قفل الخلايا لحمايتها
type: docs
weight: 130
url: /ar/javascript-cpp/how-to-lock-cells-to-protect-them/
description: يُظهر لك هذا المقال رمزًا يوضح كيفية قفل الخلايا لحمايتها باستخدام Aspose.Cells for JavaScript عبر C++.
keywords: قفل الخلايا باستخدام JavaScript لحمايتها، كيفية قفل الخلايا لحمايتها باستخدام JavaScript، قفل الخلايا لحمايتها في JavaScript.
---

## **سيناريوهات الاستخدام المحتملة**
قفل الخلايا لحمايتها هو ممارسة شائعة في تطبيقات الجداول، مثل مايكروسوفت إكسل أو جوجل شيتس، للأسباب المهمة التالية:

1. منع التغييرات العرضية: يمكن لقفل الخلايا منع المستخدمين من تعديل البيانات أو الصيغ المهمة عن غير قصد. هذا مفيد بشكل خاص في جداول البيانات المعقدة حيث يمكن أن تؤدي التغييرات غير المقصودة إلى أخطاء كبيرة.

1. الحفاظ على سلامة البيانات: من خلال قفل الخلايا، يمكنك ضمان بقاء البيانات الحرجة متسقة ودقيقة. هذا ضروري للمستندات المالية، التقارير، وأي مستندات أخرى تتطلب سلامة البيانات.

1. الوصول المُتحكم فيه: في بيئات التعاون، يتيح قفل الخلايا التحكم في من يمكنه تحرير أجزاء معينة من جدول البيانات. على سبيل المثال، قد ترغب في السماح فقط لأعضاء فريق معينين بتحرير خلايا محددة مع الحفاظ على حماية باقي ورقة العمل.

1. حماية الصيغ: غالبًا ما تكون الصيغ حاسمة للحسابات وتحليل البيانات. يضمن قفل الخلايا التي تحتوي على الصيغ أن لا تتعرض هذه الصيغ للتغيير أو الحذف عن غير قصد، مما قد يعطل وظيفة ورقة العمل بأكملها.

1. تطبيق قواعد العمل: في بعض الحالات، قد تتطلب قواعد العمل أو اللوائح حماية بيانات معينة من التعديل. يساعد قفل الخلايا على الامتثال لهذه المتطلبات.

1. توجيه المستخدمين: من خلال قفل الخلايا وتقديم تعليمات واضحة حول الخلايا التي يمكن تحريرها، يمكنك إرشاد المستخدمين حول كيفية التفاعل مع جدول البيانات، مما يقلل من الالتباس والأخطاء.

## **كيفية قفل الخلايا لحمايتها في إكسل**
إليك كيفية قفل الخلايا في Microsoft Excel:

1. تحديد الخلايا لقفلها: حدد الخلايا التي تريد قفلها. إذا كنت تريد قفل الورقة بأكملها، يمكنك تخطي هذه الخطوة.
1. فتح حوار تنسيق الخلايا: انقر بزر الماوس الأيمن على الخلايا المحددة واختر "تنسيق الخلايا"، أو اضغط على Ctrl+1.
<br>
<img src="1.png" width=60% />
1. قفل الخلايا: في مربع حوار تنسيق الخلايا، انتقل إلى علامة التبويب "الحماية". ضع علامة في خانة "مقفول". انقر "موافق".
1. حماية ورقة العمل: انتقل إلى علامة التبويب "مراجعة" على الشريط. انقر على "حماية الورقة". ضع كلمة مرور (اختياري) واختر الأذونات التي ترغب في السماح بها (مثل اختيار الخلايا المقفلة، تنسيق الخلايا، وهلم جرا). انقر "موافق".
<br>
<img src="2.png" width=60% />

## **كيفية قفل الخلايا لحمايتها باستخدام JavaScript**

Aspose.Cells مكتبة قوية للعمل مع ملفات Excel برمجيًا. لفتح الخلايا باستخدام Aspose.Cells for JavaScript عبر C++، عليك اتباع هذه الخطوات: تحميل [ملف عينة](sample.xlsx)، فك قفل جميع الخلايا أولاً (نظرًا لأنه بشكل افتراضي، كل الخلايا مقفلة ولكن لا يُطبق الحظر إلا عند حماية ورقة العمل)، ثم قفل الخلايا المحددة التي تريد حمايتها، وأخيراً حماية ورقة العمل لفرض القفل.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Protect Worksheet Example</title>
    </head>
    <body>
        <h1>Protect Worksheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, StyleFlag, ProtectionType } = AsposeCells;

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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Unlock all cells first
            const unlockStyle = workbook.createStyle();
            unlockStyle.isLocked = false;

            const styleFlag = new StyleFlag();
            styleFlag.locked = true;
            sheet.cells.applyStyle(unlockStyle, styleFlag);

            // Lock specific cells (e.g., A1 and B2)
            const lockStyle = workbook.createStyle();
            lockStyle.isLocked = true;

            sheet.cells.get("A1").style = lockStyle;
            sheet.cells.get("B2").style = lockStyle;

            // Protect the worksheet to enforce the locking
            sheet.protect(ProtectionType.All);

            // Save the modified workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_locked.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Locked Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Worksheet protected and cells locked successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


## **نتيجة الإخراج**
تضمن هذه الشفرة قفل الخلايا المحددة فقط (A1 و B2 في هذا المثال)، ويتم حماية ورقة العمل لتطبيق هذه الإعدادات. تبقى جميع الخلايا الأخرى في ورقة العمل غير مقفلة وقابلة للتحرير.

<br>
<img src="3.png" width=60% />

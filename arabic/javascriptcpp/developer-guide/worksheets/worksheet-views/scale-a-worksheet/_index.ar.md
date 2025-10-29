---
title: كيفية قياس حجم ورقة العمل باستخدام JavaScript عبر C++
linktitle: كيفية تكبير ورقة عمل
type: docs
weight: 130
url: /ar/javascript-cpp/how-to-scale-a-worksheet/
description: تُظهر لك هذه المقالة رمز يوضح كيفية قياس حجم ورقة العمل باستخدام Aspose.Cells for JavaScript عبر C++.
keywords: قياس ورقة عمل باستخدام JavaScript، كيفية قياس ورقة عمل باستخدام JavaScript عبر C++، قياس ورقة عمل في JavaScript عبر C++.
---

## **سيناريوهات الاستخدام المحتملة**
قد يكون تكبير ورقة العمل مفيدًا لأسباب متعددة، اعتمادًا على السياق الذي تعمل فيه. إليك بعض الأسباب الشائعة لتكبير ورقة العمل:
1. ملاءمة الصفحة: لضمان أن يتناسب كل المحتوى على صفحة واحدة أو عدد معين من الصفحات عند الطباعة، مما يسهل قراءتها وإدارتها بدون الحاجة للتنقل بين صفحات متعددة.

1. العرض التقديمي: لجعل ورقة العمل تبدو أكثر تنظيمًا ومهنية، خاصة عند مشاركتها مع الآخرين في الاجتماعات أو التقارير.

1. القابلية للقراءة: لضبط حجم النص والعناصر الأخرى لتحسين قابلية القراءة، خاصة للأشخاص الذين يواجهون صعوبة في قراءة الخطوط الصغيرة.

1. إدارة المساحات: لتحسين استخدام المساحة في ورقة العمل، مع ضمان عدم وجود مساحة بيضاء غير ضرورية وأن تكون جميع المعلومات المهمة مرئية دون تصفح مفرط.

1. تصور البيانات: في حالة الرسوم البيانية والجداول، يمكن أن يساعد الت scaling في جعلها أكثر قابلية للفهم من خلال تعديل حجمها لتتناسب مع المساحة المتاحة بشكل مناسب.

1. الاتساق: للحفاظ على مظهر وإحساس متناسق عبر عدة أوراق عمل أو مستندات، وهو أمر مهم بشكل خاص في البيئات المهنية والتعليمية.

## **كيفية تكبير ورقة عمل في Excel**
يمكن أن يساعد تكبير ورقة عمل في Excel على ملء المحتوى صفحة واحدة أو عدد محدد من الصفحات عند الطباعة. إليك خطوات تكبير ورقة العمل:

1. افتح ورقة العمل الخاصة بك: افتح ورقة العمل Excel التي تريد تكبيرها.

1. اذهب إلى علامة التبويب تخطيط الصفحة: انقر على التبويب تخطيط الصفحة في الشريط.

1. مجموعة التناسب مع الصفحات: في تبويب تخطيط الصفحة، ابحث عن مجموعة التناسب مع الصفحات. هنا لديك خيارات لضبط مقياس الت scaling. العرض: يتيح لك هذا الخيار تحديد عدد الصفحات بعرض الصفحة المطبوعة. الارتفاع: يتيح لك تحديد عدد الصفحات بارتفاع الصفحة المطبوعة. الت scaling: يمكنك أيضًا تحديد نسبة مئوية مخصصة للت scaling هنا.
<br>
<img src="1.png" width=60% />

1. ضبط العرض والارتفاع: اضبط العرض والارتفاع إلى العدد المطلوب من الصفحات. على سبيل المثال، ضعهما على صفحة واحدة إذا كنت تريد أن تتناسب الورقة مع صفحة واحدة.

1. ضبط نسبة الت scaling (إذا لزم الأمر): إذا كنت تفضل تحديد نسبة مئوية معينة للت scaling، قم بضبط مربع الت scaling. على سبيل المثال، ضبطها إلى 50% سيجعل كل شيء نصف الحجم.


## **كيفية تعديل مقياس ورقة عمل باستخدام جافا سكريبت عبر ++C**
Aspose.Cells for JavaScript عبر ++C مكتبة قوية للعمل مع ملفات إكسل برمجياً. لتغيير مقياس ورقة العمل باستخدام Aspose.Cells، عليك اتباع الخطوات التالية: تحميل [ملف عينة](sample.xlsx) وضبط إعدادات الطباعة بحيث تتناسب المحتويات مع العدد المطلوب من الصفحات أو نسبة مئوية معينة من الحجم الأصلي.

### **مثال: التناسب مع الصفحة**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Fit To Page Example</title>
    </head>
    <body>
        <h1>Fit Worksheet to One Page</h1>
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

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Access the PageSetup object
            const pageSetup = sheet.pageSetup;

            // Set the worksheet to fit to 1 page wide and 1 page tall
            pageSetup.fitToPagesWide = 1;
            pageSetup.fitToPagesTall = 1;

            // Saving the modified workbook and providing a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_fit_to_page.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet fitted to one page. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
<br>
<img src="3.png" width=60% />

### **مثال: التمدد إلى نسبة مئوية**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Scale Worksheet</title>
    </head>
    <body>
        <h1>Scale Worksheet Example</h1>
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

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Access the PageSetup object
            const pageSetup = sheet.pageSetup;

            // Set the scaling to a specific percentage (e.g., 75%)
            pageSetup.zoom = 75;

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_scaled_percentage.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Scaled Workbook';

            document.getElementById('result').innerHTML = '<p style="color: green;">Scaling applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
<br>
<img src="2.png" width=60% />

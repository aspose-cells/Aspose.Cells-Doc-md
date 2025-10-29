---
title: تطبيق التنسيق الشرطي في الأوراق العمل
linktitle: تطبيق التنسيق الشرطي في الأوراق العمل
description: كيفية استخدام مكتبة Aspose.Cells في جافا سكريبت عبر C++ لتطبيق التنسيق الشرطي في أوراق العمل للتحكم بشكل أفضل في مظهر الخلية.
keywords: Aspose.Cells، التنسيق الشرطي، جافا سكريبت عبر C++، ورقة العمل، التنسيق
type: docs
weight: 130
url: /ar/javascript-cpp/apply-conditional-formatting-in-worksheets/
---

{{% alert color="primary" %}}

يهدف هذا المقال إلى توفير فهم مفصل حول كيفية إضافة التنسيق الشرطي إلى مجموعة من الخلايا في ورقة عمل.

التنسيق الشرطي هو ميزة متقدمة في Microsoft Excel تسمح لك بتطبيق التنسيقات على مجموعة من الخلايا وأن يتغير ذلك التنسيق اعتمادًا على قيمة الخلية أو قيمة صيغة. على سبيل المثال، يمكن أن تكون خلفية الخلية حمراء لتسليط الضوء على قيمة سالبة، أو يمكن أن لون النص يكون أخضرًا لقيمة موجبة. عندما تفي قيمة الخلية بشرط التنسيق، يتم تطبيق التنسيق. إذا لم تف بقيمة الخلية شرط التنسيق، يتم استخدام التنسيق الافتراضي للخلية.

من الممكن تطبيق التنسيق الشرطي بواسطة Office Automation، ولكن ذلك يأتي مع عيوبه. هناك أسباب وقضايا عديدة متضمنة: مثلاً، الأمان، الاستقرار، التوسع السريع والسرعة. السبب الرئيسي للبحث عن حل آخر هو أن Microsoft نفسها تنص بشدة على عدم استخدام Office Automation لحلول البرنامج.

يعرض هذا المقال كيفية إنشاء تطبيق ويب، وإضافة تنسيق شرطي على الخلايا بقليل من الأكواد باستخدام واجهة برمجة تطبيقات Aspose.Cells.

{{% /alert %}}

## **استخدام Aspose.Cells لتطبيق تنسيق مشروط بناءً على قيمة الخلية**

1. **قم بتنزيل وتثبيت Aspose.Cells**.
   1. قم بتنزيل Aspose.Cells for JavaScript عبر C++.
1. قم بتثبيته على كمبيوتر التطوير الخاص بك.
   جميع مكونات Aspose، عند التثبيت، تعمل في وضع التقييم. وضع التقييم لا يحتوي على حد زمني ويقوم فقط بحقن العلامات المائية إلى الوثائق المنتجة.
1. **إنشاء مشروع**.
   ابدأ مشروع جافا سكريبت الخاص بك عن طريق تهيئته. يوضح هذا المثال الاستخدام في تطبيق ويب يستند إلى المتصفح.
1. **إضافة المراجع**.
   أضف مرجعًا إلى مكتبة Aspose.Cells لمشروعك، على سبيل المثال عن طريق تضمين المكتبة على النحو التالي:
   ```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Conditional Formatting Example</title>
    </head>
    <body>
        <h1>Apply Conditional Formatting Based on Cell Value</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FormatConditionType, OperatorType, CellArea, Color } = AsposeCells;

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

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Add conditional formatting collection
            const cfCollection = worksheet.conditionalFormattings;
            const idx = cfCollection.add();
            const formatConditionCollection = cfCollection.get(idx);

            // Define the cell area to apply conditional formatting (A1)
            const area = CellArea.createCellArea(0, 0, 0, 0); // fromRow, fromCol, toRow, toCol
            formatConditionCollection.addArea(area);

            // Add a condition: Cell Value > 100
            const conditionIndex = formatConditionCollection.addCondition(
                FormatConditionType.CellValue,
                OperatorType.Greater,
                "100",
                null
            );

            const formatCondition = formatConditionCollection.get(conditionIndex);

            // Modify the style for the condition: bold and red font
            const style = formatCondition.style;
            if (!style.font) {
                style.font = {};
            }
            style.font.bold = true;
            style.font.color = Color.fromArgb(255, 255, 0, 0); // ARGB red

            // Assign modified style back (property assignment pattern)
            formatCondition.style = style;

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'conditional_formatting_result.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conditional formatting applied to cell A1 (value &gt; 100). Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

عند تنفيذ الكود أعلاه، يُطبق التنسيق الشرطي على الخلية “A1” في ورقة العمل الأولى من ملف الإخراج (output.xls). يعتمد التنسيق الشرطي المطبق على A1 على قيمة الخلية. إذا كانت قيمة A1 بين 50 و100، يكون لون الخلفية أحمر بسبب التنسيق الشرطي المطبق.

## **استخدام Aspose.Cells لتطبيق التنسيق الشرطي بناءً على الصيغة**

1. تطبيق التنسيق الشرطي اعتمادًا على الصيغة (كود مصغر)
   أدناه هو الكود لإنجاز المهمة. يتم تطبيق التنسيق الشرطي على B3.

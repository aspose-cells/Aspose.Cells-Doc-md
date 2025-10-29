---
title: التحويل بين اسم الخلية ومؤشر الصف / العمود
linktitle: تحويل اسم الخلية ومؤشرها
type: docs
weight: 10
url: /ar/javascript-cpp/names-and-indices/
description: تعلم كيفية الحصول على تحويل بين اسم الخلية وفهرس الصف/العمود عبر Aspose.Cells for JavaScript باستخدام واجهة برمجة التطبيقات C++.
keywords: JavaScript عبر C++ الحصول على اسم الخلية من فهارس الصف والعمود، الحصول على فهارس الصف والعمود من اسم الخلية، إنشاء أسماء أوراق عمل آمنة، إضافة أسماء أوراق عمل آمنة
---

## **الحصول على اسم الخلية من مؤشرات الصف والعمود**
من الممكن العثور على اسم الخلية مع الاعتماد على مؤشرات الصف والعمود. يشرح هذا المقال كيفية ذلك.
يقدم برنامج Aspose.Cells for JavaScript باستخدام C++ طريقة CellsHelper.cellIndexToName التي تسمح للمطورين بالحصول على اسم الخلية إذا قاموا بتوفير فهرس الصف والعمود.

{{% alert color="primary" %}} 

يبدأ Microsoft Excel في عد فهارس الصفوف والأعمدة من 1. على عكس Microsoft Excel، يبدأ برنامج Aspose.Cells for JavaScript باستخدام C++ العد من 0.

{{% /alert %}} 

 يوضح الكود التجريبي التالي كيفية استخدام CellsHelper.cellIndexToName للوصول إلى اسم الخلية استنادًا إلى مؤشرات صف وعمود معروفين. ينتج عن الكود المخرجات التالية.



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
            // Original logic converted to browser JavaScript
            var row = 3;
            var column = 5;
            var name = AsposeCells.CellsHelper.cellIndexToName(row, column);
            console.log("Cell name: " + name);
            document.getElementById('result').innerHTML = '<p>Cell name: ' + name + '</p>';
        });
    </script>
</html>
```
## **الحصول على فهارس الصفوف والأعمدة من اسم الخلية**
من الممكن العثور على فهرس الصف والعمود للخلية من اسمها. يشرح هذا المقال كيفية ذلك.
يقدم برنامج Aspose.Cells for JavaScript باستخدام C++ طريقة CellsHelper.cellNameToIndex التي تسمح للمطورين بالحصول على فهرس الصف والعمود من اسم الخلية.

{{% alert color="primary" %}} 

يبدأ Microsoft Excel في عد فهارس الصفوف والأعمدة من 1. على عكس Microsoft Excel، يبدأ برنامج Aspose.Cells for JavaScript باستخدام C++ العد من 0.

{{% /alert %}} 

 يوضح الكود التجريبي التالي كيفية استخدام CellsHelper.cellNameToIndex للحصول على مؤشر الصف والعمود من اسم الخلية. ينتج عن الكود المخرجات التالية.



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Get Row and Column from Cell Name</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <div>
            <label for="cellName">Cell Name:</label>
            <input type="text" id="cellName" value="C4" />
        </div>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellsHelper } = AsposeCells;

        let asposeInitialized = false;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            asposeInitialized = true;
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', () => {
            if (!asposeInitialized) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Aspose.Cells is not initialized yet. Please wait and try again.</p>';
                return;
            }

            const name = document.getElementById('cellName').value || "C4";

            const rowCol = CellsHelper.cellNameToIndex(name);
            const currRow = rowCol[0];
            const currCol = rowCol[1];
            console.log("Row: " + currRow + " , Column: " + currCol);

            document.getElementById('result').innerHTML = `<p>Row: ${currRow} , Column: ${currCol}</p>`;
        });
    </script>
</html>
```

## **إنشاء أسماء صفحات آمنة**
في بعض الأحيان، هناك حاجة لتعيين اسم الورقة أثناء التشغيل. في هذا السيناريو، قد تحتوي أسماء الأوراق على بعض الأحرف الإضافية مثل <>+(؟. هناك حاجة لاستبدال أي من هذه الأحرف غير المسموح بها كاسم ورقة بحرف محدد مسبقًا يقدمه المستخدم. بالمثل، قد يزيد الطول عن 31 حرفًا ويجب قطعه. يوفر Apache POI ميزات لإنشاء أسماء آمنة، لذلك يتم توفير ميزة مماثلة بواسطة Aspose.Cells for JavaScript باستخدام C++ لمعالجة كل هذه المشكلات. يظهر الكود النموذجي التالي هذه الميزة:



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Create Safe Sheet Name</title>
    </head>
    <body>
        <h1>Create Safe Sheet Name Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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

        document.getElementById('runExample').addEventListener('click', () => {
            // Long name will be truncated to 31 characters
            var name1 = AsposeCells.CellsHelper.createSafeSheetName("this is first name which is created using CellsHelper.CreateSafeSheetName and truncated to 31 characters");

            // Any invalid character will be replaced with _
            var name2 = AsposeCells.CellsHelper.createSafeSheetName(' <> + (adj.Private ? " Private" : ")', '_');

            // Display results in the page
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '<p><strong>Safe Name 1:</strong> ' + name1 + '</p>' +
                                  '<p><strong>Safe Name 2:</strong> ' + name2 + '</p>';
        });
    </script>
</html>
```

الإخراج:

هذا هو الاسم الأول الذي تم إنشاؤه

` `<> + (adj.Private _ " خاص"

---
title: الوصول إلى خلايا ورقة العمل
type: docs
weight: 10
url: /ar/javascript-cpp/accessing-cells-of-a-worksheet/
description: توضح هذه المقالة كيفية الحصول على نطاق العرض الأقصى لورقة العمل والوصول إلى الخلايا من خلال API الخاص بـ Aspose.Cells for JavaScript عبر C++.
keywords: الحصول على كائن الخلية، الوصول إلى الخلايا، الحصول على النطاق الأقصى لعرض ورقة العمل. 
---

{{% alert color="primary" %}}

نعلم أن جميع أوراق العمل قد تحتوي على بيانات مخزنة بشكل أساسي في الخلايا (التي تتكون منها ورقة العمل). الخلية هي جزء أساسي من ورقة العمل تُستخدم لبناء كامل ورقة العمل كسلسلة من الصفوف والأعمدة. قبل محاولة الوصول إلى البيانات من ورقة العمل، نحتاج إلى الوصول إلى خلاياها. لذا، في هذا الموضوع، سنناقش بعض الأساليب الأساسية للوصول إلى خلايا ورقة العمل وقت التشغيل باستخدام Aspose.Cells for JavaScript عبر C++.

{{% /alert %}}

## **كيفية الوصول إلى الخلايا**

يقدم Aspose.Cells for JavaScript عبر C++ فئة، [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) التي تمثل ملف إكسل. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) على [**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection) تتيح الوصول إلى كل ورقة عمل في ملف إكسل. تمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) مجموعة [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) التي تمثل جميع الخلايا في ورقة العمل.

يمكننا استخدام مجموع [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) للوصول إلى الخلايا في ورقة العمل. يوفر Aspose.Cells for JavaScript عبر C++ ثلاث طرق أساسية للوصول إلى الخلايا في ورقة العمل:

1. باستخدام اسم الخلية.
1. باستخدام فهرس صف الخلية والعمود.
1. باستخدام فهرس الخلية في مجموعة [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)

 لقد ذكرنا أن الطريقة الثالثة هي الأسرع والطريقة الأولى هي الأبطأ. الفرق في الأداء بين الطرق ضئيل جدًا لذا لا تقلق بشأن تدهور الأداء، مهما كانت الطريقة التي تستخدمها.

### **كيفية الحصول على كائن الخلية باسم الخلية**

يمكن للمطورين الوصول إلى أي خلية محددة عن طريق تمرير اسم خلية إلى تجميع [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) من فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) كفهرس.

إذا قمت بإنشاء ورقة عمل فارغة في البداية، فإن عدد تجميع [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) يكون صفرًا. عند استخدامك لهذه الطريقة للوصول إلى خلية، سيقوم النظام بالتحقق مما إذا كانت تلك الخلية موجودة في التجميع أم لا. إذا كانت موجودة، يرجع كائن الخلية من التجميع، وإلا، يقوم بإنشاء كائن [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) جديد، يضيفه إلى التجميع [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) ثم يرجع الكائن. هذه هي أبسط طريقة للوصول إلى الخلية إذا كنت معتادًا على Microsoft Excel، لكنها الأبطأ مقارنة بالطرق الأخرى.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Read Cell Example</h1>
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Using the first worksheet in the workbook
            const worksheet = workbook.worksheets.get(0);

            // Accessing a cell using its name
            const cell = worksheet.cells.get("A1");

            // Output the cell's string value to the page
            document.getElementById('result').innerHTML = `<p>Cell A1 value: ${cell.stringValue}</p>`;
        });
    </script>
</html>
```

### **كيفية الحصول على كائن الخلية باستخدام مؤشر صف وعمود الخلية**

يمكن للمطورين الوصول إلى أي خلية محددة عن طريق تمرير مؤشرات صفها وعمودها إلى تجميع [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) من فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet).

يعمل هذا النهج بنفس الطريقة كطريقة الوصول الأولى.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Read Cell Value</h1>
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
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Using the first worksheet in workbook
            const worksheet = workbook.worksheets.get(0);

            // Accessing a cell using its row and column (A1 -> 0,0)
            const cell = worksheet.cells.get(0, 0);

            // Printing the string value of the cell
            const value = cell.stringValue;
            console.log(value);
            resultDiv.innerHTML = `<p>Cell A1 value: ${value}</p>`;
        });
    </script>
</html>
```

### **كيفية الحصول على كائن الخلية باستخدام فهرس الخلية في مجموعة الخلايا**

يمكن الوصول إلى الخلية أيضًا عن طريق تمرير مؤشرها الرقمي إلى تجميع [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells).

إذا استخدمت هذه الطريقة للوصول إلى الخلايا، قد يتم إطلاق استثناء إذا كان مؤشر الخلية الرقمي خارج النطاق. هذه الطريقة هي الأسرع للوصول إلى الخلايا، ولكن من المهم أن تعرف أن استخدام هذه الطريقة للوصول إلى كائن خلية قد يتغير مؤشرها بعد إضافة خلايا جديدة إلى تجميع [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells). الخلايا في التجميع [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) مرتبة داخليًا حسب مؤشرات الصف والعمود.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Read Cell String Value</h1>
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
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Using the Sheet 1 in Workbook
            const worksheet = workbook.worksheets.get(0);

            // Accessing a cell using its row and column.
            const cell = worksheet.cells.get(0, 0);

            // Output the string value of the cell
            console.log(cell.stringValue);
            resultDiv.innerHTML = `<p>Cell (0,0) string value: <strong>${cell.stringValue}</strong></p>`;
        });
    </script>
</html>
```

## **كيفية الحصول على النطاق الأقصى لعرض ورقة العمل**

يسمح Aspose.Cells for JavaScript عبر C++ للمطورين بالوصول إلى أقصى نطاق عرض لورقة العمل. النطاق الأقصى للعرض — وهو نطاق الخلايا بين أول وآخر خلية تحتوي على محتوى — مفيد عندما تحتاج إلى نسخ، أو تحديد، أو عرض المحتوى الكامل لورقة العمل في صورة.

يمكنك الوصول إلى النطاق الأقصى للعرض لورقة العمل باستخدام [**Cells.maxDisplayRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDisplayRange--). يوضح الرمز النموذجي التالي كيفية الوصول إلى الخاصية [**maxDisplayRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDisplayRange--).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            // Ensure Aspose.Cells is initialized
            await AsposeCells.onReady();

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet in the workbook
            const worksheet = workbook.worksheets.get(0);

            // Access the Maximum Display Range
            const range = worksheet.cells.maxDisplayRange;

            // Print / display the Maximum Display Range RefersTo property
            const refersTo = range.refersTo;
            resultDiv.innerHTML = `<p style="color: green;">Maximum Display Range: ${refersTo}</p>`;
        });
    </script>
</html>
```

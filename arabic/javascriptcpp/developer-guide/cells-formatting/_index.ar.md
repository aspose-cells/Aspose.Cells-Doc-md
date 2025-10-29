---
title: توسيع الخلايا باستخدام JavaScript عبر C++
description: تعلم كيفية تنسيق وتنسيق الخلايا في 8667720447سكربت عبر C++، بما في ذلك تنسيق الأرقام، وتنسيق التاريخ، وأنماط الخطوط، وخيارات نمط الخلايا الأخرى. دليلنا سيساعدك على إنشاء جداول بيانات جذابة واحترافية المظهر.
keywords: 8667720447سكربت عبر C++، تنسيق الخلايا، التجميل، تنسيق الأرقام، تنسيق التاريخ، نمط الخط، خيارات نمط الخلايا، جدول بيانات، إنشاء، مظهر احترافي، تنسيق الصفوف والأعمدة.
linktitle: تنسيق الخلايا
type: docs
weight: 120
url: /ar/javascript-cpp/cells-formatting/
---

## **مقدمة**

{{% alert color="primary" %}}

توفر Aspose.Cells الطرق [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) و [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-) من فئة [Cell](https://reference.aspose.com/cells/javascript-cpp/cell)، المستخدمة للحصول على/ضبط نمط تنسيق خلية. كما توفر Aspose.Cells فئة [**Style**](https://reference.aspose.com/cells/javascript-cpp/style).

{{% /alert %}}

## **كيفية تنسيق الخلايا باستخدام طرق النمط**

تطبيق أنواع مختلفة من أنماط التنسيق على الخلايا لتعيين ألوان الخلفية أو الأمامية، الحدود، الخطوط، المحاور الأفقية والعمودية، مستوى المسافة البادئة، اتجاه النص، زاوية الدوران والمزيد.

### **كيفية استخدام طرق النمط**

إذا كان المطورون بحاجة إلى تطبيق أنماط تنسيق مختلفة على خلايا مختلفة، فمن الأفضل استرجاع [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) للخلية عبر طريقة [**Cell.style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--)، تحديد سمات النمط، ثم تطبيق التنسيق باستخدام طريقة [**Cell.style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-). يُعطى المثال أدناه ليوضح هذا النهج لتطبيق تنسيقات متنوعة على خلية.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Styling Example</h1>
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

            // Instantiate or load workbook
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Hello Aspose!";

            // Defining a Style object
            let style;

            // Get the style from A1 cell
            style = cell.style;

            // Setting the vertical alignment
            style.verticalAlignment = AsposeCells.TextAlignmentType.Center;

            // Setting the horizontal alignment
            style.horizontalAlignment = AsposeCells.TextAlignmentType.Center;

            // Setting the font color of the text
            style.font.color = AsposeCells.Color.Green;

            // Setting to shrink according to the text contained in it
            style.shrinkToFit = true;

            // Setting the bottom border color to red
            style.borders.get(AsposeCells.BorderType.BottomBorder).color = AsposeCells.Color.Red;

            // Setting the bottom border type to medium
            style.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Medium;

            // Applying the style to A1 cell
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **كيفية استخدام كائن النمط لتنسيق خلايا مختلفة**

إذا كان المطورون بحاجة إلى تطبيق نمط تنسيق نفسه على خلايا مختلفة، يمكنهم استخدام كائن [**Style**](https://reference.aspose.com/cells/javascript-cpp/style). يرجى اتباع الخطوات أدناه لاستخدام كائن [**Style**](https://reference.aspose.com/cells/javascript-cpp/style):

1. أضف كائن [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) عن طريق استدعاء طريقة [**createStyle()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#createStyle--) الخاصة بفئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)
2. الوصول إلى كائن [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) المضاف حديثًا
3. تعيين الخصائص/السمات المرغوبة لكائن [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) لتطبيق الإعدادات التنسيقية المطلوبة
4. تعيين كائن [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) المُعدّل للخلايا المرغوبة

يمكن أن يحسن هذا النهج بشكل كبير كفاءة تطبيقاتك ويوفر ذاكرة أيضًا.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Style Cells</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TextAlignmentType, Color, BorderType, CellBorderType } = AsposeCells;

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
            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Add a new worksheet to the workbook
            const i = workbook.worksheets.add();

            // Obtain the newly added worksheet by index
            const worksheet = workbook.worksheets.get(i);

            // Access cell A1
            const cell = worksheet.cells.get("A1");

            // Set value of A1
            cell.value = "Hello Aspose!";

            // Create a new style
            const style = workbook.createStyle();

            // Set vertical and horizontal alignment
            style.verticalAlignment = TextAlignmentType.Center;
            style.horizontalAlignment = TextAlignmentType.Center;

            // Set font color
            style.font.color = Color.Green;

            // Shrink to fit
            style.shrinkToFit = true;

            // Set bottom border color and style
            style.borders.get(BorderType.BottomBorder).color = Color.Red;
            style.borders.get(BorderType.BottomBorder).lineStyle = CellBorderType.Medium;

            // Apply style to A1
            cell.style = style;

            // Apply same style to B1, C1, D1
            worksheet.cells.get("B1").style = style;
            worksheet.cells.get("C1").style = style;
            worksheet.cells.get("D1").style = style;

            // Save workbook to XLS format and provide download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and styled successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

### **كيفية استخدام أنماط Microsoft Excel 2007 المحددة مسبقًا**

إذا كنت بحاجة لتطبيق أنماط تنسيق مختلفة لـ Microsoft Excel 2007، فقم بتطبيق الأنماط باستخدام واجهة برمجة التطبيقات Aspose.Cells. يُظهر المثال التالي هذا النهج لتطبيق نمط محدد مسبقًا على خلية.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create Workbook and Set Cell Style Example</h1>
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
            // Instantiate a new Workbook.
            const workbook = new Workbook();

            // Create a style object.
            const style = workbook.createStyle();

            // Access the first worksheet in the workbook
            const worksheet = workbook.worksheets.get(0);

            // Access cell A1
            const cell = worksheet.cells.get("A1");

            // Input a value to A1 cell.
            cell.putValue("Test");

            // Apply the style to the cell.
            cell.style = style;

            // Saving the Excel 2007 file.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```



## **كيفية تنسيق الأحرف المحددة في خلية**

تشرح التعامل مع إعدادات الخط كيفية تنسيق النص في الخلايا، لكنها تشرح فقط كيفية تنسيق كل مضمون الخلية. ماذا إذا كنت ترغب في تنسيق الأحرف المحددة فقط؟

يدعم Aspose.Cells هذه الميزة أيضًا. يوضح هذا الموضوع كيفية استخدام هذه الميزة بشكل فعال.

### **كيفية تنسيق الأحرف المحددة**

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) التي تمثل ملف إكسل من Microsoft. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) على مجموعة [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) التي تتيح الوصول إلى كل ورقة عمل في ملف إكسل. تمثل الورقة بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) مجموعة [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--). يمثل كل عنصر في مجموعة [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) كائن من فئة [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell).

تقدم فئة [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) طريقة [**characters(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-number-number-) التي تستقبل المعلمات التالية لاختيار نطاق من الأحرف داخل خلية:

- **فهرس البداية**, وهو فهرس الحرف الذي يبدأ منه التحديد.
- **عدد الحروف**, عدد الأحرف المراد تحديدها.

تعيد طريقة [**characters(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-number-number-) نسخة من فئة [**FontSetting**](https://reference.aspose.com/cells/javascript-cpp/fontsetting) التي تسمح للمطورين بتنسيق الأحرف بنفس طريقة تنسيق خلية كما هو موضح أدناه في مثال التعليمات البرمجية. في الملف الناتج، في خلية A1، سيتم تنسيق كلمة 'Visit' باستخدام الخط الافتراضي ولكن 'Aspose!' بخط عريض وأزرق.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
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

            // If a file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files && fileInput.files.length > 0) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first (default) worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(0);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Visit Aspose!";

            // Setting the font of selected characters to bold and color to blue
            const charRange = cell.characters(6, 7);
            charRange.font.isBold = true;
            charRange.font.color = AsposeCells.Color.Blue;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

إذا كنت مهتمًا بتنسيق جزء من النص الغني في خلية، فكر في استخدام طريقتي [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters--) و [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-fontsettingarray-). تُستخدم طريقة [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters--) للوصول إلى أجزاء النص، ثم يمكن إجراء التعديلات باستخدام طريقة [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-fontsettingarray-)، بينما تُرجع طريقة **Get** مصفوفة من كائنات [**FontSetting**](https://reference.aspose.com/cells/javascript-cpp/fontsetting) يمكن التلاعب بها لكي تعيين خصائص مختلفة مثل اسم الخط، لون الخط، العريض، إلى آخره، ويمكن استخدام طريقة **Set** لتطبيق التغييرات.

{{% /alert %}}

## **كيفية تنسيق الصفوف والأعمدة**

في بعض الأحيان، يحتاج المطورون إلى تطبيق نفس التنسيق على الصفوف أو الأعمدة. تطبيق التنسيق على الخلايا واحدة تلو الأخرى غالبًا ما يستغرق وقتا أطول وليس حلا جيدًا.
لحل هذه المشكلة، يوفر Aspose.Cells طريقة بسيطة وسريعة يتم مناقشتها بالتفصيل في هذا المقال.

### **تنسيق الصفوف والأعمدة**

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) التي تمثل ملف إكسل من Microsoft. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) على مجموعة [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) تتيح الوصول إلى كل ورقة عمل في ملف إكسل. تمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). تقدم فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) مجموعة [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--). توفر مجموعة [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) مجموعة [**rows**](https://reference.aspose.com/cells/javascript-cpp/cells/#rows--).

### **كيفية تنسيق صف**

كل عنصر في مجموعة [**rows**](https://reference.aspose.com/cells/javascript-cpp/cells/#rows--) يمثل كائن [**Row**](https://reference.aspose.com/cells/javascript-cpp/row). يوفر كائن [**Row**](https://reference.aspose.com/cells/javascript-cpp/row) طريقة [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/javascript-cpp/row/#applyStyle-style-styleflag-) المستخدمة لضبط تنسيق الصف. لتطبيق التنسيق نفسه على صف، استخدم كائن [**Style**](https://reference.aspose.com/cells/javascript-cpp/style). تظهر الخطوات أدناه كيفية استخدامه.

1. أضف كائن [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) إلى فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) عن طريق استدعاء طريقة [**createStyle()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#createStyle--).
2. تعيين خصائص كائن [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) لتطبيق إعدادات التنسيق.
3. تفعيل السمات ذات الصلة على كائن [**StyleFlag**](https://reference.aspose.com/cells/javascript-cpp/styleflag).
4. تعيين كائن [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) المُعدّل إلى كائن [**Row**](https://reference.aspose.com/cells/javascript-cpp/row).

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
            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Obtaining the reference of the first (default) worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(0);

            // Adding a new Style to the styles
            const style = workbook.createStyle();

            // Setting the vertical alignment of the text in the "A1" cell
            style.verticalAlignment = AsposeCells.TextAlignmentType.Center;

            // Setting the horizontal alignment of the text in the "A1" cell
            style.horizontalAlignment = AsposeCells.TextAlignmentType.Center;

            // Setting the font color of the text in the "A1" cell
            style.font.color = AsposeCells.Color.Green;

            // Shrinking the text to fit in the cell
            style.shrinkToFit = true;

            // Setting the bottom border color of the cell to red
            style.borders.get(AsposeCells.BorderType.BottomBorder).color = AsposeCells.Color.Red;

            // Setting the bottom border type of the cell to medium
            style.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Medium;

            // Creating StyleFlag
            const styleFlag = new AsposeCells.StyleFlag();
            styleFlag.horizontalAlignment = true;
            styleFlag.verticalAlignment = true;
            styleFlag.shrinkToFit = true;
            styleFlag.borders = true;
            styleFlag.fontColor = true;

            // Accessing a row from the Rows collection
            const row = worksheet.cells.rows.get(0);

            // Assigning the Style object to the Style property of the row
            row.applyStyle(style, styleFlag);

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **كيفية تنسيق عمود**

توفر مجموعة [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) أيضًا مجموعة [**columns**](https://reference.aspose.com/cells/javascript-cpp/cells/#columns--). يمثل كل عنصر في مجموعة [**columns**](https://reference.aspose.com/cells/javascript-cpp/cells/#columns--) كائن [**Column**](https://reference.aspose.com/cells/javascript-cpp/column). مماثل لكائن [**Row**](https://reference.aspose.com/cells/javascript-cpp/row)، توفر كائن [**Column**](https://reference.aspose.com/cells/javascript-cpp/column) أيضًا طريقة [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/javascript-cpp/row/#applyStyle-style-styleflag-) لتنسيق عمود.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Style and Column Apply Example</h1>
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
            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Obtain the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Add a new Style to the styles
            const style = workbook.createStyle();

            // Set vertical and horizontal alignment
            style.verticalAlignment = AsposeCells.TextAlignmentType.Center;
            style.horizontalAlignment = AsposeCells.TextAlignmentType.Center;

            // Set font color
            style.font.color = AsposeCells.Color.Green;

            // Shrink to fit
            style.shrinkToFit = true;

            // Set bottom border color and style
            style.borders.get(AsposeCells.BorderType.BottomBorder).color = AsposeCells.Color.Red;
            style.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Medium;

            // Create and configure StyleFlag
            const styleFlag = new AsposeCells.StyleFlag();
            styleFlag.horizontalAlignment = true;
            styleFlag.verticalAlignment = true;
            styleFlag.shrinkToFit = true;
            styleFlag.borders = true;
            styleFlag.fontColor = true;

            // Access first column and apply style
            const column = worksheet.cells.getColumns().get(0);
            column.applyStyle(style, styleFlag);

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Style applied to column successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **مواضيع متقدمة**
- [إعدادات المحاذاة](/cells/ar/javascript-cpp/cells-alignment-settings/)
- [إعدادات الحدود](/cells/ar/javascript-cpp/cells-border-settings/)
- [ضبط الصيغ الشرطية لملفات Excel وODS.](/cells/ar/javascript-cpp/conditional-formatting/)
- [ثيمات وألوان Excel](/cells/ar/javascript-cpp/excel-themes-and-colors/)
- [إعدادات التعبئة](/cells/ar/javascript-cpp/cells-fill-settings/)
- [إعدادات الخطوط](/cells/ar/javascript-cpp/cells-font-settings/)
- [تنسيق خلايا ورق عمل في بيان عمل](/cells/ar/javascript-cpp/format-worksheet-cells-in-a-workbook/)
- [تنفيذ نظام التاريخ 1904](/cells/ar/javascript-cpp/implement-1904-date-system/)
- [دمج وفصل الخلايا](/cells/ar/javascript-cpp/merging-and-unmerging-cells/)
- [إعدادات الأرقام](/cells/ar/javascript-cpp/cells-number-settings/)
- [الحصول على وتعيين النمط للخلايا](/cells/ar/javascript-cpp/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)

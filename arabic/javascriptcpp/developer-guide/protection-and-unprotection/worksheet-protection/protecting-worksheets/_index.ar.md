---
title: حماية أوراق العمل باستخدام جافا سكريبت عبر C++
linktitle: حماية الأوراق العمل
type: docs
weight: 10
url: /ar/javascript-cpp/protecting-worksheets/
description: تعلم كيفية حماية أوراق العمل في Excel باستخدام Aspose.Cells for JavaScript عبر C++، بما في ذلك حماية الصفوف والأعمدة وخلايا محددة.
---

{{% alert color="primary" %}}

عندما يتم حماية ورقة العمل، يتم تقييد الإجراءات التي يمكن للمستخدم اتخاذها. على سبيل المثال، لا يمكنهم إدخال بيانات، أو إدراج، أو حذف صفوف أو أعمدة، إلخ.

{{% /alert %}}

## **حماية الأوراق العمل**

### **مقدمة**

خيارات الحماية العامة في Microsoft Excel هي:

- المحتويات
- الكائنات
- السيناريوهات

لاتخفي أوراق العمل المحمية البيانات الحساسة أو تحميها ، لذا فإنها تختلف عن تشفير الملف. بشكل عام ، يعتبر حماية ورقة العمل مناسبة لأغراض العرض. فهي تمنع المستخدم النهائي من تعديل البيانات والمحتوى والتنسيق في ورقة العمل.

### **حماية ورقة العمل**

توفر Aspose.Cells فصل [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) الذي يمثل ملف Excel من Microsoft. يحتوي فصل [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) على مجموعة [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) تسمح بالوصول إلى كل ورقة عمل في ملف Excel. تمثل ورقة العمل بواسطة فصل [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet).

يوفر فصل [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) الطريقة [**protect(ProtectionType)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#protect-protectiontype-) التي تُستخدم لتطبيق الحماية على ورقة العمل. يقبل الأسلوب [**protect(ProtectionType)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#protect-protectiontype-) المعلمات التالية:

- نوع الحماية، نوع الحماية المطبقة على ورقة العمل. يتم تطبيق نوع الحماية بمساعدة تعداد [**ProtectionType**](https://reference.aspose.com/cells/javascript-cpp/protectiontype).
- كلمة المرور الجديدة ، كلمة المرور الجديدة المستخدمة لحماية ورقة العمل.
- كلمة المرور القديمة ، كلمة المرور السابقة ، إذا كانت ورقة العمل محمية بكلمة مرور بالفعل. إذا لم تكن ورقة العمل محمية بكلمة مرور بالفعل ، فقط قم بتمرير قيمة فارغة.

تحتوي تعداد [**ProtectionType**](https://reference.aspose.com/cells/javascript-cpp/protectiontype) على أنواع الحماية المعرفة مسبقًا التالية:

|**أنواع الحماية**|**الوصف**|
| :- | :- |
|All| لا يمكن للمستخدم تعديل أي شيء على هذه الورقة العمل|
|Contents| لا يمكن للمستخدم إدخال بيانات في هذه الورقة العمل|
|Objects| لا يمكن للمستخدم تعديل أجسام الرسم|
|Scenarios| لا يمكن للمستخدم تعديل السيناريوهات المحفوظة|
|Structure| لا يمكن للمستخدم تعديل الهيكل|
|Windows| تم تطبيق الحماية على النوافذ|
|None| لا يوجد تطبيق للحماية|

المثال أدناه يوضح كيفية حماية ورقة عمل بكلمة مرور.

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
        const { Workbook, SaveFormat, ProtectionType, Utils } = AsposeCells;

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

            // Ensure Aspose.Cells is initialized before proceeding
            await AsposeCells.onReady();

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object with file buffer
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Protecting the worksheet with a password
            worksheet.protect(ProtectionType.All, "aspose", null);

            // Saving the modified Excel file in Excel 97-2003 format
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet protected successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

بعد استخدام الكود أعلاه لحماية الورقة العمل، يمكنك التحقق من الحماية على الورقة العمل عن طريق فتحها. بمجرد فتح الملف ومحاولة إضافة بعض البيانات إلى الورقة العمل، ستظهر لك نافذة التالي:

|**تحذير الذي يظهر عندما لا يستطيع المستخدم تعديل الورقة العمل**|
| :- |
|![todo:image_alt_text](protecting-worksheets_1.png)|

للعمل على الورقة العمل، قم بإلغاء حمايتها عن طريق تحديد **Protection**، ثم **Unprotect Sheet** من عنصر القائمة **Tools**.

بعد اختيار عنصر القائمة Unprotect Sheet، ستفتح نافذة تطالبك بإدخال كلمة المرور حتى تتمكن من العمل على الورقة العمل كما هو موضح أدناه:

|![todo:image_alt_text](protecting-worksheets_2.png)|

### **حماية خلايا قليلة في الورقة العمل باستخدام Microsoft Excel**

قد تكون هناك سيناريوهات معينة حيث تحتاج إلى قفل بعض الخلايا فقط في ورقة العمل. إذا كنت تريد قفل خلايا معينة في ورقة العمل، عليك إلغاء قفل جميع الخلايا الأخرى في ورقة العمل. جميع الخلايا في ورقة العمل مهيأة بالفعل للقفل؛ يمكنك التحقق من ذلك بفتح أي ملف Excel في MS Excel والنقر على **Format | Cells...** لعرض مربع حوار **Format Cells** ثم النقر على علامة التبويب **Protection** ورؤية مربع اختيار "Locked" المحدد افتراضيًا.

تشير النقاط التالية إلى كيفية قفل بعض الخلايا باستخدام MS Excel. تنطبق هذه الطريقة على Microsoft Office Excel 97، 2000، 2002، 2003، والإصدارات الأحدث.

1. حدد الورقة العمل بأكملها بالنقر على زر **Select All** (المستطيل الرمادي مباشرة فوق رقم الصف للصف 1 وعند اليسار من حرف العمود A).
2. انقر على **Cells** في قائمة **Format**، ثم انتقل إلى علامة التبويب **Protection**، وقم بإلغاء تحديد مربع **Locked**.
   يفتح هذا جميع الخلايا على ورقة العمل خلاف ذلك.
   إذا كانت الأمر **Cells** غير متاح، فقد يكون بعض أجزاء الورقة العمل مقفلة بالفعل. في القائمة **Tools**، قم بتوجيه المؤشر إلى **Protection**، ثم انقر على **Unprotect Sheet**.
3. حدد فقط الخلايا التي تريد قفلها وكرر الخطوة 2، ولكن هذه المرة حدد خانة الاختيار **مقفلة**.
4. في قائمة **الأدوات**، اشاره إلى **ال protection**، انقر على **Protect Sheet** ثم انقر على **موافق**.
5. في مربع الحوار **حماية الورقة**، لديك خيار تحديد كلمة مرور وتحديد العناصر التي تريد أن يتمكن المستخدمون من تغييرها.

### **حماية بعض الخلايا في ورقة العمل باستخدام Aspose.Cells**

في هذه الطريقة، نستخدم واجهة برمجة التطبيقات Aspose.Cells فقط لأداء المهمة.

مثال: يعرض المثال التالي كيفية حماية بعض الخلايا في ورقة العمل. يفتح جميع الخلايا في ورقة العمل أولاً ثم يقفل 3 خلايا (A1، B1، C1) فيها. وأخيرًا، يحمي ورقة العمل. يحتوي كائن [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) على خاصية بوليانية، [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--). يمكنك تعيين الخاصية [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--) إلى true أو false وتطبيق طريقة *Column/Row.applyStyle()* لقفل أو فتح قفل الصف أو العمود بالسمات التي ترغب بها.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Unlock Columns and Protect Specific Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, StyleFlag, ProtectionType } = AsposeCells;

        const readyPromise = AsposeCells.onReady({
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
            await readyPromise;

            // Create a new workbook.
            const wb = new Workbook();

            // Create a worksheet object and obtain the first sheet.
            const sheet = wb.worksheets.get(0);

            // Define the style object.
            let style;

            // Define the styleflag object
            const styleflag = new StyleFlag();

            // Loop through all the columns in the worksheet and unlock them.
            for (let i = 0; i <= 255; i++) {
                style = sheet.cells.columns.get(i).style;
                style.isLocked = false;
                styleflag.locked = true;
                sheet.cells.columns.get(i).applyStyle(style, styleflag);
            }

            // Lock the three cells...i.e. A1, B1, C1.
            style = sheet.cells.get("A1").style;
            style.isLocked = true;
            sheet.cells.get("A1").style = style;

            style = sheet.cells.get("B1").style;
            style.isLocked = true;
            sheet.cells.get("B1").style = style;

            style = sheet.cells.get("C1").style;
            style.isLocked = true;
            sheet.cells.get("C1").style = style;

            // Finally, Protect the sheet now.
            sheet.protect(ProtectionType.All);

            // Save the excel file and provide download link
            const outputData = wb.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **حماية صف في ورقة العمل**

يسمح لك Aspose.Cells بقفل أي صف بسهولة في ورقة العمل. هنا، يمكننا استخدام طريقة [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/javascript-cpp/row/#applyStyle-style-styleflag-) من فئة [**Aspose.Cells.Row**](https://reference.aspose.com/cells/javascript-cpp/row) لتطبيق [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) على صف معين في ورقة العمل. تستقبل هذه الطريقة وسيطين: كائن [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) و [**StyleFlag**](https://reference.aspose.com/cells/javascript-cpp/styleflag) الذي يحتوي على جميع الأعضاء المتعلقة بالتنسيق المطبق.

يُظهر المثال التالي كيفية حماية صف في ورقة العمل. يفتح جميع الخلايا في ورقة العمل أولاً ثم يقفل الصف الأول فيها. وأخيرًا، يحمي ورقة العمل. يحتوي الكائن [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) على خاصية بوليانية، [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--). يمكنك تعيين الخاصية [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--) إلى true أو false لقفل أو فتح قفل الصف أو العمود باستخدام الكائن [**StyleFlag**](https://reference.aspose.com/cells/javascript-cpp/styleflag).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Protect Worksheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, StyleFlag, ProtectionType, Utils } = AsposeCells;

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
            // Create a new workbook.
            const wb = new Workbook();

            // Create a worksheet object and obtain the first sheet.
            const sheet = wb.worksheets.get(0);

            // Define the style object.
            let style;

            // Define the styleflag object.
            const flag = new StyleFlag();

            // Loop through all the columns in the worksheet and unlock them.
            for (let i = 0; i <= 255; i++) {
                style = sheet.cells.columns.get(i).style;
                style.isLocked = false;
                flag.locked = true;
                sheet.cells.columns.get(i).applyStyle(style, flag);
            }

            // Get the first row style.
            style = sheet.cells.rows.get(0).style;

            // Lock it.
            style.isLocked = true;

            // Set the lock setting.
            flag.locked = true;

            // Apply the style to the first row.
            sheet.cells.applyRowStyle(0, style, flag);

            // Protect the sheet.
            sheet.protect(ProtectionType.All);

            // Save the excel file.
            const outputData = wb.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and protected. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

### **حماية عمود في ورقة العمل**

يسمح لك Aspose.Cells بقفل أي عمود بسهولة في ورقة العمل. هنا، يمكننا استخدام طريقة [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/javascript-cpp/column/#applyStyle-style-styleflag-) من فئة [**Aspose.Cells.Column**](https://reference.aspose.com/cells/javascript-cpp/column) لتطبيق [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) على عمود معين في ورقة العمل. تستقبل هذه الطريقة وسيطين: كائن [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) و [**StyleFlag**](https://reference.aspose.com/cells/javascript-cpp/styleflag) الذي يحتوي على جميع الأعضاء المتعلقة بالتنسيق المطبق.

يُظهر المثال التالي كيفية حماية عمود في ورقة العمل. يفتح جميع الخلايا في ورقة العمل أولاً ثم يقفل العمود الأول فيها. وأخيرًا، يحمي ورقة العمل. يحتوي الكائن [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) على خاصية بوليانية، [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--). يمكنك تعيين الخاصية [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--) إلى true أو false لقفل أو فتح قفل الصف أو العمود باستخدام الكائن [**StyleFlag**](https://reference.aspose.com/cells/javascript-cpp/styleflag).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Unlock Columns and Protect Sheet</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, StyleFlag, ProtectionType } = AsposeCells;

        const readyPromise = AsposeCells.onReady({
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
                // If no file provided, a new workbook will be created
                document.getElementById('result').innerHTML = '<p style="color: orange;">No file selected. A new workbook will be created and processed.</p>';
            } else {
                document.getElementById('result').innerHTML = '<p>Processing selected file...</p>';
            }

            await readyPromise;

            // Load workbook from file if provided, otherwise create new workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Create a worksheet object and obtain the first sheet.
            const sheet = workbook.worksheets.get(0);

            // Define the style object.
            let style;

            // Define the styleflag object.
            const flag = new StyleFlag();

            // Loop through all the columns in the worksheet and unlock them.
            for (let i = 0; i <= 255; i++) {
                style = sheet.cells.columns.get(i).style;
                style.isLocked = false;
                flag.locked = true;
                sheet.cells.columns.get(i).applyStyle(style, flag);
            }

            // Get the first column style.
            style = sheet.cells.columns.get(0).style;

            // Lock it.
            style.isLocked = true;

            // Apply the style to the first column.
            sheet.cells.columns.get(0).applyStyle(style, flag);

            // Protect the sheet.
            sheet.protect(ProtectionType.All);

            // Save the excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **السماح للمستخدمين بتعديل المدى**

يُظهر المثال التالي كيفية السماح للمستخدمين بتعديل مدى محدد في ورقة العمل الخاصة.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Protect Range</title>
    </head>
    <body>
        <h1>Protect Range Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ProtectionType, Utils } = AsposeCells;

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

            // Instantiate a new or loaded Workbook
            let book;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                book = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                book = new Workbook();
            }

            // Get the first (default) worksheet
            const sheet = book.worksheets.get(0);

            // Get the Allow Edit Ranges
            const allowRanges = sheet.allowEditRanges;

            // Define ProtectedRange
            let protected_range;

            // Create the range
            const idx = allowRanges.add("r2", 1, 1, 3, 3);
            protected_range = allowRanges.get(idx);

            // Specify the password
            protected_range.password = "123";

            // Protect the sheet
            sheet.protect(ProtectionType.All);

            // Save the Excel file
            const outputData = book.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'protectedrange.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Protected Range Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Protected range added and sheet protected successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

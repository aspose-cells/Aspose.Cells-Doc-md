---
title: التحقق من البيانات
type: docs
weight: 90
url: /ar/javascript-cpp/data-validation/
description: تعلم كيف تضيف التحقق من صحة البيانات عبر Aspose.Cells for JavaScript عبر واجهة برمجة التطبيقات C ++.
keywords: أضف التحقق من صحة البيانات JavaScript عبر C ++، احصل على قيمة التحقق من الصحة JavaScript عبر C ++، أضف تحقق من صحة الرقم الكامل JavaScript عبر C ++، أضف تحقق من صحة القائمة JavaScript عبر C ++، أضف تحقق من صحة التاريخ JavaScript عبر C ++، أضف تحقق من صحة الوقت JavaScript عبر C ++، أضف تحقق من طول النص JavaScript عبر C ++، أضف CellArea إلى التحقق من الصحة الحالية JavaScript عبر C ++، تحقق مما إذا كانت التحقق من الصحة في الخلية قائمة منسدلة JavaScript عبر C ++، أضف التحقق المخصص JavaScript عبر C ++
---

{{% alert color="primary" %}}
 تقدم Microsoft Excel بعض الميزات الجيدة للتصفية التلقائية أو التحقق من صحة ورقة العمل. يدعم Aspose.Cells بشكل كامل ميزات التحقق من صحة البيانات والتصفية التلقائية في Microsoft Excel. يوضح هذا المقال كيفية استخدام الميزات في Microsoft Excel، وكيفية برمجتها باستخدام Aspose.Cells for JavaScript عبر C ++.
{{% /alert %}}

## **أنواع التحقق من البيانات والتنفيذ**

التحقق من البيانات هو القدرة على وضع قواعد تتعلق بالبيانات المُدخلة على ورقة العمل. على سبيل المثال، استخدم التحقق لضمان أن العمود المسمى تاريخ يحتوي فقط على تواريخ، أو أن عمودًا آخر يحتوي فقط على أرقام. يمكنك حتى التأكد من أن العمود المسمى تاريخ يحتوي فقط على تواريخ ضمن نطاق معين. باستخدام التحقق من البيانات، يمكنك التحكم في ما يُدخل في الخلايا في ورقة العمل.

يدعم Microsoft Excel عددًا من أنواع التحقق المختلفة للبيانات. يُستخدم كل نوع للتحكم في نوع البيانات التي تُدخل إلى خلية أو نطاق الخلايا. أدناه، مقتطفات الكود توضح كيفية التحقق من:

- أن الأرقام صحيحة، أي أن ليس لديها جزء عشري.
- أن الأرقام العشرية تتبع الهيكل الصحيح. يحدد مثال الكود أن يكون نطاق الخلايا يجب أن يحتوي على اثنين من أماكن العشرية.
- أن القيم مقيدة بقائمة من القيم. يحدد التحقق بالقائمة قائمة منفصلة من القيم التي يمكن تطبيقها على خلية أو نطاق الخلايا.
- يتمثل التواريخ ضمن نطاق محدد.
- أن الوقت يكون ضمن نطاق محدد.
- أن النص يكون ضمن طول حرف معين.

### **التحقق من البيانات مع Microsoft Excel**

لإنشاء التحققات باستخدام Microsoft Excel:

1. في ورقة العمل، حدد الخلايا التي ترغب في تطبيق التحقق عليها.
1. من قائمة **البيانات**، حدد **التحقق**. سيتم عرض حوار التحقق.
1. انقر على علامة التبويب **الإعدادات** ثم أدخل الإعدادات.

### ** التحقق من صحة البيانات مع Aspose.Cells for JavaScript عبر C ++**

التحقق من البيانات هو ميزة قوية للتحقق من المعلومات المُدخلة في أوراق العمل. باستخدام التحقق من البيانات، يمكن للمطورين توفير للمستخدمين قائمة من الخيارات، وتقييد إدخالات البيانات إلى نوع معين أو حجم، الخ.
في Aspose.Cells for JavaScript عبر C ++، تحتوي كل فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) على مجموعة [**validations**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#validations--) تمثل مجموعة من كائنات [**Validation**](https://reference.aspose.com/cells/javascript-cpp/validation). لضبط التحقق من الصحة، اضبط بعض خصائص فئة [**Validation**](https://reference.aspose.com/cells/javascript-cpp/validation) كما يلي:

- النوع - يمثل نوع التحقق، والذي قد يتم تحديده باستخدام أحد القيم المعرفة مسبقًا في تعداد [**ValidationType**](https://reference.aspose.com/cells/javascript-cpp/validationtype).
- المشغل - يمثل العامل المستخدم في التحقق، والذي قد يتم تحديده باستخدام أحد القيم المعرفة مسبقًا في تعداد [**OperatorType**](https://reference.aspose.com/cells/javascript-cpp/operatortype).
- الصيغة1 - يمثل القيمة أو التعبير المرتبط بالجزء الأول من التحقق من البيانات.
- الصيغة2 - يمثل القيمة أو التعبير المرتبط بالجزء الثاني من التحقق من البيانات.

عند تكوين خصائص كائن [**Validation**](https://reference.aspose.com/cells/javascript-cpp/validation)، يمكن للمطورين استخدام بنية [**CellArea**](https://reference.aspose.com/cells/javascript-cpp/cellarea) لتخزين معلومات حول نطاق الخلية الذي سيتم التحقق منه باستخدام التحقق الذي تم إنشاؤه.

#### **أنواع التحقق من البيانات**

يحتوي تعداد [**ValidationType**](https://reference.aspose.com/cells/javascript-cpp/validationtype) على الأعضاء التالية:

| **اسم العضو** | **الوصف** |
| :- | :- |
|AnyValue|يُشير إلى قيمة من أي نوع.|
|WholeNumber|تشير إلى نوع التحقق من صحة للأرقام الكاملة.|
|Decimal|تشير إلى نوع التحقق من صحة للأرقام العشرية.|
|List|تشير إلى نوع التحقق من صحة لقائمة السقط.|
|Date|تشير إلى نوع التحقق من صحة للتواريخ.|
|Time|تشير إلى نوع التحقق من صحة للوقت.|
|TextLength|تشير إلى نوع التحقق من صحة لطول النص.|
|Custom|تشير إلى نوع التحقق من العرف.|

##### **تحقق البيانات من الأعداد الصحيحة**

 مع هذا النوع من التحقق، يمكن للمستخدمين إدخال أرقام كاملة فقط ضمن نطاق معين في الخلايا التي تم التحقق منها. تظهر الأمثلة البرمجية التي تلي ذلك كيفية تنفيذ نوع التحقق من صحة الرقم الكامل. ينشئ المثال نفس التحقق من صحة البيانات باستخدام Aspose.Cells for JavaScript عبر C ++ الذي أنشأناه باستخدام Microsoft Excel أعلاه.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Validation Example</h1>
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
            const resultDiv = document.getElementById('result');
            const fileInput = document.getElementById('fileInput');

            if (fileInput.files.length > 0) {
                // If a file is provided, we will open it; otherwise create a new workbook
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                // Instantiate workbook from uploaded file
                var workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new workbook
                var workbook = new Workbook();
            }

            // Create a worksheet and get the first worksheet.
            const ExcelWorkSheet = workbook.worksheets.get(0);

            // Accessing the Validations collection of the worksheet
            const validations = workbook.worksheets.get(0).validations;

            // Create Cell Area
            const ca = new AsposeCells.CellArea();
            ca.startRow = 0;
            ca.endRow = 0;
            ca.startColumn = 0;
            ca.endColumn = 0;

            // Creating a Validation object
            const idx = validations.add(ca);
            const validation = validations.get(idx);

            // Setting the validation type to whole number
            validation.type = AsposeCells.ValidationType.WholeNumber;

            // Setting the operator for validation to Between
            validation.operator = AsposeCells.OperatorType.Between;

            // Setting the minimum value for the validation
            validation.formula1 = "10";

            // Setting the maximum value for the validation
            validation.formula2 = "1000";

            // Applying the validation to a range of cells from A1 to B2 using the CellArea structure
            const area = new AsposeCells.CellArea();
            area.startRow = 0;
            area.endRow = 1;
            area.startColumn = 0;
            area.endColumn = 1;

            // Adding the cell area to Validation
            validation.addArea(area);

            // Save the workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: "application/vnd.ms-excel" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Validation added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


##### **تحقق البيانات من القائمة**

يسمح هذا النوع من التحقق للمستخدم بإدخال قيم من قائمة منسدلة. يوفر قائمة: سلسلة من الصفوف التي تحتوي على بيانات. في المثال، يتم إضافة ورقة عمل ثانية لاحتواء مصدر القائمة. يمكن للمستخدمين فقط تحديد القيم من القائمة. منطقة التحقق هي نطاق الخلية A1:A5 في الورقة العمل الأولى.

من المهم هنا أن تقوم بضبط خاصية [**Validation.inCellDropDown(boolean)**](https://reference.aspose.com/cells/javascript-cpp/validation/#inCellDropDown-boolean-) على **true**.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Validation List Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, ValidationType, OperatorType, ValidationAlertType } = AsposeCells;

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
            // This example creates a new workbook in the browser (file input is optional here).
            const workbook = new Workbook();

            // Get the first worksheet.
            const worksheet1 = workbook.worksheets.get(0);

            // Add a new worksheet and access it.
            const i = workbook.worksheets.add();
            const worksheet2 = workbook.worksheets.get(i);

            // Create a range in the second worksheet.
            const range = worksheet2.cells.createRange("E1", "E4");

            // Name the range.
            range.name = "MyRange";

            // Fill different cells with data in the range.
            range.get(0, 0).value = "Blue";
            range.get(1, 0).value = "Red";
            range.get(2, 0).value = "Green";
            range.get(3, 0).value = "Yellow";

            // Get the validations collection.
            const validations = worksheet1.validations;

            // Create Cell Area
            const ca = new CellArea();
            ca.startRow = 0;
            ca.endRow = 0;
            ca.startColumn = 0;
            ca.endColumn = 0;

            // Create a new validation to the validations list.
            const validation = validations.get(validations.add(ca));

            // Set the validation type.
            validation.type = ValidationType.List;

            // Set the operator.
            validation.operator = OperatorType.None;

            // Set the in cell drop down.
            validation.inCellDropDown = true;

            // Set the formula1.
            validation.formula1 = "=MyRange";

            // Enable it to show error.
            validation.showError = true;

            // Set the alert type severity level.
            validation.alertStyle = ValidationAlertType.Stop;

            // Set the error title.
            validation.errorTitle = "Error";

            // Set the error message.
            validation.errorMessage = "Please select a color from the list";

            // Specify the validation area.
            const area = new CellArea();
            area.startRow = 0;
            area.endRow = 4;
            area.startColumn = 0;
            area.endColumn = 0;

            // Add the validation area.
            validation.addArea(area);

            // Save the Excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Validation list created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```


##### **تحقق البيانات من التاريخ**

مع هذا النوع من التحقق، يقوم المستخدمون بإدخال قيم تاريخية ضمن النطاق المحدد، أو تلبية معايير محددة، داخل الخلايا المحققة. في المثال، يتم تقييد المستخدم لإدخال تواريخ بين 1970 و1999. هنا، منطقة التحقق هي خلية B1.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Date Validation Example</h1>
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
            // This example creates a new workbook in the browser (no file input required)
            const workbook = new Workbook();

            // Obtain the cells of the first worksheet.
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;

            // Put a string value into the A1 cell.
            const cellA1 = cells.get("A1");
            cellA1.value = "Please enter Date b/w 1/1/1970 and 12/31/1999";

            // Set row height and column width for the cells by accessing row/column objects
            const row0 = cells.rows.get(0);
            row0.height = 31;
            const col0 = cells.columns.get(0);
            col0.width = 35;

            // Get the validations collection.
            const validations = worksheet.validations;

            // Create Cell Area
            const ca = new AsposeCells.CellArea();
            ca.startRow = 0;
            ca.endRow = 0;
            ca.startColumn = 0;
            ca.endColumn = 0;

            // Add a new validation.
            const validationIndex = validations.add(ca);
            const validation = validations.get(validationIndex);

            // Set the data validation type.
            validation.type = AsposeCells.ValidationType.Date;

            // Set the operator for the data validation
            validation.operator = AsposeCells.OperatorType.Between;

            // Set the value or expression associated with the data validation.
            validation.formula1 = "1/1/1970";

            // The value or expression associated with the second part of the data validation.
            validation.formula2 = "12/31/1999";

            // Enable the error.
            validation.showError = true;

            // Set the validation alert style.
            validation.alertStyle = AsposeCells.ValidationAlertType.Stop;

            // Set the title of the data-validation error dialog box
            validation.errorTitle = "Date Error";

            // Set the data validation error message.
            validation.errorMessage = "Enter a Valid Date";

            // Set and enable the data validation input message.
            validation.inputMessage = "Date Validation Type";
            validation.ignoreBlank = true;
            validation.showInput = true;

            // Set a collection of CellArea which contains the data validation settings.
            const cellArea = new AsposeCells.CellArea();
            cellArea.startRow = 0;
            cellArea.endRow = 0;
            cellArea.startColumn = 1;
            cellArea.endColumn = 1;

            // Add the validation area.
            validation.addArea(cellArea);

            // Save the Excel file and provide download link.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: "application/vnd.ms-excel" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and validation added. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

##### **تحقق المواقيت الزمنية للبيانات**

مع هذا النوع من التحقق، يمكن للمستخدمين إدخال أوقات ضمن نطاق محدد، أو تلبية بعض المعايير، في الخلايا الموجودة. ففي المثال، يتم تقييد المستخدم بإدخال الأوقات بين الساعة 09:00 و11:30 صباحًا. هنا، مجال التحقق هو خلية B1.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Time Validation Example</h1>
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

            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new workbook if no file is provided
                workbook = new Workbook();
            }

            // Obtain the cells of the first worksheet.
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;

            // Put a string value into A1 cell.
            const a1 = cells.get("A1");
            a1.value = "Please enter Time b/w 09:00 and 11:30 'o Clock";

            // Set the row height and column width for the cells using row/column objects.
            cells.rows.get(0).height = 31;
            cells.columns.get(0).width = 35;

            // Get the validations collection.
            const validations = worksheet.validations;

            // Create Cell Area
            const ca = new AsposeCells.CellArea();
            ca.startRow = 0;
            ca.endRow = 0;
            ca.startColumn = 0;
            ca.endColumn = 0;

            // Add a new validation and obtain it.
            const validationIndex = validations.add(ca);
            const validation = validations.get(validationIndex);

            // Set the data validation type and other properties.
            validation.type = AsposeCells.ValidationType.Time;
            validation.operator = AsposeCells.OperatorType.Between;
            validation.formula1 = "09:00";
            validation.formula2 = "11:30";
            validation.showError = true;
            validation.alertStyle = AsposeCells.ValidationAlertType.Information;
            validation.errorTitle = "Time Error";
            validation.errorMessage = "Enter a Valid Time";
            validation.inputMessage = "Time Validation Type";
            validation.ignoreBlank = true;
            validation.showInput = true;

            // Set a collection of CellArea which contains the data validation settings.
            const cellArea = new AsposeCells.CellArea();
            cellArea.startRow = 0;
            cellArea.endRow = 0;
            cellArea.startColumn = 1;
            cellArea.endColumn = 1;

            // Add the validation area.
            validation.addArea(cellArea);

            // Save the Excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: 'application/vnd.ms-excel' });
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


##### **تحقق طول النصوص للبيانات**

مع هذا النوع من التحقق، يمكن للمستخدمين إدخال قيم نصية من طول محدد في الخلايا الموجودة. في المثال، يتم تقييد المستخدم بإدخال قيم سلسلة نصية بأكثر من 5 أحرف. مجال التحقق هو الخلية B1.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Add Text Length Validation</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, ValidationType, OperatorType, ValidationAlertType } = AsposeCells;

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
            const workbook = new Workbook();

            // Obtain the cells of the first worksheet.
            const cells = workbook.worksheets.get(0).cells;

            // Put a string value into A1 cell.
            const cellA1 = cells.get("A1");
            cellA1.value = "Please enter a string not more than 5 chars";

            // Set row height and column width for the cell.
            cells.rows.get(0).height = 31;
            cells.columns.get(0).width = 35;

            // Get the validations collection.
            const validations = workbook.worksheets.get(0).validations;

            // Create Cell Area
            const ca = new CellArea();
            ca.startRow = 0;
            ca.endRow = 0;
            ca.startColumn = 0;
            ca.endColumn = 0;

            // Add a new validation.
            const validationIndex = validations.add(ca);
            const validation = validations.get(validationIndex);

            // Set the data validation type.
            validation.type = ValidationType.TextLength;

            // Set the operator for the data validation.
            validation.operator = OperatorType.LessOrEqual;

            // Set the value or expression associated with the data validation.
            validation.formula1 = "5";

            // Enable the error.
            validation.showError = true;

            // Set the validation alert style.
            validation.alertStyle = ValidationAlertType.Warning;

            // Set the title of the data-validation error dialog box.
            validation.errorTitle = "Text Length Error";

            // Set the data validation error message.
            validation.errorMessage = " Enter a Valid String";

            // Set and enable the data validation input message.
            validation.inputMessage = "TextLength Validation Type";
            validation.ignoreBlank = true;
            validation.showInput = true;

            // Set a collection of CellArea which contains the data validation settings.
            const cellArea = new CellArea();
            cellArea.startRow = 0;
            cellArea.endRow = 0;
            cellArea.startColumn = 1;
            cellArea.endColumn = 1;

            // Add the validation area.
            validation.addArea(cellArea);

            // Save the Excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File created successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```


### **قواعد تحقق البيانات**

عند تنفيذ عمليات التحقق من الصحة، يمكن فحص صحة التحقق من خلال تعيين قيم مختلفة في الخلايا. يمكن استخدام [**cell.validationValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#validationValue--) لاسترداد نتيجة التحقق. يوضح المثال التالي هذه الميزة مع قيم مختلفة. يمكن تنزيل الملف النموذجي للاختبار من الرابط التالي:

[sampleDataValidationRules.xlsx](77496339.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Data Validation Check Example</h1>
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
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate the workbook from the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access Cell C1
            // Cell C1 has the Decimal Validation applied on it.
            // It can take only the values Between 10 and 20
            const cell = worksheet.cells.get("C1");

            const messages = [];

            // Enter 3 inside this cell
            // Since it is not between 10 and 20, it should fail the validation
            cell.value = 3;

            // Check if number 3 satisfies the Data Validation rule applied on this cell
            const isValid3 = cell.validationValue;
            messages.push(`Is 3 a Valid Value for this Cell: ${isValid3}`);

            // Enter 15 inside this cell
            // Since it is between 10 and 20, it should succeed the validation
            cell.value = 15;

            // Check if number 15 satisfies the Data Validation rule applied on this cell
            const isValid15 = cell.validationValue;
            messages.push(`Is 15 a Valid Value for this Cell: ${isValid15}`);

            // Enter 30 inside this cell
            // Since it is not between 10 and 20, it should fail the validation again
            cell.value = 30;

            // Check if number 30 satisfies the Data Validation rule applied on this cell
            const isValid30 = cell.validationValue;
            messages.push(`Is 30 a Valid Value for this Cell: ${isValid30}`);

            // Display results
            resultDiv.innerHTML = messages.map(m => `<p>${m}</p>`).join('');

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';
        });
    </script>
</html>
```


## **التحقق مما إذا كان التحقق في الخلية القائمة المنسدلة**

كما رأينا، هناك العديد من أنواع التحققات التي يمكن تنفيذها داخل خلية. إذا أردت التحقق مما إذا كانت التحقق من الصحة قائمة منسدلة أم لا، يمكن استخدام طريقة [**validation.inCellDropDown**](https://reference.aspose.com/cells/javascript-cpp/validation/#inCellDropDown--) لاختبار ذلك. توضح الشفرة النموذجية التالية استخدام هذه الخاصية. يمكن تنزيل ملف اختبار من الرابط التالي:

[sampleValidation.xlsx](79527947.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Check Data Validation Drop-downs</h1>
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
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the worksheet named "Sheet1"
            const sheet = workbook.worksheets.get("Sheet1");
            const cells = sheet.cells;

            const appendMessage = (msg, color = 'black') => {
                const p = document.createElement('p');
                p.style.color = color;
                p.textContent = msg;
                resultDiv.appendChild(p);
            };

            const checkDropDown = (cell, cellRef) => {
                const validation = cell.validation;
                if (validation.inCellDropDown) {
                    appendMessage(`${cellRef} is a dropdown`, 'green');
                } else {
                    appendMessage(`${cellRef} is NOT a dropdown`, 'orange');
                }
            };

            checkDropDown(cells.get("A2"), "A2");
            checkDropDown(cells.get("B2"), "B2");
            checkDropDown(cells.get("C2"), "C2");
        });
    </script>
</html>
```


## **إضافة منطقة الخلية إلى التحقق القائم**

قد تكون هناك حالات ترغب فيها في إضافة [**CellArea**](https://reference.aspose.com/cells/javascript-cpp/cellarea) إلى [**Validation**](https://reference.aspose.com/cells/javascript-cpp/validation) الموجودة. عند إضافة [**CellArea**](https://reference.aspose.com/cells/javascript-cpp/cellarea) باستخدام [**Validation.addArea(CellArea)**](https://reference.aspose.com/cells/javascript-cpp/validation/#addArea-cellarea-)، يتحقق Aspose.Cells من جميع المناطق الموجودة مسبقًا لمعرفة ما إذا كانت المنطقة الجديدة موجودة بالفعل. إذا كانت هناك العديد من التحققات في الملف، فإن ذلك يؤثر على الأداء. لتجاوز ذلك، توفر الواجهة البرمجية طريقة [**Validation.addArea(CellArea, boolean, boolean)**](https://reference.aspose.com/cells/javascript-cpp/validation/#addArea-cellarea-boolean-boolean-). يشير المعامل *checkIntersection* إلى ما إذا كان يتم التحقق من تقاطع المنطقة المعطاة مع مناطق التحقق الموجودة. ضبطه على **false** سيؤدي إلى تعطيل التحقق من المناطق الأخرى. المعامل *checkEdge* يشير إلى ما إذا كان سيتم التحقق من المناطق المطبقة. إذا أصبحت المنطقة الجديدة المنطقة العليا اليسرى، يتم إعادة بناء الإعدادات الداخلية. إذا كنت متأكدًا من أن المنطقة الجديدة ليست المنطقة العليا اليسرى، يمكنك ضبط هذا المعامل على **false**.

يوضح مقتطف الكود التالي استخدام طريقة [**Validation.addArea(CellArea, boolean, boolean)**](https://reference.aspose.com/cells/javascript-cpp/validation/#addArea-cellarea-boolean-boolean-) لإضافة [**CellArea**](https://reference.aspose.com/cells/javascript-cpp/cellarea) جديد إلى [**Validation**](https://reference.aspose.com/cells/javascript-cpp/validation) موجودة.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Validations</title>
    </head>
    <body>
        <h1>Validations Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Accessing the Validations collection of the worksheet
            const validation = worksheet.validations.get(0);

            // Create your cell area.
            const cellArea = AsposeCells.CellArea.createCellArea("D5", "E7");

            // Adding the cell area to Validation
            validation.addArea(cellArea, false, false);

            // Save the output workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ValidationsSample_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Validation area added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

الملفات الإكسل المصدر والناتج مرفقة للرجوع إليها.

[ملف المصدر](96928093.xlsx)

[ملف الإخراج](96928220.xlsx)

## **مواضيع متقدمة**
- [الحصول على التحقق من الخلية في ملفات ODS](/cells/ar/javascript-cpp/get-cell-validation-in-ods-files/)
- [الحصول على التحقق المطبق على خلية](/cells/ar/javascript-cpp/get-validation-applied-on-a-cell/)
- [التحقق من أن قيمة الخلية تلبي قواعد التحقق من البيانات](/cells/ar/javascript-cpp/verify-that-cell-value-satisfies-data-validation-rules/)

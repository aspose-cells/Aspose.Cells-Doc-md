---
title: كيفية وأين تستخدم العدادات مع جافا سكريبت عبر C++
linktitle: تكرار البيانات
type: docs
weight: 55
url: /ar/javascript-cpp/how-and-where-to-use-enumerators/
description: تعلم كيفية استخدام العدادات من خلال Aspose.Cells for JavaScript عبر واجهة برمجة التطبيقات C++.
keywords: كيفية استخدام العدادات JavaScript عبر C++، عداد الخلايا JavaScript عبر C++، عداد الصفوف JavaScript عبر C++، عداد الأعمدة JavaScript عبر C++
---

{{% alert color="primary" %}}  

المُعدِّد هو كائن يوفر القدرة على عبور حاوية أو مجموعة. يمكن استخدام العدادات لقراءة البيانات في المجموعة، لكنها لا يمكن استخدامها لتعديل المجموعة الأساسية، بينما المصفوفة هي واجهة تُعرف بطريقة واحدة `enumerator` والتي تُرجع واجهة `IEnumerator`، هذا يتيح الوصول للقراءة فقط إلى مجموعة.  

توفر واجهات برمجة تطبيقات Aspose.Cells مجموعة من المعدلات الإحصائية، ومع ذلك، يناقش هذا المقال بشكل رئيسي الثلاثة أنواع المذكورة أدناه.  

1. معدل الخلايا  
1. معدل الصفوف  
1. معدل الأعمدة  

{{% /alert %}}  

## **كيفية استخدام المعدلات الإحصائية**  

### **معدل الخلايا**  

هناك طرق مختلفة للوصول إلى معدل الخلايا، ويمكن للشخص استخدام أيًا من هذه الطرق استنادًا إلى متطلبات التطبيق. هنا الطرق التي تُرجع معدل الخلايا.  

1. [**Cells.enumerator**](https://reference.aspose.com/cells/javascript-cpp/cells/#enumerator--)  
1. [**Row.enumerator**](https://reference.aspose.com/cells/javascript-cpp/row/#enumerator--)  
1. [**Range.enumerator**](https://reference.aspose.com/cells/javascript-cpp/range/#enumerator--)  

تعود الطرق المذكورة أعلاه جميعًا بمُحدِّد العناصر الذي يسمح بجَولة جمعية الخلايا التي تم تهيئتها.  

{{% alert color="primary" %}}  

أثناء جولة الخلايا، يجب ألا يتم تعديل المجموعة (العمليات التي ستؤدي إلى إنشاء خلية جديدة أو حذف خلية موجودة). وإلا فإن المُحدِّد قد لا يكون قادرًا على جولة جميع الخلايا بشكل صحيح (قد يكون بعض العناصر قد تجولت بشكل متكرر أو تم تخطيها).  

{{% /alert %}}  

يُظهر المثال التالي تنفيذ واجهة `IEnumerator` لمجموعة الخلايا.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Read Cell Values</h1>
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

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            const resultLines = [];

            // Iterate over all cells in the worksheet
            const cellsEnumerator = worksheet.cells.getEnumerator();
            for (const cell of cellsEnumerator) {
                console.log(`${cell.name} ${cell.value}`);
                resultLines.push(`${cell.name} ${cell.value}`);
            }

            // Iterate over the first row's cells
            const firstRowEnumerator = worksheet.cells.rows.get(0).getEnumerator();
            for (const cell of firstRowEnumerator) {
                console.log(`${cell.name} ${cell.value}`);
                resultLines.push(`${cell.name} ${cell.value}`);
            }

            // Iterate over a specific range A1:B10
            const rangeEnumerator = worksheet.cells.createRange("A1:B10").getEnumerator();
            for (const cell of rangeEnumerator) {
                console.log(`${cell.name} ${cell.value}`);
                resultLines.push(`${cell.name} ${cell.value}`);
            }

            document.getElementById('result').innerHTML = `<pre>${resultLines.join('\n')}</pre>`;
        });
    </script>
</html>
```  

### **مُحدِّد الصفوف**  

يمكن الوصول إلى عداد الصفوف أثناء استخدام طريقة [**RowCollection.enumerator**](https://reference.aspose.com/cells/javascript-cpp/rowcollection/#enumerator--). يوضح المثال التالي تنفيذ واجهة `IEnumerator` لـ [**RowCollection**](https://reference.aspose.com/cells/javascript-cpp/rowcollection).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - List Row Indexes</h1>
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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get RowCollection and iterate using index
            const rows = workbook.worksheets.get(0).cells.rows;
            const rowCount = rows.count;

            // Traverse rows in the collection and display indexes
            let output = '<p>Row indexes:</p><ul>';
            for (let i = 0; i < rowCount; i++) {
                const row = rows.get(i);
                output += `<li>${row.index}</li>`;
                console.log(row.index);
            }
            output += '</ul>';
            document.getElementById('result').innerHTML = output;
        });
    </script>
</html>
```  

### **مُحدِّد الأعمدة**  

يمكن الوصول إلى عداد الأعمدة أثناء استخدام طريقة [**ColumnCollection.enumerator**](https://reference.aspose.com/cells/javascript-cpp/columncollection). يوضح المثال التالي تنفيذ واجهة `IEnumerator` لـ [**ColumnCollection**](https://reference.aspose.com/cells/javascript-cpp/columncollection).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Read Columns Indexes Example</h1>
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

            // Get columns collection from first worksheet
            const columns = workbook.worksheets.get(0).cells.columns;
            // Traverse columns using index
            const count = columns.count;
            let html = '<p>Columns indexes:</p><ul>';
            for (let i = 0; i < count; i++) {
                const col = columns.get(i);
                html += `<li>${col.index}</li>`;
                console.log(col.index);
            }
            html += '</ul>';
            document.getElementById('result').innerHTML = html;
        });
    </script>
</html>
```  

## **أين يجب استخدام المُحدِّدات**  

من أجل مناقشة مزايا استخدام العدادات، دعونا نأخذ مثالاً حقيقياً من الوقت الحقيقي.  

**سيناريو**  

متطلب التطبيق هو التجول عبر جميع الخلايا في [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) معين لقراءة قيمها. قد توجد عدة طرق لتحقيق هذا الهدف. تم توضيح بعض منها أدناه.  

### **استخدام نطاق العرض**  

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Read Max Display Range Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get Cells collection of first worksheet
            const cells = workbook.worksheets.get(0).cells;

            // Get the MaxDisplayRange
            const displayRange = cells.maxDisplayRange;

            // Loop over all cells in the MaxDisplayRange
            let outputLines = [];
            for (let row = displayRange.firstRow; row < displayRange.rowCount; row++) {
                for (let col = displayRange.firstColumn; col < displayRange.columnCount; col++) {
                    // Read the Cell value (stringValue property)
                    const cell = displayRange.get(row, col);
                    outputLines.push(cell.stringValue);
                    console.log(cell.stringValue);
                }
            }

            resultDiv.innerHTML = '<pre>' + outputLines.join('\n') + '</pre>';
        });
    </script>
</html>
```  

### **استخدام MaxDataRow و MaxDataColumn**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            #result { margin-top: 15px; max-height: 400px; overflow: auto; border: 1px solid #ddd; padding: 10px; }
            .cell-value { padding: 2px 0; border-bottom: 1px dashed #eee; }
            .error { color: red; }
        </style>
    </head>
    <body>
        <h1>Read Cells Example</h1>
        <input type="file" id="fileInput" accept=".xlsx,.xls,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook } = AsposeCells;

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

        function escapeHtml(text) {
            if (text === null || text === undefined) return '';
            return String(text)
                .replace(/&/g, '&amp;')
                .replace(/</g, '&lt;')
                .replace(/>/g, '&gt;')
                .replace(/"/g, '&quot;')
                .replace(/'/g, '&#039;');
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p class="error">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get Cells collection of first worksheet
            const cells2 = workbook.worksheets.get(0).cells;
            const maxDataRow = cells2.maxDataRow;
            const maxDataColumn = cells2.maxDataColumn;

            const outputLines = [];
            // Loop over all cells
            for (let row = 0; row <= maxDataRow; row++) {
                for (let col = 0; col <= maxDataColumn; col++) {
                    // Read the Cell value
                    const currentCell = cells2.checkCell(row, col);
                    if (currentCell) {
                        const cellText = currentCell.stringValue;
                        outputLines.push('<div class="cell-value">' + escapeHtml(cellText) + '</div>');
                        console.log(cellText);
                    }
                }
            }

            if (outputLines.length === 0) {
                resultDiv.innerHTML = '<p>No cell values found.</p>';
            } else {
                resultDiv.innerHTML = outputLines.join('');
            }
        });
    </script>
</html>
```  

كما يمكنك أن تلاحظ أن كلتا الطريقتين المذكورتين تستخدمان تقريبًا نفس المنطق، وهو: الدوران حول جميع الخلايا في المجموعة لقراءة قيم الخلايا. قد يكون هذا مشكلة لعدة أسباب كما سيتم مناقشتها أدناه.  

1. تتطلب واجهات برمجة التطبيقات مثل [**maxRow**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxRow--)، [**maxDataRow**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDataRow--)، [**maxColumn**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxColumn--)، [**maxDataColumn**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDataColumn--) و [**maxDisplayRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDisplayRange--) وقتًا إضافيًا لجمع الإحصائيات المقابلة. إذا كانت مصفوفة البيانات (صفوف × أعمدة) كبيرة، فإن استخدام هذه الواجهات يمكن أن يفرض عقبة على الأداء.  
1. في معظم الحالات، لا تتم إنشاء جميع الخلايا في النطاق المعطى. في مثل هذه الحالات، فحص كل خلية في البيانات ليس فعَّالًا كمقارنة بفحص الخلايا المهيئة فقط.  
1. الوصول إلى خلية في حلقة مثل Cells row، column سيؤدي إلى إنشاء جميع كائنات الخلايا في النطاق، مما قد يؤدي في النهاية إلى حدوث استثناء نفاد الذاكرة.  

## **الاستنتاج**  

بناءً على الحقائق المذكورة أعلاه، فإن السيناريوهات الممكنة التالية هي التي يجب استخدام المُحدِّدات فيها.  

1. الوصول القراءة فقط لمجموعة الخلايا مطلوب، أي؛ المتطلب هو تفقّد الخلايا فقط.  
1. يتعين عبور عدد كبير من الخلايا.  
1. يجب عبور الخلايا/الصفوف/الأعمدة المهيأة فقط.

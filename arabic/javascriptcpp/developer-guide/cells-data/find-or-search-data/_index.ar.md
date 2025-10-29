---
title: البحث عن البيانات أو البحث
type: docs
weight: 50
url: /ar/javascript-cpp/find-or-search-data/
description: تعلم كيف تجد أو تبحث عن خلايا في ورقة عمل تحتوي على بيانات محددة عبر Aspose.Cells for JavaScript عبر واجهة برمجة التطبيقات C ++.
keywords: ابحث عن بيانات جافا سكريبت عبر C++، ابحث عن بيانات جافا سكريبت عبر C++، ابحث عن خلايا تحتوي على صيغة جافا سكريبت عبر C++، ابحث عن خلايا تحتوي على صيغة جافا سكريبت عبر C++، ابحث عن البيانات أو الصيغ باستخدام خيارات find جافا سكريبت عبر C++، ابحث عن البيانات أو الصيغ باستخدام خيارات find جافا سكريبت عبر C++، ابحث أو استعلم عن خلايا تحتوي على قيمة أو رقم سلسلة محدد جافا سكريبت عبر C++، ابحث أو استعلم عن خلايا تحتوي على بيانات محددة
---

{{% alert color="primary" %}}  
يسمح Microsoft Excel للمستخدمين بالعثور على خلايا في ورقة العمل تحتوي على بيانات محددة.  
{{% /alert %}}  

## **العثور على الخلايا التي تحتوي على بيانات محددة**  

### **استخدام Microsoft Excel**  

يسمح Microsoft Excel للمستخدمين بالعثور على خلايا في ورقة العمل تحتوي على بيانات محددة. إذا قمت باختيار **تحرير** من قائمة **بحث** في Microsoft Excel، سترى مربع حوار يمكنك تحديد قيمة البحث فيها.  

هنا، نبحث عن القيمة "البرتقال". تسمح Aspose.Cells أيضًا للمطورين بالعثور على الخلايا في ورقة العمل التي تحتوي على القيم المحددة.  

### **استخدام Aspose.Cells for Javaسكريبت عبر C++**  

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)، التي تمثل ملف Microsoft Excel. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) على مجموعة [**Workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) التي تتيح الوصول إلى كل ورقة عمل في ملف Excel. تمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) مجموعة [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) تمثل جميع الخلايا في ورقة العمل. توفر مجموعة [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) العديد من الطرق للعثور على خلايا تحتوي على بيانات تم تحديدها من قبل المستخدم، ومن بين هذه الطرق نوقش بشكل أكثر تفصيلًا أدناه.  

{{% alert color="primary" %}}  
تعيد جميع طرق البحث مراجع الخلايا التي تحتوي على البيانات المحددة.  
{{% /alert %}}  

## **العثور على الخلايا التي تحتوي على صيغة**  

يمكن للمطورين العثور على صيغة محددة في ورقة العمل من خلال استدعاء مجموعة [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) وطريقة [**find**](https://reference.aspose.com/cells/javascript-cpp/cells/#find-object-cell-findoptions-) الخاصة بها. عادةً، تقبل طريقة [**find**](https://reference.aspose.com/cells/javascript-cpp/cells/#find-object-cell-findoptions-) ثلاثة معلمات:  

-  الكائن الذي تريد البحث عنه. يجب أن يكون النوع int أو double أو DateTime أو string أو bool.  
- خلايا سابقة تحتوي على نفس الكائن. يمكن تعيين هذا المعامل إلى null إذا كانت العملية من البداية.  
- خيارات للعثور على الكائن المطلوب.  

تستخدم الأمثلة أدناه بيانات ورقة العمل لممارسة طرق البحث:  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Find Cell Containing Formula</title>
    </head>
    <body>
        <h1>Find Cell Containing Formula</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FindOptions, LookInType } = AsposeCells;

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

            // Instantiating a Workbook object by opening the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Instantiate FindOptions Object and set to look in formulas
            const findOptions = new FindOptions();
            findOptions.lookInType = LookInType.Formulas;

            // Finding the cell containing the specified formula
            const cell = worksheet.cells.find("=SUM(A5:A10)", null, findOptions);

            // Displaying the name of the cell found after searching worksheet
            document.getElementById('result').innerHTML = `<p style="color: green;">Name of the cell containing formula: ${cell.name}</p>`;
        });
    </script>
</html>
```  


## **العثور على البيانات أو الصيغ باستخدام FindOptions**  

من الممكن العثور على القيم المحددة باستخدام طريقة [**Cells.find(object, Cell)**](https://reference.aspose.com/cells/javascript-cpp/cells/#find-object-cell-) من مجموعة [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) مع عدة [**FindOptions**](https://reference.aspose.com/cells/javascript-cpp/findoptions). عادةً، تقبل طريقة [**find**](https://reference.aspose.com/cells/javascript-cpp/cells/#find-object-cell-findoptions-) المعلمات التالية:  

- **قيمة البحث**, البيانات أو القيمة التي يتم البحث عنها.  
- **الخلية السابقة**, آخر خلية احتوت على نفس القيمة. يمكن تعيين هذه المعلمة إلى قيمة null عند البحث من البداية.  
- **خيارات البحث**, خيارات البحث.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Find Using FindOptions</title>
    </head>
    <body>
        <h1>Find Using FindOptions Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, FindOptions, CellArea, LookInType, LookAtType } = AsposeCells;

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

            // Calculate formulas in workbook
            workbook.calculateFormula();

            // Get Cells collection from first worksheet
            const cells = workbook.worksheets.get(0).cells;

            // Instantiate FindOptions Object
            const findOptions = new FindOptions();

            // Create a Cells Area
            const ca = new CellArea();
            ca.startRow = 8;
            ca.startColumn = 2;
            ca.endRow = 17;
            ca.endColumn = 13;

            // Set cells area for find options
            findOptions.range = ca;

            // Set searching properties
            findOptions.searchBackward = false;
            findOptions.searchOrderByRows = true;

            // Set the lookintype, you may specify, values, formulas, comments etc.
            findOptions.lookInType = LookInType.Values;

            // Set the lookattype, you may specify Match entire content, endswith, startswith etc.
            findOptions.lookAtType = LookAtType.EntireContent;

            // Find the cell with value
            const cell = cells.find(341, null, findOptions);

            if (cell !== null) {
                document.getElementById('result').innerHTML = `<p>Name of the cell containing the value: ${cell.name}</p>`;
            } else {
                document.getElementById('result').innerHTML = '<p>Record not found</p>';
            }
        });
    </script>
</html>
```  


## **العثور على الخلايا التي تحتوي على قيمة سلسلة أو رقم محدد**  

من الممكن العثور على قيم نصية محددة من خلال استدعاء نفس طريقة [**find**](https://reference.aspose.com/cells/javascript-cpp/cells/#find-object-cell-findoptions-) الموجودة في مجموعة [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) مع عدة [**FindOptions**](https://reference.aspose.com/cells/javascript-cpp/findoptions).  

حدد خصائص [**FindOptions.lookInType**](https://reference.aspose.com/cells/javascript-cpp/findoptions/#lookInType-lookintype-) و [**FindOptions.lookAtType**](https://reference.aspose.com/cells/javascript-cpp/findoptions/#lookAtType-lookattype-). يوضح رمز المثال التالي كيفية استخدام هذه الخصائص للعثور على خلايا تحتوي على عدد مختلف من النصوص في **البداية** أو في **المنتصف** أو في **النهاية** لنص الخلية.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Find Examples</h1>
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

            // Instantiate the workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get Cells collection
            const cells = workbook.worksheets.get(0).cells;

            const opts = new AsposeCells.FindOptions();
            opts.lookInType = AsposeCells.LookInType.Values;
            opts.lookAtType = AsposeCells.LookAtType.EntireContent;

            let messages = '';

            // Find the cell with the input integer or double
            let cell1 = cells.find(205, null, opts);

            if (cell1 !== null) {
                messages += '<p>Name of the cell containing the value: ' + cell1.name + '</p>';
            } else {
                messages += '<p>Record not found</p>';
            }

            // Find the cell with the input string
            let cell2 = cells.find("Items A", null, opts);

            if (cell2 !== null) {
                messages += '<p>Name of the cell containing the value: ' + cell2.name + '</p>';
            } else {
                messages += '<p>Record not found</p>';
            }

            // Find the cell containing the input string (partial match)
            opts.lookAtType = AsposeCells.LookAtType.Contains;
            let cell3 = cells.find("Data", null, opts);

            if (cell3 !== null) {
                messages += '<p>Name of the cell containing the value: ' + cell3.name + '</p>';
            } else {
                messages += '<p>Record not found</p>';
            }

            document.getElementById('result').innerHTML = messages;
        });
    </script>
</html>
``` 



## **مواضيع متقدمة**  
- [العثور على الخلايا ذات النمط المحدد](/cells/ar/javascript-cpp/find-cells-with-specific-style/)  
- [العثور عما إذا كانت قيمة الخلية تبدأ بعلامة اقتباس مفردة](/cells/ar/javascript-cpp/find-if-the-cell-value-starts-with-single-quote-mark/)  
- [البحث عن البيانات باستخدام القيم الأصلية](/cells/ar/javascript-cpp/search-data-using-original-values/)

---
title: عرض وإخفاء خطوط الشبكة وعناوين الصفوف والأعمدة باستخدام جافا سكريبت عبر ++C
linktitle: إظهار وإخفاء خطوط الشبكة ورؤوس الصف والعمود
type: docs
weight: 30
url: /ar/javascript-cpp/show-and-hide-gridlines-and-row-column-headers/
description: يوفر هذا المقال رمزًا نمونه لاستخدام واجهة برمجة التطبيقات جافا سكريبت عبر ++C لإخفاء أو عرض خطوط الشبكة، وعناوين الصفوف والأعمدة في ورقة عمل إكسل برمجياً.
---

{{% alert color="primary" %}}  
يدعم Aspose.Cells إخفاء وعرض خطوط الشبكة لورقة العمل التي يكون ظهورها افتراضيًا. كما يوفر التحكم في رؤوس الصف والعمود لورقة العمل.  
{{% /alert %}}  

## **إظهار وإخفاء خطوط الشبكة**  

تحتوي جميع ورقات العمل في Excel على خطوط شبكية افتراضيًا. تساعد في تحديد الخلايا بحيث يكون من السهل إدخال البيانات في خلايا معينة. تمكِّن الخطوط الشبكية من عرض ورقة العمل كمجموعة من الخلايا، حيث يمكن تحديد كل خلية بسهولة.  

### **التحكم في رؤية خطوط الشبكة**  

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)، والتي تمثل ملف Microsoft Excel. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) على مجموعة [**Workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) تتيح للمطورين الوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) مجموعة واسعة من الخصائص والأساليب لإدارة ورقة العمل. للتحكم في ظهور خطوط الشبكة، استخدم الخاصية [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isGridlinesVisible--). [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isGridlinesVisible--) هي خاصية بوليانية، مما يعني أنها يمكن أن تخزن فقط قيمة **true** أو **false**.  

#### **جعل خطوط الشبكة مرئية**  

اجعل خطوط الشبكة مرئية عن طريق ضبط الخاصية [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isGridlinesVisible--) على **true**.  

#### **إخفاء خطوط الشبكة**  

اخفِ خطوط الشبكة عن طريق ضبط الخاصية [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isGridlinesVisible--) على **false**.  

يوجد مثال كامل أدناه يوضح استخدام الخاصية [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isGridlinesVisible--) عن طريق فتح ملف Excel (book1.xls)، إخفاء خطوط الشبكة على ورقة العمل الأولى، وحفظ الملف المعدل باسم output.xls.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Hide Gridlines Example</title>
    </head>
    <body>
        <h1>Hide Gridlines Example</h1>
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

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object
            // Opening the Excel file through the file data
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Hiding the grid lines of the first worksheet of the Excel file
            worksheet.isGridlinesVisible = false;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Gridlines hidden successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **إظهار وإخفاء رؤوس الصف والعمود**  

جميع ورقات العمل في ملف Excel مكونة من خلايا مرتبة في صفوف وأعمدة. جميع الصفوف والأعمدة لها قيم فريدة يتم استخدامها لتحديدها وتحديد الخلايا الفردية. على سبيل المثال، يتم ترقيم الصفوف - 1، 2، 3، 4، الخ. - وترتيب الأعمدة ترتيبها أبجديًا - أ، ب، ج، د، الخ. تظهر قيم الصف والعمود في الرؤوس. باستخدام Aspose.Cells، يمكن للمطورين التحكم في رؤية هذه الرؤوس للصف والعمود.  

### **التحكم في رؤية ورقات العمل**  

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)، تمثل ملف إكسل من مايكروسوفت. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) على مجموعة [**Workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) تسمح للمطورين بالوصول إلى كل ورقة عمل في ملف إكسل. يتم تمثيل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) مجموعة واسعة من الخصائص والطرق لإدارة ورقة العمل. للتحكم في ظهور رؤوس الصفوف والأعمدة، استخدم خاصية [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isRowColumnHeadersVisible--). [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isRowColumnHeadersVisible--) هو خاصية من نوع Boolean، مما يعني أنه يمكنها فقط تخزين قيمة **true** أو **false**.  

#### **جعل رؤوس الصف/العمود مرئية**  

اجعل رؤوس الصفوف والأعمدة مرئية عن طريق تعيين خاصية [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isRowColumnHeadersVisible--) إلى **true**.  

#### **إخفاء رؤوس الصف/العمود**  

اخفِ رؤوس الصفوف والأعمدة عن طريق تعيين خاصية [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isRowColumnHeadersVisible--) إلى **false**.  

يوضح المثال الكامل أدناه كيفية استخدام الخاصية [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isRowColumnHeadersVisible--) عن طريق فتح ملف إكسل (book1.xls)، وإخفاء رؤوس الصفوف والأعمدة على ورقة العمل الأولى، وحفظ الملف المُعدّل باسم output.xls.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Hide Row/Column Headers</title>
    </head>
    <body>
        <h1>Hide Row and Column Headers Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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

            // Instantiating a Workbook object with the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Hiding the headers of rows and columns
            worksheet.isRowColumnHeadersVisible = false;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Headers hidden successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

{{% alert color="primary" %}}  
من الممكن أيضًا استخدام طريقتي [**Cells.unhideRows(number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#unhideRows-number-number-number-) و [**Cells.unhideColumns(number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#unhideColumns-number-number-number-) من الفئة [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) لجعل صفوف وأعمدة متعددة مرئية.  
{{% /alert %}}

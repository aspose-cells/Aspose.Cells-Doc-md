---
title: توافق الصفوف والأعمدة تلقائيًا مع جافا سكريبت عبر C++
linktitle: ضبط تلقائي للصفوف والأعمدة
type: docs
weight: 20
url: /ar/javascript-cpp/autofit-rows-and-columns/
description: توضح هذه المقالة كيفية توافق الصفوف والأعمدة، الصفوف، الصفوف من الخلايا المدمجة، والصف في نطاق خلايا باستخدام Aspose.Cells for JavaScript عبر C++.
keywords: توافق الصفوف تلقائيًا باستخدام جافا سكريبت عبر C++، توافق الأعمدة تلقائيًا باستخدام جافا سكريبت عبر C++، توافق الصف في نطاق خلايا باستخدام جافا سكريبت عبر C++، توافق صفوف الخلايا المدمجة باستخدام جافا سكريبت عبر C++
---

{{% alert color="primary" %}}  
يسمح Microsoft Excel للمستخدمين بتعديل عرض وارتفاع الخلايا تلقائيًا وفقًا لمحتواها. تتوفر هذه الميزة أيضًا عبر Aspose.Cells for JavaScript عبر C++، بحيث يمكن للمطورين ضبط أبعاد الخلية تلقائيًا أثناء التشغيل.  
{{% /alert %}}  

## **ضبط تلقائي**  

توفر Aspose.Cells فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) التي تمثل ملف Microsoft Excel. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) على مجموعة [**Workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) التي تتيح الوصول إلى كل ورقة عمل في ملف إكسل. تمثل ورقة العمل بالفئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) مجموعة واسعة من الخصائص والأساليب لإدارة ورقة العمل. يستعرض هذا المقال استخدام الفئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) للتحجيم التلقائي للصفوف أو الأعمدة.  

### **ضبط تلقائي للصف - بسيط**  

أبسط طريقة لضبط عرض وارتفاع الصف تلقائيًا هي استدعاء طريقة [**autoFitRow**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitRow-number-) لفئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). تأخذ طريقة [**autoFitRow**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitRow-number-) مؤشر صف (للصف الذي سيتم تغيير حجمه) كمعامل.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - AutoFit Row</title>
    </head>
    <body>
        <h1>AutoFit Row Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file through the buffer
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Auto-fitting the 3rd row of the worksheet (row index 1 is the 2nd row; original code used 1)
            worksheet.autoFitRow(1);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Row auto-fitted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

### **كيفية ضبط صف تلقائيًا في مجموعة من الخلايا**  

 يتكون الصف من العديد من الأعمدة. يسمح Aspose.Cells للمطورين بضبط صف تلقائيًا استنادًا إلى المحتوى في نطاق خلايا داخل الصف عن طريق استدعاء إصدار محمل زائد من طريقة [**autoFitRow**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitRow-number-number-number-). وهي تأخذ المعاملات التالية:  

- **فهرس الصف**, فهرس الصف المراد ضبطه تلقائياً.  
- **فهرس العمود الأول**, فهرس العمود الأول للصف.  
- **فهرس العمود الأخير**, فهرس العمود الأخير للصف.  

 تتحقق طريقة [**autoFitRow**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitRow-number-number-number-) من محتويات جميع الأعمدة في الصف ثم تضبط الصف تلقائيًا.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - AutoFit Row</title>
    </head>
    <body>
        <h1>Auto-Fit Row Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file through the file buffer
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Auto-fitting the 3rd row of the worksheet (row index 1, startColumn 0, endColumn 5)
            worksheet.autoFitRow(1, 0, 5);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Row auto-fitted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

### **كيفية ضبط العمود تلقائيًا في مجموعة من الخلايا**  

 العمود يتكون من العديد من الصفوف. من الممكن التحقق من التحجيم التلقائي لعمود استنادًا إلى المحتوى في نطاق من الخلايا في العمود من خلال استدعاء نسخة مفرطة التحميل من أسلوب [**autoFitColumn**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitColumn-number-) الذي يأخذ المعلمات التالية:  

- **فهرس العمود**: فهرس العمود الذي سيتم تلائم حجمه تلقائياً.  
- **فهرس الصف الأول**: فهرس أول صف في العمود.  
- **فهرس الصف الأخير**: فهرس آخر صف في العمود.  

 تتحقق طريقة [**autoFitColumn**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitColumn-number-) من محتويات جميع الصفوف في العمود ثم تضبط العمود تلقائيًا.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells AutoFit Column Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Auto-fitting the Column of the worksheet (column index 4)
            worksheet.autoFitColumn(4);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Column auto-fitted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

### **كيفية تلائم حجم الصفوف للخلايا المدمجة**  

 مع Aspose.Cells، من الممكن التحجيم التلقائي للصفوف حتى للخلايا المدمجة باستخدام واجهة برمجة التطبيقات [**AutoFitterOptions**](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions). توفر فئة [**AutoFitterOptions**](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions) الخاصية [**AutoFitterOptions.autoFitMergedCellsType()**](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions/#autoFitMergedCellsType--) التي يمكن استخدامها لتحجيم الصفوف للخلايا المدمجة. يقبل [**AutoFitterOptions.autoFitMergedCellsType()**](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions/#autoFitMergedCellsType--) مجموعة [**AutoFitMergedCellsType**](https://reference.aspose.com/cells/javascript-cpp/autofitmergedcellstype) القابلة للعد التي تحتوي على الأعضاء التالية.  

- لا شيء: تجاهل الخلايا المدمجة.  
- السطر الأول: فقط يوسع ارتفاع الصف الأول.  
- السطر الأخير: فقط يوسع ارتفاع الصف الأخير.  
- كل سطر: يوسع ارتفاع كل صف.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Autofit Rows for Merged Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, AutoFitterOptions, AutoFitMergedCellsType } = AsposeCells;

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

            // Create or load workbook
            let wb;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                wb = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                wb = new Workbook();
            }

            // Get the first (default) worksheet
            const worksheet = wb.worksheets.get(0);

            // Create a range A1:B1
            const range = worksheet.cells.createRange(0, 0, 1, 2);

            // Merge the cells
            range.merge();

            // Insert value to the merged cell A1
            const cell = worksheet.cells.get(0, 0);
            cell.value = "A quick brown fox jumps over the lazy dog. A quick brown fox jumps over the lazy dog....end";

            // Create a style object
            const style = cell.style;

            // Set wrapping text on
            style.isTextWrapped = true;

            // Apply the style to the cell
            cell.style = style;

            // Create an object for AutoFitterOptions
            const options = new AutoFitterOptions();

            // Set auto-fit for merged cells
            options.autoFitMergedCellsType = AutoFitMergedCellsType.EachLine;

            // Autofit rows in the sheet (including the merged cells)
            worksheet.autoFitRows(options);

            // Save the Excel file
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'AutofitRowsforMergedCells.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

{{% alert color="primary" %}}  
يمكنك أيضًا محاولة استخدام النسخ المفرطة التحميل لأساليب [**autoFitRows**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitRows-number-number-AutoFitterOptions-) و [**autoFitColumns**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitColumns-number-number-AutoFitterOptions-) لقبول نطاق من الصفوف/الأعمدة ونسخة من [**AutoFitterOptions**](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions) لتحجيم الصفوف/الأعمدة المختارة حسب [**AutoFitterOptions**](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions) المرغوب.  

التواقيع للطرق المذكورة سابقًا هي كما يلي:  

1. autoFitRows(int startRow, int endRow, [**AutoFitterOptions**](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions) options)  
1. autoFitColumns(int firstColumn, int lastColumn, [**AutoFitterOptions**](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions) options)  
{{% /alert %}}  

## **مهم معرفته**  

{{% alert color="primary" %}}  
إذا تم دمج خلية، فلن يتم تطبيق أساليب التحجيم التلقائي، وهو نفس السلوك في Microsoft Excel. يمكنك تجاوز ذلك باستخدام واجهة برمجة تطبيقات autofilter. علاوة على ذلك، إذا كان النص في خلية ملتفًا، فلن يتم تطبيق أسلوب [**autoFitColumn**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitColumn-number-) أيضًا. شيء آخر تحتاج إلى معرفته هو أن أساليب *autoFit* تتطلب وقتًا. لذا، يجب استدعاؤها بأقل قدر ممكن لضمان كفاءة تطبيقك.  
{{% /alert %}}  

## **مواضيع متقدمة**  
- [تلائم حجم الصفوف للخلايا المدمجة](/cells/ar/javascript-cpp/autofit-rows-for-merged-cells/)

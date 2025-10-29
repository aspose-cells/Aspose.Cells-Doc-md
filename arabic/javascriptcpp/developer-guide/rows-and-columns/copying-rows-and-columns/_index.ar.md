---
title: نسخ الصفوف والأعمدة باستخدام جافا سكريبت عبر C++
linktitle: نسخ الصفوف والأعمدة
type: docs
weight: 40
url: /ar/javascript-cpp/copying-rows-and-columns/
description: يوضح هذا المقال كيفية نسخ الصفوف والأعمدة من خلال Aspose.Cells for JavaScript عبر واجهة برمجة التطبيقات C++. 
keywords: جافاسكرابت عبر C++، كيفية نسخ الصفوف والأعمدة، نسخ الصفوف في جافاسكرابت، نسخ الأعمدة باستخدام جافاسكرابت، كيفية لصق الصفوف والأعمدة باستخدام Aspose.Cells for JavaScript عبر C++، لصق صفوف وأعمدة متعددة، كيفية نسخ ولصق صف أو عمود واحد. 
---

## **مقدمة**  

في بعض الأحيان, قد تحتاج إلى نسخ الصفوف والأعمدة في ورقة العمل دون نسخ الورقة بأكملها. مع Aspose.Cells, من الممكن نسخ الصفوف والأعمدة داخل المصنف أو بين المصنفات.  
عند نسخ صف (أو عمود), يتم نسخ البيانات الموجودة فيه, بما في ذلك الصيغ - بالمراجع المحدثة - والقيم, التعليقات, التنسيق, الخلايا المخفية, الصور, وغيرها من الكائنات التوضيحية.  

## **كيفية نسخ الصفوف والأعمدة باستخدام Microsoft Excel**  

1. حدد الصف أو العمود الذي ترغب في نسخه.  
1. لنسخ الصفوف أو الأعمدة, انقر **نسخ** على شريط الأدوات **قياسي**, أو اضغط **CTRL**+**C**.  
1. حدد صفًا أو عمودًا أسفل أو إلى اليمين من المكان الذي تريد نسخ تحديدك.  
1. عند نسخ الصفوف أو الأعمدة, انقر **الخلايا المنسوخة** على قائمة **إدراج**.  

{{% alert color="primary" %}}  
إذا قمت بالنقر على **لصق** على شريط الأدوات **قياسي** أو ضغط **CTRL**+**V** بدلاً من النقر على أمر في قائمة **إدراج**, فإن أي محتويات خلايا الوجهة يتم استبدالها.  
{{% /alert %}}  

## **كيفية لصق الصفوف والأعمدة باستخدام خيارات اللصق مع Microsoft Excel**  

1. حدد الخلايا التي تحتوي على البيانات أو السمات الأخرى التي تريد نسخها.  
1. في علامة التبويب الرئيسية, انقر **نسخ**.  
1. انقر على الخلية الأولى في المنطقة التي ترغب في **لصق** ما نسخته.  
1. على علامة التبويب الرئيسية، انقر فوق السهم المجاور لـ **لصق**, ثم حدد **لصق** خاص.  
1. حدد **الخيارات** التي تريدها.  

## **كيفية نسخ الصفوف والأعمدة باستخدام Aspose.Cells for JavaScript عبر C++**  

## **كيفية نسخ صفوف فردية**  

توفر Aspose.Cells أسلوب [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRow-cells-number-number-) من فئة [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells). هذا الأسلوب ينسخ جميع أنواع البيانات بما في ذلك الصيغ والقيم والتعليقات وتنسيقات الخلايا والخلايا المخفية والصور والكائنات الأخرى من الصف المصدر إلى الصف الوجهة.  

تأخذ طريقة [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRow-cells-number-number-) المعلمات التالية:  

- كائن [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) المصدر،  
- فهرس الصف المصدر، و  
- فهرس الصف الوجهة.  

استخدم هذا الأسلوب لنسخ صف داخل ورقة أو إلى ورقة أخرى. يعمل أسلوب [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRow-cells-number-number-) بطريقة مماثلة لبرنامج Microsoft Excel. على سبيل المثال، لا تحتاج إلى تعيين ارتفاع الصف الوجهة بشكل صريح، حيث يتم نسخه أيضًا.  

يظهر المثال التالي كيفية نسخ صف في ورقة العمل. يستخدم ملف إكسل نموذج وينسخ الصف الثاني (بما في ذلك البيانات والتنسيق والتعليقات والصور وما إلى ذلك) ويلصقه في الصف 12 في نفس ورقة العمل.  

يمكنك تخطي الخطوة التي تحصل على ارتفاع صف المصدر باستخدام طريقة [**Cells.rowHeight(number, boolean, CellsUnitType)**](https://reference.aspose.com/cells/javascript-cpp/cells/#rowHeight-number-boolean-cellsunittype-) ثم تعيين ارتفاع صف الوجهة باستخدام طريقة [**Cells.rowHeight(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#rowHeight-number-number-) حيث أن طريقة [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRow-cells-number-number-) تتولى الأمر تلقائيًا.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Copy Row</title>
    </head>
    <body>
        <h1>Copy Row Example</h1>
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

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet in the workbook.
            const wsTemplate = workbook.worksheets.get(0);

            // Copy the second row (index 1) with data, formatting, images and drawing objects
            // To the 16th row (index 15) in the worksheet.
            wsTemplate.cells.copyRow(wsTemplate.cells, 1, 15);

            // Save the excel file in Excel97To2003 format (.xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Row copied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

{{% alert color="primary" %}}  
عند نسخ الصفوف، من المهم ملاحظة الصور المتصلة، الرسوم البيانية أو العناصر الرسومية الأخرى لأن هذا هو نفس الأمر مع برنامج Microsoft Excel:  

1. إذا كان مؤشر الصف الأصلي هو 5، فإن الصورة، الرسم البياني، إلخ، تُنسخ إذا كانت موجودة في الثلاثة صفوف (مؤشر الصف البداية هو 4 ومؤشر الصف النهاية هو 6).  
1. لن يتم إزالة الصور الموجودة، الرسوم البيانية، إلخ في الصف الوجهة.  
{{% /alert %}}  

## **كيفية نسخ عدة صفوف**  

يمكنك أيضًا نسخ عدة صفوف إلى وجهة جديدة أثناء استخدام طريقة [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRows-cells-number-number-number-) التي تأخذ معلمة إضافية من نوع صحيح لتحديد عدد الصفوف المصدر التي سيتم نسخها.  

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

            // Instantiate workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the cells collection of first worksheet
            const cells = workbook.worksheets.get(0).cells;

            // Copy the first 3 rows to 7th row (indexes are zero-based)
            cells.copyRows(cells, 0, 6, 3);

            // Save the result and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Rows copied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **كيفية نسخ الأعمدة**  

توفر Aspose.Cells طريقة [**Cells.copyColumn(Cells, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyColumn-cells-number-number-) من فئة [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)، هذه الطريقة تنسخ جميع أنواع البيانات، بما في ذلك الصيغ - مع المراجع المحدّثة - والقيم، والتعليقات، وتنسيقات الخلايا، والخلايا المخفية، والصور وغيرها من عناصر الرسم من عمود المصدر إلى عمود الوجهة.  

تأخذ طريقة [**Cells.copyColumn(Cells, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyColumn-cells-number-number-) المعلمات التالية:  

- كائن [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) المصدر،  
- فهرس العمود المصدر، و  
- فهرس العمود الوجهة.  

استخدم طريقة [**Cells.copyColumn(Cells, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyColumn-cells-number-number-) لنسخ عمود داخل ورقة عمل أو إلى ورقة أخرى.  

هذا المثال ينسخ عمودًا من ورقة العمل ويلصقه في ورقة عمل في دفتر عمل آخر.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Copy Column Example</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object using the uploaded file
            const excelWorkbook1 = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet in the book.
            const ws1 = excelWorkbook1.worksheets.get(0);

            // Copy the first column from the first worksheet into the third column of the same worksheet.
            const cells = ws1.cells;
            cells.copyColumn(cells, cells.columns.get(0).index, cells.columns.get(2).index);

            // Autofit the column.
            ws1.autoFitColumn(2);

            // Save the excel file (Excel97To2003 format for .xls)
            const outputData = excelWorkbook1.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **كيفية نسخ عمود متعدد**  

مماثلة لطريقة [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRows-cells-number-number-number-)، توفر واجهات برمجة التطبيقات Aspose.Cells أيضًا طريقة [**Cells.copyColumns(Cells, number, number, number, PasteOptions)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyColumns-cells-number-number-number-pasteoptions-) لنسخ عدة أعمدة مصدر إلى موقع جديد.  

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

            // Create an instance of Workbook class by loading the existing spreadsheet
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet's cells collection
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;

            // Copy the first 3 columns to the 7th column
            cells.copyColumns(cells, 0, 6, 3);

            // Save the result and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **كيفية لصق الصفوف والأعمدة مع خيارات اللصق**  

توفر Aspose.Cells الآن [**PasteOptions**](https://reference.aspose.com/cells/javascript-cpp/pasteoptions/) أثناء استخدام الوظائف [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRows-cells-number-number-number-) و [**Cells.copyColumns(Cells, number, number, number, PasteOptions)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyColumns-cells-number-number-number-pasteoptions-). يسمح بضبط خيار اللصق المناسب بشكل مماثل لبرنامج Excel.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Change Chart Data Source</title>
    </head>
    <body>
        <h1>Change Chart Data Source Example</h1>
        <p>Select an Excel file (sampleChangeChartDataSource.xlsx) from your local machine.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PasteType, CopyOptions, PasteOptions } = AsposeCells;

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

            // Access the first sheet which contains chart
            const source = workbook.worksheets.get(0);

            // Add another sheet named DestSheet
            const destination = workbook.worksheets.add("DestSheet");

            // Set CopyOptions.ReferToDestinationSheet to true
            const options = new CopyOptions();
            options.referToDestinationSheet = true;

            // Set PasteOptions
            const pasteOptions = new PasteOptions();
            pasteOptions.pasteType = PasteType.Values;
            pasteOptions.onlyVisibleCells = true;

            // Copy all the rows of source worksheet to destination worksheet which includes chart as well
            // The chart data source will now refer to DestSheet
            destination.cells.copyRows(source.cells, 0, 0, source.cells.maxDisplayRange.rowCount, options, pasteOptions);

            // Save workbook in xlsx format and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputChangeChartDataSource.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

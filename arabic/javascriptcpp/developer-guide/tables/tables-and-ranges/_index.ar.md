---
title: جداول ونطاقات باستخدام JavaScript عبر C++
linktitle: الجداول والنطاقات
type: docs
weight: 50
url: /ar/javascript-cpp/tables-and-ranges/
---

## **مقدمة**  

أحيانًا تقوم بإنشاء جدول في برنامج Microsoft Excel ولا ترغب في الاستمرار في استخدام وظائف الجدول الخاصة به. بدلاً من ذلك، ترغب في شيء يبدو وكأنه جدول. للحفاظ على البيانات في جدول دون فقدان التنسيق، قم بتحويل الجدول إلى نطاق عادي من البيانات.  
يدعم Aspose.Cells هذه الميزة في برنامج Microsoft Excel للجداول وكائنات القوائم.  

## **استخدام Microsoft Excel**  

استخدم ميزة **تحويل إلى نطاق** لتحويل الجدول إلى نطاق بسرعة دون فقدان التنسيق. في Microsoft Excel 2007/2010:  

1. انقر في أي مكان في الجدول للتأكد من أن الخلية النشطة في عمود الجدول.  
1. في علامة التبويب **التصميم**، في مجموعة **الأدوات**، انقر فوق **تحويل إلى نطاق**.  

## **استخدام Aspose.Cells**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Convert Table to Range</title>
    </head>
    <body>
        <h1>Convert Table to Range Example</h1>
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

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet and convert the first table/list object to a normal range
            const worksheet = workbook.worksheets.get(0);
            const listObject = worksheet.listObjects.get(0);
            listObject.convertToRange();

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Table converted to range successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

{{% alert color="primary" %}}  

لا تعود ميزات الجداول متاحة بعد تحويل الجدول إلى نطاق. على سبيل المثال، لم تعد رؤوس الصفوف تحتوي على السهام للفرز والتصفية، والإشارات المنظمة (المشار إليها باستخدام أسماء الجدول) التي تم استخدامها في الصيغ تتحول إلى مراجع خلية عادية.  

{{% /alert %}}  

## **تحويل الجدول إلى نطاق بخيارات**  

يوفر Aspose.Cells خيارات إضافية أثناء تحويل الجدول إلى نطاق من خلال فئة [**TableToRangeOptions**](https://reference.aspose.com/cells/javascript-cpp/tabletorangeoptions/). توفر الفئة [**TableToRangeOptions**](https://reference.aspose.com/cells/javascript-cpp/tabletorangeoptions/) خاصية [**lastRow**](https://reference.aspose.com/cells/javascript-cpp/tabletorangeoptions/#lastRow--) التي تتيح لك تعيين الفهرس الأخير لصف الجدول. سيتم الاحتفاظ بتنسيق الجدول حتى الفهرس المحدد لصف، وسيتم إزالة بقية التنسيق.  

يظهر الشيفرة المثالية أدناه كيفية استخدام الفئة [**TableToRangeOptions**](https://reference.aspose.com/cells/javascript-cpp/tabletorangeoptions/).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Table to Range Example</title>
    </head>
    <body>
        <h1>Convert Table to Range Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TableToRangeOptions, Utils } = AsposeCells;

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
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create TableToRangeOptions and set lastRow property
            const options = new TableToRangeOptions();
            options.lastRow = 5;

            // Convert the first table/list object (from the first worksheet) to normal range
            workbook.worksheets.get(0).listObjects.get(0).convertToRange(options);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Table converted to range successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

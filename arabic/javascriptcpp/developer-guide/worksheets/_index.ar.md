---
title: إدارة أوراق العمل لملفات Microsoft Excel باستخدام JavaScript عبر C++
linktitle: أوراق العمل
type: docs
weight: 90
url: /ar/javascript-cpp/manage-worksheets/
description: إضافة، إزالة، وتنشيط أوراق العمل باستخدام Aspose.Cells for JavaScript عبر C++.
---

{{% alert color="primary" %}}
يمكن للمطورين إنشاء وإدارة أوراق العمل بشكل سهل في ملفات مايكروسوفت إكسل برمجيًا باستخدام واجهة برمجة التطبيقات المرنة لـ Aspose.Cells. يصف هذا الموضوع الطرق لإضافة وإزالة أوراق العمل في ملفات مايكروسوفت إكسل.
{{% /alert %}}

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) والتي تمثل ملف إكسل. تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) على مجموعة [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) والتي تتيح الوصول إلى كل ورقة عمل داخل ملف إكسل.

تمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) مجموعة واسعة من الخصائص والطرق لإدارة أوراق العمل.

## **إضافة ورقات العمل إلى ملف Excel جديد**

لإنشاء ملف Excel جديد برمجياً:

1. إنشاء كائن من فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook).  
2. استدعِ طريقة [**WorksheetCollection.add(SheetType)**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#add-sheettype-) من فئة [**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection). يُضاف ورقة عمل فارغة تلقائيًا إلى ملف Excel. يمكن الرجوع إليها عن طريق تمرير مؤشر الورقة إلى مجموعة [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--).  
3. الحصول على مرجع الورقة.  
4. تنفيذ العمل على أوراق العمل.  
5. حفظ ملف Excel الجديد مع أوراق العمل الجديدة عن طريق استدعاء طريقة [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-) من فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Add Worksheet Example</h1>
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

            // Get current worksheet count (converted from getWorksheets().getCount())
            const i = workbook.worksheets.count;

            // Add a new worksheet (converted from getWorksheets().add())
            workbook.worksheets.add();

            // Obtain the newly added worksheet by index (converted from getWorksheets().get(i))
            const worksheet = workbook.worksheets.get(i);

            // Set the name of the newly added worksheet (converted from setName)
            worksheet.name = "My Worksheet";

            // Save the workbook to XLS format and prepare download
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and saved. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **إضافة ورقات عمل إلى جدول التصميم**

عملية إضافة أوراق العمل إلى جدول تصميمي هي نفسها عملية إضافة ورقة عمل جديدة، باستثناء أن ملف إكسل موجود مسبقًا ويجب فتحه قبل إضافة أوراق العمل. يمكن فتح ملف جدول التصميم بواسطة فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Worksheet</title>
    </head>
    <body>
        <h1>Add Worksheet Example</h1>
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

            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Adding a new worksheet to the Workbook object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Setting the name of the newly added worksheet
            worksheet.name = "My Worksheet";

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **الوصول إلى الأوراق العمل باستخدام اسم الورقة**

الوصول إلى أي ورقة عمل عن طريق تحديد اسمها أو فهرسها.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example: Read Cell Value</h1>
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

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing a worksheet using its sheet name
            const worksheet = workbook.worksheets.get("Sheet1");
            const cell = worksheet.cells.get("A1");

            console.log(cell.value);
            document.getElementById('result').innerHTML = `<p>Cell A1 value: ${cell.value}</p>`;
        });
    </script>
</html>
```

## **إزالة الأوراق العمل باستخدام اسم الورقة**

لإزالة أوراق العمل من ملف، استدعِ طريقة [**WorksheetCollection.removeAt(string)**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#removeAt-string-) من فئة [**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection). مرر اسم الورقة إلى طريقة [**WorksheetCollection.removeAt(string)**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#removeAt-string-) لإزالة ورقة عمل محددة.

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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object
            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Removing a worksheet using its sheet name
            workbook.worksheets.removeAt("Sheet1");

            // Save workbook
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **إزالة الأوراق العمل باستخدام فهرس الورقة**

إزالة أوراق العمل بواسطة الاسم تعمل بشكل جيد عندما يكون اسم ورقة العمل معروفًا. إذا لم تعرف اسم ورقة العمل، استخدم نسخة محمّلة من طريقة [**WorksheetCollection.removeAt(string)**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#removeAt-string-) التي تأخذ فهرس الورقة بدلاً من اسمها.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Remove First Worksheet</h1>
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

            // Instantiating a Workbook object
            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Removing a worksheet using its sheet index
            workbook.worksheets.removeAt(0);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **تنشيط الأوراق وجعل خلية نشطة في ورقة العمل**

أحيانًا، تحتاج إلى أن تكون ورقة عمل معينة نشطة ومعروضة عند فتح مستخدم لملف إكسل من مايكروسوفت إكسل. بالمثل، قد ترغب في تفعيل خلية معينة وضبط أشرطة التمرير لعرض الخلية النشطة. قادر على Aspose.Cells على القيام بجميع هذه المهام.

ورقة العمل النشطة هي الورقة التي تعمل عليها: اسم الورقة النشطة على علامة التبويب يكون سميك افتراضيًا.

الخلية النشطة هي الخلية المحددة، الخلية التي يتم إدخال البيانات فيها عند بدء الكتابة. تكون خلية واحدة فقط نشطة في وقت واحد. يتم تمييز الخلية النشطة بحد ثقيل.

### **تفعيل الأوراق وجعل خلية نشطة**

توفر Aspose.Cells استدعاءات API محددة لتفعيل ورقة وخلية. على سبيل المثال، خاصية [**WorksheetCollection.activeSheetIndex**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#activeSheetIndex--) مفيدة لضبط الورقة النشطة في دفتر العمل. بالمثل، تُستخدم خاصية [**Worksheet.activeCell**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#activeCell--) لضبط والحصول على خلية نشطة في ورقة العمل.

للتأكد من أن أشرطة التمرير الأفقية أو الرأسية في موضع الفهرس الصف والعمود الذي تريد إظهار البيانات المحددة، استخدم خاصيتي [**Worksheet.firstVisibleRow**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#firstVisibleRow--) و [**Worksheet.firstVisibleColumn**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#firstVisibleColumn--).

تُظهر الشفرة المثالية التالية كيفية تفعيل ورقة عمل وجعل خلية نشطة فيها. في الناتج المولد، ستتم تمرير أشرطة التمرير لجعل الصف الثاني والعمود الثاني أول صف وعمود مرئيين لديها.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Create Workbook Example</h1>
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

            // Add a worksheet if collection is empty
            const worksheets = workbook.worksheets;
            if (worksheets.count === 0) {
                worksheets.add();
            }

            // Get the first worksheet in the workbook.
            const worksheet1 = worksheets.get(0);

            // Get the cells in the worksheet.
            const cells = worksheet1.cells;

            // Input data into B2 cell.
            const cell = cells.get(1, 1);
            cell.value = "Hello World!";

            // Set the first sheet as an active sheet.
            worksheets.activeSheetIndex = 0;

            // Set B2 cell as an active cell in the worksheet.
            worksheet1.activeCell = "B2";

            // Set the B column as the first visible column in the worksheet.
            worksheet1.firstVisibleColumn = 1;

            // Set the 2nd row as the first visible row in the worksheet.
            worksheet1.firstVisibleRow = 1;

            // Save the excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **مواضيع متقدمة**
- [نسخ ونقل أوراق العمل](/cells/ar/javascript-cpp/copying-and-moving-worksheets/)  
- [عدد الخلايا في ورقة العمل](/cells/ar/javascript-cpp/count-number-of-cells-in-the-worksheet/)  
- [الكشف عن ورق العمل الفارغة](/cells/ar/javascript-cpp/detecting-empty-worksheets/)  
- [العثور على ورقة العمل هل هي ورقة حوار](/cells/ar/javascript-cpp/find-if-the-worksheet-is-dialog-sheet/)  
- [الحصول على معرف فريد لورقة العمل](/cells/ar/javascript-cpp/get-worksheet-unique-id/)  
- [إنشاء أو تلاعب أو إزالة السيناريوهات من ورقات العمل](/cells/ar/javascript-cpp/create-manipulate-or-remove-scenarios-from-worksheets/)  
- [إدارة فواصل الصفحات](/cells/ar/javascript-cpp/managing-page-breaks/)  
- [ميزات إعداد الصفحة](/cells/ar/javascript-cpp/page-setup-features/)  
- [الاستفادة من خاصية Sheet.SheetId في الشكل المفتوحXML باستخدام Aspose.Cells](/cells/ar/javascript-cpp/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)  
- [عروض ورقة العمل](/cells/ar/javascript-cpp/worksheet-views/)

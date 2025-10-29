---
title: ترتيب البيانات
type: docs
weight: 130
url: /ar/javascript-cpp/sort-data-of-excel/
description: تعلم كيف تصف البيانات باستخدام Aspose.Cells for JavaScript عبر واجهة برمجة التطبيقات C ++.
keywords: فرز البيانات بترتيب تصاعدي أو تنازلي، فرز البيانات بناءً على لون الخلفية
---

{{% alert color="primary" %}}

 تصفية البيانات هي واحدة من العديد من الميزات المفيدة في Microsoft Excel. تتيح للمستخدمين ترتيب البيانات لجعلها أسهل للمسح. يتيح Aspose.Cells for JavaScript عبر C ++ للمطورين فرز بيانات ورقة العمل أبجديًا أو رقميًا، وهو مشابه لكيفية فرز البيانات في Microsoft Excel.

{{% /alert %}}

## **فرز البيانات في Microsoft Excel**

لفرز البيانات في Microsoft Excel:

1. حدد **البيانات** من قائمة **الترتيب**. سيتم عرض مربع الحوار للترتيب.
1. حدد خيار الفرز.

عموماً، يتم إجراء الفرز على قائمة - المعرفة بأنها مجموعة متواصلة من البيانات حيث يتم عرض البيانات في أعمدة.

## **فرز البيانات مع Aspose.Cells**

 يوفر Aspose.Cells for JavaScript عبر C ++ فئة [**DataSorter**](https://reference.aspose.com/cells/javascript-cpp/datasorter) المستخدمة لفرز البيانات في ترتيب تصاعدي أو تنازلي. تحتوي هذه الفئة على بعض الأعضاء المهمة، على سبيل المثال، الخصائص مثل Key1 ... Key3 و Order1 ... Order3. تُستخدم هذه الأعضاء لتعريف مفاتيح الفرز وتحديد ترتيب فرز المفتاح.

يجب عليك تعريف المفاتيح وتعيين ترتيب الفرز قبل تنفيذ فرز البيانات. توفر الفئة الطريقة [**DataSorter.sort**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#sort-cells-cellarea-) المستخدمة لأداء فرز البيانات بناءً على بيانات الخلية في ورقة العمل.

تقبل الطريقة [**DataSorter.sort**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#sort-cells-cellarea-) البيانات التالية:

- [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)، الخلايا للورقة العمل الأساسية.
- [**CellArea**](https://reference.aspose.com/cells/javascript-cpp/cellarea)، نطاق الخلايا. قم بتحديد منطقة الخلية قبل تطبيق فرز البيانات.

يستخدم هذا المثال ملف القالب "Book1.xls" الذي تم إنشاؤه في Microsoft Excel. بعد تنفيذ الكود أدناه، يتم فرز البيانات بشكل مناسب.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>DataSorter Example</title>
    </head>
    <body>
        <h1>DataSorter Example</h1>
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

            // Instantiate a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the workbook datasorter object.
            const sorter = workbook.dataSorter;

            // Set the first order for datasorter object.
            sorter.order1 = AsposeCells.SortOrder.Descending;
            // Define the first key.
            sorter.key1 = 0;
            // Set the second order for datasorter object.
            sorter.order2 = AsposeCells.SortOrder.Ascending;
            // Define the second key.
            sorter.key2 = 1;

            // Create a cells area (range).
            const ca = new AsposeCells.CellArea();
            // Specify the start row index.
            ca.startRow = 0;
            // Specify the start column index.
            ca.startColumn = 0;
            // Specify the last row index.
            ca.endRow = 13;
            // Specify the last column index.
            ca.endColumn = 1;

            // Sort data in the specified data range (A1:B14)
            sorter.sort(workbook.worksheets.get(0).cells, ca);

            // Save the excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Sorting completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

إذا كنت ترغب في فرز *من اليسار إلى اليمين*، استخدم السمة [**DataSorter.sortLeftToRight**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#sortLeftToRight-boolean-).

{{% /alert %}}

### **فرز البيانات مع لون الخلفية**

 يقدم Excel ميزات لفرز البيانات بناءً على لون الخلفية. يتم توفير نفس الميزة باستخدام Aspose.Cells for JavaScript عبر C ++ باستخدام DataSorter حيث يمكن استخدام [**SortOnType**](https://reference.aspose.com/cells/javascript-cpp/sortontype/).CellColor في [**DataSorter.addKey**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#addColorKey-number-sortontype-sortorder-color-) لفرز البيانات استنادًا إلى لون الخلفية. يتم وضع جميع الخلايا التي تحتوي على اللون المحدد في [**DataSorter.addKey**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#addColorKey-number-sortontype-sortorder-color-) في الأعلى أو الأسفل وفقًا لإعداد SortOrder، ولا يتغير ترتيب باقي الخلايا على الإطلاق.

فيما يلي الملفات العينية التي يمكن تنزيلها لاختبار هذه الميزة:

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Custom Sort by Cell Color</title>
    </head>
    <body>
        <h1>Custom Sort by Cell Color Example</h1>
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

            // Access the data sorter (converted from getDataSorter())
            const sorter = workbook.dataSorter;

            // Add key for second column for red color
            sorter.addKey(1, AsposeCells.SortOnType.CellColor, AsposeCells.SortOrder.Descending, AsposeCells.Color.Red);

            // Perform the sort on the first worksheet cells (converted from getWorksheets().get(0).getCells())
            sorter.sort(workbook.worksheets.get(0).cells, AsposeCells.CellArea.createCellArea("A2", "C6"));

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSortData_CustomSortList.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Sorted Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Sorting completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **مواضيع متقدمة**
- [فرز البيانات في العمود بقائمة فرز مخصصة](/cells/ar/javascript-cpp/sort-data-in-column-with-custom-sort-list/)
- [تحديد تحذير الفرز أثناء فرز البيانات](/cells/ar/javascript-cpp/specifying-sort-warning-while-sorting-data/)

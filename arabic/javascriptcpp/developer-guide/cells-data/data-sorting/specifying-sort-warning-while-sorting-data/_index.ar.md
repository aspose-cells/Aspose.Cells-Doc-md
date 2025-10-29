---
title: تحديد تحذير الفرز أثناء فرز البيانات
type: docs
weight: 140
url: /ar/javascript-cpp/specifying-sort-warning-while-sorting-data/
description: تعلم كيفية تحديد تحذير الترتيب أثناء فرز البيانات باستخدام Aspose.Cells for JavaScript عبر API C++.
keywords: إضافة تحذير الفرز عند فرز البيانات، تعيين تحذير الفرز أثناء فرز البيانات، حدد تحذير الفرز عند فرز البيانات.
---

## **سيناريوهات الاستخدام المحتملة**

 يرجى مراعاة هذه البيانات النصية أي {11، 111، 22}. يتم ترتيب هذه البيانات النصية لأنه من حيث النص، يأتي 111 قبل 22. ولكن، إذا كنت تريد فرز هذه البيانات كأرقام وليست كنص، فستصبح {11، 22، 111} لأن 111 يأتي بعد 22 رقميًا. يوفر Aspose.Cells for JavaScript عبر C++ خاصية {0} للتعامل مع هذه المشكلة. يرجى تعيين هذه الخاصية على **true** وسيتم فرز بياناتك النصية كبيانات رقمية. يُظهر لقطة الشاشة التالية التحذير من الترتيب الذي يظهره Microsoft Excel عندما يتم فرز بيانات نصية تبدو كبيانات رقمية.

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

## **الكود المثالي**

الكود المصدري العينة التالي يوضح استخدام الخاصية [**DataSorter.sortAsNumber**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#sortAsNumber-boolean-) كما هو موضح سابقا. يرجى الاطلاع على [ملف Excel عينة](43352075.xlsx) و [ملف الإخراج Excel](43352076.xlsx) لمزيد من المساعدة.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Sort As Number Example</title>
    </head>
    <body>
        <h1>Sort As Number Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellsHelper, CellArea, SortOrder } = AsposeCells;

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

            // Create your cell area.
            const ca = AsposeCells.CellArea.createCellArea("A1", "A20");

            // Create your sorter.
            const sorter = workbook.dataSorter;

            // Find the index for column A.
            const idx = CellsHelper.columnNameToIndex("A");

            // Add key in sorter, it will sort in Ascending order.
            sorter.addKey(idx, SortOrder.Ascending);

            // Set sort as number
            sorter.sortAsNumber = true;

            // Perform sort.
            sorter.sort(worksheet.cells, ca);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSortAsNumber.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Sort completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

---
title: فرز البيانات في العمود بقائمة فرز مخصصة
type: docs
weight: 290
url: /ar/javascript-cpp/sort-data-in-column-with-custom-sort-list/
description: تعلم كيفية ترتيب البيانات في العمود باستخدام قائمة مخصصة باستخدام Aspose.Cells for JavaScript عبر API C++.
keywords: فرز البيانات في العمود باستخدام قائمة الفرز المخصصة، فرز البيانات حسب القائمة المخصصة.
---

## **سيناريوهات الاستخدام المحتملة**

يمكنك فرز البيانات في العمود باستخدام قائمة مخصصة. يمكن القيام بذلك باستخدام [**DataSorter.addKey**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#addKey-number-sortorder-string-). ومع ذلك، فإن هذه الطريقة تعمل فقط إذا لم يكن لدى العناصر في القائمة المخصصة فواصل داخلها. إذا كانت تحتوي على فواصل مثل "USA,US"، "China,CN" وغيرها، فلابد من استخدام [**DataSorter.addKey(number, SortOrder, string[])**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#addKey-number-sortorder-stringarray-). هنا، المعامل الأخير ليس سلسلة نصية بل هو مصفوفة من السلاسل النصية.

## **فرز البيانات في العمود بقائمة فرز مخصصة**

يوضح رمز العينة التالي كيفية استخدام طريقة [**DataSorter.addKey(number, SortOrder, string[])**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#addKey-number-sortorder-stringarray-) لفرز البيانات باستخدام القائمة الفرزية المخصصة. يرجى الاطلاع على [ملف إكسل العينة](50528327.xlsx) المستخدم في هذا الرمز و[ملف إكسل الناتج](50528328.xlsx) الناتج عنه. يظهر لقطة الشاشة التالية تأثير الكود على ملف إكسل العينة عند التنفيذ.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Custom Sort List</title>
    </head>
    <body>
        <h1>Custom Sort List Example</h1>
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

            // Instantiating a Workbook object from uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Specify cell area - sort from A1 to A40
            const ca = AsposeCells.CellArea.createCellArea("A1", "A40");

            // Create Custom Sort list
            const customSortList = ["USA,US", "Brazil,BR", "China,CN", "Russia,RU", "Canada,CA"];

            // Add Key for Column A, Sort it in Ascending Order with Custom Sort List
            wb.dataSorter.addKey(0, AsposeCells.SortOrder.Ascending, customSortList);

            wb.dataSorter.sort(ws.cells, ca);

            // Save the output Excel file
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSortData_CustomSortList.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Sorting completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

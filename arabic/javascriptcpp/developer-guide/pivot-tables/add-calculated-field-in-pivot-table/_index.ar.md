---
title: إضافة حقل محسوب في جدول الدوران
type: docs
weight: 130
url: /ar/javascript-cpp/add-calculated-field-in-pivot-table/
description: كيفية إضافة حقل محسوب في جدول محوري باستخدام Aspose.Cells for JavaScript عبر C++.
keywords: Aspose.Cells for JavaScript عبر C++ مكتبة Excel، مكتبة JavaScript لـ Excel، إضافة حقل محسوب في جدول محوري باستخدام مكتبة Excel JavaScript.
---

## **سيناريوهات الاستخدام المحتملة**
عند إنشاء جدول دوران استنادًا إلى بيانات معروفة، تجد أن البيانات فيه ليست كما تريد. البيانات التي تريدها هي مجموعة من هذه البيانات الأصلية. على سبيل المثال، قد تحتاج إلى جمع، أو طرح، أو ضرب، وقسمة البيانات الأصلية قبل أن ترغب في البيانات. في هذا الوقت، تحتاج إلى بناء حقل محسوب وتعيين الصيغة المقابلة للحساب. ثم قم بإجراء بعض الإحصائيات والعمليات الأخرى على الحقل المحسوب. 

## **كيفية إضافة حقل محسوب في جدول النفث في إكسل**
لإدراج حقل محسوب في جدول دوران في Excel، اتبع الخطوات التالية:

1. حدد جدول الدوران الذي تريد إضافة حقل محسوب إليه. 
2. انتقل إلى علامة تبويب تحليل جدول الدوران على شريط القوائم.
3. انقر على "الحقول والعناصر والمجموعات" ثم حدد "حقل محسوب" من القائمة المنسدلة.
4. في حقل الاسم، أدخل اسمًا للحقل المحسوب.
5. في حقل "Formula"، ادخل الصيغة للحساب الذي ترغب في القيام به باستخدام أسماء الحقول المحورية المناسبة والعمليات الرياضية. 
<br>
<img src="1.png" width=80% />
6. انقر "موافق" لإنشاء الحقل المحسوب.
7. سيظهر الحقل المحسوب الجديد في قائمة حقل PivotTable تحت قسم القيم.
8. اسحب الحقل المحسوب إلى قسم القيم في PivotTable لعرض القيم المحسوبة.
<br>
<img src="2.png" width=80% />

## **كيفية إضافة حقل محسوب في جدول محوري باستخدام Aspose.Cells for JavaScript عبر مكتبة C++**
إضافة حقل محسوب إلى ملف إكسل باستخدام Aspose.Cells for JavaScript عبر C++. يرجى الاطلاع على الكود النموذجي التالي. بعد تنفيذ الكود، يتم إضافة جدول محوري مع حقل محسوب إلى ورقة العمل.
1. حدد البيانات الأصلية وأنشئ جدول محوري. 
2. أنشئ الحقل المحسوب وفقًا لحقل PivotField الحالي في الجدول المحوري.
3. أضف الحقل المحسوب إلى منطقة البيانات. 
4. أخيرًا، يحفظ الدفتر بتنسيق [XLSX الناتج](out.xlsx). 

## **الكود المثالي**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>PivotTable Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PivotFieldType, Utils } = AsposeCells;

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

            // Obtain the reference of the newly added worksheet
            const ws = workbook.worksheets.get(0);
            const cells = ws.cells;

            // Setting the value to the cells (converted putValue -> value)
            let cell = cells.get("A1");
            cell.value = "Fruit";
            cell = cells.get("B1");
            cell.value = "Count";
            cell = cells.get("C1");
            cell.value = "Price";
            cell = cells.get("A2");
            cell.value = "Apple";
            cell = cells.get("A3");
            cell.value = "Mango";
            cell = cells.get("A4");
            cell.value = "Blackberry";
            cell = cells.get("A5");
            cell.value = "Cherry";
            cell = cells.get("B2");
            cell.value = 5;
            cell = cells.get("B3");
            cell.value = 3;
            cell = cells.get("B4");
            cell.value = 6;
            cell = cells.get("B5");
            cell.value = 4;
            cell = cells.get("C2");
            cell.value = 5;
            cell = cells.get("C3");
            cell.value = 20;
            cell = cells.get("C4");
            cell.value = 30;
            cell = cells.get("C5");
            cell.value = 60;

            // Adding a PivotTable to the worksheet (converted getPivotTables -> pivotTables)
            const i = ws.pivotTables.add("=A1:C5", "D10", "PivotTable1");
            // Accessing the instance of the newly added PivotTable
            const pivotTable = ws.pivotTables.get(i);
            pivotTable.addFieldToArea(PivotFieldType.Row, 0);
            // Adding a calculated field to PivotTable and drag it to data area.
            pivotTable.addCalculatedField("total", "=Count*Price", true);
            pivotTable.refreshData();
            pivotTable.calculateData();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PivotTable created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

---
title: مسح الفلتر في الجدول الدوري Pivot
type: docs
weight: 130
url: /ar/javascript-cpp/clear-filter-in-pivot-table/
description: كيفية مسح فلتر الجدول المحوري من الحقل المحوري المحدد باستخدام Aspose.Cells for JavaScript عبر C++.
keywords: Aspose.Cells for JavaScript عبر C++ إكسل، مكتبة جافا سكريبت إكسل، مسح فلتر الجدول المحوري باستخدام Aspose.Cells for JavaScript عبر مكتبة إكسل C++.
---

## **سيناريوهات الاستخدام المحتملة**
عندما تنشئ جدول محوري ببيانات معروفة وتريد تصفية الجدول المحوري، عليك أن تتعلم وتستخدم الفلتر. يمكنه مساعدتك في تصفية البيانات التي تريدها بفعالية. باستخدام واجهة برمجة التطبيقات Aspose.Cells for JavaScript عبر C++، يمكنك تشغيل الفلتر على قيم الحقول في الجداول المحورية. 

## **كيفية مسح الفلتر في الجدول المحوري في Excel**
مسح الفلتر في الجدول الدوري Pivot في Excel، اتبع هذه الخطوات:

1. حدد الجدول الدوري Pivot الذي تريد مسح الفلتر منه. 
2. انقر على السهم المنسدل للفلتر الذي تريد مسحه في الجدول الدوري Pivot.
3. حدد "مسح الفلتر" من القائمة المنسدلة.
<img src="1.png" width=80% />
4. إذا كنت ترغب في مسح جميع الفلاتر من الجدول الدوري Pivot، يمكنك أيضًا النقر فوق زر "مسح الفلاتر" في علامة PivotTable Analyze في شريط الشريط في Excel.
<img src="2.png" width=80% />

## **كيفية مسح الفلتر في الجدول المحوري باستخدام Aspose.Cells for JavaScript عبر C++**
مسح الفلتر في الجدول المحوري باستخدام Aspose.Cells for JavaScript عبر C++. يرجى الاطلاع على الكود النموذجي التالي. 
1. ضع البيانات وأنشئ جدول محوري استنادًا إليها. 
2. أضف تصفيةً إلى حقل الصف في الجدول المحوري. 
3. احفظ الدفتر في تنسيق [XLSX الناتج](out_add.xlsx). بعد تنفيذ الشيفرة المثالية، سيتم إضافة جدول محوري مع تصفية أعلى 10 إلى ورقة العمل. 
4. أمسح التصفية على حقل محدد في الجدول المحوري. بعد تنفيذ الشيفرة لمسح التصفية، سيتم مسح التصفية على الحقل المحدد. يرجى التحقق من [XLSX الناتج](out_delete.xlsx).

## **الكود المثالي**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells PivotTable Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <div>
            <a id="downloadLinkAdd" style="display: none; margin-right: 10px;">Download Pivot Added File</a>
            <a id="downloadLinkDelete" style="display: none;">Download Pivot Filter Cleared File</a>
        </div>
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
            document.getElementById('result').innerHTML = '<p>Running example...</p>';

            // Create a new workbook
            const workbook = new Workbook();
            // Obtaining the reference of the newly added worksheet
            const ws = workbook.worksheets.get(0);
            const cells = ws.cells;

            // Setting the value to the cells
            let cell = cells.get("A1");
            cell.value = "Fruit";
            cell = cells.get("B1");
            cell.value = "Count";
            cell = cells.get("A2");
            cell.value = "Apple";
            cell = cells.get("A3");
            cell.value = "Mango";
            cell = cells.get("A4");
            cell.value = "Blackberry";
            cell = cells.get("A5");
            cell.value = "Cherry";
            cell = cells.get("A6");
            cell.value = "Guava";
            cell = cells.get("A7");
            cell.value = "Carambola";
            cell = cells.get("A8");
            cell.value = "Banana";
            cell = cells.get("B2");
            cell.value = 5;
            cell = cells.get("B3");
            cell.value = 3;
            cell = cells.get("B4");
            cell.value = 6;
            cell = cells.get("B5");
            cell.value = 4;
            cell = cells.get("B6");
            cell.value = 5;
            cell = cells.get("B7");
            cell.value = 2;
            cell = cells.get("B8");
            cell.value = 20;

            // Adding a PivotTable to the worksheet
            const i = ws.pivotTables.add("=A1:B8", "D10", "PivotTable1");
            // Accessing the instance of the newly added PivotTable
            const pivotTable = ws.pivotTables.get(i);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Count");
            pivotTable.dataFields.get(0).function = AsposeCells.ConsolidationFunction.Sum;

            const field = pivotTable.rowFields.get(0);
            field.isAutoSort = true;
            field.isAscendSort = false;
            field.autoSortField = 0;

            // Add top10 filter
            const index = pivotTable.pivotFilters.add(field.baseIndex, AsposeCells.PivotFilterType.Count);
            const filter = pivotTable.pivotFilters.get(index);
            filter.autoFilter.filterTop10(0, true, false, 5);
            pivotTable.refreshData();
            pivotTable.calculateData();

            // Save workbook after adding pivot/filter
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLinkAdd = document.getElementById('downloadLinkAdd');
            downloadLinkAdd.href = URL.createObjectURL(blob);
            downloadLinkAdd.download = 'out_add.xlsx';
            downloadLinkAdd.style.display = 'inline-block';
            downloadLinkAdd.textContent = 'Download out_add.xlsx';

            document.getElementById('result').innerHTML = '<p style="color: green;">Pivot table created and top10 filter applied. Download the file with pivot added.</p>';

            // Clear PivotFilter from the specific PivotField
            pivotTable.pivotFilters.clearFilter(field.baseIndex);
            pivotTable.refreshData();
            pivotTable.calculateData();

            // Save workbook after clearing filter
            const outputData2 = workbook.save(SaveFormat.Xlsx);
            const blob2 = new Blob([outputData2]);
            const downloadLinkDelete = document.getElementById('downloadLinkDelete');
            downloadLinkDelete.href = URL.createObjectURL(blob2);
            downloadLinkDelete.download = 'out_delete.xlsx';
            downloadLinkDelete.style.display = 'inline-block';
            downloadLinkDelete.textContent = 'Download out_delete.xlsx';

            document.getElementById('result').innerHTML += '<p style="color: green;">Pivot filter cleared and data recalculated. Download the file with filter removed.</p>';
        });
    </script>
</html>
```

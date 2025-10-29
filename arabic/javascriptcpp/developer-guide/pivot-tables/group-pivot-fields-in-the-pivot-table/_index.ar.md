---
title: تجميع حقول الجدول المحوري في جدول الدوران
type: docs
weight: 80
url: /ar/javascript-cpp/group-pivot-fields-in-the-pivot-table/
description: كيفية تجميع حقول Pivot في الجدول المحوري باستخدام Aspose.Cells for JavaScript عبر C++.
keywords: Aspose.Cells for JavaScript عبر C++ مكتبة Excel، JavaScript لـ Excel، كيفية تجميع حقول Pivot في الجدول المحوري باستخدام Aspose.Cells for JavaScript عبر مكتبة Excel لـ C++.
---

## **سيناريوهات الاستخدام المحتملة**

يتيح لك Microsoft Excel تجميع حقول النقاط في جدول المحوري. عندما يكون هناك حجم كبير من البيانات المتعلقة بحقل محوري، غالبًا ما يكون من المفيد تجميعها في أقسام. Aspose.Cells for JavaScript عبر C++ يوفر أيضًا هذه الميزة باستخدام طريقة [**PivotTable.groupBy()**](https://reference.aspose.com/cells/javascript-cpp/pivotfield/#groupBy-date-date-pivotgroupbytypearray-number-boolean-).

## **كيفية تجميع حقول الجدول المحوري**

يقوم الكود العيني التالي بتحميل ملف الإكسل العيني وينفذ عمليات التجميع على الحقل المحوري الأول باستخدام طريقة [**PivotTable.groupBy()**](https://reference.aspose.com/cells/javascript-cpp/pivotfield/#groupBy-date-date-pivotgroupbytypearray-number-boolean-). ثم يقوم بتحديث وحساب بيانات الجدول المحوري ويحفظ الدفتر كملف إكسل جديد. توضح الصورة الناتجة تأثير الكود العيني على ملف الإكسل العيني. كما يظهر في الصورة، تم تجميع الحقل المحوري الأول الآن حسب الشهور والربع.

![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Group Pivot Fields Example</title>
    </head>
    <body>
        <h1>Group Pivot Fields in PivotTable</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PivotGroupByType } = AsposeCells;

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

            // Load workbook from uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Access the second worksheet
            const ws = wb.worksheets.get(1);

            // Access the pivot table
            const pt = ws.pivotTables.get(0);

            // Specify the start and end date time
            const dtStart = new Date(2008, 1, 1);
            const dtEnd = new Date(2008, 9, 5);

            // Specify the group type list, we want to group by months and quarters
            const groupTypeList = [PivotGroupByType.Months, PivotGroupByType.Quarters];

            // Apply the grouping on first pivot field
            const field = pt.rowFields.get(0);
            field.groupBy(dtStart, dtEnd, groupTypeList, 1, true);

            // Refresh and calculate pivot table
            pt.refreshDataFlag = true;
            pt.refreshData();
            pt.calculateData();
            pt.refreshDataFlag = false;

            // Save the output Excel file
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputGroupPivotFieldsInPivotTable.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

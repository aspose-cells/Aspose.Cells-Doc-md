---
title: كيفية ضبط محور الفئة مع جافا سكريبت عبر ++C
linktitle: كيفية تعيين محور الفئة
description: تعلم كيفية ضبط محور الفئة في Aspose.Cells for JavaScript عبر ++C. دليلنا سيساعدك على فهم كيفية تحديد مدى محور الفئة، تعديل خصائصه، وتنسيق تسمياتهم.
keywords: Aspose.Cells for JavaScript عبر ++C، محور الفئة، التحديد، المدى، الخصائص، التنسيق.
type: docs
weight: 205
url: /ar/javascript-cpp/how-to-set-category-axis/
---

## **سيناريوهات الاستخدام المحتملة**
 بعد إنشاء رسم بياني في ورقة عمل، يمكنك ضبط محور الفئة له. في هذا المقال، سنوضح كيفية ضبط محور الفئة لرسوم بيانية في إكسل باستخدام Aspose.Cells for JavaScript عبر ++C مع رمز نموذج.

## **الخطوات في رمز العينة**

1. إنشاء ورقة عمل جديدة.

2. إنشاء مخطط جديد في الورقة العمل الأولى.

3. إضافة بعض القيم إلى الخلايا في الورقة العمل الأولى.

4. الآن يمكنك تعيين محور الفئة؛ هناك طريقتان: باستخدام بيانات الخلية أو باستخدام السلاسل النصية مباشرة، وكلاهما موضح في الكود النموذجي.

5. اضبط محور القيمة، واحفظ دفتر العمل لعرض النتيجة.

## **الكود المثالي**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType, LegendPositionType, Utils } = AsposeCells;

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
            // Create a new workbook
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "CHART";

            // Add a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Column, 8, 0, 20, 10);
            const chart = worksheet.charts.get(chartIndex);

            // Add some values to cells
            worksheet.cells.get("A1").putValue("Sales");
            worksheet.cells.get("A2").putValue(100);
            worksheet.cells.get("A3").putValue(150);
            worksheet.cells.get("A4").putValue(130);
            worksheet.cells.get("A5").putValue(160);
            worksheet.cells.get("A6").putValue(150);
            worksheet.cells.get("B1").putValue("Days");
            worksheet.cells.get("B2").putValue(1);
            worksheet.cells.get("B3").putValue(2);
            worksheet.cells.get("B4").putValue(3);
            worksheet.cells.get("B5").putValue(4);
            worksheet.cells.get("B6").putValue(5);

            // Some values in string
            const Sales = "100,150,130,160,150";
            const Days = "1,2,3,4,5";

            // Set Category Axis Data with string
            chart.nSeries.categoryData = `{${Days}}`;
            // Or you can set Category Axis Data with data in cells
            // chart.nSeries.categoryData = "B2:B6";

            // Add Series to the chart
            chart.nSeries.add("Demand1", true);
            // Set value axis with string 
            chart.nSeries.get(0).values = `{${Sales}}`;
            chart.nSeries.add("Demand2", true);
            // Set value axis with data in cells
            chart.nSeries.get(1).values = "A2:A6";

            // Set some Category Axis properties
            chart.categoryAxis.tickLabels.rotationAngle = 45;
            chart.categoryAxis.tickLabels.font.size = 8;
            chart.legend.position = LegendPositionType.Bottom;

            // Save the workbook to view the result file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

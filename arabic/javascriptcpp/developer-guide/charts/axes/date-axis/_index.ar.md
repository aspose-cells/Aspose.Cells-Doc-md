---
title: محور التاريخ مع JavaScript عبر C++
description: تعلم كيفية إدارة محور التاريخ في Aspose.Cells for JavaScript عبر C++. دليلنا سيساعدك في فهم كيفية العمل مع تنسيقات التاريخ المختلفة، مقاييس الزمن، وتواتر تسميات العلامات.
keywords: Aspose.Cells for JavaScript عبر C++، محور التاريخ، إدارة، تنسيقات التاريخ، مقاييس الوقت، تواتر تسميات العلامات.
type: docs
weight: 200
url: /ar/javascript-cpp/date-axis/
---

## **سيناريوهات الاستخدام المحتملة**
عند إنشاء مخطط من بيانات ورقة العمل التي تستخدم التواريخ، وتُرسم التواريخ على طول المحور الأفقي (الفئة) في المخطط، يقوم Aspose.Cells for JavaScript عبر C++ تلقائياً بتغيير محور الفئة إلى محور تاريخ (مقياس زمني).
يعرض محور التاريخ التواريخ وفقًا للترتيب الزمني بفواصل زمنية محددة أو وحدات قاعدية، مثل عدد الأيام، أو الأشهر، أو السنوات، حتى إذا كانت التواريخ على ورقة العمل ليست بترتيب تسلسلي أو بنفس الوحدات القاعدية.
افتراضيًا، تحدد Aspose.Cells الوحدات الأساسية لمحور التاريخ استنادًا إلى أصغر فرق بين أي تاريخين في بيانات ورقة العمل. على سبيل المثال، إذا كانت لديك بيانات لأسعار الأسهم حيث يكون أقل اختلاف بين التواريخ سبعة أيام، فإن Excel يضبط الوحدة الأساسية على أيام، ويمكنك تغيير الوحدة الأساسية إلى أشهر أو سنوات إذا رغبت في رؤية أداء السهم على مدى أطول.

## **معاملة محور التاريخ مثل Microsoft Excel**
 يرجى مراجعة رمز العينة التالي الذي ينشئ ملف إكسل جديد ويضع قيم الرسم البياني في ورقة العمل الأولى. 
ثم نضيف رسم بياني ونعين نوع الـ [**Axis**](https://reference.aspose.com/cells/javascript-cpp/axis/) 
إلى [**Axis.categoryType**](https://reference.aspose.com/cells/javascript-cpp/axis/#categoryType--) ومن ثم نضبط الوحدات الأساسية على الأيام.

![todo:image_alt_text](excel.png)

## **الكود المثالي**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Date Axis Chart Example</title>
    </head>
    <body>
        <h1>Date Axis Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType, CategoryType, TimeUnit, ChartTextDirectionType, FillType } = AsposeCells;

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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Shortcut to cells collection
            const cells = worksheet.cells;

            // Add the sample values to cells
            cells.get("A1").value = "Date";

            // 14 means datetime format
            const style = cells.style;
            style.number = 14;

            // Put values to cells for creating chart
            const cellA2 = cells.get("A2");
            cellA2.style = style;
            cellA2.value = new Date(Date.UTC(2022, 5, 26));

            const cellA3 = cells.get("A3");
            cellA3.style = style;
            cellA3.value = new Date(Date.UTC(2022, 4, 22));

            const cellA4 = cells.get("A4");
            cellA4.style = style;
            cellA4.value = new Date(Date.UTC(2022, 7, 3));

            cells.get("B1").value = "Price";
            cells.get("B2").value = 40;
            cells.get("B3").value = 50;
            cells.get("B4").value = 60;

            // Add a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Column, 9, 6, 21, 13);
            // Access the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Add SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
            // Converted setter to property assignment (range and boolean passed as array)
            chart.chartDataRange = ["A1:B4", true];

            // Set the Axis type to Date time
            chart.categoryAxis.categoryType = CategoryType.TimeScale;
            // Set the base unit for CategoryAxis to days
            chart.categoryAxis.baseUnitScale = TimeUnit.Days;
            // Set the direction for the axis text to be vertical
            chart.categoryAxis.tickLabels.directionType = ChartTextDirectionType.Vertical;
            // Fill the PlotArea area with nothing 
            chart.plotArea.area.fillFormat.fillType = FillType.None;
            // Set max value of Y axis.
            chart.valueAxis.maxValue = 70;
            // Set major unit.
            chart.valueAxis.majorUnit = 10;

            // Saving the modified Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'DateAxis.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

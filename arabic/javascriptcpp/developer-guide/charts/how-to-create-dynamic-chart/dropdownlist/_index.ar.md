---
title: كيفية إنشاء رسم بياني ديناميكي باستخدام قائمة منسدلة باستخدام JavaScript عبر C++
linktitle: كيفية إنشاء رسم بياني ديناميكي مع قائمة منسدلة
description: تعلم كيفية إنشاء رسم بياني ديناميكي يتحدث استنادًا إلى اختيار من قائمة منسدلة باستخدام Aspose.Cells for JavaScript عبر C++. سيُظهر دليلنا خطوة بخطوة كيفية دمج قائمة منسدلة في الرسم الخاص بك لتصور بيانات مرن.
keywords: Aspose.Cells for JavaScript عبر C++، رسم بياني ديناميكي، قائمة منسدلة، تصور البيانات، التكامل، تصور مرن.
type: docs
weight: 76
url: /ar/javascript-cpp/create-dynamic-chart-with-dropdownlist/
---

## **سيناريوهات الاستخدام المحتملة**
رسم بياني ديناميكي مع قائمة منسدلة في إكسل هو أداة قوية تتيح للمستخدمين إنشاء رسوم بيانية تفاعلية يمكن تحديثها بناءً على البيانات المحددة. تكون هذه الميزة مفيدة بشكل خاص في الحالات التي تحتاج فيها إلى تحليل مجموعات بيانات متعددة أو مقارنة سيناريوات مختلفة.

تطبيق شائع آخر لرسم بياني ديناميكي بقائمة منسدلة في التحليل المالي. على سبيل المثال ، قد تحتوي شركة على مجموعات متعددة من البيانات المالية لسنوات أو أقسام مختلفة. من خلال استخدام قائمة منسدلة ، يمكن للمستخدمين تحديد مجموعة البيانات المحددة التي يرغبون في تحليلها ، وسيتم تحديث الرسم البياني تلقائيًا لعرض المعلومات المقابلة. يُسمح بذلك بسهولة المقارنة والتعرف على الاتجاهات أو الأنماط.

تطبيق آخر هو في المبيعات والتسويق. قد تحتوي شركة على بيانات مبيعات لمنتجات أو مناطق مختلفة. باستخدام رسم بياني ديناميكي مع قائمة منسدلة ، يمكن للمستخدمين اختيار منتج محدد أو منطقة من القائمة المنسدلة ، وسيتم تحديث الرسم البياني بشكل ديناميكي لعرض أداء المبيعات للاختيار المحدد. يساعد ذلك في تحديد المناطق أو المنتجات الأكثر أداءً واتخاذ قرارات تستند إلى البيانات.

باختصار ، يوفر رسم بياني ديناميكي مع قائمة منسدلة في إكسل وسيلة مرنة وتفاعلية لتصور وتحليل البيانات. إنه قيم في الحالات التي تحتاج فيها إلى مقارنة مجموعات بيانات متعددة أو استكشاف سيناريوات مختلفة ، مما يجعله أداة متعددة الاستخدامات للتحليل المالي والمبيعات والتسويق والعديد من التطبيقات الأخرى.

## **استخدم Aspose Cells لإنشاء رسم بياني ديناميكي مع قائمة منسدلة**
في الفقرات التالية، سوف نوضح لك كيفية إنشاء رسم بياني ديناميكي باستخدام قائمة منسدلة باستخدام Aspose.Cells for JavaScript عبر C++. سنعرض لك الكود للمثال، بالإضافة إلى ملف Excel الذي تم إنشاؤه باستخدام هذا الكود.

## **الكود المثالي**
سيقوم الكود العيني التالي بتوليد [ملف رسم بياني ديناميكي مع قائمة منسدلة](DynamicChartWithDropdownlist.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Dynamic Chart with Dropdown List Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, ValidationType, BackgroundType, Color, ChartType } = AsposeCells;

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
            // Create a new workbook and access the first worksheet.
            const workbook = new Workbook();
            const sheets = workbook.worksheets;
            const sheet = sheets.get(0);

            // Populate the data for the chart. Add values to cells and set series names.
            sheet.cells.get("A3").putValue("Tea");
            sheet.cells.get("A4").putValue("Coffee");
            sheet.cells.get("A5").putValue("Sugar");

            // In this example, we will add 12 months of data
            sheet.cells.get("B2").putValue("Jan");
            sheet.cells.get("C2").putValue("Feb");
            sheet.cells.get("D2").putValue("Mar");
            sheet.cells.get("E2").putValue("Apr");
            sheet.cells.get("F2").putValue("May");
            sheet.cells.get("G2").putValue("Jun");
            sheet.cells.get("H2").putValue("Jul");
            sheet.cells.get("I2").putValue("Aug");
            sheet.cells.get("J2").putValue("Sep");
            sheet.cells.get("K2").putValue("Oct");
            sheet.cells.get("L2").putValue("Nov");
            sheet.cells.get("M2").putValue("Dec");
            const allMonths = 12;
            const iCount = 3;
            for (let i = 0; i < iCount; i++) {
                for (let j = 0; j < allMonths; j++) {
                    const _row = i + 2;
                    const _column = j + 1; 
                    sheet.cells.get(_row, _column).putValue(50 * (i % 2) + 20 * (j % 3) + 10 * (i / 3) + 10);
                }
            }

            // This is the Dropdownlist for Dynamic Data
            const ca = CellArea.createCellArea(9, 0, 9, 0);
            const _index = sheet.validations.add(ca);
            const _va = sheet.validations.get(_index);
            _va.type = ValidationType.List;
            _va.inCellDropDown = true;
            _va.formula1 = "=$B$2:$M$2";
            sheet.cells.get("A9").putValue("Current Month");
            sheet.cells.get("A10").putValue("Jan");
            const _style = sheet.cells.get("A10").style;
            _style.font.isBold = true;
            _style.pattern = BackgroundType.Solid;
            _style.foregroundColor = Color.Yellow;
            sheet.cells.get("A10").style = _style;

            // Set the dynamic range for the chart's data source. 
            let index = sheets.names.add("Sheet1!ChtMonthData");
            sheets.names.get(index).refersTo = "=OFFSET(Sheet1!$A$3,0,MATCH($A$10, $B$2:$M$2, 0),3,1)";

            // Set the dynamic range for the chart's data labels. 
            index = sheets.names.add("Sheet1!ChtXLabels");
            sheets.names.get(index).refersTo = "=Sheet1!$A$3:$A$5";

            // Create a chart object and set its data source.
            const chartIndex = sheet.charts.add(ChartType.Column, 8, 2, 20, 8);
            const chart = sheet.charts.get(chartIndex);
            chart.nSeries.add("month", true);
            chart.nSeries.get(0).name = "=Sheet1!$A$10";
            chart.nSeries.get(0).values = "Sheet1!ChtMonthData";
            chart.nSeries.get(0).xValues = "Sheet1!ChtXLabels";

            // Save the workbook as an Excel file.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'DynamicChartWithDropdownlist.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully. Click the download link to save the file.</p>';
        });
    </script>
</html>
```

## **ملاحظات**
في الملف الذي تم إنشاؤه، سيقوم الرسم البياني بحساب البيانات ديناميكيًا بالنسبة للشهر المحدد. يتم ذلك باستخدام صيغة "OFFSET" في الكود العيني:

---
title: كيفية إنشاء مخطط تقلب ديناميكي باستخدام جافا سكريبت عبر C++
linktitle: كيفية إنشاء رسم بياني ديناميكي متداول
description: تعلم كيفية إنشاء مخطط تقلب ديناميكي باستخدام Aspose.Cells for JavaScript عبر C++. سيُظهر دليلنا كيفية تنفيذ انتقالات بيانات سلسة ومتوسطات متحركة في مخططك لعرض مستمر ومُحدّث.
keywords: Aspose.Cells for JavaScript عبر C++، مخطط تقلب ديناميكي، انتقالات البيانات، متوسطات سلسة، عرض مستمر، تحديث التصور.
type: docs
weight: 74
url: /ar/javascript-cpp/create-dynamic-rolling-chart/
---

## **سيناريوهات الاستخدام المحتملة**
يشير رسم البيانات المتداول الديناميكي إلى تمثيل بياني يعرض نقاط البيانات التي تتحرك باستمرار وتحديث عبر الوقت. إنه نوع من الرسم البياني الذي يحدث نفسه باستمرار، ويعرض نافذة متداولة لأحدث نقاط البيانات بينما يتخلص من نقاط البيانات القديمة مع دخول النقاط الجديدة.

يتم استخدام رسوم بيانية متداولة ديناميكية عادةً لتصور الاتجاهات والأنماط في الوقت الفعلي أو البيانات المتدفقة. إنها مفيدة بشكل خاص في السيناريوهات التي تكون فيها الجوانب الزمنية والتغييرات عبر الوقت حرجة، مثل تحليل سوق الأسهم، مراقبة الطقس، أو تتبع الأداء الحي.

عادةً ما تستخدم هذه الرسوم البيانية آليات الرسم المتحرك أو التمرير التلقائي لضمان تقديم أحدث المعلومات دائمًا. يمكن تخصيص طول النافذة المتداولة لعرض فترة زمنية محددة، مثل الساعة الأخيرة، أو اليوم، أو الأسبوع.

في الختام، يعد رسم بياني متداول ديناميكي تمثيلًا بيانيًا محدث باستمرار يعرض أحدث نقاط البيانات مع التخلص من النقاط القديمة، مما يسمح للمستخدمين بمراقبة الاتجاهات والأنماط الفعلية.

## **استخدام Aspose Cells لإنشاء رسم بياني متداول ديناميكي**
في الفقرات التالية، سنريك كيفية إنشاء رسم بياني متداول ديناميكي باستخدام Aspose.Cells. سنريك الكود للمثال، وكذلك ملف Excel الذي تم إنشاؤه بهذا الكود.

## **الكود المثالي**
سيقوم الكود العيني التالي بتوليد [ملف رسم بياني متداول ديناميكي](DynamicRollingChart.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Dynamic Rolling Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType, Utils } = AsposeCells;

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
            sheet.cells.get("A1").value = "Month";
            sheet.cells.get("A2").value = 1;
            sheet.cells.get("A3").value = 2;
            sheet.cells.get("A4").value = 3;
            sheet.cells.get("A5").value = 4;
            sheet.cells.get("A6").value = 5;
            sheet.cells.get("A7").value = 6;
            sheet.cells.get("A8").value = 7;

            sheet.cells.get("B1").value = "Sales";
            sheet.cells.get("B2").value = 50;
            sheet.cells.get("B3").value = 45;
            sheet.cells.get("B4").value = 55;
            sheet.cells.get("B5").value = 60;
            sheet.cells.get("B6").value = 55;
            sheet.cells.get("B7").value = 65;
            sheet.cells.get("B8").value = 70;

            // Set the dynamic range for the chart's data source.
            let index = sheets.names.add("Sheet1!ChtData");
            sheets.names.get(index).refersTo = "=OFFSET(Sheet1!$B$1,COUNT(Sheet1!$B:$B),0,-5,1)";

            // Set the dynamic range for the chart's data labels.
            index = sheets.names.add("Sheet1!ChtLabels");
            sheets.names.get(index).refersTo = "=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)";

            // Create a chart object and set its data source.
            const chartIndex = sheet.charts.add(ChartType.Line, 10, 3, 25, 10);
            const chart = sheet.charts.get(chartIndex);
            chart.nSeries.add("Sales", true);
            chart.nSeries.get(0).values = "Sheet1!ChtData";
            chart.nSeries.get(0).xValues = "Sheet1!ChtLabels";

            // Save the workbook as an Excel file.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'DynamicRollingChart.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **ملاحظات**
في الملف الذي تم إنشاؤه، يمكنك متابعة إضافة البيانات في الأعمدة A و B، بينما يحسب الرسم البياني ديناميكيًا أحدث 5 مجموعات من البيانات. يتم ذلك باستخدام صيغة "OFFSET" في الكود العيني:

---
title: كيفية إنشاء مخطط تمرير ديناميكي باستخدام جافا سكريبت عبر C++
linktitle: كيفية إنشاء رسم بياني ديناميكي متدحرج
description: تعلم كيفية إنشاء مخطط تمرير ديناميكي باستخدام Aspose.Cells for JavaScript عبر C++. سيُوضح دليلنا خطوة خطوة كيفية تنفيذ انتقالات بيانات سلسة وتمرير تلقائي في مخططك لعرض مستمر ومُحدّث.
keywords: Aspose.Cells for JavaScript عبر C++، مخطط تمرير ديناميكي، انتقالات البيانات، تمرير سلس، عرض مستمر، تحديث التصور.
type: docs
weight: 75
url: /ar/javascript-cpp/create-dynamic-scrolling-chart/
---

## **سيناريوهات الاستخدام المحتملة**
رسم بياني متدحرج ديناميكي هو نوع من التمثيل البياني المستخدم لعرض البيانات التي تتغير مع مرور الوقت. تم تصميمه لتوفير رؤية في الوقت الحقيقي للبيانات، مما يتيح للمستخدمين تتبع التحديثات المستمرة والاتجاهات. يقوم الرسم البياني بالتحديث بشكل مستمر كلما تمت إضافة بيانات جديدة، ويمرر تلقائيًا لعرض أحدث المعلومات.

يتم استخدام رسوم بيانية متدحرجة ديناميكية عادة في مختلف الصناعات، مثل التمويل، وتحليل سوق الأسهم، وتتبع الطقس، وتحليل وسائل التواصل الاجتماعي. إنها تمكن المستخدمين من تصور وتحليل أنماط البيانات واتخاذ قرارات مستنيرة استنادًا إلى المعلومات في الوقت الحقيقي.

عموما، تعتبر هذه الرسوم بيانية متدحرجة ديناميكية أدوات قيمة لمراقبة وتحليل البيانات الزمنية، وتسهيل اتخاذ القرارات في الوقت الحقيقي وتعزيز القدرات على تصور البيانات.

استخدام Aspose Cells لإنشاء رسم بياني ديناميكي متدحرج

## ** استخدم Aspose.Cells لإنشاء رسم بياني متدفق ديناميكي**
في الفقرات التالية، سنوضح لك كيفية إنشاء مخطط تمرير ديناميكي باستخدام Aspose.Cells for JavaScript عبر C++. سنعرض لك كود المثال، بالإضافة إلى ملف إكسل تم إنشاؤه باستخدام هذا الكود.

## **الكود المثالي**
سينشئ الكود العينة التالي [ملف الرسم البياني الديناميكي المتدحرج](DynamicScrollingChart.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Dynamic Scrolling Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils, ChartType } = AsposeCells;

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
            sheet.cells.get("A1").value = "Day";
            sheet.cells.get("B1").value = "Sales";
            // In this example, we will add 30 days of data
            const allDays = 30;
            const showDays = 10;
            let currentDay = 1;

            for (let i = 0; i < allDays; i++) {
                const cellA = `A${i + 2}`;
                const cellB = `B${i + 2}`;
                sheet.cells.get(cellA).value = i + 1;
                sheet.cells.get(cellB).value = 50 * (i % 2) + 20 * (i % 3) + 10 * Math.floor(i / 3);
            }

            // This is the Dynamic Scrolling Control Data
            sheet.cells.get("G19").value = "Start Day";
            sheet.cells.get("G20").value = currentDay;
            sheet.cells.get("H19").value = "Show Days";
            sheet.cells.get("H20").value = showDays;

            // Set the dynamic range for the chart's data source. 
            let index = sheets.names.add("Sheet1!ChtScrollData");
            sheets.names.get(index).refersTo = "=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)";

            // Set the dynamic range for the chart's data labels. 
            index = sheets.names.add("Sheet1!ChtScrollLabels");
            sheets.names.get(index).refersTo = "=OFFSET(Sheet1!$A$2,Sheet1!$G$20,0,Sheet1!$H$20,1)";

            // Add a ScrollBar for the Dynamic Scrolling Chart
            const bar = sheet.shapes.addScrollBar(2, 0, 3, 0, 200, 30);
            bar.min = 0;
            bar.max = allDays - showDays;
            bar.currentValue = currentDay;
            bar.linkedCell = "$G$20";

            // Create a chart object and set its data source.
            const chartIndex = sheet.charts.add(ChartType.Line, 2, 4, 15, 10);
            const chart = sheet.charts.get(chartIndex);
            chart.nSeries.add("Sales", true);
            chart.nSeries.get(0).values = "Sheet1!ChtScrollData";
            chart.nSeries.get(0).xValues = "Sheet1!ChtScrollLabels";

            // Save the workbook as an Excel file.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'DynamicScrollingChart.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **ملاحظات**
في الملف الذي تم إنشاؤه، يمكنك التشغيل على شريط التمرير، في حين يقوم الرسم البياني بحساب البيانات العشر مجموعات الأحدث تلقائيًا. يتم ذلك باستخدام صيغة "OFFSET" في الكود العينة:

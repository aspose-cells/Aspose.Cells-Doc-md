---
title: كيفية إنشاء مخطط جانت باستخدام JavaScript عبر C++
linktitle: كيفية إنشاء مخطط جانت
type: docs
weight: 72
url: /ar/javascript-cpp/how-to-create-gantt-chart/
description: تعلم كيفية إنشاء مخطط جانت باستخدام Aspose.Cells for JavaScript عبر واجهة برمجة التطبيقات C++.
keywords: إنشاء مخطط جانت بواسطة JavaScript، وإضافة مخطط جانت، وإدراج مخطط جانت
---

## **ما هو مخطط جانت**

مخطط جانت هو نوع من مخططات الأعمدة يوضح جدول مشروع. يُظهر تواريخ بدء وانتهاء عناصر المشروع المختلفة. يمثل كل مهمة أو نشاط بواسطة عمود، وطوله يتوافق مع مدته. تشير مخططات جانت أيضًا إلى الاعتماديات بين المهام، مما يسمح لمديري المشاريع برؤية التسلسل الذي يجب إكمال المهام فيه. تستخدم على نطاق واسع في إدارة المشاريع لتخطيط، جدولة، وتتبع المشاريع بشكل فعال.

## **كيفية إنشاء مخطط جانت في إكسل**

يمكنك إنشاء مخطط جانت في إكسل باتباع هذه الخطوات:
1. إضافة بعض البيانات لمخطط جانت. 
<br>
<img src="00.png" width=50% />
1. اختر البيانات واذهب إلى إدراج --> مخططات --> إدراج مخطط عمود أو مخطط أعمدة --> مخطط الأعمدة المجمعة. في مثالنا، هو B1:B7، ثم إدراج مخطط **مخطط أعمدة مجمعة**.
<br>
<img src="1.png" width=50% />

1. اختر المخطط، **اختيار البيانات** -> **إضافة**، حدد **اسم السلسلة** و**قيم السلسلة** كما هو موضح أدناه.
<br>
<img src="2.png" width=50% />

1. اختر المخطط، عدل **محور البيانات الأفقي (الفئة)**.
<br>
<img src="3.png" width=50% />

1. **تنسيق المحور** للمحور الصادي، حدد **الفئات بترتيب عكسي**.
1. اختر **السلسلة الزرقاء** وضع **ملء -> لا ملء**.
1. **تنسيق محور** للمحور الأفقي، حدد **الحد الأدنى والأقصى** (1/5/2019:43470، 1/30/2019:43494).
<br>
<img src="4.png" width=50% />

1. **إضافة تسميات البيانات** للمخطط، الآن ستحصل على مخطط جانت.
<br>
<img src="0.png" width=50% />


## **كيفية إضافة مخطط جانت في Aspose.Cells**
يرجى مراجعة رمز العينة التالي. يقوم بتحميل ملف إكسل عينة ([sample.xlsx](sample.xlsx)) الذي يحتوي على بعض البيانات النموذجية. ثم ينشئ مخطط الأعمدة المجمعة استنادًا إلى البيانات الأولية ويحدد الخصائص ذات الصلة. في النهاية، يحفظ ملف العمل بصيغة XLSX الناتجة ([result.xlsx](result.xlsx)). تُظهر لقطة الشاشة التالية مخطط جانت الذي أنشأته Aspose.Cells في ملف الإكسل الناتج.
<br>
<img src="5.png" width=60% />

### **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Chart Example</title>
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
        const { Workbook, SaveFormat } = AsposeCells;

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

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Create BarStacked Chart
            const i = worksheet.charts.add(AsposeCells.ChartType.BarStacked, 5, 6, 20, 15);

            // Retrieve the Chart object
            const chart = worksheet.charts.get(i);

            // Set the chart title name 
            chart.title.text = "Gantt Chart";

            // Set the chart title is Visible
            chart.title.isVisible = true;

            // Set data range
            chart.chartDataRange = "B1:B6";

            // Add series data range
            chart.nSeries.add("C2:C6", true);

            // No fill for one serie
            chart.nSeries.get(0).area.fillFormat.fillType = AsposeCells.FillType.None;

            // Set the Horizontal(Category) Axis
            chart.nSeries.setCategoryData("A2:A6");

            // Reverse the Horizontal(Category) Axis
            chart.categoryAxis.isPlotOrderReversed = true;

            // Set the value axis's MinValue and MaxValue
            const minValue = parseFloat(worksheet.cells.get("B2").value);
            const maxValue = parseFloat(worksheet.cells.get("D6").value);
            chart.valueAxis.minValue = isNaN(minValue) ? 0 : minValue;
            chart.valueAxis.maxValue = isNaN(maxValue) ? 0 : maxValue;

            chart.plotArea.area.fillFormat.fillType = AsposeCells.FillType.None;

            // Show the DataLabels
            chart.nSeries.get(1).dataLabels.showValue = true;

            // Disable the Legend
            chart.showLegend = false;

            // Save the result
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'result.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

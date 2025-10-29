---
title: كيفية إنشاء مخطط إعصار باستخدام JavaScript عبر C++
linktitle: كيفية إنشاء رسم بياني للإعصار
type: docs
weight: 73
url: /ar/javascript-cpp/create-tornado-chart/
description: تعلم كيفية إنشاء مخطط إعصار باستخدام Aspose.Cells for JavaScript عبر API لـ C++.
keywords: إنشاء مخطط إعصار باستخدام JavaScript، وإضافة مخطط إعصار، وإدراج مخطط إعصار
---

## **مقدمة**
الرسم البياني للإعصار، المعروف أيضًا باسم الرسم البياني للإعصار أو الرسم البياني للتورنادو، هو نوع من تصور البيانات يُستخدم في التحليل الحساسية في برنامج إكسل. يساعدك على فهم تأثير تغيير المتغيرات على نتيجة معينة.

## **كيفية إنشاء رسم بياني للإعصار في إكسل**
يمكنك إنشاء رسم بياني للإعصار في إكسل من خلال اتباع هذه الخطوات:
1. حدد البيانات وانتقل إلى إدراج --> الرسوم البيانية --> إدراج رسم بياني عمودي أو شريطي --> رسم بياني عمودي مكدس. انقر عليه.
<br>
<img src="1.png" width=70% />
2. تغيير محور الصف: انقر بزر الماوس الأيمن فوق محور الصف. انقر على تنسيق المحور. في العلامات، انقر على القائمة المنسدلة لموضع العلامة وحدد العنصر المنخفض.
<br>
<img src="2.png" width=70% />
3. حدد أي شريط وانتقل إلى التنسيق. ضبط عرض الفجوة المناسب.
<br>
<img src="3.png" width=70% />
4. لنقم بإزالة علامة الناقص (-) من رسم بياني الإعصار. حدد محور السين. انتقل إلى التنسيق. في خيارات المحور، انقر على الرقم. في الفئة، حدد مخصص. في رمز التنسيق اكتب ###0،###0. انقر على إضافة.
<br>
<img src="4.png" width=70% />
5. انقر فوق محور الصف وانتقل إلى خيارات المحور. في خيارات المحور، حدد الفئات بترتيب معكوس.
<br>
<img src="5.png" width=70% />

## **كيفية إضافة مخطط إعصار في Aspose.Cells for JavaScript عبر C++**
يرجى الاطلاع على الكود النموذجي التالي. يقوم بتحميل [ملف إكسل نموذجي](sample.xlsx) الذي يحتوي على بعض البيانات النموذجية. ثم يقوم بإنشاء رسم بياني عمودي مكدس بناءً على البيانات الأولية وتعيين الخصائص ذات الصلة. في النهاية، يقوم بحفظ الدفتر إلى [تنسيق XLSX الناتج](out.xlsx). تُظهر اللقطة الشاشية التالية الرسم البياني للإعصار الذي تم إنشاؤه بواسطة Aspose.Cells في ملف الإكسل الناتج.
<br>
<img src="6.png" width=70% />

### **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xlsx" />
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const sheet = workbook.worksheets.get(0);
            const charts = sheet.charts;

            // Add bar chart
            const index = charts.add(AsposeCells.ChartType.BarStacked, 8, 1, 24, 8);
            const chart = charts.get(index);

            // Set data for bar chart
            chart.chartDataRange = "A1:C7";

            // Set properties for bar chart
            chart.title.text = "Tornado chart";
            chart.style = 2;
            chart.plotArea.area.foregroundColor = AsposeCells.Color.White;
            chart.plotArea.border.color = AsposeCells.Color.White;
            chart.legend.position = AsposeCells.LegendPositionType.Bottom;

            chart.categoryAxis.tickLabelPosition = AsposeCells.TickLabelPositionType.Low;
            chart.category```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xlsx" />
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const sheet = workbook.worksheets.get(0);
            const charts = sheet.charts;

            // Add bar chart
            const index = charts.add(AsposeCells.ChartType.BarStacked, 8, 1, 24, 8);
            const chart = charts.get(index);

            // Set data for bar chart
            chart.chartDataRange = "A1:C7";

            // Set properties for bar chart
            chart.title.text = "Tornado chart";
            chart.style = 2;
            chart.plotArea.area.foregroundColor = AsposeCells.Color.White;
            chart.plotArea.border.color = AsposeCells.Color.White;
            chart.legend.position = AsposeCells.LegendPositionType.Bottom;

            chart.categoryAxis.tickLabelPosition = AsposeCells.TickLabelPositionType.Low;
            chart.categoryAxis.isPlotOrderReversed = true;

            chart.gapWidth = 10;

            const valueAxis = chart.valueAxis;
            valueAxis.tickLabels.numberFormat = "#,##0;#,##0";

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

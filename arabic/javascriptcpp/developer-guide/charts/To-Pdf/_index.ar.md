---
title: تحويل المخطط إلى PDF باستخدام JavaScript عبر C++
linktitle: تحويل الرسم البياني إلى PDF
description: تعلم كيفية استخدام Aspose.Cells for JavaScript عبر C++ لتحويل مخطط إلى مستند PDF. يوضح دليلنا كيفية تصدير مخطط من Microsoft Excel وحفظه كمستند PDF للمزيد من التوزيع والأرشفة.
keywords: Aspose.Cells for Javaنص البرنامج النصي عبر C++، رسم بياني إلى PDF، إكسل Microsoft، تحويل PDF، تصدير، توزيع، أرشفة.
type: docs
weight: 47
url: /ar/javascript-cpp/chart-to-pdf/
---

## **عرض الرسم البياني إلى PDF**

لتحويل المخطط إلى تنسيق PDF، قامت واجهات برمجة التطبيقات Aspose.Cells بالكشف عن طريقة [**Chart.toPdf(string)**](https://reference.aspose.com/cells/javascript-cpp/chart/#toPdf-string-) مع القدرة على تخزين ملف PDF الناتج على مسار القرص أو تدفق البيانات.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Chart to PDF</title>
    </head>
    <body>
        <h1>Chart to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType } = AsposeCells;

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
            // Add a new worksheet
            const sheetIndex = workbook.worksheets.add();
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").value = 50;
            worksheet.cells.get("A2").value = 100;
            worksheet.cells.get("A3").value = 150;
            worksheet.cells.get("B1").value = 4;
            worksheet.cells.get("B2").value = 20;
            worksheet.cells.get("B3").value = 50;

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Column, 5, 0, 15, 5);
            const chart = worksheet.charts.get(chartIndex);

            // Adding Series Collection (chart data source) to the chart ranging from "A1" cell to "B3"
            chart.nSeries.add("A1:B3", true);

            // Converting chart to PDF
            const outputData = chart.toPdf();
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'chartPDF_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Chart PDF';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart converted to PDF successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```

## **إنشاء رسم بياني PDF بحجم الصفحة المطلوب**  
يمكنك إنشاء ملف PDF للمخطط بحجم الصفحة المرغوب باستخدام Aspose.Cells وتحديد كيفية محاذاة المخطط داخل الصفحة من الأعلى، الأسفل، الوسط، اليسار، اليمين، إلخ. بالإضافة إلى ذلك، يمكن إنشاء المخطط الناتج في تدفق أو على القرص. يرجى الاطلاع على المثال التالي الذي يحمّل [ملف إكسل النموذجي](64716906.xlsx)، ويصل إلى المخطط الأول داخل ورقة العمل ثم يحولها إلى [ملف PDF الناتج](64716907.pdf) بحجم الصفحة المطلوب. يوضح الصورة الملتقطة أدناه أن حجم الصفحة في ملف PDF الناتج هو 7×7 كما هو محدد داخل الكود وأن المخطط محاذى في الوسط أفقياً وعمودياً.

![todo:image_alt_text](create-chart-pdf-with-desired-page-size_1.png)  
## **الكود المثالي**  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Create Chart PDF With Desired Page Size</title>
    </head>
    <body>
        <h1>Create Chart PDF With Desired Page Size</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm" />
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Access first chart inside the worksheet.
            const chart = worksheet.charts.get(0);

            // Create chart pdf with desired page size.
            // Note: In browser API omit file path and receive output data (Uint8Array / ArrayBuffer)
            const outputData = chart.toPdf(7, 7, AsposeCells.PageLayoutAlignmentType.Center, AsposeCells.PageLayoutAlignmentType.Center);

            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputCreateChartPDFWithDesiredPageSize.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart exported to PDF successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

---
title: العثور على نوع القيم X و Y للنقاط في سلسلة المخطط باستخدام JavaScript عبر C++
linktitle: البحث عن نوع قيم X وY لنقاط في سلسلة الرسم البياني
description: تعلم كيفية تحديد نوع القيم X و Y في نقاط سلسلة المخطط باستخدام Aspose.Cells for JavaScript عبر C++. يشرح دليلنا أنواع قيم البيانات وكيفية الوصول إليها والعمل معها في مخططاتك.
keywords: Aspose.Cells for JavaScript عبر C++، رسم بياني، قيم X، قيم Y، أنواع البيانات، الوصول، العمل معها، سلسلة المخطط.
type: docs
weight: 150
url: /ar/javascript-cpp/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **سيناريوهات الاستخدام المحتملة**  
أحيانًا، تريد معرفة نوع قيم X و Y لنقاط المخطط في سلسلة. يوفر Aspose.Cells for JavaScript عبر C++ خاصيتي `ChartPoint.XValueType` و `ChartPoint.YValueType` لاستخدامها لهذا الغرض. يرجى ملاحظة أنه سيتعين عليك استدعاء طريقة `Chart.calculate()` قبل أن تتمكن من استخدام هذه الخصائص بفعالية.  

## **البحث عن نوع قيم X وY لنقاط في سلسلة الرسم البياني**  
الكود التجريبي التالي يحمل ملف Excel [العينة](64716905.xlsx) ويصل إلى المخطط الأول داخل الورقة الأولى. ثم يستدعي طريقة `Chart.calculate()` ويجد نوع قيم X و Y لنقطة المخطط الأولى ويطبعها في وحدة التحكم. يرجى مراجعة إخراج وحدة التحكم أدناه كمصدر مرجعي.  

## **الكود المثالي**  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Find Type Of X and Y Values Of Points In Chart Series</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Access first chart.
            const chart = worksheet.charts.get(0);

            // Calculate chart data.
            chart.calculate();

            // Access first chart point in the first series.
            const point = chart.nSeries.get(0).points.get(0);

            // Get the types of X and Y values of chart point.
            const xValueType = point.xValueType;
            const yValueType = point.yValueType;

            // Display results
            document.getElementById('result').innerHTML = `
                <p style="color: green;">Operation completed successfully!</p>
                <p>X Value Type: ${xValueType}</p>
                <p>Y Value Type: ${yValueType}</p>
            `;
        });
    </script>
</html>
```  

## **مخرجات الوحدة**  

{{< highlight java >}}  
 X Value Type: IsString  

Y Value Type: IsNumeric  
{{< /highlight >}}

---
title: ضبط نوع الشكل لتسميات البيانات في الرسم البياني باستخدام JavaScript عبر C++
linktitle: تعيين نوع الشكل لتسميات بيانات الرسم البياني
description: تعلم كيفية تعيين نوع شكل تسميات البيانات في الرسوم البيانية باستخدام Aspose.Cells for JavaScript عبر C++. سيشرح دليلنا أنواع الأشكال المتاحة ويُظهر لك كيفية اختيار الشكل المناسب لتسميات البيانات الخاصة بك لتعزيز العرض وسهولة الاستخدام.
keywords: Aspose.Cells for JavaScript عبر C++، رسم بياني، تسميات البيانات، أنواع الأشكال، العرض، سهولة الاستخدام.
type: docs
weight: 110
url: /ar/javascript-cpp/set-the-shape-type-of-data-labels-of-chart/
---

## **سيناريوهات الاستخدام المحتملة**
يمكنك تغيير نوع شكل تسميات البيانات على الرسم البياني باستخدام خاصية `DataLabels.shapeType`. تأخذ قيمة من تعداد `DataLabelShapeType` وتغير نوع شكل تسميات البيانات وفقًا لذلك. بعض من قيمها هي

{{< highlight javascript >}}
 DataLabelShapeType.BentLineCallout
DataLabelShapeType.DownArrowCallout
DataLabelShapeType.Ellipse
DataLabelShapeType.LineCallout
DataLabelShapeType.Rect
etc.
{{< /highlight >}}

## **تعيين نوع الشكل لتسميات بيانات الرسم البياني**
يعرض الكود النموذجي التالي تغيير نوع شكل تسميات البيانات على الرسم البياني إلى `DataLabelShapeType.WedgeEllipseCallout`. يرجى الاطلاع على ملف Excel النموذجي [الملف](60489778.xlsx) المستخدم في هذا الكود وملف Excel الناتج [الملف](60489779.xlsx) الذي تم إنشاؤه بواسطة الكود. يُظهر لقطة شاشة تأثير الكود على ملف Excel النموذجي.

![todo:image_alt_text](set-the-shape-type-of-data-labels-of-chart_1.png)
## **الكود المثالي**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Shape Type of Data Labels of Chart Example</title>
    </head>
    <body>
        <h1>Set Shape Type of Data Labels of Chart Example</h1>
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
            const resultDiv = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Accessing the first chart
            const chart = worksheet.charts.get(0);

            // Accessing the first series
            const series = chart.nSeries.get(0);

            // Set the shape type of data labels i.e. Speech Bubble Oval
            series.dataLabels.shapeType = AsposeCells.DataLabelShapeType.WedgeEllipseCallout;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSetShapeTypeOfDataLabelsOfChart.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Shape type set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

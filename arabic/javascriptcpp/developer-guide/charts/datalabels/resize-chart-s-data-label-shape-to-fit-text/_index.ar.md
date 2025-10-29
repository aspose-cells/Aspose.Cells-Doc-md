---
title: تغيير حجم شكل تسمية البيانات للمخطط ليتناسب مع النص باستخدام JavaScript عبر C++
linktitle: تغيير شكل تسمية بيانات الرسم البياني لتناسب النص
description: تعلم كيفية تغيير حجم شكل تسمية البيانات في مخطط ليتناسب مع النص في Aspose.Cells for JavaScript عبر C++. سيظهر دليلنا كيفية ضبط حجم وشكل حاوية التسمية لضمان عرض النص بشكل صحيح بدون اقتطاع أو تداخل.
keywords: Aspose.Cells for JavaScript عبر C++، رسم بياني، تسميات البيانات، تغيير حجم الشكل، توظيف النص، الاقتطاع، التداخل.
type: docs
weight: 220
url: /ar/javascript-cpp/resize-chart-s-data-label-shape-to-fit-text/
---

{{% alert color="primary" %}}  
توفر تطبيق Excel الخيار **تغيير شكل لملاءمة النص** لتسميات بيانات الرسم البياني من أجل زيادة حجم الشكل بحيث يتناسب النص بداخله.  
{{% /alert %}}  

## **كيفية تغيير شكل تسمية بيانات الرسم البياني لملاءمة النص في Microsoft Excel**  

يمكن الوصول إلى هذا الخيار على واجهة إكسل عن طريق تحديد أي من تسميات البيانات على المخطط. انقر بزر الماوس الأيمن واختر قائمة **تكوين تسميات البيانات**. في علامة التبويب **الحجم والخصائص**، قم بتوسيع **المحاذاة** للكشف عن الخصائص ذات الصلة بما في ذلك خيار **تغيير حجم الشكل لملاءمة النص**.  

## **كيفية تغيير حجم شكل تسمية البيانات للمخطط ليتناسب مع النص باستخدام Aspose.Cells for JavaScript عبر C++**  

لمحاكاة ميزة إكسل في تغيير حجم أشكال تسمية البيانات لتناسب النص، قدمت واجهات برمجة التطبيقات Aspose.Cells الخاصية [**DataLabels.isResizeShapeToFitText()**](https://reference.aspose.com/cells/javascript-cpp/charttextframe/#isResizeShapeToFitText--) من نوع Boolean. يُظهر الكود التالي سيناريو الاستخدام البسيط الخاص بـ [**DataLabels.isResizeShapeToFitText()**](https://reference.aspose.com/cells/javascript-cpp/charttextframe/#isResizeShapeToFitText--) الخاصية.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Chart Data Labels Resize Example</h1>
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

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet that contains the Chart
            const sheet = workbook.worksheets.get(0);

            for (let c = 0; c < sheet.charts.count; c++) {
                // Access the Chart
                const chart = sheet.charts.get(c);

                for (let index = 0; index < chart.nSeries.count; index++) {
                    // Access the DataLabels of indexed NSeries
                    const labels = chart.nSeries.get(index).dataLabels;

                    // Set ResizeShapeToFitText property to true
                    labels.isResizeShapeToFitText = true;
                }

                // Calculate Chart
                chart.calculate();
            }

            // Save the result
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

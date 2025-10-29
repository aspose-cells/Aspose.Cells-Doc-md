---
title: تعطيل التفاف النص لعلامات البيانات في المخطط باستخدام JavaScript عبر C++
description: تعلم كيفية تعطيل التفاف النص لعلامات البيانات في المخططات باستخدام Aspose.Cells for JavaScript عبر C++. سيظهر لك دليلنا كيفية منع تداخل العلامات الطويلة وتوفير عروض مخططات أكثر وضوحًا وسهولة في القراءة.
keywords: Aspose.Cells for JavaScript عبر C++، رسم بياني، علامات البيانات، التفاف النص، التداخل، قابلية القراءة، العروض.
type: docs
weight: 70
url: /ar/javascript-cpp/disable-text-wrapping-for-data-labels-of-the-chart/
---

{{% alert color="primary" %}}

يسمح Microsoft Excel 2013 للمستخدمين بتضمين أو عدم تضمين النص داخل تسميات البيانات في الرسم البياني. بشكل افتراضي، يكون النص داخل تسميات البيانات في الرسم البياني في حالة التضمين.

توفر Aspose.Cells خاصية [**DataLabels.isTextWrapped()**](https://reference.aspose.com/cells/javascript-cpp/datalabels/#isTextWrapped--) التي يمكنك تعيينها true أو false لتمكين أو تعطيل تغليف نص تسميات البيانات على التوالي.

{{% /alert %}}

يظهر النموذج العيني التالي كيفية تعطيل تضمين النص لتسميات البيانات في الرسم البياني.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Disable Data Label Text Wrapping</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            // Instantiating a Workbook object by loading uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the first chart inside the worksheet
            const chart = worksheet.charts.get(0);

            // Disable the Text Wrapping of Data Labels in all Series
            chart.nSeries.get(0).dataLabels.isTextWrapped = false;
            chart.nSeries.get(1).dataLabels.isTextWrapped = false;
            chart.nSeries.get(2).dataLabels.isTextWrapped = false;

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

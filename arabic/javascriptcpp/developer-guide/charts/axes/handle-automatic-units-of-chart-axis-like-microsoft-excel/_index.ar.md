---
title: التعامل مع وحدات تلقائية لمحور الرسم البياني مثل مايكروسوفت إكسل باستخدام جافا سكريبت عبر ++C
linktitle: التعامل مع الوحدات التلقائية لمحور الرسم البياني مثل Microsoft Excel
description: تعلم كيفية معالجة الوحدات التلقائية على محاور الرسم البياني في Aspose.Cells for JavaScript عبر ++C. دليلنا يوضح كيفية تكوين وتخصيص الوحدات التلقائية على محور الرسم البياني، بما في ذلك عرض الترميز العلمي وتعديل المقياس.
keywords: Aspose.Cells for JavaScript عبر ++C، محاور الرسم البياني، الوحدات التلقائية، مايكروسوفت إكسل، التكوين، التخصيص، الترميز العلمي، التدرج.
type: docs
weight: 120
url: /ar/javascript-cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/
---

## **سيناريوهات الاستخدام المحتملة**  
الإصدارات المبكرة من Aspose.Cells for JavaScript عبر ++C لم تكن قادرة على التعامل بشكل صحيح مع الوحدات التلقائية لمحور الرسم البياني عند تصدير الرسم إلى صورة أو PDF. الآن، يدعم Aspose.Cells for JavaScript عبر ++C التعامل مع الوحدات التلقائية للمحور، لا يوجد تغيير في الكود. فقط حول رسمتك إلى صورة أو PDF وسيتم عرض المحور تمامًا كما يفعله مايكروسوفت إكسل.  

## **التعامل مع الوحدات التلقائية لمحور الرسم البياني مثل Microsoft Excel**  
الشفرة النموذجية التالية تقوم بتحميل [ملف Excel النموذجي](61767755.xlsx) وتوليد [مخطط PDF الناتج](61767752.pdf). تُظهر الصورة المقتطعة الوحدات التلقائية لمحور المخطط داخل مستطيلات حمراء وتقارن أيضًا بين مخطط ملف Excel النموذجي ومخطط PDF الناتج. كلاهما مطابق تمامًا.  

![todo:image_alt_text](handle-automatic-units-of-chart-axis-like-microsoft-excel_1.png)  

## **الكود المثالي**  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Handle Automatic Units Of Chart Axis Like Microsoft Excel</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

        const readyPromise = AsposeCells.onReady({
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

            await readyPromise;

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first chart
            const chart = worksheet.charts.get(0);

            // Render chart to pdf
            const outputData = await chart.toPdf();

            // Create download link for the generated PDF
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputHandleAutomaticUnitsOfChartAxisLikeMicrosoftExcel.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart rendered to PDF successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

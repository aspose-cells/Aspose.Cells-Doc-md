---
title: تعيين رمز تنسيق القيم لسلسلة الرسم البياني باستخدام JavaScript عبر C++
description: تعلم كيف تقوم بتعيين رمز تنسيق القيم لسلسلة الرسم البياني في Aspose.Cells for Javaسكريبت عبر C++. سيساعدك هذا الدليل على فهم كيفية تنسيق بيانات سلسلة الرسم البياني الخاصة بك باستخدام رمز التنسيق المناسب، مما يسمح لك بعرض بياناتك بدقة ومهنية.
keywords: Aspose.Cells for Javaسكريبت عبر C++، سلسلة رسم بياني، رمز تنسيق القيم، التنسيق، تقديم البيانات، الدقة، الاحترافية.
linktitle: تنسيق الأرقام
type: docs
weight: 100
url: /ar/javascript-cpp/set-the-values-format-code-of-chart-series/
---

## **سيناريوهات الاستخدام المحتملة**
 يمكنك تعيين رمز تنسيق القيم لسلسلة الرسم البياني باستخدام خاصية [Series.valuesFormatCode](https://reference.aspose.com/cells/javascript-cpp/series/#valuesFormatCode--)، وهذه الخاصية مفيدة ليس فقط للسلاسل المبنية على النطاق داخل ورقة العمل، ولكن أيضًا تعمل بشكل جيد للسلاسل التي أنشئت باستخدام مصفوفة من القيم.

## **تعيين رمز تنسيق القيم لسلاسل الرسم البياني**
 يضيف الكود النموذجي التالي سلسلة في الرسم البياني الفارغ الذي لم يكن لديه سلاسل من قبل. يضيف السلسلة باستخدام مصفوفة القيم. بمجرد إضافة السلسلة، يقوم بتنسيقها باستخدام رمز $#,##0 باستخدام خاصية [Series.valuesFormatCode](https://reference.aspose.com/cells/javascript-cpp/series/#valuesFormatCode--) ويصبح الرقم 10000 هو $10,000. تعرض لقطة الشاشة تأثير الكود على ملف إكسل النموذجي (51740712.xlsx) وملف الإخراج (51740713.xlsx) بعد التنفيذ.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)

## **الكود المثالي**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Chart Series Example</h1>
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

                // Access first worksheet
                const worksheet = workbook.worksheets.get(0);

                // Access first chart
                const chart = worksheet.charts.get(0);

                // Add series using an array of values
                chart.nSeries.add("{10000, 20000, 30000, 40000}", true);

                // Access the series and set its values format code
                const series = chart.nSeries.get(0);
                series.valuesFormatCode = "$#,##0";

                // Saving the modified Excel file
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = '51740713.xlsx';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download Modified Excel File';

                document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
            });
        });
    </script>
</html>
```

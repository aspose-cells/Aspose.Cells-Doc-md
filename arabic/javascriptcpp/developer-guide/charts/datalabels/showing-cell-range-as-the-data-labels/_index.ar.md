---
title: عرض نطاق الخلايا كتسميات بيانات باستخدام JavaScript عبر C++
linktitle: عرض نطاق الخلية كعلامات البيانات
description: تعلم كيفية عرض نطاق من الخلايا كتسميات بيانات في الرسوم البيانية باستخدام Aspose.Cells for JavaScript عبر C++. سيُظهر دليلنا كيفية ربط التسميات بمصدر البيانات الخاص بك وتنسيقها لتوفير معلومات دقيقة وذات مغزى في الرسوم البيانية الخاصة بك.
keywords: Aspose.Cells for JavaScript عبر C++، رسم بياني، تسميات البيانات، نطاق الخلايا، مصدر البيانات، التنسيق، الدقة، معلومات ذات معنى.
type: docs
weight: 130
url: /ar/javascript-cpp/showing-cell-range-as-the-data-labels/
---

{{% alert color="primary" %}}
في ميكروسوفت إكسل 2013، يمكنك عرض نطاق خلايا كتسميات بيانات. يدعم Aspose.Cells for JavaScript عبر C++ ميزة ذلك.
{{% /alert %}}

## **علامة اختيار لعرض نطاق الخلايا كتسميات بيانات**

لعرض نطاق الخلايا كتسميات بيانات في Microsoft Excel:

1. حدد تسميات بيانات السلسلة وانقر بزر الماوس الأيمن لفتح القائمة المنسدلة.  
1. حدد **تنسيق تسميات البيانات**. تعرض خيارات التسميات.  
1. حدد أو قم بمسح الخيار **تحتوي التسمية على - قيمة من الخلايا**.  

الكود النموذجي أدناه يصل إلى علامات بيانات سلسلة الرسم البياني ويضبط الخاصية [**DataLabels.showCellRange**](https://reference.aspose.com/cells/javascript-cpp/datalabels/#showCellRange--) على **صحيح** لاختيار خيار **العلامة تتضمن - القيمة من الخلايا**.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Show Range in Data Labels</title>
    </head>
    <body>
        <h1>Show Range in Data Labels Example</h1>
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

            // Create workbook from the source Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the chart inside the worksheet
            const chart = worksheet.charts.get(0);

            // Check the "Label Contains - Value From Cells"
            const dataLabels = chart.nSeries.get(0).dataLabels;
            dataLabels.showCellRange = true;

            // Save the workbook
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

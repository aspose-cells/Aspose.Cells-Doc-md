---
title: تعبئة البيانات أولاً حسب الصف ثم حسب العمود
type: docs
weight: 1000
url: /ar/javascript-cpp/populate-data-first-by-row-then-by-column/
description: تعلم كيفية تعبئة البيانات أولاً بالصف ثم بالعمود باستخدام واجهة برمجة التطبيقات Aspose.Cells for JavaScript عبر C++.
keywords: تعبئة البيانات أولاً بالصف ثم بالعمود باستخدام JavaScript عبر C++، إدراج البيانات أولاً بالصف ثم بالعمود JavaScript عبر C++، إضافة البيانات أولاً بالصف ثم بالعمود JavaScript عبر C++، إدراج بيانات عالية الأداء JavaScript عبر C++، إضافة بيانات عالية الأداء JavaScript عبر C++
---

{{% alert color="primary" %}}  

تحسين أداء ملف البيانات عن طريق تعبئته بالبيانات أولاً حسب الصف ثم حسب العمود.  

{{% /alert %}}  

وضع البيانات في التسلسل A1، B1، A2، B2 أسرع من A1، A2، B1، B2. إذا كان هناك العديد من الخلايا في ورقة العمل واتبعت التسلسل الثاني، أي ملئ البيانات حسب الصف، يمكن أن يجعل هذا النصيب أسرع بكثير.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Populate Cells</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
            // Create a new workbook (blank)
            const workbook = new Workbook();

            // Populate Data into Cells
            const cells = workbook.worksheets.get(0).cells;
            cells.get("A1").value = "data1";
            cells.get("B1").value = "data2";
            cells.get("A2").value = "data3";
            cells.get("B2").value = "data4";

            // Save workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

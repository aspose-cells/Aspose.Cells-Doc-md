---
title: الحصول على ورقة العمل المرتبطة بالمخطط باستخدام JavaScript عبر C++
linktitle: الحصول على ورقة البيانات للشارت
description: تعلم كيفية استرجاع ورقة العمل المرتبطة بمخطط إكسل باستخدام Aspose.Cells for Javaسكريبت عبر C++. الوصول إلى البيانات الأساسية للمخطط ومعالجتها بكفاءة.
keywords: Aspose.Cells for Javaسكريبت، مخططات إكسل، أوراق العمل، معالجة البيانات، البيانات الأساسية، العمليات، JavaScript عبر C++
type: docs
weight: 1000
url: /ar/javascript-cpp/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

في بعض الأحيان، قد ترغب في الوصول إلى ورقة عمل من مرجع شارت. توفر Aspose.Cells ال [**Chart.worksheet**](https://reference.aspose.com/cells/javascript-cpp/chart/#worksheet--) المعني الذي يعيد مرجع الورقة التي تحتوي على الشارت.

{{% /alert %}}

يعرض المثال التالي كيفية استخدام الخاصية [**Chart.worksheet**](https://reference.aspose.com/cells/javascript-cpp/chart/#worksheet--). يُطبع اسم ورقة العمل أولاً، ثم يتم الوصول إلى أول مخطط على الورقة. ثم يُطبع اسم ورقة العمل مرة أخرى، باستخدام الخاصية [**Chart.worksheet**](https://reference.aspose.com/cells/javascript-cpp/chart/#worksheet--).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Print worksheet name
            const sheetName = worksheet.name;
            let outputHtml = `<p>Sheet Name: ${sheetName}</p>`;

            // Access the first chart inside this worksheet
            const charts = worksheet.charts;
            if (charts.count > 0) {
                const chart = charts.get(0);

                // Access the chart's sheet and display its name again
                const chartSheetName = chart.worksheet.name;
                outputHtml += `<p>Chart's Sheet Name: ${chartSheetName}</p>`;
            } else {
                outputHtml += `<p>No charts available in the worksheet.</p>`;
            }

            document.getElementById('result').innerHTML = outputHtml;
        });
    </script>
</html>
```

أدناه نتيجة الإخراج على الشاشة التي يؤدي إليها الكود المثالي. كما يمكنك رؤية، فإنه يطبع اسم الورقة نفسه بكلتا المرتين.

{{< highlight javascript >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}

---
title: تحديد أي محور موجود في الرسم البياني باستخدام جافا سكريبت عبر ++C 
linktitle: تحديد المحور الموجود في الرسم البياني
description: تعلم كيفية تحديد أي محور موجود في رسم بياني تم إنشاؤه باستخدام Aspose.Cells for JavaScript عبر ++C. دليلنا سيساعدك على التعرف والوصول إلى المحاور المختلفة في الرسم البياني، بما في ذلك المحاور الفئوية والقيمية والثانوية.
keywords: Aspose.Cells for JavaScript عبر ++C، رسم بياني، محور، وجود، فئة، قيمة، ثانوي.
type: docs
weight: 140
url: /ar/javascript-cpp/determine-which-axis-exists-in-the-chart/
---

{{% alert color="primary" %}}  
أحيانًا، يحتاج المستخدم إلى معرفة ما إذا كان محور معين موجود في المخطط. على سبيل المثال، يريد أن يعرف ما إذا كان يوجد محور قيمة ثانوي داخل المخطط أم لا. بعض المخططات مثل الفطيرة، الفطيرة المنفجرة، فطيرة عادية، فطيرة شريط، فطيرة ثلاثية الأبعاد، فطيرة ثلاثية الأبعاد منفجرة، دائرة مملوءة، مملوءة منفوخة، وغيرها لا تحتوي على محور.  

توفر Aspose.Cells [**Chart.hasAxis(axisType, isPrimary)**](https://reference.aspose.com/cells/javascript-cpp/chart/#hasAxis-AxisType-boolean-) لتحديد ما إذا كان لدى المخطط محور معين أم لا.  
{{% /alert %}}  

 يوضح الكود التالي استخدام [**Chart.hasAxis(axisType, isPrimary)**](https://reference.aspose.com/cells/javascript-cpp/chart/#hasAxis-AxisType-boolean-) لتحديد ما إذا كان الرسم البياني التجريبي يحتوي على محور فئة وقيمة أساسي وثانوي.  

## كود جافا سكريبت لتحديد أي محور موجود في الرسم البياني

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Check Chart Axes Example</h1>
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
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Check if there are any charts before accessing
            const charts = worksheet.charts;
            if (charts.count === 0) {
                resultDiv.innerHTML = '<p>No charts found in the worksheet.</p>';
                return;
            }

            // Access the chart
            const chart = charts.get(0);

            // Determine which axis exists in chart
            let outputs = [];
            let ret = chart.hasAxis(AsposeCells.AxisType.Category, true);
            outputs.push("Has Primary Category Axis: " + ret);

            ret = chart.hasAxis(AsposeCells.AxisType.Category, false);
            outputs.push("Has Secondary Category Axis: " + ret);

            ret = chart.hasAxis(AsposeCells.AxisType.Value, true);
            outputs.push("Has Primary Value Axis: " + ret);

            ret = chart.hasAxis(AsposeCells.AxisType.Value, false);
            outputs.push("Has Secondary Value Axis: " + ret);

            resultDiv.innerHTML = '<p>' + outputs.join('</p><p>') + '</p>';
        });
    </script>
</html>
```

## الناتج على واجهة الأوامر الناتجة عن الكود المثال

يظهر مخرجات وحدة التحكم للكود أدناه، والتي تعرض true للمحور الرئيسي للفئة والقيمة و false للمحور الثانوي للفئة والقيمة.  

{{< highlight java >}}  
Has Primary Category Axis: True  
Has Secondary Category Axis: False  
Has Primary Value Axis: True  
Has Secondary Value Axis: False  
{{< /highlight >}}

---
title: الحصول على نص المعادلة لاتجاه الخط البياني باستخدام JavaScript عبر C++
description: تعلم كيفية استخدام Aspose.Cells for Javaنص البرنامج النصي عبر C++ لاسترجاع نص المعادلة لاتجاه الخط في رسم بياني تم إنشاؤه في إكسل Microsoft. ستعرض دليلنا كيفية الوصول إلى واستخراج معادلة خطة الاتجاه لتحليل إضافي أو عرض.
keywords: Aspose.Cells for Javaنص البرنامج النصي عبر C++، خط الاتجاه، نص المعادلة، إكسل Microsoft، تحليل البيانات، عرض.
linktitle: خطوط الاتجاه
type: docs
weight: 110
url: /ar/javascript-cpp/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

 يمكنك استرجاع نص المعادلة لاتجاه خط الرسم البياني باستخدام Aspose.Cells for Javaنص البرنامج النصي عبر C++. توفر Aspose.Cells خاصية [**DataLabels.text**](https://reference.aspose.com/cells/javascript-cpp/datalabels/#text--) التي ترجع نص المعادلة لاتجاه خط الرسم البياني. لاستخدام هذه الخاصية، أولاً ستحتاج إلى استدعاء دالة [**Chart.calculate()**](https://reference.aspose.com/cells/javascript-cpp/chart/#calculate--).

{{% /alert %}}

يعرض لقطة الشاشة التالية المخطط مع خط اتجاه والنص المعادلة الخاص به مرئي باللون الأحمر. سنسترجع هذا النص باستخدام الخاصية [**DataLabels.text**](https://reference.aspose.com/cells/javascript-cpp/datalabels/#text--) في الكود التالي.

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

## كود جافا سكريبت للحصول على نص معادلة اتجاه خط الرسم البياني

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Read Trendline Equation Example</h1>
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the first chart inside the worksheet
            const chart = worksheet.charts.get(0);

            // Calculate the Chart to get the Equation Text of Trendline
            chart.calculate();

            // Access the Trendline
            const trendLine = chart.nSeries.get(0).trendLines.get(0);

            // Read the Equation Text of Trendline
            const equationText = trendLine.dataLabels.text;

            document.getElementById('result').innerHTML = `<p>Equation Text: ${equationText}</p>`;
        });
    </script>
</html>
```

## الإخراج الذي تم توليده بواسطة رمز العينة

هذا هو إنتاج الكونسول للكود العيني أعلاه.

{{< highlight javascript >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}

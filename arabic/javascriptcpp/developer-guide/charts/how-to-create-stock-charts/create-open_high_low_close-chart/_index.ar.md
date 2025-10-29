---
title: إنشاء مخطط الأسهم فتح  أعلى  أدنى  إغلاق (OHLC) باستخدام جافا سكريبت عبر C++
description: تعلم كيفية إنشاء مخطط سهم فتح أعلى أدنى إغلاق باستخدام Aspose.Cells for JavaScript عبر C++. ستُوضح خريطتنا كيفية رسم بيانات سوق الأسهم، بما في ذلك سعر الافتتاح، الأعلى، الأدنى، والإغلاق، على مخطط لتحليل وتحسين التصور.
keywords: Aspose.Cells for JavaScript عبر C++، مخطط الأسهم فتح أعلى أدنى إغلاق، بيانات سوق الأسهم، التحليل، التصور.
type: docs
weight: 182
url: /ar/javascript-cpp/create-open-high-low-close-stock-chart/
---

## **سيناريوهات الاستخدام المحتملة**
يستخدم مخطط Open-High-Low-Close (OHLC) خمسة أعمدة من البيانات، بالترتيب: الفئة، فتح، عالي، منخفض، وإغلاق. يتم إشارة نطاق الأسعار في كل فئة مرة أخرى بخط عمودي، بينما يتم تقديم نطاق بين الفتح والإغلاق بشريط عائم أوسع؛ إذا زاد السعر في الفئة (الإغلاق أعلى من الفتح)، يتم ملؤه بلون واحد، بينما إذا انخفض السعر، يتم ملؤه بلون آخر. يطلق على هذا النوع من الرسم البياني كثيرًا اسم الرسم الشمعي.

![todo:image_alt_text](data.png)

![todo:image_alt_text](sample.png)
## **تحسينات الرؤية في الرسم البياني**
 غالبًا ما نستخدم الألوان بدلاً من الأبيض والأسود للإشارة إلى ارتفاع وانخفاض الأسعار. في مجموعة الشموع الأولى أدناه، يظهر اللون الأحمر ارتفاع الأسعار والأخضر انخفاضها.

![todo:image_alt_text](sample2.png)
## **الكود المثالي**
الكود العينة التالي يحمل [ملف إكسل العينة](Open-High-Low-Close.xlsx) ويولد [ملف إكسل الناتج](out.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Open-High-Low-Close Stock Chart Example</h1>
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Create High-Low-Close-Stock Chart
            const pieIdx = worksheet.charts.add(AsposeCells.ChartType.StockOpenHighLowClose, 5, 6, 20, 12);

            // Retrieve the Chart object
            const chart = worksheet.charts.get(pieIdx);

            // Set the legend can be showed
            chart.showLegend = true;

            // Set the chart title name 
            chart.title.text = "Open-High-Low-Close Stock";

            // Set the Legend at the bottom of the chart area
            chart.legend.position = AsposeCells.LegendPositionType.Bottom;

            // Set data range
            chart.chartDataRange = ["A1:E9", true];

            // Set category data 
            chart.nSeries.categoryData = "A2:A9";

            // Set the DownBars and UpBars with different color
            chart.nSeries.get(0).downBars.area.foregroundColor = AsposeCells.Color.Green;
            chart.nSeries.get(0).upBars.area.foregroundColor = AsposeCells.Color.Red;

            // Fill the PlotArea area with nothing 
            chart.plotArea.area.fillFormat.fillType = AsposeCells.FillType.None;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

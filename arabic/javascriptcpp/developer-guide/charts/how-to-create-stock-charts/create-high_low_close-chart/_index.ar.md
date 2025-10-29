---
title: إنشاء مخطط سهم أعلى  أدنى  إغلاق (HLC) باستخدام جافا سكريبت عبر C++
linktitle: إنشاء رسم بياني لأسهم High Low Close (HLC)
description: تعلم كيفية إنشاء مخطط سهم أعلى أدنى إغلاق باستخدام Aspose.Cells for JavaScript عبر C++. سيرينا دليلنا خطوة بخطوة كيفية رسم بيانات سوق الأسهم، بما في ذلك أعلى، أدنى، وأسعار الإغلاق، على مخطط لتحليل وتصور أفضل.
keywords: Aspose.Cells for JavaScript عبر C++، مخطط سهم أعلى أدنى إغلاق، بيانات سوق الأسهم، التحليل، التصور.
type: docs
weight: 181
url: /ar/javascript-cpp/create-high-low-close-stock-chart/
---

## **سيناريوهات الاستخدام المحتملة**  
 يستخدم رسم الأسهم عالي-منخفض-إغلاق أربعة أعمدة من البيانات. العمود الأول هو فئة، عادةً تاريخ لكن يمكن استخدام أسماء الأسهم أيضًا. الأعمدة الثلاثة التالية، بالترتيب، هي للأسعار العليا، الدنيا، والإغلاق. يُشار إلى نطاق السعر لكل فئة بخط عمودي من أدنى إلى أعلى، ويُعرض سعر الإغلاق باستخدام علامة مميزة تمتد إلى يمين هذا الخط.  

![todo:image_alt_text](sample.png)  
## **تحسينات الرؤية في الرسم البياني**  
في بعض الأحيان، لجعل الرسم البياني يبدو أكثر تفاعلية، يمكننا تعديل مظهر العلامة (الإغلاق)، أو جعلها تظهر على المحور الثانوي.  

![todo:image_alt_text](sample2.png)  
## **الكود المثالي**  
الكود العينة التالي يحمل [ملف إكسل العينة](High-Low-Close.xlsx) ويولد [ملف إكسل الناتج](out.xlsx).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>High-Low-Close Stock Chart Example</h1>
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

            // Create an instance of Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Create High-Low-Close-Stock Chart
            const pieIdx = worksheet.charts.add(AsposeCells.ChartType.StockHighLowClose, 5, 6, 20, 12);

            // Retrieve the Chart object
            const chart = worksheet.charts.get(pieIdx);

            // Set the legend can be showed
            chart.showLegend = true;

            // Set the chart title name 
            chart.title.text = "High-Low-Close Stock";

            // Set the Legend at the bottom of the chart area
            chart.legend.position = AsposeCells.LegendPositionType.Bottom;

            // Set data range (range and orientation)
            chart.chartDataRange = ["A1:D9", true];

            // Set category data 
            chart.nSeries.categoryData = "A2:A9";

            // Set the marker with the built-in data for the 3rd series (index 2)
            const series2 = chart.nSeries.get(2);
            const marker = series2.marker;
            marker.markerStyle = AsposeCells.ChartMarkerType.Dash;
            marker.markerSize = 20;
            marker.area.formatting = AsposeCells.FormattingType.Custom;
            marker.area.foregroundColor = AsposeCells.Color.Maroon;

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

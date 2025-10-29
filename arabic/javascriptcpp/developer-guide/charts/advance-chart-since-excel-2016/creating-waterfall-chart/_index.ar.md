---
title: كيفية إنشاء مخطط Waterfall باستخدام JavaScript عبر C++
linktitle: كيفية إنشاء رسم بياني Waterfall
type: docs
weight: 160
url: /ar/javascript-cpp/creating-waterfall-chart/
description: إنشاء مخططات Waterfall في Excel باستخدام JavaScript وAspose.Cells for JavaScript عبر C++.
keywords: إنشاء مخطط Waterfall في Excel JavaScript عبر C++، كيفية إنشاء مخطط Waterfall في Excel JavaScript عبر C++، كيفية إنشاء مخطط Waterfall في Excel JavaScript عبر C++
---

{{% alert color="primary" %}}

مخطط السلسلة المائية هو نوع خاص من المخططات يُستخدم عادةً لإظهار كيفية زيادة أو نقصان الموقع الابتدائي. لدى Microsoft Excel العديد من أنواع المخططات المعرفة مسبقًا، بما في ذلك الأعمدة والخطوط والدوارات والنسب، لكن مخطط السلسلة المائية يتجاوز الرسوم البيانية الأساسية ويمكن إنشاؤه باستخدام أنواع المخططات الحالية مع تخصيص بسيط أو أكبر.

{{% /alert %}} 

 تتيح واجهات برمجة Aspose.Cells إنشاء مخطط سلسة مائية بمساعدة مخطط خطي. كما تتيح الواجهة تخصيص مظهر المخطط لمنحه شكل السلسلة المائية من خلال ضبط خصائص [**Series.upBars**](https://reference.aspose.com/cells/javascript-cpp/series/#upBars--) و [**Series.downBars**](https://reference.aspose.com/cells/javascript-cpp/series/#downBars--).

القطعة البرمجية أدناه توضح استخدام Aspose.Cells for JavaScript عبر C++ لإنشاء مخطط Waterfall من البداية.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Chart Waterfall Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType, Color, FormattingType } = AsposeCells;

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

            // Load workbook from selected file if provided, otherwise create a new workbook
            let workbook;
            if (fileInput.files && fileInput.files.length > 0) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Retrieve the first Worksheet in Workbook
            const worksheet = workbook.worksheets.get(0);

            // Retrieve the Cells of the first Worksheet
            const cells = worksheet.cells;

            // Input some data which chart will use as source
            cells.get("A1").value = "Previous Year";
            cells.get("A2").value = "January";
            cells.get("A3").value = "March";
            cells.get("A4").value = "August";
            cells.get("A5").value = "October";
            cells.get("A6").value = "Current Year";

            cells.get("B1").value = 8.5;
            cells.get("B2").value = 1.5;
            cells.get("B3").value = 7.5;
            cells.get("B4").value = 7.5;
            cells.get("B5").value = 8.5;
            cells.get("B6").value = 3.5;

            cells.get("C1").value = 1.5;
            cells.get("C2").value = 4.5;
            cells.get("C3").value = 3.5;
            cells.get("C4").value = 9.5;
            cells.get("C5").value = 7.5;
            cells.get("C6").value = 9.5;

            // Add a Chart of type Waterfall in same worksheet as of data
            const idx = worksheet.charts.add(ChartType.Waterfall, 4, 4, 25, 13);

            // Retrieve the Chart object
            const chart = worksheet.charts.get(idx);

            // Add Series
            chart.nSeries.add("$B$1:$C$6", true);

            // Add Category Data
            chart.nSeries.categoryData = "$A$1:$A$6";

            // Series has Up Down Bars
            chart.nSeries.get(0).hasUpDownBars = true;

            // Set the colors of Up and Down Bars
            chart.nSeries.get(0).upBars.area.foregroundColor = Color.Green;
            chart.nSeries.get(0).downBars.area.foregroundColor = Color.Red;

            // Make both Series Lines invisible
            chart.nSeries.get(0).border.isVisible = false;
            chart.nSeries.get(1).border.isVisible = false;

            // Set the Plot Area Formatting Automatic
            chart.plotArea.area.formatting = FormattingType.Automatic;

            // Delete the Legend
            chart.legend.legendEntries.get(0).isDeleted = true;
            chart.legend.legendEntries.get(1).isDeleted = true;

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## مقالات ذات صلة

- [إنشاء الرسوم البيانية](/cells/ar/javascript-cpp/creating-charts/)
- [تخصيص المخططات](/cells/ar/javascript-cpp/customizing-charts/)

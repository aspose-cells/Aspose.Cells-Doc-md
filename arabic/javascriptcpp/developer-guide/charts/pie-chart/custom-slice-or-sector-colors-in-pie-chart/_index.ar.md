---
title: ألوان شرائح أو قطاعات مخصصة في مخطط الدائرة باستخدام JavaScript عبر C++
linktitle: ألوان شريحة أو قطاع مخصصة في الرسم البياني الدائري
description: تعلم كيفية استخدام Aspose.Cells for JavaScript عبر C++ لتخصيص ألوان الشرائح والقطاعات في مخطط دائري. سيظهر دليلنا كيفية تعيين ألوان فريدة لكل شريحة أو قطاع أو فرقة لتحسين الجاذبية البصرية وتمثيل البيانات.
keywords: Aspose.Cells for JavaScript عبر C++، مخطط دائري، ألوان شرائح مخصصة، ألوان قطاعات مخصصة، الجاذبية البصرية، تمثيل البيانات.
type: docs
weight: 60
url: /ar/javascript-cpp/custom-slice-or-sector-colors-in-pie-chart/
---

{{% alert color="primary" %}}

يشرح هذا المقال كيفية إضافة ألوان مخصصة لشرائح/قطاعات الدائرة الدائرية. بشكل افتراضي، تستخدم الرسوم البيانية الدائرية القوالب الافتراضية لبرنامج Microsoft Excel. لاستخدام ألوان أخرى، أعيد تعريف الألوان في الرسم البياني.

{{% /alert %}}

لتعيين لون مخصص لشرائح أو قطاعات الدائرة الدائرية:

 1. الوصول إلى كائن [**Series**](https://reference.aspose.com/cells/javascript-cpp/series) و[**ChartPoint**](https://reference.aspose.com/cells/javascript-cpp/chartpoint).
 1. تعيين لونك المفضل باستخدام خاصية [**ChartPoint.foregroundColor**](https://reference.aspose.com/cells/javascript-cpp/area/#foregroundColor--).

يشرح هذا المقال أيضًا كيفية:

- بيانات فئة الرسم البياني.
- عنوان الرسم البياني المرتبط بخلية.
- إعدادات خط عنوان الرسم البياني.
- موقع وسام.

{{% alert color="primary" %}}

[**ChartPoint.foregroundColor**](https://reference.aspose.com/cells/javascript-cpp/area/#foregroundColor--) ليس محددًا لرسومات الدائرة الدائرية ولكن يمكن استخدامه لجميع أنواع الرسوم البيانية.

{{% /alert %}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Pie Chart Example</h1>
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

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Put the sample values used in a pie chart
            worksheet.cells.get("C3").value = "India";
            worksheet.cells.get("C4").value = "China";
            worksheet.cells.get("C5").value = "United States";
            worksheet.cells.get("C6").value = "Russia";
            worksheet.cells.get("C7").value = "United Kingdom";
            worksheet.cells.get("C8").value = "Others";

            // Put the sample values used in a pie chart
            worksheet.cells.get("D2").value = "% of world population";
            worksheet.cells.get("D3").value = 25;
            worksheet.cells.get("D4").value = 30;
            worksheet.cells.get("D5").value = 10;
            worksheet.cells.get("D6").value = 13;
            worksheet.cells.get("D7").value = 9;
            worksheet.cells.get("D8").value = 13;

            // Create a pie chart with desired length and width
            const pieIdx = worksheet.charts.add(AsposeCells.ChartType.Pie, 1, 6, 15, 14);

            // Access the pie chart
            const pie = worksheet.charts.get(pieIdx);

            // Set the pie chart series
            pie.nSeries.add("D3:D8", true);

            // Set the category data
            pie.nSeries.categoryData = "=Sheet1!$C$3:$C$8";

            // Set the chart title that is linked to cell D2
            pie.title.linkedSource = "D2";

            // Set the legend position at the bottom.
            pie.legend.position = AsposeCells.LegendPositionType.Bottom;

            // Set the chart title's font name and color
            pie.title.font.name = "Calibri";
            pie.title.font.size = 18;

            // Access the chart series
            const srs = pie.nSeries.get(0);

            // Color the individual points with custom colors
            srs.points.get(0).area.foregroundColor = new AsposeCells.Color(0, 246, 22, 219);
            srs.points.get(1).area.foregroundColor = new AsposeCells.Color(0, 51, 34, 84);
            srs.points.get(2).area.foregroundColor = new AsposeCells.Color(0, 46, 74, 44);
            srs.points.get(3).area.foregroundColor = new AsposeCells.Color(0, 19, 99, 44);
            srs.points.get(4).area.foregroundColor = new AsposeCells.Color(0, 208, 223, 7);
            srs.points.get(5).area.foregroundColor = new AsposeCells.Color(0, 222, 69, 8);

            // Autofit all columns
            worksheet.autoFitColumns();

            // Saving the modified Excel file and offering download
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

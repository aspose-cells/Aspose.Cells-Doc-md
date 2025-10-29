---
title: محور X مقابل محور الفئة مع جافا سكريبت عبر ++C
linktitle: المحور X مقابل محور الفئة
description: تعلم كيفية التمييز بين محور الـ X ومحور الفئة في Aspose.Cells for JavaScript عبر ++C. دليلنا سيساعدك على فهم الفروقات في استخدامهما وخصائصهما، وكيفية تكوينهما وفقًا لاحتياجاتك.
keywords: Aspose.Cells for JavaScript عبر ++C، محور X، محور الفئة، الاختلاف، الاستخدام، الخصائص، التكوين.
type: docs
weight: 180
url: /ar/javascript-cpp/X-axis-vs-category-axis/
---

## **سيناريوهات الاستخدام المحتملة**
هناك أنواع مختلفة من المحاور X. بينما يكون المحور Y محور نوع قيمة، يمكن أن يكون المحور X محور نوع فئة أو محور نوع قيمة. باستخدام محور القيمة، يتم معاملة البيانات كبيانات عددية متغيرة بشكل مستمر، ويتم وضع العلامة في نقطة على طول المحور التي تتغير وفقًا لقيمتها العددية. باستخدام محور الفئة، يتم معاملة البيانات كسلسلة من علامات النص غير الرقمية، ويتم وضع العلامة في نقطة على طول المحور وفقًا لموقعها في التسلسل. يوضح المثال أدناه الفرق بين محاور القيمة والفئة.
يتم عرض البيانات العينية لدينا في [ملف الجدول العيني](sample.png) أدناه. تحتوي العمود الأول على بيانات محور X الخاصة بنا، والتي يمكن معاملتها كفئات أو قيم. لاحظ أن الأرقام ليست منتظمة بالتساوي، ولا تظهر حتى بترتيب عددي.

![todo:image_alt_text](sample.png)
## **قم بالتعامل مع المحور X ومحور الفئة على غرار Microsoft Excel**
 سنعرض هذه البيانات على نوعين من الرسوم البيانية، الرسم البياني الأول هو XY (نقطة الانتشار) مع المحور السيني كقيم، والرسم البياني الثاني هو مخطط خطي مع المحور السيني كتصنيف.

![todo:image_alt_text](compare.png)
## **الكود المثالي**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Charts and X Axis</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType, LegendPositionType, FillType, Utils } = AsposeCells;

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

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            // Access the first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Put the sample values used in charts
            worksheet.cells.get("A2").putValue(1);
            worksheet.cells.get("A3").putValue(3);
            worksheet.cells.get("A4").putValue(2.5);
            worksheet.cells.get("A5").putValue(3.5);
            worksheet.cells.get("B1").putValue("Cats");
            worksheet.cells.get("C1").putValue("Dogs");
            worksheet.cells.get("D1").putValue("Fishes");
            worksheet.cells.get("B2").putValue(7);
            worksheet.cells.get("B3").putValue(6);
            worksheet.cells.get("B4").putValue(5);
            worksheet.cells.get("B5").putValue(4);
            worksheet.cells.get("C2").putValue(7);
            worksheet.cells.get("C3").putValue(5);
            worksheet.cells.get("C4").putValue(4);
            worksheet.cells.get("C5").putValue(3);
            worksheet.cells.get("D2").putValue(8);
            worksheet.cells.get("D3").putValue(7);
            worksheet.cells.get("D4").putValue(3);
            worksheet.cells.get("D5").putValue(2);

            // Create Line Chart: X as Category Axis
            let pieIdx = worksheet.charts.add(ChartType.LineWithDataMarkers, 6, 15, 20, 21);
            // Retrieve the Chart object
            let chart = worksheet.charts.get(pieIdx);
            // Add Series
            chart.nSeries.add("B2:D5", true);
            // Set the category data
            chart.nSeries.categoryData = "=Sheet1!$A$2:$A$5";
            // Set the first series name
            chart.nSeries.get(0).name = "Cats";
            // Set the second series name
            chart.nSeries.get(1).name = "Dogs";
            // Set the third series name
            chart.nSeries.get(2).name = "Fishes";
            // Set the Legend at the bottom of the chart area
            chart.legend.position = LegendPositionType.Bottom;
            // Fill the PlotArea area with nothing 
            chart.plotArea.area.fillFormat.fillType = FillType.None;

            // Create XY (Scatter) Chart: X as Value Axis
            pieIdx = worksheet.charts.add(ChartType.ScatterConnectedByLinesWithDataMarker, 6, 6, 20, 12);
            // Retrieve the Chart object
            chart = worksheet.charts.get(pieIdx);
            // Add Series
            chart.nSeries.add("B2:D5", true);
            // Set X values for series 
            chart.nSeries.get(0).xValues = "{1,3,2.5,3.5}";
            chart.nSeries.get(1).xValues = "{1,3,2.5,3.5}";
            chart.nSeries.get(2).xValues = "{1,3,2.5,3.5}";
            // Set the first series name
            chart.nSeries.get(0).name = "Cats";
            // Set the second series name
            chart.nSeries.get(1).name = "Dogs";
            // Set the third series name
            chart.nSeries.get(2).name = "Fishes";
            // Set the Legend at the bottom of the chart area
            chart.legend.position = LegendPositionType.Bottom;
            // Fill the PlotArea area with nothing 
            chart.plotArea.area.fillFormat.fillType = FillType.None;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'XAxis.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

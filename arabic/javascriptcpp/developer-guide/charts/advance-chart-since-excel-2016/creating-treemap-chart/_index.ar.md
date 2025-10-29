---
title: كيفية إنشاء مخطط TreeMap باستخدام JavaScript عبر C++
linktitle: كيفية إنشاء رسم بياني لخريطة الشجرة
description: تعلم كيفية إنشاء مخطط Treemap في Aspose.Cells for JavaScript عبر C++. دليلنا سيساعدك في فهم الخصائص وخيارات التنسيق المختلفة المتاحة لمخططات Treemap، بما في ذلك الألوان، والتسميات، وتمثيل البيانات.
keywords: Aspose.Cells for JavaScript عبر C++، مخطط Treemap، إنشاء، خصائص، تنسيق، ألوان، تسميات، تمثيل البيانات، مخطط دائري، تصنيف هرمي.
type: docs
weight: 161
url: /ar/javascript-cpp/creating-treemap-chart/
---

## **سيناريوهات الاستخدام المحتملة**  
رسم بياني لخريطة الشجرة يوفر رؤية تسلسلية لبياناتك ويجعل من السهل رؤية الأنماط، مثل أي العناصر هي أفضل المبيعات في المحل. تمثل الفروع الشجرية بواسطة المستطيلات، ويتم عرض كل فرع فرعي كمستطيل أصغر. يعرض رسم بياني الخريطة الشجرية الفئات بواسطة اللون والقرب، ويمكن عرض الكثير من البيانات بسهولة مما قد يكون صعبًا مع أنواع الرسوم البيانية الأخرى.  

![todo:image_alt_text](sample.png)  
## **رسم بياني لخريطة الشجرة**  
بعد تشغيل الكود أدناه، سترون رسم بياني لخريطة الشجرة كما هو موضح أدناه.  

![todo:image_alt_text](result.png)  
## **الكود المثالي**  
الكود العيني التالي يقوم بتحميل [ملف Excel العيني](treemap.xlsx) ويولد [ملف Excel الناتج](out.xlsx).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Treemap Chart Example</title>
    </head>
    <body>
        <h1>Treemap Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType, FillType } = AsposeCells;

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

            // Instantiate Workbook with uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);
            // Add a Treemap chart at row 5, column 6 with height 20 and width 12
            const pieIdx = worksheet.charts.add(ChartType.Treemap, 5, 6, 20, 12);
            // Retrieve the Chart object
            const chart = worksheet.charts.get(pieIdx);
            // Set the legend to be shown
            chart.showLegend = true;
            // Set the chart title text
            chart.title.text = "TreeMap Chart";
            // Add series data range (D2:F13)
            chart.nSeries.add("D2:F13", true);
            // Set category data (A2:C13)
            chart.nSeries.setCategoryData("A2:C13");
            // Show the DataLabels with category names for first series
            chart.nSeries.get(0).dataLabels.showCategoryName = true;
            // Fill the PlotArea area with nothing
            chart.plotArea.area.fillFormat.fillType = FillType.None;

            // Save the modified Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Treemap chart created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

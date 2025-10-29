---
title: كيفية إنشاء مخطط Sunburst باستخدام JavaScript عبر C++
linktitle: كيفية إنشاء رسم بياني للتفجير الشمسي
description: تعلم كيفية إنشاء مخطط Sunburst في Aspose.Cells for JavaScript عبر C++، وهو مخطط يعرض البيانات في دائرة. دليلنا سيساعدك في إعداد خصائص وتنسيقات مختلفة لمخططك، بما في ذلك تسميات البيانات، والوسائل التوضيحية، والألوان، وأكثر.
keywords: Aspose.Cells for JavaScript عبر C++، مخطط Sunburst، إنشاء، تعيين الخصائص، تسميات البيانات، الوسائل التوضيحية، التنسيق، اللون، دائرة، عرض البيانات.
type: docs
weight: 162
url: /ar/javascript-cpp/creating-sunburst-chart/
---

## **سيناريوهات الاستخدام المحتملة**
جداول الأشجار جيدة للمقارنة بين النسب داخل الهيكل؛ ومع ذلك، فإن جداول الأشجار ليست رائعة في عرض المستويات الهرمية بين أكبر الفئات وكل نقطة بيانات. مخطط الشمسية هو أكثر وضوحًا لهذا الغرض. يُعد مخطط الشمسية مثاليًا لعرض البيانات الهرمية. يُمثل كل مستوى من الهيكل بواسطة خاتم واحد أو دائرة، مع أصغر دائرة تمثل أعلى مستوى من الهرمية. يبدو مخطط الشمسية بدون بيانات هرمية (مستوى واحد من الفئات) مشابهًا لمخطط الدونات. ومع ذلك، فإن مخطط الشمسية متعدد المستويات يُظهر كيف ترتبط الحلقات الخارجية بالحلقات الداخلية. يتمتع مخطط الشمسية بأقصى فاعليته في إظهار كيف يتم تقسيم حلقة واحدة إلى أجزائها المساهمة، بينما نوع آخر من المخططات الهرمية، مخطط الشجرة، مثالي للمقارنة بين الأحجام النسبية.

![todo:image_alt_text](sample.png)
## **رسم بياني للتفجير الشمسي**
بعد تشغيل الكود أدناه، سترون رسم بياني للتفجير الشمسي كما هو موضح أدناه.

![todo:image_alt_text](result.png)
## **الكود المثالي**
الكود المثالي التالي يحمل [ملف Excel العيني](sunburst.xlsx) ويُولّد [ملف Excel الإخراج](out.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Sunburst Chart Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Sunburst Chart Example</h1>
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

            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const worksheet = workbook.worksheets.get(0);

            const pieIdx = worksheet.charts.add(AsposeCells.ChartType.Sunburst, 5, 6, 25, 12);
            const chart = worksheet.charts.get(pieIdx);

            chart.showLegend = true;
            chart.title.text = "Sunburst Chart";
            chart.nSeries.add("D2:D16", true);
            chart.nSeries.categoryData = "A2:C16";
            chart.nSeries.get(0).dataLabels.showCategoryName = true;
            chart.plotArea.area.fillFormat.fillType = AsposeCells.FillType.None;

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Sunburst chart created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

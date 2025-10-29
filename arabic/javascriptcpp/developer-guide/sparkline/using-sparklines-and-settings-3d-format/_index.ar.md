---
title: استخدام Sparkline والإعدادات بتنسيق ثلاثي الأبعاد مع جافا سكريبت عبر C++
linktitle: استخدام الشرائط وإعدادات تنسيق ثلاثي الأبعاد
type: docs
weight: 40
url: /ar/javascript-cpp/using-sparklines-and-settings-3d-format/
description: تعلم كيفية استخدام Sparkline وتطبيق التنسيق ثلاثي الأبعاد في ملفات Excel باستخدام Aspose.Cells for JavaScript عبر C++. 
---

## **استخدام الشرائط**
يمكن لبرنامج Microsoft Excel 2010 تحليل المعلومات بطرق أكثر من أي وقت مضى. يسمح للمستخدمين بتتبع وتسليط الضوء على اتجاهات البيانات المهمة باستخدام أدوات تحليل البيانات والرؤية الجديدة. الشرائط هي رسومات مصغرة يمكنك وضعها داخل الخلايا بحيث يمكنك عرض البيانات والرسم البياني على الجدول نفسه. عند استخدام الشرائط بشكل صحيح، يكون تحليل البيانات أسرع وأكثر دقة. كما أنها توفر رؤية بسيطة للمعلومات، مما يجنب ورقات العمل المزدحمة بالرسوم البيانية الكثيرة.

Aspose.Cells for JavaScript عبر C++ يوفر واجهة برمجة تطبيقات للتعامل مع Sparkline في جداول البيانات.
### **الشرائط في Microsoft Excel**
لإدراج الشرائط في Microsoft Excel 2010:

1. حدد الخلايا التي ترغب في ظهور الشرائط فيها. لجعلها سهلة الرؤية، حدد الخلايا على جانب البيانات.
1. انقر على **Insert** في الشريط واختر **column** في **Sparklines**.
1. حدد أو أدخل نطاق الخلايا في ورقة العمل التي تحتوي على البيانات. ستظهر الرسوم البيانية.

تساعد الشرائط في رؤية الاتجاهات، على سبيل المثال، سجل الفوز أو الخسارة لدوري الكرة اللينة. يمكن للشرائط حتى الإشارة إلى مجموع الموسم بأكمله لكل فريق في الدوري.
### **Sparkline باستخدام Aspose.Cells for JavaScript عبر C++**
يمكن للمطورين إنشاء، حذف أو قراءة Sparkline (في ملف القالب) باستخدام API المقدم من Aspose.Cells for JavaScript عبر C++. تحتوي الفصول التي تدير Sparkline على وحدة [SparklineGroupCollection](https://reference.aspose.com/cells/javascript-cpp/sparklinegroupcollection/)، لذا يلزم استدعاء هذه الوحدة قبل استخدام هذه الميزات.

من خلال إضافة رسومات مخصصة لنطاق البيانات المعطى، يحصل المطورون على حرية إضافة أنواع مختلفة من الرسوم الصغيرة إلى مناطق الخلايا المحددة.

يوضح المثال أدناه ميزة شرائط البيانات. يوضح المثال كيفية:

1. فتح ملف قالب بسيط.
1. قراءة معلومات شرائط البيانات لورقة عمل.
1. إضافة شرائط بيانات جديدة لنطاق بيانات معطى إلى منطقة خلية.
1. حفظ ملف Excel على القرص.


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Sparkline Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Sparkline Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, SparklineType, Color } = AsposeCells;

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

            // Instantiate a Workbook by opening the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            // Get the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Read the Sparklines from the worksheet (if any)
            const sparklinesCount = sheet.sparklineGroups.count;
            let logHtml = '';
            for (let i = 0; i < sparklinesCount; i++) {
                const group = sheet.sparklineGroups.get(i);
                logHtml += `sparkline group: type:${group.type}, sparkline items count:${group.sparklines.count}<br/>`;
                const sparklineCount = group.sparklines.count;
                for (let j = 0; j < sparklineCount; j++) {
                    const sparkline = group.sparklines.get(j);
                    logHtml += `sparkline: row:${sparkline.row}, col:${sparkline.column}, dataRange:${sparkline.dataRange}<br/>`;
                }
            }

            // Add Sparklines
            // Define the CellArea D2:D10 (rows and columns are zero-based: D is column 4 -> index 4)
            const ca = CellArea.createCellArea(1, 4, 7, 4);
            // Add new Sparklines for a data range to a cell area
            const idx = sheet.sparklineGroups.add(SparklineType.Column, "Sheet1!B2:D8", false, ca);
            const newGroup = sheet.sparklineGroups.get(idx);
            // Create CellsColor and set color
            const clr = workbook.createCellsColor();
            clr.color = Color.Orange;
            newGroup.seriesColor = clr;

            // Save the modified Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book1.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p><div>' + logHtml + '</div>';
        });
    </script>
</html>
```
## **ضبط تنسيق ثلاثي الأبعاد**
قد تحتاج إلى أنماط رسم بياني ثلاثية الأبعاد لتتمكن من الحصول على النتائج فقط لنطاق سيناريوك. يوفر Aspose.Cells for JavaScript عبر C++ API ذات الصلة لتطبيق تنسيق ثلاثي الأبعاد في إكسل 2007.

يتم تقديم مثال كامل أدناه لتوضيح كيفية إنشاء رسم بياني وتطبيق تنسيق Microsoft Excel 2007 ثلاثي الأبعاد. بعد تنفيذ كود المثال، سيتم إضافة رسم بياني للأعمدة (مع تأثيرات ثلاثية الأبعاد) إلى ورقة العمل.


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>3D Chart Formatting Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType, Color, BevelPresetType, PresetMaterialType, LightRigType } = AsposeCells;

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
            // Creating a new workbook
            const book = new Workbook();

            // Add a Data Worksheet
            const dataSheet = book.worksheets.add("DataSheet");

            // Add Chart Worksheet
            const sheet = book.worksheets.add("MyChart");

            // Put some values into the cells in the data worksheet
            dataSheet.cells.get("B1").value = 1;
            dataSheet.cells.get("B2").value = 2;
            dataSheet.cells.get("B3").value = 3;
            dataSheet.cells.get("A1").value = "A";
            dataSheet.cells.get("A2").value = "B";
            dataSheet.cells.get("A3").value = "C";

            // Define the Chart Collection
            const charts = sheet.charts;
            // Add a Column chart to the Chart Worksheet
            const chartSheetIdx = charts.add(ChartType.Column, 5, 0, 25, 15);

            // Get the newly added Chart
            const chart = book.worksheets.get(2).charts.get(0);

            // Set the background/foreground color for PlotArea/ChartArea
            chart.plotArea.area.backgroundColor = Color.White;
            chart.chartArea.area.backgroundColor = Color.White;
            chart.plotArea.area.foregroundColor = Color.White;
            chart.chartArea.area.foregroundColor = Color.White;

            // Hide the Legend
            chart.showLegend = false;

            // Add Data Series for the Chart
            chart.nSeries.add("DataSheet!B1:B3", true);
            // Specify the Category Data
            chart.nSeries.categoryData = "DataSheet!A1:A3";

            // Get the Data Series
            const ser = chart.nSeries.get(0);

            // Apply the 3-D formatting
            const spPr = ser.shapeProperties;
            const fmt3d = spPr.format3D;

            // Specify Bevel with its height/width
            const bevel = fmt3d.topBevel;
            bevel.type = BevelPresetType.Circle;
            bevel.height = 2;
            bevel.width = 5;

            // Specify Surface material type
            fmt3d.surfaceMaterialType = PresetMaterialType.WarmMatte;

            // Specify surface lighting type
            fmt3d.surfaceLightingType = LightRigType.ThreePoint;

            // Specify lighting angle
            fmt3d.lightingAngle = 20;

            // Specify Series background/foreground and line color
            ser.area.backgroundColor = Color.Maroon;
            ser.area.foregroundColor = Color.Maroon;
            ser.border.color = Color.Maroon;

            // Saving the modified Excel file and providing download link
            const outputData = book.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = '3d_format.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

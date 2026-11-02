---
title: تعديل تخطيط حقول الصفحة في الجدول المحوري
linktitle: تعديل تخطيط حقول الصفحة في الجدول المحوري
description: تعرف على كيفية التحكم في تخطيط منطقة حقول الصفحة في جدول محوري باستخدام Aspose.Cells for JavaScript via C++، بما في ذلك ضبط ترتيب العرض وعدد مرات الالتفاف وترتيب حقول الصفحة في أعلى الجدول المحوري.
keywords: Aspose.Cells for JavaScript via C++, جدول بيانات, جدول محوري, حقل صفحة, ترتيب حقول الصفحة, عدد مرات الالتفاف بحقول الصفحة, نقل حقل صفحة
type: docs
weight: 191
url: /ar/javascript-cpp/change-page-field-layout/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
تعتمد هذه المقالة على موضوع **إضافة حقل صفحة إلى الجدول المحوري**. وتوضح كيفية التحكم في تخطيط منطقة حقول الصفحة، أي الشريط الذي يحتوي على عناصر تحكم للتصفية في أعلى الجدول المحوري، بما في ذلك ترتيب العرض وعدد مرات الالتفاف وإعادة ترتيب الحقول.
{{% /alert %}}

## **مقدمة**
يتيح الجدول المحوري في Microsoft Excel منطقة مخصصة **لحقول الصفحة** تقع فوق منطقة الصفوف والأعمدة والبيانات في الجدول. تُعرض هذه المنطقة في هيئة شريط يحتوي على قائمة منسدلة للتصفية لكل حقل صفحة، وهو ما ينقر عليه المستخدمون النهائيون لتصفية الجدول المحوري وفق معايير مثل السنة أو المنطقة. تمثّل Aspose.Cells هذه المنطقة من خلال مجموعة `pivotTable.pageFields` وتوفّر ثلاث خصائص تتحكم في التخطيط البصري للشريط:
- `pivotTable.pageFieldOrder` (قيمة من النوع `Aspose.Cells.PrintOrderType`) تحدد ما إذا كانت حقول الصفحة الإضافية توضع *بجانب* الحقول الحالية أو *أسفلها*.
- `pivotTable.pageFieldWrapCount` تحدد عدد حقول الصفحة الموضوعة في كل صف أو عمود قبل حدوث الالتفاف.
- `pivotTable.pageFields.move(currIndex, destIndex)` يعيد ترتيب حقول الصفحة دون تغيير وضع ترتيبها.
تشرح هذه المقالة ثلاثة أمثلة برمجية، يوضح كل منها إحدى هذه العمليات على مجموعة بيانات مشتركة، لتتمكن من مقارنة التخطيطات الناتجة جنبًا إلى جنب.

## **بيانات المصدر**
| الفاكهة | السنة | المنطقة | المبلغ |
|---|---|---|---|
| تفاحة | 2022 | الشمال | 150 |
| تفاحة | 2023 | الشمال | 180 |
| موز | 2022 | الجنوب | 120 |
| موز | 2023 | الجنوب | 140 |
| كرز | 2022 | الشرق | 200 |
| كرز | 2023 | الشرق | 220 |
| عنب | 2022 | الغرب | 90 |
| عنب | 2023 | الغرب | 110 |
تكون الصفوف الثمانية جميعها ممتلئة في كل مثال برمجي وبالترتيب نفسه، لذا لا تختلف بيانات المصدر بين السيناريوهات؛ بل تتغير فقط خصائص تخطيط حقول الصفحة.

## **المثال 1: عرضي ثم رأسي**
في السيناريو الأول، نهيكل حقلي الصفحة (`Year` و`Region`) بحيث يظهران **جنبًا إلى جنب في صف واحد** في أعلى الجدول المحوري. نعين `Fruit` إلى محور الصفوف، ونضع `Year` أولًا و`Region` ثانيًا على محور الصفحة، حيث يحدد ترتيب استدعاءات `addFieldToArea` الفهرس الابتدائي، ثم نضيف `Amount` (`Sum`) كحقل بيانات، ثم نضبط `pivotTable.pageFieldOrder` على `PrintOrderType.OverThenDown` مع `pivotTable.pageFieldWrapCount = 2`. مع `OverThenDown` وعدد مرات الالتفاف البالغ 2، توضع حقول الصفحة أفقيًا جنبًا إلى جنب في صف واحد أعلى الجدول المحوري، لذا يشغل الشريط صفًا واحدًا يتسع لحقلين.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheets = workbook.worksheets;
            const pivotDataSheet = worksheets.add("PivotData");
            const pivotDataCells = pivotDataSheet.cells;
            // رؤوس الأعمدة (الصف 0)
            pivotDataCells.get(0, 0).value = "Fruit";
            pivotDataCells.get(0, 1).value = "Year";
            pivotDataCells.get(0, 2).value = "Region";
            pivotDataCells.get(0, 3).value = "Amount";
            // الصف 1: تفاح، 2022، الشمال، 150
            pivotDataCells.get(1, 0).value = "Apple";
            pivotDataCells.get(1, 1).value = 2022;
            pivotDataCells.get(1, 2).value = "North";
            pivotDataCells.get(1, 3).value = 150;
            // الصف 2: تفاح، 2023، الشمال، 180
            pivotDataCells.get(2, 0).value = "Apple";
            pivotDataCells.get(2, 1).value = 2023;
            pivotDataCells.get(2, 2).value = "North";
            pivotDataCells.get(2, 3).value = 180;
            // الصف 3: موز، 2022، الجنوب، 120
            pivotDataCells.get(3, 0).value = "Banana";
            pivotDataCells.get(3, 1).value = 2022;
            pivotDataCells.get(3, 2).value = "South";
            pivotDataCells.get(3, 3).value = 120;
            // الصف 4: موز، 2023، الجنوب، 140
            pivotDataCells.get(4, 0).value = "Banana";
            pivotDataCells.get(4, 1).value = 2023;
            pivotDataCells.get(4, 2).value = "South";
            pivotDataCells.get(4, 3).value = 140;
            // الصف 5: كرز، 2022، الشرق، 200
            pivotDataCells.get(5, 0).value = "Cherry";
            pivotDataCells.get(5, 1).value = 2022;
            pivotDataCells.get(5, 2).value = "East";
            pivotDataCells.get(5, 3).value = 200;
            // الصف 6: كرز، 2023، الشرق، 220
            pivotDataCells.get(6, 0).value = "Cherry";
            pivotDataCells.get(6, 1).value = 2023;
            pivotDataCells.get(6, 2).value = "East";
            pivotDataCells.get(6, 3).value = 220;
            // الصف 7: عنب، 2022، الغرب، 90
            pivotDataCells.get(7, 0).value = "Grape";
            pivotDataCells.get(7, 1).value = 2022;
            pivotDataCells.get(7, 2).value = "West";
            pivotDataCells.get(7, 3).value = 90;
            // الصف 8: عنب، 2023، الغرب، 110
            pivotDataCells.get(8, 0).value = "Grape";
            pivotDataCells.get(8, 1).value = 2023;
            pivotDataCells.get(8, 2).value = "West";
            pivotDataCells.get(8, 3).value = 110;
            // إضافة ورقة PivotTableReport
            const pivotTableSheet = worksheets.add("PivotTableReport");
            const pivotTables = pivotTableSheet.pivotTables;
            // إنشاء جدول محوري مصدره PivotData!A1:D9 ووضعه في A1 على ورقة PivotTableReport
            const pivotTableIndex = pivotTables.add("PivotData!A1:D9", "A1", "PivotTable1");
            const pivotTable = pivotTables.get(pivotTableIndex);
            // إضافة الحقول
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);   // الفاكهة
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);  // السنة
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);  // المنطقة
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);  // المبلغ
            pivotTable.dataFields.get(0).function = AsposeCells.ConsolidationFunction.Sum;
            // configuring تخطيط منطقة حقول الصفحة: وضع حقول الصفحة أفقيًا أولًا والالتفاف بعد كل حقلين
            pivotTable.pageFieldOrder = AsposeCells.PrintOrderType.OverThenDown;
            pivotTable.pageFieldWrapCount = 2;
            // تحديث البيانات وحسابها
            pivotTable.calculateData();
            // الحفظ
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "pageFieldLayout_overThenDown.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **المثال 2: رأسي ثم عرضي**
في هذا المثال، نضع `Fruit` على محور الصفوف، و`Year` و`Region` على محور الصفحة، مع وضع `Year` أولًا، و`Amount` (`Sum`) كحقل بيانات، تمامًا كما في المثال 1. ثم نضبط `pivotTable.pageFieldOrder` على `PrintOrderType.DownThenOver` و`pivotTable.pageFieldWrapCount` على `2`. مع `DownThenOver` وعدد مرات الالتفاف البالغ 2، تكدس حقول الصفحة رأسيًا، بحيث يكون `Year` في الأعلى و`Region` مباشرةً تحته، مما ينتج عمودًا واحدًا في أعلى الجدول المحوري. لذا يشغل الشريط صفين بعرض حقل واحد، بخلاف المثال 1.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const pivotData = workbook.worksheets.get(0);
            pivotData.name = "PivotData";
            const pivotReport = workbook.worksheets.add("PivotTableReport");
            const headers = ["Fruit", "Year", "Region", "Amount"];
            for (let c = 0; c < headers.length; c++) {
                pivotData.cells.get(0, c).value = headers[c];
            }
            const data = [
                ["Apple", 2022, "North", 150],
                ["Apple", 2023, "North", 180],
                ["Banana", 2022, "South", 120],
                ["Banana", 2023, "South", 140],
                ["Cherry", 2022, "East", 200],
                ["Cherry", 2023, "East", 220],
                ["Grape", 2022, "West", 90],
                ["Grape", 2023, "West", 110]
            ];
            for (let r = 0; r < data.length; r++) {
                for (let c = 0; c < data[r].length; c++) {
                    pivotData.cells.get(r + 1, c).value = data[r][c];
                }
            }
            const pivotTableIndex = pivotReport.pivotTables.add(
                "=PivotData!A1:D9",
                "A1",
                "PivotTable1"
            );
            const pivotTable = pivotReport.pivotTables.get(pivotTableIndex);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);
            pivotTable.pageFieldOrder = AsposeCells.PrintOrderType.DownThenOver;
            pivotTable.pageFieldWrapCount = 2;
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], {
                type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "pageFieldLayout_downThenOver.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **المثال 3: نقل حقل صفحة**
في السيناريو الثالث، نحتفظ بمجموعة البيانات نفسها وتوزيع الحقول نفسه، ونضبط تخطيطًا محايدًا (`OverThenDown` مع ضبط عدد مرات الالتفاف على `2`)، ثم نوضح عملية `pivotTable.pageFields.move`. ينقل الاستدعاء `move(0, 1)` حقل الصفحة الموجود عند الفهرس 0 (`Year`) إلى الموضع 1، وينتقل حقل الصفحة الموجود في الموضع 1 (`Region`) إلى الموضع 0. بعد هذا الاستدعاء، يصبح `Region` أول حقل صفحة ويصبح `Year` ثانيه. يبقى إعداد الالتفاف ووضع ترتيب حقول الصفحة دون تغيير، لذا لا يزال الشريط يُعرض أفقيًا وتظل حقول الصفحة متجاورة، مع تبديل ترتيب القائمتين المنسدلتين فقط.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        const initialization = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            await initialization;
            const workbook = new Workbook();
            const dataSheet = workbook.worksheets.get(0);
            dataSheet.name = "PivotData";
            const cells = dataSheet.cells;
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Region";
            cells.get("D1").value = "Amount";
            cells.get("A2").value = "Apple";
            cells.get("B2").value = 2022;
            cells.get("C2").value = "North";
            cells.get("D2").value = 150;
            cells.get("A3").value = "Apple";
            cells.get("B3").value = 2023;
            cells.get("C3").value = "North";
            cells.get("D3").value = 180;
            cells.get("A4").value = "Banana";
            cells.get("B4").value = 2022;
            cells.get("C4").value = "South";
            cells.get("D4").value = 120;
            cells.get("A5").value = "Banana";
            cells.get("B5").value = 2023;
            cells.get("C5").value = "South";
            cells.get("D5").value = 140;
            cells.get("A6").value = "Cherry";
            cells.get("B6").value = 2022;
            cells.get("C6").value = "East";
            cells.get("D6").value = 200;
            cells.get("A7").value = "Cherry";
            cells.get("B7").value = 2023;
            cells.get("C7").value = "East";
            cells.get("D7").value = 220;
            cells.get("A8").value = "Grape";
            cells.get("B8").value = 2022;
            cells.get("C8").value = "West";
            cells.get("D8").value = 90;
            cells.get("A9").value = "Grape";
            cells.get("B9").value = 2023;
            cells.get("C9").value = "West";
            cells.get("D9").value = 110;
            const pivotSheet = workbook.worksheets.add("PivotTableReport");
            const pivotTableIndex = pivotSheet.pivotTables.add(
                "=PivotData!A1:D9",
                "A3",
                "PivotTable1"
            );
            const pivotTable = pivotSheet.pivotTables.get(pivotTableIndex);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Region");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            pivotTable.pageFieldOrder = AsposeCells.PrintOrderType.OverThenDown;
            pivotTable.pageFieldWrapCount = 2;
            pivotTable.pageFields.move(0, 1);
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "pageFieldLayout_move.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **مقالات ذات صلة**
- [إضافة حقل صفحة إلى الجدول المحوري](/cells/ar/javascript-cpp/add-page-field-in-pivot-table/) — الصفحة الأم التي توضح كيفية إضافة حقول الصفحة إلى جدول محوري.
- [إدارة حقول القيم في الجدول المحوري](/cells/ar/javascript-cpp/manage-value-fields/) — تصف كيفية تهيئة منطقة البيانات (القيم)، بما في ذلك تجميع `Sum` المستخدم في هذه المقالة.
- [تطبيق نمط على الجدول المحوري](/cells/ar/javascript-cpp/apply-style-to-pivot-table/) — توضح كيفية تنسيق الجدول المحوري المعروض بعد ضبط تخطيط شريط حقول الصفحة.

{{< app/cells/assistant language="javascript-cpp" >}}
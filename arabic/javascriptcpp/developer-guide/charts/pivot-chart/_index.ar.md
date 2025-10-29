---
title: كيفية إضافة PivotChart باستخدام Aspose.Cells for JavaScript عبر C++
linktitle: مخطط محوري
type: docs
weight: 100
url: /ar/javascript-cpp/how-to-add-pivot-chart/
description: كيفية إضافة PivotChart باستخدام Aspose.Cells for JavaScript عبر C++.
keywords: PivotChart JavaScript عبر C++
---
## ما هو PivotChart

المخطط المحوري هو تمثيل بصري للبيانات في جدول محوري. يوفر المخططات المحورية وسيلة لتلخيص، تحليل، استكشاف، وعرض البيانات الملخصة. إليك بعض الميزات والجوانب الرئيسية للمخططات المحورية:

1. تمثيل البيانات ديناميكي: يتم تحديث المخططات المحورية تلقائيًا لتعكس التغييرات في الجدول المحوري. إذا أضفت أو أزلت حقولًا في الجدول، يتم تحديث المخطط المحوري وفقًا لذلك.

1. تفاعلي: المخططات المحورية تفاعلية، تتيح للمستخدمين تصفية وفرز والاستكشاف في البيانات. يسهل ذلك استكشاف جوانب مختلفة من مجموعة البيانات.

1. تصميم مرن: يمكن للمستخدمين تغيير تخطيط مخطط المحور عن طريق سحب وإفلات الحقول، مما يوفر مرونة في كيفية تصور البيانات.

1. أنواع المخططات المختلفة: يمكن إنشاء مخططات Pivot باستخدام أنواع مخططات متنوعة مثل مخططات الأعمدة، الخطوط، الدوائر، والمزيد، اعتمادًا على طبيعة البيانات والرؤى التي ترغب في اكتسابها.

1. التلخيص: تختصر مخططات Pivot كميات كبيرة من البيانات ويمكن أن تعرض الإجماليات، المتوسطات، العدادات، أو إحصاءات مختصرة أخرى.

1. التصفية: توفر قدرات التصفية، مما يسمح لك بعرض البيانات التي تلبي معايير معينة فقط.

<br>
تستخدم مخططات Pivot بشكل شائع في ذكاء الأعمال وتحليل البيانات لتقديم ملخص بصري واضح وملخص لمجموعات البيانات المعقدة. إنها أداة قوية لاتخاذ القرارات المستندة إلى البيانات.

## كيفية إضافة PivotChart باستخدام Aspose.Cells for JavaScript عبر C++

### **إضافة جدول محوري**

 لإنشاء جدول محوري باستخدام Aspose.Cells for JavaScript عبر C++:

1. أضف بعض البيانات إلى ورقة عمل باستخدام طريقة `putValue` لكائن الخلية. يمكنك أيضًا استخدام ملف قالب مسبق مملوء بالبيانات. ستُستخدم البيانات كمصدر بيانات لجدول المحوري.
1. أضف جدول محوري إلى ورقة العمل من خلال استدعاء طريقة `add` من مجموعة `PivotTables`.
1. الوصول إلى كائن جدول المحوري الجديد من مجموعة `PivotTables` عن طريق تمرير فهرسه. استخدم أي من كائنات جدول المحوري الموجودة لإدارة الجدول.

تم إعطاء أمثلة الكود أدناه.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Populate Worksheet and Download</h1>
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
            const resultDiv = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Obtaining the reference of the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Name the sheet
            sheet.name = "Data";
            const cells = sheet.cells;

            // Setting the header values to the cells
            cells.get("A1").value = "Employee";
            cells.get("B1").value = "Quarter";
            cells.get("C1").value = "Product";
            cells.get("D1").value = "Continent";
            cells.get("E1").value = "Country";
            cells.get("F1").value = "Sale";

            const namesAndValues = [
                ["David", 1, "Maxilaku", "Asia", "China", 2000],
                ["David", 2, "Maxilaku", "Asia", "India", 500],
                ["David", 3, "Chai", "Asia", "Korea", 1200],
                ["David", 4, "Maxilaku", "Asia", "India", 1500],
                ["James", 1, "Chang", "Europe", "France", 500],
                ["James", 2, "Chang", "Europe", "France", 1500],
                ["James", 3, "Chang", "Europe", "Germany", 800],
                ["James", 4, "Chang", "Europe", "Italy", 900],
                ["James", 4, "Chang", "Europe", "France", 500],
                ["Miya", 1, "Geitost", "America", "U.S.", 1600],
                ["Miya", 2, "Chai", "America", "U.S.", 600],
                ["Miya", 3, "Geitost", "America", "Brazil", 2000],
                ["Miya", 2, "Geitost", "America", "U.S.", 500],
                ["Miya", 3, "Maxilaku", "America", "Canada", 900],
                ["Miya", 4, "Geitost", "America", "U.S.", 700],
                ["Miya", 5, "Geitost", "America", "U.S.", 1400],
                ["Miya", 6, "Ikuru", "Europe", "Italy", 1350],
                ["Miya", 7, "Ikuru", "Europe", "France", 300],
                ["Miya", 8, "Ikuru", "Europe", "Italy", 500],
                ["Miya", 9, "Ikuru", "America", "New Zealand", 1000],
                ["Miya", 10, "Ipoh Coffee", "Oceania", "Australia", 1500],
                ["Miya", 11, "Chocolade", "Oceania", "Australia", 500],
                ["Miya", 12, "Chocolade", "Oceania", "New Zealand", 1500],
                ["Miya", 13, "Chocolade", "Oceania", "S.Africa", 1600],
                ["Miya", 14, "Chocolade", "Africa", "Egypt", 1000],
                ["Miya", 15, "Chocolade", "Africa", "Egypt", 1200],
                ["Miya", 16, "Chocolade", "Africa", "Egypt", 1300],
            ];

            namesAndValues.forEach((item, index) => {
                const rowIndex = index + 2;
                cells.get(`A${rowIndex}`).value = item[0];
                cells.get(`B${rowIndex}`).value = item[1];
                cells.get(`C${rowIndex}`).value = item[2];
                cells.get(`D${rowIndex}`).value = item[3];
                cells.get(`E${rowIndex}`).value = item[4];
                cells.get(`F${rowIndex}`).value = item[5];
            });

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Worksheet populated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **إضافة رسم بياني دوراني**

 لإنشاء PivotChart باستخدام Aspose.Cells for JavaScript عبر C++:

1. أضف رسم بياني.
1. اضبط `PivotSource` المخطط للإشارة إلى جدول محوري موجود في ورقة العمل.
1. قم بتعيين سمات أخرى.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Pivot Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Adding a new sheet of Chart type
            const sheetIndex = workbook.worksheets.add(AsposeCells.SheetType.Chart);
            const sheet3 = workbook.worksheets.get(sheetIndex);
            sheet3.name = "PivotChart";

            // Adding a column chart
            const index = sheet3.charts.add(AsposeCells.ChartType.Column, 0, 5, 28, 16);

            // Setting the pivot chart data source and hiding pivot field buttons
            const chart = sheet3.charts.get(index);
            chart.pivotSource = "PivotTable!PivotTable1";
            chart.hidePivotFieldButtons = false;

            // Saving the modified Excel file and providing a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'pivotChart_test_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Pivot chart created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

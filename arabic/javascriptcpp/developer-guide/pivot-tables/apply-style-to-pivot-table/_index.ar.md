---
title: تطبيق الأنماط على الجداول المحورية في Aspose.Cells for JavaScript via C++
linktitle: تطبيق الأنماط على الجداول المحورية في Aspose.Cells for JavaScript via C++
description: تعلّم كيفية تطبيق الأنماط المدمجة والمخصصة على الجداول المحورية في Aspose.Cells for JavaScript via C++، بما في ذلك التنسيقات التلقائية القديمة لملفات XLS، وأنماط الجداول المحورية الحديثة المسماة في Excel 2007+، وأنماط الجداول المحورية المخصصة، واختصار FormatAll.
keywords: Aspose.Cells for JavaScript via C++ نمط جدول محوري, PivotTableStyleType, AutoFormatType, FormatAll, نمط مخصص, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /ar/javascript-cpp/apply-style-to-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يدعم Aspose.Cells تطبيق كل من التنسيقات التلقائية القديمة للجداول المحورية (المصممة لملفات `.xls`) والأنماط الحديثة المسماة أو المخصصة للجداول المحورية (المصممة لملفات `.xlsx` و`.xlsm` و`.xlsb`). تعتمد واجهة API التي ينبغي استدعاؤها على صيغة الملف الذي يُحفظ فيه المصنف، لا على الصيغة التي حُمِّل منها.
{{% /alert %}}

## **مقدمة**
يوفر Aspose.Cells واجهتَي API متوازيتين لتحديد أنماط الجداول المحورية. يتوقف الاختيار بينهما على صيغة الملف الذي تحفظ فيه المصنف، لا على الصيغة التي تقرأ منها. ويمكن إعادة حفظ مصنف تم تحميله من ملف `.xls` بصيغة `.xlsx`، وعندئذٍ تُطبَّق واجهة API الحديثة للتنسيق بدلاً من واجهة API القديمة.
- `pivotTable.pivotTableStyleType` يحدد أحد الأنماط المدمجة المسماة (بما فيها السمات الفاتحة والداكنة، بما في ذلك الأنماط المضافة في Excel 2017). هذه الأنماط للقراءة فقط.
- `pivotTable.pivotTableStyleName` يحدد نمطًا مخصصًا تعرّفه بنفسك عبر `workbook.worksheets.tableStyles.addPivotTableStyle(...)`. وتكون الأنماط المخصصة ضرورية عند الحاجة إلى تعديل الألوان أو الحدود أو الخطوط بما يتجاوز ما توفره الأنماط المدمجة.
بالإضافة إلى ذلك، يُعد `pivotTable.formatAll(style)` اختصارًا يطبق كائن `style` واحدًا على كل خلية في الجدول المحوري، متجاوزًا أي نمط يُحدد مسبقًا عبر `pivotTable.pivotTableStyleType` أو `pivotTable.pivotTableStyleName`. وهو مفيد عند الحاجة إلى مظهر موحد بغض النظر عن السمة الأساسية.

## **تطبيق تنسيق تلقائي جاهز خاص بصيغة XLS القديمة**
يقبل `pivotTable.autoFormatType` قيمة من تعداد `Aspose.Cells.Pivot.PivotTableAutoFormatType`. القيم المتاحة هي `Report1` إلى `Report10`، و`Classic`، و`Table1` إلى `Table10`.
يحمّل المثال التالي مصنفًا جديدًا، ويملأه ببيانات العينة `Fruit/Year/Amount`، ويضيف جدولًا محوريًا، ويطبق `PivotTableAutoFormatType.Report5`، ويحفظ النتيجة بصيغة `.xls`.

{{% alert color="primary" %}}
**لماذا لا توجد حقول أعمدة؟** صُممت تنسيقات التقرير التلقائية (`Report1` إلى `Report10`، و`Table1` إلى `Table10`) في Excel الكلاسيكي للجداول المحورية **أحادية البُعد** التي تتكون من حقول الصفوف والقيم فقط، إذ لا تتضمن تنسيقات مدمجة لعناوين حقول الأعمدة. إذا احتاج جدولك المحوري إلى حقول أعمدة، فاستخدم أنماط `PivotTableStyleType` الحديثة المذكورة في [سيناريو 2](#apply-a-modern-named-preset-pivot-table-style)، فهي مصممة للتخطيط ثنائي الأبعاد الذي يستخدمه Excel الحديث.
{{% /alert %}}

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
            // Scenario 1: Apply a legacy XLS preset autoformat
            // API in use: PivotTable.AutoFormatType
            // Target file format: .xls (legacy)
            // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
            // Create a new workbook
            const workbook = new Workbook();
            // Get the first worksheet
            const sheet = workbook.worksheets.get(0);
            const cells = sheet.cells;
            // Populate the source data with header row (Fruit, Year, Amount)
            // and 9 data rows covering grape, blueberry, kiwi, cherry across 2020 and 2021
            cells.get(0, 0).value = "Fruit";
            cells.get(0, 1).value = "Year";
            cells.get(0, 2).value = "Amount";
            cells.get(1, 0).value = "grape";
            cells.get(1, 1).value = 2020;
            cells.get(1, 2).value = 50;
            cells.get(2, 0).value = "blueberry";
            cells.get(2, 1).value = 2020;
            cells.get(2, 2).value = 30;
            cells.get(3, 0).value = "kiwi";
            cells.get(3, 1).value = 2020;
            cells.get(3, 2).value = 25;
            cells.get(4, 0).value = "cherry";
            cells.get(4, 1).value = 2020;
            cells.get(4, 2).value = 40;
            cells.get(5, 0).value = "grape";
            cells.get(5, 1).value = 2021;
            cells.get(5, 2).value = 60;
            cells.get(6, 0).value = "blueberry";
            cells.get(6, 1).value = 2021;
            cells.get(6, 2).value = 35;
            cells.get(7, 0).value = "kiwi";
            cells.get(7, 1).value = 2021;
            cells.get(7, 2).value = 28;
            cells.get(8, 0).value = "cherry";
            cells.get(8, 1).value = 2021;
            cells.get(8, 2).value = 45;
            cells.get(9, 0).value = "grape";
            cells.get(9, 1).value = 2020;
            cells.get(9, 2).value = 45;
            // Add a pivot table at destination cell E3, using source range A1:C10
            const pivotTable = sheet.pivotTables.add("=A1:C10", 2, 4);
            // Assign fields: Fruit -> Rows, Amount -> Data
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // Apply the legacy XLS preset autoformat "Report5"
            // Note: This property is only meaningful when saving as .xls.
            // When saved as .xlsx/.xlsm/.xlsb, Excel ignores AutoFormatType
            // and uses whatever PivotTableStyleType / PivotTableStyleName specifies.
            pivotTable.autoFormatType = AsposeCells.PivotTableAutoFormatType.Report5;
            // Save the workbook in legacy .xls format
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: "application/vnd.ms-excel" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xls";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **تطبيق نمط جدول محوري حديث مدمج ومسمى**
يحدد `pivotTable.pivotTableStyleType` أحد الأنماط المدمجة المسماة التي أضافها Excel 2007 للجداول المحورية. يعرّف تعداد `PivotTableStyleType` ثلاث عائلات من السمات: العائلة الفاتحة من `PivotTableStyleLight1` إلى `PivotTableStyleLight28`، والعائلة المتوسطة من `PivotTableStyleMedium1` إلى `PivotTableStyleMedium28`، والعائلة الداكنة من `PivotTableStyleDark1` إلى `PivotTableStyleDark28`. كما يعرّف `None` و`Custom`. أما العناصر ذات الأرقام الأعلى في كل عائلة فهي الأنماط التي أضافها Excel 2017.
هذه الأنماط للقراءة فقط. وعندما تحتاج إلى تغيير الألوان أو الحدود أو الخطوط بما يتجاوز ما يوفره النمط الجاهز، عليك تعريف نمط جدول محوري مخصص بدلاً منه، كما هو موضح في [سيناريو 3](#define-and-apply-a-custom-pivot-table-style).

{{% alert color="primary" %}}
**لماذا الأنماط الحديثة بدلاً من تنسيقات التقرير التلقائية؟** سبقت قيم `Report1` إلى `Report10` و`Table1` إلى `Table10` في `PivotTableAutoFormatType` ظهور حقول الأعمدة في الجداول المحورية، لذلك لا تتضمن تنسيقًا لعناوين حقول الأعمدة، ويعرض Excel تلك العناوين بلا تنسيق. صُممت أنماط `PivotTableStyleType` للتخطيط ثنائي الأبعاد الذي يستخدمه Excel الحديث، وتطبق تنسيقًا على عناوين حقول الصفوف وعناوين حقول الأعمدة على حد سواء.
{{% /alert %}}

يعيد هذا السيناريو استخدام مجموعة بيانات `Fruit/Year/Amount` المستخدمة في السيناريو 1، ويضيف `Year` إلى منطقة الأعمدة إلى جانب حقل الصف `Fruit` عبر `PivotFieldType.Column`، ويطبق النمط الجاهز ذي السمة الداكنة `PivotTableStyleDark1` عبر `pivotTable.pivotTableStyleType`، ثم يحفظ النتيجة بصيغة `.xlsx` — وهي الصيغة التي تكون فيها `PivotTableStyleType` ذات معنى.

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
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        const readyPromise = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            // Scenario 2: Apply a modern Excel 2007+ named preset style using PivotTableStyleType.
            // Target file format: .xlsx. The PivotTableStyleType enum lives in the Aspose.Cells namespace
            // (not in Aspose.Cells.Pivot) -- that is why we do not need any extra using for it.
            // GitHub reference: https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            // Header row: Fruit / Year / Amount
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            // 9 data rows of Fruit / Year / Amount
            cells.get("A2").value = "Grape";
            cells.get("B2").value = 2020;
            cells.get("C2").value = 100;
            cells.get("A3").value = "Blueberry";
            cells.get("B3").value = 2020;
            cells.get("C3").value = 150;
            cells.get("A4").value = "Kiwi";
            cells.get("B4").value = 2020;
            cells.get("C4").value = 200;
            cells.get("A5").value = "Cherry";
            cells.get("B5").value = 2020;
            cells.get("C5").value = 180;
            cells.get("A6").value = "Grape";
            cells.get("B6").value = 2021;
            cells.get("C6").value = 120;
            cells.get("A7").value = "Blueberry";
            cells.get("B7").value = 2021;
            cells.get("C7").value = 170;
            cells.get("A8").value = "Kiwi";
            cells.get("B8").value = 2021;
            cells.get("C8").value = 210;
            cells.get("A9").value = "Cherry";
            cells.get("B9").value = 2021;
            cells.get("C9").value = 190;
            cells.get("A10").value = "Grape";
            cells.get("B10").value = 2021;
            cells.get("C10").value = 130;
            // Add a pivot table at E3, sourced from A1:C10
            const pivotTable = worksheet.pivotTables.add("=A1:C10", 2, 4);
            // Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // Apply a modern Excel 2007+ named preset pivot style.
            // PivotTableStyleType is the correct API for .xlsx / .xlsm / .xlsb files; AutoFormatType
            // is ignored by Excel for those formats. PivotTableStyleDark1 belongs to the dark-theme
            // family (PivotTableStyleDark1..PivotTableStyleDark28), and the same enum also exposes the
            // newer Excel 2017 light/dark themes (PivotTableStyleLight1..Light28 / Dark1..Dark28).
            pivotTable.pivotTableStyleType = AsposeCells.PivotTableStyleType.PivotTableStyleDark1;
            // Save as modern .xlsx -- this is the format for which PivotTableStyleType is meaningful.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
        </script>
    </body>
</html>
```

## **تعريف نمط جدول محوري مخصص وتطبيقه**
لا يمكن تعديل الأنماط المدمجة. عند الحاجة إلى تجاوز الألوان أو الحدود أو الخطوط، عليك تعريف نمط جدول محوري مخصص. وتتمثل العملية في ثلاث خطوات:
1. أضف نمطًا مخصصًا إلى مجموعة `tableStyles` في المصنف عبر `workbook.worksheets.tableStyles.addPivotTableStyle(name)`. يعيد هذا الأمر فهرس النمط الذي أُنشئ حديثًا.
2. اضبط النمط بإضافة عناصر (مثل `WholeTable` أو `GrandTotalRow`) عبر `tableStyle.tableStyleElements.add(tableStyleElementType)`، ثم عيّن `style` لكل عنصر عبر `tableStyleElement.setElementStyle(style)`.
3. طبّق النمط المخصص على الجدول المحوري بتعيين `pivotTable.pivotTableStyleName` إلى اسم النمط. لا تستخدم `pivotTable.pivotTableStyleType` هنا، لأن هذه الخاصية تحدد الأنماط المدمجة.

{{% alert color="primary" %}}
`pivotTable.pivotTableStyleName` و`pivotTable.pivotTableStyleType` غير قابلين للتبادل. استخدم `pivotTable.pivotTableStyleType` للأنماط المدمجة الجاهزة، واستخدم `pivotTable.pivotTableStyleName` للأنماط المخصصة التي عرّفتها عبر `addPivotTableStyle`. ولا يترتب على تعيين كليهما ضرر، لكن لا يُعرض إلا الخيار المطابق للمصدر المقصود.
تشمل قيم `TableStyleElementType` المتاحة `WholeTable`، و`FirstRow`، و`LastRow`، و`FirstColumn`، و`LastColumn`، و`GrandTotalRow`، و`GrandTotalColumn`، و`PageFieldLabels`، و`PageFieldValues`.
يعرّف المثال التالي نمط جدول محوري مخصصًا يتضمن حدًا أسود رفيعًا على `WholeTable` وخطًا أحمر عريضًا على `GrandTotalRow`، ثم يطبقه عبر `pivotTable.pivotTableStyleName` ويحفظه بصيغة `.xlsx`.
{{% /alert %}}

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
        const { Workbook } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            // Populate source data: header row + 9 data rows (A1:C10)
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            cells.get("A2").value = "Grape";
            cells.get("B2").value = 2020;
            cells.get("C2").value = 100;
            cells.get("A3").value = "Blueberry";
            cells.get("B3").value = 2020;
            cells.get("C3").value = 200;
            cells.get("A4").value = "Kiwi";
            cells.get("B4").value = 2020;
            cells.get("C4").value = 300;
            cells.get("A5").value = "Cherry";
            cells.get("B5").value = 2020;
            cells.get("C5").value = 400;
            cells.get("A6").value = "Grape";
            cells.get("B6").value = 2021;
            cells.get("C6").value = 500;
            cells.get("A7").value = "Blueberry";
            cells.get("B7").value = 2021;
            cells.get("C7").value = 600;
            cells.get("A8").value = "Kiwi";
            cells.get("B8").value = 2021;
            cells.get("C8").value = 700;
            cells.get("A9").value = "Cherry";
            cells.get("B9").value = 2021;
            cells.get("C9").value = 800;
            cells.get("A10").value = "Grape";
            cells.get("B10").value = 2021;
            cells.get("C10").value = 900;
            // Add pivot table sourced from A1:C10, anchored at E3
            const pivotTable = worksheet.pivotTables.add("=A1:C10", 2, 4);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // Step 1: register a new custom pivot table style and capture its index
            const styleIndex = workbook.worksheets.tableStyles.addPivotTableStyle("CustomPivotStyle");
            const tableStyle = workbook.worksheets.tableStyles.get(styleIndex);
            // Step 2: add a WholeTable element and apply thin black borders on all four sides
            const wholeTableElementIndex = tableStyle.tableStyleElements.add(AsposeCells.TableStyleElementType.WholeTable);
            const wholeTableElement = tableStyle.tableStyleElements.get(wholeTableElementIndex);
            const wholeTableStyle = workbook.createStyle();
            const topBorder = wholeTableStyle.borders.get(AsposeCells.BorderType.TopBorder);
            topBorder.lineStyle = AsposeCells.CellBorderType.Thin;
            topBorder.color = "black";
            const bottomBorder = wholeTableStyle.borders.get(AsposeCells.BorderType.BottomBorder);
            bottomBorder.lineStyle = AsposeCells.CellBorderType.Thin;
            bottomBorder.color = "black";
            const leftBorder = wholeTableStyle.borders.get(AsposeCells.BorderType.LeftBorder);
            leftBorder.lineStyle = AsposeCells.CellBorderType.Thin;
            leftBorder.color = "black";
            const rightBorder = wholeTableStyle.borders.get(AsposeCells.BorderType.RightBorder);
            rightBorder.lineStyle = AsposeCells.CellBorderType.Thin;
            rightBorder.color = "black";
            wholeTableElement.setElementStyle(wholeTableStyle);
            // Step 3: add a GrandTotalRow element and apply bold red font
            const grandTotalElementIndex = tableStyle.tableStyleElements.add(AsposeCells.TableStyleElementType.GrandTotalRow);
            const grandTotalElement = tableStyle.tableStyleElements.get(grandTotalElementIndex);
            const grandTotalStyle = workbook.createStyle();
            grandTotalStyle.font.isBold = true;
            grandTotalStyle.font.color = "red";
            grandTotalElement.setElementStyle(grandTotalStyle);
            // Step 4: apply the custom style by name (NOT by PivotTableStyleType, which is for built-in presets)
            pivotTable.pivotTableStyleName = "CustomPivotStyle";
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData], {
                type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **تطبيق نمط واحد على كل خلية في الجدول المحوري باستخدام formatAll**
يُعد `pivotTable.formatAll(style)` اختصارًا يطبق كائن `style` واحدًا على كل خلية في الجدول المحوري، بما في ذلك منطقة البيانات وعناوين الصفوف والأعمدة والإجماليات. يتم تجاوز كل ما سبق تعيينه عبر `pivotTable.pivotTableStyleType` أو `pivotTable.pivotTableStyleName`.

{{% alert color="primary" %}}
يتجاوز `formatAll` كلًا من `pivotTable.pivotTableStyleType` و`pivotTable.pivotTableStyleName`. استخدمه فقط عند الحاجة إلى مظهر موحد ومستقل عن السمة في جميع أنحاء الجدول المحوري.
ينشئ المثال التالي `style` ذا تعبئة صفراء صلبة وخط أزرق داكن عريض وحدود سوداء رفيعة على جميع الجهات، ثم يطبقه عبر `formatAll` ويحفظه بصيغة `.xlsx`.
{{% /alert %}}

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
            // Scenario 4: Apply a single Style to every pivot table cell using FormatAll
            // API in use: PivotTable.FormatAll(Style)
            // Target format: .xlsx
            // GitHub reference: see Aspose.Cells-for-.NET repository — pivot table styling examples
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            // Populate source data: header row (row 1) + 9 data rows (rows 2-10)
            const cells = worksheet.cells;
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            cells.get("A2").value = "Grape";
            cells.get("B2").value = 2020;
            cells.get("C2").value = 5000;
            cells.get("A3").value = "Blueberry";
            cells.get("B3").value = 2020;
            cells.get("C3").value = 3000;
            cells.get("A4").value = "Kiwi";
            cells.get("B4").value = 2020;
            cells.get("C4").value = 4000;
            cells.get("A5").value = "Cherry";
            cells.get("B5").value = 2020;
            cells.get("C5").value = 2000;
            cells.get("A6").value = "Grape";
            cells.get("B6").value = 2021;
            cells.get("C6").value = 6000;
            cells.get("A7").value = "Blueberry";
            cells.get("B7").value = 2021;
            cells.get("C7").value = 3500;
            cells.get("A8").value = "Kiwi";
            cells.get("B8").value = 2021;
            cells.get("C8").value = 4500;
            cells.get("A9").value = "Cherry";
            cells.get("B9").value = 2021;
            cells.get("C9").value = 2500;
            cells.get("A10").value = "Grape";
            cells.get("B10").value = 2021;
            cells.get("C10").value = 5500;
            // Add pivot table: source range A1:C10, destination cell E3
            const pivotTable = worksheet.pivotTables.add("=A1:C10", 2, 4);
            // Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // Build a Style that will be forced onto every cell of the pivot table
            const style = workbook.createStyle();
            style.foregroundColor = AsposeCells.Color.Yellow;
            style.pattern = AsposeCells.BackgroundType.Solid;
            style.font.isBold = true;
            style.font.color = AsposeCells.Color.DarkBlue;
            style.borders.get(AsposeCells.BorderType.TopBorder).lineStyle = AsposeCells.CellBorderType.Thin;
            style.borders.get(AsposeCells.BorderType.TopBorder).color = AsposeCells.Color.Black;
            style.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Thin;
            style.borders.get(AsposeCells.BorderType.BottomBorder).color = AsposeCells.Color.Black;
            style.borders.get(AsposeCells.BorderType.LeftBorder).lineStyle = AsposeCells.CellBorderType.Thin;
            style.borders.get(AsposeCells.BorderType.LeftBorder).color = AsposeCells.Color.Black;
            style.borders.get(AsposeCells.BorderType.RightBorder).lineStyle = AsposeCells.CellBorderType.Thin;
            style.borders.get(AsposeCells.BorderType.RightBorder).color = AsposeCells.Color.Black;
            // Apply FormatAll: forces this single style onto every cell of the pivot table,
            // overriding any PivotTableStyleType / PivotTableStyleName previously set
            pivotTable.formatAll(style);
            // Save the workbook in the modern .xlsx format
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **أي واجهة API للتنسيق ينبغي استخدامها؟**
يعتمد اختيار واجهة API للتنسيق على صيغة الملف الذي تحفظه. استخدم الجدول التالي كمرجع سريع.
| صيغة الملف الهدف | واجهة API التي ينبغي استخدامها | ملاحظات |
|---|---|---|
| `.xls` (قديم) | `pivotTable.autoFormatType` | القيم من `Aspose.Cells.Pivot.PivotTableAutoFormatType` (مثل `Report1`–`Report10`، و`Classic`، و`Table1`–`Table10`). يُتجاهل هذا الإعداد عند الحفظ في الصيغ الحديثة. |
| `.xlsx` / `.xlsm` / `.xlsb` (حديث، نمط مدمج) | `pivotTable.pivotTableStyleType` | القيم من `Aspose.Cells.PivotTableStyleType` (السمات الفاتحة والداكنة، بما في ذلك إضافات Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (حديث، نمط مخصص) | `pivotTable.pivotTableStyleName` + `workbook.worksheets.tableStyles.addPivotTableStyle(...)` | استخدم واجهة API هذه عندما لا تكفي الأنماط المدمجة الجاهزة، واضبط النمط عبر `tableStyleElement.setElementStyle(...)`. |
| أي صيغة (تجاوز موحد) | `pivotTable.formatAll(style)` | اختصار يتجاوز كل إعداد نمط آخر في الجدول المحوري بالكامل. |
في حالة الشك، احفظ الملف بصيغة `.xlsx` واستخدم `pivotTable.pivotTableStyleType` للسمات المدمجة، أو `pivotTable.pivotTableStyleName` للسمات المخصصة.

{{< app/cells/assistant language="javascript-cpp" >}}
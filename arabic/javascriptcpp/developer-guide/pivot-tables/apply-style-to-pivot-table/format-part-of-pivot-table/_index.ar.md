---
title: تنسيق جزء من جدول محوري
linktitle: تنسيق جزء من جدول محوري
description: تنسيق جزء من جدول محوري في Aspose.Cells for JavaScript via C++ عن طريق تطبيق الأنماط على مناطق PivotArea الدلالية أو مستطيلات CellArea عبر PivotTable.Format، مع تخزين التنسيقات في PivotTable.PivotFormats والحفاظ عليها عند تحديث جدول محوري.
keywords: Aspose.Cells for JavaScript via C++, جدول محوري, تنسيق, PivotArea, CellArea, PivotTable.Format, PivotFormats, PivotTableSelectionType, LabelOnly, DataOnly, SelectField, FormatAll, C++
type: docs
weight: 20
url: /ar/javascript-cpp/format-part-of-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام الممكنة**
`PivotTable.FormatAll` يطبق نمطًا واحدًا على كامل جدول محوري ويتم تغطيته في الصفحة الأم. لا يميز بين الملصقات، القيم، الإجماليات، أو مناطق معينة في التقرير.
في الواقع، عادةً ما يحتاج جزء فقط من جدول محوري إلى إبراز. تشمل الأهداف الشائعة الملصقات التابعة لحقل صف واحد، الخلايا التي تحتوي على القيم التي ينتجها حقل معين، صف الإجمالي الكلي، أو مستطيل عشوائي مثل الصفين الأولين للعناصر.
تطبيق نمط مباشرةً على خلايا ورقة عمل لجدول محوري ليس مكافئًا. Excel يخزن تنسيق الجداول المحورية كمناطق `PivotArea` دلالية بدلاً من سجلات أنماط الخلايا العادية. يبقى تنسيق منطقة pivot مرتبطًا بمنطقة مثل ملصقات حقل أو قيم البيانات، ويتم إعادة حلها عندما يُعاد حساب جدول محوري أو يُنعَّش أو يُوسَّع. أما النمط المكتوب مباشرةً إلى خلية، فهو ينتمي إلى موقع تلك الخلية ولا يتعقّبها نموذج الجدول المحوري.
Aspose.Cells يعرض العائلة الكاملة لتجاوزات `PivotTable.Format` بحيث يتوفر كلا النوعين من التنسيق:
- `Format(PivotArea, Style)` يربط نمطًا بمنطقة دلالية تُبنى باستخدام `PivotArea.Select` أو `PivotArea.SelectField`.
- `Format(CellArea, Style)` يربط نمطًا بمستطيل ورقة عمل داخل جدول محوري.
- `Format(int row, int column, Style)` يستهدف خلية واحدة.
- `FormatAll(Style)` ينسق كامل جدول محوري.

## **تنسيق منطقة PivotArea**
سير عمل المنطقة الدلالية هو النهج الموصى به عندما يجب أن يتبع التمييز حقلًا أو منطقةً في التقرير.
1. أنشئ `PivotArea` باستخدام `new PivotArea(pivotTable)`. يصف هذا الكائن منطقة دلالية تنتمي إلى جدول محوري محدد.
2. حدّد حقلًا بحسب موضعه الصفري على محور معين باستخدام `PivotArea.Select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)`.
   - `PivotTableSelectionType.DataAndLabel` يحدد كلًا من الملصقات والبيانات الخاصة بالحقل.
   - `PivotTableSelectionType.LabelOnly` يحدد ملصقات الحقل فقط.
   - `PivotTableSelectionType.DataOnly` يحدد خلايا بيانات الحقل فقط.
3. حدّد حقلًا بالاسم باستخدام `PivotArea.SelectField(PivotFieldType axisType, string fieldName)`. عندما يتم اختيار حقل صف بالاسم، تتحول المنطقة إلى خلايا القيم التي ينتجها عناصر ذلك الحقل.
4. أنشئ `Style` باستخدام `Workbook.CreateStyle()`، واضبط الخط ولون المقدمة ونمط الخلفية الصلبة، ثم مرّر النمط إلى `PivotTable.Format(area, style)`.
5. كل استدعاء لتجاوز `PivotArea` يضيف إدخالًا واحدًا من نوع `PivotTableFormat` إلى `PivotTable.PivotFormats`.
6. تُرسم التنسيقات المرتبطة بالحقل عندما يتم حساب بيانات الجدول المحوري. لذلك، استدعِ `PivotTable.CalculateData()` بعد تطبيق التنسيقات لكي تصبح الأنماط مرئية.
المثال التالي ينشئ جدولًا محوريًا صغيرًا لمبيعات الفاكهة، ويُنسّق ملصقات صف `Fruit` باستخدام `PivotArea.Select` و `PivotTableSelectionType.LabelOnly`، ويُنسّق خلايا القيمة التي ينتجها نفس حقل الصف باستخدام `PivotArea.SelectField`، ثم يُعيد حساب جدول محوري بحيث تُظهر كلا النمطين.

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
            const sheet = workbook.worksheets.get(0);
            const cells = sheet.cells;
            // Fruit sales data
            const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
            const years = [2024, 2024, 2025, 2025, 2024, 2025];
            const amounts = [100, 150, 120, 180, 90, 110];
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            for (let i = 0; i < fruits.length; i++) {
                cells.get(i + 1, 0).value = fruits[i];
                cells.get(i + 1, 1).value = years[i];
                cells.get(i + 1, 2).value = amounts[i];
            }
            // Pivot table with its top-left corner at E3 (row 2, column 4)
            const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            pivotTable.calculateData();
            // Bold yellow fill on the row field's label cells
            const labelStyle = workbook.createStyle();
            labelStyle.font.isBold = true;
            labelStyle.foregroundColor = AsposeCells.Color.Yellow;
            labelStyle.pattern = AsposeCells.BackgroundType.Solid;
            const labelArea = new AsposeCells.PivotArea(pivotTable);
            labelArea.select(
                AsposeCells.PivotFieldType.Row,
                0,
                AsposeCells.PivotTableSelectionType.LabelOnly
            );
            pivotTable.format(labelArea, labelStyle);
            // Light green fill on the value cells the row field produces
            const valueStyle = workbook.createStyle();
            valueStyle.foregroundColor = AsposeCells.Color.LightGreen;
            valueStyle.pattern = AsposeCells.BackgroundType.Solid;
            const valueArea = new AsposeCells.PivotArea(pivotTable);
            valueArea.selectField(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.format(valueArea, valueStyle);
            // Field-anchored formats are painted when the data is calculated
            pivotTable.calculateData();
            // Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "FormatPivotArea.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **تنسيق منطقة خلية ضمن جدول محوري**
استخدم `PivotTable.Format(CellArea, Style)` عندما تكون المنطقة المطلوبة مستطيل ورقة عمل عادي بدلاً من منطقة pivot دلالية.
`CellArea` يَُوصف بالحقول `startRow` و `startColumn` و `endRow` و `endColumn`. القيم هي إحداثيات ورقة العمل بصفرية، وتحدد إحداثيات النهاية الصف والعمود الأخيرين المشمولين في المستطيل، لذا يغطي المنطقة الخلايا من الموضع الابتدائي حتى الموضع النهائي شاملًا.
على عكس التنسيق المرتبط بالحقل، يتم تطبيق تنسيق `CellArea` على الخلايا فورًا. لا يلزم استدعاء إضافي لـ `CalculateData()` لظهور النمط.
قد يحتوي مستطيل `CellArea` على خلايا تسميات وخلايا قيم معًا. يصف القسم التالي كيف تمثل Aspose.Cells وExcel ذلك المستطيل داخليًا.
المثال التالي ينسق المستطيل `E4:F5` من جدول محوري بنمط مائل، أزرق فاتح، ويحفظ المصنف دون أي إعادة حساب إضافية.

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
            const sheet = workbook.worksheets.get(0);
            const cells = sheet.cells;
            const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
            const years = [2024, 2024, 2025, 2025, 2024, 2025];
            const amounts = [100, 150, 120, 180, 90, 110];
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            for (let i = 0; i < fruits.length; i++) {
                cells.get(i + 1, 0).value = fruits[i];
                cells.get(i + 1, 1).value = years[i];
                cells.get(i + 1, 2).value = amounts[i];
            }
            const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            pivotTable.calculateData();
            // Highlight the first two fruit rows (the rectangle E4:F5)
            const highlightStyle = workbook.createStyle();
            highlightStyle.font.isItalic = true;
            highlightStyle.foregroundColor = AsposeCells.Color.LightBlue;
            highlightStyle.pattern = AsposeCells.BackgroundType.Solid;
            const rectangle = new AsposeCells.CellArea();
            rectangle.startRow = 3;
            rectangle.startColumn = 4;
            rectangle.endRow = 4;
            rectangle.endColumn = 5;
            pivotTable.format(rectangle, highlightStyle);
            // E4:F5 is italic on light blue immediately, no recalculation needed
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "FormatPivotCellArea.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **كيفية ربط مناطق Pivot ومناطق CellArea**
Excel يخزن تنسيق الجداول المحورية كسجلات `pivotArea` بدلاً من سجلات أنماط خلايا ورقة عمل عادية. يستخدم Aspose.Cells نفس النموذج، لذا يتم ترجمة طلب التنسيق إلى مناطق pivot عند تسجيله.
العلاقة بين `CellArea` التي يزودها المستخدم ومناطق pivot المخزنة داخليًا هي علاقة متعدد‑إلى‑متعدد في كلا الاتجاهين.
- قد ينتج `CellArea` واحد عدة مناطق pivot. إذا كان المستطيل يشمل كلًا من خلايا التسميات وخلايا القيم، فإنه يُقسَّم إلى قواعد للملصقات والبيانات منفصلة، لأن نموذج pivot يتعامل مع تنسيق الملصقات وتنسيق البيانات بشكل مستقل.
- قد تتحول منطقة pivot واحدة إلى عدة أمثلة `CellArea` منفصلة. يمكن لمنطقة دلالية مثل صف الإجمالي الكلي، أو حقل لا تكون عناصره متجاورة، أن يغطي مستطيلات متعددة. لهذا السبب تُرجع `PivotArea.GetCellAreas()` مجموعة بدلاً من مستطيل واحد.
يتم تسجيل كل عملية تنسيق تُجرى عبر `PivotTable.Format` في `PivotTable.PivotFormats`. كل إدخال من نوع `PivotTableFormat` يعرض `PivotArea` المرتبطة والنمط `Style` المطبق عليها. يُضيف تجاوز `PivotArea` إدخالًا واحدًا بالضبط لكل استدعاء، بينما يمكن لـ `CellArea` الذي يحتوي على مناطق دلالية مختلفة إضافة عدة إدخالات.
لتمييز المناطق المخزنة، تعرض كل `PivotArea` العلامتين `OnlyLabel` و `OnlyData`. المثال أدناه ينسق مستطيلًا واحدًا يغطي كلًا من الملصقات والقيم، ويستعرض `PivotTable.PivotFormats`، ويطبع إحداثيات `CellArea` التي تحل كل منطقة pivot مخزنة إليها.

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
            const { Workbook, SaveFormat, CellArea, Color } = AsposeCells;
            AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            document.getElementById("runExample").addEventListener("click", async () => {
                const result = document.getElementById("result");
                const downloadLink = document.getElementById("downloadLink");
                const workbook = new Workbook();
                const sheet = workbook.worksheets.get(0);
                const cells = sheet.cells;
                const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
                const years = [2024, 2024, 2025, 2025, 2024, 2025];
                const amounts = [100, 150, 120, 180, 90, 110];
                cells.get("A1").value = "Fruit";
                cells.get("B1").value = "Year";
                cells.get("C1").value = "Amount";
                for (let i = 0; i < fruits.length; i++) {
                    cells.get(i + 1, 0).value = fruits[i];
                    cells.get(i + 1, 1).value = years[i];
                    cells.get(i + 1, 2).value = amounts[i];
                }
                const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                pivotTable.calculateData();
                const highlightStyle = workbook.createStyle();
                highlightStyle.font.isItalic = true;
                highlightStyle.foregroundColor = Color.LightBlue;
                highlightStyle.pattern = AsposeCells.BackgroundType.Solid;
                // ONE rectangle in...
                const rectangle = new CellArea();
                rectangle.startRow = 3;
                rectangle.startColumn = 4;
                rectangle.endRow = 4;
                rectangle.endColumn = 5;
                // ...TWO semantic pivot areas out: the label part and the data part are stored separately
                pivotTable.format(rectangle, highlightStyle);
                const pivotFormats = pivotTable.pivotFormats;
                const outputLines = [`Stored formats: ${pivotFormats.count}`];
                for (let i = 0; i < pivotFormats.count; i++) {
                    const pivotFormat = pivotFormats.get(i);
                    const storedArea = pivotFormat.pivotArea;
                    const onlyLabel = storedArea.onlyLabel ? "True" : "False";
                    const onlyData = storedArea.onlyData ? "True" : "False";
                    outputLines.push(`Format ${i}: OnlyLabel=${onlyLabel}, OnlyData=${onlyData}`);
                    const resolvedAreas = storedArea.cellAreas;
                    for (let j = 0; j < resolvedAreas.count; j++) {
                        const resolved = resolvedAreas.get(j);
                        outputLines.push(
                            `    rows ${resolved.startRow + 1}-${resolved.endRow + 1}, columns ${resolved.startColumn + 1}-${resolved.endColumn + 1}`
                        );
                    }
                }
                // This prints:
                // Stored formats: 2
                // Format 0: OnlyLabel=True, OnlyData=False
                //     rows 4-5, columns 5-5        (E4:E5, the label part)
                // Format 1: OnlyLabel=False, OnlyData=True
                //     rows 4-5, columns 6-6        (F4:F5, the data part)
                result.innerHTML =
                    `<pre>${outputLines.join("\n")}</pre>` +
                    `<p style="color: green;">Done! Click the download link to get the result file.</p>`;
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "FormatPivotAreasMap.xlsx";
                downloadLink.style.display = "block";
            });
        </script>
    </body>
</html>
```

{{% alert color="primary" %}}
نظرًا لأن التنسيقات تُخزن كمناطق pivot بدلاً من أنماط خلايا عادية، فإنها تبقى بعد إعادة الحساب والتحديث. عندما يتم تحديث جدول محوري باستخدام `PivotTable.RefreshData`، أو إعادة حسابه بـ `CalculateData`، أو حفظه وإعادة تحميله، تعيد كل منطقة pivot مخزنة حل موقعها الحالي وتُطبق النمط مرة أخرى.
{{% /alert %}}

استخدم `PivotArea` المبنية بـ `Select` أو `SelectField` عندما يجب أن يبقى التمييز مرتبطًا بحقل أو منطقة دلالية عبر عمليات التحديث، واستخدم `CellArea` عندما يكون تنسيق مستطيل ثابت في تخطيط جدول محوري الحالي كافيًا. يتوجه تجاوز `Format(int row, int column, Style)` للخلية الواحدة. استخدم `FormatAll`، الذي يُغطى في الصفحة الأم، عندما يجب إعادة تنسيق كامل جدول محوري مرة واحدة.

## **مقالات ذات صلة**
- [تطبيق نمط على جدول محوري](/cells/ar/javascript-cpp/apply-style-to-pivot-table/)
- [إضافة حقول الصف والعمود إلى جدول محوري](/cells/ar/javascript-cpp/pivot-table-add-row-and-column-fields/)
- [إدارة حقول القيم في جدول محوري](/cells/ar/javascript-cpp/manage-value-fields/)
- [تحديث جدول محوري](/cells/ar/javascript-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}
---
title: إضافة حقول الصفوف والأعمدة إلى جدول محوري في Aspose.Cells for JavaScript via C++
linktitle: إضافة حقول الصفوف والأعمدة إلى جدول محوري في Aspose.Cells for JavaScript via C++
description: تعلّم كيفية إضافة حقول الصفوف والأعمدة إلى جدول محوري والتحكم في المجاميع الفرعية لحقول الجدول المحوري باستخدام PivotField.SetSubtotals مع PivotFieldSubtotalType في Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells, JavaScript via C++, جدول محوري, حقل صف, حقل عمود, PivotField, setSubtotals, PivotFieldSubtotalType, مجاميع فرعية, JavaScript, جدول محوري في Excel
type: docs
weight: 220
url: /ar/javascript-cpp/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **إضافة حقل إلى منطقة الصفوف أو الأعمدة**
تنقل الطريقة `pivotTable.addFieldToArea(fieldType, fieldName)` حقلًا أساسيًا من بيانات المصدر إلى إحدى مناطق الجدول المحوري الأربع. تقبل الوسيطة `fieldType` إحدى قيم `PivotFieldType` التالية.
- `Row` — حقول موضوعة عموديًا على اليسار
- `Column` — حقول موضوعة أفقيًا عبر الأعلى
- `Data` — حقول يتم تجميع قيمها
- `Page` — حقول تُستخدم كمرشحات للتقرير
ترتيب تداخل الحقول مهم. فعند إضافة `Category` إلى منطقة الصفوف أولًا ثم `Item`، ينتج جدول محوري يكون التجميع الخارجي فيه هو `Category` والتجميع الداخلي فيه هو `Item`. ويؤدي عكس الترتيب إلى عكس التسلسل الهرمي.

## **المجاميع الفرعية لحقول الجدول المحوري**
تتحكم الطريقة `pivotField.setSubtotals(subtotalType, shown)` في صفوف المجاميع الفرعية التي تظهر لحقل الجدول المحوري. يبدّل كل استدعاء نوعًا واحدًا من المجاميع الفرعية بشكل مستقل. يؤدي تمرير `shown = true` إلى عرض المجموع الفرعي، بينما يؤدي `shown = false` إلى إخفائه. ولأن كل استدعاء يؤثر في نوع واحد فقط، فإن استدعاء الطريقة عدة مرات بقيم `subtotalType` المختلفة يبني مجموعة فرعية مخصصة من المجاميع الفرعية.
يحدد التعداد `PivotFieldSubtotalType` أنواع المجاميع الفرعية المتاحة.
- `Automatic` — يختار Aspose.Cells التحديد الافتراضي (عادةً `Sum` للحقول الرقمية)
- `None` — يمنع عرض كل صفوف المجاميع الفرعية
- `Sum`
- `Count`
- `Average`
- `Max`
- `Min`
- `Product`
- `StdDev`
- `StdDevp`
- `Var`
- `Varp`

{{% alert color="primary" %}}
لا تُعرض المجاميع الفرعية إلا عند وجود حقلين أو أكثر من حقول الجدول المحوري في منطقة الصفوف (أو منطقة الأعمدة). لا يوجد لدى الحقل الواحد ما يمكن تلخيصه بين المجموعات، لذا تكون استدعاءات `setSubtotals` بلا تأثير ظاهر في هذه الحالة. لذلك تضع هذه المقالة حقلين في منطقة الصفوف، هما `Category` كحقل خارجي و`Item` كحقل داخلي، في كل مثال، حتى يظهر الحد الفاصل للمجاميع الفرعية بين كل مجموعة `Category`.
{{% /alert %}}

## **السيناريو 1 — المجاميع الفرعية التلقائية (الافتراضية)**
إذا لم تستدعِ `setSubtotals` إطلاقًا، فسيطبق Aspose.Cells تحديد `Automatic` على الحقول الرقمية. ويؤكد المثال التالي هذا السلوك صراحةً من خلال استدعاء `setSubtotals(PivotFieldSubtotalType.Automatic, true)` على حقل الصف الخارجي `Category`.

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
        const readyPromise = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "Data";
            const cells = worksheet.cells;
            cells.get(0, 0).value = "Category";
            cells.get(0, 1).value = "Item";
            cells.get(0, 2).value = "Year";
            cells.get(0, 3).value = "Amount";
            cells.get(1, 0).value = "Fruit";
            cells.get(1, 1).value = "Apple";
            cells.get(1, 2).value = 2020;
            cells.get(1, 3).value = 100;
            cells.get(2, 0).value = "Fruit";
            cells.get(2, 1).value = "Apple";
            cells.get(2, 2).value = 2021;
            cells.get(2, 3).value = 150;
            cells.get(3, 0).value = "Fruit";
            cells.get(3, 1).value = "Banana";
            cells.get(3, 2).value = 2020;
            cells.get(3, 3).value = 80;
            cells.get(4, 0).value = "Fruit";
            cells.get(4, 1).value = "Banana";
            cells.get(4, 2).value = 2021;
            cells.get(4, 3).value = 90;
            cells.get(5, 0).value = "Vegetable";
            cells.get(5, 1).value = "Carrot";
            cells.get(5, 2).value = 2020;
            cells.get(5, 3).value = 50;
            cells.get(6, 0).value = "Vegetable";
            cells.get(6, 1).value = "Carrot";
            cells.get(6, 2).value = 2021;
            cells.get(6, 3).value = 60;
            cells.get(7, 0).value = "Vegetable";
            cells.get(7, 1).value = "Daikon";
            cells.get(7, 2).value = 2020;
            cells.get(7, 3).value = 40;
            cells.get(8, 0).value = "Vegetable";
            cells.get(8, 1).value = "Daikon";
            cells.get(8, 2).value = 2021;
            cells.get(8, 3).value = 45;
            const pivotTable = worksheet.pivotTables.add("=A1:D9", 2, 5);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            const categoryField = pivotTable.rowFields.get(0);
            categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Automatic, true);
            pivotTable.calculateData();
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_automatic.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **السيناريو 2 — منع جميع المجاميع الفرعية (None)**
يزيل استدعاء `setSubtotals(PivotFieldSubtotalType.None, true)` جميع صفوف المجاميع الفرعية من الجدول المحوري، تاركًا صفوف الحقول فقط والإجمالي الكلي في الأسفل. وهذا مفيد عند الرغبة في عرض البيانات المجمَّعة الخام دون أي صفوف ملخص.

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
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "Data";
            const headers = ["Category", "Item", "Year", "Amount"];
            for (let j = 0; j < headers.length; j++) {
                worksheet.cells.get(0, j).value = headers[j];
            }
            const data = [
                ["Fruit", "Apple", 2020, 100],
                ["Fruit", "Apple", 2021, 150],
                ["Fruit", "Banana", 2020, 80],
                ["Fruit", "Banana", 2021, 90],
                ["Vegetable", "Carrot", 2020, 50],
                ["Vegetable", "Carrot", 2021, 60],
                ["Vegetable", "Daikon", 2020, 40],
                ["Vegetable", "Daikon", 2021, 45]
            ];
            for (let i = 0; i < data.length; i++) {
                for (let j = 0; j < data[i].length; j++) {
                    worksheet.cells.get(i + 1, j).value = data[i][j];
                }
            }
            const pivotTable = worksheet.pivotTables.add("=A1:D9", 2, 5);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            const categoryField = pivotTable.rowFields.get(0);
            categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.None, true);
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_none.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **السيناريو 3 — مجموعة فرعية مخصصة من المجاميع الفرعية (Sum + Average)**
لا يتقيد الاستخدام بنوع واحد من المجاميع الفرعية. يعمل كل استدعاء لـ `setSubtotals` بشكل مستقل على نوع واحد. ومن ثم، فإن استدعاء الطريقة مرتين — مرة مع `Sum` ومرة مع `Average` — ينتج مجموعة فرعية مخصصة من صفين للمجاميع الفرعية لكل مجموعة `Category`.

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
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "Data";
            const cells = worksheet.cells;
            cells.get("A1").value = "Category";
            cells.get("B1").value = "Item";
            cells.get("C1").value = "Year";
            cells.get("D1").value = "Amount";
            cells.get(1, 0).value = "Fruit";
            cells.get(1, 1).value = "Apple";
            cells.get(1, 2).value = 2020;
            cells.get(1, 3).value = 100;
            cells.get(2, 0).value = "Fruit";
            cells.get(2, 1).value = "Apple";
            cells.get(2, 2).value = 2021;
            cells.get(2, 3).value = 150;
            cells.get(3, 0).value = "Fruit";
            cells.get(3, 1).value = "Banana";
            cells.get(3, 2).value = 2020;
            cells.get(3, 3).value = 80;
            cells.get(4, 0).value = "Fruit";
            cells.get(4, 1).value = "Banana";
            cells.get(4, 2).value = 2021;
            cells.get(4, 3).value = 90;
            cells.get(5, 0).value = "Vegetable";
            cells.get(5, 1).value = "Carrot";
            cells.get(5, 2).value = 2020;
            cells.get(5, 3).value = 50;
            cells.get(6, 0).value = "Vegetable";
            cells.get(6, 1).value = "Carrot";
            cells.get(6, 2).value = 2021;
            cells.get(6, 3).value = 60;
            cells.get(7, 0).value = "Vegetable";
            cells.get(7, 1).value = "Daikon";
            cells.get(7, 2).value = 2020;
            cells.get(7, 3).value = 40;
            cells.get(8, 0).value = "Vegetable";
            cells.get(8, 1).value = "Daikon";
            cells.get(8, 2).value = 2021;
            cells.get(8, 3).value = 45;
            const pivotTables = worksheet.pivotTables;
            const pivotTable = pivotTables.add("=A1:D9", 2, 5);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            const categoryField = pivotTable.rowFields.get(0);
            categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Sum, true);
            categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Average, true);
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_custom.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **الملخص**
تختلف السيناريوهات الثلاثة في شيء واحد فقط: استدعاءات `setSubtotals`. وكل ما عدا ذلك — مجموعة البيانات والحقول والمناطق التي تُسنَد إليها — متطابق، وهو ما يجعل التخطيطات قابلة للمقارنة مباشرة.
- **وضع الحقول.** تنقل الطريقة `pivotTable.addFieldToArea(PivotFieldType.Row, fieldName)` عمودًا من بيانات المصدر إلى إحدى المناطق. وداخل المنطقة الواحدة، يمثل ترتيب الاستدعاءات ترتيب العرض، لذا تكون نتيجة الاستدعاء الأول هي المجموعة الخارجية. تحتاج المجاميع الفرعية إلى حقلين أو أكثر ضمن المنطقة نفسها: فمع حقل واحد لا يوجد شيء بين المجموعات يمكن تلخيصه.
- **السيناريو 1 — المجاميع الفرعية التلقائية.** عدم استدعاء `setSubtotals` يترك الخيار إلى Excel، الذي يطبق مجموعه الفرعي الافتراضي على الحقول الرقمية. ويؤدي استدعاء `setSubtotals` مع `PivotFieldSubtotalType.Automatic` إلى تسجيل هذا الاختيار صراحةً بدلًا من تركه ضمنيًا.
- **السيناريو 2 — بلا مجاميع فرعية.** يؤدي `setSubtotals` مع `PivotFieldSubtotalType.None` إلى تعطيل المجموع الفرعي الافتراضي، فيحتفظ الجدول المحوري بصفوف الحقول والإجمالي الكلي، لكنه يحذف صفوف المجاميع الفرعية التي كان Excel سيدرجها بينهما.
- **السيناريو 3 — مجموعة فرعية مختارة.** يبدّل كل استدعاء نوعًا واحدًا بالضبط، وتتراكم الاستدعاءات بدلًا من أن تعيد ضبط بعضها البعض. لذلك، عند استدعاء الطريقة مرة واحدة مع `PivotFieldSubtotalType.Sum` ومرة أخرى مع `PivotFieldSubtotalType.Average`، يبقى كلا النوعين مفعّلًا، ويعرض الجدول المحوري مجموعًا فرعيًا من نوع `Sum`، ومتوسطًا فرعيًا من نوع `Average`، وإجماليًا كليًا.

{{% alert color="primary" %}}
لا شيء في المجاميع الفرعية خاص بمنطقة الصفوف. وتنتج الاستدعاءات ذاتها لـ `setSubtotals` على حقل مأخوذ من `pivotTable.getColumnFields()` التخطيطات الثلاثة ذاتها على محور الأعمدة، لأن هذا الإعداد يخص حقل الجدول المحوري، لا المحور الذي وُضع فيه.
{{% /alert %}}

## **مقالات ذات صلة**
- [حقول الصفحة في الجداول المحورية](/cells/ar/javascript-cpp/add-page-field-in-pivot-table/)
- [إعادة تحديث الجداول المحورية في Aspose.Cells for JavaScript via C++](/cells/ar/javascript-cpp/refresh-pivot-table/)
- [تطبيق الأنماط على الجداول المحورية](/cells/ar/javascript-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}
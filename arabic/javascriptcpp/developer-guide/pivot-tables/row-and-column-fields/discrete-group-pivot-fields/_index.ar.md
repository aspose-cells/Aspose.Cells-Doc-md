---
title: التجميع المتقطع لعناصر حقول الجدول المحوري
linktitle: التجميع المتقطع
description: تعرّف على كيفية تجميع عناصر حقول الجدول المحوري في مجموعات مخصصة ذات أسماء، مثل الفواكه والخضروات، باستخدام `DiscreteGroupItem` و`PivotFieldGroupOptions.discreteGroupItems` في Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells, جدول محوري, التجميع المتقطع, DiscreteGroupItem, PivotFieldGroupOptions, تجميع عناصر الحقول المحورية, المجموعات المخصصة, PivotField.group, Aspose.Cells for JavaScript via C++, Excel جدول محوري
type: docs
weight: 90
url: /ar/javascript-cpp/discrete-group-pivot-fields/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام المحتملة**
- يقوم التجميع التلقائي بجمع العناصر حسب نوع البيانات، مثل تجميع التواريخ في أشهر وأرباع أو الأرقام في نطاقات. يعالج التجميع المتقطع المشكلة المعاكسة، إذ يجمع عناصر محددة وغير مترابطة في مجموعات مخصصة ذات أسماء، مثل تجميع المنتجات في الفواكه والخضروات، والمتاجر في المناطق، والحسابات في المناطق التخطيطية. يوفر Aspose.Cells التجميع المتقطع عبر فئة `DiscreteGroupItem` وخاصية `PivotFieldGroupOptions.discreteGroupItems`.
- يمثل `DiscreteGroupItem` اسم مجموعة مع العناصر التي تنتمي إليها. يمكن تحديد العناصر بطريقتين: حسب أسمائها (`new DiscreteGroupItem("fruit", ["grape", "cherry"])`) أو حسب مواضعها المرقّمة من الصفر في بيانات المصدر (`new DiscreteGroupItem("fruit", [0, 3])`). وتنتج الصيغتان النتيجة نفسها.
- يُطبَّق التجميع المتقطع على حقل في منطقة الصفوف أو الأعمدة في الجدول المحوري، من خلال تمرير الخيارات إلى `PivotField.group(PivotFieldGroupOptions)`.

## **تجميع عناصر حقول الجدول المحوري حسب أسماء العناصر**
يبني المثال التالي قائمة مبيعات صغيرة (`product` و`date` و`amount`)، وينشئ جدولًا محوريًا منها، مع وضع `product` في منطقة الصفوف، و`date` في منطقة الأعمدة، و`amount` في منطقة البيانات. ثم يعرّف مجموعتين مخصصتين حسب أسماء العناصر: `fruit` (`grape` و`cherry`) و`vegetables` (`carrot` و`potato`). تعرض النتيجة تخطيطًا من مستويين للصفوف، يكون اسم المجموعة فيه هو المستوى الخارجي، وتظهر العناصر الأصلية متداخلة تحته، بحيث يمكن قراءة الاتجاهات لكل مجموعة مخصصة ولكل عنصر.

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
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
            const { Workbook, DiscreteGroupItem, PivotFieldGroupOptions } = AsposeCells;
            document.getElementById('runExample').addEventListener('click', async () => {
                const workbook = new Workbook();
                const sheet = workbook.worksheets.get(0);
                const cells = sheet.cells;
                cells.get(0, 0).value = "product";
                cells.get(1, 0).value = "grape";
                cells.get(2, 0).value = "carrot";
                cells.get(3, 0).value = "potato";
                cells.get(4, 0).value = "cherry";
                const dateStyle = workbook.createStyle();
                dateStyle.custom = "m/d/yyyy";
                cells.get(0, 1).value = "date";
                cells.get(1, 1).value = new Date(2021, 1, 5);
                cells.get(2, 1).value = new Date(2022, 2, 8);
                cells.get(3, 1).value = new Date(2023, 3, 10);
                cells.get(4, 1).value = new Date(2024, 4, 16);
                for (let r = 1; r <= 4; r++) {
                    cells.get(r, 1).style = dateStyle;
                }
                cells.get(0, 2).value = "amount";
                cells.get(1, 2).value = 50;
                cells.get(2, 2).value = 60;
                cells.get(3, 2).value = 70;
                cells.get(4, 2).value = 80;
                // Add a pivot table with the destination cell A12 (row 11, column 0)
                const pivotTable = sheet.pivotTables.add("=Sheet1!A1:C5", 11, 0);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "product");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "date");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "amount");
                pivotTable.pivotTableStyleType =
                    AsposeCells.PivotTableStyleType.PivotTableStyleMedium10;
                // Group specific items into custom groups by item names
                const fruit = new DiscreteGroupItem("fruit", ["grape", "cherry"]);
                const vegetable = new DiscreteGroupItem("vegetable", ["carrot", "potato"]);
                const groupOptions = new PivotFieldGroupOptions();
                groupOptions.discreteGroupItems = [fruit, vegetable];
                pivotTable.rowFields.get(0).group(groupOptions);
                pivotTable.calculateData();
                const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "outputDiscreteGroupPivotField.xlsx";
                downloadLink.style.display = "block";
                document.getElementById('result').innerHTML =
                    '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        });
    </script>
</html>
```

بعد `calculateData()`، تعرض منطقة الصفوف في الجدول المحوري `fruit` (`grape` 50، `cherry` 80) و`vegetable` (`carrot` 60، `potato` 70)، بإجمالي عام قدره 260، مع بقاء تسميات الأعمدة محتويةً على التواريخ الأربعة (2/5/2021، 3/8/2022، 4/10/2023، 5/16/2024).

## **تجميع عناصر حقول الجدول المحوري حسب فهارس العناصر**
عندما تكون أسماء العناصر طويلة أو مُعرَّبة، يحدّد المُنشئ الثاني لـ `DiscreteGroupItem` العناصر حسب الفهرس. الفهارس هي مواضع العناصر المرقّمة من الصفر في ترتيب ظهورها في بيانات المصدر، لا حسب الترتيب الأبجدي. في بيانات العينة أعلاه، يمثل `grape` العنصر رقم 0، و`carrot` العنصر رقم 1، و`potato` العنصر رقم 2، و`cherry` العنصر رقم 3؛ لذا يكون `fruit` هو `{ 0, 3 }` و`vegetable` هو `{ 1, 2 }`. والنتيجة مطابقة لمثال التجميع حسب الأسماء.

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
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            const {
                Workbook,
                SaveFormat,
                DiscreteGroupItem,
                PivotFieldGroupOptions
            } = AsposeCells;
            console.log("Aspose.Cells initialized");
            document.getElementById('runExample').addEventListener('click', async () => {
                const workbook = new Workbook();
                const sheet = workbook.worksheets.get(0);
                const cells = sheet.cells;
                cells.get(0, 0).value = "product";
                cells.get(1, 0).value = "grape";
                cells.get(2, 0).value = "carrot";
                cells.get(3, 0).value = "potato";
                cells.get(4, 0).value = "cherry";
                const dateStyle = workbook.createStyle();
                dateStyle.custom = "m/d/yyyy";
                cells.get(0, 1).value = "date";
                cells.get(1, 1).value = new Date(2021, 1, 5);
                cells.get(2, 1).value = new Date(2022, 2, 8);
                cells.get(3, 1).value = new Date(2023, 3, 10);
                cells.get(4, 1).value = new Date(2024, 4, 16);
                for (let r = 1; r <= 4; r++) {
                    cells.get(r, 1).style = dateStyle;
                }
                cells.get(0, 2).value = "amount";
                cells.get(1, 2).value = 50;
                cells.get(2, 2).value = 60;
                cells.get(3, 2).value = 70;
                cells.get(4, 2).value = 80;
                // Add a pivot table with the destination cell A12 (row 11, column 0)
                const pivotTable = sheet.pivotTables.add("=Sheet1!A1:C5", 11, 0);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "product");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "date");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "amount");
                pivotTable.pivotTableStyleType = AsposeCells.PivotTableStyleType.PivotTableStyleMedium10;
                // grape is item 0, carrot is item 1, potato is item 2, cherry is item 3
                // (zero-based positions in the order the items appear in the source data)
                const fruit = new DiscreteGroupItem("fruit", [0, 3]);
                const vegetable = new DiscreteGroupItem("vegetable", [1, 2]);
                const groupOptions = new PivotFieldGroupOptions();
                groupOptions.discreteGroupItems = [fruit, vegetable];
                pivotTable.rowFields.get(0).group(groupOptions);
                pivotTable.calculateData();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "outputDiscreteGroupPivotFieldByIndex.xlsx";
                downloadLink.style.display = "block";
                document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        });
    </script>
</html>
```

## **ملاحظة**

{{% alert color="primary" %}}
- لا تُفقد العناصر التي لم تُسنَد إلى أي مجموعة مخصصة. وتظل في الجدول المحوري على المستوى نفسه الذي توجد عليه المجموعات المخصصة، في صورة إدخالات مستقلة، كل واحدة منها لعنصر واحد. في المثال أعلاه، يؤدي تعريف المجموعة `fruit` فقط إلى بقاء `carrot` و`potato` في منطقة الصفوف كإدخالات مستقلة إلى جانب مجموعة `fruit`.
- تتحكم الخاصية `PivotFieldGroupOptions.newPivotField` في تخطيط التجميع المتقطع. قيمتها الافتراضية هي `true`، وهي تضيف الحقل المُجمَّع كحقل خارجي جديد بجوار الحقل الأصلي، لإنتاج تخطيط المستويين الموضح أعلاه (مع زيادة عدد الحقول في `rowFields` إلى 2). اضبطها على `false` لاستبدال الحقل الأصلي بدلاً من ذلك، فتعرض منطقة الصفوف عندئذٍ مستوى واحدًا يتضمن أسماء المجموعات وقيمها المجمّعة فقط: `fruit` 130 (50 + 80) و`vegetable` 130 (60 + 70).
- يمكن استخدام مُنشئ `DiscreteGroupItem` القائم على الاسم والمُنشئ القائم على الفهرس معًا في المصفوفة `discreteGroupItems` نفسها.
{{% /alert %}}

## **مقالات ذات صلة**
- [تجميع الحقول في الجدول المحوري](/cells/ar/javascript-cpp/group-pivot-fields-in-the-pivot-table/)
- [إضافة حقول الصفوف والأعمدة إلى الجدول المحوري](/cells/ar/javascript-cpp/pivot-table-add-row-and-column-fields/)
- [تصفية الجداول المحورية حسب التسمية أو القيمة](/cells/ar/javascript-cpp/filter-by-label-or-value-of-pivot-table/)
- [تطبيق نمط على الجدول المحوري](/cells/ar/javascript-cpp/apply-style-to-pivot-table/)
- [تحديث الجدول المحوري](/cells/ar/javascript-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}
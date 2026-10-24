---
title: تعديل تخطيط حقول الصفحة في الجدول المحوري
linktitle: تعديل تخطيط حقول الصفحة في الجدول المحوري
description: تعلّم كيفية التحكم في تخطيط منطقة حقول الصفحة في جدول محوري باستخدام Aspose.Cells for Node.js عبر C++، بما في ذلك تعيين ترتيب العرض وعدد حقول الصفحة قبل الالتفاف وترتيب حقول الصفحة في أعلى الجدول المحوري.
keywords: Aspose.Cells, مكتبة Node.js عبر C++, جدول بيانات, جدول محوري, حقل صفحة, ترتيب حقول الصفحة, عدد الالتفاف لحقول الصفحة, نقل حقل الصفحة
type: docs
weight: 191
url: /ar/nodejs-cpp/change-page-field-layout/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
هذه المقالة متابعة لموضوع **إضافة حقل صفحة إلى جدول محوري**. وتوضح كيفية التحكم في تخطيط منطقة حقول الصفحة — شريط عناصر التحكم في الترشيح الموجود أعلى الجدول المحوري — بما في ذلك ترتيب العرض وعدد الالتفاف وإعادة ترتيب الحقول.
{{% /alert %}}

## **Introduction**
يوفر الجدول المحوري في Microsoft Excel منطقة مخصصة **لحقول الصفحة** تقع أعلى منطقة الصفوف والأعمدة والبيانات في الجدول. تُعرض هذه المنطقة كشريط من عناصر التحكم المنسدلة للتصفية (عنصر واحد لكل حقل صفحة)، وهو ما ينقر عليه المستخدمون النهائيون لتقطيع الجدول المحوري وفق معايير مثل السنة أو المنطقة. يمثل Aspose.Cells for Node.js عبر C++ هذه المنطقة من خلال المجموعة `pivotTable.pageFields`، ويوفر ثلاث خصائص تتحكم في التخطيط البصري للشريط:
- `pivotTable.pageFieldOrder` (قيمة من نوع `Aspose.Cells.PrintOrderType`) تحدد ما إذا كانت حقول الصفحة الإضافية توضع *بجانب* الحقول الحالية أو *أسفلها*.
- `pivotTable.pageFieldWrapCount` تحدد عدد حقول الصفحة الموضوعة في كل صف أو عمود قبل الانتقال إلى السطر أو العمود التالي.
- `pivotTable.pageFields.move(currIndex, destIndex)` تعيد ترتيب حقول الصفحة دون تغيير وضع الترتيب.
تشرح هذه المقالة ثلاثة أمثلة برمجية توضح كل عملية من هذه العمليات باستخدام مجموعة بيانات مشتركة، حتى تتمكن من مقارنة التخطيطات الناتجة جنبًا إلى جنب.

## **Source Data**
| الفاكهة | السنة | المنطقة | المبلغ |
|--------|------|--------|--------|
| تفاح | 2022 | الشمال | 150 |
| تفاح | 2023 | الشمال | 180 |
| موز | 2022 | الجنوب | 120 |
| موز | 2023 | الجنوب | 140 |
| كرز | 2022 | الشرق | 200 |
| كرز | 2023 | الشرق | 220 |
| عنب | 2022 | الغرب | 90 |
| عنب | 2023 | الغرب | 110 |
يحتوي كل مثال برمجي على الصفوف الثمانية نفسها بترتيب متطابق، وبما أن بيانات المصدر لا تختلف بين السيناريوهات، فلا تتغير سوى خصائص تخطيط حقول الصفحة.

## **Example 1: Over Then Down**
في السيناريو الأول، نهيئ حقلي الصفحة (`Year` و`Region`) ليظهروا **جنبًا إلى جنب في صف واحد** أعلى الجدول المحوري. نعين `Fruit` على محور الصفوف، ونضع `Year` أولاً و`Region` ثانيًا على محور الصفحة (يحدد ترتيب استدعاءات `addFieldToArea` فهرس البداية)، ونضيف `Amount` (`Sum`) كحقل للبيانات، ثم نعين `pageFieldOrder` على `PrintOrderType.OverThenDown` مع `pageFieldWrapCount = 2`. مع `OverThenDown` وعدد التفاف `2`، يوضع حقلا الصفحة أفقيًا جنبًا إلى جنب في صف واحد أعلى الجدول المحوري، لذلك يشغل الشريط صفًا واحدًا بعرض حقلين.

```javascript
const AsposeCells = require("aspose.cells.node");
const fs = require("fs");
const path = require("path");
let dataDir = "output";
if (!fs.existsSync(dataDir)) {
    fs.mkdirSync(dataDir, { recursive: true });
}
let workbook = new AsposeCells.Workbook();
let worksheets = workbook.getWorksheets();
let pivotDataIdx = worksheets.add("PivotData");
let pivotDataSheet = worksheets.get(pivotDataIdx);
let pivotDataCells = pivotDataSheet.getCells();
// Headers (row 0)
pivotDataCells.get(0, 0).putValue("Fruit");
pivotDataCells.get(0, 1).putValue("Year");
pivotDataCells.get(0, 2).putValue("Region");
pivotDataCells.get(0, 3).putValue("Amount");
// Row 1: Apple, 2022, North, 150
pivotDataCells.get(1, 0).putValue("Apple");
pivotDataCells.get(1, 1).putValue(2022);
pivotDataCells.get(1, 2).putValue("North");
pivotDataCells.get(1, 3).putValue(150);
// Row 2: Apple, 2023, North, 180
pivotDataCells.get(2, 0).putValue("Apple");
pivotDataCells.get(2, 1).putValue(2023);
pivotDataCells.get(2, 2).putValue("North");
pivotDataCells.get(2, 3).putValue(180);
// Row 3: Banana, 2022, South, 120
pivotDataCells.get(3, 0).putValue("Banana");
pivotDataCells.get(3, 1).putValue(2022);
pivotDataCells.get(3, 2).putValue("South");
pivotDataCells.get(3, 3).putValue(120);
// Row 4: Banana, 2023, South, 140
pivotDataCells.get(4, 0).putValue("Banana");
pivotDataCells.get(4, 1).putValue(2023);
pivotDataCells.get(4, 2).putValue("South");
pivotDataCells.get(4, 3).putValue(140);
// Row 5: Cherry, 2022, East, 200
pivotDataCells.get(5, 0).putValue("Cherry");
pivotDataCells.get(5, 1).putValue(2022);
pivotDataCells.get(5, 2).putValue("East");
pivotDataCells.get(5, 3).putValue(200);
// Row 6: Cherry, 2023, East, 220
pivotDataCells.get(6, 0).putValue("Cherry");
pivotDataCells.get(6, 1).putValue(2023);
pivotDataCells.get(6, 2).putValue("East");
pivotDataCells.get(6, 3).putValue(220);
// Row 7: Grape, 2022, West, 90
pivotDataCells.get(7, 0).putValue("Grape");
pivotDataCells.get(7, 1).putValue(2022);
pivotDataCells.get(7, 2).putValue("West");
pivotDataCells.get(7, 3).putValue(90);
// Row 8: Grape, 2023, West, 110
pivotDataCells.get(8, 0).putValue("Grape");
pivotDataCells.get(8, 1).putValue(2023);
pivotDataCells.get(8, 2).putValue("West");
pivotDataCells.get(8, 3).putValue(110);
// Add PivotTableReport sheet
let pivotTableSheetIdx = worksheets.add("PivotTableReport");
let pivotTableSheet = worksheets.get(pivotTableSheetIdx);
let pivotTables = pivotTableSheet.getPivotTables();
// Create pivot table sourced from PivotData!A1:D9 placed at A1 on PivotTableReport
let pivotIndex = pivotTables.add("PivotData!A1:D9", "A1", "PivotTable1");
let pivotTable = pivotTables.get(pivotIndex);
// Add fields
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);   // Fruit
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);  // Year
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);  // Region
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);  // Amount
pivotTable.getDataFields().get(0).setFunction(AsposeCells.ConsolidationFunction.Sum);
// Configure page field area layout: place page fields across first, wrap after every 2
pivotTable.setPageFieldOrder(AsposeCells.PrintOrderType.OverThenDown);
pivotTable.setPageFieldWrapCount(2);
// Refresh and calculate
pivotTable.calculateData();
// Save
workbook.save(path.join(dataDir, "pageFieldLayout_overThenDown.xlsx"));
```

## **Example 2: Down Then Over**
في هذا المثال، نضع `Fruit` على محور الصفوف، و`Year` و`Region` على محور الصفحة (مع وضع `Year` أولاً)، و`Amount` مع `Sum` كحقل للبيانات — تمامًا كما في المثال 1. ثم نعين `pageFieldOrder` على `PrintOrderType.DownThenOver` و`pageFieldWrapCount` على `2`. مع `DownThenOver` وعدد الالتفاف `2`، يُكدَّس حقلا الصفحة رأسيًا — `Year` في الأعلى و`Region` تحته مباشرة — مكونين عمودًا واحدًا أعلى الجدول المحوري. لذلك يشغل الشريط صفين بعرض حقل واحد، على عكس المثال 1.

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook();
const pivotData = workbook.getWorksheets().get(0);
pivotData.setName("PivotData");
const pivotReportIdx = workbook.getWorksheets().add("PivotTableReport");
const pivotReport = workbook.getWorksheets().get(pivotReportIdx);
const headers = ["Fruit", "Year", "Region", "Amount"];
for (let c = 0; c < headers.length; c++) {
    pivotData.getCells().get(0, c).putValue(headers[c]);
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
        pivotData.getCells().get(r + 1, c).putValue(data[r][c]);
    }
}
const idx = pivotReport.getPivotTables().add("PivotData!A1:D9", "A1", "PivotTable");
const pivotTable = pivotReport.getPivotTables().get(idx);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);
pivotTable.setPageFieldOrder(AsposeCells.PrintOrderType.DownThenOver);
pivotTable.setPageFieldWrapCount(2);
pivotTable.calculateData();
workbook.save("pageFieldLayout_downThenOver.xlsx");
```

## **Example 3: Move a Page Field**
في السيناريو الثالث، نُبقي مجموعة البيانات وتوزيع الحقول كما هما، ونضبط تخطيطًا محايدًا (`OverThenDown` مع عدد الالتفاف `2`)، ثم نوضح عملية `pageFields.move`. ينقل الاستدعاء `move(0, 1)` حقل الصفحة الموجود عند الفهرس 0 (`Year`) إلى الموضع 1، وينتقل حقل الصفحة الذي كان في الموضع 1 (`Region`) إلى الموضع 0. بعد هذا الاستدعاء، يصبح `Region` أول حقول الصفحة ويصبح `Year` ثانيها. يبقى الالتفاف ووضع الترتيب دون تغيير، لذلك يظل الشريط معروضًا أفقيًا جنبًا إلى جنب — ولا يتغير سوى ترتيب القائمتين المنسدلتين.

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook();
const dataSheet = workbook.getWorksheets().get(0);
dataSheet.setName("PivotData");
dataSheet.getCells().get("A1").putValue("Fruit");
dataSheet.getCells().get("B1").putValue("Year");
dataSheet.getCells().get("C1").putValue("Region");
dataSheet.getCells().get("D1").putValue("Amount");
dataSheet.getCells().get("A2").putValue("Apple");
dataSheet.getCells().get("B2").putValue(2022);
dataSheet.getCells().get("C2").putValue("North");
dataSheet.getCells().get("D2").putValue(150);
dataSheet.getCells().get("A3").putValue("Apple");
dataSheet.getCells().get("B3").putValue(2023);
dataSheet.getCells().get("C3").putValue("North");
dataSheet.getCells().get("D3").putValue(180);
dataSheet.getCells().get("A4").putValue("Banana");
dataSheet.getCells().get("B4").putValue(2022);
dataSheet.getCells().get("C4").putValue("South");
dataSheet.getCells().get("D4").putValue(120);
dataSheet.getCells().get("A5").putValue("Banana");
dataSheet.getCells().get("B5").putValue(2023);
dataSheet.getCells().get("C5").putValue("South");
dataSheet.getCells().get("D5").putValue(140);
dataSheet.getCells().get("A6").putValue("Cherry");
dataSheet.getCells().get("B6").putValue(2022);
dataSheet.getCells().get("C6").putValue("East");
dataSheet.getCells().get("D6").putValue(200);
dataSheet.getCells().get("A7").putValue("Cherry");
dataSheet.getCells().get("B7").putValue(2023);
dataSheet.getCells().get("C7").putValue("East");
dataSheet.getCells().get("D7").putValue(220);
dataSheet.getCells().get("A8").putValue("Grape");
dataSheet.getCells().get("B8").putValue(2022);
dataSheet.getCells().get("C8").putValue("West");
dataSheet.getCells().get("D8").putValue(90);
dataSheet.getCells().get("A9").putValue("Grape");
dataSheet.getCells().get("B9").putValue(2023);
dataSheet.getCells().get("C9").putValue("West");
dataSheet.getCells().get("D9").putValue(110);
const pivotSheetIdx = workbook.getWorksheets().add("PivotTableReport");
const pivotSheet = workbook.getWorksheets().get(pivotSheetIdx);
const pivotIdx = pivotSheet.getPivotTables().add("PivotData!A1:D9", "A3", "PivotTable");
const pivotTable = pivotSheet.getPivotTables().get(pivotIdx);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);
pivotTable.setPageFieldOrder(AsposeCells.PrintOrderType.OverThenDown);
pivotTable.setPageFieldWrapCount(2);
pivotTable.getPageFields().move(0, 1);
pivotTable.calculateData();
workbook.save("pageFieldLayout_move.xlsx");
```

## **Related Articles**
- [إضافة حقل صفحة إلى جدول محوري](/cells/ar/nodejs-cpp/add-page-field-in-pivot-table/) — الصفحة الأصلية التي توضح كيفية إضافة حقول الصفحة إلى جدول محوري.
- [حقول الصفوف والأعمدة في الجدول المحوري](/cells/ar/nodejs-cpp/row-and-column-fields/) — تغطي كيفية تخصيص الحقول لمحوري الصفوف والأعمدة، وهي *مكملة* للعمل الذي يظهر هنا على محور الصفحة.
- [إدارة حقول القيم في الجدول المحوري](/cells/ar/nodejs-cpp/manage-value-fields/) — تصف كيفية تخصيص منطقة البيانات (القيم)، بما في ذلك تجميع `Sum` المستخدم في هذه المقالة.
- [تحديث الجدول المحوري](/cells/ar/nodejs-cpp/refresh-pivot-table/) — تشرح `refreshData` و`calculateData`، اللذين يلزمان بعد إعادة ترتيب حقول الصفحة.
- [تطبيق نمط على الجدول المحوري](/cells/ar/nodejs-cpp/apply-style-to-pivot-table/) — توضح كيفية تنسيق الجدول المحوري بعد ضبط تخطيط شريط حقول الصفحة.

{{< app/cells/assistant language="nodejs-cpp" >}}
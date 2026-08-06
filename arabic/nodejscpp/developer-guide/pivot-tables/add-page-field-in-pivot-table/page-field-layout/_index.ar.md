---
title: تعديل تخطيط حقل الصفحة في الجدول المحوري
linktitle: تعديل تخطيط حقل الصفحة في الجدول المحوري
description: تعلّم كيفية التحكم في تخطيط منطقة حقل الصفحة في الجدول المحوري باستخدام Aspose.Cells for Node.js via C++، بما في ذلك تعيين ترتيب العرض وعدد الالتفاف وترتيب الحقول لحقول الصفحة في الجزء العلوي من الجدول المحوري.
keywords: Aspose.Cells, Node.js via C++ library, spreadsheet, pivot table, page field, page field order, page field wrap count, move page field
type: docs
weight: 191
url: /ar/nodejs-cpp/change-page-field-layout/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
هذه المقالة هي تتمة لموضوع **إضافة حقل صفحة في الجدول المحوري**. توضح كيفية التحكم في تخطيط منطقة حقل الصفحة — وهي شريط عناصر تحكم التصفية الموجود أعلى الجدول المحوري — بما في ذلك ترتيب العرض وعدد الالتفاف وإعادة ترتيب الحقول.
{{% /alert %}}
## **المقدمة**
يُظهر الجدول المحوري في Microsoft Excel **منطقة حقل صفحة** مخصصة تقع أعلى جسم الصفوف/الأعمدة/البيانات في الجدول. تُعرض هذه المنطقة على شكل شريط من عناصر تحكم التصفية المنسدلة (عنصر واحد لكل حقل صفحة)، وهي التي ينقر عليها المستخدمون لتقسيم الجدول المحوري وفق معايير مثل السنة أو المنطقة. يُمثّل Aspose.Cells for Node.js via C++ هذه المنطقة من خلال مجموعة `pivotTable.pageFields` ويُتيح ثلاث خصائص تتحكم في كيفية عرض الشريط بصريًا:
- `pivotTable.pageFieldOrder` (قيمة من النوع `Aspose.Cells.PrintOrderType`) يحدد ما إذا كانت حقول الصفحة الإضافية ستوضع *بجانب* الحقول الحالية أم *أسفلها*.
- `pivotTable.pageFieldWrapCount` يحدد عدد حقول الصفحة الموضوعة في كل صف أو عمود قبل الالتفاف.
- `pivotTable.pageFields.move(currIndex, destIndex)` يعيد ترتيب حقول الصفحة دون تغيير نمط الترتيب.
تستعرض هذه المقالة ثلاثة أمثلة برمجية توضح كل عملية من هذه العمليات على مجموعة بيانات مشتركة، حتى تتمكن من مقارنة التخطيطات الناتجة جنبًا إلى جنب.
## **البيانات المصدر**
تحمّل جميع الأمثلة الثلاثة أدناه صفوف بيانات المبيعات الثمانية هذه في ورقة عمل باسم `PivotData`. تحتوي البيانات على مرشحين لحقول الصفحة (`Year` و`Region`)، ومرشحًا واحدًا لحقل الصف (`Fruit`)، ومقياسًا واحدًا (`Amount`)، مما يجعل فحص شريط حقل الصفحة ذا معنى.
يتم تعبئة جميع الصفوف الثمانية في كل مثال برمجي، وبنفس الترتيب، بحيث لا تختلف البيانات المصدر بين السيناريوهات — بل تختلف فقط خصائص تخطيط حقل الصفحة.
## **المثال 1: أفقي ثم عمودي**
في السيناريو الأول، نُكوّن حقلَي الصفحة (`Year` و`Region`) بحيث يظهران **جنبًا إلى جنب في صف واحد** في الجزء العلوي من الجدول المحوري. نخصص `Fruit` لمحور الصف، ونضع `Year` أولاً ثم `Region` ثانيًا على محور الصفحة (يحدد ترتيب استدعاءات `addFieldToArea` الفهرس الابتدائي)، ونضيف `Amount` (Sum) كحقل بيانات، ثم نضبط `pageFieldOrder` على `PrintOrderType.OverThenDown` مع `pageFieldWrapCount = 2`. مع `OverThenDown` وعدد التفاف يساوي 2، يُعرض حقلَا الصفحة أفقيًا جنبًا إلى جنب في صف واحد أعلى الجدول المحوري، وبالتالي يشغل الشريط صفًا واحدًا بعرض اثنين.
```javascript
let dataDir = "output";
if (!fs.existsSync(dataDir)) {
    fs.mkdirSync(dataDir, { recursive: true });
}

let workbook = new AsposeCells.Workbook();
let worksheets = workbook.getWorksheets();

let pivotDataIdx = worksheets.add("PivotData");
let pivotDataSheet = worksheets.get(pivotDataIdx);
let pivotDataCells = pivotDataSheet.getCells();

// العناوين (الصف 0)
pivotDataCells.get(0, 0).putValue("Fruit");
pivotDataCells.get(0, 1).putValue("Year");
pivotDataCells.get(0, 2).putValue("Region");
pivotDataCells.get(0, 3).putValue("Amount");

// الصف 1: تفاح، 2022، شمال، 150
pivotDataCells.get(1, 0).putValue("Apple");
pivotDataCells.get(1, 1).putValue(2022);
pivotDataCells.get(1, 2).putValue("North");
pivotDataCells.get(1, 3).putValue(150);

// الصف 2: تفاح، 2023، شمال، 180
pivotDataCells.get(2, 0).putValue("Apple");
pivotDataCells.get(2, 1).putValue(2023);
pivotDataCells.get(2, 2).putValue("North");
pivotDataCells.get(2, 3).putValue(180);

// الصف 3: موز، 2022، جنوب، 120
pivotDataCells.get(3, 0).putValue("Banana");
pivotDataCells.get(3, 1).putValue(2022);
pivotDataCells.get(3, 2).putValue("South");
pivotDataCells.get(3, 3).putValue(120);

// الصف 4: موز، 2023، جنوب، 140
pivotDataCells.get(4, 0).putValue("Banana");
pivotDataCells.get(4, 1).putValue(2023);
pivotDataCells.get(4, 2).putValue("South");
pivotDataCells.get(4, 3).putValue(140);

// الصف 5: كرز، 2022، شرق، 200
pivotDataCells.get(5, 0).putValue("Cherry");
pivotDataCells.get(5, 1).putValue(2022);
pivotDataCells.get(5, 2).putValue("East");
pivotDataCells.get(5, 3).putValue(200);

// الصف 6: كرز، 2023، شرق، 220
pivotDataCells.get(6, 0).putValue("Cherry");
pivotDataCells.get(6, 1).putValue(2023);
pivotDataCells.get(6, 2).putValue("East");
pivotDataCells.get(6, 3).putValue(220);

// الصف 7: عنب، 2022، غرب، 90
pivotDataCells.get(7, 0).putValue("Grape");
pivotDataCells.get(7, 1).putValue(2022);
pivotDataCells.get(7, 2).putValue("West");
pivotDataCells.get(7, 3).putValue(90);

// الصف 8: عنب، 2023، غرب، 110
pivotDataCells.get(8, 0).putValue("Grape");
pivotDataCells.get(8, 1).putValue(2023);
pivotDataCells.get(8, 2).putValue("West");
pivotDataCells.get(8, 3).putValue(110);

// إضافة ورقة تقرير الجدول المحوري
let pivotTableSheetIdx = worksheets.add("PivotTableReport");
let pivotTableSheet = worksheets.get(pivotTableSheetIdx);
let pivotTables = pivotTableSheet.getPivotTables();

// إنشاء جدول محوري مصدره PivotData!A1:D9 موضوع في A1 على PivotTableReport
let pivotIndex = pivotTables.add("PivotData!A1:D9", "A1", "PivotTable1");
let pivotTable = pivotTables.get(pivotIndex);

// إضافة الحقول
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);   // فاكهة
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);  // سنة
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);  // منطقة
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);  // المبلغ
pivotTable.getDataFields().get(0).setFunction(AsposeCells.ConsolidationFunction.Sum);

// تكوين تخطيط منطقة حقل الصفحة: ضع حقول الصفحة عبر الأفق أولاً، التفاف بعد كل 2
pivotTable.setPageFieldOrder(AsposeCells.PrintOrderType.OverThenDown);
pivotTable.setPageFieldWrapCount(2);

// تحديث وحساب
pivotTable.calculateData();

// حفظ
workbook.save(path.join(dataDir, "pageFieldLayout_overThenDown.xlsx"));
```
## **المثال 2: عمودي ثم أفقي**
في هذا المثال نضع `Fruit` على محور الصف، و`Year` و`Region` على محور الصفحة (مع `Year` أولاً)، و`Amount` (Sum) كحقل بيانات — تمامًا كما في المثال 1. ثم نضبط `pageFieldOrder` على `PrintOrderType.DownThenOver` و`pageFieldWrapCount` على `2`. مع `DownThenOver` وعدد التفاف يساوي 2، يُرَصّ حقلَا الصفحة عموديًا — `Year` في الأعلى، و`Region` تحته مباشرةً — مُشكّلَيْن عمودًا واحدًا أعلى الجدول المحوري. وبالتالي يشغل الشريط صفين بعرض واحد، على عكس المثال 1.
```javascript
const AsposeCells = require("aspose.cells");

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

pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, 0);
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Page, 1);
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Page, 2);
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, 3);

pivotTable.setPageFieldOrder(AsposeCells.PrintOrderType.DownThenOver);
pivotTable.setPageFieldWrapCount(2);

pivotTable.calculateData();

workbook.save("pageFieldLayout_downThenOver.xlsx");
```
## **المثال 3: نقل حقل صفحة**
في السيناريو الثالث، نحتفظ بمجموعة البيانات وتخصيص الحقول نفسه، ونضبط تخطيطًا محايدًا (`OverThenDown` مع عدد التفاف `2`)، ثم نوضح عملية `pageFields.move`. ينقل استدعاء `move(0, 1)` حقل الصفحة في الفهرس 0 (`Year`) إلى الموضع 1، وينتقل حقل الصفحة الذي كان في الموضع 1 (`Region`) إلى الموضع 0. بعد هذا الاستدعاء، يصبح `Region` هو حقل الصفحة الأول ويصبح `Year` هو الثاني. يظل نمط الالتفاف والترتيب دون تغيير، لذا يُعرض الشريط أفقيًا جنبًا إلى جنب — لم يتغير سوى ترتيب القائمتَين المنسدلتَين.
```javascript
const AsposeCells = require("aspose.cells");

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
## **مقالات ذات صلة**
- [إضافة حقل صفحة في الجدول المحوري](/cells/ar/nodejs-cpp/add-page-field-in-pivot-table/) — الصفحة الأصلية التي تشرح كيفية إضافة حقول الصفحة إلى الجدول المحوري.
- [حقول الصفوف والأعمدة في الجدول المحوري](/cells/ar/nodejs-cpp/row-and-column-fields/) — يتناول تخصيص الحقول لمحوري الصفوف والأعمدة، ويُكمل العمل على محور الصفحة الموضح هنا.
- [إدارة حقول القيم في الجدول المحوري](/cells/ar/nodejs-cpp/manage-value-fields/) — يوضح كيفية تكوين منطقة البيانات (القيم)، بما في ذلك تجميع `Sum` المستخدم في هذه المقالة.
- [تحديث الجدول المحوري](/cells/ar/nodejs-cpp/refresh-pivot-table/) — يوضح `refreshData` و`calculateData`، المطلوبَين بعد إعادة ترتيب حقول الصفحة.
- [تطبيق نمط على الجدول المحوري](/cells/ar/nodejs-cpp/apply-style-to-pivot-table/) — يوضح كيفية تنسيق الجدول المحوري بعد الانتهاء من تخطيط شريط حقل الصفحة.
{{< app/cells/assistant language="nodejs-cpp" >}}
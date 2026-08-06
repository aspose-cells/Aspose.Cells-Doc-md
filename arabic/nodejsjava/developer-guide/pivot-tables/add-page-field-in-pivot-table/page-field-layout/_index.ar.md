---
title: تعديل تخطيط حقل الصفحة في الجدول المحوري
linktitle: تعديل تخطيط حقل الصفحة في الجدول المحوري
description: تعرف على كيفية التحكم في تخطيط منطقة حقل الصفحة في جدول محوري باستخدام Aspose.Cells for Node.js via Java، بما في ذلك تعيين ترتيب العرض وعدد الالتفاف وترتيب الحقول لحقول الصفحة في أعلى الجدول المحوري.
keywords: Aspose.Cells, Node.js via Java library, spreadsheet, pivot table, page field, page field order, page field wrap count, move page field
type: docs
weight: 191
url: /ar/nodejs-java/change-page-field-layout/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
هذه المقالة هي تتمة لموضوع **إضافة حقل الصفحة في الجدول المحوري**. توضح كيفية التحكم في تخطيط منطقة حقل الصفحة — وهي شريط عناصر التحكم بالفلاتر الموجود في أعلى الجدول المحوري — بما في ذلك ترتيب العرض وعدد الالتفاف وإعادة ترتيب الحقول.
{{% /alert %}}
## **مقدمة**
يكشف الجدول المحوري في Microsoft Excel عن **منطقة حقل صفحة** مخصصة تقع فوق جسم الصفوف/الأعمدة/البيانات في الجدول. تُعرض هذه المنطقة كشريط من عناصر التحكم بالفلاتر المنسدلة (واحد لكل حقل صفحة) وهو ما ينقر عليه المستخدمون لتقسيم الجدول المحوري حسب معايير مثل السنة أو المنطقة. يقوم Aspose.Cells بنمذجة هذه المنطقة من خلال مجموعة `PivotTable.PageFields` ويعرض ثلاث خصائص تتحكم في كيفية عرض الشريط بصريًا:
- `PivotTable.PageFieldOrder` (قيمة من نوع `Aspose.Cells.PrintOrderType`) يحدد ما إذا كانت حقول الصفحة الإضافية توضع *بجانب* الحقول الموجودة أو *أسفل* منها.
- `PivotTable.PageFieldWrapCount` يحدد عدد حقول الصفحة التي توضع في كل صف أو عمود قبل الالتفاف.
- `PivotTable.PageFields.Move(currIndex, destIndex)` يعيد ترتيب حقول الصفحة دون تغيير وضع الترتيب.
تستعرض هذه المقالة ثلاثة أمثلة على التعليمات البرمجية توضح كل عملية من هذه العمليات على مجموعة بيانات مشتركة، حتى تتمكن من مقارنة التخطيطات الناتجة جنبًا إلى جنب.
## **البيانات المصدر**
تحمّل جميع الأمثلة الثلاثة أدناه هذه الصفوف الثمانية من بيانات المبيعات في ورقة عمل باسم `PivotData`. تحتوي البيانات على مرشحين لحقول الصفحة (`Year` و`Region`)، ومرشح حقل صف واحد (`Fruit`)، ومقياس واحد (`Amount`)، مما يجعل شريط حقل الصفحة ذي فائدة للفحص.
يتم ملء جميع الصفوف الثمانية في كل مثال من أمثلة التعليمات البرمجية، بنفس الترتيب، لذا لا تختلف البيانات المصدر بين السيناريوهات — فقط خصائص تخطيط حقل الصفحة هي التي تختلف.
## **المثال 1: من اليسار إلى اليمين ثم للأسفل (Over Then Down)**
في السيناريو الأول نكوّن حقلي الصفحة (`Year` و`Region`) ليظهروا **جنبًا إلى جنب في صف واحد** في أعلى الجدول المحوري. نخصص `Fruit` لمحور الصفوف، ونضع `Year` أولاً و`Region` ثانيًا على محور الصفحة (يحدد ترتيب استدعاءات `addFieldToArea` الفهرس الابتدائي)، ونضيف `Amount` (Sum) كحقل بيانات، ثم نضبط `PageFieldOrder` على `PrintOrderType.OVER_THEN_DOWN` مع `PageFieldWrapCount = 2`. مع `OVER_THEN_DOWN` وعدد التفاف 2، يتم تخطيط حقلي الصفحة أفقيًا جنبًا إلى جنب في صف واحد في أعلى الجدول المحوري، لذا يشغل الشريط صفًا واحدًا بعرض اثنين.
```javascript
let dataDir = "output";
if (!fs.existsSync(dataDir)) fs.mkdirSync(dataDir, { recursive: true });

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

// إضافة ورقة PivotTableReport
let pivotTableSheetIdx = worksheets.add("PivotTableReport");
let pivotTableSheet = worksheets.get(pivotTableSheetIdx);
let pivotTables = pivotTableSheet.getPivotTables();

// إنشاء جدول محوري مصدره PivotData!A1:D9 موضوع في A1 على PivotTableReport
let pivotIndex = pivotTables.add("PivotData!A1:D9", "A1", "PivotTable1");
let pivotTable = pivotTables.get(pivotIndex);

// إضافة الحقول
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);   // الفاكهة
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);  // السنة
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);  // المنطقة
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);  // المبلغ
pivotTable.getDataFields().get(0).setFunction(AsposeCells.ConsolidationFunction.Sum);

// تكوين تخطيط منطقة حقل الصفحة: ضع حقول الصفحة أفقيًا أولاً، واللف بعد كل 2
pivotTable.setPageFieldOrder(AsposeCells.PrintOrderType.OverThenDown);
pivotTable.setPageFieldWrapCount(2);

// التحديث والحساب
pivotTable.calculateData();

// حفظ
workbook.save(path.join(dataDir, "pageFieldLayout_overThenDown.xlsx"));
```
## **المثال 2: من الأعلى إلى الأسفل ثم لليمين (Down Then Over)**
في هذا المثال نضع `Fruit` على محور الصفوف، و`Year` و`Region` على محور الصفحة (مع `Year` أولاً)، و`Amount` (Sum) كحقل بيانات — تمامًا كما في المثال 1. ثم نضبط `PageFieldOrder` على `PrintOrderType.DOWN_THEN_OVER` و`PageFieldWrapCount` على `2`. مع `DOWN_THEN_OVER` وعدد التفاف 2، يتم تكديس حقلي الصفحة عموديًا — `Year` في الأعلى، و`Region` تحته مباشرة — مما يشكل عمودًا واحدًا في أعلى الجدول المحوري. لذلك يشغل الشريط صفين بعرض واحد، على عكس المثال 1.
```javascript
var workbook = new AsposeCells.Workbook();
var pivotData = workbook.getWorksheets().get(0);
pivotData.setName("PivotData");
var pivotReportIdx = workbook.getWorksheets().add("PivotTableReport");
var pivotReport = workbook.getWorksheets().get(pivotReportIdx);

var headers = ["Fruit", "Year", "Region", "Amount"];
for (var c = 0; c < headers.length; c++)
{
    pivotData.getCells().get(0, c).putValue(headers[c]);
}

var data = [
    ["Apple", 2022, "North", 150],
    ["Apple", 2023, "North", 180],
    ["Banana", 2022, "South", 120],
    ["Banana", 2023, "South", 140],
    ["Cherry", 2022, "East", 200],
    ["Cherry", 2023, "East", 220],
    ["Grape", 2022, "West", 90],
    ["Grape", 2023, "West", 110]
];

for (var r = 0; r < data.length; r++)
{
    for (var c = 0; c < data[r].length; c++)
    {
        pivotData.getCells().get(r + 1, c).putValue(data[r][c]);
    }
}

var idx = pivotReport.getPivotTables().add("PivotData!A1:D9", "A1", "PivotTable");
var pivotTable = pivotReport.getPivotTables().get(idx);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);

pivotTable.setPageFieldOrder(AsposeCells.PrintOrderType.DownThenOver);
pivotTable.setPageFieldWrapCount(2);

pivotTable.calculateData();

workbook.save("pageFieldLayout_downThenOver.xlsx");
```
## **المثال 3: نقل حقل صفحة**
في السيناريو الثالث نحتفظ بمجموعة البيانات وتخصيص الحقول هذا، ونضبط تخطيطًا محايدًا (`OVER_THEN_DOWN` مع عدد التفاف `2`)، ثم نوضح عملية `PageFields.Move`. ينقل استدعاء `Move(0, 1)` حقل الصفحة في الفهرس 0 (`Year`) إلى الموضع 1، وينتقل حقل الصفحة الذي كان في الموضع 1 (`Region`) إلى الموضع 0. بعد هذا الاستدعاء، يكون `Region` هو أول حقل صفحة ويكون `Year` هو الثاني. يظل وضع الالتفاف والترتيب بدون تغيير، لذا لا يزال الشريط معروضًا أفقيًا جنبًا إلى جنب — فقط تم تبديل ترتيب القائمتين المنسدلتين.
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

pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.ROW, 0);
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.PAGE, 1);
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.PAGE, 2);
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.DATA, 3);

pivotTable.setPageFieldOrder(AsposeCells.PrintOrderType.OVER_THEN_DOWN);
pivotTable.setPageFieldWrapCount(2);

pivotTable.getPageFields().move(0, 1);

pivotTable.calculateData();

workbook.save("pageFieldLayout_move.xlsx");
```
## **مقالات ذات صلة**
- [إضافة حقل الصفحة في الجدول المحوري](/cells/ar/nodejs-java/add-page-field-in-pivot-table/) — الصفحة الأصلية التي توضح كيفية إضافة حقول الصفحة إلى جدول محوري.
- [حقول الصفوف والأعمدة في الجدول المحوري](/cells/ar/nodejs-java/row-and-column-fields/) — يغطي تخصيص الحقول لمحوري الصفوف والأعمدة، مما يكمل العمل على محور الصفحة الموضح هنا.
- [إدارة حقول القيم في الجدول المحوري](/cells/ar/nodejs-java/manage-value-fields/) — يصف كيفية تكوين منطقة البيانات (القيم)، بما في ذلك تجميع `Sum` المستخدم في هذه المقالة.
- [تحديث الجدول المحوري](/cells/ar/nodejs-java/refresh-pivot-table/) — يوضح `refreshData` و`calculateData`، المطلوبان بعد إعادة ترتيب حقول الصفحة.
- [تطبيق نمط على الجدول المحوري](/cells/ar/nodejs-java/apply-style-to-pivot-table/) — يوضح كيفية تنسيق الجدول المحوري المعروض بعد وضع شريط حقل الصفحة.
{{< app/cells/assistant language="nodejs-java" >}}
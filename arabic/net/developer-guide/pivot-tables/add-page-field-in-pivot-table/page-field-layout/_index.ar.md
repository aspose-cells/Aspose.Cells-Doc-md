---
title: تعديل تخطيط حقل الصفحة في جدول محوري
linktitle: تعديل تخطيط حقل الصفحة في جدول محوري
description: تعلم كيفية التحكم في تخطيط منطقة حقل الصفحة في جدول محوري باستخدام Aspose.Cells for .NET، بما في ذلك تعيين ترتيب العرض وعدد الالتفاف وترتيب الحقول الخاصة بحقول الصفحة في أعلى الجدول المحوري.
keywords: Aspose.Cells، مكتبة .NET، جدول بيانات، جدول محوري، حقل الصفحة، ترتيب حقل الصفحة، عدد التفاف حقل الصفحة، نقل حقل الصفحة
type: docs
weight: 191
url: /ar/net/change-page-field-layout/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---


{{% alert color="primary" %}}

هذه المقالة هي امتداد لموضوع **إضافة حقل صفحة في جدول محوري**. توضح كيفية التحكم في تخطيط منطقة حقل الصفحة — شريط عناصر تحكم التصفية في أعلى الجدول المحوري — بما في ذلك ترتيب العرض وعدد الالتفاف وإعادة ترتيب الحقول.

{{% /alert %}}

## **مقدمة**

يكشف الجدول المحوري في Microsoft Excel عن **منطقة حقل صفحة** مخصصة تقع فوق جسم الصف/العمود/البيانات في الجدول. يتم عرض هذه المنطقة كشريط من عناصر تحكم التصفية المنسدلة (واحد لكل حقل صفحة) وهي التي ينقر عليها المستخدمون النهائيون لتقطيع المحور بمعايير مثل السنة أو المنطقة. Aspose.Cells تصمم هذه المنطقة من خلال مجموعة `PivotTable.PageFields` وتعرض ثلاث خصائص تتحكم في كيفية عرض الشريط بصريًا:

- `PivotTable.PageFieldOrder` (قيمة `Aspose.Cells.PrintOrderType`) تقرر ما إذا كانت حقول الصفحة الإضافية ستوضع *بجانب* الحقول الحالية أو *أسفلها*.
- `PivotTable.PageFieldWrapCount` تحدد عدد حقول الصفحة الموضوعة لكل صف أو عمود قبل الالتفاف.
- `PivotTable.PageFields.Move(currIndex, destIndex)` يعيد ترتيب حقول الصفحة دون تغيير وضع الترتيب.

تتناول هذه المقالة ثلاثة أمثلة على التعليمات البرمجية التي توضح كل عملية من هذه العمليات على مجموعة بيانات مشتركة، حتى تتمكن من مقارنة التخطيطات الناتجة جنبًا إلى جنب.

## **بيانات المصدر**

تقوم الأمثلة الثلاثة أدناه بتحميل هذه الصفوف الثمانية من بيانات المبيعات في ورقة عمل باسم `PivotData`. تحتوي البيانات على مرشحين لحقول الصفحة (`Year`، `Region`)، ومرشح واحد لحقل الصف (`Fruit`)، ومقياس واحد (`Amount`)، مما يجعل شريط حقل الصفحة ذا مغزى للفحص.

| Fruit  | Year | Region | Amount |
|--------|------|--------|--------|
| Apple  | 2022 | North  | 150    |
| Apple  | 2023 | North  | 180    |
| Banana | 2022 | South  | 120    |
| Banana | 2023 | South  | 140    |
| Cherry | 2022 | East   | 200    |
| Cherry | 2023 | East   | 220    |
| Grape  | 2022 | West   | 90     |
| Grape  | 2023 | West   | 110    |

يتم ملء جميع الصفوف الثمانية في كل مثال من أمثلة التعليمات البرمجية، بنفس الترتيب، بحيث لا تختلف بيانات المصدر أبدًا بين السيناريوهات — فقط خصائص تخطيط حقل الصفحة هي التي تختلف.

## **المثال 1: Over Then Down**

في السيناريو الأول، نقوم بتكوين حقلي الصفحة (`Year`، `Region`) ليظهروا **جنبًا إلى جنب في صف واحد** في أعلى الجدول المحوري. نخصص `Fruit` لمحور الصف، ونضع `Year` أولاً و`Region` ثانياً على محور الصفحة (يحدد ترتيب استدعاءات `AddFieldToArea` فهرس البداية)، ونضيف `Amount` (Sum) كحقل بيانات، ثم نعين `PageFieldOrder` إلى `PrintOrderType.OverThenDown` مع `PageFieldWrapCount = 2`. مع `OverThenDown` وعدد التفاف قدره 2، يتم وضع حقلي الصفحة أفقيًا جنبًا إلى جنب في صف واحد في أعلى الجدول المحوري، بحيث يشغل الشريط صفًا واحدًا بعرض اثنين.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

string dataDir = "output";
if (!Directory.Exists(dataDir)) Directory.CreateDirectory(dataDir);

Workbook workbook = new Workbook();
WorksheetCollection worksheets = workbook.Worksheets;

int pivotDataIdx = worksheets.Add("PivotData");
Worksheet pivotDataSheet = worksheets[pivotDataIdx];
Cells pivotDataCells = pivotDataSheet.Cells;

// الرؤوس (الصف 0)
pivotDataCells[0, 0].PutValue("Fruit");
pivotDataCells[0, 1].PutValue("Year");
pivotDataCells[0, 2].PutValue("Region");
pivotDataCells[0, 3].PutValue("Amount");

// الصف 1: تفاح، 2022، شمال، 150
pivotDataCells[1, 0].PutValue("Apple");
pivotDataCells[1, 1].PutValue(2022);
pivotDataCells[1, 2].PutValue("North");
pivotDataCells[1, 3].PutValue(150);

// الصف 2: تفاح، 2023، شمال، 180
pivotDataCells[2, 0].PutValue("Apple");
pivotDataCells[2, 1].PutValue(2023);
pivotDataCells[2, 2].PutValue("North");
pivotDataCells[2, 3].PutValue(180);

// الصف 3: موز، 2022، جنوب، 120
pivotDataCells[3, 0].PutValue("Banana");
pivotDataCells[3, 1].PutValue(2022);
pivotDataCells[3, 2].PutValue("South");
pivotDataCells[3, 3].PutValue(120);

// الصف 4: موز، 2023، جنوب، 140
pivotDataCells[4, 0].PutValue("Banana");
pivotDataCells[4, 1].PutValue(2023);
pivotDataCells[4, 2].PutValue("South");
pivotDataCells[4, 3].PutValue(140);

// الصف 5: كرز، 2022، شرق، 200
pivotDataCells[5, 0].PutValue("Cherry");
pivotDataCells[5, 1].PutValue(2022);
pivotDataCells[5, 2].PutValue("East");
pivotDataCells[5, 3].PutValue(200);

// الصف 6: كرز، 2023، شرق، 220
pivotDataCells[6, 0].PutValue("Cherry");
pivotDataCells[6, 1].PutValue(2023);
pivotDataCells[6, 2].PutValue("East");
pivotDataCells[6, 3].PutValue(220);

// الصف 7: عنب، 2022، غرب، 90
pivotDataCells[7, 0].PutValue("Grape");
pivotDataCells[7, 1].PutValue(2022);
pivotDataCells[7, 2].PutValue("West");
pivotDataCells[7, 3].PutValue(90);

// الصف 8: عنب، 2023، غرب، 110
pivotDataCells[8, 0].PutValue("Grape");
pivotDataCells[8, 1].PutValue(2023);
pivotDataCells[8, 2].PutValue("West");
pivotDataCells[8, 3].PutValue(110);

// إضافة ورقة PivotTableReport
int pivotTableSheetIdx = worksheets.Add("PivotTableReport");
Worksheet pivotTableSheet = worksheets[pivotTableSheetIdx];
PivotTableCollection pivotTables = pivotTableSheet.PivotTables;

// إنشاء جدول محوري مصدره PivotData!A1:D9 موضوع في A1 على PivotTableReport
int pivotIndex = pivotTables.Add("PivotData!A1:D9", "A1", "PivotTable1");
PivotTable pivotTable = pivotTables[pivotIndex];

// إضافة الحقول
pivotTable.AddFieldToArea(PivotFieldType.Row, 0);   // فاكهة
pivotTable.AddFieldToArea(PivotFieldType.Page, 1);  // سنة
pivotTable.AddFieldToArea(PivotFieldType.Page, 2);  // منطقة
pivotTable.AddFieldToArea(PivotFieldType.Data, 3);  // المبلغ
pivotTable.DataFields[0].Function = ConsolidationFunction.Sum;

// تكوين تخطيط منطقة حقل الصفحة: ضع حقول الصفحة أفقياً أولاً، التفاف بعد كل 2
pivotTable.PageFieldOrder = PrintOrderType.OverThenDown;
pivotTable.PageFieldWrapCount = 2;

// التحديث والحساب
pivotTable.CalculateData();

// حفظ
workbook.Save(Path.Combine(dataDir, "pageFieldLayout_overThenDown.xlsx"));
```

## **المثال 2: Down Then Over**

في هذا المثال نضع `Fruit` على محور الصف، و`Year` و`Region` على محور الصفحة (مع `Year` أولاً)، و`Amount` (Sum) كحقل بيانات — تمامًا كما في المثال 1. ثم نعين `PageFieldOrder` إلى `PrintOrderType.DownThenOver` و`PageFieldWrapCount` إلى `2`. مع `DownThenOver` وعدد التفاف قدره 2، يتم تكديس حقلي الصفحة عموديًا — `Year` في الأعلى، و`Region` مباشرة أدناه — مكونين عمودًا واحدًا في أعلى الجدول المحوري. وبالتالي يشغل الشريط صفين بعرض واحد، على عكس المثال 1.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

var workbook = new Workbook();
var pivotData = workbook.Worksheets[0];
pivotData.Name = "PivotData";
int pivotReportIdx = workbook.Worksheets.Add("PivotTableReport");
var pivotReport = workbook.Worksheets[pivotReportIdx];

var headers = new[] { "Fruit", "Year", "Region", "Amount" };
for (int c = 0; c < headers.Length; c++)
{
    pivotData.Cells[0, c].PutValue(headers[c]);
}

var data = new object[,]
{
    {"Apple", 2022, "North", 150},
    {"Apple", 2023, "North", 180},
    {"Banana", 2022, "South", 120},
    {"Banana", 2023, "South", 140},
    {"Cherry", 2022, "East", 200},
    {"Cherry", 2023, "East", 220},
    {"Grape", 2022, "West", 90},
    {"Grape", 2023, "West", 110}
};

for (int r = 0; r < data.GetLength(0); r++)
{
    for (int c = 0; c < data.GetLength(1); c++)
    {
        pivotData.Cells[r + 1, c].PutValue(data[r, c]);
    }
}

int idx = pivotReport.PivotTables.Add("PivotData!A1:D9", "A1", "PivotTable");
var pivotTable = pivotReport.PivotTables[idx];

pivotTable.AddFieldToArea(PivotFieldType.Row, 0);
pivotTable.AddFieldToArea(PivotFieldType.Page, 1);
pivotTable.AddFieldToArea(PivotFieldType.Page, 2);
pivotTable.AddFieldToArea(PivotFieldType.Data, 3);

pivotTable.PageFieldOrder = PrintOrderType.DownThenOver;
pivotTable.PageFieldWrapCount = 2;

pivotTable.CalculateData();

workbook.Save("pageFieldLayout_downThenOver.xlsx");
```

## **المثال 3: نقل حقل صفحة**

في السيناريو الثالث نحتفظ بمجموعة البيانات هذه وتخصيص الحقول، ونضع تخطيطًا محايدًا (`OverThenDown` مع عدد التفاف `2`)، ثم نوضح عملية `PageFields.Move`. يستدعي `Move(0, 1)` نقل حقل الصفحة في الفهرس 0 (`Year`) إلى الموضع 1، وينتقل حقل الصفحة الذي كان في الموضع 1 (`Region`) إلى الموضع 0. بعد هذا الاستدعاء، `Region` هو حقل الصفحة الأول و`Year` هو الثاني. وضع الالتفاف والترتيب لم يتغير، لذا لا يزال الشريط معروضًا أفقيًا جنبًا إلى جنب — فقط ترتيب القائمتين المنسدلتين قد تم تبديله.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

Workbook workbook = new Workbook();

Worksheet dataSheet = workbook.Worksheets[0];
dataSheet.Name = "PivotData";

dataSheet.Cells["A1"].PutValue("Fruit");
dataSheet.Cells["B1"].PutValue("Year");
dataSheet.Cells["C1"].PutValue("Region");
dataSheet.Cells["D1"].PutValue("Amount");

dataSheet.Cells["A2"].PutValue("Apple");
dataSheet.Cells["B2"].PutValue(2022);
dataSheet.Cells["C2"].PutValue("North");
dataSheet.Cells["D2"].PutValue(150);

dataSheet.Cells["A3"].PutValue("Apple");
dataSheet.Cells["B3"].PutValue(2023);
dataSheet.Cells["C3"].PutValue("North");
dataSheet.Cells["D3"].PutValue(180);

dataSheet.Cells["A4"].PutValue("Banana");
dataSheet.Cells["B4"].PutValue(2022);
dataSheet.Cells["C4"].PutValue("South");
dataSheet.Cells["D4"].PutValue(120);

dataSheet.Cells["A5"].PutValue("Banana");
dataSheet.Cells["B5"].PutValue(2023);
dataSheet.Cells["C5"].PutValue("South");
dataSheet.Cells["D5"].PutValue(140);

dataSheet.Cells["A6"].PutValue("Cherry");
dataSheet.Cells["B6"].PutValue(2022);
dataSheet.Cells["C6"].PutValue("East");
dataSheet.Cells["D6"].PutValue(200);

dataSheet.Cells["A7"].PutValue("Cherry");
dataSheet.Cells["B7"].PutValue(2023);
dataSheet.Cells["C7"].PutValue("East");
dataSheet.Cells["D7"].PutValue(220);

dataSheet.Cells["A8"].PutValue("Grape");
dataSheet.Cells["B8"].PutValue(2022);
dataSheet.Cells["C8"].PutValue("West");
dataSheet.Cells["D8"].PutValue(90);

dataSheet.Cells["A9"].PutValue("Grape");
dataSheet.Cells["B9"].PutValue(2023);
dataSheet.Cells["C9"].PutValue("West");
dataSheet.Cells["D9"].PutValue(110);

int pivotSheetIdx = workbook.Worksheets.Add("PivotTableReport");
Worksheet pivotSheet = workbook.Worksheets[pivotSheetIdx];

int pivotIdx = pivotSheet.PivotTables.Add("PivotData!A1:D9", "A3", "PivotTable");
PivotTable pivotTable = pivotSheet.PivotTables[pivotIdx];

pivotTable.AddFieldToArea(PivotFieldType.Row, 0);
pivotTable.AddFieldToArea(PivotFieldType.Page, 1);
pivotTable.AddFieldToArea(PivotFieldType.Page, 2);
pivotTable.AddFieldToArea(PivotFieldType.Data, 3);

pivotTable.PageFieldOrder = PrintOrderType.OverThenDown;
pivotTable.PageFieldWrapCount = 2;

pivotTable.PageFields.Move(0, 1);

pivotTable.CalculateData();

workbook.Save("pageFieldLayout_move.xlsx");
```

## **مقالات ذات صلة**

- [إضافة حقل صفحة في جدول محوري](/cells/ar/net/add-page-field-in-pivot-table/) — الصفحة الأم التي توضح كيفية إضافة حقول الصفحة إلى جدول محوري.
- [حقول الصفوف والأعمدة في الجدول المحوري](/cells/ar/net/pivot-table-add-row-and-column-fields/) — يغطي تخصيص الحقول لمحوري الصفوف والأعمدة، مما يكمل عمل محور الصفحة الموضح هنا.
- [إدارة حقول القيم في الجدول المحوري](/cells/ar/net/manage-value-fields/) — يصف كيفية تكوين منطقة البيانات (القيم)، بما في ذلك التجميع `Sum` المستخدم في هذه المقالة.
- [تحديث الجدول المحوري](/cells/ar/net/refresh-pivot-table/) — يوضح `RefreshData` و`CalculateData`، المطلوبان بعد إعادة ترتيب حقول الصفحة.
- [تطبيق نمط على الجدول المحوري](/cells/ar/net/apply-style-to-pivot-table/) — يوضح كيفية تنسيق الجدول المحوري المعروض بعد وضع شريط حقل الصفحة.

{{< app/cells/assistant language="csharp" >}}

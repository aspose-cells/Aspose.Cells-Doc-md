---
title: إظهار أو تصفية أفضل 10 في الجدول المحوري
linktitle: إظهار أو تصفية أفضل 10
description: تعلّم كيفية عرض العناصر الأعلى أو الأدنى تصنيفًا فقط في حقل محوري باستخدام Aspose.Cells for .NET. يتناول هذا المقال طريقة Top10AutoShow في Excel 97-2003، وقراءة الخيارات عبر Top10AutoShowSettings، وتصفية أفضل 10 في Excel 2007-365 عبر FilterTop10.
keywords: Aspose.Cells, .NET, جدول محوري, أفضل 10, العرض التلقائي, Top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, FilterTop10, PivotFilterType, PivotField, C#
type: docs
weight: 20
url: /ar/net/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام المحتملة**
قد يكون جدول محوري يسرد جميع عناصر حقل الصف صعب القراءة عندما يحتوي ذلك الحقل على عشرات العناصر. يحتفظ تقرير أفضل 10 بأعلى العناصر أو أدناها تصنيفًا فقط، وهو ما تحتاجه تقارير الترتيب تحديدًا — «أفضل 5 منتجات حسب الإيرادات» أو «أدنى 3 مناطق حسب عدد المبيعات». يدعم Aspose.Cells آليتين لهذا الغرض، تقابلان جيلين من إصدارات Microsoft Excel.
- **العرض التلقائي في Excel 97-2003** — طريقة `PivotField.Top10AutoShow()`. تمثل هذه الطريقة الإعداد الكلاسيكي لإظهار أفضل N عناصر أو أدنى N عناصر. ويُحفظ هذا الإعداد مباشرةً في حقل الجدول المحوري، ويعمل في جميع إصدارات Excel، القديمة والحديثة، لأنه جزء من تنسيق الجدول المحوري الأصلي.
- **تصفية أفضل 10 في Excel 2007-365** — طريقة `PivotField.FilterTop10()`. تمثل هذه الطريقة مرشح القيم الحديث لأفضل 10، الموجود ضمن «مرشحات القيم» في قائمة الحقل. ويُحفظ في صورة كائن `PivotFilter` مرتبط بالحقل، ويتيح ترتيب العناصر استنادًا إلى عددها أو نسبتها المئوية.

## **إظهار أفضل 10 في Excel 97-2003 (Top10AutoShow)**
يُضبط الإعداد الكلاسيكي للعرض التلقائي من خلال استدعاء واحد لـ `PivotField.Top10AutoShow(bool isAutoShow, bool isTop, int count, int rankBy)`:
- `isAutoShow` — يتيح إعداد العرض التلقائي على الحقل أو يعطله.
- `isTop` — تحتفظ القيمة `true` بالعناصر الأعلى تصنيفًا (الأعلى)، بينما تحتفظ `false` بالعناصر الأدنى (الأسفل).
- `count` — عدد العناصر المطلوب الاحتفاظ بها، مثل 10 في تقرير كلاسيكي لأفضل 10.
- `rankBy` — الفهرس بدءًا من الصفر لحقل **البيانات** الذي تحدد قيمه ترتيب العناصر. مرّر -1 لترتيب العناصر حسب الحقل نفسه.
يمكن أن يعتمد الترتيب على حقل قيمة أو على الحقل نفسه. ويوضح المستند أدناه خيارين طبيعيين.

### **الترتيب حسب حقل قيمة**
رتّب عناصر حقل الصف وفق حقل قيمة عادي مثل «مجموع المبيعات». يبني المثال التالي جدولًا محوريًا يتكون من حقل صف واحد (`Sport`) وحقل بيانات واحد (`Sales`)، ثم يعرض أفضل عنصرين من `Sport` حسب المبيعات. قيمة `rankBy` هي 0 لأن «مجموع المبيعات» هو حقل البيانات الموجود عند الفهرس 0.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Cells["A1"].PutValue("Sport");
worksheet.Cells["B1"].PutValue("Quarter");
worksheet.Cells["C1"].PutValue("Sales");
string[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
foreach (string sport in sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.Cells[row, 0].PutValue(sport);
        worksheet.Cells[row, 1].PutValue("Qtr" + quarter);
        worksheet.Cells[row, 2].PutValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.PivotTables.Add("A1:C16", 2, 5);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Sport");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Sales");
pivotTable.CalculateData();
PivotField sportField = pivotTable.RowFields[0];
// عرض أفضل عنصرين مرتبين حسب "مجموع المبيعات" (فهرس حقل البيانات 0)
sportField.Top10AutoShow(true, true, 2, 0);
pivotTable.CalculateData();
workbook.Save("output-top10-by-value-field.xlsx");
```

### **الترتيب حسب الحقل نفسه**
يمكن أيضًا ترتيب الحقل حسب نفسه — مرّر -1 كقيمة `rankBy`. لا يلزم وجود حقل بيانات إضافي لهذا الخيار؛ يكفي أن يوضع الحقل في منطقة الصفوف (أو الأعمدة). يعرض المثال التالي أدنى 3 عناصر من حقل `Sport`، مرتبة حسب الحقل نفسه. لا تُدرج سمة `rankBy` في XML الخاص بالجدول المحوري عند حفظ هذا الإعداد، لأن -1 هي القيمة الافتراضية للتنسيق، وتُرجع الخاصية `Top10AutoShowSettings.RankBy` القيمة -1.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Cells["A1"].PutValue("Sport");
worksheet.Cells["B1"].PutValue("Quarter");
worksheet.Cells["C1"].PutValue("Sales");
string[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
foreach (string sport in sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.Cells[row, 0].PutValue(sport);
        worksheet.Cells[row, 1].PutValue("Qtr" + quarter);
        worksheet.Cells[row, 2].PutValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.PivotTables.Add("A1:C16", 2, 5);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Sport");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Sales");
pivotTable.CalculateData();
PivotField sportField = pivotTable.RowFields[0];
// إظهار أدنى 3 عناصر مرتبة حسب الحقل نفسه (rankBy = -1)
sportField.Top10AutoShow(true, false, 3, -1);
pivotTable.CalculateData();
workbook.Save("output-top10-by-field-itself.xlsx");
```

## **قراءة الخيارات الحالية (Top10AutoShowSettings)**
تعيد الخاصية `PivotField.Top10AutoShowSettings` كائن `PivotFieldTop10AutoShowSettings` يتيح الوصول إلى خيارات العرض التلقائي المحفوظة حاليًا على الحقل. استخدمه للتحقق من طريقة عرض العناصر في مصنف موجود، أو في جدول محوري تم إعداده للتو، بما في ذلك المصنفات المحمّلة من ملف.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook("output-top10-by-value-field.xlsx");
PivotTable pivotTable = workbook.Worksheets[0].PivotTables[0];
PivotField sportField = pivotTable.RowFields[0];
PivotFieldTop10AutoShowSettings settings = sportField.Top10AutoShowSettings;
Console.WriteLine("AutoShow enabled: " + settings.IsAutoShow);
Console.WriteLine("Direction: " + (settings.IsTop ? "Top" : "Bottom"));
Console.WriteLine("Item count: " + settings.AutoShowCount);
Console.WriteLine("Ranking data field index: " + settings.RankBy);
```

تُقابل الخصائص الأربع سمات العرض التلقائي الكلاسيكية المكتوبة في XML الخاص بالجدول المحوري (`autoShow`، `topAutoShow`، `itemPageCount`، `rankBy`)، لذا تكون القيم المقروءة هي القيم التي تعتمدها جميع إصدارات Excel.

## **ملاحظة**

{{% alert color="primary" %}}
- الخصائص المباشرة لكائن `PivotField` المسماة `IsAutoShow` و`IsAscendShow` و`AutoShowCount` و`AutoShowField` موسومة بأنها مهملة. استخدم كائن `Top10AutoShowSettings` بدلًا منها: يقابل `Top10AutoShowSettings.IsAutoShow` خاصية `IsAutoShow`، ويقابل `Top10AutoShowSettings.IsTop` خاصية `IsAscendShow`، ويقابل `Top10AutoShowSettings.AutoShowCount` خاصية `AutoShowCount`، ويقابل `Top10AutoShowSettings.RankBy` خاصية `AutoShowField`. طريقة `Top10AutoShow()` نفسها هي الطريقة المدعومة لتغيير الإعدادات.
- تعمل `Top10AutoShow` مع حقول الصفوف والأعمدة. ولا يمكن ترتيب حقل موجود في منطقة الصفحات (التصفية) فقط بهذه الطريقة، لأن عناصره لا تُدرج ضمن تخطيط جسم الجدول المحوري.
{{% /alert %}}

## **Excel 2007-365: تصفية أفضل 10 (FilterTop10)**
تتيح إصدارات Excel الحديثة استخدام أفضل 10 بوصفه مرشح قيم في قائمة الحقل («مرشحات القيم»، «أفضل 10...»). يقدم Aspose.Cells تمثيلًا لهذا المرشح من خلال طريقة `PivotField.FilterTop10(int valueFieldIndex, PivotFilterType type, bool isTop, int itemCount)` التي تُرجع كائن `PivotFilter` الذي تم إنشاؤه:
- `valueFieldIndex` — الفهرس بدءًا من الصفر لحقل البيانات الذي تحدد قيمه المجمعة ترتيب العناصر.
- `type` — معنى `itemCount`. يحتفظ `PivotFilterType.Count` بعدد ثابت من العناصر (خيار «العناصر» في مربع الحوار). ويحتفظ `PivotFilterType.Percent` بنسبة مئوية من العناصر، لذا تكون `itemCount` هي النسبة نفسها؛ أي أن قيمة 30 تحتفظ بأفضل 30٪. ويرتب `PivotFilterType.Sum` العناصر وفق تغطية القيمة التراكمية.
- `isTop` — تعني القيمة `true` «الأعلى»، بينما تعني `false` «الأسفل».
- `itemCount` — قيمة N في «أفضل N»، وتعتمد وحدتها على `type`.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Cells["A1"].PutValue("Sport");
worksheet.Cells["B1"].PutValue("Quarter");
worksheet.Cells["C1"].PutValue("Sales");
string[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
foreach (string sport in sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.Cells[row, 0].PutValue(sport);
        worksheet.Cells[row, 1].PutValue("Qtr" + quarter);
        worksheet.Cells[row, 2].PutValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.PivotTables.Add("A1:C16", 2, 5);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Sport");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Sales");
pivotTable.CalculateData();
PivotField sportField = pivotTable.RowFields[0];
// مرشح Top 10 — احتفظ بأعلى عنصرين حسب "مجموع المبيعات" (فهرس حقل البيانات 0)
PivotFilter filter = sportField.FilterTop10(0, PivotFilterType.Count, true, 2);
// لاستخدام مرشح قائم على النسبة بدلاً من ذلك، احتفظ بأعلى 30٪ من العناصر:
// sportField.FilterTop10(0, PivotFilterType.Percent, true, 30);
pivotTable.PivotCache.Refresh();
pivotTable.CalculateData();
workbook.Save("output-top10-filter.xlsx");
```

{{% alert color="primary" %}}
`Top10AutoShow` و`FilterTop10` ميزتان منفصلتان. يكتب العرض التلقائي سمة `autoShow` الكلاسيكية على حقل الجدول المحوري، وتستخدمها جميع إصدارات Excel منذ Excel 97. ويكتب `FilterTop10` إدخال `PivotFilter` حديثًا، ويتطلب ذلك Excel 2007 أو أحدث. وعند فتح مصنف في إصدار أقدم من Excel، يعود الجدول المحوري الذي يستخدم المرشح الحديث إلى عرض جميع العناصر. وفضّل `Top10AutoShow` للمستندات التي يجب أن تُمرَّر ذهابًا وإيابًا عبر أدوات قديمة؛ أما المصنفات الحديثة، ففضّل `FilterTop10` لأنه يتوافق مع مرشحات القيم الأخرى.
{{% /alert %}}

## **المقالات ذات الصلة**
- [تصفية الجداول المحورية حسب التسمية أو القيمة](/cells/ar/net/filter-by-label-or-value-of-pivot-table/)
- [إضافة حقول الصفوف والأعمدة إلى الجدول المحوري](/cells/ar/net/pivot-table-add-row-and-column-fields/)
- [تجميع حقول الجدول المحوري](/cells/ar/net/group-pivot-fields-in-the-pivot-table/)
- [تحديث الجدول المحوري](/cells/ar/net/refresh-pivot-table/)
- [إضافة حقل صفحة إلى الجدول المحوري](/cells/ar/net/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="csharp" >}}
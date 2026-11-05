---
title: إضافة التنسيق الشرطي إلى جدول محوري
linktitle: إضافة التنسيق الشرطي إلى جدول محوري
description: إضافة التنسيق الشرطي إلى جدول محوري في Aspose.Cells for .NET, ربط قاعدة بمنطقة البيانات باستخدام ApplyTo ونوع النطاق PivotConditionFormatScopeType, أو تعريف الهدف باستخدام AddCellArea و PivotAreas, ثم إرفاق القواعد والأنماط عبر FormatConditions.AddCondition.
keywords: Aspose.Cells, جدول محوري, التنسيق الشرطي, PivotConditionalFormat, ConditionalFormats, ApplyTo, PivotConditionFormatScopeType, Data, Field, Selection, AddCellArea, PivotAreas, AddPivotArea, FormatConditions, AddCondition, FormatConditionType, C#
type: docs
weight: 30
url: /ar/net/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام الممكنة**
الأنماط الموضحة في الصفحة الأم والصفحة الشقيقة ثابتة - يتم رسم منطقة `PivotArea` أو `CellArea` مرة واحدة وتحتفظ بنمطها بغض النظر عن القيم. التنسيق الشرطي هو المقابل القائم على القواعد - تمييز كل مبلغ يزيد عن 200، تظليل الخمسين بالمئة الوسطى، أو وضع علامة على العناصر ذات الترتيب الأدنى - ويستمر التمييز مع القيم كلما تم إعادة حساب أو تحديث جدول محوري.
في Aspose.Cells، يعيش التنسيق الشرطي للجدول المحوري في مجموعة `PivotTable.ConditionalFormats`. كل إدخال هو `PivotConditionalFormat` يجيب عن سؤالين بشكل مستقل:
- **أين تنطبق القاعدة؟** يتم تعريف المنطقة المستهدفة إما عبر `ApplyTo(int row, int column, PivotConditionFormatScopeType scope)`، الذي يعكس منتقي النطاق في واجهة مستخدم Excel، أو عبر `AddCellArea(CellArea)` ومجموعة `PivotAreas`، اللتين تسميان المنطقة صراحةً.
- **ماذا تختبر القاعدة؟** تتم إضافة شرط أو أكثر إلى `FormatConditions` باستخدام `FormatConditionCollection.AddCondition(FormatConditionType type, OperatorType operatorType, string formula1, string formula2)`، وكل شرط يحمل `Style` الخاص به.

{{% alert color="primary" %}}
لا تستدعي `FormatConditionCollection.Add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, string formula1, string formula2)` أو `FormatConditionCollection.AddArea(CellArea)` على كائن `FormatConditions` لتنسيق شرطي للجدول المحوري. هذان التحميلان موروثان من واجهة برمجة تطبيقات التنسيق الشرطي العادي في ورقة العمل ولا يعملان مع الجداول المحورية - لا يتم أبداً تحويل منطقة الخلية إلى منطقة محورية، لذا يتم تجاهل الطلب صامتًا. يجب دائمًا تعريف المنطقة على `PivotConditionalFormat` نفسها (`ApplyTo` أو `AddCellArea` أو `PivotAreas`) وإضافة القاعدة باستخدام أحد التحميلات `AddCondition`.
{{% /alert %}}

## **تطبيق قاعدة بنطاق (طريقة واجهة Excel)**
الطريقة الأولى تضع القاعدة كما تفعل واجهة Excel. يتم تسمية خلية جدول محوري بواسطة إحداثيات ورقة عمل صفرية، ويساعد نطاق `PivotConditionFormatScopeType` Aspose.Cells على تحديد مدى وصول القاعدة من تلك الخلية:
- `PivotConditionFormatScopeType.Data` - جميع خلايا القيم التي ينتجها جدول محوري، بما في ذلك الإجماليات العامة.
- `PivotConditionFormatScopeType.Field` - خلايا القيم التي تنتمي إلى الحقل الذي تحدده الخلية، مستثنية الإجماليات العامة. يجب أن تكون الخلية خلية حقل مثل تسمية حقل صف؛ تمرير خلية قيمة يؤدي إلى استثناء.
- `PivotConditionFormatScopeType.Selection` - فقط خلايا القيم عند التقاطع التي تحددها الخلية، عادةً خلية قيمة واحدة.
المثال أدناه يبني جدولًا محوريًا لمبيعات الفواكه مع الزاوية العلوية اليسرى في E3، يربط تنسيقًا شرطيًا بخلية F4 (الصف 3، العمود 5) بنطاق `Data`، ويظهر كل مبلغ أكبر من 200 بخط عريض أبيض على خلفية حمراء. مع القيم Apple 220، Banana 330، Cherry 200، والإجمالي العام 750، تقوم القاعدة بتلوين F4 وF5 وF7 - المنطقة التي تم حلها هي عمود البيانات الكامل F4:F7، وتضاء فقط الخلايا التي يمر قيمتها عبر القاعدة.

```csharp
using System;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cells cells = sheet.Cells;
string[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells["A1"].PutValue("Fruit");
cells["B1"].PutValue("Year");
cells["C1"].PutValue("Amount");
for (int i = 0; i < fruits.Length; i++)
{
    cells[i + 1, 0].PutValue(fruits[i]);
    cells[i + 1, 1].PutValue(years[i]);
    cells[i + 1, 2].PutValue(amounts[i]);
}
// Pivot table with its top-left corner at E3
PivotTable pivotTable = sheet.PivotTables.Add("=A1:C7", 2, 4);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.CalculateData();
// Anchor the conditional format at F4 (row 3, column 5) with the Data scope
int index = pivotTable.ConditionalFormats.Add();
PivotConditionalFormat format = pivotTable.ConditionalFormats[index];
format.ApplyTo(3, 5, PivotConditionFormatScopeType.Data);
// Rule - highlight amounts greater than 200
int conditionIndex = format.FormatConditions.AddCondition(
    FormatConditionType.CellValue, OperatorType.GreaterThan, "200", null);
Style style = workbook.CreateStyle();
style.Font.IsBold = true;
style.Font.Color = Color.White;
style.ForegroundColor = Color.Red;
style.Pattern = BackgroundType.Solid;
format.FormatConditions[conditionIndex].Style = style;
workbook.Save("PivotConditionalFormatData.xlsx");
```

ربط القاعدة نفسها بتسمية حقل الصف E4 (الصف 3، العمود 4) بنطاق `Field` ينتج عنه F4:F6 بدلاً من ذلك - نفس عمود البيانات دون صف الإجمالي العام - لأن النطاق الآن يصف حقل `Fruit` بدلاً من مساحة القيم كلها. النطاق `Selection` المرتبط بـ F4 ينتج عنه F4 فقط.

## **تحديد المنطقة يدويًا**
الطريقة الثانية تتخطى منتقي النطاق وتسمي المنطقة صراحةً على `PivotConditionalFormat`.

### **مستطيل ورقة العمل باستخدام AddCellArea**
`AddCellArea(CellArea)` يسجل المستطيل المحدد كهدف للقاعدة. الإحداثيات هي إحداثيات ورقة عمل صفرية، والمنطقة هي بالضبط المستطيل المقدم - دون توسيع إلى عمود البيانات ودون منطق الإجماليات العامة. استخدمه عندما تكون الخلايا المثيرة للاهتمام مستطيلًا ثابتًا معروفًا في تخطيط الجدول المحوري الحالي.

```csharp
using System;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cells cells = sheet.Cells;
string[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells["A1"].PutValue("Fruit");
cells["B1"].PutValue("Year");
cells["C1"].PutValue("Amount");
for (int i = 0; i < fruits.Length; i++)
{
    cells[i + 1, 0].PutValue(fruits[i]);
    cells[i + 1, 1].PutValue(years[i]);
    cells[i + 1, 2].PutValue(amounts[i]);
}
PivotTable pivotTable = sheet.PivotTables.Add("=A1:C7", 2, 4);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.CalculateData();
// Target the rectangle F4:F6 (the value cells without the grand total)
int index = pivotTable.ConditionalFormats.Add();
PivotConditionalFormat format = pivotTable.ConditionalFormats[index];
format.AddCellArea(new CellArea { StartRow = 3, StartColumn = 5, EndRow = 5, EndColumn = 5 });
// Rule - italic on light yellow for amounts between 150 and 300
int conditionIndex = format.FormatConditions.AddCondition(
    FormatConditionType.CellValue, OperatorType.Between, "150", "300");
Style style = workbook.CreateStyle();
style.Font.IsItalic = true;
style.ForegroundColor = Color.LightYellow;
style.Pattern = BackgroundType.Solid;
format.FormatConditions[conditionIndex].Style = style;
workbook.Save("PivotConditionalFormatCellArea.xlsx");
```

### **منطقة محورية دلالية باستخدام PivotAreas**
`PivotAreas` هو نموذج المنطقة الدلالية نفسه الذي تستخدمه الصفحة الشقيقة للأنماط الثابتة. أنشئ `PivotArea`، وحدد حقلًا أو منطقةً باستخدام `Select` أو `SelectField`، ثم أضفها باستخدام `PivotAreas.AddPivotArea(PivotArea)`. تبقى المنطقة الدلالية مرتبطة بحقلها، لذا يتبع التنسيق الشرطي الحقل عندما يتم تحديث جدول محوري ويتغير التخطيط. لا يزال التحميل `PivotAreas.Add(PivotArea)` يُجمع لكن تم وسمه كمهمل - يفضَّل استخدام `AddPivotArea`.

```csharp
using System;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cells cells = sheet.Cells;
string[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells["A1"].PutValue("Fruit");
cells["B1"].PutValue("Year");
cells["C1"].PutValue("Amount");
for (int i = 0; i < fruits.Length; i++)
{
    cells[i + 1, 0].PutValue(fruits[i]);
    cells[i + 1, 1].PutValue(years[i]);
    cells[i + 1, 2].PutValue(amounts[i]);
}
PivotTable pivotTable = sheet.PivotTables.Add("=A1:C7", 2, 4);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.CalculateData();
// Attach the rule to the Amount data field as a semantic region
int index = pivotTable.ConditionalFormats.Add();
PivotConditionalFormat format = pivotTable.ConditionalFormats[index];
PivotArea area = new PivotArea(pivotTable);
area.SelectField(PivotFieldType.Data, "Amount");
format.PivotAreas.AddPivotArea(area);
// Rule - grey text for amounts below 150
int conditionIndex = format.FormatConditions.AddCondition(
    FormatConditionType.CellValue, OperatorType.LessThan, "150", null);
Style style = workbook.CreateStyle();
style.Font.Color = Color.Gray;
format.FormatConditions[conditionIndex].Style = style;
workbook.Save("PivotConditionalFormatPivotArea.xlsx");
```

## **مكان تخزين القواعد وكيفية بقاءها بعد إعادة التحميل**
كل استدعاء `ConditionalFormats.Add()` يضيف `PivotConditionalFormat` واحد إلى جدول محوري. تُحفظ الشروط وصيغها وأنماطها مع المصنف - فتح الملف مرة أخرى في المثال أدناه يظهر القاعدة نفسها مع نوعها وعاملها وصيغتها سليمة، وتُظهر `GetCellAreas()` نفس المناطق. تُحذف الإدخالات التي لم تتلقى شرطًا عند حفظ المصنف، بنفس الطريقة التي يزيل بها Excel تنسيقًا شرطيًا لا يحتوي على قاعدة.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook("PivotConditionalFormatData.xlsx");
PivotTable pivotTable = workbook.Worksheets[0].PivotTables[0];
Console.WriteLine("Conditional formats: " + pivotTable.ConditionalFormats.Count);
for (int i = 0; i < pivotTable.ConditionalFormats.Count; i++)
{
    PivotConditionalFormat format = pivotTable.ConditionalFormats[i];
    for (int j = 0; j < format.FormatConditions.Count; j++)
    {
        FormatCondition condition = format.FormatConditions[j];
        Console.WriteLine($"Format {i}: {condition.Type} {condition.Operator} formula1={condition.Formula1}");
    }
    foreach (CellArea area in format.GetCellAreas())
        Console.WriteLine($"    rows {area.StartRow + 1}-{area.EndRow + 1}, columns {area.StartColumn + 1}-{area.EndColumn + 1}");
}
// This prints:
// Conditional formats: 1
// Format 0: CellValue GreaterThan formula1==200
//     rows 4-7, columns 6-6        (F4:F7, the resolved data region)
```

## **مقالات ذات صلة**
- [تطبيق نمط على جدول محوري](/cells/ar/net/apply-style-to-pivot-table/)
- [تنسيق جزء من جدول محوري](/cells/ar/net/format-part-of-pivot-table/)
- [أعلى 10 إظهار أو تصفية في جدول محوري](/cells/ar/net/top-10-show-or-filter-in-pivot-table/)
- [تصفية الجداول المحورية حسب التسمية أو القيمة](/cells/ar/net/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="csharp" >}}
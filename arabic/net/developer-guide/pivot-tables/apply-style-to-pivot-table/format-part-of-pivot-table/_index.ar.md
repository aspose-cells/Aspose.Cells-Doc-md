---
title: تنسيق جزء من جدول محوري
description: قم بتنسيق جزء من جدول محوري في Aspose.Cells for .NET عن طريق تطبيق الأنماط على مناطق PivotArea الدلالية أو مستطيلات CellArea عبر PivotTable.Format، مع تخزين التنسيقات في PivotTable.PivotFormats والحفاظ عليها عند تحديث الجدول المحوري.
linktitle: Format Part of a Pivot Table
keywords: Aspose.Cells, جدول محوري, تنسيق, PivotArea, CellArea, PivotTable.Format, PivotFormats, PivotTableSelectionType, LabelOnly, DataOnly, SelectField, FormatAll, C#
type: docs
weight: 20
url: /ar/net/format-part-of-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام المحتملة**
`PivotTable.FormatAll` يطبق نمطًا واحدًا على كامل الجدول المحوري ويتم تغطيته في الصفحة الأصلية. لا يفرق بين التسميات، القيم، الإجماليات، أو المناطق المحددة في التقرير.
عمليًا، عادةً ما يحتاج جزء فقط من الجدول المحوري إلى التمييز. تشمل الأهداف الشائعة التسميات التابعة لحقل صف واحد، الخلايا ذات القيم التي ينتجها حقل واحد، صف الإجمالي الكلي، أو مستطيل عشوائي مثل الصفين الأولين من العناصر.
تطبيق نمط مباشرةً على خلايا ورقة العمل للجدول المحوري ليس مكافئًا. يقوم Excel بتخزين تنسيقات الجدول المحوري كمناطق `PivotArea` دلالية بدلاً من سجلات نمط الخلايا العادية. يبقى تنسيق منطقة المحور مربوطًا بمنطقة مثل تسميات الحقل أو قيم البيانات، ويتم إعادة حلها عندما يُعاد حساب الجدول المحوري أو يتم تحديثه أو توسيعه. أما النمط المكتوب مباشرةً إلى خلية، فهو يخص موقع تلك الخلية ولا يتعقّبها نموذج الجدول المحوري.
Aspose.Cells يكشف عن عائلة التحميل الزائدة الكاملة `PivotTable.Format` بحيث يتوفر كلا النوعين من التنسيق:
- `Format(PivotArea, Style)` يربط نمطًا بمنطقة دلالية تُبنى باستخدام `PivotArea.Select` أو `PivotArea.SelectField`.
- `Format(CellArea, Style)` يربط نمطًا بمستطيل ورقة عمل داخل الجدول المحوري.
- `Format(int row, int column, Style)` يستهدف خلية واحدة.
- `FormatAll(Style)` ينسق كامل الجدول المحوري.

## **تنسيق مساحة PivotArea**
تدفق العمل القائم على المنطقة الدلالية هو النهج الموصى به عندما يجب أن يتبع التمييز حقلًا أو منطقة من التقرير.
1. إنشاء كائن `PivotArea` باستخدام `new PivotArea(pivotTable)`. يصف الكائن منطقة دلالية تنتمي إلى ذلك الجدول المحوري المحدد.
2. حدد حقلًا بناءً على موقعه الصفري على محور معين باستخدام `PivotArea.Select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)`.
   - `PivotTableSelectionType.DataAndLabel` يحدد كلًا من التسميات والبيانات الخاصة بالحقل.
   - `PivotTableSelectionType.LabelOnly` يحدد تسميات الحقل فقط.
   - `PivotTableSelectionType.DataOnly` يحدد خلايا بيانات الحقل فقط.
3. حدد حقلًا بالاسم باستخدام `PivotArea.SelectField(PivotFieldType axisType, string fieldName)`. عندما يتم اختيار حقل صف بالاسم، تتحول المنطقة إلى خلايا القيم التي ينتجها عناصر ذلك الحقل.
4. أنشئ `Style` باستخدام `Workbook.CreateStyle()`، واضبط الخط ولون المقدمة ونمط الخلفية الصلبة، ثم مرر النمط إلى `PivotTable.Format(area, style)`.
5. كل استدعاء لتحميل الزائدة `PivotArea` يضيف إدخالًا واحدًا من نوع `PivotTableFormat` إلى `PivotTable.PivotFormats`.
6. تُرسم التنسيقات المرتبطة بالحقل عند حساب بيانات المحور. لذلك، استدع `PivotTable.CalculateData()` بعد تطبيق التنسيقات لكي تصبح الأنماط مرئية.
المثال التالي يبني جدولًا محوريًا صغيرًا لمبيعات الفواكه، ينسق تسميات صف `Fruit` باستخدام `PivotArea.Select` و `PivotTableSelectionType.LabelOnly`، ينسق خلايا القيم التي ينتجها نفس حقل الصف باستخدام `PivotArea.SelectField`، ثم يُعيد حساب الجدول المحوري لكي تُطبق كلا النمطين.

```csharp
using System;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cells cells = sheet.Cells;
// Fruit sales data
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
// Bold yellow fill on the row field's label cells
Style labelStyle = workbook.CreateStyle();
labelStyle.Font.IsBold = true;
labelStyle.ForegroundColor = Color.Yellow;
labelStyle.Pattern = BackgroundType.Solid;
PivotArea labelArea = new PivotArea(pivotTable);
labelArea.Select(PivotFieldType.Row, 0, PivotTableSelectionType.LabelOnly);
pivotTable.Format(labelArea, labelStyle);
// Light green fill on the value cells the row field produces
Style valueStyle = workbook.CreateStyle();
valueStyle.ForegroundColor = Color.LightGreen;
valueStyle.Pattern = BackgroundType.Solid;
PivotArea valueArea = new PivotArea(pivotTable);
valueArea.SelectField(PivotFieldType.Row, "Fruit");
pivotTable.Format(valueArea, valueStyle);
// Field-anchored formats are painted when the data is calculated
pivotTable.CalculateData();
// Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.Save("FormatPivotArea.xlsx");
```

## **تنسيق CellArea في الجدول المحوري**
يُستخدم `PivotTable.Format(CellArea, Style)` عندما تكون المنطقة المطلوبة مستطيلًا بسيطًا في ورقة العمل بدلاً من منطقة محورية دلالية.
يتم وصف `CellArea` بواسطة خصائص `StartRow` و `StartColumn` و `EndRow` و `EndColumn`. القيم هي إحداثيات ورقة العمل بصفر أساس، وتحديد الإحداثيات النهائية يحدد آخر صف وعمود متضمنين في المستطيل، وبالتالي تغطي المنطقة الخلايا من الموضع الابتدائي إلى الموضع النهائي شاملًا.
على عكس تنسيق مرتبط بحقل، يُطبق تنسيق `CellArea` على الخلايا فورًا. لا يلزم استدعاء آخر لـ `CalculateData()` لتظهر النمط.
قد يحتوي مستطيل `CellArea` على خلايا تسميات وخلايا قيم معًا. يصف القسم التالي كيفية تمثيل Aspose.Cells وExcel لهذا المستطيل داخليًا.
المثال التالي ينسق المستطيل `E4:F5` في الجدول المحوري بنمط مائل وأزرق فاتح ويحفظ المصنف دون أي إعادة حساب إضافية.

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
// Highlight the first two fruit rows (the rectangle E4:F5)
Style highlightStyle = workbook.CreateStyle();
highlightStyle.Font.IsItalic = true;
highlightStyle.ForegroundColor = Color.FromArgb(0xFF, 0x99, 0xCC, 0xFF);
highlightStyle.Pattern = BackgroundType.Solid;
CellArea rectangle = new CellArea { StartRow = 3, StartColumn = 4, EndRow = 4, EndColumn = 5 };
pivotTable.Format(rectangle, highlightStyle);
// E4:F5 is italic on light blue immediately, no recalculation needed
workbook.Save("FormatPivotCellArea.xlsx");
```

## **كيفية تعيين PivotAreas و CellAreas**
يقوم Excel بتخزين تنسيقات الجدول المحوري كسجلات `pivotArea` بدلاً من سجلات نمط الخلايا العادية في ورقة العمل. يستخدم Aspose.Cells نفس النموذج، لذا يتم تحويل طلب التنسيق إلى مناطق Pivot عند تسجيله.
العلاقة بين `CellArea` التي يقدمها المستخدم ومناطق الـ Pivot المخزنة داخليًا هي علاقة متعدد إلى متعدد في كلا الاتجاهين.
- قد ينتج عن `CellArea` واحدة عدة مناطق Pivot. إذا كان المستطيل يمتد لكل من خلايا التسميات والقيم، يتم تفكيكه إلى قواعد تسمية وبيانات منفصلة، لأن نموذج المحور يعالج تنسيق التسميات وتنسيق البيانات بشكل مستقل.
- قد يتحول منطقة Pivot واحدة إلى عدة مثيلات `CellArea` منفصلة. يمكن لمنطقة دلالية مثل صف الإجمالي الكلي، أو حقل لا تكون عناصره متتالية، أن تغطي مستطيلات متعددة. لهذا السبب تُعيد الدالة `PivotArea.GetCellAreas()` مجموعة بدلاً من مستطيل واحد.
كل عملية تنسيق تُجرى عبر `PivotTable.Format` تُسجل في `PivotTable.PivotFormats`. كل إدخال من نوع `PivotTableFormat` يُظهر `PivotArea` المرتبط والنمط `Style` المطبق عليه. تحميل الزائدة `PivotArea` يضيف إدخالًا واحدًا بالضبط لكل استدعاء، بينما `CellArea` التي تحتوي على مناطق دلالية مختلفة يمكن أن تُضيف عدة إدخالات.
للتمييز بين المناطق المخزنة، يُظهر كل `PivotArea` علمي `OnlyLabel` و `OnlyData`. المثال أدناه ينسق مستطيلًا واحدًا يغطي كلًا من التسميات والقيم، ويستعرض `PivotTable.PivotFormats`، ويطبع إحداثيات `CellArea` التي تحل كل منطقة Pivot مخزنة إليها.

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
Style highlightStyle = workbook.CreateStyle();
highlightStyle.Font.IsItalic = true;
highlightStyle.ForegroundColor = Color.FromArgb(0xFF, 0x99, 0xCC, 0xFF);
highlightStyle.Pattern = BackgroundType.Solid;
// ONE rectangle in...
CellArea rectangle = new CellArea { StartRow = 3, StartColumn = 4, EndRow = 4, EndColumn = 5 };
pivotTable.Format(rectangle, highlightStyle);
// ...TWO semantic pivot areas out: the label part and the data part are stored separately
Console.WriteLine("Stored formats: " + pivotTable.PivotFormats.Count);
for (int i = 0; i < pivotTable.PivotFormats.Count; i++)
{
    PivotArea storedArea = pivotTable.PivotFormats[i].PivotArea;
    Console.WriteLine($"Format {i}: OnlyLabel={storedArea.OnlyLabel}, OnlyData={storedArea.OnlyData}");
    foreach (CellArea resolved in storedArea.GetCellAreas())
        Console.WriteLine($"    rows {resolved.StartRow + 1}-{resolved.EndRow + 1}, columns {resolved.StartColumn + 1}-{resolved.EndColumn + 1}");
}
// This prints:
// Stored formats: 2
// Format 0: OnlyLabel=True, OnlyData=False
//     rows 4-5, columns 5-5        (E4:E5, the label part)
// Format 1: OnlyLabel=False, OnlyData=True
//     rows 4-5, columns 6-6        (F4:F5, the data part)
workbook.Save("FormatPivotAreasMap.xlsx");
```

{{% alert color="primary" %}}
نظرًا لأن التنسيقات تُخزن كمناطق Pivot بدلاً من أنماط خلايا عادية، فإنها تبقى صالحة بعد إعادة الحساب والتحديث. عندما يتم تحديث الجدول المحوري باستخدام `PivotTable.RefreshData`، أو إعادة حسابه بـ `CalculateData`، أو حفظه وإعادة تحميله، فإن كل منطقة Pivot مخزنة تُعيد حل موقعها الحالي وتُطبق النمط مرة أخرى.
{{% /alert %}}

استخدم `PivotArea` المبنية بـ `Select` أو `SelectField` عندما يجب أن يبقى التمييز مرتبطًا بحقل أو منطقة دلالية عبر عمليات التحديث، واستخدم `CellArea` عندما يكون تنسيق مستطيل ثابت في تخطيط الجدول المحوري الحالي كافيًا. تحميل الزائدة `Format(int row, int column, Style)` يستهدف خلية فردية. استخدم `FormatAll`، المذكور في الصفحة الأصلية، عندما يجب إعادة تنسيق كامل الجدول المحوري مرة واحدة.

## **مقالات ذات صلة**
- [تطبيق نمط على جدول محوري](/cells/ar/net/apply-style-to-pivot-table/)
- [إضافة حقول صف وعمود إلى جدول محوري](/cells/ar/net/pivot-table-add-row-and-column-fields/)
- [إدارة حقول القيم في جدول محوري](/cells/ar/net/manage-value-fields/)
- [تحديث جدول محوري](/cells/ar/net/refresh-pivot-table/)

{{< app/cells/assistant language="csharp" >}}
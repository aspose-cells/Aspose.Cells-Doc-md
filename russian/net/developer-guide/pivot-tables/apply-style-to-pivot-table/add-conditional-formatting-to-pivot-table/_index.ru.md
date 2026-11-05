---
title: Добавить условное форматирование к сводной таблице
linktitle: Добавить условное форматирование к сводной таблице
description: Добавьте условное форматирование к сводной таблице в Aspose.Cells for .NET — привяжите правило к области данных с помощью ApplyTo и области PivotConditionFormatScopeType, либо определите цель с помощью AddCellArea и PivotAreas, затем присоедините правила и стили через FormatConditions.AddCondition.
keywords: Aspose.Cells, сводная таблица, условное форматирование, PivotConditionalFormat, ConditionalFormats, ApplyTo, PivotConditionFormatScopeType, Data, Field, Selection, AddCellArea, PivotAreas, AddPivotArea, FormatConditions, AddCondition, FormatConditionType, C#
type: docs
weight: 30
url: /ru/net/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
Стилы, описанные на родительской странице и на соседней странице, являются статическими — область `PivotArea` или `CellArea` окрашивается один раз и сохраняет свой стиль независимо от значений. Условное форматирование — это правило‑управляемый аналог: подсветить каждую сумму выше 200, затенить средние пятьдесят процентов или пометить элементы с низшим рейтингом — и подсветка будет следовать за значениями каждый раз, когда сводная таблица пересчитывается или обновляется.  
В Aspose.Cells условное форматирование сводных таблиц находится в коллекции `PivotTable.ConditionalFormats`. Каждая запись представляет собой объект `PivotConditionalFormat`, который независимо отвечает на два вопроса:
- **Где применяется правило?** Целевая область задаётся либо через `ApplyTo(int row, int column, PivotConditionFormatScopeType scope)`, что соответствует выбору области в пользовательском интерфейсе Excel, либо через `AddCellArea(CellArea)` и коллекцию `PivotAreas`, где область указывается явно.  
- **Что проверяет правило?** Одно или несколько условий добавляются в `FormatConditions` с помощью `FormatConditionCollection.AddCondition(FormatConditionType type, OperatorType operatorType, string formula1, string formula2)`, причём каждое условие имеет собственный `Style`.

{{% alert color="primary" %}}
Не вызывайте `FormatConditionCollection.Add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, string formula1, string formula2)` или `FormatConditionCollection.AddArea(CellArea)` у объекта `FormatConditions` условного формата сводной таблицы. Эти два перегруженных метода наследованы из обычного API условного форматирования листа и не работают для сводных таблиц — область ячейки никогда не преобразуется в область сводной таблицы, поэтому запрос тихо игнорируется. Всегда задавайте область непосредственно в объекте `PivotConditionalFormat` (`ApplyTo`, `AddCellArea` или `PivotAreas`) и добавляйте правило через одну из перегрузок `AddCondition`.  
{{% /alert %}}

## **Применить правило с областью (как в интерфейсе Excel)**
Первый способ позиционирует правило так же, как это делает пользовательский интерфейс Excel. Ячейка сводной таблицы определяется её нулевыми координатами листа, а область `PivotConditionFormatScopeType` указывает Aspose.Cells, насколько далеко должно распространяться правило от этой ячейки:
- `PivotConditionFormatScopeType.Data` — все ячейки‑значения, создаваемые сводной таблицей, включая итоги.
- `PivotConditionFormatScopeType.Field` — ячейки‑значения, принадлежащие полю, которому соответствует данная ячейка, без итоговых строк. Ячейка должна быть меткой поля, например меткой строки; попытка передать ячейку‑значение вызывает исключение.
- `PivotConditionFormatScopeType.Selection` — только ячейки‑значения на пересечении, выбранные данной ячейкой, обычно одна ячейка‑значение.
Ниже пример, где создаётся сводная таблица продаж фруктов, левый верхний угол которой находится в E3, правило условного форматирования привязывается к ячейке F4 (строка 3, столбец 5) с областью `Data` и выделяет каждую сумму более 200 полужирным белым на красном фоне. При значениях Apple 220, Banana 330, Cherry 200 и общем итоге 750 правило закрашивает F4, F5 и F7 — разрешённая область представляет собой весь столбец данных F4:F7, и лишь ячейки, удовлетворяющие условию, подсвечиваются.

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

Привязка того же правила к метке поля строки E4 (строка 3, столбец 4) с областью `Field` приводит к диапазону F4:F6 — тот же столбец данных без строки итога, потому что область теперь описывает поле `Fruit`, а не всю область значений. Область `Selection`, привязанная к F4, ограничивается только F4.

## **Определить область вручную**
Второй способ обходит выбор области и задаёт её явно в объекте `PivotConditionalFormat`.

### **Прямоугольник листа с AddCellArea**
`AddCellArea(CellArea)` фиксирует переданный прямоугольник как цель правила. Координаты — нулевые координаты листа, и область точно соответствует указанному прямоугольнику — без расширения до столбца данных и без логики итогов. Используйте, когда интересующие ячейки представляют собой известный фиксированный прямоугольник текущего макета сводной таблицы.

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

### **Семантическая область сводной таблицы с PivotAreas**
`PivotAreas` — это та же семантическая модель области, которую использует соседняя страница для статических стилей. Создайте `PivotArea`, выберите поле или область с помощью `Select` или `SelectField` и добавьте её через `PivotAreas.AddPivotArea(PivotArea)`. Семантическая область остаётся привязанной к своему полю, поэтому условный формат следует за полем при обновлении сводной таблицы и изменении макета. Перегрузка `PivotAreas.Add(PivotArea)` всё ещё компилируется, но помечена устаревшей — предпочтительнее `AddPivotArea`.

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

## **Где хранятся правила и как они сохраняются при перезагрузке**
Каждый вызов `ConditionalFormats.Add()` добавляет один `PivotConditionalFormat` в сводную таблицу. Условия, их формулы и стили сохраняются вместе с рабочей книгой — повторное открытие файла в примере ниже показывает то же правило с его типом, оператором и формулой, а `GetCellAreas()` возвращает те же области. Записи, которым никогда не было присвоено условие, отбрасываются при сохранении рабочей книги, аналогично тому, как Excel удаляет условный формат без правила.

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

## **Сопутствующие статьи**
- [Применение стиля к сводной таблице](/cells/ru/net/apply-style-to-pivot-table/)
- [Форматировать часть сводной таблицы](/cells/ru/net/format-part-of-pivot-table/)
- [Отображение или фильтрация Top 10 в сводной таблице](/cells/ru/net/top-10-show-or-filter-in-pivot-table/)
- [Фильтрация сводных таблиц по метке или значению](/cells/ru/net/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="csharp" >}}
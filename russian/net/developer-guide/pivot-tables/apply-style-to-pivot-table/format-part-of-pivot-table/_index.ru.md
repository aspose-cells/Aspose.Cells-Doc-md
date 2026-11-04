---
title: Форматирование части сводной таблицы
description: Форматировать часть сводной таблицы в Aspose.Cells for .NET, применяя стили к семантическим регионам PivotArea или прямоугольникам CellArea через PivotTable.Format, при этом форматы сохраняются в PivotTable.PivotFormats и сохраняются при обновлении сводной таблицы.
linktitle: Format Part of a Pivot Table
keywords: Aspose.Cells, сводная таблица, форматирование, PivotArea, CellArea, PivotTable.Format, PivotFormats, PivotTableSelectionType, LabelOnly, DataOnly, SelectField, FormatAll, C#
type: docs
weight: 20
url: /ru/net/format-part-of-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
`PivotTable.FormatAll` применяет один стиль ко всей сводной таблице и описан на родительской странице. Он не различает метки, значения, итоги или отдельные регионы отчёта.
На практике обычно необходимо выделить только часть сводной таблицы. Распространённые цели включают метки, принадлежащие одному полю строк, ячейки значений, полученные от одного поля, строку общих итогов или произвольный прямоугольник, например первые две строки элементов.
Применение стиля непосредственно к ячейкам листа сводной таблицы не эквивалентно. Excel сохраняет форматирование сводной таблицы как семантические регионы `PivotArea`, а не как обычные записи стилей ячеек. Формат `PivotArea` привязан к региону, например к меткам поля или к значениям данных, и переопределяется при пересчёте, обновлении или расширении сводной таблицы. Стиль, записанный напрямую в ячейку, относится к конкретному расположению ячейки и не отслеживается моделью сводной таблицы.
Aspose.Cells предоставляет полный набор перегрузок `PivotTable.Format`, поэтому доступны оба типа форматирования:
- `Format(PivotArea, Style)` привязывает стиль к семантическому региону, построенному с помощью `PivotArea.Select` или `PivotArea.SelectField`.
- `Format(CellArea, Style)` привязывает стиль к прямоугольнику листа внутри сводной таблицы.
- `Format(int row, int column, Style)` ориентирован на одну ячейку.
- `FormatAll(Style)` форматирует всю сводную таблицу.

## **Форматировать область Pivot**
Рабочий процесс с семантической областью рекомендуется, когда выделение должно следовать за полем или регионом отчёта.
1. Создайте `PivotArea` с помощью `new PivotArea(pivotTable)`. Этот объект описывает семантический регион, принадлежащий конкретной сводной таблице.
2. Выберите поле по его нулевой позиции на заданной оси с помощью `PivotArea.Select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)`.
   - `PivotTableSelectionType.DataAndLabel` выбирает как метки, так и данные поля.
   - `PivotTableSelectionType.LabelOnly` выбирает только метки поля.
   - `PivotTableSelectionType.DataOnly` выбирает только ячейки данных поля.
3. Выберите поле по имени с помощью `PivotArea.SelectField(PivotFieldType axisType, string fieldName)`. Когда поле строк выбирается по имени, регион преобразуется в ячейки значений, созданные элементами этого поля.
4. Создайте `Style` с помощью `Workbook.CreateStyle()`, настройте шрифт, цвет переднего плана и сплошной фон, затем передайте стиль в `PivotTable.Format(area, style)`.
5. Каждый вызов перегрузки `PivotArea` добавляет одну запись `PivotTableFormat` в `PivotTable.PivotFormats`.
6. Форматы, привязанные к полю, применяются при расчёте данных сводной таблицы. Поэтому после применения форматов вызовите `PivotTable.CalculateData()`, чтобы стили стали видимыми.
Следующий пример создает небольшую сводную таблицу продаж фруктов, стилизует метки строк `Fruit` с помощью `PivotArea.Select` и `PivotTableSelectionType.LabelOnly`, стилизует ячейки значений, полученные тем же полем строки, используя `PivotArea.SelectField`, а затем пересчитывает сводную таблицу, чтобы оба стиля отобразились.

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

## **Форматировать область ячеек сводной таблицы**
Используйте `PivotTable.Format(CellArea, Style)`, когда интересующий регион представляет собой обычный прямоугольник листа, а не семантическую область сводной таблицы.
`CellArea` задаётся свойствами `StartRow`, `StartColumn`, `EndRow` и `EndColumn`. Значения являются координатами листа с нулевой базой, а конечные координаты указывают последнюю строку и столбец, включённые в прямоугольник, поэтому область охватывает ячейки от начального положения до конечного включительно.
В отличие от формата, привязанного к полю, формат `CellArea` применяется к ячейкам сразу. Дополнительный вызов `CalculateData()` не требуется для отображения стиля.
Прямоугольник `CellArea` может содержать одновременно метки и ячейки значений. В следующем разделе описывается, как Aspose.Cells и Excel представляют такой прямоугольник внутренне.
Следующий пример форматирует прямоугольник `E4:F5` сводной таблицы стилем курсив, светло‑голубой, и сохраняет рабочую книгу без дополнительного пересчёта.

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

## **Как сопоставляются Pivot Area и Cell Area**
Excel сохраняет форматирование сводной таблицы как записи `pivotArea`, а не как обычные записи стилей ячеек листа. Такая же модель используется в Aspose.Cells, поэтому запрос форматирования преобразуется в области pivot при сохранении.
Взаимосвязь между пользовательским `CellArea` и внутренними сохранёнными областями pivot является многим‑ко‑многим в обеих направлениях.
- Один `CellArea` может породить несколько областей pivot. Если прямоугольник охватывает как метки, так и ячейки значений, он разбивается на отдельные правила для меток и данных, поскольку модель pivot обрабатывает форматирование меток и данных независимо.
- Одна область pivot может соответствовать нескольким разъединённым `CellArea`. Семантический регион, например строка общих итогов, или поле, элементы которого не смежные, может охватывать несколько прямоугольников. Поэтому `PivotArea.GetCellAreas()` возвращает коллекцию, а не один прямоугольник.
Каждая операция форматирования, выполненная через `PivotTable.Format`, фиксируется в `PivotTable.PivotFormats`. Каждая запись `PivotTableFormat` раскрывает связанный `PivotArea` и применённый к нему `Style`. Перегрузка `PivotArea` добавляет ровно одну запись за вызов, тогда как `CellArea`, содержащий разные семантические регионы, может добавить несколько записей.
Чтобы различать сохранённые регионы, каждый `PivotArea` раскрывает флаги `OnlyLabel` и `OnlyData`. Пример ниже форматирует один прямоугольник, охватывающий как метки, так и значения, просматривает `PivotTable.PivotFormats` и выводит координаты `CellArea`, к которым каждая сохранённая область pivot преобразуется.

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
Поскольку форматы хранятся как области pivot, а не как обычные стили ячеек, они сохраняются при пересчёте и обновлении. Когда сводная таблица обновляется с помощью `PivotTable.RefreshData`, пересчитывается с помощью `CalculateData` или сохраняется и повторно загружается, каждая сохранённая область pivot переопределяется к текущему положению её региона, и стиль повторно применяются.
{{% /alert %}}

Используйте `PivotArea`, построенный с помощью `Select` или `SelectField`, когда выделение должно оставаться привязанным к полю или семантическому региону при обновлениях, и используйте `CellArea`, когда достаточно отформатировать фиксированный прямоугольник в текущем макете сводной таблицы. Перегрузка `Format(int row, int column, Style)` для одной ячейки ориентирована на отдельную ячейку. Применяйте `FormatAll`, описанный на родительской странице, когда необходимо переоформить всю сводную таблицу сразу.

## **Связанные статьи**
- [Применение стиля к сводной таблице](/cells/ru/net/apply-style-to-pivot-table/)
- [Добавление полей строк и столбцов в сводную таблицу](/cells/ru/net/pivot-table-add-row-and-column-fields/)
- [Управление полями значений в сводной таблице](/cells/ru/net/manage-value-fields/)
- [Обновление сводной таблицы](/cells/ru/net/refresh-pivot-table/)

{{< app/cells/assistant language="csharp" >}}
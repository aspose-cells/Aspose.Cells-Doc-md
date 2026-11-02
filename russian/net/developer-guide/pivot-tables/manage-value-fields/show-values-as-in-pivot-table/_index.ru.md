---
title: Отображение значений как в сводной таблице
linktitle: Отображение значений как в сводной таблице
description: Отображайте значения полей данных сводной таблицы в виде процента от общего итога, разницы с базовым элементом, скользящих итогов, рангов и др. с помощью Aspose.Cells for .NET.
keywords: Aspose.Cells, сводная таблица, показать значения как, формат отображения данных, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, C#
type: docs
weight: 145
url: /ru/net/show-values-as-in-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
Сводная таблица обычно агрегирует каждое поле данных с помощью агрегатной функции, такой как `Sum` или `Count`. Функция Excel **Show Values As** заменяет каждый отображаемый результат вторичным вычислением, полученным из этой агрегатной функции — например, процентом от общего итога, скользящим итогом, разницей от выбранного базового элемента или рангом — что позволяет выполнять сравнительный анализ без вспомогательных формул или вычисляемых столбцов. Типичные применения включают анализ доли от общего итога, включая проценты по строке, столбцу или общему итогу; накопленную отчётность с использованием скользящего итога в поле периода; анализ отклонений от эталонного элемента с помощью разницы или процентной разницы от базового элемента; а также ранжирование значений от наименьшего к наибольшему или наоборот. В Aspose.Cells for .NET `PivotFieldDataDisplayFormat` выбирает вторичное вычисление. Свойство только для чтения `PivotField.ShowValuesSetting` возвращает объект `PivotShowValuesSetting`, в котором записываемые свойства `CalculationType`, `BaseFieldIndex`, `BaseItemPositionType` и `BaseItemIndex` настраивают поведение; удобный метод `PivotField.ShowValuesAs(...)` применяет те же четыре параметра одним вызовом. Применяйте эти настройки к полю данных (value field), полученному из `PivotTable.DataFields`.

## **Элементы перечисления PivotFieldDataDisplayFormat**
Поле данных сохраняет свою агрегатную функцию, такую как Sum или Count, а **Show Values As** изменяет только способ отображения агрегированного значения. Помимо прямой записи свойств `PivotShowValuesSetting` (см. последний раздел), удобный одношаговый метод применяет ту же конфигурацию:

```csharp
public void ShowValuesAs(PivotFieldDataDisplayFormat displayFormat, int baseField, PivotItemPositionType baseItemPositionType, int baseItem)
```

| Параметр | Описание | Когда требуется |
| --- | --- | --- |
| `displayFormat` | Вторичное вычисление `PivotFieldDataDisplayFormat`, которое следует применить. | Всегда. |
| `baseField` | Нулевая позиция индекса базового поля среди базовых полей сводной таблицы (например, индекс строкового поля, к которому относится базовый элемент). | Только шесть базовых форматов ниже (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfRunningTotalIn`, `PercentageOfParentTotal`); игнорируется всеми остальными форматами. |
| `baseItemPositionType` | Способ выбора базового элемента относительно текущего: `PivotItemPositionType.Previous`, `.Next` или `.Custom`. | Только три формата базового элемента (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`); игнорируется всеми остальными форматами. |
| `baseItem` | Нулевая позиция индекса базового элемента. | Только когда `baseItemPositionType` установлен в `Custom` (индекс элемента указывает точный базовый элемент); игнорируется для `Previous` / `Next` и всех не базовых форматов — передайте `0`. |

| Тип расчёта | Поведение | Параметры базового элемента |
| --- | --- | --- |
| `Normal` | Без вторичного вычисления; агрегированное значение отображается как есть (по умолчанию). | — |
| `DifferenceFrom` | Отображает значение как разницу от значения базового элемента в базовом поле. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` только при `Custom`) |
| `PercentageOf` | Отображает значение как процент от значения базового элемента в базовом поле. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` только при `Custom`) |
| `PercentageDifferenceFrom` | Отображает значение как процентную разницу от значения базового элемента в базовом поле. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` только при `Custom`) |
| `RunningTotalIn` | Отображает значение как скользящий итог для последовательных элементов базового поля. | `baseField` (поле, определяющее порядок накопления) |
| `PercentageOfRow` | Отображает значение как процент от итога строки. | — |
| `PercentageOfColumn` | Отображает значение как процент от итога столбца. | — |
| `PercentageOfTotal` | Отображает значение как процент от общего итога. | — |
| `Index` | Отображает значение по формуле Excel Index ((value * grand total) / (row total * column total)). | — |
| `PercentageOfParentRowTotal` | Отображает значение как процент от родительского итога строки (для вложенных строковых полей). | — |
| `PercentageOfParentColumnTotal` | Отображает значение как процент от родительского итога столбца (для вложенных столбцовых полей). | — |
| `PercentageOfParentTotal` | Отображает значение как процент от родительского итога. | `baseField` (базовое родительское поле) |
| `PercentageOfRunningTotalIn` | Отображает значение как процент от скользящего итога в базовом поле. | `baseField` (поле накопления) |
| `RankSmallestToLargest` | Ранжирует значение от наименьшего (1) к наибольшему. | — |
| `RankLargestToSmallest` | Ранжирует значение от наибольшего (1) к наименьшему. | — |

{{% alert color="primary" %}}
`ShowValuesAs(...)` записывает свойства `PivotShowValuesSetting` (`CalculationType`, `BaseFieldIndex`, `BaseItemPositionType`, `BaseItemIndex`) — метод и объект свойства представляют два способа настройки одного и того же состояния, аналогично выбору базового поля и базового элемента в диалоговом окне Excel **Show Values As**.
{{% /alert %}}

## **Отображение значений в виде процента от общего итога**
Вызовите метод `PivotField.ShowValuesAs` с параметром `PivotFieldDataDisplayFormat.PercentageOfTotal`, чтобы преобразовать каждую ячейку поля данных, включая общий итог, в её долю от общего итога. Отображаемые числа тогда представляют собой пропорции полного набора результатов. Этот формат сравнивает каждое значение только с общим итогом, поэтому не требует указания базового поля или базового элемента — завершающие аргументы (`0`, `PivotItemPositionType.Previous`, `0`) являются заполнительными и игнорируются форматом, как указано в таблице параметров.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;
// Load or create a workbook with source data
Workbook workbook = new Workbook();
Worksheet dataSheet = workbook.Worksheets[0];
dataSheet.Cells["A1"].PutValue("Fruit");
dataSheet.Cells["B1"].PutValue("Amount");
string[] fruits = { "Apple", "Banana", "Apple", "Cherry", "Banana", "Apple" };
int[] amounts = { 10, 20, 30, 40, 50, 60 };
for (int i = 0; i < fruits.Length; i++)
{
    dataSheet.Cells[i + 1, 0].PutValue(fruits[i]);
    dataSheet.Cells[i + 1, 1].PutValue(amounts[i]);
}
// Add a pivot table on a new worksheet
int pivotSheetIndex = workbook.Worksheets.Add();
PivotTable pivotTable = workbook.Worksheets[pivotSheetIndex].PivotTables.Add("=Sheet1!A1:B7", 2, 2);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.CalculateData();
// Show the Amount data field as a percentage of the grand total with the
// one-call method; PercentageOfTotal takes no base item, so the trailing
// base arguments (0, Previous, 0) are placeholders the format ignores
PivotField dataField = pivotTable.DataFields[0];
dataField.ShowValuesAs(PivotFieldDataDisplayFormat.PercentageOfTotal, 0, PivotItemPositionType.Previous, 0);
pivotTable.CalculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.Save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **Получение и настройка PivotField.ShowValuesSetting**
Прочитайте текущую конфигурацию через `PivotField.ShowValuesSetting`: свойство только для чтения возвращает объект `PivotShowValuesSetting` поля, в котором четыре свойства описывают активное вычисление **Show Values As**. Чтобы изменить конфигурацию, вызовите метод `PivotField.ShowValuesAs` — он записывает все четыре настройки за один вызов, поэтому нет необходимости назначать свойства по отдельности. Объект `PivotShowValuesSetting` раскрывает четыре свойства, которые записывает `ShowValuesAs`:
- `CalculationType` выбирает вторичное вычисление `PivotFieldDataDisplayFormat`.
- `BaseFieldIndex` указывает нулевой индекс базового поля среди полей сводной таблицы. Используется базовыми форматами.
- `BaseItemPositionType` определяет положение базового элемента относительно текущего и принимает значения `PivotItemPositionType.Next`, `PivotItemPositionType.Previous` или `PivotItemPositionType.Custom`.
- `BaseItemIndex` задаёт нулевой индекс базового элемента и используется, когда `BaseItemPositionType` установлен в `Custom`.
После вызова `ShowValuesAs` снова вызовите `PivotTable.CalculateData()`, чтобы тело сводной таблицы пересчиталось и перерисовалось с обновлённой конфигурацией.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook("ShowValuesAsPercentageOfTotal.xlsx");
PivotTable pivotTable = workbook.Worksheets[1].PivotTables[0];
PivotField dataField = pivotTable.DataFields[0];
// Read the current show-values settings
PivotShowValuesSetting settings = dataField.ShowValuesSetting;
Console.WriteLine($"CalculationType: {settings.CalculationType}");
Console.WriteLine($"BaseFieldIndex: {settings.BaseFieldIndex}");
Console.WriteLine($"BaseItemPositionType: {settings.BaseItemPositionType}");
Console.WriteLine($"BaseItemIndex: {settings.BaseItemIndex}");
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
dataField.ShowValuesAs(PivotFieldDataDisplayFormat.DifferenceFrom,
    pivotTable.RowFields[0].BaseIndex, PivotItemPositionType.Previous, 0);
pivotTable.CalculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
Console.WriteLine($"CalculationType now: {dataField.ShowValuesSetting.CalculationType}");
workbook.Save("ShowValuesAsDifferenceFrom.xlsx");
```

## **Связанные статьи**
- [Управление полями значений в сводной таблице](/cells/ru/net/manage-value-fields/)
- [Работа с форматами отображения данных поля DataField в сводной таблице](/cells/ru/net/working-with-data-display-formats-of-datafield-in-pivot-table/)
- [Обновление сводной таблицы](/cells/ru/net/refresh-pivot-table/)
- [Применение стиля к сводной таблице](/cells/ru/net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="csharp" >}}
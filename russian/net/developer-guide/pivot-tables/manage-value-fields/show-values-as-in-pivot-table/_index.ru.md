---
title: Отображение значений в сводной таблице
linktitle: Отображение значений в сводной таблице
description: Отображение значений полей данных сводной таблицы с использованием дополнительных вычислений, включая проценты от итога, отличие от базового элемента, нарастающие итоги и ранги, с помощью Aspose.Cells for .NET.
keywords: Aspose.Cells, сводная таблица, отображать значения как, PivotShowValuesAsType, PercentageOfTotal, PivotShowValuesSetting, ShowValuesAs, BaseFieldIndex, BaseItemIndex, C#
type: docs
weight: 145
url: /ru/net/show-values-as-in-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
Сводная таблица обычно агрегирует каждое поле данных с помощью агрегатной функции, например `Sum` или `Count`. Команда Excel **«Отображать значения как»** заменяет каждый отображаемый результат дополнительным вычислением, производным от этого агрегата, например процентом от общего итога, нарастающим итогом, отличием от выбранного базового элемента или рангом, и позволяет выполнять сравнительный анализ без вспомогательных формул и вычисляемых столбцов.
Типичные варианты применения включают анализ доли в общем итоге, в том числе расчет процентов от итога строки, столбца или общего итога; составление накопительной отчетности с использованием нарастающего итога в поле периода; анализ отклонений относительно эталонного элемента с помощью отличия от базового элемента или процентного отличия от него; а также ранжирование значений от наименьшего к наибольшему или от наибольшего к наименьшему.
В Aspose.Cells for .NET перечисление `PivotShowValuesAsType` задает тип дополнительного вычисления. Доступное только для чтения свойство `PivotField.ShowValuesSetting` возвращает объект `PivotShowValuesSetting`, изменяемые свойства которого `ShowValuesAs`, `BaseFieldIndex` и `BaseItemIndex` настраивают поведение; удобный метод `PivotField.ShowValuesAs(...)` применяет те же настройки одним вызовом. Примените эти настройки к полю данных или полю значений, полученному из `PivotTable.DataFields`.

## **Члены перечисления `PivotShowValuesAsType`**
Поле данных сохраняет агрегатную функцию, например Sum или Count, а команда «Отображать значения как» изменяет только способ отображения агрегированного значения.
Помимо прямого задания свойств `PivotShowValuesSetting` (см. последний раздел), для применения той же конфигурации предусмотрен удобный метод, выполняющий все настройки одним вызовом. Он представлен в двух перегрузках: первая определяет базовое поле и базовый элемент по индексам, вторая — по имени базового поля и подписи базового элемента:

```csharp
public void ShowValuesAs(PivotShowValuesAsType showValuesAsType, int baseField, int baseItem)
public void ShowValuesAs(PivotShowValuesAsType showValuesAsType, string baseField, string baseItem)
```

| Параметр | Значение | Когда требуется |
| --- | --- | --- |
| `showValuesAsType` | Дополнительное вычисление `PivotShowValuesAsType`, которое необходимо применить. | Всегда. |
| `baseField` | Индекс базового поля (с нуля) среди базовых полей сводной таблицы (например, индекс поля строки, к которому относится базовый элемент) или — в перегрузке со строкой — имя базового поля. | Для восьми приведенных ниже форматов, связанных с базовым полем (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn`, `RankSmallestToLargest`, `RankLargestToSmallest`); для всех остальных форматов передайте `0` (или `null` в перегрузке со строкой). |
| `baseItem` | Индекс базового элемента (с нуля); предусмотрены два служебных значения: `PivotShowValuesSetting.PreviousPivotItem` (-1) выбирает предыдущий элемент, а `PivotShowValuesSetting.NextPivotItem` (-2) — следующий. Перегрузка со строкой принимает вместо этого подпись базового элемента, а также `null`, если выбранному формату базовый элемент не требуется. | Только три формата, связанных с базовым элементом (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`), используют базовый элемент; пять форматов, связанных с полем (`RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn`, оба ранга), игнорируют его — передайте `0` или `null`. |

| Тип вычисления | Поведение | Параметры базового элемента |
| --- | --- | --- |
| `Normal` | Дополнительное вычисление отсутствует; агрегированное значение отображается как есть (по умолчанию). | — |
| `DifferenceFrom` | Отображает значение как отличие от значения базового элемента в базовом поле. | `baseField` + `baseItem` (индекс или подпись либо служебное значение предыдущего/следующего элемента) |
| `PercentageOf` | Отображает значение в процентах от значения базового элемента в базовом поле. | `baseField` + `baseItem` (индекс или подпись либо служебное значение предыдущего/следующего элемента) |
| `PercentageDifferenceFrom` | Отображает значение как процентное отличие от значения базового элемента в базовом поле. | `baseField` + `baseItem` (индекс или подпись либо служебное значение предыдущего/следующего элемента) |
| `RunningTotalIn` | Отображает значение как нарастающий итог по последовательным элементам базового поля. | `baseField` (поле, порядок элементов которого определяет накопление) |
| `PercentageOfRow` | Отображает значение в процентах от итога строки. | — |
| `PercentageOfColumn` | Отображает значение в процентах от итога столбца. | — |
| `PercentageOfTotal` | Отображает значение в процентах от общего итога. | — |
| `Index` | Отображает значение по формуле индекса Excel ((значение * общий итог) / (итог строки * итог столбца)). | — |
| `PercentageOfParentRowTotal` | Отображает значение в процентах от итога родительской строки (для вложенных полей строк). | — |
| `PercentageOfParentColumnTotal` | Отображает значение в процентах от итога родительского столбца (для вложенных полей столбцов). | — |
| `PercentageOfParentTotal` | Отображает значение в процентах от итога родительского поля. | `baseField` (родительское поле, итог которого служит базой) |
| `PercentageOfRunningTotalIn` | Отображает значение в процентах от нарастающего итога в базовом поле. | `baseField` (поле накопления) |
| `RankSmallestToLargest` | Ранжирует значение от наименьшего (1) до наибольшего. | `baseField` (поле, элементы которого определяют область ранжирования) |
| `RankLargestToSmallest` | Ранжирует значение от наибольшего (1) до наименьшего. | `baseField` (поле, элементы которого определяют область ранжирования) |

{{% alert color="primary" %}}
`ShowValuesAs(...)` записывает состояние `PivotShowValuesSetting` (`ShowValuesAs`, `BaseFieldIndex`, `BaseItemIndex`). Метод и объект, возвращаемый свойством, позволяют настроить одно и то же состояние двумя способами, аналогично выбору базового поля и базового элемента в диалоговом окне Excel «Отображать значения как».
{{% /alert %}}

## **Отображение значений в процентах от итога**
Вызовите метод `PivotField.ShowValuesAs` с `PivotShowValuesAsType.PercentageOfTotal`, чтобы значение каждой ячейки поля данных, включая ячейку общего итога, отображалось как доля от общего итога. Таким образом, отображаемые числа представляют доли полного набора результатов. Этот формат сопоставляет каждое значение только с общим итогом, поэтому базовое поле или базовый элемент ему не нужны — последние аргументы (`0`, `0`) являются условными значениями, которые игнорирует данный формат, как указано в приведенной выше таблице параметров.

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
// base arguments (0, 0) are placeholders the format ignores
PivotField dataField = pivotTable.DataFields[0];
dataField.ShowValuesAs(PivotShowValuesAsType.PercentageOfTotal, 0, 0);
pivotTable.CalculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.Save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **Получение и настройка `PivotField.ShowValuesSetting`**
Получите текущую конфигурацию с помощью `PivotField.ShowValuesSetting`: доступное только для чтения свойство возвращает объект `PivotShowValuesSetting` поля, свойства которого описывают активное вычисление команды «Отображать значения как». Чтобы изменить конфигурацию, вызовите метод `PivotField.ShowValuesAs`: он записывает все настройки одним вызовом, поэтому не требуется задавать свойства по одному.
Объект `PivotShowValuesSetting` предоставляет состояние, записываемое методом `ShowValuesAs`:
- `ShowValuesAs` выбирает дополнительное вычисление `PivotShowValuesAsType`.
- `BaseFieldIndex` задает индекс базового поля (с нуля) среди полей сводной таблицы. Он используется форматами, связанными с базовым полем.
- `BaseItemIndex` задает базовый элемент: индекс определенного элемента сводной таблицы (с нуля) или одно из двух служебных значений — `PivotShowValuesSetting.PreviousPivotItem` (-1) для предыдущего элемента и `PivotShowValuesSetting.NextPivotItem` (-2) для следующего элемента. Он используется форматами, связанными с базовым элементом.
- `BaseFieldName` и `BaseItemCaption` доступны только для чтения и возвращают определенное имя базового поля и подпись базового элемента; например, после выбора служебного значения предыдущего элемента `BaseItemCaption` возвращает `(previous)`.
После вызова `ShowValuesAs` снова вызовите `PivotTable.CalculateData()`, чтобы пересчитать и перерисовать тело сводной таблицы с обновленной конфигурацией.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook("ShowValuesAsPercentageOfTotal.xlsx");
PivotTable pivotTable = workbook.Worksheets[1].PivotTables[0];
PivotField dataField = pivotTable.DataFields[0];
// Read the current show-values settings
PivotShowValuesSetting settings = dataField.ShowValuesSetting;
Console.WriteLine($"ShowValuesAs: {settings.ShowValuesAs}");
Console.WriteLine($"BaseFieldIndex: {settings.BaseFieldIndex}");
Console.WriteLine($"BaseItemIndex: {settings.BaseItemIndex}");
Console.WriteLine($"BaseFieldName: {settings.BaseFieldName}");
Console.WriteLine($"BaseItemCaption: {settings.BaseItemCaption}");
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
dataField.ShowValuesAs(PivotShowValuesAsType.DifferenceFrom,
    pivotTable.RowFields[0].BaseIndex, PivotShowValuesSetting.PreviousPivotItem);
pivotTable.CalculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
Console.WriteLine($"ShowValuesAs now: {dataField.ShowValuesSetting.ShowValuesAs}");
workbook.Save("ShowValuesAsDifferenceFrom.xlsx");
```

## **Связанные статьи**
- [Управление полями значений в сводной таблице](/cells/ru/net/manage-value-fields/)
- [Работа с форматами отображения данных DataField в сводной таблице](/cells/ru/net/working-with-data-display-formats-of-datafield-in-pivot-table/)
- [Обновление сводной таблицы](/cells/ru/net/refresh-pivot-table/)
- [Применение стиля к сводной таблице](/cells/ru/net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="csharp" >}}
---
title: Показ значений как в сводной таблице
linktitle: Показ значений как в сводной таблице
description: Отображать значения полей данных сводной таблицы в виде процента от общего итога, разницы от базового элемента, накопительных итогов, рангов и т.д. с помощью Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells, Aspose.Cells for Node.js via C++, сводная таблица, отображать значения как, PivotShowValuesAsType, PercentageOfTotal, PivotShowValuesSetting, showValuesAs, BaseFieldIndex, BaseItemIndex
type: docs
weight: 145
url: /ru/nodejs-cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
Сводная таблица обычно агрегирует каждое поле данных с помощью агрегатной функции, такой как `SUM` или `COUNT`. Функция **Show Values As** в Excel заменяет каждый отображаемый результат вторичным вычислением, полученным из этой агрегации — например, процент от общего итога, накопительный итог, разницу от выбранного базового элемента или ранг — что позволяет выполнять сравнительный анализ без вспомогательных формул или вычисляемых столбцов.  
Обычными применениями являются анализ доли от общего итога, включая проценты по строке, столбцу или общему итогу; накопительная отчётность с использованием накопительного итога в поле периода; анализ отклонений относительно базового элемента с помощью разницы или процентной разницы от базового элемента; а также ранжирование значений от наименьшего к наибольшему или наоборот.  
В Aspose.Cells for Node.js via C++ перечисление `PivotShowValuesAsType` выбирает вторичное вычисление. Только для чтения аксессор `PivotField.getShowValuesSetting()` возвращает объект `PivotShowValuesSetting`, методы `setShowValuesAs()`, `setBaseFieldIndex()` и `setBaseItemIndex()` которого настраивают поведение; удобный метод `PivotField.showValuesAs(...)` применяет те же настройки одним вызовом. Примените эти настройки к полю данных или значений, полученному из `PivotTable.getDataFields()`.

## **Члены перечисления PivotShowValuesAsType**
Поле данных сохраняет свою агрегатную функцию, например SUM или COUNT, тогда как Show Values As изменяет только способ отображения агрегированного значения.  
Помимо прямой записи настроек `PivotShowValuesSetting` (см. последний раздел), удобный метод с одним вызовом применяет ту же конфигурацию. Он доступен в двух формах — с указанием базового поля и базового элемента по индексу и по имени:

```javascript
const AsposeCells = require("aspose.cells.node");
function showValuesAs(pivotField, showValuesAsType, baseField, baseItem) {
    pivotField.showValuesAs(showValuesAsType, baseField, baseItem);
}
function showValuesAsByName(pivotField, showValuesAsType, baseField, baseItem) {
    pivotField.showValuesAs(showValuesAsType, baseField, baseItem);
}
// index form: AsposeCells.PivotShowValuesAsType.PercentageOfTotal, 0, 0
// name form:  AsposeCells.PivotShowValuesAsType.PercentageOf, "Fruit", "Apple"
```

| Параметр | Значение | Когда требуется |
| --- | --- | --- |
| `showValuesAsType` | `PivotShowValuesAsType` — вторичный расчёт, который необходимо применить. | Всегда. |
| `baseField` | Нулевой индекс базового поля среди базовых полей сводной таблицы (например, индекс строкового поля, к которому относится базовый элемент) или — в форме имени — имя базового поля. | Восемь форматов, зависящих от базового поля ниже (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn`, `RankSmallestToLargest`, `RankLargestToSmallest`); для всех остальных форматов передайте `0` (или `null` в форме имени). |
| `baseItem` | Нулевой индекс базового элемента с двумя сигнальными значениями: -1 выбирает предыдущий элемент, а -2 — следующий (привязка Node.js via C++ не экспортирует именованные константы — передайте литеральные значения). В форме имени вместо индекса используется подпись базового элемента, а `null`, если выбранный формат не требует базового элемента. | Только три формата, использующие базовый элемент (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`) учитывают базовый элемент; пять форматов, зависящих от поля (`RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn`, оба ранга) игнорируют его — передайте `0` или `null`. |

| Тип расчёта | Поведение | Параметры базового элемента |
| --- | --- | --- |
| `Normal` | Без вторичного расчёта; агрегированное значение отображается как есть (по умолчанию). | — |
| `DifferenceFrom` | Отображает значение как разницу от значения базового элемента в базовом поле. | `baseField` + `baseItem` (индекс или подпись, либо сигнальное предыдущее/следующее значение) |
| `PercentageOf` | Отображает значение в виде процента от значения базового элемента в базовом поле. | `baseField` + `baseItem` (индекс или подпись, либо сигнальное предыдущее/следующее значение) |
| `PercentageDifferenceFrom` | Отображает значение как процентную разницу от значения базового элемента в базовом поле. | `baseField` + `baseItem` (индекс или подпись, либо сигнальное предыдущее/следующее значение) |
| `RunningTotalIn` | Отображает значение как накопительный итог по последовательным элементам базового поля. | `baseField` (поле, порядок элементов которого определяет накопление) |
| `PercentageOfRow` | Отображает значение как процент от итога строки. | — |
| `PercentageOfColumn` | Отображает значение как процент от итога столбца. | — |
| `PercentageOfTotal` | Отображает значение как процент от общего итога. | — |
| `Index` | Отображает значение, используя формулу индекса Excel ((value * grand total) / (row total * column total)). | — |
| `PercentageOfParentRowTotal` | Отображает значение как процент от итоговой суммы родительской строки (для вложенных строковых полей). | — |
| `PercentageOfParentColumnTotal` | Отображает значение как процент от итоговой суммы родительского столбца (для вложенных столбцовых полей). | — |
| `PercentageOfParentTotal` | Отображает значение как процент от итоговой суммы родительского поля. | `baseField` (родительское поле, чья сумма служит эталоном) |
| `PercentageOfRunningTotalIn` | Отображает значение как процент от накопительного итога в базовом поле. | `baseField` (поле накопления) |
| `RankSmallestToLargest` | Ранжирует значение от наименьшего (1) до наибольшего. | `baseField` (поле, элементы которого задают диапазон ранжирования) |
| `RankLargestToSmallest` | Ранжирует значение от наибольшего (1) до наименьшего. | `baseField` (поле, элементы которого задают диапазон ранжирования) |

{{% alert color="primary" %}}
`showValuesAs(...)` записывает настройки `PivotShowValuesSetting` (`getShowValuesAs()`/`setShowValuesAs()`, `getBaseFieldIndex()`/`setBaseFieldIndex()`, и `getBaseItemIndex()`/`setBaseItemIndex()`) — метод и объект свойства являются двумя способами настроить одно и то же состояние, отражая выбор базового поля и базового элемента в диалоге Show Values As в Excel.
{{% /alert %}}

## **Отображение значений как процент от общего итога**
Вызовите метод `PivotField.showValuesAs()` с параметром `PivotShowValuesAsType.PercentageOfTotal`, чтобы преобразовать каждую ячейку поля данных, включая общий итог, в её долю от общего итога. Отображаемые числа тогда представляют собой пропорции полной выборки. Этот формат сравнивает каждое значение только с общим итогом, поэтому не требуется базовое поле или базовый элемент — конечные аргументы (`0`, `0`) являются заполнителями, которые игнорируются форматом, как указано в таблице параметров выше.

```javascript
const AsposeCells = require("aspose.cells.node");
// Load or create a workbook with source data
const workbook = new AsposeCells.Workbook();
const dataSheet = workbook.getWorksheets().get(0);
dataSheet.getCells().get("A1").putValue("Fruit");
dataSheet.getCells().get("B1").putValue("Amount");
const fruits = ["Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"];
const amounts = [10, 20, 30, 40, 50, 60];
for (let i = 0; i < fruits.length; i++) {
    dataSheet.getCells().get(i + 1, 0).putValue(fruits[i]);
    dataSheet.getCells().get(i + 1, 1).putValue(amounts[i]);
}
// Add a pivot table on a new worksheet
const pivotSheetIndex = workbook.getWorksheets().add();
const pivotTable = workbook
    .getWorksheets()
    .get(pivotSheetIndex)
    .getPivotTables()
    .add("=Sheet1!A1:B7", 2, 2);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
// Show the Amount data field as a percentage of the grand total with the
// one-call method; PercentageOfTotal takes no base item, so the trailing
// base arguments (0, 0) are placeholders the format ignores
const dataField = pivotTable.getDataFields().get(0);
dataField.showValuesAs(AsposeCells.PivotShowValuesAsType.PercentageOfTotal, 0, 0);
pivotTable.calculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **Получить и настроить PivotField.getShowValuesSetting()**
Прочитайте текущие настройки через `PivotField.getShowValuesSetting()`: только для чтения аксессор возвращает объект `PivotShowValuesSetting` поля, чьи параметры описывают активный расчёт Show Values As. Чтобы изменить конфигурацию, вызовите метод `PivotField.showValuesAs()` — он записывает все параметры одним вызовом, поэтому вам не придётся задавать их по отдельности.  
Объект `PivotShowValuesSetting` раскрывает состояние, которое записывает `showValuesAs()`:
- `getShowValuesAs()` и `setShowValuesAs()` выбирают вторичный расчёт `PivotShowValuesAsType`.
- `getBaseFieldIndex()` и `setBaseFieldIndex()` указывают нулевой индекс базового поля среди полей сводной таблицы. Он используется в форматах, зависящих от базового поля.
- `getBaseItemIndex()` и `setBaseItemIndex()` указывают базовый элемент: нулевой индекс конкретного элемента сводной таблицы или одно из двух сигнальных значений — -1 для предыдущего элемента, -2 для следующего (привязка не экспортирует именованные константы). Он используется в форматах, зависящих от базового элемента.
- `getBaseFieldName()` и `getBaseItemCaption()` — только для чтения представления, которые возвращают разрешённое имя базового поля и подпись базового элемента; например, после выбора сигнального значения предыдущего элемента `getBaseItemCaption()` вернёт `(previous)`.  
После вызова `showValuesAs()` снова вызовите `PivotTable.calculateData()`, чтобы тело сводной таблицы было пересчитано и перерисовано с обновлённой конфигурацией.

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook("ShowValuesAsPercentageOfTotal.xlsx");
const pivotTable = workbook.getWorksheets().get(1).getPivotTables().get(0);
const dataField = pivotTable.getDataFields().get(0);
// Read the current show-values settings
const settings = dataField.getShowValuesSetting();
console.log(`ShowValuesAs: ${settings.getShowValuesAs()}`);
console.log(`BaseFieldIndex: ${settings.getBaseFieldIndex()}`);
console.log(`BaseItemIndex: ${settings.getBaseItemIndex()}`);
console.log(`BaseFieldName: ${settings.getBaseFieldName()}`);
console.log(`BaseItemCaption: ${settings.getBaseItemCaption()}`);
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
// -1 is the previous-item sentinel (the binding does not export the named constant)
dataField.showValuesAs(
    AsposeCells.PivotShowValuesAsType.DifferenceFrom,
    pivotTable.getRowFields().get(0).getBaseIndex(),
    -1
);
pivotTable.calculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
console.log(`ShowValuesAs now: ${dataField.getShowValuesSetting().getShowValuesAs()}`);
workbook.save("ShowValuesAsDifferenceFrom.xlsx");
```

## **Связанные статьи**
- [Управление полями значений в сводной таблице](/cells/ru/nodejs-cpp/manage-value-fields/)
- [Обновление сводной таблицы](/cells/ru/nodejs-cpp/refresh-pivot-table/)
- [Применение стиля к сводной таблице](/cells/ru/nodejs-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}
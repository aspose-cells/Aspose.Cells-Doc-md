---
title: Показать значения как в сводной таблице
linktitle: Показать значения как в сводной таблице
description: Отображать значения полей данных сводной таблицы в виде процента от общего итога, разницы от базового элемента, накопительных итогов, рангов и др. с Aspose.Cells for Node.js via Java.
keywords: Aspose.Cells, Aspose.Cells for Node.js via Java, сводная таблица, показать значения как, PivotShowValuesAsType, PERCENTAGE_OF_TOTAL, PivotShowValuesSetting, showValuesAs, BaseFieldIndex, BaseItemIndex
type: docs
weight: 145
url: /ru/nodejs-java/show-values-as-in-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
Сводная таблица обычно агрегирует каждое поле данных с помощью агрегирующей функции, такой как `SUM` или `COUNT`. Функция **Show Values As** в Excel заменяет каждый отображаемый результат вторичным вычислением, полученным из агрегата — например, процентом от общего итога, накопительным итогом, разницей от выбранного базового элемента или рангом — позволяя выполнять сравнительный анализ без вспомогательных формул или вычисляемых столбцов. Обычные применения включают анализ доли от общего итога, включая проценты по строке, столбцу или общему итогу; кумулятивную отчетность с использованием накопительного итога в поле периода; анализ отклонений от базового элемента с помощью разницы или процентной разницы; а также ранжирование значений от наименьшего к наибольшему или наоборот. В Aspose.Cells for Node.js via Java перечисление `PivotShowValuesAsType` выбирает вторичное вычисление. Метод только для чтения `PivotField.getShowValuesSetting()` возвращает объект `PivotShowValuesSetting`, чьи методы `setShowValuesAs()`, `setBaseFieldIndex()` и `setBaseItemIndex()` настраивают поведение; удобный метод `PivotField.showValuesAs(...)` применяет те же настройки одним вызовом. Применяйте эти настройки к полю данных или значений, полученному из `PivotTable.getDataFields()`.

## **Члены перечисления PivotShowValuesAsType**
Поле данных сохраняет свою агрегирующую функцию, например SUM или COUNT, тогда как Show Values As преобразует только способ отображения агрегированного значения. Помимо прямого использования сеттеров `PivotShowValuesSetting` (см. последний раздел), удобный метод с одним вызовом применяет ту же конфигурацию. Он существует в двух вариантах — один принимает базовое поле и базовый элемент по индексу, другой — по имени:

```javascript
const AsposeCells = require("aspose.cells");
function showValuesAs(pivotField, showValuesAsType, baseField, baseItem) {
    pivotField.showValuesAs(showValuesAsType, baseField, baseItem);
}
function showValuesAsByName(pivotField, showValuesAsType, baseField, baseItem) {
    pivotField.showValuesAs(showValuesAsType, baseField, baseItem);
}
// index form: AsposeCells.PivotShowValuesAsType.PERCENTAGE_OF_TOTAL, 0, 0
// name form:  AsposeCells.PivotShowValuesAsType.PERCENTAGE_OF, "Fruit", "Apple"
```

| Parameter | Meaning | When It Is Required |
| --- | --- | --- |
| `showValuesAsType` | Вторичное вычисление `PivotShowValuesAsType`, которое нужно применить. | Всегда. |
| `baseField` | Нулевой индекс базового поля среди базовых полей сводной таблицы (например, индекс строкового поля, к которому относится базовый элемент), или — в варианте по имени — имя базового поля. | Для восьми форматов, зависящих от базового поля (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `RANK_SMALLEST_TO_LARGEST`, `RANK_LARGEST_TO_SMALLEST`); для остальных форматов передайте `0` (или `null` в варианте по имени). |
| `baseItem` | Нулевой индекс базового элемента, с двумя специальными значениями: -1 выбирает предшествующий элемент и -2 — последующий (корень пакета не экспортирует константы `PivotShowValuesSetting` — передайте буквальные значения). В варианте по имени вместо индекса указывается подпись базового элемента, а `null`, когда выбранный формат не требует базового элемента. | Только три формата, использующие базовый элемент (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`) учитывают базовый элемент; пять форматов, зависящих от поля (`RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, оба ранга) игнорируют его — передайте `0` или `null`. |

| Calculation Type | Behavior | Base Item Parameters |
| --- | --- | --- |
| `NORMAL` | Отсутствие вторичного вычисления; агрегированное значение отображается как есть (по умолчанию). | — |
| `DIFFERENCE_FROM` | Отображает значение как разницу от значения базового элемента в базовом поле. | `baseField` + `baseItem` (индекс или подпись, либо предшествующий/последующий маркер) |
| `PERCENTAGE_OF` | Отображает значение как процент от значения базового элемента в базовом поле. | `baseField` + `baseItem` (индекс или подпись, либо предшествующий/последующий маркер) |
| `PERCENTAGE_DIFFERENCE_FROM` | Отображает значение как процентную разницу от значения базового элемента в базовом поле. | `baseField` + `baseItem` (индекс или подпись, либо предшествующий/последующий маркер) |
| `RUNNING_TOTAL_IN` | Отображает значение как накопительный итог для последовательных элементов базового поля. | `baseField` (поле, определяющее порядок накопления) |
| `PERCENTAGE_OF_ROW` | Отображает значение как процент от итога строки. | — |
| `PERCENTAGE_OF_COLUMN` | Отображает значение как процент от итога столбца. | — |
| `PERCENTAGE_OF_TOTAL` | Отображает значение как процент от общего итога. | — |
| `INDEX` | Отображает значение по формуле Excel INDEX ((value * grand total) / (row total * column total)). | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Отображает значение как процент от родительского итога строки (для вложенных строковых полей). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Отображает значение как процент от родительского итога столбца (для вложенных столбцовых полей). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Отображает значение как процент от родительского итога. | `baseField` (родительское поле, чьи итоги являются эталоном) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Отображает значение как процент от накопительного итога в базовом поле. | `baseField` (поле накопления) |
| `RANK_SMALLEST_TO_LARGEST` | Ранжирует значение от наименьшего (1) к наибольшему. | `baseField` (поле, определяющее область ранжирования) |
| `RANK_LARGEST_TO_SMALLEST` | Ранжирует значение от наибольшего (1) к наименьшему. | `baseField` (поле, определяющее область ранжирования) |

{{% alert color="primary" %}}
`showValuesAs(...)` записывает состояние `PivotShowValuesSetting` через `setShowValuesAs()`, `setBaseFieldIndex()` и `setBaseItemIndex()` — метод и объект свойства предоставляют два способа настройки одного и того же состояния, отражая выбор базового поля и базового элемента в диалоговом окне Show Values As Excel.
{{% /alert %}}

## **Показать значения как процент от общего итога**
Вызовите метод `PivotField.showValuesAs()` с параметром `PivotShowValuesAsType.PERCENTAGE_OF_TOTAL`, чтобы преобразовать каждую ячейку поля данных, включая общий итог, в её долю от общего итога. Отображаемые числа таким образом представляют собой доли от полного набора результатов. Этот формат сравнивает каждое значение только с общим итогом, поэтому не требует базового поля или базового элемента — завершающие аргументы (`0`, `0`) являются заполнительными и игнорируются форматом, как указано в таблице параметров выше.

```javascript
const AsposeCells = require("aspose.cells");
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
const pivotTable = workbook.getWorksheets().get(pivotSheetIndex).getPivotTables().add("=Sheet1!A1:B7", 2, 2);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Show the Amount data field as a percentage of the grand total with the
// one-call method; PERCENTAGE_OF_TOTAL takes no base item, so the trailing
// base arguments (0, 0) are placeholders the format ignores
const dataField = pivotTable.getDataFields().get(0);
dataField.showValuesAs(AsposeCells.PivotShowValuesAsType.PERCENTAGE_OF_TOTAL, 0, 0);
pivotTable.calculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **Получить и настроить PivotField.getShowValuesSetting()**
Прочитайте текущую конфигурацию с помощью `PivotField.getShowValuesSetting()`: метод только для чтения возвращает объект `PivotShowValuesSetting` поля, чьи свойства описывают активное вычисление Show Values As. Чтобы изменить конфигурацию, вызовите метод `PivotField.showValuesAs()` — он записывает все настройки одним вызовом, поэтому отдельные установки не требуются. Объект `PivotShowValuesSetting` раскрывает состояние, которое записывает `showValuesAs()`:
- `getShowValuesAs()` / `setShowValuesAs()` выбирает вторичное вычисление `PivotShowValuesAsType`.
- `getBaseFieldIndex()` / `setBaseFieldIndex()` указывает нулевой индекс базового поля среди полей сводной таблицы. Он используется форматами, зависящими от базового поля.
- `getBaseItemIndex()` / `setBaseItemIndex()` указывает базовый элемент: нулевой индекс конкретного элемента сводной таблицы или одно из двух специальных значений — -1 для предшествующего элемента, -2 для последующего (корень пакета не экспортирует именованные константы). Он используется форматами, зависящими от базового элемента.
- `getBaseFieldName()` и `getBaseItemCaption()` — только для чтения, показывают разрешённое имя базового поля и подпись базового элемента; например, после выбора маркера предыдущего элемента `getBaseItemCaption()` возвращает `(previous)`.
После вызова `showValuesAs()` снова вызовите `PivotTable.calculateData()`, чтобы тело сводной таблицы было пересчитано и перерисовано с обновлённой конфигурацией.

```javascript
const AsposeCells = require("aspose.cells");
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
// (-1 is the previous-item sentinel; the constants are not exported here)
dataField.showValuesAs(
    AsposeCells.PivotShowValuesAsType.DIFFERENCE_FROM,
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

## **Related Articles**
- [Управление полями значений в сводной таблице](/cells/ru/nodejs-java/manage-value-fields/)
- [Обновление сводной таблицы](/cells/ru/nodejs-java/refresh-pivot-table/)
- [Применение стиля к сводной таблице](/cells/ru/nodejs-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}
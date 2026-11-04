---
title: Показ значений как в сводной таблице
linktitle: Показ значений как в сводной таблице
description: Отображайте значения полей данных сводной таблицы в виде процента от общего итога, разницы от базового элемента, накопительные итоги, ранжирование и другие варианты с Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells, Aspose.Cells for Node.js via C++, сводная таблица, отобразить значения как, формат отображения данных, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex
type: docs
weight: 145
url: /ru/nodejs-cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
Сводная таблица обычно агрегирует каждое поле данных с помощью агрегирующей функции, такой как `SUM` или `COUNT`. Функция Excel **Show Values As** заменяет каждый отображаемый результат вторичным вычислением, полученным из этой агрегации — например, процентом от общего итога, накопительным итогом, разницей от выбранного базового элемента или рангом — позволяя выполнять сравнительный анализ без вспомогательных формул или вычисляемых столбцов.  
Типичные применения включают анализ доли от общего результата (проценты по строке, столбцу или общему итогу), накопительные отчёты, анализ отклонений от базового элемента посредством разницы или процентной разницы, а также ранжирование значений от наименьшего к наибольшему и наоборот.  
В Aspose.Cells for Node.js via C++ параметр `PivotFieldDataDisplayFormat` выбирает вторичное вычисление. Только для чтения accessor `PivotField.getShowValuesSetting()` возвращает объект `PivotShowValuesSetting`, свойства которого (`setCalculationType()`, `setBaseFieldIndex()`, `setBaseItemPositionType()`, `setBaseItemIndex()`) позволяют настроить поведение; удобный метод `PivotField.showValuesAs(...)` применяет те же четыре параметра одним вызовом. Применяйте эти настройки к полю данных, полученному через `PivotTable.getDataFields()`.

## **PivotFieldDataDisplayFormat Enumeration Members**
Поле данных сохраняет свою агрегирующую функцию, например `SUM` или `COUNT`, тогда как Show Values As меняет лишь способ отображения полученного агрегированного значения.  
Помимо прямого задания свойств `PivotShowValuesSetting` (см. последний раздел), удобный метод, вызываемый одним разом, применяет ту же конфигурацию:

```javascript
const AsposeCells = require("aspose.cells.node");
function showValuesAs(pivotField, displayFormat, baseField, baseItemPositionType, baseItem) {
    pivotField.showValuesAs(displayFormat, baseField, baseItemPositionType, baseItem);
}
function pickEnum(enumType, candidates, fallback) {
    const type = enumType || {};
    for (const name of candidates) {
        if (type[name] !== undefined && type[name] !== null) {
            return type[name];
        }
    }
    return fallback;
}
const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().add("PivotData");
const cells = sheet.getCells();
// --- Source data -----------------------------------------------------------
const headers = ["Region", "Product", "Sales"];
for (const [c, header] of headers.entries()) {
    cells.get(0, c).putValue(header);
}
const rows = [
    ["East", "Apple", 100],
    ["East", "Banana", 120],
    ["West", "Apple", 90],
    ["West", "Banana", 60],
    ["North", "Apple", 75],
    ["North", "Banana", 45]
];
for (const [r, row] of rows.entries()) {
    for (const [c, value] of row.entries()) {
        cells.get(r + 1, c).putValue(value);
    }
}
// --- Pivot table ------------------------------------------------------------
const pivotTables = sheet.getPivotTables();
const pivotTable = pivotTables.add("A1:C7", 0, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Region");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");
const salesField = pivotTable.getDataFields().get(0);
// --- ShowValuesAs -----------------------------------------------------------
const displayFormat = pickEnum(
    AsposeCells.PivotFieldDataDisplayFormat,
    ["PERCENT_OF_TOTAL", "PercentOfTotal", "PERCENTAGE_OF_TOTAL", "PercentageOfTotal"],
    7
);
const baseItemPositionType = pickEnum(
    AsposeCells.PivotItemPositionType,
    ["DEFAULT", "Default"],
    0
);
showValuesAs(salesField, displayFormat, -1, baseItemPositionType, -1);
// --- Save -------------------------------------------------------------------
workbook.save("ShowValuesAs.xlsx");
console.log("ShowValuesAs applied and workbook saved.");
```

| Параметр | Значение | Когда требуется |
| --- | --- | --- |
| `displayFormat` | Вторичное вычисление `PivotFieldDataDisplayFormat`, которое следует применить. | Всегда. |
| `baseField` | Нулевая индексация базового поля среди базовых полей сводной таблицы (например, индекс строкового поля, к которому относится базовый элемент). | Только шесть базовых форматов ниже (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`); игнорируется всеми остальными форматами. |
| `baseItemPositionType` | Способ выбора базового элемента относительно текущего: `PivotItemPositionType.PREVIOUS`, `.NEXT` или `.CUSTOM`. | Только три формата базового элемента (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`); игнорируется всеми остальными форматами. |
| `baseItem` | Нулевая индексация базового элемента. | Только когда `baseItemPositionType` равен `CUSTOM` (индекс указывает точный базовый элемент); игнорируется для `PREVIOUS`/`NEXT` и всех не‑базовых форматов — передайте `0`. |

| Тип расчёта | Поведение | Параметры базового элемента |
| --- | --- | --- |
| `NORMAL` | Без вторичного расчёта; отображается агрегированное значение как есть (по умолчанию). | — |
| `DIFFERENCE_FROM` | Показывает значение как разницу от значения базового элемента в базовом поле. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` только при `CUSTOM`) |
| `PERCENTAGE_OF` | Показывает значение как процент от значения базового элемента в базовом поле. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` только при `CUSTOM`) |
| `PERCENTAGE_DIFFERENCE_FROM` | Показывает значение как процентную разницу от значения базового элемента в базовом поле. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` только при `CUSTOM`) |
| `RUNNING_TOTAL_IN` | Показывает значение как накопительный итог для последовательных элементов базового поля. | `baseField` (поле, определяющее порядок накопления) |
| `PERCENTAGE_OF_ROW` | Показывает значение как процент от итога строки. | — |
| `PERCENTAGE_OF_COLUMN` | Показывает значение как процент от итога столбца. | — |
| `PERCENTAGE_OF_TOTAL` | Показывает значение как процент от общего итога. | — |
| `INDEX` | Показывает значение по формуле Excel INDEX ((value * grand total) / (row total * column total)). | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Показывает значение как процент от итога родительской строки (для вложенных строковых полей). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Показывает значение как процент от итога родительского столбца (для вложенных столбцовых полей). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Показывает значение как процент от итога родительского уровня. | `baseField` (базовое родительское поле) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Показывает значение как процент от накопительного итога в базовом поле. | `baseField` (поле накопления) |
| `RANK_SMALLEST_TO_LARGEST` | Ранжирует значение от наименьшего (1) к наибольшему. | — |
| `RANK_LARGEST_TO_SMALLEST` | Ранжирует значение от наибольшего (1) к наименьшему. | — |

{{% alert color="primary" %}}
`showValuesAs(...)` записывает настройки `PivotShowValuesSetting` (`getCalculationType()`/`setCalculationType()`, `getBaseFieldIndex()`/`setBaseFieldIndex()`, `getBaseItemPositionType()`/`setBaseItemPositionType()`, `getBaseItemIndex()`/`setBaseItemIndex()`) — метод и объект свойства представляют два способа задать одно и то же состояние, аналогично выбору базового поля и базового элемента в диалоговом окне Show Values As Excel.
{{% /alert %}}

## **Отображение значений в виде процента от общего итога**
Вызовите метод `PivotField.showValuesAs()` с параметром `PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL`, чтобы преобразовать каждую ячейку поля данных, включая общий итог, в её долю от общего итога. Отображаемые числа тогда представляют собой пропорции полного набора результатов. Этот формат сравнивает каждое значение только с общим итогом, поэтому не требует указания базового поля или базового элемента — завершающие аргументы (`0`, `PivotItemPositionType.PREVIOUS`, `0`) являются заполняющими значениями, которые формат игнорирует, как указано в таблице параметров выше.

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
// base arguments (0, Previous, 0) are placeholders the format ignores
const dataField = pivotTable.getDataFields().get(0);
dataField.showValuesAs(
    AsposeCells.PivotFieldDataDisplayFormat.PercentageOfTotal,
    0,
    AsposeCells.PivotItemPositionType.Previous,
    0
);
pivotTable.calculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **Получить и настроить PivotField.getShowValuesSetting()**
Прочитайте текущую конфигурацию через `PivotField.getShowValuesSetting()`: аксессор только для чтения возвращает объект `PivotShowValuesSetting` поля, в котором четыре свойства описывают активный расчёт **Show Values As**. Чтобы изменить конфигурацию, вызовите метод `PivotField.showValuesAs()` — он записывает все четыре настройки одним вызовом, поэтому нет необходимости задавать свойства по отдельности.  
Объект `PivotShowValuesSetting` раскрывает четыре настройки, записываемые `showValuesAs()`:
- `getCalculationType()` и `setCalculationType()` выбирают вторичное вычисление `PivotFieldDataDisplayFormat`.
- `getBaseFieldIndex()` и `setBaseFieldIndex()` указывают нулевой индекс базового поля среди полей сводной таблицы. Используется базовыми форматами.
- `getBaseItemPositionType()` и `setBaseItemPositionType()` определяют позицию базового элемента относительно текущего и принимают значения `PivotItemPositionType.NEXT`, `PivotItemPositionType.PREVIOUS` или `PivotItemPositionType.CUSTOM`.
- `getBaseItemIndex()` и `setBaseItemIndex()` задают нулевой индекс базового элемента и используются, когда `getBaseItemPositionType()` равно `CUSTOM`.  
После вызова `showValuesAs()` вновь вызовите `PivotTable.calculateData()`, чтобы тело сводной таблицы было пересчитано и перерисовано с обновлённой конфигурацией.

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook("ShowValuesAsPercentageOfTotal.xlsx");
const pivotTable = workbook.getWorksheets().get(1).getPivotTables().get(0);
const dataField = pivotTable.getDataFields().get(0);
// Read the current show-values settings
const settings = dataField.getShowValuesSetting();
console.log(`CalculationType: ${settings.getCalculationType()}`);
console.log(`BaseFieldIndex: ${settings.getBaseFieldIndex()}`);
console.log(`BaseItemPositionType: ${settings.getBaseItemPositionType()}`);
console.log(`BaseItemIndex: ${settings.getBaseItemIndex()}`);
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
dataField.showValuesAs(
    AsposeCells.PivotFieldDataDisplayFormat.DifferenceFrom,
    pivotTable.getRowFields().get(0).getBaseIndex(),
    AsposeCells.PivotItemPositionType.Previous,
    0
);
pivotTable.calculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
console.log(`CalculationType now: ${dataField.getShowValuesSetting().getCalculationType()}`);
workbook.save("ShowValuesAsDifferenceFrom.xlsx");
```

## **Связанные статьи**
- [Управление полями значений в сводной таблице](/cells/ru/nodejs-cpp/manage-value-fields/)
- [Обновление сводной таблицы](/cells/ru/nodejs-cpp/refresh-pivot-table/)
- [Применение стиля к сводной таблице](/cells/ru/nodejs-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}
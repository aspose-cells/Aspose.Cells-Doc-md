---
title: Отображение значений как в сводной таблице
description: Отображайте значения полей данных сводной таблицы в виде процента от общего итога, разницы от базового элемента, накопительных итогов, рангов и др. с помощью Aspose.Cells for Node.js via Java.
linktitle: Отображение значений как
keywords: Aspose.Cells, сводная таблица, отображение значений как, формат отображения данных, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, Node.js via Java
type: docs
weight: 145
url: /ru/nodejs-java/show-values-as-in-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
Сводная таблица обычно агрегирует каждое поле данных с помощью функции агрегирования, такой как `SUM` или `COUNT`. Функция Excel **Show Values As** заменяет каждый отображаемый результат вторичным расчётом, полученным из этой агрегаты — например, процентом от общего итога, накопительным итогом, разницей от выбранного базового элемента или рангом — что позволяет выполнять сравнительный анализ без вспомогательных формул или вычисляемых столбцов.  
Типичное применение включает анализ доли от общего итога, включая проценты по строке, столбцу или общему итогу; накопительную отчётность с использованием накопительного итога в поле периода; анализ отклонений от базового элемента с помощью разницы или процентной разницы; а также ранжирование значений от меньшего к большему или наоборот.  
В Aspose.Cells for Node.js via Java параметр `PivotFieldDataDisplayFormat` выбирает вторичный расчёт. Метод `PivotField.getShowValuesSetting()` только для чтения возвращает объект `PivotShowValuesSetting`. Его методы `setCalculationType()`, `setBaseFieldIndex()`, `setBaseItemPositionType()` и `setBaseItemIndex()` настраивают поведение; удобный метод `PivotField.showValuesAs(...)` применяет те же четыре параметра одним вызовом. Применяйте эти настройки к полю данных или значений, полученному через `PivotTable.getDataFields()`.

## **Перечисление PivotFieldDataDisplayFormat**
Поле данных сохраняет свою функцию агрегирования, такую как SUM или COUNT, в то время как Show Values As изменяет только способ отображения агрегированного значения.  
Помимо прямой записи параметров `PivotShowValuesSetting` (см. последний раздел), удобный метод‑один‑вызов применяет ту же конфигурацию:

```javascript
const AsposeCells = require("aspose.cells");
function showValuesAs(pivotField, displayFormat, baseField, baseItemPositionType, baseItem) {
    pivotField.showValuesAs(displayFormat, baseField, baseItemPositionType, baseItem);
}
module.exports = { showValuesAs };
```

| Параметр | Описание | Когда требуется |
| --- | --- | --- |
| `displayFormat` | Вторичный расчёт `PivotFieldDataDisplayFormat`, который необходимо применить. | Всегда. |
| `baseField` | Нулевой индекс базового поля среди базовых полей сводной таблицы (например, индекс строкового поля, к которому относится базовый элемент). | Только шесть базовых форматов ниже (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`); игнорируется всеми остальными форматами. |
| `baseItemPositionType` | Способ выбора базового элемента относительно текущего: `PivotItemPositionType.PREVIOUS`, `.NEXT` или `.CUSTOM`. | Только три формата базового элемента (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`); игнорируется всеми остальными форматами. |
| `baseItem` | Нулевой индекс базового элемента. | Только когда `baseItemPositionType` установлен в `CUSTOM` (индекс элемента указывает точный базовый элемент); игнорируется для `PREVIOUS`/`NEXT` и всех форматов без базового элемента — передайте `0`. |

| Тип расчёта | Поведение | Параметры базового элемента |
| --- | --- | --- |
| `NORMAL` | Нет вторичного расчёта; агрегированное значение отображается как есть (по умолчанию). | — |
| `DIFFERENCE_FROM` | Отображает значение как разницу от значения базового элемента в базовом поле. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` только при `CUSTOM`) |
| `PERCENTAGE_OF` | Отображает значение как процент от значения базового элемента в базовом поле. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` только при `CUSTOM`) |
| `PERCENTAGE_DIFFERENCE_FROM` | Отображает значение как процентную разницу от значения базового элемента в базовом поле. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` только при `CUSTOM`) |
| `RUNNING_TOTAL_IN` | Отображает значение как накопительный итог для последовательных элементов базового поля. | `baseField` (поле, определяющее порядок накопления) |
| `PERCENTAGE_OF_ROW` | Отображает значение как процент от итоговой суммы строки. | — |
| `PERCENTAGE_OF_COLUMN` | Отображает значение как процент от итоговой суммы столбца. | — |
| `PERCENTAGE_OF_TOTAL` | Отображает значение как процент от общего итога. | — |
| `INDEX` | Отображает значение по формуле Excel INDEX ((value * grand total) / (row total * column total)). | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Отображает значение как процент от родительского итога строки (для вложенных строковых полей). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Отображает значение как процент от родительского итога столбца (для вложенных столбцовых полей). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Отображает значение как процент от родительского итога. | `baseField` (базовое родительское поле) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Отображает значение как процент от накопительного итога в базовом поле. | `baseField` (поле накопления) |
| `RANK_SMALLEST_TO_LARGEST` | Присваивает ранг от наименьшего (1) к наибольшему. | — |
| `RANK_LARGEST_TO_SMALLEST` | Присваивает ранг от наибольшего (1) к наименьшему. | — |

{{% alert color="primary" %}}
`showValuesAs(...)` записывает настройки `PivotShowValuesSetting` (`setCalculationType()`, `setBaseFieldIndex()`, `setBaseItemPositionType()`, `setBaseItemIndex()`) — метод и объект настроек представляют два способа задать одно и то же состояние, аналогично выбору базового поля и базового элемента в диалоговом окне Show Values As Excel.
{{% /alert %}}

## **Отображение значений в виде процента от общего итога**
Вызовите метод `PivotField.showValuesAs()` с параметром `PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL`, чтобы преобразовать каждую ячейку поля данных, включая общий итог, в её долю от общего итога. Отображаемые числа тогда представляют собой пропорции полного набора результатов. Этот формат сравнивает каждое значение только с общим итогом, поэтому не требуется базовое поле или базовый элемент — завершающие аргументы (`0`, `PivotItemPositionType.PREVIOUS`, `0`) являются заполнителями, которые формат игнорирует, как указано в таблице параметров.

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
Считайте текущую конфигурацию через `PivotField.getShowValuesSetting()`: метод только для чтения возвращает объект `PivotShowValuesSetting` поля, где четыре настройки описывают активный расчёт Show Values As. Чтобы изменить конфигурацию, вызовите метод `PivotField.showValuesAs()` — он записывает все четыре настройки одним вызовом, поэтому вам не придётся задавать их по отдельности.  
Объект `PivotShowValuesSetting` раскрывает четыре настройки, которые записывает `showValuesAs()`:
- `getCalculationType()` / `setCalculationType()` выбирает вторичный расчёт `PivotFieldDataDisplayFormat`.  
- `getBaseFieldIndex()` / `setBaseFieldIndex()` задаёт нулевой индекс базового поля среди полей сводной таблицы. Используется базовыми форматами.  
- `getBaseItemPositionType()` / `setBaseItemPositionType()` определяет расположение базового элемента относительно текущего и принимает `PivotItemPositionType.NEXT`, `PivotItemPositionType.PREVIOUS` или `PivotItemPositionType.CUSTOM`.  
- `getBaseItemIndex()` / `setBaseItemIndex()` задаёт нулевой индекс базового элемента и используется, когда `getBaseItemPositionType()` установлен в `CUSTOM`.  
После вызова `showValuesAs()` вызовите `PivotTable.calculateData()` ещё раз, чтобы тело сводной таблицы было перерасчитано и отрисовано с обновлённой конфигурацией.

```javascript
const AsposeCells = require("aspose.cells");
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
- [Управление полями значений в сводной таблице](/cells/ru/nodejs-java/manage-value-fields/)
- [Обновление сводной таблицы](/cells/ru/nodejs-java/refresh-pivot-table/)
- [Применение стиля к сводной таблице](/cells/ru/nodejs-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}
---
title: Показать значения как в сводной таблице
linktitle: Показать значения как в сводной таблице
description: Отображайте значения полей данных сводной таблицы в виде процента от общего итога, разницы от базового элемента, накопительных итогов, рангов и др. с Aspose.Cells for Python via Java.
keywords: Aspose.Cells, сводная таблица, показать значения как, формат отображения данных, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, Python via Java
type: docs
weight: 145
url: /ru/python-java/show-values-as-in-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
Сводная таблица обычно агрегирует каждое поле данных с помощью функции агрегирования, такой как `Sum` или `Count`. Функция Excel **Show Values As** заменяет каждый отображаемый результат вторичным вычислением, полученным из этой агрегированной величины — например, процентом от общего итога, накопительным итогом, разницей от выбранного базового элемента или рангом — что позволяет проводить сравнительный анализ без вспомогательных формул или вычисляемых столбцов.  
Обычные применения включают анализ доли от общего итога (проценты по строке, столбцу или общему итогу), кумулятивные отчёты с использованием накопительного итога в поле периода, анализ отклонений относительно эталонного элемента (разница или процентная разница от базового элемента) и ранжирование значений от наименьшего к наибольшему или наоборот.  
В Aspose.Cells for Python via Java класс `PivotFieldDataDisplayFormat` выбирает вторичное вычисление. Метод только для чтения `PivotField.getShowValuesSetting()` возвращает объект `PivotShowValuesSetting`, свойства которого (`setCalculationType`, `setBaseFieldIndex`, `setBaseItemPositionType` и `setBaseItemIndex`) позволяют настроить поведение; удобный метод `PivotField.showValuesAs(...)` применяет те же четыре параметра одним вызовом. Применяйте эти настройки к полю данных или значений, полученному через `PivotTable.getDataFields()`.

## **Элементы перечисления PivotFieldDataDisplayFormat**
Поле данных сохраняет свою функцию агрегирования, например Sum или Count, тогда как Show Values As изменяет только способ отображения агрегированного значения.  
Помимо прямой установки свойств `PivotShowValuesSetting` (см. последний раздел), удобный однострочный метод применяет ту же конфигурацию:

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    PivotField,
    PivotFieldDataDisplayFormat,
    PivotItemPositionType,
)
def show_values_as(
    pivot_field: PivotField,
    display_format: PivotFieldDataDisplayFormat,
    base_field: int,
    base_item_position_type: PivotItemPositionType,
    base_item: int,
) -> None:
    pivot_field.showValuesAs(
        display_format,
        base_field,
        base_item_position_type,
        base_item,
    )
jpype.shutdownJVM()
```

| Параметр | Описание | Когда требуется |
| --- | --- | --- |
| `displayFormat` | Вторичное вычисление `PivotFieldDataDisplayFormat`, которое следует применить. | Всегда. |
| `baseField` | Индекс базового поля (нумерация с нуля) среди базовых полей сводной таблицы (например, индекс строкового поля, к которому относится базовый элемент). | Только шесть базовых форматов ниже (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfRunningTotalIn`, `PercentageOfParentTotal`); игнорируется всеми остальными форматами. |
| `baseItemPositionType` | Способ выбора базового элемента относительно текущего: `PivotItemPositionType.Previous`, `.Next` или `.Custom`. | Только три формата базового элемента (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`); игнорируется всеми остальными форматами. |
| `baseItem` | Индекс базового элемента (нумерация с нуля). | Только когда `baseItemPositionType` установлен в `Custom` (индекс выбирает точный базовый элемент); игнорируется при `Previous`/`Next` и всеми форматами, не использующими базовый элемент — передайте `0`. |

| Тип вычисления | Поведение | Параметры базового элемента |
| --- | --- | --- |
| `Normal` | Без вторичного вычисления; агрегированное значение отображается как есть (по умолчанию). | — |
| `DifferenceFrom` | Отображает значение как разницу от значения базового элемента в базовом поле. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` только при `Custom`) |
| `PercentageOf` | Отображает значение как процент от значения базового элемента в базовом поле. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` только при `Custom`) |
| `PercentageDifferenceFrom` | Отображает значение как процентную разницу от значения базового элемента в базовом поле. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` только при `Custom`) |
| `RunningTotalIn` | Отображает значение как накопительный итог для последовательных элементов базового поля. | `baseField` (поле, определяющее порядок элементов накопления) |
| `PercentageOfRow` | Отображает значение как процент от итога строки. | — |
| `PercentageOfColumn` | Отображает значение как процент от итога столбца. | — |
| `PercentageOfTotal` | Отображает значение как процент от общего итога. | — |
| `Index` | Отображает значение по формуле индекса Excel ((value * grand total) / (row total * column total)). | — |
| `PercentageOfParentRowTotal` | Отображает значение как процент от итога родительской строки (для вложенных строковых полей). | — |
| `PercentageOfParentColumnTotal` | Отображает значение как процент от итога родительского столбца (для вложенных столбцовых полей). | — |
| `PercentageOfParentTotal` | Отображает значение как процент от итога родительского уровня. | `baseField` (базовое родительское поле) |
| `PercentageOfRunningTotalIn` | Отображает значение как процент от накопительного итога в базовом поле. | `baseField` (поле накопления) |
| `RankSmallestToLargest` | Ранжирует значение от наименьшего (1) к наибольшему. | — |
| `RankLargestToSmallest` | Ранжирует значение от наибольшего (1) к наименьшему. | — |

{{% alert color="primary" %}}
`showValuesAs(...)` записывает значения `PivotShowValuesSetting` через `setCalculationType`, `setBaseFieldIndex`, `setBaseItemPositionType` и `setBaseItemIndex` — метод и объект настроек представляют два способа задать одно и то же состояние, аналогично выбору базового поля и базового элемента в диалоговом окне Excel **Show Values As**.
{{% /alert %}}

## **Показать значения как процент от общего итога**
Вызовите метод `PivotField.showValuesAs` с параметром `PivotFieldDataDisplayFormat.PercentageOfTotal`, чтобы преобразовать каждую ячейку поля данных, включая общий итог, в её долю от общего итога. Отображаемые числа будут представлять собой пропорции от полного набора результатов. Этот формат сравнивает каждое значение только с общим итогом, поэтому не требует указания базового поля или базового элемента — конечные аргументы (`0`, `PivotItemPositionType.Previous`, `0`) являются лишь заполняющими значениями, которые игнорируются форматом, как указано в таблице параметров.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import (
    Workbook,
    Worksheet,
    Cells,
    Range,
    SaveFormat,
    PivotTable,
    PivotField,
    PivotFieldType,
    PivotFieldDataDisplayFormat,
    PivotItemPositionType,
)
# Load or create a workbook with source data
workbook = Workbook()
data_sheet = workbook.getWorksheets().get(0)
data_sheet.getCells().get("A1").putValue("Fruit")
data_sheet.getCells().get("B1").putValue("Amount")
fruits = ["Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"]
amounts = [10, 20, 30, 40, 50, 60]
for i in range(len(fruits)):
    data_sheet.getCells().get(i + 1, 0).putValue(fruits[i])
    data_sheet.getCells().get(i + 1, 1).putValue(amounts[i])
# Add a pivot table on a new worksheet (getWorksheets().add() returns the sheet index)
pivot_sheet_index = workbook.getWorksheets().add()
pivot_table = workbook.getWorksheets().get(pivot_sheet_index).getPivotTables().add("=Sheet1!A1:B7", 2, 2)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.calculateData()
# Show the Amount data field as a percentage of the grand total with the
# one-call method; PercentageOfTotal takes no base item, so the trailing
# base arguments (0, Previous, 0) are placeholders the format ignores
data_field = pivot_table.getDataFields().get(0)
data_field.showValuesAs(
    PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL,
    0,
    PivotItemPositionType.PREVIOUS,
    0,
)
pivot_table.calculateData()
# Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx")
jpype.shutdownJVM()
```

## **Получить и настроить PivotField.getShowValuesSetting()**
Прочитайте текущую конфигурацию через `PivotField.getShowValuesSetting()`: метод только для чтения возвращает объект `PivotShowValuesSetting` поля, в котором находятся четыре свойства, описывающие активное вычисление **Show Values As**. Чтобы изменить конфигурацию, вызовите метод `PivotField.showValuesAs` — он записывает все четыре настройки за один вызов, поэтому нет необходимости задавать свойства по отдельности.  
Объект `PivotShowValuesSetting` раскрывает четыре свойства, которые записывает `showValuesAs`:
- `getCalculationType()` возвращает вторичное вычисление `PivotFieldDataDisplayFormat`, а `setCalculationType(...)` изменяет его.  
- `getBaseFieldIndex()` и `setBaseFieldIndex(...)` указывают индекс базового поля (нумерация с нуля) внутри полей сводной таблицы. Используется базовыми форматами.  
- `getBaseItemPositionType()` и `setBaseItemPositionType(...)` определяют расположение базового элемента относительно текущего и принимают значения `PivotItemPositionType.Next`, `PivotItemPositionType.Previous` или `PivotItemPositionType.Custom`.  
- `getBaseItemIndex()` и `setBaseItemIndex(...)` задают индекс базового элемента (нумерация с нуля) и используются, когда `BaseItemPositionType` установлен в `Custom`.  
После вызова `showValuesAs` снова вызовите `PivotTable.calculateData()`, чтобы тело сводной таблицы было пересчитано и перерисовано с обновлённой конфигурацией.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import (
    Workbook,
    Worksheet,
    Cells,
    Range,
    SaveFormat,
    PivotFieldDataDisplayFormat,
    PivotItemPositionType,
)
workbook = Workbook("ShowValuesAsPercentageOfTotal.xlsx")
pivot_table = workbook.getWorksheets().get(1).getPivotTables().get(0)
data_field = pivot_table.getDataFields().get(0)
# Read the current show-values settings
settings = data_field.getShowValuesSetting()
print(f"CalculationType: {settings.getCalculationType()}")
print(f"BaseFieldIndex: {settings.getBaseFieldIndex()}")
print(f"BaseItemPositionType: {settings.getBaseItemPositionType()}")
print(f"BaseItemIndex: {settings.getBaseItemIndex()}")
# Switch to a base-item calculation with the one-call method: difference
# from the value of the previous item in the row field
data_field.showValuesAs(
    PivotFieldDataDisplayFormat.DIFFERENCE_FROM,
    pivot_table.getRowFields().get(0).getBaseIndex(),
    PivotItemPositionType.PREVIOUS,
    0,
)
pivot_table.calculateData()
# Note: the percentage number format saved by the previous example still
# clings to the data field cells; the underlying values are now differences
# Re-read the applied configuration
print(f"CalculationType now: {data_field.getShowValuesSetting().getCalculationType()}")
workbook.save("ShowValuesAsDifferenceFrom.xlsx")
jpype.shutdownJVM()
```

## **Связанные статьи**
- [Управление полями значений в сводной таблице](/cells/ru/python-java/manage-value-fields/)
- [Обновление (Refresh) сводной таблицы](/cells/ru/python-java/refresh-pivot-table/)
- [Применение стиля к сводной таблице](/cells/ru/python-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python" >}}
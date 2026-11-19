---
title: Показать значения как в сводной таблице
linktitle: Показать значения как в сводной таблице
description: Отображать значения полей данных сводной таблицы в виде процента от общей суммы, разницы от базового элемента, накопительных итогов, рангов и др. с использованием Aspose.Cells for Python via Java.
keywords: Aspose.Cells, сводная таблица, показать значения как, PivotShowValuesAsType, PERCENTAGE_OF_TOTAL, PivotShowValuesSetting, showValuesAs, BaseFieldIndex, BaseItemIndex, Python
type: docs
weight: 145
url: /ru/python-java/show-values-as-in-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Варианты использования**
Сводная таблица обычно агрегирует каждое поле данных с помощью агрегирующей функции, такой как `SUM` или `COUNT`. Функция **Show Values As** в Excel заменяет каждый отображаемый результат вторичным вычислением, полученным из этой агрегирующей функции — например, процент от общей суммы, накопительный итог, разница от выбранного базового элемента или ранг — позволяя выполнять сравнительный анализ без вспомогательных формул или вычисляемых столбцов.  
Типичные применения включают анализ долей от общей суммы, включая проценты по строке, столбцу или общей сумме; построение кумулятивных отчётов с помощью накопительного итога в полевом периоде; анализ отклонений от эталона с использованием разницы или процентной разницы от базового элемента; а также ранжирование значений от меньшего к большему или наоборот.  
В Aspose.Cells for Python via Java перечисление `PivotShowValuesAsType` выбирает вторичное вычисление. Метод только для чтения `PivotField.getShowValuesSetting()` возвращает объект `PivotShowValuesSetting`, у которого методы `setShowValuesAs(...)`, `setBaseFieldIndex(...)` и `setBaseItemIndex(...)` настраивают поведение; удобный метод `PivotField.showValuesAs(...)` применяет те же настройки одним вызовом. Применяйте эти настройки к полю данных или значений, полученному через `PivotTable.getDataFields()`.

## **Элементы перечисления PivotShowValuesAsType**
Поле данных сохраняет свою агрегирующую функцию, такую как `SUM` или `COUNT`, тогда как Show Values As преобразует только способ отображения агрегированного значения.  
Помимо прямого использования сеттеров `PivotShowValuesSetting` (см. последний раздел), удобный одношаговый метод применяет ту же конфигурацию. Он доступен в двух формах — одна использует индексы базового поля и базового элемента, другая — их имена:

```python
from asposecells.api import PivotField, PivotShowValuesAsType
def show_values_as(
    pivot_field: PivotField,
    show_values_as_type: PivotShowValuesAsType,
    base_field: int,
    base_item: int,
):
    pivot_field.showValuesAs(show_values_as_type, base_field, base_item)

def show_values_as_by_name(
    pivot_field: PivotField,
    show_values_as_type: PivotShowValuesAsType,
    base_field: str,
    base_item: str,
):
    pivot_field.showValuesAs(show_values_as_type, base_field, base_item)
```

| Параметр | Значение | Требуется |
| --- | --- | --- |
| `show_values_as` | Вторичный расчёт `PivotShowValuesAsType`, который необходимо применить. | Всегда. |
| `base_field` | Нулевой‑базовый индекс базового поля среди базовых полей сводной таблицы (например, индекс строкового поля, к которому относится базовый элемент), либо — в форме имени — название базового поля. | Для восьми базово‑относительных форматов ниже (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `RANK_SMALLEST_TO_LARGEST`, `RANK_LARGEST_TO_SMALLEST`); для остальных форматов передайте `0` (или `None` в форме имени). |
| `base_item` | Нулевой‑базовый индекс базового элемента, с двумя метками‑сентинелами: `PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) выбирает предыдущий элемент, а `PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2) — следующий. В форме имени указывается подпись базового элемента, а `None` — когда выбранный формат не требует базового элемента. | Только три формата, использующие базовый элемент (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`) оценивают базовый элемент; пять форматов, зависящих от поля (`RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, оба ранга) игнорируют его — передайте `0` или `None`. |

| Тип расчёта | Поведение | Параметры базового элемента |
| --- | --- | --- |
| `NORMAL` | Нет вторичного расчёта; агрегированное значение отображается как есть (по умолчанию). | — |
| `DIFFERENCE_FROM` | Отображает значение как разницу от значения базового элемента в базовом поле. | `base_field` + `base_item` (индекс или подпись, либо метка предшествующего/следующего элемента) |
| `PERCENTAGE_OF` | Отображает значение как процент от значения базового элемента в базовом поле. | `base_field` + `base_item` (индекс или подпись, либо метка предшествующего/следующего элемента) |
| `PERCENTAGE_DIFFERENCE_FROM` | Отображает значение как процентную разницу от значения базового элемента в базовом поле. | `base_field` + `base_item` (индекс или подпись, либо метка предшествующего/следующего элемента) |
| `RUNNING_TOTAL_IN` | Отображает значение как накопительный итог для последовательных элементов базового поля. | `base_field` (поле, порядок элементов которого определяет накопление) |
| `PERCENTAGE_OF_ROW` | Отображает значение как процент от строки. | — |
| `PERCENTAGE_OF_COLUMN` | Отображает значение как процент от столбца. | — |
| `PERCENTAGE_OF_TOTAL` | Отображает значение как процент от общей суммы. | — |
| `INDEX` | Отображает значение по формуле Excel INDEX ((value * grand total) / (row total * column total)). | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Отображает значение как процент от родительской строки (для вложенных строковых полей). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Отображает значение как процент от родительского столбца (для вложенных столбцовых полей). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Отображает значение как процент от родительской суммы. | `base_field` (родительское поле, сумма которого используется в качестве ссылки) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Отображает значение как процент от накопительного итога в базовом поле. | `base_field` (поле накопления) |
| `RANK_SMALLEST_TO_LARGEST` | Ранжирует значение от наименьшего (1) к наибольшему. | `base_field` (поле, элементы которого определяют область ранжирования) |
| `RANK_LARGEST_TO_SMALLEST` | Ранжирует значение от наибольшего (1) к наименьшему. | `base_field` (поле, элементы которого определяют область ранжирования) |

{{% alert color="primary" %}}
`showValuesAs(...)` записывает значения `PivotShowValuesSetting` через `setShowValuesAs`, `setBaseFieldIndex` и `setBaseItemIndex` — метод и объект настройки представляют два способа конфигурировать одно и то же состояние, аналогично выборам базового поля и базового элемента в диалоговом окне Excel **Show Values As**.
{{% /alert %}}

## **Отображение значений как процент от общей суммы**
Вызовите метод `PivotField.showValuesAs` с параметром `PivotShowValuesAsType.PERCENTAGE_OF_TOTAL`, чтобы преобразовать каждую ячейку поля данных, включая общую сумму, в её долю от общей суммы. Отображаемые числа тем самым представляют собой долю от полного набора результатов. Этот формат сравнивает каждое значение только с общей суммой, поэтому не требуется базовое поле или базовый элемент — завершающие аргументы (`0`, `0`) являются заполнителями, которые формат игнорирует, как указано в таблице параметров выше.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    PivotFieldType,
    PivotShowValuesAsType,
)
# Load or create a workbook with source data
workbook = Workbook()
data_sheet = workbook.getWorksheets().get(0)
data_sheet.getCells().get("A1").putValue("Fruit")
data_sheet.getCells().get("B1").putValue("Amount")
fruits = ["Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"]
# float literals keep putValue on the double overload (an untyped Python int is ambiguous between putValue(boolean/int/Object) overloads)
amounts = [10.0, 20.0, 30.0, 40.0, 50.0, 60.0]
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
# one-call method; PERCENTAGE_OF_TOTAL takes no base item, so the trailing
# base arguments (0, 0) are placeholders the format ignores
data_field = pivot_table.getDataFields().get(0)
data_field.showValuesAs(PivotShowValuesAsType.PERCENTAGE_OF_TOTAL, 0, 0)
pivot_table.calculateData()
# Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx")
jpype.shutdownJVM()
```

## **Получение и настройка PivotField.getShowValuesSetting()**
Считайте текущую конфигурацию через `PivotField.getShowValuesSetting()`: метод только для чтения возвращает объект `PivotShowValuesSetting` поля, свойства которого описывают активный расчёт **Show Values As**. Чтобы изменить конфигурацию, вызовите метод `PivotField.showValuesAs` — он записывает все настройки одним вызовом, поэтому нет необходимости задавать свойства по отдельности.  
Объект `PivotShowValuesSetting` раскрывает состояние, которое записывает `showValuesAs`:
- `getShowValuesAs()` возвращает вторичный расчёт `PivotShowValuesAsType`, а `setShowValuesAs(...)` меняет его.
- `getBaseFieldIndex()` и `setBaseFieldIndex(...)` указывают нулевой‑базовый индекс базового поля среди полей сводной таблицы. Используется базово‑относительными форматами.
- `getBaseItemIndex()` и `setBaseItemIndex(...)` указывают базовый элемент: нулевой‑базовый индекс конкретного элемента сводной таблицы или одну из двух меток‑сентинелов — `PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) для предыдущего элемента, `PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2) для следующего. Используется форматами, зависящими от базового элемента.
- `getBaseFieldName()` и `getBaseItemCaption()` — только для чтения, предоставляют разрешённые названия базового поля и подпись базового элемента; например, после выбора сентинела предыдущего элемента `getBaseItemCaption()` возвращает `(previous)`.  
После вызова `showValuesAs` вызовите `PivotTable.calculateData()` повторно, чтобы тело сводной таблицы было пересчитано и перерисовано с обновлённой конфигурацией.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    PivotShowValuesAsType,
    PivotShowValuesSetting,
)
workbook = Workbook("ShowValuesAsPercentageOfTotal.xlsx")
pivot_table = workbook.getWorksheets().get(1).getPivotTables().get(0)
data_field = pivot_table.getDataFields().get(0)
# Read the current show-values settings
settings = data_field.getShowValuesSetting()
print(f"ShowValuesAs: {settings.getShowValuesAs()}")
print(f"BaseFieldIndex: {settings.getBaseFieldIndex()}")
print(f"BaseItemIndex: {settings.getBaseItemIndex()}")
print(f"BaseFieldName: {settings.getBaseFieldName()}")
print(f"BaseItemCaption: {settings.getBaseItemCaption()}")
# Switch to a base-item calculation with the one-call method: difference
# from the value of the previous item in the row field
data_field.showValuesAs(
    PivotShowValuesAsType.DIFFERENCE_FROM,
    pivot_table.getRowFields().get(0).getBaseIndex(),
    PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM,
)
pivot_table.calculateData()
# Note: the percentage number format saved by the previous example still
# clings to the data field cells; the underlying values are now differences
# Re-read the applied configuration
print(f"ShowValuesAs now: {data_field.getShowValuesSetting().getShowValuesAs()}")
workbook.save("ShowValuesAsDifferenceFrom.xlsx")
jpype.shutdownJVM()
```

## **Сопутствующие статьи**
- [Управление полями значений в сводной таблице](/cells/ru/python-java/manage-value-fields/)
- [Обновление сводной таблицы](/cells/ru/python-java/refresh-pivot-table/)
- [Применение стиля к сводной таблице](/cells/ru/python-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python" >}}
---
title: Отображение значений как в сводной таблице
linktitle: Отображение значений как в сводной таблице
description: Отображайте значения полей данных сводной таблицы в виде процента от общего итога, разницы от базового элемента, накопительных итогов, рангов и т.д. с помощью Aspose.Cells for Python via .NET.
keywords: Aspose.Cells, сводная таблица, отображение значений как, PivotShowValuesAsType, PERCENTAGE_OF_TOTAL, PivotShowValuesSetting, show_values_as, base_field_index, base_item_index, Python
type: docs
weight: 145
url: /ru/python-net/show-values-as-in-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
Сводная таблица обычно агрегирует **каждое поле данных** с помощью агрегирующей функции, такой как `SUM` или `COUNT`. Функция Excel **Show Values As** заменяет каждый отображаемый результат вторичным расчётом, полученным из этой агрегированной величины — например, процент от общего итога, накопительный итог, разницу от выбранного базового элемента или ранг — что позволяет выполнять сравнительный анализ без вспомогательных формул или вычисляемых столбцов.  
Типичные применения включают анализ доли от общего итога (процент строки, столбца или общего итога); накопительные отчёты с помощью текущего (накопительного) итога в поле периода; анализ отклонений от эталонного элемента с помощью разницы или процентной разницы от базового элемента; а также ранжирование значений от наименьшего к наибольшему или наоборот.  
В Aspose.Cells for Python via .NET перечисление `PivotShowValuesAsType` выбирает вторичный расчёт. Свойство только для чтения `PivotField.show_values_setting` возвращает объект `PivotShowValuesSetting`, у которого записываемые свойства `show_values_as`, `base_field_index` и `base_item_index` задают поведение; удобный метод `PivotField.show_values_as(...)` применяет те же настройки одним вызовом. Применяйте эти настройки к полю данных или значений, полученному из `PivotTable.data_fields`.

## **Перечисление PivotShowValuesAsType**
Поле данных сохраняет свою агрегирующую функцию, например `SUM` или `COUNT`, тогда как Show Values As изменяет только способ отображения агрегированного значения.  
Помимо прямой записи свойств `PivotShowValuesSetting` (см. последний раздел), удобный метод в один вызов применяет ту же конфигурацию. Он доступен в двух формах — одна принимает базовое поле и базовый элемент по индексу, другая — по имени:

```python
from aspose.cells.pivot import PivotField, PivotShowValuesAsType
def show_values_as(
    pivot_field: PivotField,
    show_values_as_type: PivotShowValuesAsType,
    base_field: int,
    base_item: int,
) -> None:
    pivot_field.show_values_as(
        show_values_as_type,
        base_field,
        base_item,
    )

def show_values_as_by_name(
    pivot_field: PivotField,
    show_values_as_type: PivotShowValuesAsType,
    base_field: str,
    base_item: str,
) -> None:
    pivot_field.show_values_as(
        show_values_as_type,
        base_field,
        base_item,
    )
```

| Параметр | Значение | Когда требуется |
| --- | --- | --- |
| `show_values_as_type` | Вторичный расчёт `PivotShowValuesAsType`, который следует применить. | Всегда. |
| `base_field` | Нулевой индекс базового поля среди базовых полей сводной таблицы (например, индекс поля строки, к которому принадлежит базовый элемент), или — в форме по имени — имя базового поля. | Для восьми базово‑относительных форматов ниже (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `RANK_SMALLEST_TO_LARGEST`, `RANK_SMALLEST_TO_LARGEST`); для остальных форматов передайте `0` (или `None` в форме по имени). |
| `base_item` | Нулевой индекс базового элемента, с двумя специальными значениями: `PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) выбирает предыдущий элемент, а `PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2) — следующий. В форме по имени используется подпись базового элемента, а `None`, если выбранный формат не требует базового элемента. | Только три формата, зависящие от базового элемента (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`) используют базовый элемент; пять форматов, зависящих от базового поля (`RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, оба ранга) игнорируют его — передайте `0` или `None`. |

| Тип расчёта | Поведение | Параметры базового элемента |
| --- | --- | --- |
| `NORMAL` | Нет вторичного расчёта; отображается агрегированное значение без изменений (по умолчанию). | — |
| `DIFFERENCE_FROM` | Отображает значение как разницу от значения базового элемента в базовом поле. | `base_field` + `base_item` (индекс или подпись, либо специальный маркер предыдущий/следующий) |
| `PERCENTAGE_OF` | Отображает значение как процент от значения базового элемента в базовом поле. | `base_field` + `base_item` (индекс или подпись, либо специальный маркер предыдущий/следующий) |
| `PERCENTAGE_DIFFERENCE_FROM` | Отображает значение как процентную разницу от значения базового элемента в базовом поле. | `base_field` + `base_item` (индекс или подпись, либо специальный маркер предыдущий/следующий) |
| `RUNNING_TOTAL_IN` | Отображает значение как текущий суммарный итог для последовательных элементов базового поля. | `base_field` (поле, определяющее порядок накопления) |
| `PERCENTAGE_OF_ROW` | Отображает значение как процент от суммы строки. | — |
| `PERCENTAGE_OF_COLUMN` | Отображает значение как процент от суммы столбца. | — |
| `PERCENTAGE_OF_TOTAL` | Отображает значение как процент от общего итога. | — |
| `INDEX` | Отображает значение по формуле Excel INDEX ((value * grand total) / (row total * column total)). | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Отображает значение как процент от родительского итога строки (для вложенных полей строк). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Отображает значение как процент от родительского итога столбца (для вложенных полей столбцов). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Отображает значение как процент от родительского итога. | `base_field` (родительское поле, чей итог используется в качестве ссылки) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Отображает значение как процент от текущего суммарного итога в базовом поле. | `base_field` (поле накопления) |
| `RANK_SMALLEST_TO_LARGEST` | Присваивает ранги от наименьшего (1) к наибольшему. | `base_field` (поле, элементы которого определяют диапазон ранжирования) |
| `RANK_LARGEST_TO_SMALLEST` | Присваивает ранги от наибольшего (1) к наименьшему. | `base_field` (поле, элементы которого определяют диапазон ранжирования) |

{{% alert color="primary" %}}
`show_values_as(...)` записывает свойства объекта `PivotShowValuesSetting` (`show_values_as`, `base_field_index`, `base_item_index`) — метод и объект‑свойство представляют два способа конфигурировать одно и то же состояние, аналогично элементам выбора базового поля и базового элемента в диалоговом окне Excel **Show Values As**.
{{% /alert %}}

## **Отображение значений как процент от общего итога**
Вызовите метод `PivotField.show_values_as` с параметром `PivotShowValuesAsType.PERCENTAGE_OF_TOTAL`, чтобы преобразовать каждую ячейку поля данных, включая общий итог, в её долю от общего итога. Отображаемые числа тогда представляют собой доли полного набора результатов. Этот формат сравнивает каждое значение только с общим итогом, поэтому не требует указания базового поля или базового элемента — завершающие аргументы (`0`, `0`) являются заполнителями, которые формат игнорирует, как указано в таблице параметров выше.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType, PivotShowValuesAsType
# Load or create a workbook with source data
workbook = ac.Workbook()
data_sheet = workbook.worksheets[0]
data_sheet.cells.get("A1").put_value("Fruit")
data_sheet.cells.get("B1").put_value("Amount")
fruits = ["Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"]
amounts = [10, 20, 30, 40, 50, 60]
for i in range(len(fruits)):
    data_sheet.cells.get(i + 1, 0).put_value(fruits[i])
    data_sheet.cells.get(i + 1, 1).put_value(amounts[i])
# Add a pivot table on a new worksheet (worksheets.add() returns the sheet index)
pivot_sheet_index = workbook.worksheets.add()
pivot_table = workbook.worksheets[pivot_sheet_index].pivot_tables.add("=Sheet1!A1:B7", 2, 2)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
# Show the Amount data field as a percentage of the grand total with the
# one-call method; PercentageOfTotal takes no base item, so the trailing
# base arguments (0, 0) are placeholders the format ignores
data_field = pivot_table.data_fields[0]
data_field.show_values_as(PivotShowValuesAsType.PERCENTAGE_OF_TOTAL, 0, 0)
pivot_table.calculate_data()
# Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx")
```

## **Получение и настройка PivotField.show_values_setting**
Прочитайте текущую конфигурацию через `PivotField.show_values_setting`: свойство только для чтения возвращает объект `PivotShowValuesSetting` поля, свойства которого описывают активный расчёт **Show Values As**. Чтобы изменить конфигурацию, вызовите метод `PivotField.show_values_as` — он записывает все настройки одним вызовом, поэтому нет необходимости присваивать свойства по отдельности.  
Объект `PivotShowValuesSetting` раскрывает состояние, записываемое `show_values_as`:
- `show_values_as` выбирает вторичный расчёт `PivotShowValuesAsType`.
- `base_field_index` указывает нулевой индекс базового поля среди полей сводной таблицы. Он используется базово‑относительными форматами.
- `base_item_index` указывает базовый элемент: нулевой индекс конкретного элемента сводной таблицы или один из двух специальных маркеров — `PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) для предыдущего элемента, `PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2) для следующего. Он используется базово‑элементными форматами.
- `base_field_name` и `base_item_caption` — только для чтения, показывают разрешённое имя базового поля и подпись базового элемента; например, после выбора маркера предыдущего элемента `base_item_caption` возвращает `(previous)`.  
После вызова `show_values_as` вызовите `PivotTable.calculate_data()` ещё раз, чтобы тело сводной таблицы пересчиталось и перерисовалось с обновлённой конфигурацией.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType, PivotShowValuesAsType, PivotShowValuesSetting
workbook = ac.Workbook("ShowValuesAsPercentageOfTotal.xlsx")
pivot_table = workbook.worksheets[1].pivot_tables[0]
data_field = pivot_table.data_fields[0]
# Read the current show-values settings
settings = data_field.show_values_setting
print(f"ShowValuesAs: {settings.show_values_as}")
print(f"BaseFieldIndex: {settings.base_field_index}")
print(f"BaseItemIndex: {settings.base_item_index}")
print(f"BaseFieldName: {settings.base_field_name}")
print(f"BaseItemCaption: {settings.base_item_caption}")
# Switch to a base-item calculation with the one-call method: difference
# from the value of the previous item in the row field
data_field.show_values_as(
    PivotShowValuesAsType.DIFFERENCE_FROM,
    pivot_table.row_fields[0].base_index,
    PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM
)
pivot_table.calculate_data()
# Note: the percentage number format saved by the previous example still
# clings to the data field cells; the underlying values are now differences
# Re-read the applied configuration
print(f"ShowValuesAs now: {data_field.show_values_setting.show_values_as}")
workbook.save("ShowValuesAsDifferenceFrom.xlsx")
```

## **Сопутствующие статьи**
- [Управление полями значений в сводной таблице](/cells/ru/python-net/manage-value-fields/)
- [Обновление сводной таблицы](/cells/ru/python-net/refresh-pivot-table/)
- [Применение стиля к сводной таблице](/cells/ru/python-net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python-net" >}}
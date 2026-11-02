---
title: Показать значения как в сводной таблице
linktitle: Показать значения как в сводной таблице
description: Отображайте значения полей данных сводной таблицы в виде процента от общего итога, разницы от базового элемента, накопительных итогов, рангов и т.д. с помощью Aspose.Cells for Python via .NET.
keywords: Aspose.Cells for Python via .NET, сводная таблица, показать значения как, формат отображения данных, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, Python
type: docs
weight: 145
url: /ru/python-net/show-values-as-in-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
Сводная таблица обычно агрегирует каждое поле данных с помощью функции агрегирования, такой как `SUM` или `COUNT`. Функция Excel **Show Values As** заменяет каждый отображаемый результат вторичным вычислением, полученным из этой агрегированной величины — например, процент от общего итога, накопительный итог, разница от выбранного базового элемента или ранжирование — позволяя проводить сравнительный анализ без вспомогательных формул или вычисляемых столбцов.  
Типичные применения включают анализ доли от общего итога (процент от строки, столбца или общего итога), накопительный отчёт с использованием накопительного итога в периодическом поле, анализ отклонений от эталонного элемента с помощью разницы или процентной разницы, а также ранжирование значений от наименьшего к наибольшему или наоборот.  
В Aspose.Cells for Python via .NET объект `PivotFieldDataDisplayFormat` выбирает вторичное вычисление. Свойство только для чтения `PivotField.show_values_setting` возвращает объект `PivotShowValuesSetting`, а его записываемые свойства `calculation_type`, `base_field_index`, `base_item_position_type` и `base_item_index` конфигурируют поведение; удобный метод `PivotField.show_values_as(...)` применяет те же четыре параметра одним вызовом. Применяйте эти настройки к полю данных или значений, полученному из `PivotTable.data_fields`.

## **Элементы перечисления PivotFieldDataDisplayFormat**
Поле данных сохраняет свою функцию агрегирования, например `SUM` или `COUNT`, тогда как Show Values As изменяет только способ отображения агрегированного значения.  
Помимо прямой записи свойств `PivotShowValuesSetting` (см. последний раздел), удобный метод, вызываемый один раз, задает ту же конфигурацию:

```python
from aspose.cells.pivot import PivotField, PivotFieldDataDisplayFormat, PivotItemPositionType
def show_values_as(
    pivot_field: PivotField,
    display_format: PivotFieldDataDisplayFormat,
    base_field: int,
    base_item_position_type: PivotItemPositionType,
    base_item: int,
) -> None:
    pivot_field.show_values_as(
        display_format,
        base_field,
        base_item_position_type,
        base_item,
    )
```

| Параметр | Описание | Когда требуется |
| --- | --- | --- |
| `display_format` | Вторичное вычисление `PivotFieldDataDisplayFormat`, которое необходимо применить. | Всегда. |
| `base_field` | Нулевой индекс базового поля среди базовых полей сводной таблицы (например, индекс строкового поля, к которому относится базовый элемент). | Только шесть базовых форматов ниже (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`); игнорируется всеми остальными форматами. |
| `base_item_position_type` | Как выбирается базовый элемент относительно текущего: `PivotItemPositionType.PREVIOUS`, `.NEXT` или `.CUSTOM`. | Только три формата базового элемента (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`); игнорируется всеми остальными форматами. |
| `base_item` | Нулевой индекс базового элемента. | Только когда `base_item_position_type` установлен в `CUSTOM` (тогда индекс определяет точный базовый элемент); для `PREVIOUS`/`NEXT` и всех не‑базовых форматов передайте `0`. |

| Тип вычисления | Поведение | Параметры базового элемента |
| --- | --- | --- |
| `NORMAL` | Нет вторичного вычисления; агрегированное значение отображается как есть (по умолчанию). | — |
| `DIFFERENCE_FROM` | Показывает значение как разницу от значения базового элемента в базовом поле. | `base_field` + `PREVIOUS`/`NEXT`/`CUSTOM` (`base_item` только при `CUSTOM`) |
| `PERCENTAGE_OF` | Показывает значение как процент от значения базового элемента в базовом поле. | `base_field` + `PREVIOUS`/`NEXT`/`CUSTOM` (`base_item` только при `CUSTOM`) |
| `PERCENTAGE_DIFFERENCE_FROM` | Показывает значение как процентную разницу от значения базового элемента в базовом поле. | `base_field` + `PREVIOUS`/`NEXT`/`CUSTOM` (`base_item` только при `CUSTOM`) |
| `RUNNING_TOTAL_IN` | Показывает значение как накопительный итог для последовательных элементов базового поля. | `base_field` (поле, определяющее порядок накопления) |
| `PERCENTAGE_OF_ROW` | Показывает значение как процент от суммы строки. | — |
| `PERCENTAGE_OF_COLUMN` | Показывает значение как процент от суммы столбца. | — |
| `PERCENTAGE_OF_TOTAL` | Показывает значение как процент от общего итога. | — |
| `INDEX` | Показывает значение по формуле Excel INDEX ((value * grand total) / (row total * column total)). | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Показывает значение как процент от итога родительской строки (для вложенных строковых полей). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Показывает значение как процент от итога родительского столбца (для вложенных столбцовых полей). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Показывает значение как процент от итога его родительского уровня. | `baseField` (базовое родительское поле) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Показывает значение как процент от накопительного итога в базовом поле. | `base_field` (поле накопления) |
| `RANK_SMALLEST_TO_LARGEST` | Ранжирует значение от наименьшего (1) к наибольшему. | — |
| `RANK_LARGEST_TO_SMALLEST` | Ранжирует значение от наибольшего (1) к наименьшему. | — |

{{% alert color="primary" %}}
`show_values_as(...)` записывает свойства `PivotShowValuesSetting` (`calculation_type`, `base_field_index`, `base_item_position_type`, `base_item_index`) — метод и объект свойства представляют два способа настройки одинакового состояния, аналогично выборам базового поля и базового элемента в диалоговом окне Excel **Show Values As**.
{{% /alert %}}

## **Отображение значений в виде процента от общего итога**
Вызовите метод `PivotField.show_values_as` с параметром `PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL`, чтобы преобразовать каждую ячейку поля данных, включая общую итоговую ячейку, в её долю от общего итога. Отображаемые числа будут представлять собой пропорции полного набора результатов. Этот формат сравнивает каждое значение только с общим итогом, поэтому не требует указания базового поля или базового элемента — конечные аргументы (`0`, `PivotItemPositionType.PREVIOUS`, `0`) являются заполнителями, которые формат игнорирует, как указано в таблице параметров выше.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldDataDisplayFormat, PivotFieldType, PivotItemPositionType
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
# base arguments (0, Previous, 0) are placeholders the format ignores
data_field = pivot_table.data_fields[0]
data_field.show_values_as(
    PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL,
    0,
    PivotItemPositionType.PREVIOUS,
    0,
)
pivot_table.calculate_data()
# Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx")
```

## **Получить и настроить PivotField.show_values_setting**
Прочитайте текущую конфигурацию через `PivotField.show_values_setting`: свойство только для чтения возвращает объект `PivotShowValuesSetting`, у которого четыре свойства описывают текущую вычисляемую настройку Show Values As. Чтобы изменить конфигурацию, вызовите метод `PivotField.show_values_as` — он записывает все четыре настройки одним вызовом, поэтому нет необходимости задавать свойства по отдельности.  
Объект `PivotShowValuesSetting` раскрывает четыре свойства, которые записывает `show_values_as`:
- `calculation_type` выбирает вторичное вычисление `PivotFieldDataDisplayFormat`.
- `base_field_index` указывает нулевой индекс базового поля среди полей сводной таблицы. Используется базовыми форматами.
- `base_item_position_type` определяет позицию базового элемента относительно текущего и принимает значения `PivotItemPositionType.NEXT`, `PivotItemPositionType.PREVIOUS` или `PivotItemPositionType.CUSTOM`.
- `base_item_index` задаёт нулевой индекс базового элемента и используется, когда `base_item_position_type` установлен в `CUSTOM`.  
После вызова `show_values_as` снова вызовите `PivotTable.calculate_data()`, чтобы тело сводной таблицы было пересчитано и переотображено с обновлённой конфигурацией.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldDataDisplayFormat, PivotFieldType, PivotItemPositionType
workbook = ac.Workbook("ShowValuesAsPercentageOfTotal.xlsx")
pivot_table = workbook.worksheets[1].pivot_tables[0]
data_field = pivot_table.data_fields[0]
# Read the current show-values settings
settings = data_field.show_values_setting
print(f"CalculationType: {settings.calculation_type}")
print(f"BaseFieldIndex: {settings.base_field_index}")
print(f"BaseItemPositionType: {settings.base_item_position_type}")
print(f"BaseItemIndex: {settings.base_item_index}")
# Switch to a base-item calculation with the one-call method: difference
# from the value of the previous item in the row field
data_field.show_values_as(
    PivotFieldDataDisplayFormat.DIFFERENCE_FROM,
    pivot_table.row_fields[0].base_index,
    PivotItemPositionType.PREVIOUS,
    0
)
pivot_table.calculate_data()
# Note: the percentage number format saved by the previous example still
# clings to the data field cells; the underlying values are now differences
# Re-read the applied configuration
print(f"CalculationType now: {data_field.show_values_setting.calculation_type}")
workbook.save("ShowValuesAsDifferenceFrom.xlsx")
```

## **Связанные статьи**
- [Управление полями значений в сводной таблице](/cells/ru/python-net/manage-value-fields/)
- [Обновление сводной таблицы](/cells/ru/python-net/refresh-pivot-table/)
- [Применение стиля к сводной таблице](/cells/ru/python-net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python-net" >}}
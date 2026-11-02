---
title: Отображение или фильтрация топ-10 в сводной таблице
linktitle: Отображение или фильтрация топ-10 в сводной таблице
description: Узнайте, как отображать только элементы поля сводной таблицы с наивысшим или наименьшим рейтингом в Aspose.Cells for Python с помощью .NET. В этой статье рассматриваются метод top_10_auto_show для Excel 97-2003, чтение параметров с помощью top_10_auto_show_settings и фильтр «Топ-10» для Excel 2007-365 с помощью filter_top10.
keywords: Aspose.Cells, Python с помощью .NET, сводная таблица, топ-10, автопоказ, top_10_auto_show, top_10_auto_show_settings, PivotFieldTop10AutoShowSettings, filter_top10, PivotFilterType, PivotField, Python
type: docs
weight: 20
url: /ru/python-net/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
Сводная таблица, в которой перечислены все элементы поля строки, может быть неудобна для чтения, если это поле содержит десятки элементов. Отчет «Топ-10» оставляет только элементы с наивысшим или наименьшим рейтингом — именно то, что требуется для рейтинговых отчетов, например «5 товаров с наибольшей выручкой» или «3 региона с наименьшим количеством продаж». Aspose.Cells поддерживает два механизма, соответствующих двум поколениям Microsoft Excel.
- **Автопоказ Excel 97-2003** — метод `PivotField.top_10_auto_show()`. Это классическая настройка «Показать N верхних/нижних элементов», которая хранится непосредственно в поле сводной таблицы. Она работает во всех версиях Excel, как старых, так и новых, поскольку является частью исходного формата сводной таблицы.
- **Фильтр «Топ-10» Excel 2007-365** — метод `PivotField.filter_top10()`. Это современный фильтр значений «Топ-10», доступный в меню поля в разделе «Фильтры значений». Он хранится в виде объекта `PivotFilter`, присоединенного к полю, и поддерживает варианты на основе количества элементов и процентов.

## **Отображение топ-10 в Excel 97-2003 (top_10_auto_show)**
Классический автопоказ настраивается одним вызовом `PivotField.top_10_auto_show(bool is_auto_show, bool is_top, int count, int rank_by)`:
- `is_auto_show` — включает или отключает автопоказ в поле.
- `is_top` — `True` оставляет элементы с наивысшим рейтингом (верхние), `False` — с наименьшим (нижние).
- `count` — количество элементов, которые следует оставить, например 10 для классического отчета «Топ-10».
- `rank_by` — индекс (с нуля) **поля данных**, значения которого определяют рейтинг элементов. Передайте значение -1, чтобы ранжировать элементы по самому полю.
Ранжирование может выполняться по полю значений или по самому полю. Ниже показаны два варианта.

### **Ранжирование по полю значений**
Ранжируйте элементы поля строки по обычному полю значений, например «Сумма продаж». Следующий пример создает сводную таблицу с одним полем строки (`Sport`) и одним полем данных (`Sales`), после чего отображает 2 вида спорта с наибольшим объемом продаж. `rank_by` равен 0, поскольку «Сумма продаж» является полем данных с индексом 0.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Sport")
worksheet.cells.get("B1").put_value("Quarter")
worksheet.cells.get("C1").put_value("Sales")
sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
row = 2
for sport in sports:
    for quarter in range(1, 4):
        worksheet.cells.get(row, 0).put_value(sport)
        worksheet.cells.get(row, 1).put_value("Qtr" + str(quarter))
        worksheet.cells.get(row, 2).put_value(1000 + 777 * row)
        row += 1
pivot_table = worksheet.pivot_tables.add("A1:C16", 2, 5)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Sport")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Sales")
pivot_table.calculate_data()
sport_field = pivot_table.row_fields[0]
# Показать 2 верхних элемента, ранжированных по "Sum of Sales" (индекс поля данных 0)
sport_field.top_10_auto_show(True, True, 2, 0)
pivot_table.calculate_data()
workbook.save("output-top10-by-value-field.xlsx")
```

### **Ранжирование по самому полю**
Ранжирование может выполняться и по самому полю — в этом случае передайте -1 в качестве `rank_by`. Дополнительное поле данных для этого варианта не требуется; достаточно разместить поле в области строк (или столбцов). Следующий пример показывает 3 вида спорта с наименьшим рейтингом при ранжировании по самому полю. При сохранении этой настройки атрибут `rank_by` исключается из XML сводной таблицы, поскольку -1 является значением по умолчанию для данного формата, а `top_10_auto_show_settings.rank_by` при чтении возвращает -1.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Sport")
worksheet.cells.get("B1").put_value("Quarter")
worksheet.cells.get("C1").put_value("Sales")
sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
row = 2
for sport in sports:
    for quarter in range(1, 4):
        worksheet.cells.get(row, 0).put_value(sport)
        worksheet.cells.get(row, 1).put_value("Qtr" + str(quarter))
        worksheet.cells.get(row, 2).put_value(1000 + 777 * row)
        row += 1
pivot_table = worksheet.pivot_tables.add("A1:C16", 2, 5)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Sport")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Sales")
pivot_table.calculate_data()
sport_field = pivot_table.row_fields[0]
sport_field.top_10_auto_show(True, False, 3, -1)
pivot_table.calculate_data()
workbook.save("output-top10-by-field-itself.xlsx")
```

## **Чтение текущих параметров (top_10_auto_show_settings)**
Свойство `PivotField.top_10_auto_show_settings` возвращает объект `PivotFieldTop10AutoShowSettings`, предоставляющий текущие параметры автопоказа, сохраненные в поле. С его помощью можно проверить, как будут отображаться элементы существующей рабочей книги (в том числе загруженной из файла) или только что настроенной сводной таблицы.

```python
import aspose.cells as ac
workbook = ac.Workbook("output-top10-by-value-field.xlsx")
pivot_table = workbook.worksheets[0].pivot_tables[0]
sport_field = pivot_table.row_fields[0]
settings = sport_field.top_10_auto_show_settings
print("AutoShow enabled: " + str(settings.is_auto_show))
print("Direction: " + ("Top" if settings.is_top else "Bottom"))
print("Item count: " + str(settings.auto_show_count))
print("Ranking data field index: " + str(settings.rank_by))
```

Четыре свойства соответствуют классическим атрибутам автопоказа, записываемым в XML сводной таблицы (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`), поэтому при чтении возвращаются именно те значения, которые учитываются всеми версиями Excel.

## **Примечание**

{{% alert color="primary" %}}
- Прямые свойства `PivotField`: `is_auto_show`, `is_ascend_show`, `auto_show_count` и `auto_show_field` помечены как устаревшие. Вместо них используйте объект `top_10_auto_show_settings`: `is_auto_show` заменяется на `top_10_auto_show_settings.is_auto_show`, `is_ascend_show` — на `top_10_auto_show_settings.is_top`, `auto_show_count` — на `top_10_auto_show_settings.auto_show_count`, а `auto_show_field` — на `top_10_auto_show_settings.rank_by`. Для изменения настроек используйте поддерживаемый метод `top_10_auto_show()`.
- `top_10_auto_show` работает с полями строк и столбцов. Поле, находящееся только в области страницы (фильтра), нельзя ранжировать таким способом, поскольку его элементы не расположены в основной части сводной таблицы.
{{% /alert %}}

## **Excel 2007-365: фильтр «Топ-10» (filter_top10)**
В современных версиях Excel фильтр «Топ-10» доступен в меню поля (в разделе «Фильтры значений», пункт «Топ-10...»). В Aspose.Cells этот фильтр реализован методом `PivotField.filter_top10(int value_field_index, PivotFilterType type, bool is_top, int item_count)`, который создает и возвращает объект `PivotFilter`:
- `value_field_index` — индекс (с нуля) поля данных, агрегированные значения которого используются для ранжирования элементов.
- `type` — определяет смысл `item_count`. `PivotFilterType.COUNT` оставляет фиксированное количество элементов (вариант «Элементы» в диалоговом окне). `PivotFilterType.PERCENT` оставляет заданный процент элементов, поэтому `item_count` задает сам процент: значение 30 оставляет верхние 30% элементов. `PivotFilterType.SUM` ранжирует элементы по накопленному покрытию значений.
- `is_top` — `True` для верхних элементов, `False` для нижних.
- `item_count` — значение N в выражении «Топ N»; его единица измерения зависит от `type`.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType, PivotFilterType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Sport")
worksheet.cells.get("B1").put_value("Quarter")
worksheet.cells.get("C1").put_value("Sales")
sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
row = 2
for sport in sports:
    for quarter in range(1, 4):
        worksheet.cells.get(row, 0).put_value(sport)
        worksheet.cells.get(row, 1).put_value("Qtr" + str(quarter))
        worksheet.cells.get(row, 2).put_value(1000 + 777 * row)
        row += 1
pivot_table = worksheet.pivot_tables.add("A1:C16", 2, 5)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Sport")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Sales")
pivot_table.calculate_data()
sport_field = pivot_table.row_fields[0]
# Фильтр топ-10 — оставить 2 верхних элемента по значению «Сумма продаж» (индекс поля данных 0)
filter = sport_field.filter_top10(0, PivotFilterType.COUNT, True, 2)
# Для фильтра на основе процентов вместо этого оставьте 30 процентов элементов:
# sport_field.filter_top10(0, PivotFilterType.PERCENT, True, 30)
pivot_table.pivot_cache.refresh()
pivot_table.calculate_data()
workbook.save("output-top10-filter.xlsx")
```

{{% alert color="primary" %}}
`top_10_auto_show` и `filter_top10` — две отдельные возможности. Автопоказ записывает классический атрибут `autoShow` в поле сводной таблицы и учитывается всеми версиями Excel, начиная с Excel 97. `filter_top10` записывает современную запись `PivotFilter`, для которой требуется Excel 2007 или более поздняя версия. Если рабочую книгу открыть в более старой версии Excel, сводная таблица с современным фильтром будет отображать все элементы. Для документов, которые должны сохраняться и затем повторно открываться в устаревших инструментах, предпочтителен `top_10_auto_show`; для современных рабочих книг предпочтителен `filter_top10`, поскольку он может применяться вместе с другими фильтрами значений.
{{% /alert %}}

## **Связанные статьи**
- [Фильтрация сводных таблиц по метке или значению](/cells/ru/python-net/filter-by-label-or-value-of-pivot-table/)
- [Добавление полей строки и столбца в сводную таблицу](/cells/ru/python-net/pivot-table-add-row-and-column-fields/)
- [Группировка полей сводной таблицы](/cells/ru/python-net/group-pivot-fields-in-the-pivot-table/)
- [Обновление сводной таблицы](/cells/ru/python-net/refresh-pivot-table/)
- [Добавление поля страницы в сводную таблицу](/cells/ru/python-net/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="python-net" >}}
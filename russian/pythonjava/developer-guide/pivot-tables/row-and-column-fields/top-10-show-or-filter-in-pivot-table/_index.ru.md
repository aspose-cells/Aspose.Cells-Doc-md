---
title: Отображение или фильтрация топ-10 в сводной таблице
linktitle: Отображение или фильтрация топ-10 в сводной таблице
description: Узнайте, как с помощью Aspose.Cells for Python via Java отображать только элементы с наивысшим или низшим рейтингом в поле сводной таблицы. В этой статье рассматриваются метод top10AutoShow для Excel 97-2003, чтение параметров с помощью Top10AutoShowSettings, а также фильтр «Топ-10» для Excel 2007-365 с помощью filterTop10.
keywords: Aspose.Cells for Python via Java, сводная таблица, топ-10, автопоказ, top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, filterTop10, PivotFilterType, PivotField, Python
type: docs
weight: 20
url: /ru/python-java/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
Сводная таблица, в которой перечислены все элементы поля строки, может быть сложной для восприятия, если поле содержит десятки элементов. Отчёт «Топ-10» оставляет только элементы с наивысшим или низшим рейтингом — именно это и требуется для отчётов с ранжированием, например «5 товаров с наибольшей выручкой» или «3 региона с наименьшим количеством продаж». Aspose.Cells поддерживает два механизма, соответствующих двум поколениям Microsoft Excel.
- **Автопоказ в Excel 97-2003** — метод `PivotField.top10AutoShow()`. Это классическая настройка «Показать верхние/нижние N элементов», которая хранится непосредственно в поле сводной таблицы. Она работает во всех версиях Excel, как в старых, так и в новых, поскольку входит в исходный формат сводной таблицы.
- **Фильтр топ-10 в Excel 2007-365** — метод `PivotField.filterTop10()`. Это современный фильтр значений «Топ-10», доступный в меню поля в разделе «Фильтры значений». Он хранится в виде объекта `PivotFilter`, связанного с полем, и поддерживает ранжирование на основе количества элементов или процента.

## **Отображение топ-10 в Excel 97-2003 (top10AutoShow)**
Классический автопоказ настраивается одним вызовом метода `PivotField.top10AutoShow(boolean isAutoShow, boolean isTop, int count, int rankBy)`:
- `isAutoShow` — включает или отключает параметр автопоказа в поле.
- `isTop` — `True` оставляет элементы с наивысшим рейтингом, а `False` — элементы с низким рейтингом.
- `count` — количество оставляемых элементов, например 10 для классического отчёта «Топ-10».
- `rankBy` — индекс (с нуля) **поля данных**, значения которого определяют рейтинг элементов. Передайте значение -1, чтобы ранжировать элементы по самому полю.
Ранжирование может выполняться по полю значений или по самому полю. Ниже приведены два варианта.

### **Ранжирование по полю значений**
Ранжируйте элементы поля строки по обычному полю значений, например «Сумма продаж». В следующем примере создаётся сводная таблица с одним полем строки (`Sport`) и одним полем данных (`Sales`), после чего показываются 2 вида спорта с наибольшими продажами. Значение `rankBy` равно 0, поскольку «Сумма продаж» — поле данных с индексом 0.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Sport")
worksheet.getCells().get("B1").putValue("Quarter")
worksheet.getCells().get("C1").putValue("Sales")
sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
row = 2
for sport in sports:
    for quarter in range(1, 4):
        worksheet.getCells().get(row, 0).putValue(sport)
        worksheet.getCells().get(row, 1).putValue("Qtr" + str(quarter))
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row)
        row += 1
pivot_table = worksheet.getPivotTables().add("A1:C16", 2, 5)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Sport")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Sales")
pivot_table.calculateData()
sport_field = pivot_table.getRowFields().get(0)
sport_field.setAutoShow(True)
sport_field.setAutoShowCount(2)
sport_field.setAutoShowField(2)
pivot_table.calculateData()
workbook.save("output-top10-by-value-field.xlsx")
jpype.shutdownJVM()
```

### **Ранжирование по самому полю**
Поле также можно ранжировать по самому себе — передайте значение -1 в `rankBy`. Для этого варианта не требуется дополнительное поле данных; достаточно, чтобы поле находилось в области строк или столбцов. В следующем примере показаны 3 вида спорта, занимающие нижние позиции в рейтинге по самому полю. При сохранении этой настройки атрибут `rankBy` не записывается в XML сводной таблицы, поскольку -1 является значением по умолчанию для этого формата, а `Top10AutoShowSettings.getRankBy()` считывает значение -1.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Sport")
worksheet.getCells().get("B1").putValue("Quarter")
worksheet.getCells().get("C1").putValue("Sales")
sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
row = 2
for sport in sports:
    for quarter in range(1, 4):
        worksheet.getCells().get(row, 0).putValue(sport)
        worksheet.getCells().get(row, 1).putValue("Qtr" + str(quarter))
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row)
        row += 1
pivot_table = worksheet.getPivotTables().add("A1:C16", 2, 5)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Sport")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Sales")
pivot_table.calculateData()
sport_field = pivot_table.getRowFields().get(0)
# Показать 3 нижних элемента, ранжированных по самому полю (rankBy = -1)
sport_field.top10AutoShow(True, False, 3, -1)
pivot_table.calculateData()
workbook.save("output-top10-by-field-itself.xlsx")
jpype.shutdownJVM()
```

## **Чтение текущих параметров (Top10AutoShowSettings)**
Метод `PivotField.getTop10AutoShowSettings()` возвращает объект `PivotFieldTop10AutoShowSettings`, предоставляющий доступ к текущим параметрам автопоказа, сохранённым в поле. Его можно использовать, чтобы проверить, как будут представлены элементы в существующей рабочей книге или только что настроенной сводной таблице, включая рабочие книги, загруженные из файла.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat
workbook = Workbook("output-top10-by-value-field.xlsx")
pivot_table = workbook.getWorksheets().get(0).getPivotTables().get(0)
sport_field = pivot_table.getRowFields()[0]
settings = sport_field.getTop10AutoShowSettings()
print("AutoShow enabled: " + str(settings.isAutoShow()))
print("Direction: " + ("Top" if settings.isTop() else "Bottom"))
print("Item count: " + str(settings.getAutoShowCount()))
print("Ranking data field index: " + str(settings.getRankBy()))
jpype.shutdownJVM()
```

Четыре свойства соответствуют классическим атрибутам автопоказа, которые записываются в XML сводной таблицы (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`), поэтому Excel любой версии будет применять считанные значения.

## **Примечание**

{{% alert color="primary" %}}
- Прямые средства доступа `PivotField` — `isAutoShow()`, `isAscendShow()`, `getAutoShowCount()` и `getAutoShowField()` — помечены как устаревшие. Вместо них используйте объект `Top10AutoShowSettings`: `PivotField.isAutoShow()` заменяется на `Top10AutoShowSettings.isAutoShow()`, `PivotField.isAscendShow()` заменяется на `Top10AutoShowSettings.isTop()`, `PivotField.getAutoShowCount()` заменяется на `Top10AutoShowSettings.getAutoShowCount()`, а `PivotField.getAutoShowField()` заменяется на `Top10AutoShowSettings.getRankBy()`. Сам метод `top10AutoShow()` — поддерживаемый способ изменения параметров.
- `top10AutoShow` работает с полями строк и столбцов. Поле, находящееся только в области страницы (фильтра), нельзя ранжировать таким способом, поскольку его элементы не выводятся в теле сводной таблицы.
{{% /alert %}}

## **Excel 2007-365: фильтр топ-10 (filterTop10)**
Современные версии Excel предоставляют «Топ-10» в качестве фильтра значений в меню поля («Фильтры значений», «Топ-10...»). В Aspose.Cells этот фильтр реализован с помощью метода `PivotField.filterTop10(int valueFieldIndex, PivotFilterType type, boolean isTop, int itemCount)`, который возвращает созданный объект `PivotFilter`:
- `valueFieldIndex` — индекс (с нуля) поля данных, агрегированные значения которого определяют рейтинг элементов.
- `type` — определяет смысл `itemCount`. `PivotFilterType.COUNT` оставляет фиксированное количество элементов (параметр «Элементы» в диалоговом окне). `PivotFilterType.PERCENT` оставляет заданный процент элементов, поэтому `itemCount` сам является процентом: значение 30 оставляет 30 процентов верхних элементов. `PivotFilterType.SUM` ранжирует элементы по накопленной сумме значений.
- `isTop` — `True` для верхних элементов, `False` — для нижних.
- `itemCount` — число N в обозначении «Топ N»; его единица измерения зависит от `type`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType, PivotFilterType
try:
    workbook = Workbook()
    worksheet = workbook.getWorksheets().get(0)
    worksheet.getCells().get("A1").putValue("Sport")
    worksheet.getCells().get("B1").putValue("Quarter")
    worksheet.getCells().get("C1").putValue("Sales")
    sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
    row = 2
    for sport in sports:
        for quarter in range(1, 4):
            worksheet.getCells().get(row, 0).putValue(sport)
            worksheet.getCells().get(row, 1).putValue("Qtr" + str(quarter))
            worksheet.getCells().get(row, 2).putValue(1000 + 777 * row)
            row += 1
    pivot_table = worksheet.getPivotTables().add("A1:C16", 2, 5)
    pivot_table.addFieldToArea(PivotFieldType.ROW, "Sport")
    pivot_table.addFieldToArea(PivotFieldType.DATA, "Sales")
    pivot_table.calculateData()
    sport_field = pivot_table.getRowFields().get(0)
    # Фильтр Top 10 — оставить 2 верхних элемента по значению «Сумма продаж» (индекс поля данных 0)
    filter = sport_field.filterTop10(0, PivotFilterType.COUNT, True, 2)
    # Для фильтра на основе процентов вместо этого оставьте 30 процентов верхних элементов:
    # sport_field.filterTop10(0, PivotFilterType.PERCENT, True, 30)
    pivot_table.getPivotCache().refresh()
    pivot_table.calculateData()
    workbook.save("output-top10-filter.xlsx")
finally:
    jpype.shutdownJVM()
```

{{% alert color="primary" %}}
`top10AutoShow` и `filterTop10` — две отдельные возможности. Автопоказ записывает классический атрибут `autoShow` в поле сводной таблицы. Этот атрибут учитывается всеми версиями Excel, начиная с Excel 97. `filterTop10` записывает современную запись `PivotFilter`, для которой требуется Excel 2007 или более поздняя версия. Если открыть рабочую книгу в более старой версии Excel, сводная таблица с современным фильтром отобразит все элементы. Если документ должен проходить цикл сохранения и повторного открытия с помощью устаревших инструментов, используйте `top10AutoShow`; для современных рабочих книг используйте `filterTop10`, поскольку он сочетается с другими фильтрами значений.
{{% /alert %}}

## **Связанные статьи**
- [Фильтрация сводных таблиц по метке или значению](/cells/ru/python-java/filter-by-label-or-value-of-pivot-table/)
- [Добавление полей строки и столбца в сводную таблицу](/cells/ru/python-java/pivot-table-add-row-and-column-fields/)
- [Группировка полей сводной таблицы](/cells/ru/python-java/group-pivot-fields-in-the-pivot-table/)
- [Обновление сводной таблицы](/cells/ru/python-java/refresh-pivot-table/)
- [Добавление поля страницы в сводную таблицу](/cells/ru/python-java/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="python" >}}
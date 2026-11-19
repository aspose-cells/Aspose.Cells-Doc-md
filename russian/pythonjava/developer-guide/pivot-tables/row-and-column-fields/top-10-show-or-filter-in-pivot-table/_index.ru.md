---
title: Отображение или фильтрация топ-10 в сводной таблице
linktitle: Отображение или фильтрация топ-10 в сводной таблице
description: Узнайте, как отображать только элементы, занимающие верхние или нижние позиции в рейтинге поля сводной таблицы, в Aspose.Cells for Python via Java. В этой статье рассматриваются метод top10AutoShow для Excel 97–2003, чтение параметров с помощью Top10AutoShowSettings и фильтр «Топ-10» для Excel 2007–365 с помощью filterTop10.
keywords: Aspose.Cells for Python via Java, сводная таблица, топ-10, автопоказ, top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, filterTop10, PivotFilterType, PivotField, Python
type: docs
weight: 20
url: /ru/python-java/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
Сводная таблица, в которой перечислены все элементы поля строк, может быть трудной для восприятия, если поле содержит десятки элементов. Отчёт «Топ-10» оставляет только элементы, занимающие верхние или нижние позиции в рейтинге, — именно для этого и предназначены отчёты с ранжированием, например «5 товаров с наибольшей выручкой» или «3 региона с наименьшим количеством продаж». Aspose.Cells поддерживает два механизма, соответствующих двум поколениям Microsoft Excel.
- **Автопоказ Excel 97–2003** — метод `PivotField.top10AutoShow()`. Это классическая настройка «Показать N верхних/нижних элементов», которая хранится непосредственно в поле сводной таблицы. Она работает во всех версиях Excel, как старых, так и новых, поскольку является частью исходного формата сводной таблицы.
- **Фильтр «Топ-10» Excel 2007–365** — метод `PivotField.filterTop10()`. Это современный фильтр значений «Топ-10», доступный в меню поля в разделе «Фильтры по значениям». Он хранится в виде объекта `PivotFilter`, привязанного к полю, и позволяет выполнять ранжирование по фиксированному количеству элементов или по проценту.

## **Отображение топ-10 в Excel 97–2003 (top10AutoShow)**
Классический автопоказ настраивается одним вызовом `PivotField.top10AutoShow(boolean isAutoShow, boolean isTop, int count, int rankBy)`:
- `isAutoShow` — включает или отключает параметр автопоказа в поле.
- `isTop` — значение `True` оставляет элементы с самым высоким рейтингом (Top), а `False` — с самым низким (Bottom).
- `count` — количество элементов, которые следует оставить, например 10 для классического отчёта «Топ-10».
- `rankBy` — индекс поля данных (с нуля), значения которого определяют рейтинг элементов. Передайте -1, чтобы ранжировать элементы по самому полю.
Рейтинг может определяться полем значений или самим полем. Далее приведены два варианта.

### **Ранжирование по полю значений**
Ранжирование элементов поля строк по обычному полю значений, например «Сумма продаж». В следующем примере создается сводная таблица с одним полем строк (`Sport`) и одним полем данных (`Sales`), после чего отображаются два вида спорта с наибольшим объёмом продаж. `rankBy` равен 0, поскольку «Сумма продаж» — это поле данных с индексом 0.

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
sport_field.top10AutoShow(True, True, 2, 0)
pivot_table.calculateData()
workbook.save("output-top10-by-value-field.xlsx")
jpype.shutdownJVM()
```

### **Ранжирование по самому полю**
Поле также можно использовать для ранжирования по его собственным значениям — передайте -1 в качестве `rankBy`. Для этого варианта не требуется дополнительное поле данных; достаточно разместить поле в области строк или столбцов. В следующем примере показаны три вида спорта, занимающие нижние позиции в рейтинге по самому полю. При сохранении этой настройки атрибут `rankBy` не записывается в XML сводной таблицы, поскольку -1 является значением по умолчанию для данного формата, а `Top10AutoShowSettings.getRankBy()` считывает -1.

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
# Show the bottom 3 items ranked by the field itself (rankBy = -1)
sport_field.top10AutoShow(True, False, 3, -1)
pivot_table.calculateData()
workbook.save("output-top10-by-field-itself.xlsx")
jpype.shutdownJVM()
```

## **Чтение текущих параметров (Top10AutoShowSettings)**
Метод `PivotField.getTop10AutoShowSettings()` возвращает объект `PivotFieldTop10AutoShowSettings`, предоставляющий доступ к параметрам AutoShow, которые в данный момент хранятся в поле. Используйте его, чтобы проверить, как будут представлены элементы в существующей рабочей книге или только что настроенной сводной таблице. Это также применимо к рабочим книгам, загруженным из файла.

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

Четыре свойства соответствуют классическим атрибутам AutoShow, записываемым в XML сводной таблицы (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`), поэтому считанные значения будут учитываться всеми версиями Excel.

## **Примечание**

{{% alert color="primary" %}}
- Прямые аксессоры `PivotField` — `isAutoShow()`, `isAscendShow()`, `getAutoShowCount()` и `getAutoShowField()` — помечены как устаревшие. Вместо них используйте объект `Top10AutoShowSettings`: `PivotField.isAutoShow()` становится `Top10AutoShowSettings.isAutoShow()`, `PivotField.isAscendShow()` становится `Top10AutoShowSettings.isTop()`, `PivotField.getAutoShowCount()` становится `Top10AutoShowSettings.getAutoShowCount()`, а `PivotField.getAutoShowField()` становится `Top10AutoShowSettings.getRankBy()`. Сам метод `top10AutoShow()` является поддерживаемым способом изменения этих параметров.
- `top10AutoShow` работает с полями строк и столбцов. Поле, находящееся только в области страницы (фильтра), нельзя таким образом ранжировать, поскольку его элементы не размещены в основной части сводной таблицы.
{{% /alert %}}

## **Excel 2007–365: фильтр «Топ-10» (filterTop10)**
Современные версии Excel предоставляют фильтр «Топ-10» в меню поля (раздел «Фильтры по значениям», пункт «Топ-10...»). Aspose.Cells моделирует его с помощью метода `PivotField.filterTop10(int valueFieldIndex, PivotFilterType type, boolean isTop, int itemCount)`, который возвращает созданный объект `PivotFilter`:
- `valueFieldIndex` — индекс поля данных (с нуля), агрегированные значения которого определяют рейтинг элементов.
- `type` — определяет смысл `itemCount`. `PivotFilterType.COUNT` оставляет фиксированное количество элементов (вариант «Элементы» в диалоговом окне). `PivotFilterType.PERCENT` оставляет заданный процент элементов, поэтому `itemCount` задаёт сам процент: значение 30 оставляет 30% элементов с наибольшими значениями. `PivotFilterType.SUM` ранжирует элементы по совокупному объёму их значений.
- `isTop` — значение `True` для выбора верхних элементов, `False` — нижних.
- `itemCount` — число N в выражении «Топ N»; его единица измерения зависит от `type`.

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
    # Top 10 Filter — keep the top 2 items by "Sum of Sales" (data field index 0)
    filter = sport_field.filterTop10(0, PivotFilterType.COUNT, True, 2)
    # For a percentage-based filter instead, keep the top 30 percent of the items:
    # sport_field.filterTop10(0, PivotFilterType.PERCENT, True, 30)
    pivot_table.getPivotCache().refresh()
    pivot_table.calculateData()
    workbook.save("output-top10-filter.xlsx")
finally:
    jpype.shutdownJVM()
```

{{% alert color="primary" %}}
`top10AutoShow` и `filterTop10` — два отдельных механизма. Автопоказ записывает классический атрибут `autoShow` в поле сводной таблицы и поддерживается всеми версиями Excel, начиная с Excel 97. `filterTop10` записывает современную запись `PivotFilter`, для которой требуется Excel 2007 или более поздняя версия. При открытии рабочей книги в более старой версии Excel сводная таблица с современным фильтром отображает все элементы. Для документов, которые должны поддерживать цикл сохранения и чтения с помощью устаревших инструментов, предпочтительнее использовать `top10AutoShow`; для современных рабочих книг предпочтительнее использовать `filterTop10`, поскольку он работает совместно с другими фильтрами по значениям.
{{% /alert %}}

## **Связанные статьи**
- [Фильтрация сводных таблиц по метке или значению](/cells/ru/python-java/filter-by-label-or-value-of-pivot-table/)
- [Добавление полей строк и столбцов сводной таблицы](/cells/ru/python-java/pivot-table-add-row-and-column-fields/)
- [Группировка полей сводной таблицы](/cells/ru/python-java/group-pivot-fields-in-the-pivot-table/)
- [Обновление сводной таблицы](/cells/ru/python-java/refresh-pivot-table/)
- [Добавление поля страницы в сводную таблицу](/cells/ru/python-java/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="python" >}}
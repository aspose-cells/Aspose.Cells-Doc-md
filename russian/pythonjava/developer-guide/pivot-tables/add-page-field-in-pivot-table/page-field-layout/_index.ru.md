---
title: Изменение макета полей страниц в сводной таблице
linktitle: Изменение макета полей страниц в сводной таблице
description: Узнайте, как управлять макетом области полей страниц в сводной таблице с помощью Aspose.Cells for Python via Java, включая настройку порядка отображения, количества полей в строке и порядка следования полей страниц в верхней части сводной таблицы.
keywords: Aspose.Cells for Python via Java, библиотека Python Java, электронная таблица, сводная таблица, поле страницы, порядок полей страниц, количество полей страниц в строке, перемещение поля страницы
type: docs
weight: 191
url: /ru/python-java/change-page-field-layout/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
Эта статья является продолжением темы **Добавление поля страницы в сводную таблицу**. В ней показано, как управлять макетом области полей страниц — полосой элементов управления фильтрацией в верхней части сводной таблицы — включая порядок отображения, количество полей в строке и изменение порядка полей.
{{% /alert %}}
## **Введение**
Сводная таблица в Microsoft Excel предоставляет выделенную **область полей страниц**, которая располагается над телом таблицы со строками, столбцами и данными. Эта область отображается в виде полосы раскрывающихся элементов управления фильтрацией (по одному на каждое поле страницы), на которые конечные пользователи нажимают, чтобы отфильтровать данные сводной таблицы по таким критериям, как год или регион. Aspose.Cells for Python via Java моделирует эту область через коллекцию `pivot_table.page_fields` и предоставляет три свойства, которые управляют визуальным расположением полосы:
- `pivot_table.page_field_order` (значение типа `Aspose.Cells.PrintOrderType`) определяет, будут ли дополнительные поля страниц размещены *рядом* с существующими или *под* ними.
- `pivot_table.page_field_wrap_count` задаёт количество полей страниц, размещаемых в одной строке или столбце до переноса.
- `pivot_table.page_fields.move(curr_index, dest_index)` изменяет порядок полей страниц без изменения режима упорядочивания.
В этой статье рассматриваются три примера кода, демонстрирующие каждую из этих операций на одном и том же наборе данных, чтобы вы могли сравнить полученные макеты бок о бок.
## **Исходные данные**
Все три примера ниже загружают эти восемь строк данных о продажах на рабочий лист с именем `PivotData`. Данные содержат два кандидата на поля страниц (`Year`, `Region`), один кандидат на поле строки (`Fruit`) и один показатель (`Amount`), что делает полосу полей страниц удобной для изучения.
| Fruit  | Year | Region | Amount |
|--------|------|--------|--------|
| Apple  | 2022 | North  | 150    |
| Apple  | 2023 | North  | 180    |
| Banana | 2022 | South  | 120    |
| Banana | 2023 | South  | 140    |
| Cherry | 2022 | East   | 200    |
| Cherry | 2023 | East   | 220    |
| Grape  | 2022 | West   | 90     |
| Grape  | 2023 | West   | 110    |
Все восемь строк заполняются в каждом примере кода в одинаковом порядке, поэтому исходные данные никогда не различаются между сценариями — различаются только свойства макета полей страниц.
## **Пример 1: Сначала по горизонтали, затем вниз**
В первом сценарии мы настраиваем два поля страницы (`Year`, `Region`) так, чтобы они отображались **бок о бок в одной строке** в верхней части сводной таблицы. Мы назначаем `Fruit` на ось строк, размещаем `Year` первым, а `Region` вторым на оси страниц (порядок вызовов `add_field_to_area` определяет начальный индекс), добавляем `Amount` (Сумма) в качестве поля данных, а затем устанавливаем `page_field_order` равным `PrintOrderType.OVER_THEN_DOWN` со значением `page_field_wrap_count = 2`. При `OVER_THEN_DOWN` и количестве полей в строке, равном 2, два поля страниц располагаются горизонтально бок о бок в одной строке в верхней части сводной таблицы, поэтому полоса занимает одну строку и два столбца.
```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, WorksheetCollection, Worksheet, Cells, PivotTableCollection, PivotTable, PivotFieldType, ConsolidationFunction, PrintOrderType

dataDir = "output"
if not os.path.exists(dataDir):
    os.makedirs(dataDir, exist_ok=True)

workbook = Workbook()
worksheets = workbook.getWorksheets()

pivotDataIdx = worksheets.add("PivotData")
pivotDataSheet = worksheets.get(pivotDataIdx)
pivotDataCells = pivotDataSheet.getCells()

# Заголовки (строка 0)
pivotDataCells.get(0, 0).putValue("Fruit")
pivotDataCells.get(0, 1).putValue("Year")
pivotDataCells.get(0, 2).putValue("Region")
pivotDataCells.get(0, 3).putValue("Amount")

# Строка 1: Apple, 2022, North, 150
pivotDataCells.get(1, 0).putValue("Apple")
pivotDataCells.get(1, 1).putValue(2022)
pivotDataCells.get(1, 2).putValue("North")
pivotDataCells.get(1, 3).putValue(150)

# Строка 2: Apple, 2023, North, 180
pivotDataCells.get(2, 0).putValue("Apple")
pivotDataCells.get(2, 1).putValue(2023)
pivotDataCells.get(2, 2).putValue("North")
pivotDataCells.get(2, 3).putValue(180)

# Строка 3: Banana, 2022, South, 120
pivotDataCells.get(3, 0).putValue("Banana")
pivotDataCells.get(3, 1).putValue(2022)
pivotDataCells.get(3, 2).putValue("South")
pivotDataCells.get(3, 3).putValue(120)

# Строка 4: Banana, 2023, South, 140
pivotDataCells.get(4, 0).putValue("Banana")
pivotDataCells.get(4, 1).putValue(2023)
pivotDataCells.get(4, 2).putValue("South")
pivotDataCells.get(4, 3).putValue(140)

# Строка 5: Cherry, 2022, East, 200
pivotDataCells.get(5, 0).putValue("Cherry")
pivotDataCells.get(5, 1).putValue(2022)
pivotDataCells.get(5, 2).putValue("East")
pivotDataCells.get(5, 3).putValue(200)

# Строка 6: Cherry, 2023, East, 220
pivotDataCells.get(6, 0).putValue("Cherry")
pivotDataCells.get(6, 1).putValue(2023)
pivotDataCells.get(6, 2).putValue("East")
pivotDataCells.get(6, 3).putValue(220)

# Строка 7: Grape, 2022, West, 90
pivotDataCells.get(7, 0).putValue("Grape")
pivotDataCells.get(7, 1).putValue(2022)
pivotDataCells.get(7, 2).putValue("West")
pivotDataCells.get(7, 3).putValue(90)

# Строка 8: Grape, 2023, West, 110
pivotDataCells.get(8, 0).putValue("Grape")
pivotDataCells.get(8, 1).putValue(2023)
pivotDataCells.get(8, 2).putValue("West")
pivotDataCells.get(8, 3).putValue(110)

# Добавление листа PivotTableReport
pivotTableSheetIdx = worksheets.add("PivotTableReport")
pivotTableSheet = worksheets.get(pivotTableSheetIdx)
pivotTables = pivotTableSheet.getPivotTables()

# Создание сводной таблицы с источником PivotData!A1:D9, размещённой в A1 на PivotTableReport
pivotIndex = pivotTables.add("PivotData!A1:D9", "A1", "PivotTable1")
pivotTable = pivotTables.get(pivotIndex)

# Добавление полей
pivotTable.addFieldToArea(PivotFieldType.ROW, 0)   # Fruit
pivotTable.addFieldToArea(PivotFieldType.PAGE, 1)  # Year
pivotTable.addFieldToArea(PivotFieldType.PAGE, 2)  # Region
pivotTable.addFieldToArea(PivotFieldType.DATA, 3)  # Amount
pivotTable.getDataFields().get(0).setFunction(ConsolidationFunction.SUM)

# Настройка макета области полей страницы: сначала поля страницы располагаются по горизонтали, перенос после каждых 2
pivotTable.setPageFieldOrder(PrintOrderType.OVER_THEN_DOWN)
pivotTable.setPageFieldWrapCount(2)

# Обновление и расчёт
pivotTable.calculateData()

# Сохранение
workbook.save(os.path.join(dataDir, "pageFieldLayout_overThenDown.xlsx"))

jpype.shutdownJVM()
```
## **Пример 2: Сначала вниз, затем вправо**
В этом примере мы размещаем `Fruit` на оси строк, `Year` и `Region` на оси страниц (сначала `Year`) и `Amount` (Сумма) в качестве поля данных — точно так же, как в примере 1. Затем мы устанавливаем `page_field_order` равным `PrintOrderType.DOWN_THEN_OVER` и `page_field_wrap_count` равным `2`. При `DOWN_THEN_OVER` и количестве полей в строке, равном 2, два поля страниц располагаются вертикально друг под другом — `Year` сверху, `Region` непосредственно под ним — образуя один столбец в верхней части сводной таблицы. Таким образом, полоса занимает две строки и один столбец, в отличие от примера 1.
```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFieldType, PrintOrderType

workbook = Workbook()
pivotData = workbook.getWorksheets().get(0)
pivotData.setName("PivotData")
pivotReportIdx = workbook.getWorksheets().add("PivotTableReport")
pivotReport = workbook.getWorksheets().get(pivotReportIdx)

headers = ["Fruit", "Year", "Region", "Amount"]
for c in range(len(headers)):
    pivotData.getCells().get(0, c).putValue(headers[c])

data = [
    ["Apple", 2022, "North", 150],
    ["Apple", 2023, "North", 180],
    ["Banana", 2022, "South", 120],
    ["Banana", 2023, "South", 140],
    ["Cherry", 2022, "East", 200],
    ["Cherry", 2023, "East", 220],
    ["Grape", 2022, "West", 90],
    ["Grape", 2023, "West", 110]
]

for r in range(len(data)):
    for c in range(len(data[r])):
        pivotData.getCells().get(r + 1, c).putValue(data[r][c])

idx = pivotReport.getPivotTables().add("PivotData!A1:D9", "A1", "PivotTable")
pivotTable = pivotReport.getPivotTables().get(idx)

pivotTable.addFieldToArea(PivotFieldType.ROW, 0)
pivotTable.addFieldToArea(PivotFieldType.PAGE, 1)
pivotTable.addFieldToArea(PivotFieldType.PAGE, 2)
pivotTable.addFieldToArea(PivotFieldType.DATA, 3)

pivotTable.setPageFieldOrder(PrintOrderType.DOWN_THEN_OVER)
pivotTable.setPageFieldWrapCount(2)

pivotTable.calculateData()

workbook.save("pageFieldLayout_downThenOver.xlsx")

jpype.shutdownJVM()
```
## **Пример 3: Перемещение поля страницы**
В третьем сценарии мы сохраняем этот набор данных и распределение полей, задаём нейтральный макет (`OVER_THEN_DOWN` с количеством полей в строке `2`), а затем демонстрируем операцию `page_fields.move`. Вызов `move(0, 1)` перемещает поле страницы с индексом 0 (`Year`) на позицию 1, а поле страницы, которое было на позиции 1 (`Region`), сдвигается на позицию 0. После этого вызова `Region` становится первым полем страницы, а `Year` — вторым. Режим переноса и упорядочивания остаётся неизменным, поэтому полоса по-прежнему отображается горизонтально бок о бок — изменился только порядок двух раскрывающихся списков.
```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType, PrintOrderType

workbook = Workbook()

dataSheet = workbook.getWorksheets().get(0)
dataSheet.setName("PivotData")

dataSheet.getCells().get("A1").putValue("Fruit")
dataSheet.getCells().get("B1").putValue("Year")
dataSheet.getCells().get("C1").putValue("Region")
dataSheet.getCells().get("D1").putValue("Amount")

dataSheet.getCells().get("A2").putValue("Apple")
dataSheet.getCells().get("B2").putValue(2022)
dataSheet.getCells().get("C2").putValue("North")
dataSheet.getCells().get("D2").putValue(150)

dataSheet.getCells().get("A3").putValue("Apple")
dataSheet.getCells().get("B3").putValue(2023)
dataSheet.getCells().get("C3").putValue("North")
dataSheet.getCells().get("D3").putValue(180)

dataSheet.getCells().get("A4").putValue("Banana")
dataSheet.getCells().get("B4").putValue(2022)
dataSheet.getCells().get("C4").putValue("South")
dataSheet.getCells().get("D4").putValue(120)

dataSheet.getCells().get("A5").putValue("Banana")
dataSheet.getCells().get("B5").putValue(2023)
dataSheet.getCells().get("C5").putValue("South")
dataSheet.getCells().get("D5").putValue(140)

dataSheet.getCells().get("A6").putValue("Cherry")
dataSheet.getCells().get("B6").putValue(2022)
dataSheet.getCells().get("C6").putValue("East")
dataSheet.getCells().get("D6").putValue(200)

dataSheet.getCells().get("A7").putValue("Cherry")
dataSheet.getCells().get("B7").putValue(2023)
dataSheet.getCells().get("C7").putValue("East")
dataSheet.getCells().get("D7").putValue(220)

dataSheet.getCells().get("A8").putValue("Grape")
dataSheet.getCells().get("B8").putValue(2022)
dataSheet.getCells().get("C8").putValue("West")
dataSheet.getCells().get("D8").putValue(90)

dataSheet.getCells().get("A9").putValue("Grape")
dataSheet.getCells().get("B9").putValue(2023)
dataSheet.getCells().get("C9").putValue("West")
dataSheet.getCells().get("D9").putValue(110)

pivotSheetIdx = workbook.getWorksheets().add("PivotTableReport")
pivotSheet = workbook.getWorksheets().get(pivotSheetIdx)

pivotIdx = pivotSheet.getPivotTables().add("PivotData!A1:D9", "A3", "PivotTable")
pivotTable = pivotSheet.getPivotTables().get(pivotIdx)

pivotTable.addFieldToArea(PivotFieldType.ROW, 0)
pivotTable.addFieldToArea(PivotFieldType.PAGE, 1)
pivotTable.addFieldToArea(PivotFieldType.PAGE, 2)
pivotTable.addFieldToArea(PivotFieldType.DATA, 3)

pivotTable.setPageFieldOrder(PrintOrderType.OVER_THEN_DOWN)
pivotTable.setPageFieldWrapCount(2)

pivotTable.getPageFields().move(0, 1)

pivotTable.calculateData()

workbook.save("pageFieldLayout_move.xlsx")

jpype.shutdownJVM()
```
## **Связанные статьи**
- [Добавление поля страницы в сводную таблицу](/cells/ru/python-java/add-page-field-in-pivot-table/) — родительская страница, рассказывающая о том, как добавлять поля страниц в сводную таблицу.
- [Поля строк и столбцов в сводной таблице](/cells/ru/python-java/row-and-column-fields/) — рассматривает распределение полей по осям строк и столбцов, дополняя работу с осью страниц, показанную здесь.
- [Управление полями значений в сводной таблице](/cells/ru/python-java/manage-value-fields/) — описывает настройку области данных (значений), включая агрегацию `SUM`, используемую в этой статье.
- [Обновление сводной таблицы](/cells/ru/python-java/refresh-pivot-table/) — поясняет методы `refresh_data` и `calculate_data`, которые необходимо вызывать после изменения порядка полей страниц.
- [Применение стиля к сводной таблице](/cells/ru/python-java/apply-style-to-pivot-table/) — показывает, как форматировать отображаемую сводную таблицу после размещения полосы полей страниц.
{{< app/cells/assistant language="python" >}}
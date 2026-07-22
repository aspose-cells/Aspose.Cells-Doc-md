---
title: Спарклайны в Aspose.Cells for Python via Java
linktitle: Спарклайны
description: Aspose.Cells — это библиотека Python via Java для работы с файлами электронных таблиц, которая поддерживает создание спарклайнов — миниатюрных диаграмм, размещаемых внутри ячеек рабочего листа. В этой статье объясняется, как добавлять и настраивать линейные, столбчатые спарклайны и спарклайны «выигрыш/проигрыш» с помощью библиотеки Aspose.Cells.
keywords: Aspose.Cells, Python via Java library, spreadsheet, sparklines, line sparkline, column sparkline, win/loss sparkline, SparklineGroup, SparklineType
type: docs
weight: 195
url: /ru/python-java/creating-sparklines/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells поддерживает создание спарклайнов внутри ячеек рабочего листа. Спарклайны — это миниатюрные диаграммы, которые помещаются в одной ячейке и обеспечивают быстрое визуальное представление тенденций в данных. Aspose.Cells поддерживает линейные, столбчатые спарклайны и спарклайны «выигрыш/проигрыш», каждый из которых можно настроить по цвету, толщине линии, высоким/низким точкам и маркерам.

{{% /alert %}}

## **Введение**

Спарклайны — это крошечные внутриклеточные диаграммы, которые полезны, когда требуется отобразить быструю тенденцию рядом со строкой или столбцом данных, не занимая места полноценной диаграммы. Excel поддерживает три вида спарклайнов: **линейные**, **столбчатые** и **выигрыш/проигрыш**. Aspose.Cells воспроизводит эту возможность через API `SparklineGroup` и `SparklineGroupCollection`, которые находятся в пространстве имён `Aspose.Cells.Charts`.

В Aspose.Cells каждый добавляемый спарклайн создаётся с помощью `worksheet.getSparklineGroups().add(...)`, который возвращает объект `SparklineGroup`. Затем вы можете использовать этот объект для задания типа спарклайна, диапазона данных, целевой ячейки и визуальных свойств, таких как цвет линии, толщина линии, маркеры и индикаторы высоких/низких точек.

{{% alert color="primary" %}}

Один объект `SparklineGroup` может содержать один или несколько спарклайнов, использующих общий стиль. Когда вы вызываете `add` и передаёте строку данных и одну целевую ячейку, вы получаете один спарклайн внутри этой ячейки. Если ваш целевой диапазон шире одной ячейки, отдельный спарклайн рисуется в каждой целевой ячейке, при этом все они используют одинаковый стиль и диапазон данных.

{{% /alert %}}

В этой статье рассматривается каждый из трёх типов спарклайнов, поддерживаемых Aspose.Cells — **Линейный**, **Столбчатый** и **Выигрыш/Проигрыш** — и показано, как их добавлять, настраивать их цвета и сохранять полученную рабочую книгу.

## **Линейные спарклайны**

Линейный спарклайн рисует непрерывную линию через точки данных в ряду, что делает его наиболее естественным выбором для отображения тенденций во времени. В Aspose.Cells линейный спарклайн создаётся путём передачи `SparklineType.LINE` в метод `add`.

Рабочий процесс аналогичен любому другому типу спарклайнов:

1. Создайте новую `Workbook` и получите доступ к первому рабочему листу.
2. Заполните строку исходных данных (например, строка 1, столбцы A–E) значениями, которые вы хотите визуализировать.
3. Создайте `CellArea`, описывающую целевую ячейку, в которой будет нарисован спарклайн.
4. Вызовите `worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest)`. Третий аргумент — `false` — сообщает Aspose.Cells, что диапазон данных горизонтальный (строка), а не вертикальный (столбец).
5. При желании настройте возвращённый `SparklineGroup`. Для линейного спарклайна вы можете задать цвет линии с помощью `group.getLine().getColor()` (который ожидает `CellsColor` из `Aspose.Cells.Drawing`), отрегулировать толщину линии и включить маркеры высоких/низких точек.
6. Сохраните рабочую книгу.

Следующий пример создаёт рабочую книгу, записывает значения 5, -3, 8, -2, 6 в ячейки A1–E1 и добавляет линейный спарклайн в ячейку F1, который отслеживает эти значения. Он также настраивает цвет линии на красный и включает маркеры для высоких и низких точек.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, CellArea, SparklineType
from java.awt import Color

# Шаг 1: Создаём Workbook и получаем первый лист
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()

# Шаг 2: Записываем пример значений 5, -3, 8, -2, 6 в ячейки A1:E1
cells.get("A1").putValue(5)
cells.get("B1").putValue(-3)
cells.get("C1").putValue(8)
cells.get("D1").putValue(-2)
cells.get("E1").putValue(6)

# Шаг 3: Создаём CellArea, указывающую на ячейку назначения F1
dest = CellArea()
dest.setStartColumn(5)  # столбец F (нумерация с 0)
dest.setEndColumn(5)
dest.setStartRow(0)     # строка 1 (нумерация с 0)
dest.setEndRow(0)

# Шаг 4: Добавляем линейную спарклайн-диаграмму из A1:E1 в F1
# SparklineGroups.add возвращает индекс только что добавленной группы
index = worksheet.getSparklineGroups().add(SparklineType.Line, "A1:E1", False, dest)
group = worksheet.getSparklineGroups().get(index)

# Шаг 5: Создаём красный CellsColor и назначаем его цвету линии спарклайна
red = workbook.createCellsColor()
red.setColor(Color.RED)
group.setSeriesColor(red)

# Шаг 6: Включаем маркеры верхних и нижних точек
group.setShowHighPoint(True)
group.setShowLowPoint(True)

# Шаг 7: Сохраняем книгу
workbook.save("output_line.xlsx")

jpype.shutdownJVM()
```

## **Столбчатые спарклайны**

Столбчатый спарклайн отображает каждую точку данных в виде вертикальной полосы. Это делает его хорошо подходящим для данных, величина которых имеет значение — например, ежемесячные показатели продаж или подсчёты. В Aspose.Cells вы создаёте столбчатый спарклайн путём передачи `SparklineType.COLUMN` в метод `add`.

Процедура аналогична примеру с линейным спарклайном:

1. Создайте новую `Workbook` и получите доступ к первому рабочему листу.
2. Заполните тот же исходный диапазон (A1:E1) значениями, которые вы хотите визуализировать.
3. Создайте `CellArea`, описывающую целевую ячейку.
4. Вызовите `worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest)`.
5. При желании настройте полученный `SparklineGroup` — например, задав `group.getType()` для подтверждения типа, или изменив цвет полос.
6. Сохраните рабочую книгу в отдельный выходной файл, чтобы он не перезаписал пример с линейным спарклайном.

Пример ниже записывает значения 5, -3, 8, -2, 6 в A1:E1 и отображает столбчатый спарклайн в F1. Отрицательные значения рисуются как полосы, направленные вниз, а положительные — как полосы, направленные вверх, что позволяет легко определить положительный и отрицательный вклад одним взглядом.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, CellArea, SparklineType

# Шаг 1: Создаём Workbook и получаем первый рабочий лист
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Шаг 2: Записываем пример значений в A1:E1
values = [5, -3, 8, -2, 6]
for i in range(len(values)):
    worksheet.getCells().get(0, i).putValue(values[i])

# Шаг 3: Создаём CellArea, указывающую на F1 (индекс столбца 5, индекс строки 0)
dest = CellArea()
dest.setStartColumn(5)
dest.setEndColumn(5)
dest.setStartRow(0)
dest.setEndRow(0)

# Шаг 4: Добавляем спарклайн типа Column в целевую ячейку
idx = worksheet.getSparklineGroups().add(
    SparklineType.Column, "A1:E1", False, dest)
group = worksheet.getSparklineGroups().get(idx)

# Шаг 5: Проверяем тип спарклайна, считывая group.Type
print("Sparkline Type added: " + str(group.getType()))

# Шаг 6: Сохраняем рабочую книгу
workbook.save("output_column.xlsx")

print("Workbook saved as output_column.xlsx")

jpype.shutdownJVM()
```

## **Спарклайны «Выигрыш/Проигрыш»**

Спарклайн «выигрыш/проигрыш» — это особый вариант столбчатого спарклайна, предназначенный для отображения только двух исходов: положительное значение рисуется как «восходящая» полоса (выигрыш), а нулевое или отрицательное значение — как «нисходящая» полоса (проигрыш). Спарклайны «выигрыш/проигрыш» обычно используются для визуализации последовательностей побед и поражений, результатов «сдал/не сдал» или любого бинарного исхода во времени.

В Aspose.Cells спарклайн «выигрыш/проигрыш» создаётся путём передачи `SparklineType.STACKED` в метод `add`. (Несмотря на название, `SparklineType.STACKED` — это значение перечисления, используемое для запроса отрисовки «выигрыш/проигрыш».)

Процедура аналогична двум другим типам:

1. Создайте новую `Workbook` и получите доступ к первому рабочему листу.
2. Заполните исходный диапазон. Поскольку спарклайны «выигрыш/проигрыш» рассматривают каждое значение как выигрыш или проигрыш, величина значения не имеет значения — важен только его знак. Положительные значения становятся восходящими полосами, а неположительные — нисходящими.
3. Создайте `CellArea`, описывающую целевую ячейку.
4. Вызовите `worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest)`.
5. При желании настройте возвращённый `SparklineGroup`, например, задав акцентные цвета для полос выигрыша и проигрыша.
6. Сохраните рабочую книгу под уникальным именем файла, чтобы все три примера могли сосуществовать на диске.

Пример ниже использует те же входные данные, что и предыдущие два раздела. Значения 5, -3, 8, -2, 6 интерпретируются как выигрыш, проигрыш, выигрыш, проигрыш, выигрыш — и спарклайн, нарисованный в F1, отражает именно этот паттерн.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, CellArea, SparklineType, CellsColor, Color

# Шаг 1: Создаем Workbook и получаем первый рабочий лист
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("WinLoss")

# Шаг 2: Заполняем пример данных в строке 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.getCells().get("A1").putValue(5)
worksheet.getCells().get("B1").putValue(-3)
worksheet.getCells().get("C1").putValue(8)
worksheet.getCells().get("D1").putValue(-2)
worksheet.getCells().get("E1").putValue(6)

# Шаг 3: Создаем CellArea, указывающую на F1 (столбец 5, строка 0)
dest = CellArea()
dest.setStartColumn(5)   # F
dest.setEndColumn(5)
dest.setStartRow(0)      # строка 1
dest.setEndRow(0)

# Шаг 4: Добавляем спарклайн Win/Loss (SparklineType.Stacked)
groupIndex = worksheet.getSparklineGroups().add(
    SparklineType.Stacked,
    "A1:E1",
    False,
    dest)
group = worksheet.getSparklineGroups().get(groupIndex)

# Шаг 5: Настраиваем группу спарклайнов
# Включаем маркеры верхних и нижних точек
group.setShowHighPoint(True)
group.setShowLowPoint(True)
group.setShowNegativePoints(True)

# Устанавливаем зеленый цвет для верхних точек
highColor = workbook.createCellsColor()
highColor.setColor(Color.GREEN)
group.setHighPointColor(highColor)

# Устанавливаем красный цвет для нижних точек
lowColor = workbook.createCellsColor()
lowColor.setColor(Color.RED)
group.setLowPointColor(lowColor)

# Устанавливаем оранжевый цвет для отрицательных точек
negColor = workbook.createCellsColor()
negColor.setColor(Color.ORANGE)
group.setNegativePointsColor(negColor)

# Устанавливаем цвет серии по умолчанию (используется для положительных столбцов)
seriesColor = workbook.createCellsColor()
seriesColor.setColor(Color.STEELBLUE)
group.setSeriesColor(seriesColor)

# Шаг 6: Сохраняем книгу
workbook.save("output_winloss.xlsx")

print("Workbook saved successfully: output_winloss.xlsx")

jpype.shutdownJVM()
```

## **Объединение всех трёх типов спарклайнов**

Каждый из предыдущих трёх примеров создаёт свою рабочую книгу, чтобы выходные файлы было легко просматривать изолированно. Однако в реальных сценариях часто требуется сравнить несколько рядов данных бок о бок. Самый чистый способ сделать это — поместить более одной группы спарклайнов в один и тот же рабочий лист, где каждая группа отображает свой стиль.

Вы можете добавить несколько объектов `SparklineGroup` в одну и ту же `SparklineGroupCollection`, и каждая группа может быть нацелена на разную целевую ячейку или разный диапазон. Например, можно поместить линейный спарклайн в F1, столбчатый спарклайн в F2 и спарклайн «выигрыш/проигрыш» в F3 — все они будут читать одни и те же исходные данные в строке 1 — чтобы читатель мог увидеть три разных визуальных представления одних и тех же чисел.

Комбинированный пример ниже создаёт одну рабочую книгу, заполняет строку 1 значениями 5, -3, 8, -2, 6, а затем добавляет три группы спарклайнов в ячейки F1, F2 и F3 — по одной каждого типа — так что полученный файл демонстрирует все три стиля спарклайнов одновременно.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, CellArea, CellsColor, SparklineType
from java.awt import Color

# Шаг 1: Создайте рабочую книгу и получите первый рабочий лист
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Шаг 2: Заполните образец данных в строке 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5)
worksheet.getCells().get("B1").putValue(-3)
worksheet.getCells().get("C1").putValue(8)
worksheet.getCells().get("D1").putValue(-2)
worksheet.getCells().get("E1").putValue(6)

# Шаг 3: Добавьте группу линейных спарклайнов в F1
lineArea = CellArea()
lineArea.setStartColumn(5)
lineArea.setEndColumn(5)
lineArea.setStartRow(0)
lineArea.setEndRow(0)
lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", False, lineArea)
lineGroup = worksheet.getSparklineGroups().get(lineIdx)

# Настройте цвет линейного спарклайна с помощью CellsColor
lineColor = workbook.createCellsColor()
lineColor.setColor(Color.BLUE)
lineGroup.setSeriesColor(lineColor)

# Шаг 4: Добавьте группу столбчатых спарклайнов в F2
columnArea = CellArea()
columnArea.setStartColumn(5)
columnArea.setEndColumn(5)
columnArea.setStartRow(1)
columnArea.setEndRow(1)
columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", False, columnArea)
columnGroup = worksheet.getSparklineGroups().get(columnIdx)

# Настройте цвет серии столбчатого спарклайна
columnColor = workbook.createCellsColor()
columnColor.setColor(Color.GREEN)
columnGroup.setSeriesColor(columnColor)

# Шаг 5: Добавьте группу спарклайнов Win/Loss (С накоплением) в F3
stackedArea = CellArea()
stackedArea.setStartColumn(5)
stackedArea.setEndColumn(5)
stackedArea.setStartRow(2)
stackedArea.setEndRow(2)
stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", False, stackedArea)
stackedGroup = worksheet.getSparklineGroups().get(stackedIdx)

# Настройте цвет серии спарклайна win/loss
stackedColor = workbook.createCellsColor()
stackedColor.setColor(Color(255, 140, 0))  # Темно-оранжевый
stackedGroup.setSeriesColor(stackedColor)

# Шаг 6: Сохраните рабочую книгу
workbook.save("output_all.xlsx")

jpype.shutdownJVM()
```

{{% alert color="primary" %}}

Когда вы объединяете несколько групп спарклайнов в одном рабочем листе, каждая группа независима. Они могут совместно использовать один и тот же исходный диапазон или использовать разные исходные диапазоны, и они могут быть стилизованы независимо. Это позволяет легко создать небольшую «панель мониторинга» из внутриклеточных визуализаций непосредственно внутри существующего рабочего листа.

{{% /alert %}}

## **Настройка внешнего вида спарклайнов**

После того как `SparklineGroup` создан и добавлен в `worksheet.getSparklineGroups()`, вы можете прочитать или изменить несколько его визуальных свойств перед сохранением рабочей книги. Наиболее часто настраиваемые свойства:

- **`group.getType()`** — тип `SparklineType` (LINE, COLUMN или STACKED). Он задаётся при добавлении группы, но вы можете прочитать его для подтверждения.
- **`group.getLine().getColor()`** — цвет линии, выраженный как `CellsColor`, созданный с помощью `workbook.createCellsColor()`. Это свойство используется для задания цвета обводки линейного спарклайна.
- **`group.getLine().getWeight()`** — толщина линии в пунктах. Более высокие значения дают более толстые линии.
- **Маркеры высоких/низких точек** — флаги, включающие маленькие маркеры на самых высоких и самых низких точках данных, полезные для выделения экстремумов.
- **Маркеры первой/последней/отрицательной точек** — флаги, переключающие маркеры на первой, последней и отрицательной точках данных.

Чтобы изменить цвет, всегда создавайте экземпляр `CellsColor` и присваивайте его соответствующему свойству. Не присваивайте `java.awt.Color` напрямую свойствам цвета спарклайна — они ожидают тип `CellsColor` из `Aspose.Cells.Drawing`. Сам метод `add` возвращает полностью типизированный объект `SparklineGroup`, поэтому вы можете связывать присваивания свойств с возвращаемым значением или сохранять его в локальной переменной и настраивать перед сохранением.



{{< app/cells/assistant language="python" >}}
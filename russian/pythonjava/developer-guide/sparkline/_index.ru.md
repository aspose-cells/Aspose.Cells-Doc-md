---
title: Спарклайны в Aspose.Cells for Python via Java
linktitle: Спарклайны в Aspose.Cells for Python via Java
description: Aspose.Cells — это библиотека Python via Java для работы с файлами электронных таблиц, которая поддерживает создание спарклайнов — миниатюрных диаграмм, размещаемых внутри ячеек рабочего листа. В этой статье объясняется, как добавлять и настраивать линейные, столбцовые спарклайны и спарклайны выигрышей/проигрышей с помощью библиотеки Aspose.Cells.
keywords: Aspose.Cells, библиотека Python via Java, электронная таблица, спарклайны, линейный спарклайн, столбцовый спарклайн, спарклайн выигрышей/проигрышей, SparklineGroup, SparklineType
type: docs
weight: 195
url: /ru/python-java/creating-sparklines/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells поддерживает создание спарклайнов внутри ячеек рабочего листа. Спарклайны — это миниатюрные диаграммы, которые помещаются в одну ячейку и обеспечивают быстрое визуальное представление тенденций данных. Aspose.Cells поддерживает линейные, столбцовые спарклайны и спарклайны выигрышей/проигрышей, каждый из которых можно настроить по цвету, толщине линии, точкам максимума/минимума и маркерам.

## **Введение**
Спарклайны — это крошечные внутриклеточные диаграммы, которые полезны, когда требуется отобразить быструю тенденцию рядом со строкой или столбцом данных, не занимая места полноценной диаграммы. Excel поддерживает три вида спарклайнов: **линейные**, **столбцовые** и **выигрышей/проигрышей**. Aspose.Cells дублирует эту возможность через API `SparklineGroup` и `SparklineGroupCollection`, расположенные в пространстве имён `Aspose.Cells.Charts`.
В Aspose.Cells каждый добавляемый спарклайн создаётся через `worksheet.getSparklineGroups().add(...)`, который возвращает объект `SparklineGroup`. Затем этот объект можно использовать для задания типа спарклайна, диапазона данных, ячейки назначения и визуальных свойств, таких как цвет линии, толщина линии, маркеры и индикаторы точек максимума/минимума.
В этой статье рассматриваются все три типа спарклайнов, поддерживаемых Aspose.Cells — **Линейные**, **Столбцовые** и **Выигрышей/проигрышей** — и показано, как их добавлять, настраивать их цвета и сохранять полученную рабочую книгу.

## **Линейные спарклайны**
Линейный спарклайн проводит непрерывную линию через точки данных в ряду, что делает его наиболее естественным выбором для отображения тенденций во времени. В Aspose.Cells линейный спарклайн создаётся путём передачи `SparklineType.LINE` методу `add`.
1. Создайте новую рабочую книгу `Workbook` и откройте первый рабочий лист.
2. Заполните строку исходных данных (например, строку 1, столбцы от A до E) значениями, которые требуется визуализировать.
3. Сформируйте `CellArea`, описывающую ячейку назначения, в которой будет нарисован спарклайн.
4. Вызовите `worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest)`. Третий аргумент — `false` — сообщает Aspose.Cells, что диапазон данных является горизонтальным (строка), а не вертикальным (столбец).
5. При необходимости настройте возвращённый `SparklineGroup`. Для линейного спарклайна можно задать цвет линии с помощью `group.getLine().getColor()` (который ожидает `CellsColor` из `Aspose.Cells.Drawing`), отрегулировать толщину линии и включить маркеры точек максимума/минимума.
6. Сохраните рабочую книгу.
В следующем примере создаётся рабочая книга, значения 5, -3, 8, -2, 6 записываются в ячейки A1–E1, и в ячейку F1 добавляется линейный спарклайн, отслеживающий эти значения. Также задаётся красный цвет линии и включаются маркеры для точек максимума и минимума.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, CellArea, CellsColor, SparklineType
from java.awt import Color
# Step 1: Create a Workbook and get the first worksheet
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Step 2: Populate sample data in row 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5)
worksheet.getCells().get("B1").putValue(-3)
worksheet.getCells().get("C1").putValue(8)
worksheet.getCells().get("D1").putValue(-2)
worksheet.getCells().get("E1").putValue(6)
# Step 3: Add a Line sparkline group at F1
lineArea = CellArea()
lineArea.setStartColumn(5)
lineArea.setEndColumn(5)
lineArea.setStartRow(0)
lineArea.setEndRow(0)
lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", False, lineArea)
lineGroup = worksheet.getSparklineGroups().get(lineIdx)
# Customize the line sparkline color via CellsColor
lineColor = workbook.createCellsColor()
lineColor.setColor(Color.BLUE)
lineGroup.setSeriesColor(lineColor)
# Step 4: Add a Column sparkline group at F2
columnArea = CellArea()
columnArea.setStartColumn(5)
columnArea.setEndColumn(5)
columnArea.setStartRow(1)
columnArea.setEndRow(1)
columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", False, columnArea)
columnGroup = worksheet.getSparklineGroups().get(columnIdx)
# Customize the column sparkline series color
columnColor = workbook.createCellsColor()
columnColor.setColor(Color.GREEN)
columnGroup.setSeriesColor(columnColor)
# Step 5: Add a Win/Loss (Stacked) sparkline group at F3
stackedArea = CellArea()
stackedArea.setStartColumn(5)
stackedArea.setEndColumn(5)
stackedArea.setStartRow(2)
stackedArea.setEndRow(2)
stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", False, stackedArea)
stackedGroup = worksheet.getSparklineGroups().get(stackedIdx)
# Customize the win/loss sparkline series color
stackedColor = workbook.createCellsColor()
stackedColor.setColor(Color(255, 140, 0))  # DarkOrange
stackedGroup.setSeriesColor(stackedColor)
# Step 6: Save the workbook
workbook.save("output_all.xlsx")
jpype.shutdownJVM()
```

## **Столбцовые спарклайны**
Столбцовый спарклайн отображает каждую точку данных в виде вертикальной полосы. Это делает его хорошо подходящим для данных, величина которых имеет значение — например, ежемесячных показателей продаж или количественных значений. В Aspose.Cells столбцовый спарклайн создаётся путём передачи `SparklineType.COLUMN` методу `add`.
Процедура повторяет пример с линейным спарклайном:
1. Создайте новую рабочую книгу `Workbook` и откройте первый рабочий лист.
2. Заполните строку исходных данных значениями, которые требуется визуализировать.
3. Сформируйте `CellArea`, описывающую ячейку назначения.
4. Вызовите `worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest)`.
5. При необходимости настройте полученный `SparklineGroup` — например, задав `group.getType()` для подтверждения типа или скорректировав цвет столбцов.
6. Сохраните рабочую книгу в отдельный выходной файл, чтобы не перезаписать пример с линейным спарклайном.
В приведённом ниже примере значения 5, -3, 8, -2, 6 записываются в A1:E1, а в ячейке F1 отображается столбцовый спарклайн. Отрицательные значения отображаются столбцами, направленными вниз, а положительные — столбцами, направленными вверх, что позволяет легко разглядеть положительный и отрицательный вклад одним взглядом.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, CellArea, SparklineType
# Шаг 1: Создайте рабочую книгу и получите первый рабочий лист
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Шаг 2: Запишите образцы значений в A1:E1
values = [5, -3, 8, -2, 6]
for i in range(len(values)):
    worksheet.getCells().get(0, i).putValue(values[i])
# Шаг 3: Создайте CellArea, указывающий на F1 (индекс столбца 5, индекс строки 0)
dest = CellArea()
dest.setStartColumn(5)
dest.setEndColumn(5)
dest.setStartRow(0)
dest.setEndRow(0)
# Шаг 4: Добавьте столбцовую спарклайн в ячейку назначения
idx = worksheet.getSparklineGroups().add(
    SparklineType.Column, "A1:E1", False, dest)
group = worksheet.getSparklineGroups().get(idx)
# Шаг 5: Подтвердите тип спарклайн, прочитав group.Type
print("Sparkline Type added: " + str(group.getType()))
# Шаг 6: Сохраните рабочую книгу
workbook.save("output_column.xlsx")
print("Workbook saved as output_column.xlsx")
jpype.shutdownJVM()
```

## **Спарклайны выигрышей/проигрышей**
Спарклайн выигрышей/проигрышей — это особый вариант столбцового спарклайна, предназначенный для отображения только двух исходов: положительное значение отображается как «верхний» столбец (выигрыш), а нулевое или отрицательное значение — как «нижний» столбец (проигрыш). Спарклайны выигрышей/проигрышей обычно используются для визуализации последовательностей побед и поражений, результатов «сдал/не сдал» или любого бинарного исхода во времени.
В Aspose.Cells спарклайн выигрышей/проигрышей создаётся путём передачи `SparklineType.STACKED` методу `add`. (Несмотря на название, `SparklineType.STACKED` — это значение перечисления, используемое для запроса рендеринга выигрышей/проигрышей.)
1. Создайте новую рабочую книгу `Workbook` и откройте первый рабочий лист.
2. Заполните исходный диапазон. Поскольку спарклайны выигрышей/проигрышей трактуют каждое значение либо как выигрыш, либо как проигрыш, величина значения не имеет значения — важен только его знак. Положительные значения становятся верхними столбцами, а неположительные — нижними.
3. Сформируйте `CellArea`, описывающую ячейку назначения.
4. Вызовите `worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest)`.
5. При необходимости настройте возвращённый `SparklineGroup`, например задав акцентные цвета для столбцов выигрышей и проигрышей.
6. Сохраните рабочую книгу под отдельным именем файла, чтобы все три примера могли сосуществовать на диске.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, CellArea, SparklineType, CellsColor, Color
# Step 1: Create a Workbook and get the first worksheet
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("WinLoss")
# Step 2: Populate sample data in row 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.getCells().get("A1").putValue(5)
worksheet.getCells().get("B1").putValue(-3)
worksheet.getCells().get("C1").putValue(8)
worksheet.getCells().get("D1").putValue(-2)
worksheet.getCells().get("E1").putValue(6)
# Step 3: Build a CellArea pointing to F1 (column 5, row 0)
dest = CellArea()
dest.setStartColumn(5)   # F
dest.setEndColumn(5)
dest.setStartRow(0)      # row 1
dest.setEndRow(0)
# Step 4: Add a Win/Loss sparkline (SparklineType.Stacked)
groupIndex = worksheet.getSparklineGroups().add(
    SparklineType.Stacked,
    "A1:E1",
    False,
    dest)
group = worksheet.getSparklineGroups().get(groupIndex)
# Step 5: Customize the sparkline group
# Enable high-point and low-point markers
group.setShowHighPoint(True)
group.setShowLowPoint(True)
group.setShowNegativePoints(True)
# Set the high-point color to green
highColor = workbook.createCellsColor()
highColor.setColor(Color.GREEN)
group.setHighPointColor(highColor)
# Set the low-point color to red
lowColor = workbook.createCellsColor()
lowColor.setColor(Color.RED)
group.setLowPointColor(lowColor)
# Set the negative-point color to orange
negColor = workbook.createCellsColor()
negColor.setColor(Color.ORANGE)
group.setNegativePointsColor(negColor)
# Set the default series color (used for positive bars)
seriesColor = workbook.createCellsColor()
seriesColor.setColor(Color.STEELBLUE)
group.setSeriesColor(seriesColor)
# Step 6: Save the workbook
workbook.save("output_winloss.xlsx")
print("Workbook saved successfully: output_winloss.xlsx")
jpype.shutdownJVM()
```

## **Объединение всех трёх типов спарклайнов**
Приведённый ниже комбинированный пример создаёт одну рабочую книгу, заполняет строку 1 значениями 5, -3, 8, -2, 6, а затем добавляет три группы спарклайнов в ячейки F1, F2 и F3 — по одной каждого типа — так что полученный файл демонстрирует все три стиля спарклайнов одновременно.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, CellArea, SparklineType
from java.awt import Color
# Step 1: Create a Workbook and get the first worksheet
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()
# Step 2: Write sample values 5, -3, 8, -2, 6 into cells A1:E1
cells.get("A1").putValue(5)
cells.get("B1").putValue(-3)
cells.get("C1").putValue(8)
cells.get("D1").putValue(-2)
cells.get("E1").putValue(6)
# Step 3: Build a CellArea pointing to destination cell F1
dest = CellArea()
dest.setStartColumn(5)  # column F (0-indexed)
dest.setEndColumn(5)
dest.setStartRow(0)     # row 1 (0-indexed)
dest.setEndRow(0)
# Step 4: Add a Line sparkline from A1:E1 into F1
# SparklineGroups.add returns the index of the newly added group
index = worksheet.getSparklineGroups().add(SparklineType.Line, "A1:E1", False, dest)
group = worksheet.getSparklineGroups().get(index)
# Step 5: Create a red CellsColor and assign it to the sparkline line color
red = workbook.createCellsColor()
red.setColor(Color.RED)
group.setSeriesColor(red)
# Step 6: Enable high-point and low-point markers
group.setShowHighPoint(True)
group.setShowLowPoint(True)
# Step 7: Save the workbook
workbook.save("output_line.xlsx")
jpype.shutdownJVM()
```

## **Настройка внешнего вида спарклайнов**
После того как `SparklineGroup` создан и добавлен в `worksheet.getSparklineGroups()`, можно считать или изменить несколько его визуальных свойств перед сохранением рабочей книги. Наиболее часто настраиваемые свойства:
- **`group.getType()`** — `SparklineType` (LINE, COLUMN или STACKED). Это свойство задаётся при добавлении группы, но можно прочитать его обратно для подтверждения.
- **`group.getLine().getColor()`** — цвет линии, выраженный как `CellsColor`, созданный с помощью `workbook.createCellsColor()`. Это свойство используется для задания цвета обводки линейного спарклайна.
- **`group.getLine().getWeight()`** — толщина линии в пунктах. Более высокие значения дают более толстые линии.
- **Маркеры точек максимума/минимума** — флаги, включающие небольшие маркеры на самой высокой и самой низкой точках данных, полезные для выделения экстремумов.
- **Маркеры первой/последней/отрицательной точек** — флаги, переключающие маркеры на первой, последней и отрицательной точках данных.
Чтобы изменить цвет, всегда создавайте экземпляр `CellsColor` и присваивайте его соответствующему свойству. Не присваивайте `java.awt.Color` напрямую свойствам цвета спарклайна — они ожидают тип `CellsColor` из `Aspose.Cells.Drawing`. Сам метод `add` возвращает полностью типизированный объект `SparklineGroup`, поэтому можно объединять присваивания свойств в цепочку на возвращаемом значении или сохранить его в локальной переменной и настроить перед сохранением.
{{% /alert %}}

{{< app/cells/assistant language="python" >}}
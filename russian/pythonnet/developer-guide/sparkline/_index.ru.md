---
title: Спарклайны в Aspose.Cells for Python via .NET
description: Aspose.Cells — это библиотека Python для работы с файлами электронных таблиц, которая поддерживает создание спарклайнов — миниатюрных диаграмм, размещаемых внутри ячеек рабочего листа. В этой статье объясняется, как добавлять и настраивать линейные, столбцовые спарклайны и спарклайны победа/поражение с помощью библиотеки Aspose.Cells.
linktitle: Спарклайны
keywords: Aspose.Cells, библиотека Python, электронная таблица, спарклайны, линейный спарклайн, столбцовый спарклайн, спарклайн победа/поражение, SparklineGroup, SparklineType
type: docs
weight: 195
url: /ru/python-net/creating-sparklines/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells поддерживает создание спарклайнов внутри ячеек рабочего листа. Спарклайны — это миниатюрные диаграммы, которые помещаются в одну ячейку и обеспечивают быстрое визуальное представление тенденций данных. Aspose.Cells поддерживает линейные, столбцовые спарклайны и спарклайны победа/поражение, каждый из которых можно настроить по цвету, толщине линии, точкам максимума/минимума и маркерам.

## **Введение**
Спарклайны — это крошечные внутриклеточные диаграммы, которые полезны, когда нужно отобразить кратковременную тенденцию рядом со строкой или столбцом данных, не занимая места полноценной диаграммы. Excel поддерживает три вида спарклайнов: **линейные**, **столбцовые** и **победа/поражение**. Aspose.Cells дублирует эту возможность через API `SparklineGroup` и `SparklineGroupCollection`, которые находятся в пространстве имён `aspose.cells.charts`.
В Aspose.Cells каждый добавляемый спарклайн создаётся через `worksheet.sparkline_groups.add(...)`, который возвращает объект `SparklineGroup`. Затем с помощью этого объекта можно задать тип спарклайна, диапазон данных, ячейку назначения и визуальные свойства, такие как цвет линии, толщина линии, маркеры и индикаторы точек максимума/минимума.
В этой статье рассматриваются все три типа спарклайнов, поддерживаемые Aspose.Cells — **Line**, **Column** и **Win/Loss** — и показано, как их добавлять, настраивать их цвета и сохранять полученную рабочую книгу.

## **Линейные спарклайны**
Линейный спарклайн проводит непрерывную линию через точки данных в ряде, что делает его наиболее естественным выбором для отображения тенденций во времени. В Aspose.Cells линейный спарклайн создаётся путём передачи `SparklineType.Line` методу `sparkline_groups.add`.
1. Создайте новую `Workbook` и откройте первый рабочий лист.
2. Заполните строку исходных данных (например, строка 1, столбцы A–E) значениями, которые вы хотите визуализировать.
3. Сформируйте `CellArea`, описывающую ячейку назначения, в которой будет отрисован спарклайн.
4. Вызовите `worksheet.sparkline_groups.add(SparklineType.Line, "A1:E1", False, dest)`. Третий аргумент — `False` — указывает Aspose.Cells, что диапазон данных горизонтальный (строка), а не вертикальный (столбец).
5. При необходимости настройте возвращённый `SparklineGroup`. Для линейного спарклайна можно задать цвет линии с помощью `group.line.color` (который ожидает `CellsColor` из `aspose.cells.drawing`), отрегулировать толщину линии и включить маркеры точек максимума/минимума.
6. Сохраните рабочую книгу.
Следующий пример создаёт рабочую книгу, записывает значения 5, -3, 8, -2, 6 в ячейки A1–E1 и добавляет линейный спарклайн в ячейку F1, который отслеживает эти значения. Также настраивается красный цвет линии и включаются маркеры для точек максимума и минимума.

## **Столбцовые спарклайны**
Столбцовый спарклайн отображает каждую точку данных в виде вертикальной полосы. Это делает его хорошо подходящим для данных, величина которых имеет значение — например, ежемесячных показателей продаж или количественных значений. В Aspose.Cells столбцовый спарклайн создаётся путём передачи `SparklineType.Column` методу `sparkline_groups.add`.
Процедура аналогична примеру с линейным спарклайном:
1. Создайте новую `Workbook` и откройте первый рабочий лист.
2. Заполните строку исходных данных (например, строка 1, столбцы A–E) значениями, которые вы хотите визуализировать.
3. Сформируйте `CellArea`, описывающую ячейку назначения.
4. Вызовите `worksheet.sparkline_groups.add(SparklineType.Column, "A1:E1", False, dest)`.
5. При необходимости настройте полученный `SparklineGroup` — например, задав `group.type` для подтверждения типа или скорректировав цвет полос.
6. Сохраните рабочую книгу в отдельный выходной файл, чтобы не перезаписать пример с линейным спарклайном.
В примере ниже значения 5, -3, 8, -2, 6 записываются в A1:E1 и отрисовывается столбцовый спарклайн в F1. Отрицательные значения отображаются в виде полос, направленных вниз, а положительные — в виде полос, направленных вверх, что позволяет легко увидеть положительный и отрицательный вклад.

```python
import aspose.cells as ac
# Шаг 1: Создайте рабочую книгу и получите первый рабочий лист
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Шаг 2: Запишите образцы значений в ячейки A1:E1
values = [5, -3, 8, -2, 6]
for i in range(len(values)):
    worksheet.cells[0, i].put_value(values[i])
# Шаг 3: Сформируйте CellArea, указывающую на F1 (индекс столбца 5, индекс строки 0)
dest = ac.CellArea()
dest.start_column = 5
dest.end_column = 5
dest.start_row = 0
dest.end_row = 0
# Шаг 4: Добавьте столбцовую спарклайн-диаграмму в целевую ячейку
idx = worksheet.sparkline_groups.add(
    ac.SparklineType.COLUMN, "A1:E1", False, dest)
group = worksheet.sparkline_groups[idx]
# Шаг 5: Подтвердите тип спарклайн-диаграммы, считав group.Type
print("Sparkline Type added: " + str(group.type))
# Шаг 6: Сохраните рабочую книгу
workbook.save("output_column.xlsx")
print("Workbook saved as output_column.xlsx")
```

## **Спарклайны победа/поражение**
Спарклайн победа/поражение — это особый вариант столбцового спарклайна, предназначенный для отображения только двух исходов: положительное значение отображается как «верхняя» полоса (победа), а нулевое или отрицательное значение — как «нижняя» полоса (поражение). Спарклайны победа/поражение обычно используются для визуализации последовательностей побед и поражений, результатов «пройдено/не пройдено» или любых бинарных исходов во времени.
В Aspose.Cells спарклайн победа/поражение создаётся путём передачи `SparklineType.Stacked` методу `sparkline_groups.add`. (Несмотря на название, `SparklineType.Stacked` — это значение перечисления, используемое для запроса отрисовки победа/поражение.)
1. Создайте новую `Workbook` и откройте первый рабочий лист.
2. Заполните диапазон исходных данных. Поскольку спарклайны победа/поражение трактуют каждое значение как победу или поражение, величина значения не имеет значения — важен только его знак. Положительные значения становятся верхними полосами, а неположительные — нижними.
3. Сформируйте `CellArea`, описывающую ячейку назначения.
4. Вызовите `worksheet.sparkline_groups.add(SparklineType.Stacked, "A1:E1", False, dest)`.
5. При необходимости настройте возвращённый `SparklineGroup`, например задав акцентные цвета для полос победы и поражения.
6. Сохраните рабочую книгу под уникальным именем файла, чтобы все три примера могли сосуществовать на диске.

## **Объединение всех трёх типов спарклайнов**
В комбинированном примере ниже создаётся одна рабочая книга, строка 1 заполняется значениями 5, -3, 8, -2, 6, а затем в ячейки F1, F2 и F3 добавляются три группы спарклайнов — по одной каждого типа — так что полученный файл демонстрирует все три стиля спарклайнов одновременно.

```python
import aspose.cells as ac
import System.Drawing
# Шаг 1: Создайте Workbook и получите первый рабочий лист
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Шаг 2: Заполните образец данных в строке 1 (A1:E1)
worksheet.cells["A1"].put_value(5)
worksheet.cells["B1"].put_value(-3)
worksheet.cells["C1"].put_value(8)
worksheet.cells["D1"].put_value(-2)
worksheet.cells["E1"].put_value(6)
# Шаг 3: Добавьте группу спарклайнов "Линия" в F1
line_area = ac.CellArea()
line_area.start_column = 5
line_area.end_column = 5
line_area.start_row = 0
line_area.end_row = 0
line_idx = worksheet.sparkline_groups.add(ac.SparklineType.LINE, "A1:E1", False, line_area)
line_group = worksheet.sparkline_groups[line_idx]
# Настройте цвет спарклайна "Линия" через CellsColor
line_color = workbook.create_cells_color()
line_color.color = System.Drawing.Color.Blue
line_group.series_color = line_color
# Шаг 4: Добавьте группу спарклайнов "Столбец" в F2
column_area = ac.CellArea()
column_area.start_column = 5
column_area.end_column = 5
column_area.start_row = 1
column_area.end_row = 1
column_idx = worksheet.sparkline_groups.add(ac.SparklineType.COLUMN, "A1:E1", False, column_area)
column_group = worksheet.sparkline_groups[column_idx]
# Настройте цвет серии спарклайна "Столбец"
column_color = workbook.create_cells_color()
column_color.color = System.Drawing.Color.Green
column_group.series_color = column_color
# Шаг 5: Добавьте группу спарклайнов "Победа/Поражение" (Составной) в F3
stacked_area = ac.CellArea()
stacked_area.start_column = 5
stacked_area.end_column = 5
stacked_area.start_row = 2
stacked_area.end_row = 2
stacked_idx = worksheet.sparkline_groups.add(ac.SparklineType.STACKED, "A1:E1", False, stacked_area)
stacked_group = worksheet.sparkline_groups[stacked_idx]
# Настройте цвет серии спарклайна "Победа/Поражение"
stacked_color = workbook.create_cells_color()
stacked_color.color = System.Drawing.Color.DarkOrange
stacked_group.series_color = stacked_color
# Шаг 6: Сохраните workbook
workbook.save("output_all.xlsx")
```

## **Настройка внешнего вида спарклайнов**
После создания и добавления `SparklineGroup` в `worksheet.sparkline_groups` можно прочитать или изменить несколько его визуальных свойств перед сохранением рабочей книги. Наиболее часто настраиваемые свойства:
- **`group.type`** — тип `SparklineType` (Line, Column или Stacked). Задаётся при добавлении группы, но можно прочитать его обратно для подтверждения.
- **`group.line.color`** — цвет линии, представленный как `CellsColor`, созданный с помощью `workbook.create_cells_color()`. Это свойство используется для цвета обводки линейного спарклайна.
- **`group.line.weight`** — толщина линии в пунктах. Большие значения дают более толстые линии.
- **Маркеры точек максимума/минимума** — флаги, включающие небольшие маркеры на самых высоких и самых низких точках данных, полезные для выделения экстремумов.
- **Маркеры первой/последней/отрицательной точек** — флаги, переключающие маркеры на первой, последней и отрицательной точках данных.
Чтобы изменить цвет, всегда создавайте экземпляр `CellsColor` и присваивайте его соответствующему свойству. Свойства цвета спарклайна ожидают тип `CellsColor` из `aspose.cells.drawing` — не присваивайте им непосредственно значение цвета. Сам метод `sparkline_groups.add` возвращает полностью типизированный объект `SparklineGroup`, поэтому можно либо сразу присваивать свойства возвращаемому значению, либо сохранить его в локальной переменной и настроить перед сохранением.
{{% /alert %}}python

```python
import aspose.cells as ac
import System.Drawing
# Step 1: Create a Workbook and get the first worksheet
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
cells = worksheet.cells
# Step 2: Write sample values 5, -3, 8, -2, 6 into cells A1:E1
cells["A1"].put_value(5)
cells["B1"].put_value(-3)
cells["C1"].put_value(8)
cells["D1"].put_value(-2)
cells["E1"].put_value(6)
# Step 3: Build a CellArea pointing to destination cell F1
dest = ac.CellArea()
dest.start_column = 5   # column F (0-indexed)
dest.end_column = 5
dest.start_row = 0      # row 1 (0-indexed)
dest.end_row = 0
# Step 4: Add a Line sparkline from A1:E1 into F1
# SparklineGroups.Add returns the index of the newly added group
index = worksheet.sparkline_groups.add(ac.SparklineType.LINE, "A1:E1", False, dest)
group = worksheet.sparkline_groups[index]
# Step 5: Create a red CellsColor and assign it to the sparkline line color
red = workbook.create_cells_color()
red.color = System.Drawing.Color.Red
group.series_color = red
# Step 6: Enable high-point and low-point markers
group.show_high_point = True
group.show_low_point = True
# Step 7: Save the workbook
workbook.save("output_line.xlsx")
```

```python
import aspose.cells as ac
import System.Drawing
# Step 1: Create a Workbook and get the first worksheet
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "WinLoss"
# Step 2: Populate sample data in row 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.cells["A1"].put_value(5)
worksheet.cells["B1"].put_value(-3)
worksheet.cells["C1"].put_value(8)
worksheet.cells["D1"].put_value(-2)
worksheet.cells["E1"].put_value(6)
# Step 3: Build a CellArea pointing to F1 (column 5, row 0)
dest = ac.CellArea()
dest.start_column = 5   # F
dest.end_column = 5
dest.start_row = 0      # row 1
dest.end_row = 0
# Step 4: Add a Win/Loss sparkline (SparklineType.Stacked)
group_index = worksheet.sparkline_groups.add(
    ac.SparklineType.Stacked,
    "A1:E1",
    False,
    dest)
group = worksheet.sparkline_groups[group_index]
# Step 5: Customize the sparkline group
# Enable high-point and low-point markers
group.show_high_point = True
group.show_low_point = True
group.show_negative_points = True
# Set the high-point color to green
high_color = workbook.create_cells_color()
high_color.color = System.Drawing.Color.Green
group.high_point_color = high_color
# Set the low-point color to red
low_color = workbook.create_cells_color()
low_color.color = System.Drawing.Color.Red
group.low_point_color = low_color
# Set the negative-point color to orange
neg_color = workbook.create_cells_color()
neg_color.color = System.Drawing.Color.Orange
group.negative_points_color = neg_color
# Set the default series color (used for positive bars)
series_color = workbook.create_cells_color()
series_color.color = System.Drawing.Color.SteelBlue
group.series_color = series_color
# Step 6: Save the workbook
workbook.save("output_winloss.xlsx")
print("Workbook saved successfully: output_winloss.xlsx")
```

{{< app/cells/assistant language="python" >}}
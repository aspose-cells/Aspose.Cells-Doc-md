---
title: Спарклайны в Aspose.Cells для Aspose.Cells for Python через .NET
linktitle: Sparklines
description: Aspose.Cells — это библиотека Python для работы с файлами электронных таблиц, которая поддерживает создание спарклайнов — миниатюрных диаграмм, размещаемых внутри ячеек рабочего листа. В этой статье объясняется, как добавлять и настраивать линейные, столбчатые спарклайны и спарклайны «выигрыш/проигрыш» с использованием библиотеки Aspose.Cells.
keywords: Aspose.Cells, библиотека Python, электронная таблица, спарклайны, линейный спарклайн, столбчатый спарклайн, спарклайн выигрыш/проигрыш, SparklineGroup, SparklineType
type: docs
weight: 195
url: /ru/python-net/creating-sparklines/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells поддерживает создание спарклайнов внутри ячеек рабочего листа. Спарклайны — это миниатюрные диаграммы, которые помещаются в одну ячейку и обеспечивают быстрое визуальное представление тенденций данных. Aspose.Cells поддерживает линейные, столбчатые спарклайны и спарклайны «выигрыш/проигрыш», каждый из которых можно настроить по цвету, толщине линии, точкам максимума/минимума и маркерам.

{{% /alert %}}

## **Введение**

Спарклайны — это крошечные внутриклеточные диаграммы, которые полезны, когда нужно отобразить быструю тенденцию рядом со строкой или столбцом данных, не занимая пространство полноценной диаграммы. Excel поддерживает три вида спарклайнов: **линейные**, **столбчатые** и **выигрыш/проигрыш**. Aspose.Cells дублирует эту возможность через API `SparklineGroup` и `SparklineGroupCollection`, расположенные в пространстве имён `aspose.cells.charts`.

В Aspose.Cells каждый добавляемый вами спарклайн создаётся с помощью `worksheet.sparkline_groups.add(...)`, который возвращает объект `SparklineGroup`. Затем вы можете использовать этот объект для задания типа спарклайна, диапазона данных, целевой ячейки и визуальных свойств, таких как цвет линии, толщина линии, маркеры и индикаторы точек максимума/минимума.

{{% alert color="primary" %}}

Один объект `SparklineGroup` может содержать один или несколько спарклайнов, имеющих общий стиль. Когда вы вызываете `add` и передаёте строку данных и одну целевую ячейку, вы получаете один спарклайн внутри этой ячейки. Если ваш целевой диапазон шире одной ячейки, отдельный спарклайн рисуется в каждой целевой ячейке, и все они используют один и тот же стиль и диапазон данных.

{{% /alert %}}

В этой статье рассматриваются все три типа спарклайнов, поддерживаемых Aspose.Cells — **линейные**, **столбчатые** и **выигрыш/проигрыш** — и показано, как их добавлять, настраивать их цвета и сохранять полученную рабочую книгу.

## **Линейные спарклайны**

Линейный спарклайн рисует непрерывную линию через точки данных в серии, что делает его наиболее естественным выбором для отображения тенденций во времени. В Aspose.Cells линейный спарклайн создаётся путём передачи `SparklineType.Line` в метод `sparkline_groups.add`.

Рабочий процесс аналогичен любому другому типу спарклайна:

1. Создайте новый `Workbook` и откройте первый рабочий лист.
2. Заполните строку исходных данных (например, строка 1, столбцы от A до E) значениями, которые вы хотите визуализировать.
3. Создайте объект `CellArea`, описывающий целевую ячейку, в которой будет нарисован спарклайн.
4. Вызовите `worksheet.sparkline_groups.add(SparklineType.Line, "A1:E1", False, dest)`. Третий аргумент — `False` — сообщает Aspose.Cells, что диапазон данных горизонтальный (строка), а не вертикальный (столбец).
5. При необходимости настройте возвращённый `SparklineGroup`. Для линейного спарклайна вы можете задать цвет линии с помощью `group.line.color` (который ожидает `CellsColor` из `aspose.cells.drawing`), отрегулировать толщину линии и включить маркеры точек максимума/минимума.
6. Сохраните рабочую книгу.

В следующем примере создаётся рабочая книга, значения 5, -3, 8, -2, 6 записываются в ячейки от A1 до E1, и в ячейку F1 добавляется линейный спарклайн, отслеживающий эти значения. Также настраивается красный цвет линии и включаются маркеры для точек максимума и минимума.

```python
import aspose.cells as ac
import System.Drawing

# Шаг 1: Создайте рабочую книгу и получите первый рабочий лист
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
cells = worksheet.cells

# Шаг 2: Запишите примеры значений 5, -3, 8, -2, 6 в ячейки A1:E1
cells["A1"].put_value(5)
cells["B1"].put_value(-3)
cells["C1"].put_value(8)
cells["D1"].put_value(-2)
cells["E1"].put_value(6)

# Шаг 3: Создайте CellArea, указывающую на целевую ячейку F1
dest = ac.CellArea()
dest.start_column = 5   # столбец F (с индексом 0)
dest.end_column = 5
dest.start_row = 0      # строка 1 (с индексом 0)
dest.end_row = 0

# Шаг 4: Добавьте спарклайн-линию из A1:E1 в F1
# SparklineGroups.Add возвращает индекс вновь добавленной группы
index = worksheet.sparkline_groups.add(ac.SparklineType.LINE, "A1:E1", False, dest)
group = worksheet.sparkline_groups[index]

# Шаг 5: Создайте красный CellsColor и назначьте его цвету линии спарклайна
red = workbook.create_cells_color()
red.color = System.Drawing.Color.Red
group.series_color = red

# Шаг 6: Включите маркеры высоких и низких точек
group.show_high_point = True
group.show_low_point = True

# Шаг 7: Сохраните рабочую книгу
workbook.save("output_line.xlsx")
```

## **Столбчатые спарклайны**

Столбчатый спарклайн отображает каждую точку данных в виде вертикальной полосы. Это делает его хорошо подходящим для данных, величина которых имеет значение — например, ежемесячных показателей продаж или подсчётов. В Aspose.Cells столбчатый спарклайн создаётся путём передачи `SparklineType.Column` в метод `sparkline_groups.add`.

Процедура аналогична примеру с линейным спарклайном:

1. Создайте новый `Workbook` и откройте первый рабочий лист.
2. Заполните тот же исходный диапазон (A1:E1) значениями, которые вы хотите визуализировать.
3. Создайте объект `CellArea`, описывающий целевую ячейку.
4. Вызовите `worksheet.sparkline_groups.add(SparklineType.Column, "A1:E1", False, dest)`.
5. При необходимости настройте полученный `SparklineGroup` — например, задав `group.type` для подтверждения типа или изменив цвет полос.
6. Сохраните рабочую книгу в отдельный выходной файл, чтобы она не перезаписала пример с линейным спарклайном.

В примере ниже значения 5, -3, 8, -2, 6 записываются в A1:E1 и в F1 отрисовывается столбчатый спарклайн. Отрицательные значения отображаются в виде полос, направленных вниз, а положительные — в виде полос, направленных вверх, что позволяет легко определить положительный и отрицательный вклад при первом взгляде.

```python
import aspose.cells as ac

# Шаг 1: Создайте Workbook и получите первый рабочий лист
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Шаг 2: Запишите образцы значений в A1:E1
values = [5, -3, 8, -2, 6]
for i in range(len(values)):
    worksheet.cells[0, i].put_value(values[i])

# Шаг 3: Создайте CellArea, указывающую на F1 (индекс столбца 5, индекс строки 0)
dest = ac.CellArea()
dest.start_column = 5
dest.end_column = 5
dest.start_row = 0
dest.end_row = 0

# Шаг 4: Добавьте спарклайн столбцов в ячейку назначения
idx = worksheet.sparkline_groups.add(
    ac.SparklineType.COLUMN, "A1:E1", False, dest)
group = worksheet.sparkline_groups[idx]

# Шаг 5: Подтвердите тип спарклайна, прочитав group.Type
print("Sparkline Type added: " + str(group.type))

# Шаг 6: Сохраните workbook
workbook.save("output_column.xlsx")

print("Workbook saved as output_column.xlsx")
```

## **Спарклайны «выигрыш/проигрыш»**

Спарклайн «выигрыш/проигрыш» — это особый вариант столбчатого спарклайна, предназначенный для отображения только двух исходов: положительное значение рисуется как полоса вверх (выигрыш), а нулевое или отрицательное значение — как полоса вниз (проигрыш). Спарклайны «выигрыш/проигрыш» обычно используются для визуализации последовательностей побед и поражений, результатов «сдал/не сдал» или любого бинарного исхода во времени.

В Aspose.Cells спарклайн «выигрыш/проигрыш» создаётся путём передачи `SparklineType.Stacked` в метод `sparkline_groups.add`. (Несмотря на название, `SparklineType.Stacked` — это значение перечисления, используемое для запроса отрисовки «выигрыш/проигрыш».)

Процедура такая же, как для двух других типов:

1. Создайте новый `Workbook` и откройте первый рабочий лист.
2. Заполните исходный диапазон. Поскольку спарклайны «выигрыш/проигрыш» рассматривают каждое значение либо как выигрыш, либо как проигрыш, величина значения не имеет значения — важен только его знак. Положительные значения становятся полосами вверх, а неположительные — полосами вниз.
3. Создайте объект `CellArea`, описывающий целевую ячейку.
4. Вызовите `worksheet.sparkline_groups.add(SparklineType.Stacked, "A1:E1", False, dest)`.
5. При необходимости настройте возвращённый `SparklineGroup`, например, задав акцентные цвета для полос выигрыша и проигрыша.
6. Сохраните рабочую книгу под отличным именем файла, чтобы все три примера могли сосуществовать на диске.

В примере ниже используются те же входные данные, что и в предыдущих двух разделах. Значения 5, -3, 8, -2, 6 интерпретируются как выигрыш, проигрыш, выигрыш, проигрыш, выигрыш — и спарклайн, нарисованный в F1, точно отражает этот шаблон.

```python
import aspose.cells as ac
import System.Drawing

# Шаг 1: Создаем книгу и получаем первый рабочий лист
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "WinLoss"

# Шаг 2: Заполняем образцы данных в строке 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.cells["A1"].put_value(5)
worksheet.cells["B1"].put_value(-3)
worksheet.cells["C1"].put_value(8)
worksheet.cells["D1"].put_value(-2)
worksheet.cells["E1"].put_value(6)

# Шаг 3: Создаем CellArea, указывающую на F1 (столбец 5, строка 0)
dest = ac.CellArea()
dest.start_column = 5   # F
dest.end_column = 5
dest.start_row = 0      # строка 1
dest.end_row = 0

# Шаг 4: Добавляем спарклайн Win/Loss (SparklineType.Stacked)
group_index = worksheet.sparkline_groups.add(
    ac.SparklineType.Stacked,
    "A1:E1",
    False,
    dest)
group = worksheet.sparkline_groups[group_index]

# Шаг 5: Настраиваем группу спарклайнов
# Включаем маркеры высоких и низких точек
group.show_high_point = True
group.show_low_point = True
group.show_negative_points = True

# Устанавливаем зеленый цвет для высоких точек
high_color = workbook.create_cells_color()
high_color.color = System.Drawing.Color.Green
group.high_point_color = high_color

# Устанавливаем красный цвет для низких точек
low_color = workbook.create_cells_color()
low_color.color = System.Drawing.Color.Red
group.low_point_color = low_color

# Устанавливаем оранжевый цвет для отрицательных точек
neg_color = workbook.create_cells_color()
neg_color.color = System.Drawing.Color.Orange
group.negative_points_color = neg_color

# Устанавливаем цвет серии по умолчанию (используется для положительных столбцов)
series_color = workbook.create_cells_color()
series_color.color = System.Drawing.Color.SteelBlue
group.series_color = series_color

# Шаг 6: Сохраняем книгу
workbook.save("output_winloss.xlsx")

print("Workbook saved successfully: output_winloss.xlsx")
```

## **Объединение всех трёх типов спарклайнов**

Каждый из предыдущих трёх примеров создаёт свою рабочую книгу, чтобы выходные файлы было легко изучать изолированно. Однако в реальном сценарии вы часто захотите сравнить несколько серий данных бок о бок. Самый простой способ сделать это — поместить более одной группы спарклайнов в один рабочий лист, где каждая группа отображает свой стиль.

Вы можете добавить несколько объектов `SparklineGroup` в одну и ту же коллекцию `SparklineGroupCollection`, и каждая группа может быть направлена на другую целевую ячейку или другой диапазон. Например, можно разместить линейный спарклайн в F1, столбчатый спарклайн в F2 и спарклайн «выигрыш/проигрыш» в F3 — все они считывают данные из одного источника в строке 1 — чтобы читатель мог увидеть три различных визуальных представления одних и тех же чисел.

В комбинированном примере ниже создаётся одна рабочая книга, строка 1 заполняется значениями 5, -3, 8, -2, 6, а затем в ячейки F1, F2 и F3 добавляются три группы спарклайнов — по одной каждого типа — так что полученный файл демонстрирует все три стиля спарклайнов одновременно.

```python
import aspose.cells as ac
import System.Drawing

# Шаг 1: Создаём Workbook и получаем первый рабочий лист
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Шаг 2: Заполняем пример данных в строке 1 (A1:E1)
worksheet.cells["A1"].put_value(5)
worksheet.cells["B1"].put_value(-3)
worksheet.cells["C1"].put_value(8)
worksheet.cells["D1"].put_value(-2)
worksheet.cells["E1"].put_value(6)

# Шаг 3: Добавляем группу линейных спарклайнов в F1
line_area = ac.CellArea()
line_area.start_column = 5
line_area.end_column = 5
line_area.start_row = 0
line_area.end_row = 0
line_idx = worksheet.sparkline_groups.add(ac.SparklineType.LINE, "A1:E1", False, line_area)
line_group = worksheet.sparkline_groups[line_idx]

# Настраиваем цвет линейного спарклайна через CellsColor
line_color = workbook.create_cells_color()
line_color.color = System.Drawing.Color.Blue
line_group.series_color = line_color

# Шаг 4: Добавляем группу столбчатых спарклайнов в F2
column_area = ac.CellArea()
column_area.start_column = 5
column_area.end_column = 5
column_area.start_row = 1
column_area.end_row = 1
column_idx = worksheet.sparkline_groups.add(ac.SparklineType.COLUMN, "A1:E1", False, column_area)
column_group = worksheet.sparkline_groups[column_idx]

# Настраиваем цвет серии столбчатого спарклайна
column_color = workbook.create_cells_color()
column_color.color = System.Drawing.Color.Green
column_group.series_color = column_color

# Шаг 5: Добавляем группу спарклайнов Win/Loss (Stacked) в F3
stacked_area = ac.CellArea()
stacked_area.start_column = 5
stacked_area.end_column = 5
stacked_area.start_row = 2
stacked_area.end_row = 2
stacked_idx = worksheet.sparkline_groups.add(ac.SparklineType.STACKED, "A1:E1", False, stacked_area)
stacked_group = worksheet.sparkline_groups[stacked_idx]

# Настраиваем цвет серии спарклайна win/loss
stacked_color = workbook.create_cells_color()
stacked_color.color = System.Drawing.Color.DarkOrange
stacked_group.series_color = stacked_color

# Шаг 6: Сохраняем книгу
workbook.save("output_all.xlsx")
```

{{% alert color="primary" %}}

Когда вы объединяете несколько групп спарклайнов в одном рабочем листе, каждая группа независима. Они могут совместно использовать один и тот же исходный диапазон или использовать разные исходные диапазоны, и они могут быть стилизованы независимо. Это позволяет легко создать небольшую «панель мониторинга» внутриклеточных визуализаций непосредственно внутри существующего рабочего листа.

{{% /alert %}}

## **Настройка внешнего вида спарклайнов**

После того как `SparklineGroup` создан и добавлен в `worksheet.sparkline_groups`, вы можете считать или изменить несколько его визуальных свойств перед сохранением рабочей книги. Наиболее часто настраиваемые свойства:

- **`group.type`** — тип `SparklineType` (Line, Column или Stacked). Он задаётся при добавлении группы, но вы можете прочитать его обратно для подтверждения.
- **`group.line.color`** — цвет линии, выраженный как `CellsColor`, созданный с помощью `workbook.create_cells_color()`. Это свойство используется для цвета обводки линейного спарклайна.
- **`group.line.weight`** — толщина линии в пунктах. Более высокие значения дают более толстые линии.
- **Маркеры точек максимума/минимума** — флаги, которые включают маленькие маркеры в самых высоких и самых низких точках данных, что полезно для выделения экстремумов.
- **Маркеры первой/последней/отрицательной точки** — флаги, которые переключают маркеры на первой, последней и отрицательной точках данных.

Чтобы изменить цвет, всегда создавайте экземпляр `CellsColor` и присваивайте его соответствующему свойству. Свойства цвета спарклайна ожидают тип `CellsColor` из `aspose.cells.drawing` — не присваивайте им непосредственно значение цвета в чистом виде. Сам метод `sparkline_groups.add` возвращает полностью типизированный объект `SparklineGroup`, поэтому вы можете объединять присваивания свойств в цепочку на возвращаемом значении или сохранить его в локальной переменной и настроить перед сохранением.



{{< app/cells/assistant language="python" >}}
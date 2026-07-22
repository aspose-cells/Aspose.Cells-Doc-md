---
title: Спарклайны в Aspose.Cells for Node.js via C++
linktitle: Спарклайны
description: Aspose.Cells — это библиотека Node.js для работы с файлами электронных таблиц, которая поддерживает создание спарклайнов — миниатюрных диаграмм, размещаемых внутри ячеек рабочего листа. В этой статье объясняется, как добавлять и настраивать спарклайны-линии, спарклайны-столбцы и спарклайны «победа/поражение» с использованием библиотеки Aspose.Cells.
keywords: Aspose.Cells, библиотека Node.js, электронная таблица, спарклайны, спарклайн-линия, спарклайн-столбец, спарклайн победа/поражение, SparklineGroup, SparklineType
type: docs
weight: 195
url: /ru/nodejs-cpp/creating-sparklines/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells поддерживает создание спарклайнов внутри ячеек рабочего листа. Спарклайны — это миниатюрные диаграммы, которые помещаются в одну ячейку и обеспечивают быстрое визуальное представление тенденций данных. Aspose.Cells поддерживает спарклайны-линии, спарклайны-столбцы и спарклайны «победа/поражение», каждый из которых можно настроить с точки зрения цвета, толщины линии, точек максимума/минимума и маркеров.

{{% /alert %}}

## **Введение**

Спарклайны — это крошечные диаграммы внутри ячеек, которые полезны, когда требуется отобразить быструю тенденцию рядом со строкой или столбцом данных, не занимая пространство полноценной диаграммы. Excel поддерживает три вида спарклайнов: **линия**, **столбец** и **победа/поражение**. Aspose.Cells воспроизводит эту возможность через API `SparklineGroup` и `SparklineGroupCollection`, расположенные в пространстве имён `Aspose.Cells.Charts`.

В Aspose.Cells каждый добавляемый спарклайн создаётся с помощью `worksheet.sparklineGroups.add(...)`, который возвращает объект `SparklineGroup`. Затем этот объект можно использовать для задания типа спарклайна, диапазона данных, целевой ячейки и визуальных свойств, таких как цвет линии, толщина линии, маркеры и индикаторы точек максимума/минимума.

{{% alert color="primary" %}}

Один `SparklineGroup` может содержать один или несколько спарклайнов, имеющих общий стиль. Когда вы вызываете `add` и передаёте строку данных плюс одну целевую ячейку, вы получаете один спарклайн внутри этой ячейки. Если ваш целевой диапазон шире одной ячейки, в каждой целевой ячейке рисуется отдельный спарклайн, причём все они используют один и тот же стиль и диапазон данных.

{{% /alert %}}

В этой статье рассматривается каждый из трёх типов спарклайнов, поддерживаемых Aspose.Cells — **линия**, **столбец** и **победа/поражение** — и показывается, как их добавлять, настраивать их цвета и сохранять полученную рабочую книгу.

## **Спарклайны-линии**

Спарклайн-линия рисует непрерывную линию через точки данных в серии, что делает его наиболее естественным выбором для отображения тенденций во времени. В Aspose.Cells спарклайн-линия создаётся путём передачи `SparklineType.Line` в метод `sparklineGroups.add`.

Рабочий процесс аналогичен любому другому типу спарклайна:

1. Создайте новую `Workbook` и откройте первый рабочий лист.
2. Заполните строку исходных данных (например, строка 1, столбцы от A до E) значениями, которые вы хотите визуализировать.
3. Постройте `CellArea`, описывающую целевую ячейку, в которой будет нарисован спарклайн.
4. Вызовите `worksheet.sparklineGroups.add(SparklineType.Line, "A1:E1", false, dest)`. Третий аргумент — `false` — указывает Aspose.Cells, что диапазон данных горизонтальный (строка), а не вертикальный (столбец).
5. При необходимости настройте возвращённый `SparklineGroup`. Для спарклайна-линии вы можете задать цвет линии с помощью `group.line.color` (который ожидает `CellsColor` из `Aspose.Cells.Drawing`), настроить толщину линии и включить маркеры точек максимума/минимума.
6. Сохраните рабочую книгу.

Следующий пример создаёт рабочую книгу, записывает значения 5, -3, 8, -2, 6 в ячейки A1–E1 и добавляет спарклайн-линию в ячейку F1, которая отслеживает эти значения. Он также настраивает цвет линии на красный и включает маркеры для точек максимума и минимума.

```javascript
const AsposeCells = require("aspose.cells");

// Шаг 1: Создаём Workbook и получаем первый лист
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();

// Шаг 2: Записываем значения 5, -3, 8, -2, 6 в ячейки A1:E1
cells.get("A1").putValue(5);
cells.get("B1").putValue(-3);
cells.get("C1").putValue(8);
cells.get("D1").putValue(-2);
cells.get("E1").putValue(6);

// Шаг 3: Создаём CellArea, указывающий на целевую ячейку F1
const dest = new AsposeCells.CellArea();
dest.setStartColumn(5);   // столбец F (индекс с нуля)
dest.setEndColumn(5);
dest.setStartRow(0);      // строка 1 (индекс с нуля)
dest.setEndRow(0);

// Шаг 4: Добавляем линейную спарклайн-диаграмму из A1:E1 в ячейку F1
// SparklineGroups.Add возвращает индекс добавленной группы
const index = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, dest);
const group = worksheet.getSparklineGroups().get(index);

// Шаг 5: Создаём красный цвет CellsColor и назначаем его цвету линии спарклайн-диаграммы
const red = workbook.createCellsColor();
red.setColor(AsposeCells.Color.fromArgb(255, 0, 0));
group.setSeriesColor(red);

// Шаг 6: Включаем маркеры максимальных и минимальных точек
group.setShowHighPoint(true);
group.setShowLowPoint(true);

// Шаг 7: Сохраняем книгу
workbook.save("output_line.xlsx");
```

## **Спарклайны-столбцы**

Спарклайн-столбец отображает каждую точку данных в виде вертикальной полосы. Это делает его хорошо подходящим для данных, величина которых имеет значение — например, ежемесячных показателей продаж или подсчётов. В Aspose.Cells спарклайн-столбец создаётся путём передачи `SparklineType.Column` в метод `sparklineGroups.add`.

Процедура повторяет пример со спарклайном-линией:

1. Создайте новую `Workbook` и откройте первый рабочий лист.
2. Заполните тот же исходный диапазон (A1:E1) значениями, которые вы хотите визуализировать.
3. Постройте `CellArea`, описывающую целевую ячейку.
4. Вызовите `worksheet.sparklineGroups.add(SparklineType.Column, "A1:E1", false, dest)`.
5. При необходимости настройте полученный `SparklineGroup` — например, путём установки `group.type` для подтверждения типа или путём корректировки цвета полос.
6. Сохраните рабочую книгу в отдельный выходной файл, чтобы не перезаписать пример со спарклайном-линией.

Пример ниже записывает значения 5, -3, 8, -2, 6 в A1:E1 и отображает спарклайн-столбец в F1. Отрицательные значения рисуются как полосы, направленные вниз, а положительные — как полосы, направленные вверх, что позволяет легко разглядеть положительные и отрицательные вклады с первого взгляда.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Шаг 2: Записать примеры значений в ячейки A1:E1
let values = [5, -3, 8, -2, 6];
for (let i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}

// Шаг 3: Создать CellArea, указывающую на F1 (индекс столбца 5, индекс строки 0)
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);

// Шаг 4: Добавить столбцовую спарклайн-линию в целевую ячейку
let idx = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Column, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(idx);

// Шаг 5: Подтвердить тип спарклайн-линии, прочитав group.Type
console.log("Sparkline Type added: " + group.getType());

// Шаг 6: Сохранить книгу
workbook.save("output_column.xlsx");

console.log("Workbook saved as output_column.xlsx");
```

## **Спарклайны «победа/поражение»**

Спарклайн «победа/поражение» — это особый вариант спарклайна-столбца, предназначенный для отображения только двух исходов: положительное значение рисуется как «верхняя» полоса (победа), а нулевое или отрицательное — как «нижняя» полоса (поражение). Спарклайны «победа/поражение» обычно используются для визуализации последовательностей побед и поражений, результатов «прошёл/не прошёл» или любого двоичного исхода во времени.

В Aspose.Cells спарклайн «победа/поражение» создаётся путём передачи `SparklineType.Stacked` в метод `sparklineGroups.add`. (Несмотря на название, `SparklineType.Stacked` — это значение перечисления, используемое для запроса отображения «победа/поражение».)

Процедура аналогична двум другим типам:

1. Создайте новую `Workbook` и откройте первый рабочий лист.
2. Заполните исходный диапазон. Поскольку спарклайны «победа/поражение» трактуют каждое значение либо как победу, либо как поражение, величина значения не имеет значения — важен только его знак. Положительные значения становятся верхними полосами, а неположительные — нижними.
3. Постройте `CellArea`, описывающую целевую ячейку.
4. Вызовите `worksheet.sparklineGroups.add(SparklineType.Stacked, "A1:E1", false, dest)`.
5. При необходимости настройте возвращённый `SparklineGroup`, например, задав акцентные цвета для полос победы и поражения.
6. Сохраните рабочую книгу под отличающимся именем файла, чтобы все три примера могли сосуществовать на диске.

Пример ниже использует те же входные данные, что и два предыдущих раздела. Значения 5, -3, 8, -2, 6 интерпретируются как победа, поражение, победа, поражение, победа — и спарклайн, нарисованный в F1, в точности отражает этот шаблон.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("WinLoss");

// Шаг 2: Заполнение образцов данных в строке 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// Шаг 3: Создание CellArea, указывающей на F1 (столбец 5, строка 0)
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);   // F
dest.setEndColumn(5);
dest.setStartRow(0);      // строка 1
dest.setEndRow(0);

// Шаг 4: Добавление спарклайна Win/Loss (SparklineType.Stacked)
let groupIndex = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Stacked,
    "A1:E1",
    false,
    dest);
let group = worksheet.getSparklineGroups().get(groupIndex);

// Шаг 5: Настройка группы спарклайнов
// Включение маркеров верхних и нижних точек
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);

// Установка зелёного цвета для маркера верхней точки
let highColor = workbook.createCellsColor();
highColor.setColor(AsposeCells.Color.Green);
group.setHighPointColor(highColor);

// Установка красного цвета для маркера нижней точки
let lowColor = workbook.createCellsColor();
lowColor.setColor(AsposeCells.Color.Red);
group.setLowPointColor(lowColor);

// Установка оранжевого цвета для маркера отрицательных точек
let negColor = workbook.createCellsColor();
negColor.setColor(AsposeCells.Color.Orange);
group.setNegativePointsColor(negColor);

// Установка цвета серии по умолчанию (используется для положительных столбцов)
let seriesColor = workbook.createCellsColor();
seriesColor.setColor(AsposeCells.Color.SteelBlue);
group.setSeriesColor(seriesColor);

// Шаг 6: Сохранение книги
workbook.save("output_winloss.xlsx");

console.log("Книга успешно сохранена: output_winloss.xlsx");
```

## **Объединение всех трёх типов спарклайнов**

Каждый из предыдущих трёх примеров создаёт свою рабочую книгу, чтобы выходные файлы было легко изучать изолированно. Однако в реальном сценарии вам часто захочется сравнить несколько серий данных бок о бок. Самый чистый способ сделать это — поместить более одной группы спарклайнов в один и тот же рабочий лист, причём каждая группа отображает свой стиль.

Вы можете добавить несколько объектов `SparklineGroup` в одну и ту же `SparklineGroupCollection`, и каждая группа может быть нацелена на разную целевую ячейку или разный диапазон. Например, вы можете разместить спарклайн-линию в F1, спарклайн-столбец в F2 и спарклайн «победа/поражение» в F3 — все они считывают данные из одного и того же источника в строке 1 — чтобы читатель мог видеть три различных визуальных представления одних и тех же чисел.

Комбинированный пример ниже создаёт одну рабочую книгу, заполняет строку 1 значениями 5, -3, 8, -2, 6, а затем добавляет три группы спарклайнов в ячейки F1, F2 и F3 — по одной каждого типа — так, чтобы полученный файл демонстрировал все три стиля спарклайнов одновременно.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Шаг 2: Заполнение образцов данных в строке 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// Шаг 3: Добавление группы линейных спарклайнов в F1
let lineArea = new AsposeCells.CellArea();
lineArea.setStartColumn(5);
lineArea.setEndColumn(5);
lineArea.setStartRow(0);
lineArea.setEndRow(0);
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, lineArea);
let lineGroup = worksheet.getSparklineGroups().get(lineIdx);

// Настройка цвета линейного спарклайна через CellsColor
let lineColor = workbook.createCellsColor();
lineColor.setColor(AsposeCells.Color.Blue);
lineGroup.setSeriesColor(lineColor);

// Шаг 4: Добавление группы столбчатых спарклайнов в F2
let columnArea = new AsposeCells.CellArea();
columnArea.setStartColumn(5);
columnArea.setEndColumn(5);
columnArea.setStartRow(1);
columnArea.setEndRow(1);
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "A1:E1", false, columnArea);
let columnGroup = worksheet.getSparklineGroups().get(columnIdx);

// Настройка цвета серии столбчатого спарклайна
let columnColor = workbook.createCellsColor();
columnColor.setColor(AsposeCells.Color.Green);
columnGroup.setSeriesColor(columnColor);

// Шаг 5: Добавление группы спарклайнов "Победа/Поражение" (составной) в F3
let stackedArea = new AsposeCells.CellArea();
stackedArea.setStartColumn(5);
stackedArea.setEndColumn(5);
stackedArea.setStartRow(2);
stackedArea.setEndRow(2);
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);
let stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);

// Настройка цвета серии спарклайна "Победа/Поражение"
let stackedColor = workbook.createCellsColor();
stackedColor.setColor(AsposeCells.Color.DarkOrange);
stackedGroup.setSeriesColor(stackedColor);

// Шаг 6: Сохранение книги
workbook.save("output_all.xlsx");
```

{{% alert color="primary" %}}

Когда вы объединяете несколько групп спарклайнов на одном рабочем листе, каждая группа независима. Они могут совместно использовать один и тот же исходный диапазон или использовать разные исходные диапазоны, и они могут быть оформлены независимо. Это упрощает построение небольшой «информационной панели» визуализаций внутри ячеек непосредственно в существующем рабочем листе.

{{% /alert %}}

## **Настройка внешнего вида спарклайнов**

После того как `SparklineGroup` создан и добавлен в `worksheet.sparklineGroups`, вы можете считывать или изменять ряд его визуальных свойств перед сохранением рабочей книги. Наиболее часто настраиваемыми свойствами являются:

- **`group.type`** — `SparklineType` (Line, Column или Stacked). Он задаётся при добавлении группы, но вы можете прочитать его для подтверждения.
- **`group.line.color`** — цвет линии, выраженный как `CellsColor`, созданный с помощью `workbook.createCellsColor()`. Это свойство используется для цвета обводки спарклайна-линии.
- **`group.line.weight`** — толщина линии в пунктах. Более высокие значения дают более толстые линии.
- **Маркеры точек максимума/минимума** — флаги, включающие небольшие маркеры на точках данных с наибольшим и наименьшим значениями, полезные для подчёркивания экстремумов.
- **Маркеры первой/последней/отрицательной точек** — флаги, переключающие маркеры на первой, последней и отрицательной точках данных.

Чтобы изменить цвет, всегда создавайте экземпляр `CellsColor` и присваивайте его соответствующему свойству. Не присваивайте `System.Drawing.Color` напрямую свойствам цвета спарклайна — они ожидают тип `CellsColor` из `Aspose.Cells.Drawing`. Сам метод `sparklineGroups.add` возвращает полностью типизированный объект `SparklineGroup`, поэтому вы можете связывать присваивания свойств с возвращаемым значением или сохранить его в локальной переменной и настроить перед сохранением.



{{< app/cells/assistant language="javascript" >}}
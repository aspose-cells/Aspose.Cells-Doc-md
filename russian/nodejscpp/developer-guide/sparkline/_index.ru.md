---
title: Спарклайны в Aspose.Cells for Node.js via C++
linktitle: Спарклайны в Aspose.Cells for Node.js via C++
description: Aspose.Cells — это библиотека Node.js для работы с файлами электронных таблиц, которая поддерживает создание спарклайнов — миниатюрных диаграмм, размещаемых внутри ячеек рабочего листа. В этой статье объясняется, как добавлять и настраивать линейные, столбцовые спарклайны и спарклайны победа/поражение с помощью библиотеки Aspose.Cells.
keywords: Aspose.Cells, библиотека Node.js, электронная таблица, спарклайны, линейный спарклайн, столбцовый спарклайн, спарклайн победа/поражение, SparklineGroup, SparklineType
type: docs
weight: 195
url: /ru/nodejs-cpp/creating-sparklines/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells поддерживает создание спарклайнов внутри ячеек рабочего листа. Спарклайны — это миниатюрные диаграммы, которые помещаются в одну ячейку и обеспечивают быстрое наглядное отображение тенденций данных. Aspose.Cells поддерживает линейные, столбцовые спарклайны и спарклайны победа/поражение, каждый из которых можно настроить по цвету, толщине линии, верхним/нижним точкам и маркерам.

## **Введение**
Спарклайны — это крошечные диаграммы, встраиваемые в ячейки, которые полезны, когда требуется отобразить быструю тенденцию рядом со строкой или столбцом данных, не занимая места полноценной диаграммы. Excel поддерживает три вида спарклайнов: **линейный**, **столбцовый** и **победа/поражение**. Aspose.Cells дублирует эту возможность через API `SparklineGroup` и `SparklineGroupCollection`, которые находятся в пространстве имён `Aspose.Cells.Charts`.
В Aspose.Cells каждый добавляемый вами спарклайн создаётся с помощью `worksheet.sparklineGroups.add(...)`, который возвращает объект `SparklineGroup`. Затем вы можете использовать этот объект для задания типа спарклайна, диапазона данных, целевой ячейки и визуальных свойств, таких как цвет линии, толщина линии, маркеры и индикаторы верхних/нижних точек.
В этой статье рассматривается каждый из трёх типов спарклайнов, поддерживаемых Aspose.Cells — **Линейный**, **Столбцовый** и **Победа/Поражение** — и показывается, как их добавлять, настраивать их цвета и сохранять полученную рабочую книгу.

## **Линейные спарклайны**
Линейный спарклайн рисует непрерывную линию через точки данных в серии, что делает его наиболее естественным выбором для отображения тенденций во времени. В Aspose.Cells линейный спарклайн создаётся путём передачи `SparklineType.Line` методу `sparklineGroups.add`.
1. Создайте новую `Workbook` и откройте первый рабочий лист.
2. Заполните строку исходными данными (например, строка 1, столбцы от A до E) значениями, которые вы хотите визуализировать.
3. Создайте `CellArea`, описывающую целевую ячейку, в которой будет нарисован спарклайн.
4. Вызовите `worksheet.sparklineGroups.add(SparklineType.Line, "A1:E1", false, dest)`. Третий аргумент — `false` — сообщает Aspose.Cells, что диапазон данных горизонтальный (строка), а не вертикальный (столбец).
5. При необходимости настройте возвращённый `SparklineGroup`. Для линейного спарклайна можно задать цвет линии с помощью `group.line.color` (который ожидает `CellsColor` из `Aspose.Cells.Drawing`), отрегулировать толщину линии и переключать маркеры верхних/нижних точек.
6. Сохраните рабочую книгу.
Следующий пример создаёт рабочую книгу, записывает значения 5, -3, 8, -2, 6 в ячейки от A1 до E1 и добавляет линейный спарклайн в ячейку F1, который отслеживает эти значения. Также он настраивает цвет линии на красный и включает маркеры для верхних и нижних точек.

```javascript
const AsposeCells = require("aspose.cells");
// Шаг 1: Создаём Workbook и получаем первый лист
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();
// Шаг 2: Записываем пример значений 5, -3, 8, -2, 6 в ячейки A1:E1
cells.get("A1").putValue(5);
cells.get("B1").putValue(-3);
cells.get("C1").putValue(8);
cells.get("D1").putValue(-2);
cells.get("E1").putValue(6);
// Шаг 3: Создаём CellArea, указывающую на целевую ячейку F1
const dest = new AsposeCells.CellArea();
dest.setStartColumn(5);   // столбец F (индекс с нуля)
dest.setEndColumn(5);
dest.setStartRow(0);      // строка 1 (индекс с нуля)
dest.setEndRow(0);
// Шаг 4: Добавляем линейный спарклайн из A1:E1 в F1
// SparklineGroups.Add возвращает индекс только что добавленной группы
const index = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, dest);
const group = worksheet.getSparklineGroups().get(index);
// Шаг 5: Создаём красный CellsColor и назначаем его цветом линии спарклайна
const red = workbook.createCellsColor();
red.setColor(AsposeCells.Color.fromArgb(255, 0, 0));
group.setSeriesColor(red);
// Шаг 6: Включаем маркеры максимальных и минимальных точек
group.setShowHighPoint(true);
group.setShowLowPoint(true);
// Шаг 7: Сохраняем книгу
workbook.save("output_line.xlsx");
```

## **Столбцовые спарклайны**
Столбцовый спарклайн отображает каждую точку данных в виде вертикальной полосы. Это делает его хорошо подходящим для данных, величина которых значима — например, ежемесячные показатели продаж или количества. В Aspose.Cells столбцовый спарклайн создаётся путём передачи `SparklineType.Column` методу `sparklineGroups.add`.
Процедура аналогична примеру с линейным спарклайном:
1. Создайте новую `Workbook` и откройте первый рабочий лист.
2. Создайте `CellArea`, описывающую целевую ячейку.
3. Вызовите `worksheet.sparklineGroups.add(SparklineType.Column, "A1:E1", false, dest)`.
4. При необходимости настройте полученный `SparklineGroup` — например, задав `group.type` для подтверждения типа или скорректировав цвет полосы.
5. Сохраните рабочую книгу в отдельный выходной файл, чтобы не перезаписать пример с линейным спарклайном.
Пример ниже записывает значения 5, -3, 8, -2, 6 в ячейки A1:E1 и отображает столбцовый спарклайн в F1. Отрицательные значения отображаются как полосы, идущие вниз, а положительные значения — как полосы, идущие вверх, что позволяет легко определить положительные и отрицательные вклады.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Шаг 2: Записать примеры значений в A1:E1
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
// Шаг 4: Добавить столбцовую спарклайн в целевую ячейку
let idx = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Column, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(idx);
// Шаг 5: Подтвердить тип спарклайн, прочитав group.Type
console.log("Sparkline Type added: " + group.getType());
// Шаг 6: Сохранить книгу
workbook.save("output_column.xlsx");
console.log("Workbook saved as output_column.xlsx");
```

## **Спарклайны победа/поражение**
Спарклайн победа/поражение — это особый вариант столбцового спарклайна, предназначенный для отображения только двух исходов: положительное значение отображается как «верхняя» полоса (победа), а нулевое или отрицательное значение — как «нижняя» полоса (поражение). Спарклайны победа/поражение обычно используются для визуализации последовательностей побед и поражений, результатов пройдено/не пройдено или любого бинарного исхода во времени.
В Aspose.Cells спарклайн победа/поражение создаётся путём передачи `SparklineType.Stacked` методу `sparklineGroups.add`. (Несмотря на название, `SparklineType.Stacked` — это значение перечисления, используемое для запроса рендеринга победа/поражение.)
1. Создайте новую `Workbook` и откройте первый рабочий лист.
2. Заполните диапазон исходных данных. Поскольку спарклайны победа/поражение рассматривают каждое значение либо как победу, либо как поражение, величина значения не имеет значения — важен только его знак. Положительные значения становятся верхними полосами, а неположительные — нижними.
3. Создайте `CellArea`, описывающую целевую ячейку.
4. Вызовите `worksheet.sparklineGroups.add(SparklineType.Stacked, "A1:E1", false, dest)`.
5. При необходимости настройте возвращённый `SparklineGroup`, например, задав акцентные цвета для полос победы и поражения.
6. Сохраните рабочую книгу под отдельным именем файла, чтобы все три примера могли сосуществовать на диске.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("WinLoss");
// Шаг 2: Заполнение примера данных в строке 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
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
// Включение маркеров верхней и нижней точек
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);
// Установка зелёного цвета для верхней точки
let highColor = workbook.createCellsColor();
highColor.setColor(AsposeCells.Color.Green);
group.setHighPointColor(highColor);
// Установка красного цвета для нижней точки
let lowColor = workbook.createCellsColor();
lowColor.setColor(AsposeCells.Color.Red);
group.setLowPointColor(lowColor);
// Установка оранжевого цвета для отрицательной точки
let negColor = workbook.createCellsColor();
negColor.setColor(AsposeCells.Color.Orange);
group.setNegativePointsColor(negColor);
// Установка цвета серии по умолчанию (используется для положительных столбцов)
let seriesColor = workbook.createCellsColor();
seriesColor.setColor(AsposeCells.Color.SteelBlue);
group.setSeriesColor(seriesColor);
// Шаг 6: Сохранение книги
workbook.save("output_winloss.xlsx");
console.log("Workbook saved successfully: output_winloss.xlsx");
```

## **Объединение всех трёх типов спарклайнов**
Приведённый ниже комбинированный пример создаёт одну рабочую книгу, заполняет строку 1 значениями 5, -3, 8, -2, 6, а затем добавляет три группы спарклайнов в ячейки F1, F2 и F3 — по одной каждого типа — чтобы полученный файл демонстрировал все три стиля спарклайнов одновременно.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Step 2: Populate sample data in row 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// Step 3: Add a Line sparkline group at F1
let lineArea = new AsposeCells.CellArea();
lineArea.setStartColumn(5);
lineArea.setEndColumn(5);
lineArea.setStartRow(0);
lineArea.setEndRow(0);
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, lineArea);
let lineGroup = worksheet.getSparklineGroups().get(lineIdx);
// Customize the line sparkline color via CellsColor
let lineColor = workbook.createCellsColor();
lineColor.setColor(AsposeCells.Color.Blue);
lineGroup.setSeriesColor(lineColor);
// Step 4: Add a Column sparkline group at F2
let columnArea = new AsposeCells.CellArea();
columnArea.setStartColumn(5);
columnArea.setEndColumn(5);
columnArea.setStartRow(1);
columnArea.setEndRow(1);
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "A1:E1", false, columnArea);
let columnGroup = worksheet.getSparklineGroups().get(columnIdx);
// Customize the column sparkline series color
let columnColor = workbook.createCellsColor();
columnColor.setColor(AsposeCells.Color.Green);
columnGroup.setSeriesColor(columnColor);
// Step 5: Add a Win/Loss (Stacked) sparkline group at F3
let stackedArea = new AsposeCells.CellArea();
stackedArea.setStartColumn(5);
stackedArea.setEndColumn(5);
stackedArea.setStartRow(2);
stackedArea.setEndRow(2);
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);
let stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);
// Customize the win/loss sparkline series color
let stackedColor = workbook.createCellsColor();
stackedColor.setColor(AsposeCells.Color.DarkOrange);
stackedGroup.setSeriesColor(stackedColor);
// Step 6: Save the workbook
workbook.save("output_all.xlsx");
```

## **Настройка внешнего вида спарклайнов**
После того как `SparklineGroup` создан и добавлен в `worksheet.sparklineGroups`, вы можете прочитать или изменить некоторые его визуальные свойства перед сохранением рабочей книги. Наиболее часто настраиваемые свойства:
- **`group.type`** — `SparklineType` (Line, Column или Stacked). Устанавливается при добавлении группы, но можно прочитать его обратно для подтверждения.
- **`group.line.color`** — цвет линии, выраженный как `CellsColor`, созданный через `workbook.createCellsColor()`. Это свойство используется для цвета обводки линейного спарклайна.
- **`group.line.weight`** — толщина линии в пунктах. Большие значения дают более толстые линии.
- **Маркеры верхних/нижних точек** — флаги, которые включают маленькие маркеры на самых высоких и самых низких точках данных, полезные для выделения экстремумов.
- **Маркеры первых/последних/отрицательных точек** — флаги, которые переключают маркеры на первой, последней и отрицательной точках данных.
Чтобы изменить цвет, всегда создавайте экземпляр `CellsColor` и присваивайте его соответствующему свойству. Не присваивайте `System.Drawing.Color` напрямую свойствам цвета спарклайна — они ожидают тип `CellsColor` из `Aspose.Cells.Drawing`. Сам метод `sparklineGroups.add` возвращает полностью типизированный объект `SparklineGroup`, поэтому вы можете связывать присваивания свойств с возвращаемым значением или сохранить его в локальной переменной и настроить перед сохранением.
{{% /alert %}}

{{< app/cells/assistant language="javascript" >}}
---
title: Спарклайны в Aspose.Cells for Node.js via Java
linktitle: Спарклайны в Aspose.Cells for Node.js via Java
description: Aspose.Cells — это библиотека Node.js via Java для работы с файлами электронных таблиц, которая поддерживает создание спарклайнов — миниатюрных диаграмм, размещаемых внутри ячеек рабочего листа. В этой статье объясняется, как добавлять и настраивать линейные, столбцовые спарклайны и спарклайны победа/поражение с помощью библиотеки Aspose.Cells.
keywords: Aspose.Cells, библиотека Node.js via Java, электронная таблица, спарклайны, линейный спарклайн, столбцовый спарклайн, спарклайн победа/поражение, SparklineGroup, SparklineType
type: docs
weight: 195
url: /ru/nodejs-java/creating-sparklines/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells поддерживает создание спарклайнов внутри ячеек рабочего листа. Спарклайны — это миниатюрные диаграммы, которые помещаются в одной ячейке и обеспечивают быстрое визуальное представление трендов данных. Aspose.Cells поддерживает линейные, столбцовые спарклайны и спарклайны победа/поражение, каждый из которых можно настроить по цвету, толщине линии, верхним/нижним точкам и маркерам.
{{% /alert %}}

## **Введение**
Спарклайны — это крошечные диаграммы внутри ячеек, которые полезны, когда требуется отобразить быстрый тренд рядом со строкой или столбцом данных, не занимая места полноценной диаграммы. Excel поддерживает три вида спарклайнов: **линейные**, **столбцовые** и **победа/поражение**. Aspose.Cells реализует эту возможность через API `SparklineGroup` и `SparklineGroupCollection`, расположенные в пространстве имён `com.aspose.cells.Charts`.
В Aspose.Cells каждый добавляемый спарклайн создаётся с помощью `worksheet.SparklineGroups.add(...)`, который возвращает объект `SparklineGroup`. Затем этот объект можно использовать для задания типа спарклайна, диапазона данных, ячейки назначения и визуальных свойств, таких как цвет линии, толщина линии, маркеры и индикаторы верхних/нижних точек.
В этой статье рассматриваются все три типа спарклайнов, поддерживаемых Aspose.Cells — **линейные**, **столбцовые** и **победа/поражение** — и показано, как их добавлять, настраивать цвета и сохранять полученную рабочую книгу.

## **Линейные спарклайны**
Линейный спарклайн рисует непрерывную линию через точки данных в серии, что делает его наиболее естественным выбором для отображения трендов во времени. В Aspose.Cells линейный спарклайн создаётся путём передачи `SparklineType.Line` в метод `SparklineGroups.add`.
1. Создайте новый объект `Workbook` и получите доступ к первому рабочему листу.
2. Заполните строку исходными данными (например, строка 1, столбцы от A до E) значениями, которые требуется визуализировать.
3. Создайте объект `CellArea`, описывающий ячейку назначения, в которой будет нарисован спарклайн.
4. Вызовите `worksheet.SparklineGroups.add(SparklineType.Line, "A1:E1", false, dest)`. Третий аргумент — `false` — сообщает Aspose.Cells, что диапазон данных является горизонтальным (строка), а не вертикальным (столбец).
5. При необходимости настройте возвращённый объект `SparklineGroup`. Для линейного спарклайна можно задать цвет линии с помощью `group.Line.Color` (который ожидает объект `CellsColor` из `com.aspose.cells.Drawing`), настроить толщину линии и включить маркеры верхних/нижних точек.
6. Сохраните рабочую книгу.
В следующем примере создаётся рабочая книга, значения 5, -3, 8, -2, 6 записываются в ячейки от A1 до E1, и в ячейку F1 добавляется линейный спарклайн, отображающий эти значения. Также настраивается красный цвет линии и включаются маркеры для верхней и нижней точек.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
let cells = worksheet.getCells();
// Шаг 2: Записать примеры значений 5, -3, 8, -2, 6 в ячейки A1:E1
cells.get("A1").putValue(5);
cells.get("B1").putValue(-3);
cells.get("C1").putValue(8);
cells.get("D1").putValue(-2);
cells.get("E1").putValue(6);
// Шаг 3: Создать CellArea, указывающую на целевую ячейку F1
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);   // столбец F (индексация с 0)
dest.setEndColumn(5);
dest.setStartRow(0);      // строка 1 (индексация с 0)
dest.setEndRow(0);
// Шаг 4: Добавить линейную спарклайн из A1:E1 в F1
// SparklineGroups.Add возвращает индекс вновь добавленной группы
let index = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(index);
// Шаг 5: Создать красный CellsColor и назначить его цвету линии спарклайна
let red = workbook.createCellsColor();
red.setColor(AsposeCells.Color.fromArgb(255, 0, 0));
group.setSeriesColor(red);
// Шаг 6: Включить маркеры максимальной и минимальной точек
group.setShowHighPoint(true);
group.setShowLowPoint(true);
// Шаг 7: Сохранить книгу
workbook.save("output_line.xlsx");
```

## **Столбцовые спарклайны**
Столбцовый спарклайн отображает каждую точку данных в виде вертикальной полосы. Это хорошо подходит для данных, величина которых имеет значение — например, ежемесячных объёмов продаж или количественных показателей. В Aspose.Cells столбцовый спарклайн создаётся путём передачи `SparklineType.Column` в метод `SparklineGroups.add`.
Процедура аналогична примеру с линейным спарклайном:
1. Создайте новый объект `Workbook` и получите доступ к первому рабочему листу.
2. Заполните строку исходными данными (например, строка 1, столбцы от A до E) значениями, которые требуется визуализировать.
3. Создайте объект `CellArea`, описывающий ячейку назначения.
4. Вызовите `worksheet.SparklineGroups.add(SparklineType.Column, "A1:E1", false, dest)`.
5. При необходимости настройте полученный объект `SparklineGroup` — например, задав `group.Type` для подтверждения типа или изменив цвет полос.
6. Сохраните рабочую книгу в отдельный выходной файл, чтобы не перезаписать пример с линейным спарклайном.
В примере ниже значения 5, -3, 8, -2, 6 записываются в A1:E1, и в ячейке F1 отображается столбцовый спарклайн. Отрицательные значения отображаются как полосы, направленные вниз, а положительные — как полосы, направленные вверх, что позволяет легко увидеть положительный и отрицательный вклад.

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
Спарклайн победа/поражение — это особый вариант столбцового спарклайна, предназначенный для отображения только двух исходов: положительное значение отображается как полоса вверх (победа), а нулевое или отрицательное значение — как полоса вниз (поражение). Спарклайны победа/поражение обычно используются для визуализации последовательностей побед и поражений, результатов «прошёл/не прошёл» или любого бинарного исхода во времени.
В Aspose.Cells спарклайн победа/поражение создаётся путём передачи `SparklineType.Stacked` в метод `SparklineGroups.add`. (Несмотря на название, `SparklineType.Stacked` — это значение перечисления, используемое для запроса отображения победа/поражение.)
1. Создайте новый объект `Workbook` и получите доступ к первому рабочему листу.
2. Заполните диапазон исходных данных. Поскольку спарклайны победа/поражение трактуют каждое значение как победу или поражение, величина значения не имеет значения — важен только его знак. Положительные значения становятся полосами вверх, а неположительные — полосами вниз.
3. Создайте объект `CellArea`, описывающий ячейку назначения.
4. Вызовите `worksheet.SparklineGroups.add(SparklineType.Stacked, "A1:E1", false, dest)`.
5. При необходимости настройте возвращённый объект `SparklineGroup`, например задав акцентные цвета для полос победы и поражения.
6. Сохраните рабочую книгу под отдельным именем файла, чтобы все три примера могли сосуществовать на диске.

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
    dest
);
let group = worksheet.getSparklineGroups().get(groupIndex);
// Шаг 5: Настройка группы спарклайнов
// Включение маркеров верхних и нижних точек
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);
// Установка зеленого цвета для верхних точек
let highColor = workbook.createCellsColor();
highColor.setColor(AsposeCells.Color.getGreen());
group.setHighPointColor(highColor);
// Установка красного цвета для нижних точек
let lowColor = workbook.createCellsColor();
lowColor.setColor(AsposeCells.Color.getRed());
group.setLowPointColor(lowColor);
// Установка оранжевого цвета для отрицательных точек
let negColor = workbook.createCellsColor();
negColor.setColor(AsposeCells.Color.getOrange());
group.setNegativePointsColor(negColor);
// Установка цвета серии по умолчанию (используется для положительных столбцов)
let seriesColor = workbook.createCellsColor();
seriesColor.setColor(AsposeCells.Color.getSteelBlue());
group.setSeriesColor(seriesColor);
// Шаг 6: Сохранение книги
workbook.save("output_winloss.xlsx");
console.log("Workbook saved successfully: output_winloss.xlsx");
```

## **Объединение всех трёх типов спарклайнов**
В следующем комбинированном примере создаётся одна рабочая книга, в строке 1 записываются значения 5, -3, 8, -2, 6, после чего добавляются три группы спарклайнов в ячейки F1, F2 и F3 — по одной каждого типа — чтобы полученный файл демонстрировал все три стиля спарклайнов одновременно.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Шаг 2: Заполнение образца данных в строке 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// Шаг 3: Добавление группы спарклайнов «Линия» в F1
let lineArea = new AsposeCells.CellArea();
lineArea.setStartColumn(5);
lineArea.setEndColumn(5);
lineArea.setStartRow(0);
lineArea.setEndRow(0);
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, lineArea);
let lineGroup = worksheet.getSparklineGroups().get(lineIdx);
// Настройка цвета спарклайна «Линия» через CellsColor
let lineColor = workbook.createCellsColor();
lineColor.setColor(AsposeCells.Color.getBlue());
lineGroup.setSeriesColor(lineColor);
// Шаг 4: Добавление группы спарклайнов «Столбец» в F2
let columnArea = new AsposeCells.CellArea();
columnArea.setStartColumn(5);
columnArea.setEndColumn(5);
columnArea.setStartRow(1);
columnArea.setEndRow(1);
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "A1:E1", false, columnArea);
let columnGroup = worksheet.getSparklineGroups().get(columnIdx);
// Настройка цвета серии спарклайна «Столбец»
let columnColor = workbook.createCellsColor();
columnColor.setColor(AsposeCells.Color.getGreen());
columnGroup.setSeriesColor(columnColor);
// Шаг 5: Добавление группы спарклайнов «Выигрыш/Проигрыш» (Стопочная) в F3
let stackedArea = new AsposeCells.CellArea();
stackedArea.setStartColumn(5);
stackedArea.setEndColumn(5);
stackedArea.setStartRow(2);
stackedArea.setEndRow(2);
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);
let stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);
// Настройка цвета серии спарклайна «Выигрыш/Проигрыш»
let stackedColor = workbook.createCellsColor();
stackedColor.setColor(AsposeCells.Color.getDarkOrange());
stackedGroup.setSeriesColor(stackedColor);
// Шаг 6: Сохранение книги
workbook.save("output_all.xlsx");
```

## **Настройка внешнего вида спарклайна**
После создания объекта `SparklineGroup` и его добавления в `worksheet.SparklineGroups` можно прочитать или изменить несколько его визуальных свойств перед сохранением рабочей книги. Наиболее часто настраиваемыми свойствами являются:
- **`group.Type`** — тип `SparklineType` (Line, Column или Stacked). Он задаётся при добавлении группы, но можно прочитать его обратно для подтверждения.
- **`group.Line.Color`** — цвет линии, представленный объектом `CellsColor`, созданным с помощью `workbook.createCellsColor()`. Это свойство используется для задания цвета обводки линейного спарклайна.
- **`group.Line.Weight`** — толщина линии в пунктах. Бо́льшие значения дают более толстые линии.
- **Маркеры верхних/нижних точек** — флаги, включающие небольшие маркеры на самой высокой и самой низкой точках данных, полезные для выделения экстремумов.
- **Маркеры первой/последней/отрицательной точек** — флаги, переключающие маркеры на первой, последней и отрицательной точках данных.
Чтобы изменить цвет, всегда создавайте экземпляр `CellsColor` и присваивайте его соответствующему свойству. Не присваивайте `java.awt.Color` напрямую свойствам цвета спарклайна — они ожидают тип `CellsColor` из `com.aspose.cells.Drawing`. Сам метод `SparklineGroups.add` возвращает полностью типизированный объект `SparklineGroup`, поэтому можно либо объединять присваивания свойств в цепочку на возвращаемом значении, либо сохранить его в локальную переменную и настроить перед сохранением.

{{< app/cells/assistant language="javascript" >}}
---
title: Спарклайны в Aspose.Cells для Aspose.Cells для Node.js через Java
linktitle: Спарклайны
description: Aspose.Cells — это библиотека Node.js через Java для работы с файлами электронных таблиц, которая поддерживает создание спарклайнов — миниатюрных диаграмм, размещаемых внутри ячеек рабочего листа. В этой статье объясняется, как добавлять и настраивать спарклайны типов «линия», «столбец» и «выигрыш/проигрыш» с использованием библиотеки Aspose.Cells.
keywords: Aspose.Cells, библиотека Node.js через Java, электронная таблица, спарклайны, линейный спарклайн, столбцовый спарклайн, спарклайн выигрыш/проигрыш, SparklineGroup, SparklineType
type: docs
weight: 195
url: /ru/nodejs-java/creating-sparklines/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells поддерживает создание спарклайнов внутри ячеек рабочего листа. Спарклайны — это миниатюрные диаграммы, которые помещаются в одну ячейку и обеспечивают быструю визуальную интерпретацию тенденций данных. Aspose.Cells поддерживает линейные, столбцовые спарклайны и спарклайны «выигрыш/проигрыш», каждый из которых можно настроить по цвету, толщине линии, точкам максимума/минимума и маркерам.

{{% /alert %}}

## **Введение**

Спарклайны — это крошечные внутриклеточные диаграммы, которые полезны, когда нужно отобразить быструю тенденцию рядом со строкой или столбцом данных, не занимая места полноценной диаграммы. Excel поддерживает три типа спарклайнов: **линейные**, **столбцовые** и **выигрыш/проигрыш**. Aspose.Cells дублирует эту возможность через API `SparklineGroup` и `SparklineGroupCollection`, расположенные в пространстве имён `com.aspose.cells.Charts`.

В Aspose.Cells каждый добавляемый спарклайн создаётся через `worksheet.SparklineGroups.add(...)`, который возвращает объект `SparklineGroup`. Затем вы можете использовать этот объект для установки типа спарклайна, диапазона данных, целевой ячейки и визуальных свойств, таких как цвет линии, толщина линии, маркеры и индикаторы точек максимума/минимума.

{{% alert color="primary" %}}

Один объект `SparklineGroup` может содержать один или несколько спарклайнов, использующих одинаковый стиль. Когда вы вызываете `add` и передаёте строку данных плюс одну целевую ячейку, вы получаете один спарклайн внутри этой ячейки. Если ваш диапазон назначения шире одной ячейки, в каждой целевой ячейке рисуется отдельный спарклайн, все с одинаковым стилем и диапазоном данных.

{{% /alert %}}

В этой статье рассматривается каждый из трёх типов спарклайнов, поддерживаемых Aspose.Cells — **Линейный**, **Столбцовый** и **Выигрыш/Проигрыш** — и показано, как их добавлять, настраивать их цвета и сохранять полученную рабочую книгу.

## **Линейные спарклайны**

Линейный спарклайн проводит непрерывную линию через точки данных в серии, что делает его наиболее естественным выбором для отображения тенденций во времени. В Aspose.Cells линейный спарклайн создаётся путём передачи `SparklineType.Line` методу `SparklineGroups.add`.

Рабочий процесс аналогичен любому другому типу спарклайна:

1. Создайте новую `Workbook` и откройте первый рабочий лист.
2. Заполните строку исходных данных (например, строка 1, столбцы от A до E) значениями, которые вы хотите визуализировать.
3. Создайте `CellArea`, описывающую целевую ячейку, в которой будет нарисован спарклайн.
4. Вызовите `worksheet.SparklineGroups.add(SparklineType.Line, "A1:E1", false, dest)`. Третий аргумент — `false` — сообщает Aspose.Cells, что диапазон данных горизонтальный (строка), а не вертикальный (столбец).
5. При необходимости настройте возвращённый `SparklineGroup`. Для линейного спарклайна вы можете задать цвет линии с помощью `group.Line.Color` (который ожидает `CellsColor` из `com.aspose.cells.Drawing`), отрегулировать толщину линии и включить маркеры точек максимума/минимума.
6. Сохраните рабочую книгу.

Следующий пример создаёт рабочую книгу, записывает значения 5, -3, 8, -2, 6 в ячейки с A1 по E1 и добавляет линейный спарклайн в ячейку F1, который отслеживает эти значения. Также настраивается цвет линии на красный и включаются маркеры для точек максимума и минимума.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
let cells = worksheet.getCells();

// Шаг 2: Записать образцы значений 5, -3, 8, -2, 6 в ячейки A1:E1
cells.get("A1").putValue(5);
cells.get("B1").putValue(-3);
cells.get("C1").putValue(8);
cells.get("D1").putValue(-2);
cells.get("E1").putValue(6);

// Шаг 3: Создать CellArea, указывающую на целевую ячейку F1
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);   // столбец F (индекс с 0)
dest.setEndColumn(5);
dest.setStartRow(0);      // строка 1 (индекс с 0)
dest.setEndRow(0);

// Шаг 4: Добавить спарклайн-линию из A1:E1 в F1
// SparklineGroups.Add возвращает индекс вновь добавленной группы
let index = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(index);

// Шаг 5: Создать красный CellsColor и назначить его цветом линии спарклайна
let red = workbook.createCellsColor();
red.setColor(AsposeCells.Color.fromArgb(255, 0, 0));
group.setSeriesColor(red);

// Шаг 6: Включить маркеры высоких и низких точек
group.setShowHighPoint(true);
group.setShowLowPoint(true);

// Шаг 7: Сохранить книгу
workbook.save("output_line.xlsx");
```

## **Столбцовые спарклайны**

Столбцовый спарклайн отображает каждую точку данных в виде вертикальной полосы. Это делает его хорошо подходящим для данных, величина которых имеет значение — например, ежемесячные показатели продаж или подсчёты. В Aspose.Cells столбцовый спарклайн создаётся путём передачи `SparklineType.Column` методу `SparklineGroups.add`.

Процедура аналогична примеру с линейным спарклайном:

1. Создайте новую `Workbook` и откройте первый рабочий лист.
2. Заполните тот же исходный диапазон (A1:E1) значениями, которые вы хотите визуализировать.
3. Создайте `CellArea`, описывающую целевую ячейку.
4. Вызовите `worksheet.SparklineGroups.add(SparklineType.Column, "A1:E1", false, dest)`.
5. При необходимости настройте полученный `SparklineGroup` — например, задав `group.Type` для подтверждения типа или изменив цвет полос.
6. Сохраните рабочую книгу в отдельный выходной файл, чтобы он не перезаписывал пример с линейным спарклайном.

В примере ниже значения 5, -3, 8, -2, 6 записываются в A1:E1, и в F1 рисуется столбцовый спарклайн. Отрицательные значения отображаются как полосы, направленные вниз, а положительные — как полосы, направленные вверх, что позволяет легко увидеть положительные и отрицательные вклады с первого взгляда.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Шаг 2: Записать образец значений в A1:E1
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

// Шаг 4: Добавить спарклайн типа Column в целевую ячейку
let idx = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Column, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(idx);

// Шаг 5: Подтвердить тип спарклайна, прочитав group.Type
console.log("Sparkline Type added: " + group.getType());

// Шаг 6: Сохранить книгу
workbook.save("output_column.xlsx");

console.log("Workbook saved as output_column.xlsx");
```

## **Спарклайны «Выигрыш/Проигрыш»**

Спарклайн «выигрыш/проигрыш» — это особый вариант столбцового спарклайна, предназначенный для отображения только двух исходов: положительное значение отображается как «верхняя» полоса (выигрыш), а нулевое или отрицательное значение — как «нижняя» полоса (проигрыш). Спарклайны «выигрыш/проигрыш» обычно используются для визуализации последовательностей побед и поражений, результатов «прошёл/не прошёл» или любого бинарного исхода во времени.

В Aspose.Cells спарклайн «выигрыш/проигрыш» создаётся путём передачи `SparklineType.Stacked` методу `SparklineGroups.add`. (Несмотря на название, `SparklineType.Stacked` — это значение перечисления, используемое для запроса рендеринга «выигрыш/проигрыш».)

Процедура аналогична двум другим типам:

1. Создайте новую `Workbook` и откройте первый рабочий лист.
2. Заполните исходный диапазон. Поскольку спарклайны «выигрыш/проигрыш» обрабатывают каждое значение либо как выигрыш, либо как проигрыш, величина значения не имеет значения — важен только его знак. Положительные значения становятся верхними полосами, а неположительные — нижними.
3. Создайте `CellArea`, описывающую целевую ячейку.
4. Вызовите `worksheet.SparklineGroups.add(SparklineType.Stacked, "A1:E1", false, dest)`.
5. При необходимости настройте возвращённый `SparklineGroup`, например, задав акцентные цвета для полос выигрыша и проигрыша.
6. Сохраните рабочую книгу под уникальным именем файла, чтобы все три примера могли сосуществовать на диске.

В примере ниже используются те же входные данные, что и в предыдущих двух разделах. Значения 5, -3, 8, -2, 6 интерпретируются как выигрыш, проигрыш, выигрыш, проигрыш, выигрыш — и спарклайн, нарисованный в F1, точно отражает этот шаблон.

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

// Шаг 4: Добавление спарклайн-диаграммы Win/Loss (SparklineType.Stacked)
let groupIndex = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Stacked,
    "A1:E1",
    false,
    dest
);
let group = worksheet.getSparklineGroups().get(groupIndex);

// Шаг 5: Настройка группы спарклайнов
// Включение маркеров высоких и низких точек
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);

// Установка зелёного цвета для высоких точек
let highColor = workbook.createCellsColor();
highColor.setColor(AsposeCells.Color.getGreen());
group.setHighPointColor(highColor);

// Установка красного цвета для низких точек
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

Каждый из предыдущих трёх примеров создаёт свою рабочую книгу, чтобы выходные файлы было легко изучать по отдельности. Однако в реальном сценарии часто требуется сравнить несколько серий данных бок о бок. Самый чистый способ сделать это — поместить более одной группы спарклайнов в один рабочий лист, где каждая группа отображает свой стиль.

Вы можете добавить несколько объектов `SparklineGroup` в одну `SparklineGroupCollection`, и каждая группа может быть нацелена на разную целевую ячейку или разный диапазон. Например, вы можете разместить линейный спарклайн в F1, столбцовый спарклайн в F2 и спарклайн «выигрыш/проигрыш» в F3 — все считывающие данные из одного и того же источника в строке 1 — чтобы читатель мог видеть три различных визуальных представления одних и тех же чисел.

Комбинированный пример ниже создаёт одну рабочую книгу, заполняет строку 1 значениями 5, -3, 8, -2, 6, а затем добавляет три группы спарклайнов в ячейки F1, F2 и F3 — по одной каждого типа — так что полученный файл демонстрирует все три стиля спарклайнов одновременно.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Шаг 2: Заполнение примера данных в строке 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// Шаг 3: Добавление группы линейных спарклайнов в ячейку F1
let lineArea = new AsposeCells.CellArea();
lineArea.setStartColumn(5);
lineArea.setEndColumn(5);
lineArea.setStartRow(0);
lineArea.setEndRow(0);
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, lineArea);
let lineGroup = worksheet.getSparklineGroups().get(lineIdx);

// Настройка цвета линейного спарклайна с помощью CellsColor
let lineColor = workbook.createCellsColor();
lineColor.setColor(AsposeCells.Color.getBlue());
lineGroup.setSeriesColor(lineColor);

// Шаг 4: Добавление группы столбчатых спарклайнов в ячейку F2
let columnArea = new AsposeCells.CellArea();
columnArea.setStartColumn(5);
columnArea.setEndColumn(5);
columnArea.setStartRow(1);
columnArea.setEndRow(1);
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "A1:E1", false, columnArea);
let columnGroup = worksheet.getSparklineGroups().get(columnIdx);

// Настройка цвета серии столбчатого спарклайна
let columnColor = workbook.createCellsColor();
columnColor.setColor(AsposeCells.Color.getGreen());
columnGroup.setSeriesColor(columnColor);

// Шаг 5: Добавление группы спарклайнов "Победа/Проигрыш" (С накоплением) в ячейку F3
let stackedArea = new AsposeCells.CellArea();
stackedArea.setStartColumn(5);
stackedArea.setEndColumn(5);
stackedArea.setStartRow(2);
stackedArea.setEndRow(2);
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);
let stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);

// Настройка цвета серии спарклайна "Победа/Проигрыш"
let stackedColor = workbook.createCellsColor();
stackedColor.setColor(AsposeCells.Color.getDarkOrange());
stackedGroup.setSeriesColor(stackedColor);

// Шаг 6: Сохранение книги
workbook.save("output_all.xlsx");
```

{{% alert color="primary" %}}

Когда вы объединяете несколько групп спарклайнов в одном рабочем листе, каждая группа независима. Они могут использовать один и тот же исходный диапазон или разные исходные диапазоны, и их можно стилизовать независимо. Это упрощает создание небольшой «панели мониторинга» внутриклеточных визуализаций непосредственно внутри существующего рабочего листа.

{{% /alert %}}

## **Настройка внешнего вида спарклайна**

После создания `SparklineGroup` и добавления его в `worksheet.SparklineGroups` вы можете прочитать или изменить несколько его визуальных свойств перед сохранением рабочей книги. Наиболее часто настраиваемые свойства:

- **`group.Type`** — `SparklineType` (Line, Column или Stacked). Он устанавливается при добавлении группы, но вы можете прочитать его обратно для подтверждения.
- **`group.Line.Color`** — цвет линии, выраженный как `CellsColor`, созданный через `workbook.createCellsColor()`. Это свойство используется для цвета обводки линейного спарклайна.
- **`group.Line.Weight`** — толщина линии в пунктах. Более высокие значения дают более толстые линии.
- **Маркеры точек максимума/минимума** — флаги, включающие небольшие маркеры на самых высоких и самых низких точках данных, полезные для выделения экстремумов.
- **Маркеры первой/последней/отрицательной точки** — флаги, переключающие маркеры на первой, последней и отрицательной точках данных.

Чтобы изменить цвет, всегда создавайте экземпляр `CellsColor` и присваивайте его соответствующему свойству. Не присваивайте `java.awt.Color` напрямую свойствам цвета спарклайна — они ожидают тип `CellsColor` из `com.aspose.cells.Drawing`. Сам метод `SparklineGroups.add` возвращает полностью типизированный объект `SparklineGroup`, поэтому вы можете связывать присваивания свойств на возвращаемом значении или сохранить его в локальной переменной и настроить перед сохранением.



{{< app/cells/assistant language="javascript" >}}
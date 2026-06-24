---
title: Спарклайны в Aspose.Cells for Java
linktitle: Sparklines
description: Aspose.Cells — это Java-библиотека для работы с файлами электронных таблиц, которая поддерживает создание спарклайнов — миниатюрных диаграмм, размещаемых внутри ячеек рабочего листа. В этой статье объясняется, как добавлять и настраивать линейные, столбцовые спарклайны и спарклайны «выигрыш/проигрыш» с помощью библиотеки Aspose.Cells.
keywords: Aspose.Cells, Java library, spreadsheet, sparklines, line sparkline, column sparkline, win/loss sparkline, SparklineGroup, SparklineType
type: docs
weight: 195
url: /ru/java/creating-sparklines/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells поддерживает создание спарклайнов внутри ячеек рабочего листа. Спарклайны — это миниатюрные диаграммы, которые помещаются в одну ячейку и обеспечивают быстрое визуальное представление тенденций данных. Aspose.Cells поддерживает линейные, столбцовые спарклайны и спарклайны «выигрыш/проигрыш», каждый из которых можно настроить по цвету, толщине линии, верхним/нижним точкам и маркерам.

{{% /alert %}}

## **Введение**

Спарклайны — это маленькие внутриклеточные диаграммы, которые полезны, когда требуется отобразить быструю тенденцию рядом со строкой или столбцом данных, не занимая места полноценной диаграммы. Excel поддерживает три вида спарклайнов: **линейные**, **столбцовые** и **«выигрыш/проигрыш»**. Aspose.Cells дублирует эту возможность через API `SparklineGroup` и `SparklineGroupCollection`, расположенные в пространстве имён `Aspose.Cells.Charts`.

В Aspose.Cells каждый добавляемый спарклайн создаётся с помощью `worksheet.getSparklineGroups().add(...)`, который возвращает объект `SparklineGroup`. Затем можно использовать этот объект, чтобы задать тип спарклайна, диапазон данных, ячейку назначения и визуальные свойства, такие как цвет линии, толщина линии, маркеры и индикаторы верхних/нижних точек.

{{% alert color="primary" %}}

Один `SparklineGroup` может содержать один или несколько спарклайнов, которые используют общий стиль. Когда вы вызываете `add` и передаёте строку данных и одну ячейку назначения, вы получаете один спарклайн внутри этой ячейки. Если ваш диапазон назначения шире одной ячейки, в каждой ячейке назначения рисуется отдельный спарклайн, при этом все они используют один и тот же стиль и диапазон данных.

{{% /alert %}}

В этой статье рассматривается каждый из трёх типов спарклайнов, поддерживаемых Aspose.Cells — **линейные**, **столбцовые** и **«выигрыш/проигрыш»** — и показано, как их добавлять, настраивать их цвета и сохранять полученную рабочую книгу.

## **Линейные спарклайны**

Линейный спарклайн рисует непрерывную линию через точки данных в серии, что делает его наиболее естественным выбором для отображения тенденций во времени. В Aspose.Cells линейный спарклайн создаётся путём передачи `SparklineType.LINE` методу `add`.

Рабочий процесс такой же, как и для любого другого типа спарклайна:

1. Создайте новую `Workbook` и получите доступ к первому рабочему листу.
2. Заполните строку исходных данных (например, строка 1, столбцы от A до E) значениями, которые требуется визуализировать.
3. Создайте `CellArea`, описывающую ячейку назначения, в которой будет нарисован спарклайн.
4. Вызовите `worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest)`. Третий аргумент — `false` — сообщает Aspose.Cells, что диапазон данных является горизонтальным (строка), а не вертикальным (столбец).
5. При необходимости настройте возвращённый `SparklineGroup`. Для линейного спарклайна можно задать цвет линии с помощью `group.getLine().setColor(...)` (который ожидает `CellsColor` из `Aspose.Cells.Drawing`), настроить толщину линии и переключить маркеры верхних/нижних точек.
6. Сохраните рабочую книгу.

В следующем примере создаётся рабочая книга, значения 5, -3, 8, -2, 6 записываются в ячейки A1–E1, и в ячейку F1 добавляется линейный спарклайн, отслеживающий эти значения. Также настраивается красный цвет линии и включаются маркеры для верхних и нижних точек.

```java
public class CodeRunner {
    public static void main(String[] args) {
        try {
            // Шаг 1: Создайте Workbook и получите первый рабочий лист
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.getWorksheets().get(0);
            Cells cells = worksheet.getCells();

            // Шаг 2: Запишите примеры значений 5, -3, 8, -2, 6 в ячейки A1:E1
            cells.get("A1").putValue(5);
            cells.get("B1").putValue(-3);
            cells.get("C1").putValue(8);
            cells.get("D1").putValue(-2);
            cells.get("E1").putValue(6);

            // Шаг 3: Создайте CellArea, указывающий на ячейку назначения F1
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // столбец F (с нулевой индексацией)
            dest.EndColumn = 5;
            dest.StartRow = 0;      // строка 1 (с нулевой индексацией)
            dest.EndRow = 0;

            // Шаг 4: Добавьте спарклайн Line из A1:E1 в F1
            // SparklineGroups.add возвращает индекс вновь добавленной группы
            int index = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest);
            SparklineGroup group = worksheet.getSparklineGroups().get(index);

            // Шаг 5: Создайте красный CellsColor и назначьте его цвету линии спарклайна
            CellsColor red = workbook.createCellsColor();
            red.setColor(com.aspose.cells.Color.getRed());
            group.setSeriesColor(red);

            // Шаг 6: Включите маркеры высоких и низких точек
            group.setShowHighPoint(true);
            group.setShowLowPoint(true);

            // Шаг 7: Сохраните книгу
            workbook.save("output_line.xlsx");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

## **Столбцовые спарклайны**

Столбцовый спарклайн отображает каждую точку данных в виде вертикальной полосы. Это делает его хорошо подходящим для данных, величина которых имеет значение — например, ежемесячных показателей продаж или подсчётов. В Aspose.Cells столбцовый спарклайн создаётся путём передачи `SparklineType.COLUMN` методу `add`.

Процедура аналогична примеру с линейным спарклайном:

1. Создайте новую `Workbook` и получите доступ к первому рабочему листу.
2. Заполните тот же диапазон источника (A1:E1) значениями, которые требуется визуализировать.
3. Создайте `CellArea`, описывающую ячейку назначения.
4. Вызовите `worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest)`.
5. При необходимости настройте полученный `SparklineGroup` — например, установив `group.getType()` для подтверждения типа, или изменив цвет полос.
6. Сохраните рабочую книгу в отдельный выходной файл, чтобы не перезаписать пример с линейным спарклайном.

В примере ниже значения 5, -3, 8, -2, 6 записываются в A1:E1, а в F1 отображается столбцовый спарклайн. Отрицательные значения рисуются в виде полос, направленных вниз, а положительные — в виде полос, направленных вверх, что позволяет легко определить положительный и отрицательный вклад с первого взгляда.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// Записать образец значений в A1:E1
int[] values = new int[] { 5, -3, 8, -2, 6 };
for (int i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}

// Создать CellArea, указывающую на F1 (индекс столбца 5, индекс строки 0)
CellArea dest = new CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);

// Добавить столбцовую спарклайн-диаграмму в ячейку назначения
int idx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest);
SparklineGroup group = worksheet.getSparklineGroups().get(idx);

// Подтвердить тип спарклайн-диаграммы, прочитав group.Type
System.out.println("Sparkline Type added: " + group.getType());

// Сохранить книгу
workbook.save("output_column.xlsx");

System.out.println("Workbook saved as output_column.xlsx");
```

## **Спарклайны «Выигрыш/Проигрыш»**

Спарклайн «выигрыш/проигрыш» — это особый вариант столбцового спарклайна, предназначенный для отображения только двух исходов: положительное значение рисуется в виде полосы «вверх» (выигрыш), а нулевое или отрицательное значение — в виде полосы «вниз» (проигрыш). Спарклайны «выигрыш/проигрыш» обычно используются для визуализации последовательностей побед и поражений, результатов «успех/неудача» или любого бинарного исхода во времени.

В Aspose.Cells спарклайн «выигрыш/проигрыш» создаётся путём передачи `SparklineType.STACKED` методу `add`. (Несмотря на название, `SparklineType.STACKED` — это значение перечисления, используемое для запроса отрисовки «выигрыш/проигрыш».)

Процедура такая же, как и для двух других типов:

1. Создайте новую `Workbook` и получите доступ к первому рабочему листу.
2. Заполните диапазон источника. Поскольку спарклайны «выигрыш/проигрыш» рассматривают каждое значение как выигрыш или проигрыш, величина значения не имеет значения — важен только его знак. Положительные значения становятся полосами вверх, а неположительные — полосами вниз.
3. Создайте `CellArea`, описывающую ячейку назначения.
4. Вызовите `worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest)`.
5. При необходимости настройте возвращённый `SparklineGroup`, например, задав акцентные цвета для полос выигрыша и проигрыша.
6. Сохраните рабочую книгу под отдельным именем файла, чтобы все три примера могли сосуществовать на диске.

В примере ниже используются те же входные данные, что и в двух предыдущих разделах. Значения 5, -3, 8, -2, 6 интерпретируются как выигрыш, проигрыш, выигрыш, проигрыш, выигрыш — и спарклайн, нарисованный в F1, отражает именно этот шаблон.

```java
import com.aspose.cells.*;
import com.aspose.cells.charts.*;
import com.aspose.cells.drawing.*;
import java.awt.Color;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("WinLoss");

// Заполнение примерами данных
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// Создание CellArea, указывающей на F1 (столбец 5, строка 0)
CellArea dest = new CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);

// Добавление спарклайна "Выигрыш/Проигрыш" (SparklineType.Stacked)
int groupIndex = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest);
SparklineGroup group = worksheet.getSparklineGroups().get(groupIndex);

// Настройка группы спарклайнов
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);

// Установка зелёного цвета для высоких точек
CellsColor highColor = workbook.createCellsColor();
highColor.setColor(Color.GREEN);
group.setHighPointColor(highColor);

// Установка красного цвета для низких точек
CellsColor lowColor = workbook.createCellsColor();
lowColor.setColor(Color.RED);
group.setLowPointColor(lowColor);

// Установка оранжевого цвета для отрицательных точек
CellsColor negColor = workbook.createCellsColor();
negColor.setColor(Color.ORANGE);
group.setNegativePointsColor(negColor);

// Установка цвета серии по умолчанию (используется для положительных столбцов)
CellsColor seriesColor = workbook.createCellsColor();
seriesColor.setColor(new Color(70, 130, 180)); // Приближение к SteelBlue
group.setSeriesColor(seriesColor);

// Сохранение книги
workbook.save("output_winloss.xlsx");

System.out.println("Workbook saved successfully: output_winloss.xlsx");
```

## **Объединение всех трёх типов спарклайнов**

Предыдущие три примера создают отдельные рабочие книги, чтобы выходные файлы было легко просматривать по отдельности. Однако в реальном сценарии часто требуется сравнить несколько серий данных бок о бок. Самый простой способ сделать это — поместить более одной группы спарклайнов в один рабочий лист, где каждая группа отображает свой стиль.

Можно добавить несколько объектов `SparklineGroup` в одну `SparklineGroupCollection`, и каждая группа может быть нацелена на разную ячейку назначения или разный диапазон. Например, можно разместить линейный спарклайн в F1, столбцовый спарклайн в F2 и спарклайн «выигрыш/проигрыш» в F3 — все они считывают данные из одного источника в строке 1 — чтобы читатель мог видеть три различных визуальных представления одних и тех же чисел.

В комбинированном примере ниже создаётся одна рабочая книга, строка 1 заполняется значениями 5, -3, 8, -2, 6, после чего в ячейки F1, F2 и F3 добавляются три группы спарклайнов — по одной каждого типа — так что полученный файл демонстрирует все три стиля спарклайнов одновременно.

```java
import com.aspose.cells.*;

// Шаг 1: Создайте рабочую книгу и получите первый рабочий лист
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// Шаг 2: Заполните образец данных в строке 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// Шаг 3: Добавьте группу линейных спарклайнов в F1
CellArea lineArea = CellArea.createCellArea(0, 5, 0, 5); // Исправление: Используйте статический фабричный метод
int lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, lineArea);
SparklineGroup lineGroup = worksheet.getSparklineGroups().get(lineIdx);

// Настройте цвет линейного спарклайна через CellsColor
CellsColor lineColor = workbook.createCellsColor();
lineColor.setColor(com.aspose.cells.Color.getBlue());
lineGroup.setSeriesColor(lineColor);

// Шаг 4: Добавьте группу столбчатых спарклайнов в F2
CellArea columnArea = CellArea.createCellArea(1, 5, 1, 5); // Исправление: Используйте статический фабричный метод
int columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, columnArea);
SparklineGroup columnGroup = worksheet.getSparklineGroups().get(columnIdx);

// Настройте цвет серии столбчатого спарклайна
CellsColor columnColor = workbook.createCellsColor();
columnColor.setColor(com.aspose.cells.Color.getGreen());
columnGroup.setSeriesColor(columnColor);

// Шаг 5: Добавьте группу спарклайнов Победа/Поражение (Составной) в F3
CellArea stackedArea = CellArea.createCellArea(2, 5, 2, 5); // Исправление: Используйте статический фабричный метод
int stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, stackedArea);
SparklineGroup stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);

// Настройте цвет серии спарклайна победа/поражение
CellsColor stackedColor = workbook.createCellsColor();
stackedColor.setColor(com.aspose.cells.Color.getDarkOrange());
stackedGroup.setSeriesColor(stackedColor);

// Шаг 6: Сохраните рабочую книгу
workbook.save("output_all.xlsx");
```

{{% alert color="primary" %}}

При объединении нескольких групп спарклайнов в одном рабочем листе каждая группа является независимой. Они могут совместно использовать один и тот же диапазон источника или использовать разные диапазоны источника, и они могут быть оформлены независимо. Это позволяет легко создать небольшую «панель мониторинга» внутриклеточных визуализаций непосредственно внутри существующего рабочего листа.

{{% /alert %}}

## **Настройка внешнего вида спарклайнов**

После создания `SparklineGroup` и добавления его в `worksheet.getSparklineGroups()` можно прочитать или изменить несколько его визуальных свойств перед сохранением рабочей книги. Наиболее часто настраиваемые свойства:

- **`group.getType()`** — `SparklineType` (LINE, COLUMN или STACKED). Оно задаётся при добавлении группы, но его можно прочитать обратно для подтверждения.
- **`group.getLine().setColor(...)`** — цвет линии, выраженный как `CellsColor`, созданный с помощью `workbook.createCellsColor()`. Это свойство используется для задания цвета обводки линейного спарклайна.
- **`group.getLine().setWeight(...)`** — толщина линии в пунктах. Более высокие значения дают более толстые линии.
- **Маркеры верхних/нижних точек** — флаги, которые включают маленькие маркеры на самых высоких и самых низких точках данных, полезные для выделения экстремумов.
- **Маркеры первой/последней/отрицательной точек** — флаги, которые переключают маркеры на первой, последней и отрицательной точках данных.

Чтобы изменить цвет, всегда создавайте экземпляр `CellsColor` и присваивайте его соответствующему свойству. Не присваивайте `java.awt.Color` напрямую свойствам цвета спарклайна — они ожидают тип `CellsColor` из `Aspose.Cells.Drawing`. Сам метод `add` возвращает полностью типизированный объект `SparklineGroup`, поэтому можно связывать присвоения свойств с возвращаемым значением или сохранить его в локальной переменной и настроить перед сохранением.



{{< app/cells/assistant language="java" >}}
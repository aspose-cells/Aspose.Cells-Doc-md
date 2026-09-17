---
title: Спарклайны в Aspose.Cells for Java
linktitle: Спарклайны в Aspose.Cells for Java
description: Aspose.Cells — это библиотека Java для работы с файлами электронных таблиц, которая поддерживает создание спарклайнов — миниатюрных диаграмм, размещаемых внутри ячеек рабочего листа. В этой статье объясняется, как добавлять и настраивать линейные, столбцовые и спарклайны победа/поражение с помощью библиотеки Aspose.Cells.
keywords: Aspose.Cells, библиотека Java, электронная таблица, спарклайны, линейный спарклайн, столбцовый спарклайн, спарклайн победа/поражение, SparklineGroup, SparklineType
type: docs
weight: 195
url: /ru/java/creating-sparklines/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells поддерживает создание спарклайнов внутри ячеек рабочего листа. Спарклайны — это миниатюрные диаграммы, которые помещаются в одной ячейке и обеспечивают быстрое визуальное представление тенденций данных. Aspose.Cells поддерживает линейные, столбцовые спарклайны, а также спарклайны победа/поражение, каждый из которых можно настроить по цвету, толщине линии, верхним/нижним точкам и маркерам.

## **Введение**
Спарклайны — это крошечные внутриклеточные диаграммы, которые полезны, когда требуется отобразить быструю тенденцию рядом со строкой или столбцом данных, не занимая пространство полноценной диаграммы. Excel поддерживает три вида спарклайнов: **линейные**, **столбцовые** и **победа/поражение**. Aspose.Cells дублирует эту возможность через API `SparklineGroup` и `SparklineGroupCollection`, которые находятся в пространстве имён `Aspose.Cells.Charts`.
В Aspose.Cells каждый добавляемый вами спарклайн создаётся через `worksheet.getSparklineGroups().add(...)`, который возвращает объект `SparklineGroup`. Затем вы можете использовать этот объект, чтобы задать тип спарклайна, диапазон данных, целевую ячейку и визуальные свойства, такие как цвет линии, толщина линии, маркеры и индикаторы верхних/нижних точек.
В этой статье рассматриваются все три типа спарклайнов, поддерживаемых Aspose.Cells — **Линейный**, **Столбцовый** и **Победа/Поражение** — и показано, как их добавлять, настраивать их цвета и сохранять полученную рабочую книгу.

## **Линейные спарклайны**
Линейный спарклайн рисует непрерывную линию через точки данных в серии, что делает его наиболее естественным выбором для отображения тенденций во времени. В Aspose.Cells линейный спарклайн создаётся путём передачи `SparklineType.LINE` в метод `add`.
1. Создайте новую `Workbook` и откройте первый рабочий лист.
2. Заполните строку исходными данными (например, строка 1, столбцы от A до E) значениями, которые вы хотите визуализировать.
3. Создайте `CellArea`, описывающую целевую ячейку, в которой будет нарисован спарклайн.
4. Вызовите `worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest)`. Третий аргумент — `false` — сообщает Aspose.Cells, что диапазон данных горизонтальный (строка), а не вертикальный (столбец).
5. При необходимости настройте возвращённый `SparklineGroup`. Для линейного спарклайна вы можете задать цвет линии с помощью `group.getLine().setColor(...)` (который ожидает `CellsColor` из `Aspose.Cells.Drawing`), настроить толщину линии и включить маркеры верхних/нижних точек.
6. Сохраните рабочую книгу.
В следующем примере создаётся рабочая книга, значения 5, -3, 8, -2, 6 записываются в ячейки от A1 до E1, а в ячейку F1 добавляется линейный спарклайн, отслеживающий эти значения. Также настраивается красный цвет линии и включаются маркеры для верхних и нижних точек.

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
            // Шаг 3: Создайте CellArea, указывающую на ячейку назначения F1
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // столбец F (нумерация с 0)
            dest.EndColumn = 5;
            dest.StartRow = 0;      // строка 1 (нумерация с 0)
            dest.EndRow = 0;
            // Шаг 4: Добавьте спарклайн-линию из A1:E1 в F1
            // SparklineGroups.add возвращает индекс только что добавленной группы
            int index = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest);
            SparklineGroup group = worksheet.getSparklineGroups().get(index);
            // Шаг 5: Создайте красный CellsColor и назначьте его цветом линии спарклайна
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
Столбцовый спарклайн отображает каждую точку данных в виде вертикальной полосы. Это делает его хорошо подходящим для данных, величина которых имеет значение — например, ежемесячных показателей продаж или количественных значений. В Aspose.Cells столбцовый спарклайн создаётся путём передачи `SparklineType.COLUMN` в метод `add`.
Процедура аналогична примеру с линейным спарклайном:
1. Создайте новую `Workbook` и откройте первый рабочий лист.
2. Заполните строку исходными данными (например, строка 1, столбцы от A до E) значениями, которые вы хотите визуализировать.
3. Создайте `CellArea`, описывающую целевую ячейку.
4. Вызовите `worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest)`.
5. При необходимости настройте полученный `SparklineGroup` — например, проверив тип через `group.getType()` или изменив цвет полос.
6. Сохраните рабочую книгу в отдельный выходной файл, чтобы не перезаписать пример с линейным спарклайном.
В примере ниже значения 5, -3, 8, -2, 6 записываются в A1:E1, а в F1 отображается столбцовый спарклайн. Отрицательные значения рисуются в виде полос, направленных вниз, а положительные — в виде полос, направленных вверх, что позволяет легко увидеть положительные и отрицательные вклады с одного взгляда.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// Write sample values into A1:E1
int[] values = new int[] { 5, -3, 8, -2, 6 };
for (int i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}
// Build a CellArea pointing to F1 (column index 5, row index 0)
CellArea dest = new CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);
// Add a Column sparkline to the destination cell
int idx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest);
SparklineGroup group = worksheet.getSparklineGroups().get(idx);
// Confirm the sparkline type by reading group.Type
System.out.println("Sparkline Type added: " + group.getType());
// Save the workbook
workbook.save("output_column.xlsx");
System.out.println("Workbook saved as output_column.xlsx");
```

## **Спарклайны Победа/Поражение**
Спарклайн победа/поражение — это особый вариант столбцового спарклайна, предназначенный для отображения только двух исходов: положительное значение рисуется как «восходящая» полоса (победа), а нулевое или отрицательное значение — как «нисходящая» полоса (поражение). Спарклайны победа/поражение обычно используются для визуализации последовательностей побед и поражений, результатов «прошёл/не прошёл» или любого бинарного исхода во времени.
В Aspose.Cells спарклайн победа/поражение создаётся путём передачи `SparklineType.STACKED` в метод `add`. (Несмотря на название, `SparklineType.STACKED` — это значение перечисления, используемое для запроса рендеринга победа/поражение.)
1. Создайте новую `Workbook` и откройте первый рабочий лист.
2. Заполните исходный диапазон. Поскольку спарклайны победа/поражение трактуют каждое значение либо как победу, либо как поражение, величина значения не имеет значения — важен только его знак. Положительные значения становятся восходящими полосами, а неположительные — нисходящими.
3. Создайте `CellArea`, описывающую целевую ячейку.
4. Вызовите `worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest)`.
5. При необходимости настройте возвращённый `SparklineGroup`, например, задав акцентные цвета для полос победы и поражения.
6. Сохраните рабочую книгу под отдельным именем файла, чтобы все три примера могли сосуществовать на диске.

```java
import com.aspose.cells.*;
import com.aspose.cells.charts.*;
import com.aspose.cells.drawing.*;
import java.awt.Color;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("WinLoss");
// Заполнение примера данных
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
// Добавление спарклайн-диаграммы "Победа/Поражение" (SparklineType.Stacked)
int groupIndex = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest);
SparklineGroup group = worksheet.getSparklineGroups().get(groupIndex);
// Настройка группы спарклайн-диаграмм
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);
// Установка зелёного цвета для точки максимума
CellsColor highColor = workbook.createCellsColor();
highColor.setColor(Color.GREEN);
group.setHighPointColor(highColor);
// Установка красного цвета для точки минимума
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
// Сохранение рабочей книги
workbook.save("output_winloss.xlsx");
System.out.println("Workbook saved successfully: output_winloss.xlsx");
```

## **Объединение всех трёх типов спарклайнов**
В комбинированном примере ниже создаётся одна рабочая книга, строка 1 заполняется значениями 5, -3, 8, -2, 6, а затем в ячейки F1, F2 и F3 добавляются три группы спарклайнов — по одной каждого типа — так, что полученный файл демонстрирует все три стиля спарклайнов одновременно.

```java
import com.aspose.cells.*;
// Step 1: Create a Workbook and get the first worksheet
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// Step 2: Populate sample data in row 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// Step 3: Add a Line sparkline group at F1
CellArea lineArea = CellArea.createCellArea(0, 5, 0, 5); // Fix: Use static factory method
int lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, lineArea);
SparklineGroup lineGroup = worksheet.getSparklineGroups().get(lineIdx);
// Customize the line sparkline color via CellsColor
CellsColor lineColor = workbook.createCellsColor();
lineColor.setColor(com.aspose.cells.Color.getBlue());
lineGroup.setSeriesColor(lineColor);
// Step 4: Add a Column sparkline group at F2
CellArea columnArea = CellArea.createCellArea(1, 5, 1, 5); // Fix: Use static factory method
int columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, columnArea);
SparklineGroup columnGroup = worksheet.getSparklineGroups().get(columnIdx);
// Customize the column sparkline series color
CellsColor columnColor = workbook.createCellsColor();
columnColor.setColor(com.aspose.cells.Color.getGreen());
columnGroup.setSeriesColor(columnColor);
// Step 5: Add a Win/Loss (Stacked) sparkline group at F3
CellArea stackedArea = CellArea.createCellArea(2, 5, 2, 5); // Fix: Use static factory method
int stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, stackedArea);
SparklineGroup stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);
// Customize the win/loss sparkline series color
CellsColor stackedColor = workbook.createCellsColor();
stackedColor.setColor(com.aspose.cells.Color.getDarkOrange());
stackedGroup.setSeriesColor(stackedColor);
// Step 6: Save the workbook
workbook.save("output_all.xlsx");
```

## **Настройка внешнего вида спарклайнов**
После того как `SparklineGroup` создан и добавлен в `worksheet.getSparklineGroups()`, вы можете прочитать или изменить несколько его визуальных свойств перед сохранением рабочей книги. Наиболее часто настраиваемые свойства:
- **`group.getType()`** — `SparklineType` (LINE, COLUMN или STACKED). Оно устанавливается при добавлении группы, но вы можете прочитать его обратно, чтобы убедиться.
- **`group.getLine().setColor(...)`** — цвет линии, выраженный как `CellsColor`, созданный через `workbook.createCellsColor()`. Это свойство следует использовать для цвета обводки линейного спарклайна.
- **`group.getLine().setWeight(...)`** — толщина линии в пунктах. Более высокие значения дают более толстые линии.
- **Маркеры верхних/нижних точек** — флаги, которые включают небольшие маркеры на самых высоких и самых низких точках данных, что полезно для выделения экстремумов.
- **Маркеры первой/последней/отрицательной точки** — флаги, которые переключают маркеры на первой, последней и отрицательной точках данных.
Чтобы изменить цвет, всегда создавайте экземпляр `CellsColor` и присваивайте его соответствующему свойству. Не присваивайте `java.awt.Color` непосредственно свойствам цвета спарклайна — они ожидают тип `CellsColor` из `Aspose.Cells.Drawing`. Сам метод `add` возвращает полностью типизированный объект `SparklineGroup`, поэтому вы можете объединять присваивания свойств в возвращаемом значении или сохранить его в локальной переменной и настроить перед сохранением.
{{% /alert %}}

{{< app/cells/assistant language="java" >}}
---
title: Спарклайны в Aspose.Cells for .NET
description: Aspose.Cells — это библиотека .NET для работы с файлами электронных таблиц, которая поддерживает создание спарклайнов — миниатюрных диаграмм, размещаемых внутри ячеек рабочего листа. В этой статье объясняется, как добавлять и настраивать линейные, столбчатые спарклайны и спарклайны победа/поражение с использованием библиотеки Aspose.Cells.
linktitle: Спарклайны
keywords: Aspose.Cells, библиотека .NET, электронная таблица, спарклайны, линейный спарклайн, столбчатый спарклайн, спарклайн победа/поражение, SparklineGroup, SparklineType
type: docs
weight: 195
url: /ru/net/creating-sparklines/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells поддерживает создание спарклайнов внутри ячеек рабочего листа. Спарклайны — это миниатюрные диаграммы, которые помещаются в одну ячейку и обеспечивают быструю визуальную индикацию тенденций данных. Aspose.Cells поддерживает линейные, столбчатые спарклайны и спарклайны победа/поражение, каждый из которых можно настроить по цвету, толщине линии, маркерам максимальных/минимальных точек и другим маркерам.

## **Введение**
Спарклайны — это крошечные внутриклеточные диаграммы, которые полезны, когда требуется отобразить быструю тенденцию рядом со строкой или столбцом данных, не занимая пространства полноценной диаграммы. Excel поддерживает три вида спарклайнов: **линейные**, **столбчатые** и **победа/поражение**. Aspose.Cells реализует ту же возможность через API `SparklineGroup` и `SparklineGroupCollection`, расположенные в пространстве имён `Aspose.Cells.Charts`.
В Aspose.Cells каждый добавляемый спарклайн создаётся через `worksheet.SparklineGroups.Add(...)`, который возвращает объект `SparklineGroup`. Затем этот объект можно использовать для задания типа спарклайна, диапазона данных, ячейки назначения и визуальных свойств, таких как цвет линии, толщина линии, маркеры и индикаторы максимальных/минимальных точек.
В этой статье рассматривается каждый из трёх типов спарклайнов, поддерживаемых Aspose.Cells — **Линейный**, **Столбчатый** и **Победа/Поражение** — и показано, как их добавлять, настраивать их цвета и сохранять полученную рабочую книгу.

## **Линейные спарклайны**
Линейный спарклайн рисует непрерывную линию через точки данных в серии, что делает его наиболее естественным выбором для отображения тенденций во времени. В Aspose.Cells линейный спарклайн создаётся путём передачи `SparklineType.Line` в метод `SparklineGroups.Add`.
1. Создайте новый объект `Workbook` и откройте первый рабочий лист.
2. Заполните строку исходных данных (например, строка 1, столбцы от A до E) значениями, которые требуется визуализировать.
3. Создайте объект `CellArea`, описывающий ячейку назначения, в которой будет нарисован спарклайн.
4. Вызовите `worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest)`. Третий аргумент — `false` — указывает Aspose.Cells, что диапазон данных горизонтальный (строка), а не вертикальный (столбец).
5. При необходимости настройте возвращённый объект `SparklineGroup`. Для линейного спарклайна можно задать цвет линии с помощью `group.Line.Color` (который ожидает `CellsColor` из `Aspose.Cells.Drawing`), настроить толщину линии и включить/отключить маркеры максимальных/минимальных точек.
6. Сохраните рабочую книгу.
Следующий пример создаёт рабочую книгу, записывает значения 5, -3, 8, -2, 6 в ячейки от A1 до E1 и добавляет линейный спарклайн в ячейку F1, который отображает эти значения. Также в нём настраивается красный цвет линии и включаются маркеры для максимальных и минимальных точек.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Charts;
using Aspose.Cells.Drawing;
namespace SparklineDemo
{
    public class Program
    {
        public static void Main()
        {
            // Шаг 1: Создаём книгу и получаем первый лист
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            Cells cells = worksheet.Cells;
            // Шаг 2: Записываем образцы значений 5, -3, 8, -2, 6 в ячейки A1:E1
            cells["A1"].PutValue(5);
            cells["B1"].PutValue(-3);
            cells["C1"].PutValue(8);
            cells["D1"].PutValue(-2);
            cells["E1"].PutValue(6);
            // Шаг 3: Создаём CellArea, указывающую на целевую ячейку F1
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // столбец F (индекс с нуля)
            dest.EndColumn = 5;
            dest.StartRow = 0;      // строка 1 (индекс с нуля)
            dest.EndRow = 0;
            // Шаг 4: Добавляем спарклайн-линию из A1:E1 в F1
            // SparklineGroups.Add возвращает индекс вновь добавленной группы
            int index = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest);
            SparklineGroup group = worksheet.SparklineGroups[index];
            // Шаг 5: Создаём красный CellsColor и назначаем его цветом линии спарклайна
            CellsColor red = workbook.CreateCellsColor();
            red.Color = System.Drawing.Color.Red;
            group.SeriesColor = red;
            // Шаг 6: Включаем маркеры максимальной и минимальной точек
            group.ShowHighPoint = true;
            group.ShowLowPoint = true;
            // Шаг 7: Сохраняем книгу
            workbook.Save("output_line.xlsx");
        }
    }
}
```

## **Столбчатые спарклайны**
Столбчатый спарклайн отображает каждую точку данных в виде вертикальной полосы. Это делает его хорошо подходящим для данных, величина которых значима — например, ежемесячные показатели продаж или подсчёты. В Aspose.Cells столбчатый спарклайн создаётся путём передачи `SparklineType.Column` в метод `SparklineGroups.Add`.
Процедура повторяет пример с линейным спарклайном:
1. Создайте новый объект `Workbook` и откройте первый рабочий лист.
2. Заполните строку исходных данных (например, строка 1, столбцы от A до E) значениями, которые требуется визуализировать.
3. Создайте объект `CellArea`, описывающий ячейку назначения.
4. Вызовите `worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, dest)`.
5. При необходимости настройте полученный объект `SparklineGroup` — например, задав `group.Type` для подтверждения типа или подобрав цвет полос.
6. Сохраните рабочую книгу в отдельный выходной файл, чтобы она не перезаписала пример с линейным спарклайном.
В примере ниже значения 5, -3, 8, -2, 6 записываются в A1:E1, а в F1 отображается столбчатый спарклайн. Отрицательные значения рисуются в виде полос, направленных вниз, а положительные — вверх, что позволяет легко выделить положительный и отрицательный вклад.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Charts;
using Aspose.Cells.Drawing;
namespace SparklineDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            // Шаг 1: Создайте рабочую книгу и получите первый рабочий лист
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            // Шаг 2: Запишите образцовые значения в A1:E1
            int[] values = { 5, -3, 8, -2, 6 };
            for (int i = 0; i < values.Length; i++)
            {
                worksheet.Cells[0, i].PutValue(values[i]);
            }
            // Шаг 3: Создайте CellArea, указывающую на F1 (индекс столбца 5, индекс строки 0)
            CellArea dest = new CellArea();
            dest.StartColumn = 5;
            dest.EndColumn = 5;
            dest.StartRow = 0;
            dest.EndRow = 0;
            // Шаг 4: Добавьте спарклайн типа Column в целевую ячейку
            int idx = worksheet.SparklineGroups.Add(
                SparklineType.Column, "A1:E1", false, dest);
            SparklineGroup group = worksheet.SparklineGroups[idx];
            // Шаг 5: Подтвердите тип спарклайна, прочитав group.Type
            Console.WriteLine("Sparkline Type added: " + group.Type);
            // Шаг 6: Сохраните рабочую книгу
            workbook.Save("output_column.xlsx");
            Console.WriteLine("Workbook saved as output_column.xlsx");
        }
    }
}
```

## **Спарклайны победа/поражение**
Спарклайн победа/поражение — это особая разновидность столбчатого спарклайна, предназначенная для отображения только двух исходов: положительное значение рисуется как полоса вверх (победа), а нулевое или отрицательное значение — как полоса вниз (поражение). Спарклайны победа/поражение часто используются для визуализации последовательностей побед и поражений, результатов «пройдено/не пройдено» или любого бинарного исхода во времени.
В Aspose.Cells спарклайн победа/поражение создаётся путём передачи `SparklineType.Stacked` в метод `SparklineGroups.Add`. (Несмотря на название, `SparklineType.Stacked` — это значение перечисления, используемое для запроса отрисовки победа/поражение.)
1. Создайте новый объект `Workbook` и откройте первый рабочий лист.
2. Заполните исходный диапазон. Поскольку спарклайны победа/поражение рассматривают каждое значение как победу или поражение, величина значения не имеет значения — важен только его знак. Положительные значения становятся полосами вверх, а неположительные — полосами вниз.
3. Создайте объект `CellArea`, описывающий ячейку назначения.
4. Вызовите `worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, dest)`.
5. При необходимости настройте возвращённый объект `SparklineGroup`, например задав акцентные цвета для полос победы и поражения.
6. Сохраните рабочую книгу под уникальным именем файла, чтобы все три примера могли сосуществовать на диске.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Charts;
using Aspose.Cells.Drawing;
namespace SparklineDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            // Шаг 1: Создайте книгу и получите первый рабочий лист
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            worksheet.Name = "WinLoss";
            // Шаг 2: Заполните образец данных в строке 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
            worksheet.Cells["A1"].PutValue(5);
            worksheet.Cells["B1"].PutValue(-3);
            worksheet.Cells["C1"].PutValue(8);
            worksheet.Cells["D1"].PutValue(-2);
            worksheet.Cells["E1"].PutValue(6);
            // Шаг 3: Создайте CellArea, указывающую на F1 (столбец 5, строка 0)
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // F
            dest.EndColumn = 5;
            dest.StartRow = 0;      // строка 1
            dest.EndRow = 0;
            // Шаг 4: Добавьте спарклайн Win/Loss (SparklineType.Stacked)
            int groupIndex = worksheet.SparklineGroups.Add(
                SparklineType.Stacked,
                "A1:E1",
                false,
                dest);
            SparklineGroup group = worksheet.SparklineGroups[groupIndex];
            // Шаг 5: Настройте группу спарклайнов
            // Включите маркеры верхних и нижних точек
            group.ShowHighPoint = true;
            group.ShowLowPoint = true;
            group.ShowNegativePoints = true;
            // Установите зеленый цвет для верхних точек
            CellsColor highColor = workbook.CreateCellsColor();
            highColor.Color = System.Drawing.Color.Green;
            group.HighPointColor = highColor;
            // Установите красный цвет для нижних точек
            CellsColor lowColor = workbook.CreateCellsColor();
            lowColor.Color = System.Drawing.Color.Red;
            group.LowPointColor = lowColor;
            // Установите оранжевый цвет для отрицательных точек
            CellsColor negColor = workbook.CreateCellsColor();
            negColor.Color = System.Drawing.Color.Orange;
            group.NegativePointsColor = negColor;
            // Установите цвет серии по умолчанию (используется для положительных столбцов)
            CellsColor seriesColor = workbook.CreateCellsColor();
            seriesColor.Color = System.Drawing.Color.SteelBlue;
            group.SeriesColor = seriesColor;
            // Шаг 6: Сохраните книгу
            workbook.Save("output_winloss.xlsx");
            Console.WriteLine("Workbook saved successfully: output_winloss.xlsx");
        }
    }
}
```

## **Объединение всех трёх типов спарклайнов**
В приведённом ниже комбинированном примере создаётся одна рабочая книга, строка 1 заполняется значениями 5, -3, 8, -2, 6, после чего в ячейки F1, F2 и F3 добавляются три группы спарклайнов — по одной каждого типа — так что полученный файл одновременно демонстрирует все три стиля спарклайнов.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Charts;
// Шаг 1: Создайте рабочую книгу и получите первый рабочий лист
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// Шаг 2: Заполните образец данных в строке 1 (A1:E1)
worksheet.Cells["A1"].PutValue(5);
worksheet.Cells["B1"].PutValue(-3);
worksheet.Cells["C1"].PutValue(8);
worksheet.Cells["D1"].PutValue(-2);
worksheet.Cells["E1"].PutValue(6);
// Шаг 3: Добавьте группу спарклайнов "Линия" в F1
CellArea lineArea = new CellArea();
lineArea.StartColumn = 5;
lineArea.EndColumn = 5;
lineArea.StartRow = 0;
lineArea.EndRow = 0;
int lineIdx = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, lineArea);
SparklineGroup lineGroup = worksheet.SparklineGroups[lineIdx];
// Настройте цвет спарклайна "Линия" с помощью CellsColor
CellsColor lineColor = workbook.CreateCellsColor();
lineColor.Color = System.Drawing.Color.Blue;
lineGroup.SeriesColor = lineColor;
// Шаг 4: Добавьте группу спарклайнов "Столбец" в F2
CellArea columnArea = new CellArea();
columnArea.StartColumn = 5;
columnArea.EndColumn = 5;
columnArea.StartRow = 1;
columnArea.EndRow = 1;
int columnIdx = worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, columnArea);
SparklineGroup columnGroup = worksheet.SparklineGroups[columnIdx];
// Настройте цвет серии спарклайна "Столбец"
CellsColor columnColor = workbook.CreateCellsColor();
columnColor.Color = System.Drawing.Color.Green;
columnGroup.SeriesColor = columnColor;
// Шаг 5: Добавьте группу спарклайнов "Победа/Проигрыш" (Составной) в F3
CellArea stackedArea = new CellArea();
stackedArea.StartColumn = 5;
stackedArea.EndColumn = 5;
stackedArea.StartRow = 2;
stackedArea.EndRow = 2;
int stackedIdx = worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, stackedArea);
SparklineGroup stackedGroup = worksheet.SparklineGroups[stackedIdx];
// Настройте цвет серии спарклайна "Победа/Проигрыш"
CellsColor stackedColor = workbook.CreateCellsColor();
stackedColor.Color = System.Drawing.Color.DarkOrange;
stackedGroup.SeriesColor = stackedColor;
// Шаг 6: Сохраните рабочую книгу
workbook.Save("output_all.xlsx");
```

## **Настройка внешнего вида спарклайнов**
После создания объекта `SparklineGroup` и его добавления в `worksheet.SparklineGroups` можно прочитать или изменить несколько его визуальных свойств перед сохранением рабочей книги. Наиболее часто настраиваемые свойства:
- **`group.Type`** — значение `SparklineType` (Line, Column или Stacked). Оно задаётся при добавлении группы, но можно прочитать его обратно для подтверждения.
- **`group.Line.Color`** — цвет линии, выраженный как `CellsColor`, созданный с помощью `workbook.CreateCellsColor()`. Это свойство используется для задания цвета обводки линейного спарклайна.
- **`group.Line.Weight`** — толщина линии в пунктах. Бо́льшие значения дают более толстые линии.
- **Маркеры максимальных/минимальных точек** — флаги, которые включают небольшие маркеры на наивысших и наименьших точках данных; полезны для выделения экстремумов.
- **Маркеры первой/последней/отрицательной точек** — флаги, которые включают или отключают маркеры на первой, последней и отрицательной точках данных.
Чтобы изменить цвет, всегда создавайте экземпляр `CellsColor` и присваивайте его соответствующему свойству. Не присваивайте `System.Drawing.Color` напрямую свойствам цвета спарклайна — они ожидают тип `CellsColor` из `Aspose.Cells.Drawing`. Сам метод `SparklineGroups.Add` возвращает полностью типизированный объект `SparklineGroup`, поэтому можно связывать присваивания свойств к возвращаемому значению либо сохранить его в локальной переменной и настроить перед сохранением.
{{% /alert %}}

## Связанные статьи
- [Преобразование спарклайна в изображение и HTML в Aspose.Cells for .NET](/cells/ru/net/convert-sparkline-to-image-and-html/)
- [Добавление полей фильтра в сводную таблицу в Aspose.Cells for .NET](/cells/ru/net/add-page-field-in-pivot-table/)
- [Применение стилей к сводным таблицам в Aspose.Cells for .NET](/cells/ru/net/apply-style-to-pivot-table/)
- [Изменение макета поля страницы в сводной таблице](/cells/ru/net/change-page-field-layout/)
- [Преобразование Excel в формат OFD](/cells/ru/net/converting-excel-to-ofd-format/)csharp

{{< app/cells/assistant language="csharp" >}}
---
title: Спарклайны в Aspose.Cells for .NET
linktitle: Спарклайны
description: Aspose.Cells — это библиотека для .NET для работы с файлами электронных таблиц, которая поддерживает создание спарклайнов — миниатюрных диаграмм, размещаемых внутри ячеек рабочего листа. В этой статье объясняется, как добавлять и настраивать линейные, столбцовые и спарклайны «выигрыш/проигрыш» с помощью библиотеки Aspose.Cells.
keywords: Aspose.Cells, .NET library, spreadsheet, sparklines, line sparkline, column sparkline, win/loss sparkline, SparklineGroup, SparklineType
type: docs
weight: 195
url: /ru/net/creating-sparklines/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells поддерживает создание спарклайнов внутри ячеек рабочего листа. Спарклайны — это миниатюрные диаграммы, которые помещаются в одну ячейку и дают быстрое визуальное представление о тенденциях в данных. Aspose.Cells поддерживает линейные, столбцовые спарклайны и спарклайны «выигрыш/проигрыш», каждый из которых можно настроить по цвету, толщине линии, отображению максимальных/минимальных точек и маркеров.

{{% /alert %}}

## **Введение**

Спарклайны — это крошечные внутриклеточные диаграммы, которые удобны, когда требуется отобразить быструю тенденцию рядом со строкой или столбцом данных, не занимая пространство полноценной диаграммы. Excel поддерживает три вида спарклайнов: **линейные**, **столбцовые** и **«выигрыш/проигрыш»**. Aspose.Cells воспроизводит эту возможность через API `SparklineGroup` и `SparklineGroupCollection`, расположенные в пространстве имён `Aspose.Cells.Charts`.

В Aspose.Cells каждый добавляемый вами спарклайн создаётся с помощью `worksheet.SparklineGroups.Add(...)`, который возвращает объект `SparklineGroup`. Затем вы можете использовать этот объект, чтобы задать тип спарклайна, диапазон данных, целевую ячейку и визуальные свойства, такие как цвет линии, толщина линии, маркеры и индикаторы максимальных/минимальных точек.

{{% alert color="primary" %}}

Один `SparklineGroup` может содержать один или несколько спарклайнов, имеющих общий стиль. Когда вы вызываете `Add` и передаёте строку данных и одну целевую ячейку, вы получаете один спарклайн внутри этой ячейки. Если ваш диапазон назначения шире одной ячейки, в каждой ячейке назначения рисуется отдельный спарклайн, все с использованием одного и того же стиля и диапазона данных.

{{% /alert %}}

В этой статье рассматривается каждый из трёх типов спарклайнов, поддерживаемых Aspose.Cells — **Линейный**, **Столбцовый** и **«Выигрыш/Проигрыш»** — и показано, как их добавлять, настраивать их цвета и сохранять полученную рабочую книгу.

## **Линейные спарклайны**

Линейный спарклайн рисует непрерывную линию через точки данных в серии, что делает его наиболее естественным выбором для отображения тенденций во времени. В Aspose.Cells линейный спарклайн создаётся путём передачи `SparklineType.Line` в метод `SparklineGroups.Add`.

Рабочий процесс аналогичен любому другому типу спарклайна:

1. Создайте новую `Workbook` и откройте первый рабочий лист.
2. Заполните строку исходных данных (например, строка 1, столбцы от A до E) значениями, которые вы хотите визуализировать.
3. Создайте `CellArea`, описывающую целевую ячейку, в которой будет нарисован спарклайн.
4. Вызовите `worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest)`. Третий аргумент — `false` — указывает Aspose.Cells, что диапазон данных расположен горизонтально (строка), а не вертикально (столбец).
5. При необходимости настройте возвращённый `SparklineGroup`. Для линейного спарклайна можно задать цвет линии с помощью `group.Line.Color` (который ожидает `CellsColor` из `Aspose.Cells.Drawing`), отрегулировать толщину линии и включить/отключить маркеры максимальных/минимальных точек.
6. Сохраните рабочую книгу.

Следующий пример создаёт рабочую книгу, записывает значения 5, -3, 8, -2, 6 в ячейки от A1 до E1 и добавляет линейный спарклайн в ячейку F1, который отслеживает эти значения. Он также настраивает цвет линии на красный и включает маркеры для максимальных и минимальных точек.

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
            // Шаг 1: Создаем книгу и получаем первый лист
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            Cells cells = worksheet.Cells;

            // Шаг 2: Записываем образцы значений 5, -3, 8, -2, 6 в ячейки A1:E1
            cells["A1"].PutValue(5);
            cells["B1"].PutValue(-3);
            cells["C1"].PutValue(8);
            cells["D1"].PutValue(-2);
            cells["E1"].PutValue(6);

            // Шаг 3: Создаем CellArea, указывающую на ячейку назначения F1
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // столбец F (с нулевой индексацией)
            dest.EndColumn = 5;
            dest.StartRow = 0;      // строка 1 (с нулевой индексацией)
            dest.EndRow = 0;

            // Шаг 4: Добавляем линейную спарклайн из A1:E1 в F1
            // SparklineGroups.Add возвращает индекс только что добавленной группы
            int index = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest);
            SparklineGroup group = worksheet.SparklineGroups[index];

            // Шаг 5: Создаем красный CellsColor и назначаем его цвету линии спарклайна
            CellsColor red = workbook.CreateCellsColor();
            red.Color = System.Drawing.Color.Red;
            group.SeriesColor = red;

            // Шаг 6: Включаем маркеры высоких и низких точек
            group.ShowHighPoint = true;
            group.ShowLowPoint = true;

            // Шаг 7: Сохраняем книгу
            workbook.Save("output_line.xlsx");
        }
    }
}
```

## **Столбцовые спарклайны**

Столбцовый спарклайн отображает каждую точку данных в виде вертикальной полосы. Это делает его хорошо подходящим для данных, величина которых имеет значение — например, ежемесячных показателей продаж или подсчётов. В Aspose.Cells столбцовый спарклайн создаётся путём передачи `SparklineType.Column` в метод `SparklineGroups.Add`.

Процедура повторяет пример с линейным спарклайном:

1. Создайте новую `Workbook` и откройте первый рабочий лист.
2. Заполните тот же исходный диапазон (A1:E1) значениями, которые вы хотите визуализировать.
3. Создайте `CellArea`, описывающую целевую ячейку.
4. Вызовите `worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, dest)`.
5. При необходимости настройте полученный `SparklineGroup` — например, задав `group.Type` для подтверждения типа или изменив цвет полос.
6. Сохраните рабочую книгу в отдельный выходной файл, чтобы не перезаписать пример с линейным спарклайном.

Пример ниже записывает значения 5, -3, 8, -2, 6 в A1:E1 и отображает столбцовый спарклайн в F1. Отрицательные значения рисуются как полосы, направленные вниз, а положительные — как полосы, направленные вверх, что позволяет легко увидеть положительные и отрицательные вклады.

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
            // Шаг 1: Создайте Workbook и получите первый рабочий лист
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];

            // Шаг 2: Запишите образец значений в A1:E1
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

            // Шаг 4: Добавьте спарклайн типа Column в ячейку назначения
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

## **Спарклайны «Выигрыш/Проигрыш»**

Спарклайн «выигрыш/проигрыш» — это особый вариант столбцового спарклайна, предназначенный для отображения только двух исходов: положительное значение рисуется как «верхняя» полоса (выигрыш), а нулевое или отрицательное значение — как «нижняя» полоса (проигрыш). Спарклайны «выигрыш/проигрыш» обычно используются для визуализации последовательностей побед и поражений, результатов «сдал/не сдал» или любого бинарного исхода во времени.

В Aspose.Cells спарклайн «выигрыш/проигрыш» создаётся путём передачи `SparklineType.Stacked` в метод `SparklineGroups.Add`. (Несмотря на название, `SparklineType.Stacked` — это значение перечисления, используемое для запроса отрисовки «выигрыш/проигрыш».)

Процедура такая же, как для двух других типов:

1. Создайте новую `Workbook` и откройте первый рабочий лист.
2. Заполните исходный диапазон. Поскольку спарклайны «выигрыш/проигрыш» интерпретируют каждое значение как выигрыш или проигрыш, величина значения не имеет значения — важен только его знак. Положительные значения становятся верхними полосами, а неположительные — нижними.
3. Создайте `CellArea`, описывающую целевую ячейку.
4. Вызовите `worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, dest)`.
5. При необходимости настройте возвращённый `SparklineGroup`, например, задав акцентные цвета для полос выигрыша и проигрыша.
6. Сохраните рабочую книгу под уникальным именем файла, чтобы все три примера могли сосуществовать на диске.

Пример ниже использует те же входные данные, что и предыдущие два раздела. Значения 5, -3, 8, -2, 6 интерпретируются как выигрыш, проигрыш, выигрыш, проигрыш, выигрыш — и спарклайн, нарисованный в F1, точно отражает этот шаблон.

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
            // Шаг 1: Создаём Workbook и получаем первый рабочий лист
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            worksheet.Name = "WinLoss";

            // Шаг 2: Заполняем выборочными данными строку 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
            worksheet.Cells["A1"].PutValue(5);
            worksheet.Cells["B1"].PutValue(-3);
            worksheet.Cells["C1"].PutValue(8);
            worksheet.Cells["D1"].PutValue(-2);
            worksheet.Cells["E1"].PutValue(6);

            // Шаг 3: Создаём CellArea, указывающую на F1 (столбец 5, строка 0)
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // F
            dest.EndColumn = 5;
            dest.StartRow = 0;      // строка 1
            dest.EndRow = 0;

            // Шаг 4: Добавляем спарклайн Win/Loss (SparklineType.Stacked)
            int groupIndex = worksheet.SparklineGroups.Add(
                SparklineType.Stacked,
                "A1:E1",
                false,
                dest);
            SparklineGroup group = worksheet.SparklineGroups[groupIndex];

            // Шаг 5: Настраиваем группу спарклайнов
            // Включаем маркеры верхних и нижних точек
            group.ShowHighPoint = true;
            group.ShowLowPoint = true;
            group.ShowNegativePoints = true;

            // Устанавливаем зелёный цвет для верхних точек
            CellsColor highColor = workbook.CreateCellsColor();
            highColor.Color = System.Drawing.Color.Green;
            group.HighPointColor = highColor;

            // Устанавливаем красный цвет для нижних точек
            CellsColor lowColor = workbook.CreateCellsColor();
            lowColor.Color = System.Drawing.Color.Red;
            group.LowPointColor = lowColor;

            // Устанавливаем оранжевый цвет для отрицательных точек
            CellsColor negColor = workbook.CreateCellsColor();
            negColor.Color = System.Drawing.Color.Orange;
            group.NegativePointsColor = negColor;

            // Устанавливаем цвет серии по умолчанию (используется для положительных столбцов)
            CellsColor seriesColor = workbook.CreateCellsColor();
            seriesColor.Color = System.Drawing.Color.SteelBlue;
            group.SeriesColor = seriesColor;

            // Шаг 6: Сохраняем книгу
            workbook.Save("output_winloss.xlsx");

            Console.WriteLine("Книга успешно сохранена: output_winloss.xlsx");
        }
    }
}
```

## **Объединение всех трёх типов спарклайнов**

Предыдущие три примера создают каждую свою рабочую книгу, чтобы выходные файлы было легко просматривать по отдельности. Однако в реальном сценарии часто требуется сравнить несколько серий данных бок о бок. Самый чистый способ сделать это — поместить более одной группы спарклайнов в один и тот же рабочий лист, где каждая группа отображает свой стиль.

Вы можете добавить несколько объектов `SparklineGroup` в одну и ту же `SparklineGroupCollection`, и каждая группа может быть нацелена на разную целевую ячейку или диапазон. Например, вы можете разместить линейный спарклайн в F1, столбцовый спарклайн в F2 и спарклайн «выигрыш/проигрыш» в F3 — все считывающие из одних и тех же исходных данных в строке 1 — чтобы читатель мог увидеть три разных визуальных представления одних и тех же чисел.

Комбинированный пример ниже создаёт одну рабочую книгу, заполняет строку 1 значениями 5, -3, 8, -2, 6, а затем добавляет три группы спарклайнов в ячейки F1, F2 и F3 — по одной каждого типа — так что полученный файл демонстрирует все три стиля спарклайнов одновременно.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Charts;

// Шаг 1: Создайте рабочую книгу и получите первый рабочий лист
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// Шаг 2: Заполните образцы данных в строке 1 (A1:E1)
worksheet.Cells["A1"].PutValue(5);
worksheet.Cells["B1"].PutValue(-3);
worksheet.Cells["C1"].PutValue(8);
worksheet.Cells["D1"].PutValue(-2);
worksheet.Cells["E1"].PutValue(6);

// Шаг 3: Добавьте группу линейных спарклайнов в F1
CellArea lineArea = new CellArea();
lineArea.StartColumn = 5;
lineArea.EndColumn = 5;
lineArea.StartRow = 0;
lineArea.EndRow = 0;
int lineIdx = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, lineArea);
SparklineGroup lineGroup = worksheet.SparklineGroups[lineIdx];

// Настройте цвет линейного спарклайна с помощью CellsColor
CellsColor lineColor = workbook.CreateCellsColor();
lineColor.Color = System.Drawing.Color.Blue;
lineGroup.SeriesColor = lineColor;

// Шаг 4: Добавьте группу столбчатых спарклайнов в F2
CellArea columnArea = new CellArea();
columnArea.StartColumn = 5;
columnArea.EndColumn = 5;
columnArea.StartRow = 1;
columnArea.EndRow = 1;
int columnIdx = worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, columnArea);
SparklineGroup columnGroup = worksheet.SparklineGroups[columnIdx];

// Настройте цвет серии столбчатого спарклайна
CellsColor columnColor = workbook.CreateCellsColor();
columnColor.Color = System.Drawing.Color.Green;
columnGroup.SeriesColor = columnColor;

// Шаг 5: Добавьте группу спарклайнов «Выигрыш/Проигрыш» (Стек) в F3
CellArea stackedArea = new CellArea();
stackedArea.StartColumn = 5;
stackedArea.EndColumn = 5;
stackedArea.StartRow = 2;
stackedArea.EndRow = 2;
int stackedIdx = worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, stackedArea);
SparklineGroup stackedGroup = worksheet.SparklineGroups[stackedIdx];

// Настройте цвет серии спарклайна «Выигрыш/Проигрыш»
CellsColor stackedColor = workbook.CreateCellsColor();
stackedColor.Color = System.Drawing.Color.DarkOrange;
stackedGroup.SeriesColor = stackedColor;

// Шаг 6: Сохраните рабочую книгу
workbook.Save("output_all.xlsx");
```

{{% alert color="primary" %}}

Когда вы объединяете несколько групп спарклайнов в одном рабочем листе, каждая группа независима. Они могут использовать один и тот же исходный диапазон или разные исходные диапазоны, и их можно стилизовать независимо. Это позволяет легко построить небольшую «панель мониторинга» внутриклеточных визуализаций прямо внутри существующего рабочего листа.

{{% /alert %}}

## **Настройка внешнего вида спарклайнов**

После того как `SparklineGroup` создан и добавлен в `worksheet.SparklineGroups`, вы можете прочитать или изменить несколько его визуальных свойств перед сохранением рабочей книги. Наиболее часто настраиваемые свойства:

- **`group.Type`** — `SparklineType` (Line, Column или Stacked). Он задаётся при добавлении группы, но его можно прочитать обратно для подтверждения.
- **`group.Line.Color`** — цвет линии, выраженный как `CellsColor`, созданный через `workbook.CreateCellsColor()`. Это свойство используется для цвета обводки линейного спарклайна.
- **`group.Line.Weight`** — толщина линии в пунктах. Более высокие значения дают более толстые линии.
- **Маркеры максимальных/минимальных точек** — флаги, которые включают маленькие маркеры на самых высоких и самых низких точках данных, полезные для выделения экстремумов.
- **Маркеры первой/последней/отрицательной точки** — флаги, которые переключают маркеры на первой, последней и отрицательной точках данных.

Чтобы изменить цвет, всегда создавайте экземпляр `CellsColor` и присваивайте его соответствующему свойству. Не присваивайте `System.Drawing.Color` напрямую свойствам цвета спарклайна — они ожидают тип `CellsColor` из `Aspose.Cells.Drawing`. Сам метод `SparklineGroups.Add` возвращает полностью типизированный объект `SparklineGroup`, поэтому вы можете связывать присвоения свойств на возвращаемом значении или сохранить его в локальной переменной и настроить перед сохранением.

## **Связанные статьи**

- [Accessing Cells of a Worksheet](/cells/ru/net/accessing-cells-of-a-worksheet/)
- [Format Worksheet Cells in a Workbook](/cells/ru/net/format-worksheet-cells-in-a-workbook/)
- [Customizing Charts](/cells/ru/net/customizing-charts/)
- [Create Dynamic Charts](/cells/ru/net/create-dynamic-charts/)
- [Manage data of Excel files](/cells/ru/net/cells-data/)

{{< app/cells/assistant language="csharp" >}}
---
title: Спарклайны в Aspose.Cells for C++
linktitle: Sparklines
description: Aspose.Cells — это библиотека C++ для работы с файлами электронных таблиц, которая поддерживает создание спарклайнов — миниатюрных диаграмм, размещаемых внутри ячеек рабочего листа. В этой статье объясняется, как добавлять и настраивать линейные, столбчатые спарклайны и спарклайны выигрышей/проигрышей с помощью библиотеки Aspose.Cells.
keywords: Aspose.Cells, C++ library, spreadsheet, sparklines, line sparkline, column sparkline, win/loss sparkline, SparklineGroup, SparklineType
type: docs
weight: 195
url: /ru/cpp/creating-sparklines/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells поддерживает создание спарклайнов внутри ячеек рабочего листа. Спарклайны — это миниатюрные диаграммы, которые помещаются в одну ячейку и обеспечивают быструю визуальную демонстрацию тенденций в данных. Aspose.Cells поддерживает линейные, столбчатые спарклайны и спарклайны выигрышей/проигрышей, каждый из которых можно настроить по цвету, толщине линии, точкам максимума/минимума и маркерам.

{{% /alert %}}

## **Введение**

Спарклайны — это крошечные внутриклеточные диаграммы, которые полезны, когда требуется отобразить быструю тенденцию рядом со строкой или столбцом данных, не занимая места полноценной диаграммы. Excel поддерживает три вида спарклайнов: **линейные**, **столбчатые** и **выигрышей/проигрышей**. Aspose.Cells дублирует эту возможность через API `SparklineGroup` и `SparklineGroupCollection`, которые находятся в пространстве имён `Aspose.Cells.Charts`.

В Aspose.Cells каждый добавляемый вами спарклайн создаётся с помощью `worksheet.SparklineGroups.Add(...)`, который возвращает объект `SparklineGroup`. Затем вы можете использовать этот объект, чтобы задать тип спарклайна, диапазон данных, целевую ячейку и визуальные свойства, такие как цвет линии, толщина линии, маркеры и индикаторы точек максимума/минимума.

{{% alert color="primary" %}}

Один объект `SparklineGroup` может содержать один или несколько спарклайнов, имеющих одинаковый стиль. Когда вы вызываете `Add` и передаёте строку данных плюс одну целевую ячейку, вы получаете один спарклайн внутри этой ячейки. Если ваш целевой диапазон шире одной ячейки, в каждой целевой ячейке рисуется отдельный спарклайн, при этом все они используют одинаковый стиль и диапазон данных.

{{% /alert %}}

В этой статье рассматривается каждый из трёх типов спарклайнов, поддерживаемых Aspose.Cells — **линейный**, **столбчатый** и **выигрышей/проигрышей** — и показывается, как их добавлять, настраивать их цвета и сохранять полученную рабочую книгу.

## **Линейные спарклайны**

Линейный спарклайн проводит непрерывную линию через точки данных в серии, что делает его наиболее естественным выбором для отображения тенденций во времени. В Aspose.Cells линейный спарклайн создаётся путём передачи `SparklineType.Line` методу `SparklineGroups.Add`.

Рабочий процесс аналогичен любому другому типу спарклайнов:

1. Создайте новую `Workbook` и получите доступ к первому рабочему листу.
2. Заполните строку исходных данных (например, строка 1, столбцы от A до E) значениями, которые вы хотите визуализировать.
3. Сформируйте `CellArea`, описывающую целевую ячейку, в которой будет нарисован спарклайн.
4. Вызовите `worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest)`. Третий аргумент — `false` — сообщает Aspose.Cells, что диапазон данных является горизонтальным (строка), а не вертикальным (столбец).
5. При необходимости настройте возвращённый `SparklineGroup`. Для линейного спарклайна вы можете задать цвет линии с помощью `group.Line.Color` (который ожидает `CellsColor` из `Aspose.Cells.Drawing`), настроить толщину линии и включить маркеры точек максимума/минимума.
6. Сохраните рабочую книгу.

В следующем примере создаётся рабочая книга, значения 5, -3, 8, -2, 6 записываются в ячейки от A1 до E1, а в ячейку F1 добавляется линейный спарклайн, отслеживающий эти значения. Также цвет линии настраивается на красный и включаются маркеры для точек максимума и минимума.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Шаг 1: Создаём книгу и получаем первый лист
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Шаг 2: Записываем примеры значений 5, -3, 8, -2, 6 в ячейки A1:E1
    cells.Get(u"A1").PutValue(5);
    cells.Get(u"B1").PutValue(-3);
    cells.Get(u"C1").PutValue(8);
    cells.Get(u"D1").PutValue(-2);
    cells.Get(u"E1").PutValue(6);

    // Шаг 3: Создаём CellArea, указывающую на ячейку назначения F1
    CellArea dest;
    dest.StartColumn = 5;   // столбец F (0-индексированный)
    dest.EndColumn = 5;
    dest.StartRow = 0;      // строка 1 (0-индексированная)
    dest.EndRow = 0;

    // Шаг 4: Добавляем линейный спарклайн из A1:E1 в F1
    int index = worksheet.GetSparklineGroups().Add(SparklineType::Line, u"A1:E1", false, dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(index);

    // Шаг 5: Создаём красный CellsColor и назначаем его цветом линии спарклайна
    CellsColor red = workbook.CreateCellsColor();
    red.SetColor(Color::Red());
    group.SetSeriesColor(red);

    // Шаг 6: Включаем маркеры верхних и нижних точек
    group.SetShowHighPoint(true);
    group.SetShowLowPoint(true);

    // Шаг 7: Сохраняем книгу
    workbook.Save(u"output_line.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Столбчатые спарклайны**

Столбчатый спарклайн отображает каждую точку данных в виде вертикальной полосы. Это делает его хорошо подходящим для данных, величина которых имеет значение — например, ежемесячные объёмы продаж или количественные показатели. В Aspose.Cells вы создаёте столбчатый спарклайн, передавая `SparklineType.Column` методу `SparklineGroups.Add`.

Процедура аналогична примеру с линейным спарклайном:

1. Создайте новую `Workbook` и получите доступ к первому рабочему листу.
2. Заполните тот же исходный диапазон (A1:E1) значениями, которые вы хотите визуализировать.
3. Сформируйте `CellArea`, описывающую целевую ячейку.
4. Вызовите `worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, dest)`.
5. При необходимости настройте полученный `SparklineGroup` — например, установив `group.Type` для подтверждения типа или скорректировав цвет полос.
6. Сохраните рабочую книгу в отдельный выходной файл, чтобы он не перезаписал пример с линейным спарклайном.

В примере ниже значения 5, -3, 8, -2, 6 записываются в A1:E1, и в F1 отрисовывается столбчатый спарклайн. Отрицательные значения изображаются в виде полос, направленных вниз, а положительные — в виде полос, направленных вверх, что позволяет легко различить положительный и отрицательный вклад.

```cpp
#include "Aspose.Cells.h"
#include <iostream>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Шаг 1: Создать Workbook и получить первый рабочий лист
    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);

    // Шаг 2: Записать примеры значений в A1:E1
    int values[5] = { 5, -3, 8, -2, 6 };
    Cells cells = worksheet.GetCells();
    for (int i = 0; i < 5; i++) {
        cells.Get(0, i).PutValue(values[i]);
    }

    // Шаг 3: Сформировать CellArea, указывающую на F1 (индекс столбца 5, индекс строки 0)
    CellArea dest;
    dest.StartColumn = 5;
    dest.EndColumn = 5;
    dest.StartRow = 0;
    dest.EndRow = 0;

    // Шаг 4: Добавить столбцовую спарклайн-диаграмму в целевую ячейку
    int idx = worksheet.GetSparklineGroups().Add(
        SparklineType::Column, u"A1:E1", false, dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(idx);

    // Шаг 5: Проверить тип спарклайн-диаграммы, прочитав group.Type
    std::cout << "Sparkline Type added: " << static_cast<int>(group.GetType()) << std::endl;

    // Шаг 6: Сохранить книгу
    wb.Save(u"output_column.xlsx");

    std::cout << "Workbook saved as output_column.xlsx" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Спарклайны выигрышей/проигрышей**

Спарклайн выигрышей/проигрышей — это особый вариант столбчатого спарклайна, предназначенный для отображения только двух исходов: положительное значение отображается как «верхняя» полоса (выигрыш), а нулевое или отрицательное значение — как «нижняя» полоса (проигрыш). Спарклайны выигрышей/проигрышей обычно используются для визуализации последовательностей побед и поражений, результатов «пройдено/не пройдено» или любого бинарного исхода во времени.

В Aspose.Cells спарклайн выигрышей/проигрышей создаётся путём передачи `SparklineType.Stacked` методу `SparklineGroups.Add`. (Несмотря на название, `SparklineType.Stacked` — это значение перечисления, используемое для запроса отрисовки выигрышей/проигрышей.)

Процедура такая же, как и для двух других типов:

1. Создайте новую `Workbook` и получите доступ к первому рабочему листу.
2. Заполните исходный диапазон. Поскольку спарклайны выигрышей/проигрышей трактуют каждое значение либо как выигрыш, либо как проигрыш, величина значения не имеет значения — важен только его знак. Положительные значения становятся верхними полосами, а неположительные — нижними.
3. Сформируйте `CellArea`, описывающую целевую ячейку.
4. Вызовите `worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, dest)`.
5. При необходимости настройте возвращённый `SparklineGroup`, например, задав акцентные цвета для полос выигрышей и проигрышей.
6. Сохраните рабочую книгу под уникальным именем файла, чтобы все три примера могли сосуществовать на диске.

В примере ниже используются те же входные данные, что и в двух предыдущих разделах. Значения 5, -3, 8, -2, 6 интерпретируются как выигрыш, проигрыш, выигрыш, проигрыш, выигрыш — и спарклайн, нарисованный в F1, точно отражает этот шаблон.

```cpp
#include "Aspose.Cells.h"
#include <iostream>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Шаг 1: Создаём Workbook и получаем первый лист
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"WinLoss");

    // Шаг 2: Заполняем пример данных в строке 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
    worksheet.GetCells().Get(u"A1").PutValue(5);
    worksheet.GetCells().Get(u"B1").PutValue(-3);
    worksheet.GetCells().Get(u"C1").PutValue(8);
    worksheet.GetCells().Get(u"D1").PutValue(-2);
    worksheet.GetCells().Get(u"E1").PutValue(6);

    // Шаг 3: Создаём CellArea, указывающий на F1 (столбец 5, строка 0)
    CellArea dest;
    dest.StartColumn = 5;   // F
    dest.EndColumn = 5;
    dest.StartRow = 0;      // строка 1
    dest.EndRow = 0;

    // Шаг 4: Добавляем спарклайн Win/Loss (SparklineType.Stacked)
    int groupIndex = worksheet.GetSparklineGroups().Add(
        SparklineType::Stacked,
        u"A1:E1",
        false,
        dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(groupIndex);

    // Шаг 5: Настраиваем группу спарклайнов
    // Включаем маркеры верхних и нижних точек
    group.SetShowHighPoint(true);
    group.SetShowLowPoint(true);
    group.SetShowNegativePoints(true);

    // Устанавливаем зелёный цвет для верхних точек
    CellsColor highColor = workbook.CreateCellsColor();
    highColor.SetColor(Color::Green());
    group.SetHighPointColor(highColor);

    // Устанавливаем красный цвет для нижних точек
    CellsColor lowColor = workbook.CreateCellsColor();
    lowColor.SetColor(Color::Red());
    group.SetLowPointColor(lowColor);

    // Устанавливаем оранжевый цвет для отрицательных точек
    CellsColor negColor = workbook.CreateCellsColor();
    negColor.SetColor(Color::Orange());
    group.SetNegativePointsColor(negColor);

    // Устанавливаем цвет серии по умолчанию (используется для положительных столбцов)
    CellsColor seriesColor = workbook.CreateCellsColor();
    seriesColor.SetColor(Color::SteelBlue());
    group.SetSeriesColor(seriesColor);

    // Шаг 6: Сохраняем книгу
    workbook.Save(u"output_winloss.xlsx");

    std::cout << "Книга успешно сохранена: output_winloss.xlsx" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Объединение всех трёх типов спарклайнов**

Каждый из трёх предыдущих примеров создаёт собственную рабочую книгу, чтобы выходные файлы было удобно просматривать изолированно. Однако в реальном сценарии часто требуется сравнить несколько серий данных бок о бок. Самый простой способ сделать это — поместить более одной группы спарклайнов в один и тот же рабочий лист, при этом каждая группа будет отображать свой стиль.

Вы можете добавить несколько объектов `SparklineGroup` в одну и ту же `SparklineGroupCollection`, и каждая группа может указывать на разную целевую ячейку или разный диапазон. Например, вы можете разместить линейный спарклайн в F1, столбчатый спарклайн в F2 и спарклайн выигрышей/проигрышей в F3 — все они будут считывать данные из одного и того же источника в строке 1 — чтобы читатель мог увидеть три различных визуальных представления одних и тех же чисел.

В комбинированном примере ниже создаётся одна рабочая книга, строка 1 заполняется значениями 5, -3, 8, -2, 6, после чего в ячейки F1, F2 и F3 добавляются три группы спарклайнов — по одной каждого типа — так что полученный файл демонстрирует все три стиля спарклайнов одновременно.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Шаг 1: Создайте рабочую книгу и получите первый рабочий лист
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Шаг 2: Заполните образцы данных в строке 1 (A1:E1)
    worksheet.GetCells().Get(u"A1").PutValue(5);
    worksheet.GetCells().Get(u"B1").PutValue(-3);
    worksheet.GetCells().Get(u"C1").PutValue(8);
    worksheet.GetCells().Get(u"D1").PutValue(-2);
    worksheet.GetCells().Get(u"E1").PutValue(6);

    // Шаг 3: Добавьте группу линейных спарклайнов в F1
    CellArea lineArea;
    lineArea.StartColumn = 5;
    lineArea.EndColumn = 5;
    lineArea.StartRow = 0;
    lineArea.EndRow = 0;
    int lineIdx = worksheet.GetSparklineGroups().Add(SparklineType::Line, u"A1:E1", false, lineArea);
    SparklineGroup lineGroup = worksheet.GetSparklineGroups().Get(lineIdx);

    // Настройте цвет линейного спарклайна через CellsColor
    CellsColor lineColor = workbook.CreateCellsColor();
    lineColor.SetColor(Color::Blue());
    lineGroup.SetSeriesColor(lineColor);

    // Шаг 4: Добавьте группу столбчатых спарклайнов в F2
    CellArea columnArea;
    columnArea.StartColumn = 5;
    columnArea.EndColumn = 5;
    columnArea.StartRow = 1;
    columnArea.EndRow = 1;
    int columnIdx = worksheet.GetSparklineGroups().Add(SparklineType::Column, u"A1:E1", false, columnArea);
    SparklineGroup columnGroup = worksheet.GetSparklineGroups().Get(columnIdx);

    // Настройте цвет серии столбчатого спарклайна
    CellsColor columnColor = workbook.CreateCellsColor();
    columnColor.SetColor(Color::Green());
    columnGroup.SetSeriesColor(columnColor);

    // Шаг 5: Добавьте группу спарклайнов Выигрыш/Проигрыш (Составной) в F3
    CellArea stackedArea;
    stackedArea.StartColumn = 5;
    stackedArea.EndColumn = 5;
    stackedArea.StartRow = 2;
    stackedArea.EndRow = 2;
    int stackedIdx = worksheet.GetSparklineGroups().Add(SparklineType::Stacked, u"A1:E1", false, stackedArea);
    SparklineGroup stackedGroup = worksheet.GetSparklineGroups().Get(stackedIdx);

    // Настройте цвет серии спарклайна Выигрыш/Проигрыш
    CellsColor stackedColor = workbook.CreateCellsColor();
    stackedColor.SetColor(Color::FromArgb(0xFF8C00));
    stackedGroup.SetSeriesColor(stackedColor);

    // Шаг 6: Сохраните рабочую книгу
    workbook.Save(u"output_all.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

Когда вы объединяете несколько групп спарклайнов на одном рабочем листе, каждая группа является независимой. Они могут использовать общий исходный диапазон или разные исходные диапазоны, и их можно оформлять независимо. Это позволяет легко создать небольшую «панель мониторинга» внутриклеточных визуализаций прямо внутри существующего рабочего листа.

{{% /alert %}}

## **Настройка внешнего вида спарклайнов**

После того как `SparklineGroup` создан и добавлен в `worksheet.SparklineGroups`, вы можете прочитать или изменить несколько его визуальных свойств перед сохранением рабочей книги. Наиболее часто настраиваемые свойства:

- **`group.Type`** — `SparklineType` (Line, Column или Stacked). Оно задаётся при добавлении группы, но вы можете прочитать его обратно для подтверждения.
- **`group.Line.Color`** — цвет линии, выраженный как `CellsColor`, созданный с помощью `workbook.CreateCellsColor()`. Это свойство используется для цвета обводки линейного спарклайна.
- **`group.Line.Weight`** — толщина линии в пунктах. Более высокие значения дают более толстые линии.
- **Маркеры точек максимума/минимума** — флаги, которые включают небольшие маркеры на самых высоких и самых низких точках данных, что полезно для выделения экстремумов.
- **Маркеры первой/последней/отрицательной точек** — флаги, которые переключают маркеры на первой, последней и отрицательной точках данных.

Чтобы изменить цвет, всегда создавайте экземпляр `CellsColor` и присваивайте его соответствующему свойству. Не присваивайте необработанное значение цвета напрямую свойствам цвета спарклайна — они ожидают тип `CellsColor` из `Aspose.Cells.Drawing`. Сам метод `SparklineGroups.Add` возвращает полностью типизированный объект `SparklineGroup`, поэтому вы можете связывать присвоения свойств с возвращаемым значением или сохранить его в локальной переменной и настроить перед сохранением.



{{< app/cells/assistant language="cpp" >}}
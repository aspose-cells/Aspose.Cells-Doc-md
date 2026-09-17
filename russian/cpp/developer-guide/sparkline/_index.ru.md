---
title: Спарклайны в Aspose.Cells for C++
linktitle: Спарклайны в Aspose.Cells for C++
description: Aspose.Cells — это библиотека C++ для работы с файлами электронных таблиц, которая поддерживает создание спарклайнов — миниатюрных диаграмм, размещаемых внутри ячеек рабочего листа. В этой статье объясняется, как добавлять и настраивать линейные, столбцовые спарклайны и спарклайны победа/поражение с помощью библиотеки Aspose.Cells.
keywords: Aspose.Cells, библиотека C++, электронная таблица, спарклайны, линейный спарклайн, столбцовый спарклайн, спарклайн победа/поражение, SparklineGroup, SparklineType
type: docs
weight: 195
url: /ru/cpp/creating-sparklines/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells поддерживает создание спарклайнов внутри ячеек рабочего листа. Спарклайны — это миниатюрные диаграммы, которые помещаются в одну ячейку и обеспечивают быструю визуальную репрезентацию тенденций данных. Aspose.Cells поддерживает линейные, столбцовые спарклайны и спарклайны победа/поражение, каждый из которых можно настроить по цвету, толщине линии, точкам максимума/минимума и маркерам.

## **Введение**
Спарклайны — это крошечные внутриклеточные диаграммы, которые полезны, когда нужно отобразить быструю тенденцию рядом со строкой или столбцом данных, не занимая пространство полноценной диаграммы. Excel поддерживает три типа спарклайнов: **линейные**, **столбцовые** и **победа/поражение**. Aspose.Cells воспроизводит эту возможность через API `SparklineGroup` и `SparklineGroupCollection`, расположенные в пространстве имён `Aspose.Cells.Charts`.
В Aspose.Cells каждый добавляемый вами спарклайн создаётся через `worksheet.SparklineGroups.Add(...)`, который возвращает объект `SparklineGroup`. Затем вы можете использовать этот объект для задания типа спарклайна, диапазона данных, целевой ячейки и визуальных свойств, таких как цвет линии, толщина линии, маркеры и индикаторы точек максимума/минимума.
В этой статье рассматривается каждый из трёх типов спарклайнов, поддерживаемых Aspose.Cells — **Line**, **Column** и **Win/Loss** — и показано, как их добавлять, настраивать их цвета и сохранять полученную рабочую книгу.

## **Линейные спарклайны**
Линейный спарклайн рисует непрерывную линию через точки данных в ряду, что делает его наиболее естественным выбором для отображения тенденций во времени. В Aspose.Cells линейный спарклайн создаётся путём передачи `SparklineType.Line` в метод `SparklineGroups.Add`.
1. Создайте новую `Workbook` и откройте первый рабочий лист.
2. Заполните строку исходных данных (например, строка 1, столбцы от A до E) значениями, которые вы хотите визуализировать.
3. Создайте `CellArea`, описывающую целевую ячейку, в которой будет нарисован спарклайн.
4. Вызовите `worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest)`. Третий аргумент — `false` — сообщает Aspose.Cells, что диапазон данных является горизонтальным (строка), а не вертикальным (столбец).
5. При необходимости настройте возвращённый `SparklineGroup`. Для линейного спарклайна можно задать цвет линии с помощью `group.Line.Color` (который ожидает `CellsColor` из `Aspose.Cells.Drawing`), отрегулировать толщину линии и включить маркеры точек максимума/минимума.
6. Сохраните рабочую книгу.
Следующий пример создаёт рабочую книгу, записывает значения 5, -3, 8, -2, 6 в ячейки от A1 до E1 и добавляет линейный спарклайн в ячейку F1, который отслеживает эти значения. Также настраивается красный цвет линии и включаются маркеры для точек максимума и минимума.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // Шаг 1: Создаём книгу и получаем первый рабочий лист
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    // Шаг 2: Записываем примеры значений 5, -3, 8, -2, 6 в ячейки A1:E1
    cells.Get(u"A1").PutValue(5);
    cells.Get(u"B1").PutValue(-3);
    cells.Get(u"C1").PutValue(8);
    cells.Get(u"D1").PutValue(-2);
    cells.Get(u"E1").PutValue(6);
    // Шаг 3: Создаём CellArea, указывающий на целевую ячейку F1
    CellArea dest;
    dest.StartColumn = 5;   // столбец F (с нулевым индексом)
    dest.EndColumn = 5;
    dest.StartRow = 0;      // строка 1 (с нулевым индексом)
    dest.EndRow = 0;
    // Шаг 4: Добавляем линейную спарклайн-диаграмму из A1:E1 в F1
    int index = worksheet.GetSparklineGroups().Add(SparklineType::Line, u"A1:E1", false, dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(index);
    // Шаг 5: Создаём красный CellsColor и назначаем его цветом линии спарклайна
    CellsColor red = workbook.CreateCellsColor();
    red.SetColor(Color::Red());
    group.SetSeriesColor(red);
    // Шаг 6: Включаем маркеры максимальных и минимальных точек
    group.SetShowHighPoint(true);
    group.SetShowLowPoint(true);
    // Шаг 7: Сохраняем книгу
    workbook.Save(u"output_line.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Столбцовые спарклайны**
Столбцовый спарклайн отображает каждую точку данных в виде вертикальной полосы. Это делает его хорошо подходящим для данных, величина которых имеет значение — например, ежемесячные объёмы продаж или подсчёты. В Aspose.Cells столбцовый спарклайн создаётся путём передачи `SparklineType.Column` в метод `SparklineGroups.Add`.
Процедура зеркально отражает пример с линейным спарклайном:
1. Создайте новую `Workbook` и откройте первый рабочий лист.
2. Заполните строку исходных данных значениями, которые вы хотите визуализировать.
3. Создайте `CellArea`, описывающую целевую ячейку.
4. Вызовите `worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, dest)`.
5. При необходимости настройте полученный `SparklineGroup` — например, задав `group.Type` для подтверждения типа или изменив цвет полос.
6. Сохраните рабочую книгу в отдельный выходной файл, чтобы не перезаписать пример с линейным спарклайном.
Пример ниже записывает значения 5, -3, 8, -2, 6 в A1:E1 и отображает столбцовый спарклайн в F1. Отрицательные значения отображаются в виде полос, направленных вниз, а положительные — в виде полос, направленных вверх, что позволяет легко обнаружить положительный и отрицательный вклад одним взглядом.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // Шаг 1: Создать рабочую книгу и получить первый рабочий лист
    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);
    // Шаг 2: Записать примеры значений в A1:E1
    int values[5] = { 5, -3, 8, -2, 6 };
    Cells cells = worksheet.GetCells();
    for (int i = 0; i < 5; i++) {
        cells.Get(0, i).PutValue(values[i]);
    }
    // Шаг 3: Создать CellArea, указывающую на F1 (индекс столбца 5, индекс строки 0)
    CellArea dest;
    dest.StartColumn = 5;
    dest.EndColumn = 5;
    dest.StartRow = 0;
    dest.EndRow = 0;
    // Шаг 4: Добавить спарклайн-столбец в целевую ячейку
    int idx = worksheet.GetSparklineGroups().Add(
        SparklineType::Column, u"A1:E1", false, dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(idx);
    // Шаг 5: Подтвердить тип спарклайна, прочитав group.Type
    std::cout << "Sparkline Type added: " << static_cast<int>(group.GetType()) << std::endl;
    // Шаг 6: Сохранить рабочую книгу
    wb.Save(u"output_column.xlsx");
    std::cout << "Workbook saved as output_column.xlsx" << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Спарклайны победа/поражение**
Спарклайн победа/поражение — это особый вариант столбцового спарклайна, предназначенный для отображения только двух исходов: положительное значение отображается в виде полосы «вверх» (победа), а нулевое или отрицательное значение — в виде полосы «вниз» (поражение). Спарклайны победа/поражение обычно используются для визуализации последовательностей побед и поражений, результатов «прошёл/не прошёл» или любого бинарного исхода во времени.
В Aspose.Cells спарклайн победа/поражение создаётся путём передачи `SparklineType.Stacked` в метод `SparklineGroups.Add`. (Несмотря на название, `SparklineType.Stacked` — это значение перечисления, используемое для запроса отрисовки победа/поражение.)
1. Создайте новую `Workbook` и откройте первый рабочий лист.
2. Заполните диапазон источника. Поскольку спарклайны победа/поражение рассматривают каждое значение либо как победу, либо как поражение, величина значения не имеет значения — имеет значение только его знак. Положительные значения становятся полосами «вверх», а неположительные — полосами «вниз».
3. Создайте `CellArea`, описывающую целевую ячейку.
4. Вызовите `worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, dest)`.
5. При необходимости настройте возвращённый `SparklineGroup`, например задав акцентные цвета для полос победы и поражения.
6. Сохраните рабочую книгу под отдельным именем файла, чтобы все три примера могли сосуществовать на диске.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // Шаг 1: Создаём Workbook и получаем первый рабочий лист
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"WinLoss");
    // Шаг 2: Заполняем примеры данных в строке 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
    worksheet.GetCells().Get(u"A1").PutValue(5);
    worksheet.GetCells().Get(u"B1").PutValue(-3);
    worksheet.GetCells().Get(u"C1").PutValue(8);
    worksheet.GetCells().Get(u"D1").PutValue(-2);
    worksheet.GetCells().Get(u"E1").PutValue(6);
    // Шаг 3: Формируем CellArea, указывающую на F1 (столбец 5, строка 0)
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
    // Включаем маркеры для максимальных и минимальных точек
    group.SetShowHighPoint(true);
    group.SetShowLowPoint(true);
    group.SetShowNegativePoints(true);
    // Задаём зелёный цвет для максимальных точек
    CellsColor highColor = workbook.CreateCellsColor();
    highColor.SetColor(Color::Green());
    group.SetHighPointColor(highColor);
    // Задаём красный цвет для минимальных точек
    CellsColor lowColor = workbook.CreateCellsColor();
    lowColor.SetColor(Color::Red());
    group.SetLowPointColor(lowColor);
    // Задаём оранжевый цвет для отрицательных точек
    CellsColor negColor = workbook.CreateCellsColor();
    negColor.SetColor(Color::Orange());
    group.SetNegativePointsColor(negColor);
    // Задаём цвет серии по умолчанию (используется для положительных значений)
    CellsColor seriesColor = workbook.CreateCellsColor();
    seriesColor.SetColor(Color::SteelBlue());
    group.SetSeriesColor(seriesColor);
    // Шаг 6: Сохраняем книгу
    workbook.Save(u"output_winloss.xlsx");
    std::cout << "Workbook saved successfully: output_winloss.xlsx" << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Объединение всех трёх типов спарклайнов**
Комбинированный пример ниже создаёт одну рабочую книгу, заполняет строку 1 значениями 5, -3, 8, -2, 6, а затем добавляет три группы спарклайнов в ячейки F1, F2 и F3 — по одной каждого типа — так что результирующий файл демонстрирует все три стиля спарклайнов одновременно.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // Шаг 1: Создать рабочую книгу и получить первый лист
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    // Шаг 2: Заполнить пример данных в строке 1 (A1:E1)
    worksheet.GetCells().Get(u"A1").PutValue(5);
    worksheet.GetCells().Get(u"B1").PutValue(-3);
    worksheet.GetCells().Get(u"C1").PutValue(8);
    worksheet.GetCells().Get(u"D1").PutValue(-2);
    worksheet.GetCells().Get(u"E1").PutValue(6);
    // Шаг 3: Добавить группу спарклайнов "Линия" в F1
    CellArea lineArea;
    lineArea.StartColumn = 5;
    lineArea.EndColumn = 5;
    lineArea.StartRow = 0;
    lineArea.EndRow = 0;
    int lineIdx = worksheet.GetSparklineGroups().Add(SparklineType::Line, u"A1:E1", false, lineArea);
    SparklineGroup lineGroup = worksheet.GetSparklineGroups().Get(lineIdx);
    // Настроить цвет спарклайна "Линия" через CellsColor
    CellsColor lineColor = workbook.CreateCellsColor();
    lineColor.SetColor(Color::Blue());
    lineGroup.SetSeriesColor(lineColor);
    // Шаг 4: Добавить группу спарклайнов "Столбец" в F2
    CellArea columnArea;
    columnArea.StartColumn = 5;
    columnArea.EndColumn = 5;
    columnArea.StartRow = 1;
    columnArea.EndRow = 1;
    int columnIdx = worksheet.GetSparklineGroups().Add(SparklineType::Column, u"A1:E1", false, columnArea);
    SparklineGroup columnGroup = worksheet.GetSparklineGroups().Get(columnIdx);
    // Настроить цвет серии спарклайнов "Столбец"
    CellsColor columnColor = workbook.CreateCellsColor();
    columnColor.SetColor(Color::Green());
    columnGroup.SetSeriesColor(columnColor);
    // Шаг 5: Добавить группу спарклайнов "Победа/Проигрыш" (С накоплением) в F3
    CellArea stackedArea;
    stackedArea.StartColumn = 5;
    stackedArea.EndColumn = 5;
    stackedArea.StartRow = 2;
    stackedArea.EndRow = 2;
    int stackedIdx = worksheet.GetSparklineGroups().Add(SparklineType::Stacked, u"A1:E1", false, stackedArea);
    SparklineGroup stackedGroup = worksheet.GetSparklineGroups().Get(stackedIdx);
    // Настроить цвет серии спарклайнов "Победа/Проигрыш"
    CellsColor stackedColor = workbook.CreateCellsColor();
    stackedColor.SetColor(Color::FromArgb(0xFF8C00));
    stackedGroup.SetSeriesColor(stackedColor);
    // Шаг 6: Сохранить рабочую книгу
    workbook.Save(u"output_all.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Настройка внешнего вида спарклайна**
После того как `SparklineGroup` создан и добавлен в `worksheet.SparklineGroups`, вы можете прочитать или изменить несколько его визуальных свойств перед сохранением рабочей книги. Наиболее часто настраиваемыми свойствами являются:
- **`group.Type`** — `SparklineType` (Line, Column или Stacked). Оно задаётся при добавлении группы, но вы можете прочитать его обратно для подтверждения.
- **`group.Line.Color`** — цвет линии, выраженный как `CellsColor`, созданный через `workbook.CreateCellsColor()`. Это свойство используется для задания цвета обводки линейного спарклайна.
- **`group.Line.Weight`** — толщина линии в пунктах. Большие значения дают более толстые линии.
- **Маркеры точек максимума/минимума** — флаги, которые включают маленькие маркеры на самой высокой и самой низкой точках данных, что полезно для выделения экстремумов.
- **Маркеры первой/последней/отрицательной точек** — флаги, которые переключают маркеры на первой, последней и отрицательной точках данных.
Чтобы изменить цвет, всегда создавайте экземпляр `CellsColor` и присваивайте его соответствующему свойству. Не присваивайте необработанное значение цвета напрямую свойствам цвета спарклайна — они ожидают тип `CellsColor` из `Aspose.Cells.Drawing`. Сам метод `SparklineGroups.Add` возвращает полностью типизированный объект `SparklineGroup`, поэтому вы можете связывать присваивания свойств с возвращаемым значением или сохранить его в локальной переменной и настроить перед сохранением.
{{% /alert %}}

{{< app/cells/assistant language="cpp" >}}
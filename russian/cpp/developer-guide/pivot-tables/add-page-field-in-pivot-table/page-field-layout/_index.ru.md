---
title: Изменение макета поля страницы в сводной таблице
linktitle: Изменение макета поля страницы в сводной таблице
description: Узнайте, как управлять макетом области полей страницы в сводной таблице с помощью Aspose.Cells for C++, включая настройку порядка отображения, количества переносов и порядка полей страницы в верхней части сводной таблицы.
keywords: Aspose.Cells, библиотека C++, электронная таблица, сводная таблица, поле страницы, порядок полей страницы, количество переносов полей страницы, перемещение поля страницы
type: docs
weight: 191
url: /ru/cpp/change-page-field-layout/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
Эта статья является продолжением темы **Добавление поля страницы в сводную таблицу**. В ней демонстрируется, как управлять макетом области полей страницы — полосы элементов управления фильтрацией в верхней части сводной таблицы — включая порядок отображения, количество переносов и изменение порядка полей.
{{% /alert %}}
## **Введение**
Сводная таблица в Microsoft Excel содержит выделенную **область полей страницы**, расположенную над областью строк, столбцов и данных таблицы. Эта область отображается в виде полосы раскрывающихся элементов управления фильтрацией (по одному на каждое поле страницы), на которые пользователи нажимают, чтобы разделить данные сводной таблицы по таким критериям, как год или регион. Aspose.Cells for C++ моделирует эту область через коллекцию `PivotTable.PageFields` и предоставляет три свойства, управляющих визуальным расположением полосы:
- `PivotTable.PageFieldOrder` (значение `Aspose.Cells.PrintOrderType`) определяет, размещаются ли дополнительные поля страницы *рядом* с существующими или *под* ними.
- `PivotTable.PageFieldWrapCount` задаёт, сколько полей страницы размещается в одной строке или столбце до переноса.
- `PivotTable.PageFields.Move(currIndex, destIndex)` изменяет порядок полей страницы без изменения режима упорядочивания.
В этой статье последовательно рассматриваются три примера кода, демонстрирующие каждую из этих операций на общем наборе данных, чтобы можно было сравнить полученные макеты.
## **Исходные данные**
Во всех трёх примерах ниже эти восемь строк данных о продажах загружаются на рабочий лист с именем `PivotData`. Данные содержат два кандидата на поля страницы (`Year`, `Region`), одного кандидата на поле строки (`Fruit`) и один показатель (`Amount`), что делает осмысленным изучение полосы полей страницы.
| Fruit  | Year | Region | Amount |
|--------|------|--------|--------|
| Apple  | 2022 | North  | 150    |
| Apple  | 2023 | North  | 180    |
| Banana | 2022 | South  | 120    |
| Banana | 2023 | South  | 140    |
| Cherry | 2022 | East   | 200    |
| Cherry | 2023 | East   | 220    |
| Grape  | 2022 | West   | 90     |
| Grape  | 2023 | West   | 110    |
Все восемь строк заполняются в каждом примере кода в одинаковом порядке, поэтому исходные данные никогда не различаются между сценариями — различаются только свойства макета поля страницы.
## **Пример 1: Сначала по горизонтали, затем вниз**
В первом сценарии мы настраиваем два поля страницы (`Year`, `Region`) так, чтобы они отображались **бок о бок в одной строке** в верхней части сводной таблицы. Мы назначаем `Fruit` оси строк, размещаем `Year` первым и `Region` вторым на оси страниц (порядок вызовов `AddFieldToArea` определяет начальный индекс), добавляем `Amount` (Sum) как поле данных, а затем устанавливаем `PageFieldOrder` равным `PrintOrderType.OverThenDown` с `PageFieldWrapCount = 2`. При `OverThenDown` и количестве переносов, равном 2, два поля страницы располагаются горизонтально бок о бок в одной строке в верхней части сводной таблицы, поэтому полоса занимает одну строку шириной в два элемента.
```cpp
#include "Aspose.Cells.h"
#include <string>
#include <filesystem>

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    std::string dataDir = "output";
    if (!std::filesystem::exists(dataDir)) {
        std::filesystem::create_directories(dataDir);
    }

    Workbook workbook;
    WorksheetCollection worksheets = workbook.GetWorksheets();

    Worksheet pivotDataSheet = worksheets.Add(u"PivotData");
    Cells pivotDataCells = pivotDataSheet.GetCells();

    // Заголовки (строка 0)
    pivotDataCells.Get(0, 0).PutValue(u"Fruit");
    pivotDataCells.Get(0, 1).PutValue(u"Year");
    pivotDataCells.Get(0, 2).PutValue(u"Region");
    pivotDataCells.Get(0, 3).PutValue(u"Amount");

    // Строка 1: Apple, 2022, North, 150
    pivotDataCells.Get(1, 0).PutValue(u"Apple");
    pivotDataCells.Get(1, 1).PutValue(2022);
    pivotDataCells.Get(1, 2).PutValue(u"North");
    pivotDataCells.Get(1, 3).PutValue(150);

    // Строка 2: Apple, 2023, North, 180
    pivotDataCells.Get(2, 0).PutValue(u"Apple");
    pivotDataCells.Get(2, 1).PutValue(2023);
    pivotDataCells.Get(2, 2).PutValue(u"North");
    pivotDataCells.Get(2, 3).PutValue(180);

    // Строка 3: Banana, 2022, South, 120
    pivotDataCells.Get(3, 0).PutValue(u"Banana");
    pivotDataCells.Get(3, 1).PutValue(2022);
    pivotDataCells.Get(3, 2).PutValue(u"South");
    pivotDataCells.Get(3, 3).PutValue(120);

    // Строка 4: Banana, 2023, South, 140
    pivotDataCells.Get(4, 0).PutValue(u"Banana");
    pivotDataCells.Get(4, 1).PutValue(2023);
    pivotDataCells.Get(4, 2).PutValue(u"South");
    pivotDataCells.Get(4, 3).PutValue(140);

    // Строка 5: Cherry, 2022, East, 200
    pivotDataCells.Get(5, 0).PutValue(u"Cherry");
    pivotDataCells.Get(5, 1).PutValue(2022);
    pivotDataCells.Get(5, 2).PutValue(u"East");
    pivotDataCells.Get(5, 3).PutValue(200);

    // Строка 6: Cherry, 2023, East, 220
    pivotDataCells.Get(6, 0).PutValue(u"Cherry");
    pivotDataCells.Get(6, 1).PutValue(2023);
    pivotDataCells.Get(6, 2).PutValue(u"East");
    pivotDataCells.Get(6, 3).PutValue(220);

    // Строка 7: Grape, 2022, West, 90
    pivotDataCells.Get(7, 0).PutValue(u"Grape");
    pivotDataCells.Get(7, 1).PutValue(2022);
    pivotDataCells.Get(7, 2).PutValue(u"West");
    pivotDataCells.Get(7, 3).PutValue(90);

    // Строка 8: Grape, 2023, West, 110
    pivotDataCells.Get(8, 0).PutValue(u"Grape");
    pivotDataCells.Get(8, 1).PutValue(2023);
    pivotDataCells.Get(8, 2).PutValue(u"West");
    pivotDataCells.Get(8, 3).PutValue(110);

    // Добавить лист PivotTableReport
    Worksheet pivotTableSheet = worksheets.Add(u"PivotTableReport");
    PivotTableCollection pivotTables = pivotTableSheet.GetPivotTables();

    // Создать сводную таблицу на основе PivotData!A1:D9, размещённую в A1 на PivotTableReport
    int pivotIndex = pivotTables.Add(u"PivotData!A1:D9", u"A1", u"PivotTable1");
    PivotTable pivotTable = pivotTables.Get(pivotIndex);

    // Добавить поля
    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);   // Fruit
    pivotTable.AddFieldToArea(PivotFieldType::Page, 1);  // Year
    pivotTable.AddFieldToArea(PivotFieldType::Page, 2);  // Region
    pivotTable.AddFieldToArea(PivotFieldType::Data, 3);  // Amount
    pivotTable.GetDataFields().Get(0).SetFunction(ConsolidationFunction::Sum);

    // Настроить макет области полей страницы: сначала по горизонтали, перенос после каждых 2
    pivotTable.SetPageFieldOrder(PrintOrderType::OverThenDown);
    pivotTable.SetPageFieldWrapCount(2);

    // Обновить и вычислить
    pivotTable.CalculateData();

    // Сохранить
    std::string filePath = dataDir + "/pageFieldLayout_overThenDown.xlsx";
    workbook.Save(U16String(filePath.c_str()));

    Aspose::Cells::Cleanup();
    return 0;
}
```
## **Пример 2: Сначала вниз, затем по горизонтали**
В этом примере мы размещаем `Fruit` на оси строк, `Year` и `Region` на оси страниц (`Year` первым), а `Amount` (Sum) как поле данных — точно так же, как в примере 1. Затем устанавливаем `PageFieldOrder` равным `PrintOrderType.DownThenOver`, а `PageFieldWrapCount` равным `2`. При `DownThenOver` и количестве переносов, равном 2, два поля страницы располагаются вертикально — `Year` сверху, `Region` непосредственно под ним — образуя один столбец в верхней части сводной таблицы. Таким образом, полоса занимает две строки шириной в один элемент, в отличие от примера 1.
```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet pivotData = workbook.GetWorksheets().Get(0);
    pivotData.SetName(u"PivotData");
    Worksheet pivotReport = workbook.GetWorksheets().Add(u"PivotTableReport");

    const char* headers[] = { "Fruit", "Year", "Region", "Amount" };
    for (int c = 0; c < 4; c++)
    {
        pivotData.GetCells().Get(0, c).PutValue(U16String(headers[c]));
    }

    struct DataRow {
        U16String fruit;
        int year;
        U16String region;
        int amount;
    };

    DataRow data[] = {
        {U16String("Apple"),  2022, U16String("North"), 150},
        {U16String("Apple"),  2023, U16String("North"), 180},
        {U16String("Banana"), 2022, U16String("South"), 120},
        {U16String("Banana"), 2023, U16String("South"), 140},
        {U16String("Cherry"), 2022, U16String("East"),  200},
        {U16String("Cherry"), 2023, U16String("East"),  220},
        {U16String("Grape"),  2022, U16String("West"),  90},
        {U16String("Grape"),  2023, U16String("West"),  110}
    };

    for (int r = 0; r < 8; r++)
    {
        pivotData.GetCells().Get(r + 1, 0).PutValue(data[r].fruit);
        pivotData.GetCells().Get(r + 1, 1).PutValue(data[r].year);
        pivotData.GetCells().Get(r + 1, 2).PutValue(data[r].region);
        pivotData.GetCells().Get(r + 1, 3).PutValue(data[r].amount);
    }

    int idx = pivotReport.GetPivotTables().Add(u"PivotData!A1:D9", u"A1", u"PivotTable");
    PivotTable pivotTable = pivotReport.GetPivotTables().Get(idx);

    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);
    pivotTable.AddFieldToArea(PivotFieldType::Page, 1);
    pivotTable.AddFieldToArea(PivotFieldType::Page, 2);
    pivotTable.AddFieldToArea(PivotFieldType::Data, 3);

    pivotTable.SetPageFieldOrder(PrintOrderType::DownThenOver);
    pivotTable.SetPageFieldWrapCount(2);

    pivotTable.CalculateData();

    workbook.Save(u"pageFieldLayout_downThenOver.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
## **Пример 3: Перемещение поля страницы**
В третьем сценарии мы сохраняем этот набор данных и распределение полей, задаём нейтральный макет (`OverThenDown` с количеством переносов `2`) и демонстрируем операцию `PageFields.Move`. Вызов `Move(0, 1)` перемещает поле страницы с индексом 0 (`Year`) на позицию 1, а поле страницы, которое было на позиции 1 (`Region`), сдвигается на позицию 0. После этого вызова `Region` становится первым полем страницы, а `Year` — вторым. Режим переноса и упорядочивания остаются неизменными, поэтому полоса по-прежнему отображается горизонтально бок о бок — изменился только порядок двух раскрывающихся списков.
```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    Workbook wb;

    Worksheet dataSheet = wb.GetWorksheets().Get(0);
    dataSheet.SetName(u"PivotData");

    Cells dataCells = dataSheet.GetCells();

    dataCells.Get(u"A1").PutValue(u"Fruit");
    dataCells.Get(u"B1").PutValue(u"Year");
    dataCells.Get(u"C1").PutValue(u"Region");
    dataCells.Get(u"D1").PutValue(u"Amount");

    dataCells.Get(u"A2").PutValue(u"Apple");
    dataCells.Get(u"B2").PutValue(2022);
    dataCells.Get(u"C2").PutValue(u"North");
    dataCells.Get(u"D2").PutValue(150);

    dataCells.Get(u"A3").PutValue(u"Apple");
    dataCells.Get(u"B3").PutValue(2023);
    dataCells.Get(u"C3").PutValue(u"North");
    dataCells.Get(u"D3").PutValue(180);

    dataCells.Get(u"A4").PutValue(u"Banana");
    dataCells.Get(u"B4").PutValue(2022);
    dataCells.Get(u"C4").PutValue(u"South");
    dataCells.Get(u"D4").PutValue(120);

    dataCells.Get(u"A5").PutValue(u"Banana");
    dataCells.Get(u"B5").PutValue(2023);
    dataCells.Get(u"C5").PutValue(u"South");
    dataCells.Get(u"D5").PutValue(140);

    dataCells.Get(u"A6").PutValue(u"Cherry");
    dataCells.Get(u"B6").PutValue(2022);
    dataCells.Get(u"C6").PutValue(u"East");
    dataCells.Get(u"D6").PutValue(200);

    dataCells.Get(u"A7").PutValue(u"Cherry");
    dataCells.Get(u"B7").PutValue(2023);
    dataCells.Get(u"C7").PutValue(u"East");
    dataCells.Get(u"D7").PutValue(220);

    dataCells.Get(u"A8").PutValue(u"Grape");
    dataCells.Get(u"B8").PutValue(2022);
    dataCells.Get(u"C8").PutValue(u"West");
    dataCells.Get(u"D8").PutValue(90);

    dataCells.Get(u"A9").PutValue(u"Grape");
    dataCells.Get(u"B9").PutValue(2023);
    dataCells.Get(u"C9").PutValue(u"West");
    dataCells.Get(u"D9").PutValue(110);

    Worksheet pivotSheet = wb.GetWorksheets().Add(u"PivotTableReport");

    int32_t pivotIndex = pivotSheet.GetPivotTables().Add(u"PivotData!A1:D9", u"A3", u"PivotTable");
    PivotTable pivotTable = pivotSheet.GetPivotTables().Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);
    pivotTable.AddFieldToArea(PivotFieldType::Page, 1);
    pivotTable.AddFieldToArea(PivotFieldType::Page, 2);
    pivotTable.AddFieldToArea(PivotFieldType::Data, 3);

    pivotTable.SetPageFieldOrder(PrintOrderType::OverThenDown);
    pivotTable.SetPageFieldWrapCount(2);

    pivotTable.GetPageFields().Move(0, 1);

    pivotTable.CalculateData();

    wb.Save(u"pageFieldLayout_move.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
## **Связанные статьи**
- [Добавление поля страницы в сводную таблицу](/cells/ru/cpp/add-page-field-in-pivot-table/) — родительская страница, рассказывающая о добавлении полей страницы в сводную таблицу.
- [Поля строк и столбцов в сводной таблице](/cells/ru/cpp/row-and-column-fields/) — описывает распределение полей по осям строк и столбцов, дополняя работу с осью страниц, показанную здесь.
- [Управление полями значений в сводной таблице](/cells/ru/cpp/manage-value-fields/) — описывает настройку области данных (значений), включая агрегацию `Sum`, используемую в данной статье.
- [Обновление сводной таблицы](/cells/ru/cpp/refresh-pivot-table/) — поясняет `RefreshData` и `CalculateData`, которые требуются после изменения порядка полей страницы.
- [Применение стиля к сводной таблице](/cells/ru/cpp/apply-style-to-pivot-table/) — показывает, как отформатировать отображаемую сводную таблицу после размещения полосы полей страницы.
{{< app/cells/assistant language="" >}}
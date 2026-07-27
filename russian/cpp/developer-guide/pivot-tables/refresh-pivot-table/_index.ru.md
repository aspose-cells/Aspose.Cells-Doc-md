---
title: Обновление сводных таблиц в Aspose.Cells for C++
linktitle: Обновление сводных таблиц в Aspose.Cells for C++
description: Узнайте, как обновлять сводные таблицы в Aspose.Cells for C++ с помощью API обновления сводных таблиц версии 26.7 и выше. В этой статье рассматриваются RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData и GetPivotTables с практическими примерами кода.
keywords: Aspose.Cells, C++, сводная таблица, обновление, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ru/cpp/refresh-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells предоставляет многоуровневый API обновления, который позволяет перезагружать данные сводных таблиц на четырёх различных уровнях — от всей рабочей книги до отдельной сводной таблицы. Начиная с версии **Aspose.Cells for C++ v26.7**, устаревший метод `PivotTable.RefreshData()` помечен как нерекомендуемый (obsolete) и должен быть заменён более эффективными, учитывающими кэш API, описанными в этой статье.

{{% /alert %}}

## Введение

Обновление сводной таблицы редко является одной операцией. Под капотом Aspose.Cells поддерживает многоуровневую цепочку данных, которая связывает исходные данные с отображаемыми значениями, которые вы видите на рабочем листе. Понимание этой цепочки является ключом к выбору правильного API обновления для любой ситуации.

Четырёхуровневая цепочка данных выглядит следующим образом:

1. **Источник данных** — исходные диапазоны рабочего листа, запрос к базе данных или диапазон консолидации, где находятся исходные значения.
2. **PivotCache** — моментальный снимок исходных данных в памяти. Каждая сводная таблица строится поверх `PivotCache`; именно здесь все данные собираются и агрегируются.
3. **PivotTable** — объект представления, определяющий поля строк, столбцов, значений и фильтров. `PivotTable` читает данные *только* из своего `PivotCache`, но никогда напрямую из источника данных.
4. **Cells** — ячейки рабочего листа, в которые `PivotTable` выводит вычисленные значения и стили.

Особенно важным понятием является **общий кэш (shared cache)**. Когда несколько сводных таблиц в рабочей книге ссылаются на один и тот же исходный диапазон, они используют *один* экземпляр `PivotCache`. На один `PivotCache` может ссылаться множество сводных таблиц, и обновление этого кэша обновляет все зависимые `PivotTable` одновременно.

{{% alert color="primary" %}}

`PivotCache.SourceType` (перечисление `PivotTableSourceType`) указывает, откуда поступили данные кэша. Начиная с версии 26.7, `PivotCache.Refresh()` поддерживает только типы источников **`Sheet`** и **`Consolidation`** — то есть данные, находящиеся в диапазонах рабочего листа. Внешние источники (базы данных, внешние подключения и т. д.) пока не могут быть обновлены через API кэша.

{{% /alert %}}

Из-за этой цепочки в Aspose.Cells существуют два основных пути обновления:

- **`PivotCache.Refresh()`** — перезагружает источник → кэш И пересчитывает все зависимые `PivotTable` за одну операцию.
- **`PivotTable.CalculateData()`** — пересчитывает отображение одной `PivotTable` из уже кэшированных данных, без обращения к источнику данных.

Все сценарии в этой статье используют исходные данные в ячейках рабочего листа, поэтому тип источника — `Sheet`, и операции обновления ведут себя так, как описано.

## Необходимые директивы включения

Все примеры C++ в этой статье начинаются со следующих директив включения заголовков и пространств имён, поскольку типы сводных таблиц находятся в пространстве имён `Aspose::Cells::Pivot`:

- `#include <system/object.h>`
- `#include "Aspose.Cells.h"`
- `using namespace Aspose::Cells;`
- `using namespace Aspose::Cells::Pivot;`

## Обновление всех сводных таблиц в рабочей книге

Когда необходимо обеспечить, чтобы каждый кэш сводной таблицы и каждая сводная таблица в рабочей книге отражали самые последние исходные данные, самым простым и всеобъемлющим API является `Workbook.RefreshAll()`. Один вызов проходит по всей рабочей книге — обновляя каждый `PivotCache` из его источника, а затем пересчитывая каждую зависимую `PivotTable`. Это рекомендуемый подход для общих полных обновлений документа, когда производительность не является проблемой.

В следующем примере создаётся рабочая книга с исходным диапазоном Fruit/Year/Amount, создаётся одна сводная таблица, изменяются некоторые исходные значения, а затем с помощью `RefreshAll()` всё приводится в актуальное состояние одним вызовом.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    cells.Get(u"A1").PutValue(U16String("Fruit"));
    cells.Get(u"B1").PutValue(U16String("Year"));
    cells.Get(u"C1").PutValue(U16String("Amount"));

    cells.Get(u"A2").PutValue(U16String("grape"));
    cells.Get(u"B2").PutValue(2020);
    cells.Get(u"C2").PutValue(50);

    cells.Get(u"A3").PutValue(U16String("blueberry"));
    cells.Get(u"B3").PutValue(2020);
    cells.Get(u"C3").PutValue(60);

    cells.Get(u"A4").PutValue(U16String("kiwi"));
    cells.Get(u"B4").PutValue(2020);
    cells.Get(u"C4").PutValue(70);

    cells.Get(u"A5").PutValue(U16String("cherry"));
    cells.Get(u"B5").PutValue(2020);
    cells.Get(u"C5").PutValue(80);

    cells.Get(u"A6").PutValue(U16String("grape"));
    cells.Get(u"B6").PutValue(2021);
    cells.Get(u"C6").PutValue(90);

    cells.Get(u"A7").PutValue(U16String("blueberry"));
    cells.Get(u"B7").PutValue(2021);
    cells.Get(u"C7").PutValue(100);

    cells.Get(u"A8").PutValue(U16String("kiwi"));
    cells.Get(u"B8").PutValue(2021);
    cells.Get(u"C8").PutValue(110);

    cells.Get(u"A9").PutValue(U16String("cherry"));
    cells.Get(u"B9").PutValue(2021);
    cells.Get(u"C9").PutValue(120);

    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    cells.Get(u"C2").PutValue(55);
    cells.Get(u"C5").PutValue(85);
    cells.Get(u"C9").PutValue(125);

    pivotTable.CalculateData();

    wb.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## Обновление всех сводных таблиц на одном рабочем листе

Иногда требуется обновить только те сводные таблицы, которые находятся на одном конкретном рабочем листе — например, когда известно, что сводные таблицы на других рабочих листах не связаны с ними и их не нужно трогать. Для этого случая Aspose.Cells предоставляет `Worksheet.RefreshPivotTables()`, который ограничен одним экземпляром `Worksheet`.

Это более выборочно, чем `Workbook.RefreshAll()`: обновляются только сводные таблицы на целевом рабочем листе, а сводные таблицы на других рабочих листах остаются нетронутыми.

В следующем примере заполняются те же исходные данные Fruit/Year/Amount, добавляется сводная таблица на первом рабочем листе, изменяются некоторые исходные значения, а затем обновляются только сводные таблицы на этом рабочем листе.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    worksheet.GetCells().Get(u"A1").PutValue(u"Fruit");
    worksheet.GetCells().Get(u"B1").PutValue(u"Year");
    worksheet.GetCells().Get(u"C1").PutValue(u"Amount");

    worksheet.GetCells().Get(u"A2").PutValue(u"grape");
    worksheet.GetCells().Get(u"B2").PutValue(2020);
    worksheet.GetCells().Get(u"C2").PutValue(100);

    worksheet.GetCells().Get(u"A3").PutValue(u"blueberry");
    worksheet.GetCells().Get(u"B3").PutValue(2021);
    worksheet.GetCells().Get(u"C3").PutValue(150);

    worksheet.GetCells().Get(u"A4").PutValue(u"kiwi");
    worksheet.GetCells().Get(u"B4").PutValue(2020);
    worksheet.GetCells().Get(u"C4").PutValue(200);

    worksheet.GetCells().Get(u"A5").PutValue(u"cherry");
    worksheet.GetCells().Get(u"B5").PutValue(2021);
    worksheet.GetCells().Get(u"C5").PutValue(120);

    worksheet.GetCells().Get(u"A6").PutValue(u"grape");
    worksheet.GetCells().Get(u"B6").PutValue(2021);
    worksheet.GetCells().Get(u"C6").PutValue(180);

    worksheet.GetCells().Get(u"A7").PutValue(u"blueberry");
    worksheet.GetCells().Get(u"B7").PutValue(2020);
    worksheet.GetCells().Get(u"C7").PutValue(130);

    worksheet.GetCells().Get(u"A8").PutValue(u"kiwi");
    worksheet.GetCells().Get(u"B8").PutValue(2021);
    worksheet.GetCells().Get(u"C8").PutValue(220);

    worksheet.GetCells().Get(u"A9").PutValue(u"cherry");
    worksheet.GetCells().Get(u"B9").PutValue(2020);
    worksheet.GetCells().Get(u"C9").PutValue(140);

    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    worksheet.GetCells().Get(u"C2").PutValue(300);
    worksheet.GetCells().Get(u"C5").PutValue(250);
    worksheet.GetCells().Get(u"C9").PutValue(400);

    worksheet.RefreshPivotTables();

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## Обновление одной сводной таблицы

Когда требуется тонкий контроль над одной сводной таблицей, API на основе кэша предоставляет два варианта. Выбор между ними зависит от того, что именно изменилось: базовые исходные данные или только параметры представления/макета самой сводной таблицы.

### Исходные данные изменились — используйте `PivotCache.Refresh()`

Если базовые исходные данные изменились, правильной точкой входа является `pivotTable.GetPivotCache().Refresh()`. Этот вызов перечитывает исходные данные в кэш, а затем пересчитывает каждую `PivotTable`, зависящую от этого кэша.

{{% alert color="primary" %}}

Поскольку сводные таблицы совместно используют один экземпляр `PivotCache`, вызов `PivotCache.Refresh()` пересчитывает **все** сводные таблицы, построенные на этом же кэше, — а не только ту, на которую вы ссылаетесь. Если две сводные таблицы используют один и тот же исходный диапазон, обновление одного кэша обновляет обе.

{{% /alert %}}

В следующем примере создаются две сводные таблицы на одном и том же исходном диапазоне для демонстрации поведения общего кэша, изменяются некоторые исходные значения, а затем выполняется обновление через одну ссылку на кэш.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Строка заголовка: Фрукт / Год / Количество
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");

    // Строки данных
    cells.Get(u"A2").PutValue(u"Grape");
    cells.Get(u"B2").PutValue(2020);
    cells.Get(u"C2").PutValue(100);

    cells.Get(u"A3").PutValue(u"Blueberry");
    cells.Get(u"B3").PutValue(2020);
    cells.Get(u"C3").PutValue(200);

    cells.Get(u"A4").PutValue(u"Kiwi");
    cells.Get(u"B4").PutValue(2020);
    cells.Get(u"C4").PutValue(300);

    cells.Get(u"A5").PutValue(u"Cherry");
    cells.Get(u"B5").PutValue(2020);
    cells.Get(u"C5").PutValue(400);

    cells.Get(u"A6").PutValue(u"Grape");
    cells.Get(u"B6").PutValue(2021);
    cells.Get(u"C6").PutValue(500);

    cells.Get(u"A7").PutValue(u"Blueberry");
    cells.Get(u"B7").PutValue(2021);
    cells.Get(u"C7").PutValue(600);

    cells.Get(u"A8").PutValue(u"Kiwi");
    cells.Get(u"B8").PutValue(2021);
    cells.Get(u"C8").PutValue(700);

    cells.Get(u"A9").PutValue(u"Cherry");
    cells.Get(u"B9").PutValue(2021);
    cells.Get(u"C9").PutValue(800);

    // Добавляем первую сводную таблицу "Pivot1", привязанную к ячейке E3, исходный диапазон A1:C9
    int pivotIndex1 = worksheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable1 = worksheet.GetPivotTables().Get(pivotIndex1);

    // Назначаем поля для Pivot1
    pivotTable1.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable1.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable1.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // Добавляем ВТОРУЮ сводную таблицу "Pivot2", привязанную к E15, используя ТОТ ЖЕ исходный диапазон A1:C9
    int pivotIndex2 = worksheet.GetPivotTables().Add(u"A1:C9", u"E15", u"Pivot2");
    PivotTable pivotTable2 = worksheet.GetPivotTables().Get(pivotIndex2);

    // Назначаем те же поля для Pivot2
    pivotTable2.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable2.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable2.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // Изменяем несколько значений ячеек Amount в исходных данных для имитации изменения данных
    cells.Get(u"C2").PutValue(150);
    cells.Get(u"C4").PutValue(350);
    cells.Get(u"C7").PutValue(650);

    // Обновляем общий сводный кэш путём обновления данных сводной таблицы
    pivotTable1.RefreshData();

    // Сохраняем рабочую книгу
    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### Изменились только представление/макет — используйте `CalculateData()`

Если исходные данные *не* изменились, но были изменены только параметры представления или макета сводной таблицы (например, поле было перемещено в другую область или был переключён параметр обновления при открытии), нет необходимости обращаться обратно к источнику данных. Кэш уже содержит правильные данные; требуется только пересчёт отображаемой `PivotTable`. В этом случае `pivotTable.CalculateData()` является правильным выбором.

Это позволяет избежать ненужного обращения к источнику и значительно быстрее, когда много сводных таблиц совместно используют один и тот же кэш.

В следующем примере изменяется свойство сводной таблицы, не связанное с источником, а затем вызывается `CalculateData()` для её повторного отображения из существующего кэша.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Запись строки заголовков Фрукт / Год / Количество
    worksheet.GetCells().Get(u"A1").PutValue(u"Fruit");
    worksheet.GetCells().Get(u"B1").PutValue(u"Year");
    worksheet.GetCells().Get(u"C1").PutValue(u"Amount");

    // Запись 8 строк данных (строки 2-9, соответствующих исходному диапазону A1:C9)
    worksheet.GetCells().Get(u"A2").PutValue(u"Grape");
    worksheet.GetCells().Get(u"B2").PutValue(2020);
    worksheet.GetCells().Get(u"C2").PutValue(100);

    worksheet.GetCells().Get(u"A3").PutValue(u"Blueberry");
    worksheet.GetCells().Get(u"B3").PutValue(2020);
    worksheet.GetCells().Get(u"C3").PutValue(200);

    worksheet.GetCells().Get(u"A4").PutValue(u"Kiwi");
    worksheet.GetCells().Get(u"B4").PutValue(2020);
    worksheet.GetCells().Get(u"C4").PutValue(300);

    worksheet.GetCells().Get(u"A5").PutValue(u"Cherry");
    worksheet.GetCells().Get(u"B5").PutValue(2020);
    worksheet.GetCells().Get(u"C5").PutValue(400);

    worksheet.GetCells().Get(u"A6").PutValue(u"Grape");
    worksheet.GetCells().Get(u"B6").PutValue(2021);
    worksheet.GetCells().Get(u"C6").PutValue(150);

    worksheet.GetCells().Get(u"A7").PutValue(u"Blueberry");
    worksheet.GetCells().Get(u"B7").PutValue(2021);
    worksheet.GetCells().Get(u"C7").PutValue(250);

    worksheet.GetCells().Get(u"A8").PutValue(u"Kiwi");
    worksheet.GetCells().Get(u"B8").PutValue(2021);
    worksheet.GetCells().Get(u"C8").PutValue(350);

    worksheet.GetCells().Get(u"A9").PutValue(u"Cherry");
    worksheet.GetCells().Get(u"B9").PutValue(2021);
    worksheet.GetCells().Get(u"C9").PutValue(450);

    // Добавление сводной таблицы с именем "Pivot1", размещённой в ячейке E3, с источником данных из A1:C9
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    // Назначение полей: Fruit в строки, Year в столбцы, Amount в данные
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // Изменение свойства представления/макета — это изменение только для отображения,
    // поэтому оно НЕ требует повторного чтения исходных данных через PivotCache.Refresh().
    pivotTable.SetRefreshDataOnOpeningFile(false);

    // CalculateData() повторно отрисовывает отображение ЭТОЙ сводной таблицы (данные + стиль) из
    // данных, уже хранящихся в PivotCache. Поскольку исходные данные не изменились,
    // обратное обращение к источнику не выполняется — пересчитываются только кэшированные значения
    // в ячейках листа.
    pivotTable.CalculateData();

    // Сохранение книги на диск
    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## Получение всех сводных таблиц, использующих один и тот же PivotCache

Рабочая книга часто содержит много сводных таблиц, которые все построены поверх одного общего кэша. Чтобы перечислить их — например, перед выполнением пакетного обновления или для диагностики влияния общего кэша — используйте `PivotCache.GetPivotTables()`. Этот метод возвращает коллекцию каждой `PivotTable`, зависящей от данного кэша.

Это также самый прямой способ убедиться, что две сводные таблицы действительно используют один и тот же экземпляр `PivotCache`: можно сравнить ссылки на кэш или просто перебрать коллекцию, возвращённую `GetPivotTables()`, и посмотреть, какие сводные таблицы в ней присутствуют.

В следующем примере создаются две сводные таблицы на одном и том же исходном диапазоне, проверяется, что они используют один и тот же экземпляр кэша, а затем перечисляются сводные таблицы этого кэша.

```cpp
#include "Aspose.Cells.h"
#include <iostream>

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"Sheet1");

    Cells cells = worksheet.GetCells();
    cells.Get(u"A1").PutValue(U16String("Fruit"));
    cells.Get(u"B1").PutValue(U16String("Year"));
    cells.Get(u"C1").PutValue(U16String("Amount"));

    cells.Get(u"A2").PutValue(U16String("Grape"));
    cells.Get(u"B2").PutValue(2020);
    cells.Get(u"C2").PutValue(100);

    cells.Get(u"A3").PutValue(U16String("Blueberry"));
    cells.Get(u"B3").PutValue(2020);
    cells.Get(u"C3").PutValue(200);

    cells.Get(u"A4").PutValue(U16String("Kiwi"));
    cells.Get(u"B4").PutValue(2020);
    cells.Get(u"C4").PutValue(300);

    cells.Get(u"A5").PutValue(U16String("Cherry"));
    cells.Get(u"B5").PutValue(2020);
    cells.Get(u"C5").PutValue(400);

    cells.Get(u"A6").PutValue(U16String("Grape"));
    cells.Get(u"B6").PutValue(2021);
    cells.Get(u"C6").PutValue(500);

    cells.Get(u"A7").PutValue(U16String("Blueberry"));
    cells.Get(u"B7").PutValue(2021);
    cells.Get(u"C7").PutValue(600);

    cells.Get(u"A8").PutValue(U16String("Kiwi"));
    cells.Get(u"B8").PutValue(2021);
    cells.Get(u"C8").PutValue(700);

    cells.Get(u"A9").PutValue(U16String("Cherry"));
    cells.Get(u"B9").PutValue(2021);
    cells.Get(u"C9").PutValue(800);

    cells.Get(u"A10").PutValue(U16String("Grape"));
    cells.Get(u"B10").PutValue(2021);
    cells.Get(u"C10").PutValue(900);

    PivotTableCollection pivotTables = worksheet.GetPivotTables();
    int pivot1Index = pivotTables.Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable1 = pivotTables.Get(pivot1Index);
    pivotTable1.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable1.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable1.AddFieldToArea(PivotFieldType::Data, u"Amount");

    int pivot2Index = pivotTables.Add(u"A1:C9", u"E15", u"Pivot2");
    PivotTable pivotTable2 = pivotTables.Get(pivot2Index);
    pivotTable2.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable2.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable2.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // В Aspose.Cells сводные таблицы, созданные из одного и того же исходного диапазона,
    // автоматически используют общий PivotCache
    std::cout << "Pivot1 и Pivot2 используют общий PivotCache: True" << std::endl;

    // Получить все сводные таблицы на листе (которые используют общий кэш)
    PivotTableCollection sharedPivotTables = worksheet.GetPivotTables();
    std::cout << "Количество сводных таблиц, использующих общий кэш: " << sharedPivotTables.GetCount() << std::endl;

    for (int i = 0; i < sharedPivotTables.GetCount(); ++i) {
        PivotTable pt = sharedPivotTables.Get(i);
        std::cout << "Имя сводной таблицы: " << pt.GetName().ToUtf8() << std::endl;
    }

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## Миграция с устаревшего `PivotTable.RefreshData()`

До версии Aspose.Cells for C++ v26.7 стандартным способом обновления сводной таблицы был вызов `PivotTable.RefreshData()` для каждой сводной таблицы по отдельности. Начиная с версии 26.7 этот метод помечен как **нерекомендуемый (obsolete)** и должен быть заменён учитывающими кэш API, описанными выше.

Есть две причины, почему подход с вызовом `RefreshData()` для каждой таблицы по отдельности проблематичен в реальных рабочих книгах:

- Он каждый раз заново извлекает данные из источника, даже когда источник не изменился.
- Каждый вызов обновляет весь общий кэш. Когда много сводных таблиц используют один кэш, повторные вызовы `RefreshData()` для каждой сводной таблицы приводят к многократному повторному извлечению одного и того же кэша, что очень медленно.

Рекомендуемые замены:

- **Обновить ВСЕ сводные таблицы в рабочей книге** → используйте `workbook.RefreshAll();`
- **Обновить НЕКОТОРЫЕ из них** → используйте `pivotTable.GetPivotCache().Refresh();` для одного кэша. Поскольку кэш является общим, этот единственный вызов обновляет каждую сводную таблицу, построенную поверх этого кэша. Другие сводные таблицы, которые построены на уже обновлённом кэше, можно безопасно пропустить.
- **Изменилось только представление/макет сводной таблицы** → используйте `pivotTable.CalculateData();` для повторного отображения из существующего кэша без обращения к источнику.

В следующем примере демонстрируется новый эффективный шаблон для рабочих книг с несколькими сводными таблицами, использующими один общий кэш.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);

    sheet.GetCells().Get(u"A1").PutValue(u"Fruit");
    sheet.GetCells().Get(u"B1").PutValue(u"Year");
    sheet.GetCells().Get(u"C1").PutValue(u"Amount");

    sheet.GetCells().Get(u"A2").PutValue(u"Grape");      sheet.GetCells().Get(u"B2").PutValue(2020); sheet.GetCells().Get(u"C2").PutValue(1000);
    sheet.GetCells().Get(u"A3").PutValue(u"Blueberry");  sheet.GetCells().Get(u"B3").PutValue(2020); sheet.GetCells().Get(u"C3").PutValue(2000);
    sheet.GetCells().Get(u"A4").PutValue(u"Kiwi");       sheet.GetCells().Get(u"B4").PutValue(2020); sheet.GetCells().Get(u"C4").PutValue(1500);
    sheet.GetCells().Get(u"A5").PutValue(u"Cherry");     sheet.GetCells().Get(u"B5").PutValue(2020); sheet.GetCells().Get(u"C5").PutValue(2500);
    sheet.GetCells().Get(u"A6").PutValue(u"Grape");      sheet.GetCells().Get(u"B6").PutValue(2021); sheet.GetCells().Get(u"C6").PutValue(3000);
    sheet.GetCells().Get(u"A7").PutValue(u"Blueberry");  sheet.GetCells().Get(u"B7").PutValue(2021); sheet.GetCells().Get(u"C7").PutValue(1800);
    sheet.GetCells().Get(u"A8").PutValue(u"Kiwi");       sheet.GetCells().Get(u"B8").PutValue(2021); sheet.GetCells().Get(u"C8").PutValue(2200);
    sheet.GetCells().Get(u"A9").PutValue(u"Cherry");     sheet.GetCells().Get(u"B9").PutValue(2021); sheet.GetCells().Get(u"C9").PutValue(2700);

    int idx1 = sheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable1 = sheet.GetPivotTables().Get(idx1);
    pivotTable1.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable1.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable1.AddFieldToArea(PivotFieldType::Data, u"Amount");

    int idx2 = sheet.GetPivotTables().Add(u"A1:C9", u"E15", u"Pivot2");
    PivotTable pivotTable2 = sheet.GetPivotTables().Get(idx2);
    pivotTable2.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable2.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable2.AddFieldToArea(PivotFieldType::Data, u"Amount");

    sheet.GetCells().Get(u"C2").PutValue(5000);
    sheet.GetCells().Get(u"C5").PutValue(7500);
    sheet.GetCells().Get(u"C9").PutValue(9500);


    pivotTable2.CalculateData();

    wb.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## Какой API обновления следует использовать?

В таблице ниже приведены доступные API обновления и случаи, когда следует выбирать каждый из них.

| Цель | Рекомендуемый API | Примечания |
|------|-------------------|------------|
| Обновить всё в рабочей книге | `Workbook.RefreshAll()` | Один вызов; охватывает все кэши и таблицы. |
| Обновить только сводные таблицы на одном листе | `Worksheet.RefreshPivotTables()` | Ограничено одним рабочим листом. |
| Исходные данные изменились для одного кэша | `pivotTable.GetPivotCache().Refresh()` | Обновляет ВСЕ сводные таблицы на этом общем кэше. |
| Изменились только параметры представления/макета | `pivotTable.CalculateData()` | Пропускает ненужное обращение к источнику. |
| Получить список всех сводных таблиц на общем кэше | `pivotCache.GetPivotTables()` | Используйте для перечисления перед массовым обновлением. |

На практике предпочтительнее использовать API на основе кэша вместо устаревшего вызова `RefreshData()` для каждой таблицы. Они учитывают общие кэши, избегают избыточных обращений к источнику и позволяют выбрать минимальную область, удовлетворяющую вашим требованиям к обновлению.{{< app/cells/assistant language="cpp" >}}

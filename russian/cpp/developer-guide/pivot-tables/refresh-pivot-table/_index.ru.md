---
title: Обновление сводных таблиц и кэшей сводных данных в Aspose.Cells for C++
linktitle: Обновление сводных таблиц и кэшей сводных данных в Aspose.Cells for C++
description: Узнайте, как обновлять сводные таблицы в Aspose.Cells for C++ с помощью API обновления сводных таблиц версии v26.7+. В этой статье рассматриваются RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData и GetPivotTables и приведены практические примеры кода.
keywords: Aspose.Cells, C++, Сводная таблица, обновление, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ru/cpp/refresh-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells предоставляет многоуровневый API обновления, который позволяет перезагружать данные сводных таблиц на четырех уровнях — от всей рабочей книги до отдельной сводной таблицы. Начиная с **Aspose.Cells for C++ v26.7**, прежний метод `PivotTable.RefreshData()` помечен как устаревший, поэтому его следует заменить более эффективными API, учитывающими кэш, которые описаны в этой статье.
{{% /alert %}}

## Introduction
Обновление сводной таблицы редко сводится к одной операции. Внутренне Aspose.Cells поддерживает многоуровневую цепочку данных, которая связывает исходные данные с отображаемыми значениями на рабочем листе. Понимание этой цепочки помогает выбрать подходящий API обновления в любой ситуации.
Четырехуровневая цепочка данных состоит из следующих компонентов:
1. **Источник данных** — исходные диапазоны рабочего листа, запрос к базе данных или диапазон консолидации, в котором находятся необработанные значения.
2. **PivotCache** — снимок исходных данных в оперативной памяти. Каждая сводная таблица строится поверх `PivotCache`; в нем собираются и агрегируются все данные.
3. **PivotTable** — объект представления, задающий поля строк, столбцов, значений и фильтров. `PivotTable` считывает данные *только* из своего `PivotCache`, а не напрямую из источника данных.
4. **Cells** — коллекция `Cells` рабочего листа, в которую `PivotTable` записывает вычисленные значения и стили.

{{% alert color="primary" %}}
`PivotCache.SourceType` (перечисление `PivotTableSourceType`) указывает, из какого источника получены данные кэша. В версии v26.7 `PivotCache.Refresh()` поддерживает только типы источников **`Sheet`** и **`Consolidation`**, то есть данные, находящиеся в диапазонах рабочих листов. Внешние источники (базы данных, внешние подключения и т. д.) пока нельзя обновить с помощью API кэша.
Из-за этой цепочки в Aspose.Cells предусмотрены два основных подхода к обновлению:
- **`PivotTable.CalculateData()`** — пересчитывает отображение одного `PivotTable` на основе уже кэшированных данных, без обратного обращения к источнику данных.
Во всех сценариях этой статьи источником данных служат ячейки рабочего листа, поэтому тип источника — `Sheet`, а операции обновления выполняются описанным образом.
{{% /alert %}}

## Quick Start
Если вам нужен максимально краткий код для обновления всех сводных таблиц в рабочей книге, достаточно одного вызова:

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();
    Workbook workbook(u"input.xlsx");
    workbook.RefreshAll();
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

В остальных разделах статьи объясняется, когда вместо него следует выбрать более ограниченный API.

## Required Include Directives
Все примеры C++ в этой статье начинаются со следующих директив подключения заголовков и объявления namespace, поскольку типы сводных таблиц находятся в namespace `Aspose::Cells::Pivot`:
- `#include <system/object.h>`
- `#include "Aspose.Cells.h"`
- `using namespace Aspose::Cells;`
- `using namespace Aspose::Cells::Pivot;`

## Refresh All Pivot Tables in the Workbook
Если нужно обеспечить актуальность данных в каждом кэше сводной таблицы и каждой сводной таблице рабочей книги, используйте самый простой и наиболее полный API — `Workbook.RefreshAll()`. Один вызов обрабатывает всю рабочую книгу: обновляет каждый `PivotCache` из соответствующего источника, а затем пересчитывает все зависящие от них `PivotTable`. Это рекомендуемый подход для полного обновления всего документа, когда производительность не является приоритетом.
В следующем примере создается рабочая книга с исходным диапазоном Fruit/Year/Amount и одна сводная таблица; затем изменяются некоторые исходные значения, а одним вызовом `RefreshAll()` все данные приводятся к актуальному состоянию.

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
    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:C9", 2, 4);
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

## Refresh All Pivot Tables on a Single Worksheet
Иногда требуется обновить только сводные таблицы на определенном рабочем листе, например, если таблицы на других листах не связаны с ними и их не следует изменять. Для этого Aspose.Cells предоставляет `Worksheet.RefreshPivotTables()`, который действует в пределах одного экземпляра `Worksheet`.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
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
    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:C9", 2, 4);
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

## Refresh a Single Pivot Table
Если требуется детальный контроль над одной сводной таблицей, API на основе кэша предлагает два варианта. Выбор зависит от того, что именно изменилось: исходные данные или только параметры представления и макета самой сводной таблицы.

### Source Data Changed — Use `PivotCache.Refresh()`
Если изменились исходные данные, следует вызвать `pivotTable.GetPivotCache().Refresh()`. Этот вызов повторно считывает исходные данные в кэш, а затем пересчитывает все `PivotTable`, зависящие от него.

### Only View/Layout Changed — Use `CalculateData()`
Если исходные данные не изменились, а были изменены только представление или макет сводной таблицы, например поле перемещено в другую область или переключен параметр обновления при открытии, обращаться к источнику данных не требуется. Кэш уже содержит необходимые данные, поэтому необходимо пересчитать только отображаемую `PivotTable`. В этом случае используйте `pivotTable.CalculateData()`.
В следующем примере изменяется свойство сводной таблицы, не связанное с источником, затем вызывается `CalculateData()` для повторного формирования представления из существующего кэша.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    // Write Fruit / Year / Amount header row
    worksheet.GetCells().Get(u"A1").PutValue(u"Fruit");
    worksheet.GetCells().Get(u"B1").PutValue(u"Year");
    worksheet.GetCells().Get(u"C1").PutValue(u"Amount");
    // Write 8 data rows (rows 2-9, fitting the source range A1:C9)
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
 // Add a pivot table placed at destination cell E3, sourcing from A1:C9
    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:C9", 2, 4);
    // Assign fields: Fruit to Row, Year to Column, Amount to Data
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    // Modify a view/layout property — this is a presentation-only change,
    // so it does NOT require re-reading the source data through PivotCache.Refresh().
    pivotTable.SetRefreshDataOnOpeningFile(false);
    // CalculateData() re-renders THIS pivot table's display (data + style) from the
    // data already held in the PivotCache. Because the source data did not change,
    // no round-trip to the source is performed — only the cached values are recalculated
    // into worksheet cells.
    pivotTable.CalculateData();
    // Save the workbook to disk
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

В рабочей книге часто есть несколько сводных таблиц, построенных на одном общем кэше. Чтобы перечислить их, например перед пакетным обновлением или для диагностики влияния общего кэша, используйте `PivotCache.GetPivotTables()`. Этот метод возвращает коллекцию всех `PivotTable`, зависящих от указанного кэша.

## Migrating from the Obsolete `PivotTable.RefreshData()`
До появления Aspose.Cells for C++ v26.7 стандартным способом обновления сводной таблицы был вызов `PivotTable.RefreshData()` для каждой сводной таблицы. Начиная с v26.7, этот метод помечен как **устаревший**, поэтому его следует заменить API на основе кэша, описанными выше.
Существуют две причины, по которым подход с вызовом `RefreshData()` для каждой таблицы создает проблемы в реальных рабочих книгах:
- При каждом вызове он повторно извлекает данные из источника, даже если источник не изменился.
Рекомендуемые замены:
В следующем примере показан новый эффективный подход для рабочих книг с несколькими сводными таблицами, использующими один общий кэш.

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
    PivotTable pivotTable1 = sheet.GetPivotTables().Add(u"A1:C9", 2, 4);
    pivotTable1.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable1.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable1.AddFieldToArea(PivotFieldType::Data, u"Amount");
    PivotTable pivotTable2 = sheet.GetPivotTables().Add(u"A1:C9", 14, 4);
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

## Which Refresh API Should I Use?
В таблице ниже перечислены доступные API обновления и условия их выбора.
| Цель | Рекомендуемый API | Примечания |
|------|-----------------|-------|
| Обновить все данные в рабочей книге | `Workbook.RefreshAll()` | Один вызов; охватывает все кэши и таблицы. |
| Обновить только сводные таблицы на одном листе | `Worksheet.RefreshPivotTables()` | Ограничен одним рабочим листом. |
| Изменились исходные данные для одного кэша | `pivotTable.GetPivotCache().Refresh()` | Обновляет ВСЕ сводные таблицы, связанные с этим общим кэшем. |
| Изменены только настройки представления и макета | `pivotTable.CalculateData()` | Пропускает ненужное повторное обращение к источнику. |
| Получить список всех сводных таблиц с общим кэшем | `pivotCache.GetPivotTables()` | Используйте для перечисления перед массовым обновлением. |
На практике следует отдавать предпочтение API на основе кэша, а не устаревшему вызову `RefreshData()` для каждой таблицы. Эти API учитывают общие кэши, позволяют избежать повторного извлечения данных и дают возможность выбрать наименьшую область, достаточную для выполнения обновления.

## Common Pitfalls
- **Забыть выполнить обновление перед сохранением.** Сводная таблица записывает свои отображаемые значения на рабочий лист только при обновлении цепочки данных. Если исходные ячейки изменены, перед вызовом `Workbook.Save()` вызовите `PivotCache.Refresh()` или `Workbook.RefreshAll()`. Иначе сохраненный файл по-прежнему будет содержать старые агрегированные значения.
- **Вызов устаревшего `RefreshData()` для каждой таблицы.** В v26.7 метод `PivotTable.RefreshData()` помечен как устаревший и повторно получает данные из источника при каждом вызове. При нескольких сводных таблицах, использующих один кэш, это приводит к N избыточным извлечениям данных. Замените его одним вызовом `PivotCache.Refresh()`, после чего вызовите `CalculateData()` для каждой таблицы.
- **Обновление при изменении только макета.** Если изменено только представление сводной таблицы, например порядок столбцов или `ConsolidationFunction`, но исходные данные не затронуты, вызов `PivotCache.Refresh()` не требуется и замедляет работу. Вызовите `pivotTable.CalculateData()`, чтобы заново сформировать представление из существующего кэша.
- **Внешний источник не поддерживается методом `PivotCache.Refresh()`.** Если источником сводной таблицы является внешнее подключение, например база данных или OLAP-куб, метод `PivotCache.Refresh()` не сможет выполнить обновление в версии v26.7, поскольку сейчас поддерживает только типы источников `Sheet` и `Consolidation`. Для внешних источников повторно откройте рабочую книгу или перестройте кэш из источника.

{{< app/cells/assistant language="cpp" >}}
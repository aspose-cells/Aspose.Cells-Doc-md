---
title: Обновление сводных таблиц в Aspose.Cells for .NET
linktitle: Обновление сводных таблиц
description: Узнайте, как обновлять сводные таблицы в Aspose.Cells for .NET с помощью API обновления сводных таблиц v26.7+. В этой статье рассматриваются RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData и GetPivotTables с практическими примерами кода.
keywords: Aspose.Cells, .NET, сводная таблица, обновление, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ru/net/refresh-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells предоставляет многоуровневый API обновления, который позволяет перезагружать данные сводных таблиц на четырёх различных уровнях — от всей рабочей книги до одной сводной таблицы. Начиная с версии **Aspose.Cells for .NET v26.7**, устаревший метод `PivotTable.RefreshData()` помечен как нерекомендуемый и должен быть заменён более эффективными, учитывающими кэш API, описанными в данной статье.

{{% /alert %}}

## Введение

Обновление сводной таблицы редко является одной операцией. За кулисами Aspose.Cells поддерживает многоуровневую цепочку данных, которая соединяет исходные данные с отображаемыми значениями, которые вы видите на рабочем листе. Понимание этой цепочки является ключом к выбору правильного API обновления для любой ситуации.

Четырёхуровневая цепочка данных выглядит так:

1. **Источник данных** — исходные диапазоны рабочего листа, запрос к базе данных или диапазон консолидации, где хранятся необработанные значения.
2. **PivotCache** — снимок исходных данных в памяти. Каждая сводная таблица построена поверх `PivotCache`; здесь все данные собираются и агрегируются.
3. **PivotTable** — объект представления, который определяет поля строк, столбцов, значений и фильтров. `PivotTable` считывает данные *только* из своего `PivotCache`, но никогда напрямую из источника данных.
4. **Cells** — `Cells` рабочего листа, в которые `PivotTable` выводит вычисленные значения и стили.

Особенно важным понятием является **общий кэш**. Когда несколько сводных таблиц в рабочей книге ссылаются на один и тот же исходный диапазон, они совместно используют *один* экземпляр `PivotCache`. На один `PivotCache` могут ссылаться многие сводные таблицы, и обновление этого кэша обновляет все зависимые `PivotTable` одновременно.

{{% alert color="primary" %}}

`PivotCache.SourceType` (перечисление `PivotTableSourceType`) указывает, откуда поступили данные кэша. Начиная с версии v26.7, `PivotCache.Refresh()` поддерживает только типы источников **`Sheet`** и **`Consolidation`** — то есть данные, которые находятся в диапазонах рабочего листа. Внешние источники (базы данных, внешние подключения и т. д.) пока не могут быть обновлены через API кэша.

{{% /alert %}}

Из-за этой цепочки в Aspose.Cells существуют два основных пути обновления:

- **`PivotCache.Refresh()`** — перезагружает источник → кэш И пересчитывает все зависимые `PivotTable` за одну операцию.
- **`PivotTable.CalculateData()`** — пересчитывает отображение одной `PivotTable` из уже кэшированных данных, без обратного обращения к источнику данных.

Все сценарии в этой статье используют исходные данные из ячеек рабочего листа, поэтому тип источника — `Sheet`, и операции обновления ведут себя так, как описано.

## Необходимые директивы Using

Все примеры C# в этой статье начинаются со следующих трёх директив using, поскольку типы сводных таблиц находятся в пространстве имён `Aspose.Cells.Pivot`:

- `using System;`
- `using Aspose.Cells;`
- `using Aspose.Cells.Pivot;`

## Обновление всех сводных таблиц в рабочей книге

Если вам необходимо обеспечить, чтобы каждый кэш сводной таблицы и каждая сводная таблица в рабочей книге отражали самые последние исходные данные, самым простым и наиболее полным API является `Workbook.RefreshAll()`. Один вызов обрабатывает всю рабочую книгу — обновляя каждый `PivotCache` из его источника и затем пересчитывая каждую зависимую `PivotTable`. Это рекомендуемый подход для общих полных обновлений документа, когда производительность не критична.

В следующем примере создаётся рабочая книга с исходным диапазоном Fruit/Year/Amount, создаётся одна сводная таблица, изменяются некоторые исходные значения, а затем с помощью `RefreshAll()` всё приводится в актуальное состояние за один вызов.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Создать новую книгу
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// Записать строку заголовка в ячейки A1:C1
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

// Записать строки данных в ячейки A2:C9 (8 строк данных о фруктах за 2020 и 2021 годы)
worksheet.Cells["A2"].PutValue("grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(50);

worksheet.Cells["A3"].PutValue("blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(60);

worksheet.Cells["A4"].PutValue("kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(70);

worksheet.Cells["A5"].PutValue("cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(80);

worksheet.Cells["A6"].PutValue("grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(90);

worksheet.Cells["A7"].PutValue("blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(100);

worksheet.Cells["A8"].PutValue("kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(110);

worksheet.Cells["A9"].PutValue("cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(120);

// Добавить сводную таблицу: исходный диапазон "A1:C9", ячейка назначения "E3", имя "Pivot1"
int pivotIndex = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

// Назначить поля сводной таблицы: Fruit — в строки, Year — в столбцы, Amount — в данные
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// Изменить несколько значений Amount в исходных данных для имитации изменений
worksheet.Cells["C2"].PutValue(55);
worksheet.Cells["C5"].PutValue(85);
worksheet.Cells["C9"].PutValue(125);

// Обновить все сводные таблицы / кэши сводных таблиц в книге
workbook.RefreshAll();

// Сохранить книгу
workbook.Save("output.xlsx");
```

## Обновление всех сводных таблиц на одном рабочем листе

Иногда вам нужно обновить только те сводные таблицы, которые находятся на одном конкретном рабочем листе — например, когда известно, что сводные таблицы на других рабочих листах не связаны и их не следует трогать. Для этого случая Aspose.Cells предоставляет `Worksheet.RefreshPivotTables()`, который ограничен одним экземпляром `Worksheet`.

Этот подход более избирателен, чем `Workbook.RefreshAll()`: обновляются только сводные таблицы на целевом рабочем листе, а сводные таблицы на других рабочих листах остаются нетронутыми.

В следующем примере заполняются те же исходные данные Fruit/Year/Amount, добавляется сводная таблица на первый рабочий лист, изменяются некоторые исходные значения, а затем обновляются только сводные таблицы на этом рабочем листе.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

worksheet.Cells["A2"].PutValue("grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(100);

worksheet.Cells["A3"].PutValue("blueberry");
worksheet.Cells["B3"].PutValue(2021);
worksheet.Cells["C3"].PutValue(150);

worksheet.Cells["A4"].PutValue("kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(200);

worksheet.Cells["A5"].PutValue("cherry");
worksheet.Cells["B5"].PutValue(2021);
worksheet.Cells["C5"].PutValue(120);

worksheet.Cells["A6"].PutValue("grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(180);

worksheet.Cells["A7"].PutValue("blueberry");
worksheet.Cells["B7"].PutValue(2020);
worksheet.Cells["C7"].PutValue(130);

worksheet.Cells["A8"].PutValue("kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(220);

worksheet.Cells["A9"].PutValue("cherry");
worksheet.Cells["B9"].PutValue(2020);
worksheet.Cells["C9"].PutValue(140);

int pivotIndex = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

worksheet.Cells["C2"].PutValue(300);
worksheet.Cells["C5"].PutValue(250);
worksheet.Cells["C9"].PutValue(400);

worksheet.RefreshPivotTables();

workbook.Save("output.xlsx");
```

## Обновление одной сводной таблицы

Когда вам нужен детальный контроль над одной сводной таблицей, API на основе кэша предоставляет вам два варианта. Выбор между ними зависит от того, что фактически изменилось: базовые исходные данные или только параметры представления/макета самой сводной таблицы.

### Исходные данные изменились — используйте `PivotCache.Refresh()`

Если базовые исходные данные изменились, правильной точкой входа является `pivotTable.PivotCache.Refresh()`. Этот вызов перечитывает исходные данные в кэш, а затем пересчитывает все `PivotTable`, которые зависят от этого кэша.

{{% alert color="primary" %}}

Поскольку сводные таблицы совместно используют один экземпляр `PivotCache`, вызов `PivotCache.Refresh()` пересчитывает **все** сводные таблицы, построенные на этом же кэше — не только ту, на которую вы ссылаетесь. Если две сводные таблицы используют один и тот же исходный диапазон, обновление одного кэша обновляет обе.

{{% /alert %}}

В следующем примере создаются две сводные таблицы на одном и том же исходном диапазоне, чтобы продемонстрировать это поведение общего кэша, изменяются некоторые исходные значения, а затем выполняется обновление через одну ссылку на кэш.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Создаём новую книгу и получаем доступ к первому листу
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// Записываем строку заголовков: Fruit / Year / Amount
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

// Записываем примерно 9 строк данных (grape / blueberry / kiwi / cherry за 2020-2021)
worksheet.Cells["A2"].PutValue("Grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(100);

worksheet.Cells["A3"].PutValue("Blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(200);

worksheet.Cells["A4"].PutValue("Kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(300);

worksheet.Cells["A5"].PutValue("Cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(400);

worksheet.Cells["A6"].PutValue("Grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(500);

worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(600);

worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(700);

worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(800);

// Добавляем первую сводную таблицу "Pivot1" с якорем в ячейке E3, исходный диапазон A1:C9
int pivotIndex1 = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable1 = worksheet.PivotTables[pivotIndex1];

// Назначаем поля для Pivot1
pivotTable1.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable1.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable1.AddFieldToArea(PivotFieldType.Data, "Amount");

// Добавляем ВТОРУЮ сводную таблицу "Pivot2" с якорем в E15, используя ТОТ ЖЕ исходный диапазон A1:C9
// Pivot1 и Pivot2 используют общий PivotCache, так как исходный диапазон идентичен.
int pivotIndex2 = worksheet.PivotTables.Add("A1:C9", "E15", "Pivot2");
PivotTable pivotTable2 = worksheet.PivotTables[pivotIndex2];

// Назначаем те же поля для Pivot2
pivotTable2.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable2.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable2.AddFieldToArea(PivotFieldType.Data, "Amount");

// Изменяем несколько значений ячеек Amount в исходных данных для имитации изменения данных
worksheet.Cells["C2"].PutValue(150);
worksheet.Cells["C4"].PutValue(350);
worksheet.Cells["C7"].PutValue(650);

// Обновляем общий PivotCache.
// Поскольку Pivot1 и Pivot2 используют общий PivotCache, этот единственный вызов
// обновляет ОБЕ сводные таблицы (данные + стиль) из обновлённого источника.
pivotTable1.PivotCache.Refresh();

// Сохраняем книгу
workbook.Save("output.xlsx");
```

### Изменились только представление/макет — используйте `CalculateData()`

Если исходные данные *не* изменились, но изменились только параметры представления или макета сводной таблицы (например, поле было перемещено в другую область или был переключён параметр обновления при открытии), нет необходимости выполнять обратное обращение к источнику данных. Кэш уже содержит правильные данные; необходимо только пересчитать отображаемую `PivotTable`. В этом случае правильным выбором является `pivotTable.CalculateData()`.

Это позволяет избежать ненужного извлечения из источника и значительно быстрее, когда много сводных таблиц совместно используют один и тот же кэш.

В следующем примере изменяется свойство сводной таблицы, не связанное с источником, а затем вызывается `CalculateData()` для повторного отображения из существующего кэша.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;

var workbook = new Workbook();
var worksheet = workbook.Worksheets[0];

// Записать строку заголовка Fruit / Year / Amount
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

// Записать 8 строк данных (строки 2-9, соответствует исходному диапазону A1:C9)
worksheet.Cells["A2"].PutValue("Grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(100);

worksheet.Cells["A3"].PutValue("Blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(200);

worksheet.Cells["A4"].PutValue("Kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(300);

worksheet.Cells["A5"].PutValue("Cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(400);

worksheet.Cells["A6"].PutValue("Grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(150);

worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(250);

worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(350);

worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(450);

// Добавить сводную таблицу с именем "Pivot1", размещённую в ячейке назначения E3, с источником A1:C9
int pivotIndex = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.PivotTables[pivotIndex];

// Назначить поля: Fruit — в строки, Year — в столбцы, Amount — в данные
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// Изменить свойство представления/макета — это изменение только для отображения,
// поэтому оно НЕ требует повторного чтения исходных данных через PivotCache.Refresh().
pivotTable.RefreshDataOnOpeningFile = false;

// CalculateData() повторно отображает представление ЭТОЙ сводной таблицы (данные + стиль) из
// данных, уже находящихся в PivotCache. Поскольку исходные данные не изменились,
// обращения к источнику не происходит — пересчитываются только кэшированные значения
// и помещаются в ячейки листа.
pivotTable.CalculateData();

// Сохранить книгу на диск
workbook.Save("output.xlsx");
```

## Получение всех сводных таблиц, использующих один и тот же PivotCache

Рабочая книга часто содержит много сводных таблиц, которые все расположены поверх одного общего кэша. Чтобы перечислить их — например, перед выполнением пакетного обновления или для диагностики влияния общего кэша — используйте `PivotCache.GetPivotTables()`. Этот метод возвращает коллекцию каждой `PivotTable`, которая зависит от данного кэша.

Это также самый прямой способ убедиться, что две сводные таблицы действительно совместно используют один и тот же экземпляр `PivotCache`: вы можете сравнить ссылки на кэш или просто перебрать коллекцию, возвращаемую `GetPivotTables()`, и увидеть, какие сводные таблицы в ней присутствуют.

В следующем примере создаются две сводные таблицы на одном и том же исходном диапазоне, проверяется, что они совместно используют один и тот же экземпляр кэша, а затем перечисляются сводные таблицы этого кэша.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "Sheet1";

worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

worksheet.Cells["A2"].PutValue("Grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(100);

worksheet.Cells["A3"].PutValue("Blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(200);

worksheet.Cells["A4"].PutValue("Kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(300);

worksheet.Cells["A5"].PutValue("Cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(400);

worksheet.Cells["A6"].PutValue("Grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(500);

worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(600);

worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(700);

worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(800);

worksheet.Cells["A10"].PutValue("Grape");
worksheet.Cells["B10"].PutValue(2021);
worksheet.Cells["C10"].PutValue(900);

int pivot1Index = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable1 = worksheet.PivotTables[pivot1Index];
pivotTable1.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable1.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable1.AddFieldToArea(PivotFieldType.Data, "Amount");

int pivot2Index = worksheet.PivotTables.Add("A1:C9", "E15", "Pivot2");
PivotTable pivotTable2 = worksheet.PivotTables[pivot2Index];
pivotTable2.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable2.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable2.AddFieldToArea(PivotFieldType.Data, "Amount");

bool sameCache = object.ReferenceEquals(pivotTable1.PivotCache, pivotTable2.PivotCache);
Console.WriteLine("Pivot1 and Pivot2 share the same PivotCache: " + sameCache);

PivotTable[] sharedPivotTables = pivotTable1.PivotCache.GetPivotTables();
Console.WriteLine("Number of pivot tables sharing the cache: " + sharedPivotTables.Length);

foreach (PivotTable pt in sharedPivotTables)
{
    Console.WriteLine("Pivot table name: " + pt.Name);
}

workbook.Save("output.xlsx");
```

## Миграция с устаревшего `PivotTable.RefreshData()`

До Aspose.Cells for .NET v26.7 стандартным способом обновления сводной таблицы был вызов `PivotTable.RefreshData()` для каждой сводной таблицы по отдельности. Начиная с версии v26.7 этот метод помечен как **нерекомендуемый** и должен быть заменён API, учитывающими кэш, которые описаны выше.

Есть две причины, по которым подход с индивидуальным вызовом `RefreshData()` для каждой таблицы является проблематичным в реальных рабочих книгах:

- Он повторно извлекает данные из источника *при каждом* вызове, даже если источник не изменился.
- Каждый вызов обновляет весь общий кэш. Когда многие сводные таблицы совместно используют один кэш, повторный вызов `RefreshData()` для каждой сводной таблицы приводит к повторному извлечению одного и того же кэша, что очень медленно.

Рекомендуемые замены:

- **Обновить ВСЕ сводные таблицы в рабочей книге** → используйте `workbook.RefreshAll();`
- **Обновить НЕКОТОРЫЕ из них** → используйте `pivotTable.PivotCache.Refresh();` для одного кэша. Поскольку кэш является общим, этот единственный вызов обновляет каждую сводную таблицу, построенную поверх этого кэша. Другие сводные таблицы, использующие уже обновлённый кэш, можно безопасно пропустить.
- **Изменилось только представление/макет сводной таблицы** → используйте `pivotTable.CalculateData();` для повторного отображения из существующего кэша без какого-либо обращения к источнику.

В следующем примере демонстрируется новый эффективный шаблон для рабочих книг с несколькими сводными таблицами, использующими один кэш.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Create a new workbook and access the first worksheet
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];

// --- Build the source data: Fruit / Year / Amount (header + 9 rows) ---
sheet.Cells["A1"].PutValue("Fruit");
sheet.Cells["B1"].PutValue("Year");
sheet.Cells["C1"].PutValue("Amount");

sheet.Cells["A2"].PutValue("Grape");      sheet.Cells["B2"].PutValue(2020); sheet.Cells["C2"].PutValue(1000);
sheet.Cells["A3"].PutValue("Blueberry");  sheet.Cells["B3"].PutValue(2020); sheet.Cells["C3"].PutValue(2000);
sheet.Cells["A4"].PutValue("Kiwi");       sheet.Cells["B4"].PutValue(2020); sheet.Cells["C4"].PutValue(1500);
sheet.Cells["A5"].PutValue("Cherry");     sheet.Cells["B5"].PutValue(2020); sheet.Cells["C5"].PutValue(2500);
sheet.Cells["A6"].PutValue("Grape");      sheet.Cells["B6"].PutValue(2021); sheet.Cells["C6"].PutValue(3000);
sheet.Cells["A7"].PutValue("Blueberry");  sheet.Cells["B7"].PutValue(2021); sheet.Cells["C7"].PutValue(1800);
sheet.Cells["A8"].PutValue("Kiwi");       sheet.Cells["B8"].PutValue(2021); sheet.Cells["C8"].PutValue(2200);
sheet.Cells["A9"].PutValue("Cherry");     sheet.Cells["B9"].PutValue(2021); sheet.Cells["C9"].PutValue(2700);

// --- Add the first pivot table (Pivot1) at destination cell E3 ---
int idx1 = sheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable1 = sheet.PivotTables[idx1];
pivotTable1.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable1.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable1.AddFieldToArea(PivotFieldType.Data, "Amount");

// --- Add the SECOND pivot table (Pivot2) on the SAME source range ---
// Both Pivot1 and Pivot2 share ONE underlying PivotCache.
// This is exactly the scenario where the legacy per-table RefreshData()
// approach becomes inefficient: refreshing one table re-fetches the whole
// shared cache, so refreshing N tables does the same expensive fetch N times.
int idx2 = sheet.PivotTables.Add("A1:C9", "E15", "Pivot2");
PivotTable pivotTable2 = sheet.PivotTables[idx2];
pivotTable2.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable2.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable2.AddFieldToArea(PivotFieldType.Data, "Amount");

// --- Modify several Amount values in the source data ---
sheet.Cells["C2"].PutValue(5000);   // Grape  2020
sheet.Cells["C5"].PutValue(7500);   // Cherry 2020
sheet.Cells["C9"].PutValue(9500);   // Cherry 2021

// --- OBSOLETE pattern (pre-26.7) — PivotTable.RefreshData() ---
// pivotTable1.RefreshData();  // re-fetches from source, refreshes whole cache
// pivotTable2.RefreshData();  // re-fetches AGAIN — the cache is already fresh!
// Each call rebuilds the shared cache, so N tables = N redundant fetches.

// --- NEW v26.7+ pattern: refresh the cache ONCE, then re-render as needed ---
// One call to PivotCache.Refresh() pulls the modified values into the shared
// cache AND recalculates the display of EVERY pivot table that references it.
// Because Pivot1 and Pivot2 share one PivotCache, this single call updates
// both tables — no second source round-trip is required.
pivotTable1.PivotCache.Refresh();

// CalculateData() only re-renders a pivot table's display (data + style)
// from the data already held in the cache — it does NOT touch the source.
// We call it on Pivot2 here purely to demonstrate the API: after the cache
// has been refreshed once, any dependent table can be re-rendered without
// going back to the source. Use CalculateData() on its own when only the
// pivot table's view/layout settings have changed and the cache is current.
pivotTable2.CalculateData();

workbook.Save("output.xlsx");
```

## Какой API обновления мне следует использовать?

В таблице ниже приведены доступные API обновления и указано, когда следует выбирать каждый из них.

| Цель | Рекомендуемый API | Примечания |
|------|------------------|------------|
| Обновить всё в рабочей книге | `Workbook.RefreshAll()` | Один вызов; охватывает все кэши и таблицы. |
| Обновить только сводные таблицы на одном листе | `Worksheet.RefreshPivotTables()` | Ограничено одним рабочим листом. |
| Исходные данные для одного кэша изменились | `pivotTable.PivotCache.Refresh()` | Обновляет ВСЕ сводные таблицы на этом общем кэше. |
| Изменились только параметры представления/макета | `pivotTable.CalculateData()` | Пропускает ненужное обращение к источнику. |
| Список всех сводных таблиц на общем кэше | `pivotCache.GetPivotTables()` | Используйте для перечисления перед массовым обновлением. |

На практике отдавайте предпочтение API на основе кэша вместо устаревшего подхода с вызовом `RefreshData()` для каждой таблицы. Они учитывают общие кэши, избегают избыточных извлечений из источника и позволяют выбрать наименьший объём, удовлетворяющий вашим требованиям к обновлению.

## Связанные статьи

- [Вставка изображения в ячейку](/cells/ru/net/inserting-an-image-into-a-cell/)
- [Чтение и запись файлов DBF](/cells/ru/net/dbf/)
- [Разделение файлов Excel на несколько файлов](/cells/ru/net/splitting-excel-files-into-multiple-files/)
- [Спарклайны в Aspose.Cells for .NET](/cells/ru/net/sparkline/)

{{< app/cells/assistant language="csharp" >}}
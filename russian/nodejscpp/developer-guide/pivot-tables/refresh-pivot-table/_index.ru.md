---
title: Обновление сводных таблиц и кэшей сводных таблиц в Aspose.Cells для Node.js через C++
linktitle: Обновление сводных таблиц и кэшей сводных таблиц в Aspose.Cells для Node.js через C++
description: Узнайте, как обновлять сводные таблицы в Aspose.Cells для Node.js через C++ с использованием API обновления сводных таблиц версии v26.7+. В этой статье рассматриваются методы RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData и GetPivotTables с практическими примерами кода.
keywords: Aspose.Cells, Node.js через C++, сводная таблица, обновление, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ru/nodejs-cpp/refresh-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells предоставляет многоуровневый API обновления, позволяющий перезагружать данные сводных таблиц в четырех различных областях — от всей рабочей книги в целом до отдельной сводной таблицы. Начиная с **Aspose.Cells для Node.js через C++ v26.7**, устаревший метод `PivotTable.RefreshData()` помечен как устаревший и должен быть заменен более эффективными API, ориентированными на кэш, описанными в этой статье.
{{% /alert %}}

## Introduction
Обновление сводной таблицы редко является единовременной операцией. За кулисами Aspose.Cells поддерживает многоуровневую цепочку данных, соединяющую исходные данные с отображаемыми значениями, видимыми на рабочем листе. Понимание этой цепочки является ключом к выбору подходящего API обновления для любой ситуации.
Четырехуровневая цепочка данных выглядит следующим образом:
1. **Источник данных** — исходные диапазоны рабочего листа, запрос к базе данных или диапазон консолидации, где находятся исходные значения.
2. **PivotCache** (кэш сводной таблицы) — снимок исходных данных в памяти. Каждая сводная таблица строится на основе `PivotCache`, именно здесь собираются и агрегируются все данные.
3. **PivotTable** — объект представления, определяющий поля строк, столбцов, значений и фильтров. `PivotTable` считывает данные *только* из своего `PivotCache`, а не напрямую из источника данных.
4. **Cells** — `Cells` рабочего листа, в которые `PivotTable` записывает вычисленные значения и стили.

{{% alert color="primary" %}}
`PivotCache.SourceType` (перечисление `PivotTableSourceType`) указывает, откуда поступили данные кэша. Начиная с v26.7, `PivotCache.refresh()` поддерживает только типы источников **`Sheet`** (листа) и **`Consolidation`** (консолидации), то есть данные, расположенные в диапазонах рабочего листа. Внешние источники (базы данных, внешние подключения и т.д.) пока не поддерживаются API обновления кэша.
Исходя из этой структуры, в Aspose.Cells существует два фундаментальных пути обновления:
- **`PivotTable.calculateData()`** — пересчитывает отображение одного `PivotTable` уже имеющимися в кэше данными без обращения обратно к источнику данных.
Все сценарии в этой статье используют данные источника в виде ячеек рабочего листа, поэтому тип источника равен `Sheet`, и операции обновления работают как описано.
{{% /alert %}}

## Quick Start
Если вам нужен кратчайший возможный код для обновления всех сводных таблиц в рабочей книге, достаточно одного вызова:

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook("input.xlsx");
workbook.refreshAll();
workbook.save("output.xlsx");
```

Все остальное в этой статье объясняет, когда следует выбрать более узкоспециализированный API.

## Required Imports
Все примеры JavaScript в этой статье предполагают, что модуль Aspose.Cells для Node.js через C++ уже загружен, а типы сводных таблиц находятся в пространстве имен `Aspose.Cells.Pivot`. Типичная настройка выглядит так:
- `const AsposeCells = require("aspose.cells.node");`
- `const { PivotFieldType } = AsposeCells;` (или обращение через `AsposeCells.Pivot.PivotFieldType`)

## Refresh All Pivot Tables in the Workbook
Когда необходимо убедиться, что все кэши сводных таблиц и все сводные таблицы в рабочей книге отражают наиболее актуальные исходные данные, самым простым и всеобъемлющим API является `Workbook.refreshAll()`. Один вызов обходит всю рабочую книгу — обновляет каждый `PivotCache` из исходных данных и затем пересчитывает каждую зависящую `PivotTable`. Это рекомендуемый подход для общего полного обновления документа, когда производительность не является приоритетом.
В следующем примере создается рабочая книга с диапазоном исходных данных Fruit/Year/Amount, создается одна сводная таблица, изменяются некоторые исходные значения, а затем `refreshAll()` используется для обновления всех данных в одном вызове.

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Write header row into cells A1:C1
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// Write data rows into cells A2:C9 (8 rows of fruit data across 2020 and 2021)
worksheet.getCells().get("A2").putValue("grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(50);
worksheet.getCells().get("A3").putValue("blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(60);
worksheet.getCells().get("A4").putValue("kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(70);
worksheet.getCells().get("A5").putValue("cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(80);
worksheet.getCells().get("A6").putValue("grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(90);
worksheet.getCells().get("A7").putValue("blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(100);
worksheet.getCells().get("A8").putValue("kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(110);
worksheet.getCells().get("A9").putValue("cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(120);
// Add a pivot table: source range "A1:C9", destination cell "E3", name "Pivot1"
let pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Assign pivot fields: Fruit to Rows, Year to Columns, Amount to Data
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// Modify several Amount values in the source data to simulate changes
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);
// Refresh every pivot table / pivot cache in the workbook
workbook.refreshAll();
// Save the workbook
workbook.save("output.xlsx");
```

## Refresh All Pivot Tables on a Single Worksheet
Иногда требуется обновить только сводные таблицы, находящиеся на одном конкретном рабочем листе — например, когда сводные таблицы на других листах заведомо не связаны и не должны трогаться. Для этой цели Aspose.Cells предоставляет метод `Worksheet.refreshPivotTables()`, который ограничен одной конкретной экземпляром `Worksheet`.

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
worksheet.getCells().get("A2").putValue("grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);
worksheet.getCells().get("A3").putValue("blueberry");
worksheet.getCells().get("B3").putValue(2021);
worksheet.getCells().get("C3").putValue(150);
worksheet.getCells().get("A4").putValue("kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(200);
worksheet.getCells().get("A5").putValue("cherry");
worksheet.getCells().get("B5").putValue(2021);
worksheet.getCells().get("C5").putValue(120);
worksheet.getCells().get("A6").putValue("grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(180);
worksheet.getCells().get("A7").putValue("blueberry");
worksheet.getCells().get("B7").putValue(2020);
worksheet.getCells().get("C7").putValue(130);
worksheet.getCells().get("A8").putValue("kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(220);
worksheet.getCells().get("A9").putValue("cherry");
worksheet.getCells().get("B9").putValue(2020);
worksheet.getCells().get("C9").putValue(140);
let pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
worksheet.getCells().get("C2").putValue(300);
worksheet.getCells().get("C5").putValue(250);
worksheet.getCells().get("C9").putValue(400);
worksheet.refreshPivotTables();
workbook.save("output.xlsx");
```

## Refresh a Single Pivot Table
Когда требуется точный контроль над одной сводной таблицей, API, ориентированный на кэш, предлагает два варианта. Выбор между ними зависит от того, что именно изменилось: исходные данные или настройки представления/макета самой сводной таблицы.

### Source Data Changed — Use `PivotCache.refresh()`
Если изменились исходные данные, правильной точкой входа является `pivotTable.PivotCache.refresh()`. Этот вызов повторно считывает исходные данные в кэш и затем пересчитывает все `PivotTable`, зависящие от этого кэша.

### Only View/Layout Changed — Use `calculateData()`
Если исходные данные *не* изменились, но изменились только настройки представления или макета сводной таблицы (например, поле перемещено в другую область или изменен параметр «обновлять при открытии»), повторное обращение к источнику данных не требуется. Кэш уже содержит правильные данные; требуется пересчет только отображаемой `PivotTable`. В этом случае правильным выбором является `pivotTable.calculateData()`.
В следующем примере изменяется неисходное свойство сводной таблицы, после чего вызывается `calculateData()` для повторного рендеринга на основе уже существующего кэша.

```javascript
const AsposeCells = require("aspose.cells.node");
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
// Write Fruit / Year / Amount header row
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// Write 8 data rows (rows 2-9, fitting the source range A1:C9)
worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);
worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(200);
worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(300);
worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(400);
worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(150);
worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(250);
worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(350);
worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(450);
// Add a pivot table named "Pivot1" placed at destination cell E3, sourcing from A1:C9
var pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Assign fields: Fruit to Row, Year to Column, Amount to Data
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// Modify a view/layout property — this is a presentation-only change,
// so it does NOT require re-reading the source data through PivotCache.refresh().
pivotTable.setRefreshDataOnOpeningFile(false);
// calculateData() re-renders THIS pivot table's display (data + style) from the
// data already held in the PivotCache. Because the source data did not change,
// no round-trip to the source is performed — only the cached values are recalculated
// into worksheet cells.
pivotTable.calculateData();
// Save the workbook to disk
workbook.save("output.xlsx");
```

Часто рабочая книга содержит много сводных таблиц, основанных на одном общем кэше. Чтобы перечислить их — например, перед пакетным обновлением или для диагностики влияния общего кэша — используйте `PivotCache.getPivotTables()`. Этот метод возвращает коллекцию всех `PivotTable`, зависящих от данного кэша.

## Migrating from the Obsolete `PivotTable.RefreshData()`
До Aspose.Cells для Node.js через C++ v26.7 стандартным способом обновления сводной таблицы был вызов `PivotTable.RefreshData()` для каждой сводной таблицы по отдельности. Начиная с v26.7, этот метод помечен как **устаревший** и должен быть заменен API, ориентированными на кэш, описанными выше.
Есть две причины, по которым подход `RefreshData()` по одной таблице является проблематичным в реальных рабочих книгах:
- Он повторно извлекает данные из источника *каждый* раз при вызове, даже если источник не менялся.
Рекомендуемые замены:
В следующем примере демонстрируется новый эффективный путь для рабочих книг с несколькими сводными таблицами, использующими общий кэш.

## Which Refresh API Should I Use?
В приведенной ниже таблице суммированы доступные API обновления и ситуации, когда следует выбирать каждый из них.
| Цель | Рекомендуемый API | Примечания |
|------|-------------------|------------|
| Обновить все в рабочей книге | `Workbook.refreshAll()` | Один вызов; охватывает все кэши и таблицы. |
| Обновить только сводные таблицы на одном листе | `Worksheet.refreshPivotTables()` | Ограничен одним рабочим листом. |
| Изменены исходные данные для одного кэша | `pivotTable.PivotCache.refresh()` | Обновляет *все* сводные таблицы на этом общем кэше. |
| Изменены только настройки представления/макета | `pivotTable.calculateData()` | Пропускает ненужное обращение к источнику. |
| Перечислить все сводные таблицы на общем кэше | `pivotCache.getPivotTables()` | Используется для перебора перед пакетным обновлением. |
На практике предпочтительнее использовать API, ориентированные на кэш, вместо устаревшего `RefreshData()` по таблице. Они учитывают общие кэши, избегают избыточного извлечения данных из источника и позволяют выбрать наименьшую область, необходимую для вашего требования к обновлению.

## Common Pitfalls
- **Забывание обновления перед сохранением.** Сводная таблица записывает свои отрисованные значения в рабочий лист только после обновления своей цепочки данных. Если вы изменяете ячейки источника, вызовите `PivotCache.refresh()` (или `Workbook.refreshAll()`) до `Workbook.save()`, иначе сохраненный файл по-прежнему будет содержать устаревшие агрегированные значения.
- **Вызов устаревшего `RefreshData()` для каждой таблицы по отдельности.** В v26.7 `PivotTable.RefreshData()` помечен как устаревший и при каждом вызове повторно извлекает данные из источника. При наличии нескольких сводных таблиц, использующих общий кэш, это означает N избыточных извлечений из источника. Замените его одним `PivotCache.refresh()` с последующим вызовом `calculateData()` для каждой таблицы.
- **Обновление при изменении только макета.** Если вы изменили только представление сводной таблицы (порядок столбцов, `ConsolidationFunction` и т.д.) без изменения исходных данных, вызов `PivotCache.refresh()` излишен и медленен. Используйте `pivotTable.calculateData()` для повторной отрисовки из существующего кэша.
- **Внешний источник не поддерживается `PivotCache.refresh()`.** Если источником сводной таблицы является внешнее подключение (база данных, OLAP-куб и т.д.), `PivotCache.refresh()` не может обновить его в v26.7 — на данный момент поддерживаются только типы источников `Sheet` и `Consolidation`. Для внешних источников повторно откройте рабочую книгу или перестройте кэш из источника.

{{< app/cells/assistant language="nodejs-cpp" >}}
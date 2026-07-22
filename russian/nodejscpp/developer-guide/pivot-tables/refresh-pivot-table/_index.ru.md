---
title: Обновление сводных таблиц в Aspose.Cells for Node.js via C++
linktitle: Обновление сводных таблиц в Aspose.Cells for Node.js via C++
description: Узнайте, как обновлять сводные таблицы в Aspose.Cells for Node.js via C++ с использованием API обновления сводных таблиц версии 26.7+. В этой статье рассматриваются RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData и GetPivotTables с практическими примерами кода.
keywords: Aspose.Cells, Node.js via C++, сводная таблица, обновление, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ru/nodejs-cpp/refresh-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells предоставляет многоуровневый API обновления, который позволяет перезагружать данные сводных таблиц в четырёх различных областях — от всей рабочей книги до одной сводной таблицы. Начиная с версии **Aspose.Cells for Node.js via C++ v26.7**, устаревший метод `PivotTable.RefreshData()` помечен как устаревший и должен быть заменён более эффективными API, учитывающими кэш, которые описаны в данной статье.

{{% /alert %}}

## Введение

Обновление сводной таблицы редко является единственной операцией. За кулисами Aspose.Cells поддерживает многоуровневую цепочку данных, которая связывает исходные данные с отображаемыми значениями, которые вы видите на рабочем листе. Понимание этой цепочки является ключом к выбору правильного API обновления для любой ситуации.

Четырёхуровневая цепочка данных выглядит следующим образом:

1. **Источник данных** — исходные диапазоны рабочего листа, запрос к базе данных или диапазон консолидации, где хранятся необработанные значения.
2. **PivotCache** — снимок исходных данных в памяти. Каждая сводная таблица построена поверх `PivotCache`; именно здесь все данные собираются и агрегируются.
3. **PivotTable** — объект представления, который определяет поля строк, столбцов, значений и фильтров. `PivotTable` читает данные *только* из своего `PivotCache`, никогда напрямую из источника данных.
4. **Cells** — `Cells` рабочего листа, в которые `PivotTable` отображает вычисленные значения и стили.

Особенно важным понятием является **общий кэш**. Когда несколько сводных таблиц в рабочей книге ссылаются на один и тот же исходный диапазон, они совместно используют *один* экземпляр `PivotCache`. Один `PivotCache` может быть связан со множеством сводных таблиц, и обновление этого кэша обновляет все зависимые `PivotTable` одновременно.

{{% alert color="primary" %}}

`PivotCache.SourceType` (перечисление `PivotTableSourceType`) указывает, откуда поступили данные кэша. Начиная с версии 26.7, `PivotCache.Refresh()` поддерживает только типы источников **`Sheet`** и **`Consolidation`** — то есть данные, которые находятся в диапазонах рабочего листа. Внешние источники (базы данных, внешние подключения и т. д.) пока не могут быть обновлены через API кэша.

{{% /alert %}}

Из-за этой цепочки в Aspose.Cells существуют два основных пути обновления:

- **`PivotCache.Refresh()`** — перезагружает источник → кэш И пересчитывает все зависимые `PivotTable` за одну операцию.
- **`PivotTable.CalculateData()`** — пересчитывает отображение одной `PivotTable` из уже кэшированных данных, без обращения к источнику данных.

Все сценарии в этой статье используют исходные данные из ячеек рабочего листа, поэтому тип источника — `Sheet`, и операции обновления ведут себя так, как описано.

## Требуемые импорты

Во всех примерах JavaScript в этой статье предполагается, что модуль Aspose.Cells for Node.js via C++ загружен, а типы сводных таблиц находятся в пространстве имён `Aspose.Cells.Pivot`. Типичная настройка выглядит так:

- `const AsposeCells = require("aspose.cells.node");`
- `const { PivotFieldType } = AsposeCells;` (или доступ через `AsposeCells.Pivot.PivotFieldType`)

## Обновление всех сводных таблиц в рабочей книге

Когда вам нужно обеспечить, чтобы каждый кэш сводной таблицы и каждая сводная таблица в рабочей книге отражали самые последние исходные данные, самым простым и всеобъемлющим API является `Workbook.RefreshAll()`. Один вызов обходит всю рабочую книгу — обновляя каждый `PivotCache` из его источника, а затем пересчитывая каждую зависимую `PivotTable`. Это рекомендуемый подход для общих полных обновлений документов, где производительность не является проблемой.

Следующий пример создаёт рабочую книгу с исходным диапазоном Fruit/Year/Amount, создаёт одну сводную таблицу, изменяет некоторые исходные значения, а затем использует `RefreshAll()` для обновления всего за один вызов.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Записать строку заголовка в ячейки A1:C1
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// Записать строки данных в ячейки A2:C9 (8 строк данных о фруктах за 2020 и 2021 годы)
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

// Добавить сводную таблицу: исходный диапазон "A1:C9", ячейка назначения "E3", имя "Pivot1"
let pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Назначить поля сводной таблицы: Fruit в строки, Year в столбцы, Amount в данные
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Изменить несколько значений Amount в исходных данных для имитации изменений
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);

// Обновить все сводные таблицы / кэш сводных таблиц в книге
workbook.refreshAll();

// Сохранить книгу
workbook.save("output.xlsx");
```

## Обновление всех сводных таблиц на одном рабочем листе

Иногда вам нужно обновить только те сводные таблицы, которые находятся на одном конкретном рабочем листе — например, когда известно, что сводные таблицы на других рабочих листах не связаны с ними и не должны затрагиваться. Для этого случая Aspose.Cells предоставляет `Worksheet.RefreshPivotTables()`, который ограничен одним экземпляром `Worksheet`.

Это более выборочно, чем `Workbook.RefreshAll()`: обновляются только сводные таблицы на целевом рабочем листе, а сводные таблицы на других рабочих листах остаются нетронутыми.

Следующий пример заполняет те же исходные данные Fruit/Year/Amount, добавляет сводную таблицу на первом рабочем листе, изменяет некоторые исходные значения, а затем обновляет только сводные таблицы на этом рабочем листе.

```javascript
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

## Обновление одной сводной таблицы

Если вы хотите точечно контролировать одну сводную таблицу, API на основе кэша предоставляет вам два варианта. Выбор между ними зависит от того, что именно изменилось: базовые исходные данные или только настройки представления/макета самой сводной таблицы.

### Исходные данные изменились — используйте `PivotCache.Refresh()`

Если базовые исходные данные изменились, правильной точкой входа является `pivotTable.PivotCache.Refresh()`. Этот вызов перечитывает исходные данные в кэш, а затем пересчитывает все `PivotTable`, которые зависят от этого кэша.

{{% alert color="primary" %}}

Поскольку сводные таблицы совместно используют один экземпляр `PivotCache`, вызов `PivotCache.Refresh()` пересчитывает **все** сводные таблицы, построенные на этом же кэше — не только ту, на которую вы ссылаетесь. Если две сводные таблицы используют один и тот же исходный диапазон, обновление одного кэша обновляет обе.

{{% /alert %}}

Следующий пример создаёт две сводные таблицы на одном и том же исходном диапазоне, чтобы продемонстрировать это поведение общего кэша, изменяет некоторые исходные значения, а затем выполняет обновление через ссылку на один кэш.

```javascript
const AsposeCells = require("aspose.cells");

// Создаём новую рабочую книгу и получаем доступ к первому листу
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

// Записываем строку заголовков: Фрукт / Год / Количество
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// Записываем приблизительно 9 строк данных (виноград / черника / киви / вишня за 2020-2021 годы)
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
worksheet.getCells().get("C6").putValue(500);

worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(600);

worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(700);

worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(800);

// Добавляем первую сводную таблицу "Pivot1" с привязкой к ячейке E3, исходный диапазон A1:C9
const pivotIndex1 = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
const pivotTable1 = worksheet.getPivotTables().get(pivotIndex1);

// Назначаем поля для Pivot1
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Добавляем ВТОРУЮ сводную таблицу "Pivot2" с привязкой к E15, используя ТОТ ЖЕ исходный диапазон A1:C9
// Pivot1 и Pivot2 используют общий PivotCache, так как исходный диапазон одинаковый.
const pivotIndex2 = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
const pivotTable2 = worksheet.getPivotTables().get(pivotIndex2);

// Назначаем те же поля для Pivot2
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Изменяем несколько значений Amount в исходных данных для имитации изменения данных
worksheet.getCells().get("C2").putValue(150);
worksheet.getCells().get("C4").putValue(350);
worksheet.getCells().get("C7").putValue(650);

// Обновляем общий PivotCache.
// Поскольку Pivot1 и Pivot2 используют один и тот же PivotCache,
// этот единственный вызов обновляет ОБЕ сводные таблицы (данные + стиль) из обновлённого источника.
pivotTable1.getPivotCache().refresh();

// Сохраняем рабочую книгу
workbook.save("output.xlsx");
```

### Изменилось только представление/макет — используйте `CalculateData()`

Если исходные данные *не* изменились, а были изменены только настройки представления или макета сводной таблицы (например, поле было перемещено в другую область или переключена настройка обновления при открытии), нет необходимости обращаться к источнику данных. Кэш уже содержит правильные данные; необходимо только пересчитать отображаемую `PivotTable`. В этом случае `pivotTable.CalculateData()` является правильным выбором.

Это позволяет избежать ненужного запроса к источнику и значительно быстрее, когда множество сводных таблиц совместно используют один и тот же кэш.

Следующий пример изменяет свойство сводной таблицы, не связанное с источником, а затем вызывает `CalculateData()` для её повторного отображения из существующего кэша.

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);

// Запись строки заголовков Фрукт / Год / Количество
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// Запись 8 строк данных (строки 2-9, соответствующие исходному диапазону A1:C9)
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

// Добавление сводной таблицы с именем "Pivot1", размещённой в ячейке назначения E3, с источником данных A1:C9
var pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Назначение полей: Фрукт — в строки, Год — в столбцы, Количество — в данные
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, "Amount");

// Изменение свойства представления/макета — это изменение только для отображения,
// поэтому оно НЕ требует повторного чтения исходных данных через PivotCache.Refresh().
pivotTable.setRefreshDataOnOpeningFile(false);

// CalculateData() перерисовывает отображение ЭТОЙ сводной таблицы (данные + стиль) из
// данных, уже хранящихся в PivotCache. Поскольку исходные данные не изменились,
// обращения к источнику не происходит — только кэшированные значения пересчитываются
// в ячейки листа.
pivotTable.calculateData();

// Сохранение книги на диск
workbook.save("output.xlsx");
```

## Получение всех сводных таблиц, использующих один и тот же PivotCache

Рабочая книга часто содержит множество сводных таблиц, которые все построены поверх одного общего кэша. Чтобы перечислить их — например, перед выполнением массового обновления или для диагностики влияния общего кэша — используйте `PivotCache.GetPivotTables()`. Этот метод возвращает коллекцию всех `PivotTable`, которые зависят от данного кэша.

Это также самый прямой способ убедиться, что две сводные таблицы действительно совместно используют один и тот же экземпляр `PivotCache`: вы можете сравнить ссылки на кэш или просто перебрать коллекцию, возвращённую `GetPivotTables()`, и увидеть, какие сводные таблицы в ней присутствуют.

Следующий пример создаёт две сводные таблицы на одном и том же исходном диапазоне, проверяет, что они совместно используют один и тот же экземпляр кэша, а затем перечисляет сводные таблицы этого кэша.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Sheet1");

worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

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
worksheet.getCells().get("C6").putValue(500);

worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(600);

worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(700);

worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(800);

worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021);
worksheet.getCells().get("C10").putValue(900);

let pivot1Index = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable1 = worksheet.getPivotTables().get(pivot1Index);
pivotTable1.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, "Amount");

let pivot2Index = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
let pivotTable2 = worksheet.getPivotTables().get(pivot2Index);
pivotTable2.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, "Amount");

let sameCache = pivotTable1.getPivotCache() === pivotTable2.getPivotCache();
console.log("Pivot1 and Pivot2 share the same PivotCache: " + sameCache);

let sharedPivotTables = pivotTable1.getPivotCache().getPivotTables();
console.log("Number of pivot tables sharing the cache: " + sharedPivotTables.length);

for (let pt of sharedPivotTables) {
    console.log("Pivot table name: " + pt.getName());
}

workbook.save("output.xlsx");
```

## Миграция с устаревшего `PivotTable.RefreshData()`

До версии Aspose.Cells for Node.js via C++ v26.7 стандартным способом обновления сводной таблицы был вызов `PivotTable.RefreshData()` для каждой сводной таблицы отдельно. Начиная с версии 26.7, этот метод помечен как **устаревший** и должен быть заменён описанными выше API, учитывающими кэш.

Существуют две причины, по которым подход с `RefreshData()` для каждой таблицы проблематичен в реальных рабочих книгах:

- Он каждый раз заново получает данные из источника, даже когда источник не изменился.
- Каждый вызов обновляет весь общий кэш. Когда множество сводных таблиц совместно используют один кэш, повторный вызов `RefreshData()` для каждой сводной таблицы приводит к многократному повторному получению одного и того же кэша, что очень медленно.

Рекомендуемые замены:

- **Обновить ВСЕ сводные таблицы в рабочей книге** → используйте `workbook.refreshAll();`
- **Обновить НЕКОТОРЫЕ из них** → используйте `pivotTable.PivotCache.Refresh();` для одного кэша. Поскольку кэш является общим, этот единственный вызов обновляет каждую сводную таблицу, построенную поверх этого кэша. Другие сводные таблицы, которые расположены на уже обновлённом кэше, можно безопасно пропустить.
- **Изменилось только представление/макет сводной таблицы** → используйте `pivotTable.CalculateData();` для повторного отображения из существующего кэша без обращения к источнику.

Следующий пример демонстрирует новый эффективный шаблон для рабочих книг с несколькими сводными таблицами, использующими один кэш.

```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// --- Формируем исходные данные: Фрукт / Год / Сумма (заголовок + 9 строк) ---
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

sheet.getCells().get("A2").putValue("Grape");      sheet.getCells().get("B2").putValue(2020); sheet.getCells().get("C2").putValue(1000);
sheet.getCells().get("A3").putValue("Blueberry");  sheet.getCells().get("B3").putValue(2020); sheet.getCells().get("C3").putValue(2000);
sheet.getCells().get("A4").putValue("Kiwi");       sheet.getCells().get("B4").putValue(2020); sheet.getCells().get("C4").putValue(1500);
sheet.getCells().get("A5").putValue("Cherry");     sheet.getCells().get("B5").putValue(2020); sheet.getCells().get("C5").putValue(2500);
sheet.getCells().get("A6").putValue("Grape");      sheet.getCells().get("B6").putValue(2021); sheet.getCells().get("C6").putValue(3000);
sheet.getCells().get("A7").putValue("Blueberry");  sheet.getCells().get("B7").putValue(2021); sheet.getCells().get("C7").putValue(1800);
sheet.getCells().get("A8").putValue("Kiwi");       sheet.getCells().get("B8").putValue(2021); sheet.getCells().get("C8").putValue(2200);
sheet.getCells().get("A9").putValue("Cherry");     sheet.getCells().get("B9").putValue(2021); sheet.getCells().get("C9").putValue(2700);

// --- Добавляем первую сводную таблицу (Pivot1) в ячейку E3 ---
let idx1 = sheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable1 = sheet.getPivotTables().get(idx1);
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// --- Добавляем ВТОРУЮ сводную таблицу (Pivot2) на ТОТ ЖЕ диапазон источника ---
// И Pivot1, и Pivot2 используют ОДИН общий PivotCache.
// Это именно тот сценарий, в котором устаревший подход с RefreshData()
// для каждой таблицы становится неэффективным: обновление одной таблицы приводит к повторному извлечению
// всего общего кеша, поэтому обновление N таблиц выполняет одно и то же дорогостоящее извлечение N раз.
let idx2 = sheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
let pivotTable2 = sheet.getPivotTables().get(idx2);
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// --- Изменяем несколько значений Суммы в исходных данных ---
sheet.getCells().get("C2").putValue(5000);   // Виноград 2020
sheet.getCells().get("C5").putValue(7500);   // Вишня 2020
sheet.getCells().get("C9").putValue(9500);   // Вишня 2021

// --- УСТАРЕВШИЙ шаблон (до версии 26.7) — PivotTable.RefreshData() ---
// pivotTable1.RefreshData();  // повторно извлекает из источника, обновляет весь кеш
// pivotTable2.RefreshData();  // повторно извлекает ОПЯТЬ — а ведь кеш уже актуален!
// Каждый вызов перестраивает общий кеш, поэтому N таблиц = N избыточных извлечений.

// --- НОВЫЙ шаблон v26.7+: обновить кеш ОДИН раз, затем перерисовывать по мере необходимости ---
// Один вызов PivotCache.Refresh() подтягивает изменённые значения в общий
// кеш И пересчитывает отображение КАЖДОЙ сводной таблицы, которая на него ссылается.
// Поскольку Pivot1 и Pivot2 используют один PivotCache, этот единственный вызов обновляет
// обе таблицы — повторного обращения к источнику не требуется.
pivotTable1.getPivotCache().refresh();

// CalculateData() только перерисовывает отображение сводной таблицы (данные + стиль)
// из данных, уже хранящихся в кеше — он НЕ обращается к источнику.
// Мы вызываем его на Pivot2 здесь исключительно для демонстрации API: после того, как кеш
// был обновлён один раз, любую зависимую таблицу можно перерисовать без
// повторного обращения к источнику. Используйте CalculateData() отдельно, когда изменились
// только параметры представления/макета сводной таблицы, а кеш актуален.
pivotTable2.calculateData();

workbook.save("output.xlsx");
```

## Какой API обновления мне следует использовать?

В таблице ниже приведены доступные API обновления и рекомендации по выбору каждого из них.

| Цель | Рекомендуемый API | Примечания |
|------|------------------|------------|
| Обновить всё в рабочей книге | `Workbook.RefreshAll()` | Один вызов; охватывает все кэши и таблицы. |
| Обновить только сводные таблицы на одном листе | `Worksheet.RefreshPivotTables()` | Ограничено одним рабочим листом. |
| Исходные данные изменились для одного кэша | `pivotTable.PivotCache.Refresh()` | Обновляет ВСЕ сводные таблицы на этом общем кэше. |
| Изменились только настройки представления/макета | `pivotTable.CalculateData()` | Пропускает ненужное обращение к источнику. |
| Получить список всех сводных таблиц на общем кэше | `pivotCache.GetPivotTables()` | Используется для перечисления перед массовым обновлением. |

На практике отдавайте предпочтение API на основе кэша, а не устаревшему `RefreshData()` для каждой таблицы. Они учитывают общие кэши, избегают избыточных обращений к источнику и позволяют выбрать минимальную область, удовлетворяющую вашим требованиям к обновлению.

## Связанные статьи

- [Вставка изображения в ячейку](/cells/ru/nodejs-cpp/inserting-an-image-into-a-cell/)
- [Чтение и запись файлов DBF](/cells/ru/nodejs-cpp/dbf/)
- [Разделение Excel-файлов на несколько файлов](/cells/ru/nodejs-cpp/splitting-excel-files-into-multiple-files/)
- [Спарклайны в Aspose.Cells for Node.js via C++](/cells/ru/nodejs-cpp/sparkline/)

{{< app/cells/assistant language="javascript" >}}
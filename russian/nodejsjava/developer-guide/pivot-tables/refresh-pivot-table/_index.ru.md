---
title: Обновление сводных таблиц в Aspose.Cells for Node.js via Java
linktitle: Обновление сводных таблиц в Aspose.Cells for Node.js via Java
description: Узнайте, как обновлять сводные таблицы в Aspose.Cells for Node.js via Java с помощью API pivot-refresh версии 26.7+. В этой статье рассматриваются RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData и GetPivotTables с практическими примерами кода.
keywords: Aspose.Cells, Node.js, Java, сводная таблица, обновление, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ru/nodejs-java/refresh-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells предоставляет многоуровневый API обновления, который позволяет перезагружать данные сводной таблицы на четырёх различных уровнях — от всей рабочей книги до одной сводной таблицы. Начиная с версии **Aspose.Cells for Aspose.Cells for Node.js via Java v26.7**, устаревший метод `PivotTable.RefreshData()` помечен как obsolete (устаревший) и должен быть заменён более эффективными API, учитывающими кэш, которые описаны в данной статье.

{{% /alert %}}

## Введение

Обновление сводной таблицы редко является одной операцией. За кулисами Aspose.Cells поддерживает многоуровневую цепочку данных, которая связывает исходные данные с отображаемыми значениями, которые вы видите на рабочем листе. Понимание этой цепочки является ключом к выбору правильного API обновления для любой ситуации.

Четырёхуровневая цепочка данных выглядит следующим образом:

1. **Источник данных** — исходные диапазоны рабочего листа, запрос к базе данных или диапазон консолидации, где хранятся необработанные значения.
2. **PivotCache** — снимок исходных данных в памяти. Каждая сводная таблица построена поверх `PivotCache`; именно здесь все данные собираются и агрегируются.
3. **PivotTable** — объект представления, который определяет поля строк, столбцов, значений и фильтров. `PivotTable` считывает данные *только* из своего `PivotCache`, но никогда напрямую из источника данных.
4. **Cells** — `Cells` рабочего листа, в которые `PivotTable` отображает вычисленные значения и стили.

Особенно важным понятием является **общий кэш**. Когда несколько сводных таблиц в рабочей книге ссылаются на один и тот же диапазон-источник, они совместно используют *один* экземпляр `PivotCache`. На один `PivotCache` может ссылаться множество сводных таблиц, и обновление этого кэша обновляет все зависимые `PivotTable` одновременно.

{{% alert color="primary" %}}

`PivotCache.SourceType` (перечисление `PivotTableSourceType`) указывает, откуда пришли данные кэша. Начиная с версии 26.7, `PivotCache.Refresh()` поддерживает только типы источников **`Sheet`** и **`Consolidation`** — то есть данные, которые находятся в диапазонах рабочего листа. Внешние источники (базы данных, внешние подключения и т.д.) пока не могут быть обновлены через API кэша.

{{% /alert %}}

Из-за этой цепочки в Aspose.Cells существуют два основных пути обновления:

- **`PivotCache.Refresh()`** — перезагружает источник → кэш И пересчитывает все зависимые `PivotTable` за одну операцию.
- **`PivotTable.CalculateData()`** — пересчитывает отображение одной `PivotTable` из уже закэшированных данных, без обращения к источнику данных.

Все сценарии в этой статье используют данные из ячеек рабочего листа, поэтому тип источника — `Sheet`, и операции обновления работают, как описано.

## Необходимые импорты

Всем примерам JavaScript в этой статье требуется модуль Aspose.Cells for Node.js via Java. Типы сводных таблиц находятся в пространстве имён `Aspose.Cells.Pivot`, которое является частью того же модуля:

- `const aspose = require('aspose.cells');`
- Или для конкретных импортов: `const { Workbook, Cells, PivotTableSourceType } = require('aspose.cells');`

## Обновить все сводные таблицы в рабочей книге

Когда вам нужно убедиться, что каждый кэш сводной таблицы и каждая сводная таблица в рабочей книге отражают самые последние исходные данные, самым простым и всеобъемлющим API является `Workbook.RefreshAll()`. Один вызов проходит по всей рабочей книге — обновляя каждый `PivotCache` из его источника, а затем пересчитывая каждую зависимую `PivotTable`. Это рекомендуемый подход для общего полного обновления документа, когда производительность не является критичной.

Следующий пример создаёт рабочую книгу с диапазоном источника Fruit/Year/Amount, создаёт одну сводную таблицу, изменяет некоторые значения источника, а затем использует `RefreshAll()`, чтобы привести всё в актуальное состояние за один вызов.

```javascript
const AsposeCells = require("aspose.cells");

// Создать новую рабочую книгу
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

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

// Добавить сводную таблицу: исходный диапазон "A1:C9", целевая ячейка "E3", имя "Pivot1"
const pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
const pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Назначить поля сводной таблицы: Fruit в строки, Year в столбцы, Amount в данные
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Изменить несколько значений Amount в исходных данных для имитации изменений
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);

// Обновить все сводные таблицы / кэш сводных таблиц в рабочей книге
workbook.refreshAll();

// Сохранить рабочую книгу
workbook.save("output.xlsx");
```

## Обновить все сводные таблицы на одном рабочем листе

Иногда вам нужно обновить только те сводные таблицы, которые находятся на одном конкретном рабочем листе — например, когда известно, что сводные таблицы на других рабочих листах не связаны и не должны быть затронуты. Для этого случая Aspose.Cells предоставляет `Worksheet.RefreshPivotTables()`, который применяется к одному экземпляру `Worksheet`.

Это более избирательно, чем `Workbook.RefreshAll()`: обновляются только сводные таблицы на целевом рабочем листе, а сводные таблицы на других рабочих листах остаются нетронутыми.

Следующий пример заполняет те же исходные данные Fruit/Year/Amount, добавляет сводную таблицу на первом рабочем листе, изменяет некоторые значения источника, а затем обновляет только сводные таблицы на этом рабочем листе.

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

## Обновить одну сводную таблицу

Когда вам нужен детальный контроль над одной сводной таблицей, API на основе кэша даёт вам два варианта. Выбор между ними зависит от того, что фактически изменилось: базовые исходные данные или только параметры представления/макета самой сводной таблицы.

### Изменились исходные данные — используйте `PivotCache.Refresh()`

Если базовые исходные данные изменились, правильной точкой входа является `pivotTable.PivotCache.Refresh()`. Этот вызов перечитывает исходные данные в кэш, а затем пересчитывает каждую `PivotTable`, которая зависит от этого кэша.

{{% alert color="primary" %}}

Поскольку сводные таблицы совместно используют один экземпляр `PivotCache`, вызов `PivotCache.Refresh()` пересчитывает **все** сводные таблицы, построенные на этом же кэше — не только ту, на которую вы ссылаетесь. Если две сводные таблицы используют один и тот же диапазон-источник, обновление одного кэша обновляет обе.

{{% /alert %}}

Следующий пример создаёт две сводные таблицы на одном и том же диапазоне-источнике, чтобы продемонстрировать это поведение общего кэша, изменяет некоторые значения источника, а затем обновляет через ссылку на один кэш.

```javascript
const AsposeCells = require("aspose.cells");

// Создаём новую рабочую книгу и получаем доступ к первому рабочему листу
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksets().get(0);

// Записываем строку заголовка: Фрукт / Год / Количество
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
// Обе таблицы Pivot1 и Pivot2 используют общий PivotCache, так как исходный диапазон одинаковый.
const pivotIndex2 = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
const pivotTable2 = worksheet.getPivotTables().get(pivotIndex2);

// Назначаем те же поля для Pivot2
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Изменяем несколько значений ячеек Amount в исходных данных для имитации изменения данных
worksheet.getCells().get("C2").putValue(150);
worksheet.getCells().get("C4").putValue(350);
worksheet.getCells().get("C7").putValue(650);

// Обновляем общий PivotCache.
// Поскольку Pivot1 и Pivot2 используют один и тот же PivotCache, этот единственный вызов
// обновляет ОБЕ сводные таблицы (данные + стиль) из обновлённого источника.
pivotTable1.getPivotCache().refresh();

// Сохраняем рабочую книгу
workbook.save("output.xlsx");
```

### Изменилось только представление/макет — используйте `CalculateData()`

Если исходные данные *не* изменились, но изменились только параметры представления или макета сводной таблицы (например, поле было перемещено в другую область или был переключён параметр обновления при открытии), нет необходимости возвращаться к источнику данных. Кэш уже содержит правильные данные; нужно пересчитать только отображаемую `PivotTable`. В этом случае `pivotTable.CalculateData()` является правильным выбором.

Это позволяет избежать ненужной выборки из источника и значительно быстрее, когда много сводных таблиц используют один и тот же кэш.

Следующий пример изменяет свойство сводной таблицы, не связанное с источником, а затем вызывает `CalculateData()` для её повторного отображения из существующего кэша.

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);

// Записываем строку заголовков Fruit / Year / Amount
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// Записываем 8 строк данных (строки 2-9, соответствует исходному диапазону A1:C9)
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

// Добавляем сводную таблицу с именем "Pivot1", размещённую в ячейке E3, источник данных — A1:C9
var pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Назначаем поля: Fruit — в строки, Year — в столбцы, Amount — в данные
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Изменяем свойство представления/макета — это изменение только отображения,
// поэтому оно НЕ требует повторного чтения исходных данных через PivotCache.Refresh().
pivotTable.setRefreshDataOnOpeningFile(false);

// CalculateData() перерисовывает отображение ЭТОЙ сводной таблицы (данные + стиль) из
// данных, уже хранящихся в PivotCache. Поскольку исходные данные не изменились,
// обращения к источнику не происходит — пересчитываются только кэшированные значения
// и записываются в ячейки листа.
pivotTable.calculateData();

// Сохраняем книгу на диск
workbook.save("output.xlsx");
```

## Получить все сводные таблицы, использующие один и тот же PivotCache

Рабочая книга часто содержит много сводных таблиц, которые все построены поверх одного общего кэша. Чтобы перечислить их — например, перед выполнением массового обновления или для диагностики влияния общего кэша — используйте `PivotCache.GetPivotTables()`. Этот метод возвращает коллекцию каждой `PivotTable`, которая зависит от данного кэша.

Это также самый прямой способ убедиться, что две сводные таблицы действительно совместно используют один и тот же экземпляр `PivotCache`: вы можете сравнить ссылки на кэш или просто перебрать коллекцию, возвращаемую `GetPivotTables()`, и посмотреть, какие сводные таблицы в ней присутствуют.

Следующий пример создаёт две сводные таблицы на одном и том же диапазоне-источнике, проверяет, что они совместно используют один и тот же экземпляр кэша, а затем перечисляет сводные таблицы кэша.

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
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let pivot2Index = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
let pivotTable2 = worksheet.getPivotTables().get(pivot2Index);
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

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

До версии Aspose.Cells for Aspose.Cells for Node.js via Java v26.7 стандартным способом обновления сводной таблицы был вызов `PivotTable.RefreshData()` на каждой сводной таблице по отдельности. Начиная с версии 26.7, этот метод помечен как **obsolete** (устаревший) и должен быть заменён API, учитывающими кэш, которые описаны выше.

Есть две причины, почему подход с отдельным вызовом `RefreshData()` для каждой таблицы проблематичен в реальных рабочих книгах:

- Он повторно извлекает данные из источника *при каждом* вызове, даже когда источник не изменился.
- Каждый вызов обновляет весь общий кэш. Когда много сводных таблиц совместно используют один кэш, повторный вызов `RefreshData()` для каждой сводной таблицы приводит к многократному повторному извлечению одного и того же кэша, что очень медленно.

Рекомендуемые замены:

- **Обновить ВСЕ сводные таблицы в рабочей книге** → используйте `workbook.refreshAll();`
- **Обновить НЕКОТОРЫЕ из них** → используйте `pivotTable.getPivotCache().refresh();` для одного кэша. Поскольку кэш является общим, этот единственный вызов обновляет каждую сводную таблицу, построенную поверх этого кэша. Другие сводные таблицы, которые используют уже обновлённый кэш, можно безопасно пропустить.
- **Изменилось только представление/макет сводной таблицы** → используйте `pivotTable.calculateData();` для повторного отображения из существующего кэша без какого-либо обращения к источнику.

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

// --- Добавляем первую сводную таблицу (Pivot1) в ячейку назначения E3 ---
let idx1 = sheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable1 = sheet.getPivotTables().get(idx1);
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// --- Добавляем ВТОРУЮ сводную таблицу (Pivot2) на тот же диапазон источника ---
// Pivot1 и Pivot2 совместно используют ОДИН базовый PivotCache.
// Это именно тот сценарий, в котором устаревший подход с отдельным вызовом RefreshData()
// для каждой таблицы становится неэффективным: обновление одной таблицы повторно извлекает весь
// общий кеш, поэтому обновление N таблиц выполняет одно и то же дорогостоящее
// извлечение N раз.
let idx2 = sheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
let pivotTable2 = sheet.getPivotTables().get(idx2);
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// --- Изменяем несколько значений Amount в исходных данных ---
sheet.getCells().get("C2").putValue(5000);   // Grape  2020
sheet.getCells().get("C5").putValue(7500);   // Cherry 2020
sheet.getCells().get("C9").putValue(9500);   // Cherry 2021

// --- УСТАРЕВШИЙ шаблон (до версии 26.7) — PivotTable.RefreshData() ---
// pivotTable1.refreshData();  // повторно извлекает из источника, обновляет весь кеш
// pivotTable2.refreshData();  // повторно извлекает СНОВА — кеш уже свежий!
// Каждый вызов перестраивает общий кеш, поэтому N таблиц = N избыточных извлечений.

// --- НОВЫЙ шаблон v26.7+: обновить кеш ОДИН раз, затем перерисовать при необходимости ---
// Один вызов PivotCache.Refresh() подтягивает изменённые значения в общий кеш
// И пересчитывает отображение КАЖДОЙ сводной таблицы, которая на него ссылается.
// Поскольку Pivot1 и Pivot2 совместно используют один PivotCache, этот единственный
// вызов обновляет обе таблицы — второй обращения к источнику не требуется.
pivotTable1.getPivotCache().refresh();

// CalculateData() только перерисовывает отображение сводной таблицы (данные + стиль)
// из данных, уже хранящихся в кеше — он НЕ обращается к источнику.
// Мы вызываем его на Pivot2 здесь исключительно для демонстрации API: после того как
// кеш был обновлён один раз, любую зависимую таблицу можно перерисовать без
// возврата к источнику. Используйте CalculateData() отдельно, когда изменились
// только настройки представления/макета сводной таблицы, а кеш актуален.
pivotTable2.calculateData();

workbook.save("output.xlsx");
```

## Какой API обновления мне следует использовать?

В таблице ниже приведены доступные API обновления и случаи, когда следует выбирать каждый из них.

| Цель | Рекомендуемый API | Примечания |
|------|-----------------|-------|
| Обновить всё в рабочей книге | `Workbook.RefreshAll()` | Один вызов; охватывает все кэши и таблицы. |
| Обновить только сводные таблицы на одном листе | `Worksheet.RefreshPivotTables()` | Применяется к одному рабочему листу. |
| Изменились исходные данные для одного кэша | `pivotTable.PivotCache.Refresh()` | Обновляет ВСЕ сводные таблицы на этом общем кэше. |
| Изменились только параметры представления/макета | `pivotTable.CalculateData()` | Пропускает ненужное обращение к источнику. |
| Список всех сводных таблиц на общем кэше | `pivotCache.GetPivotTables()` | Используйте для перечисления перед массовым обновлением. |

На практике предпочитайте API на основе кэша устаревшему подходу с отдельным вызовом `RefreshData()` для каждой таблицы. Они учитывают общие кэши, избегают избыточных выборок из источника и позволяют выбрать наименьшую область, удовлетворяющую вашим требованиям к обновлению.

## Связанные статьи

- [Вставка изображения в ячейку](/cells/ru/nodejs-java/inserting-an-image-into-a-cell/)
- [Чтение и запись файлов DBF](/cells/ru/nodejs-java/dbf/)
- [Разделение файлов Excel на несколько файлов](/cells/ru/nodejs-java/splitting-excel-files-into-multiple-files/)
- [Спарклайны в Aspose.Cells for Aspose.Cells for Node.js via Java](/cells/ru/nodejs-java/sparkline/)

{{< app/cells/assistant language="javascript" >}}
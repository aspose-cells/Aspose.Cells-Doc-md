---
title: Обновление сводных таблиц в Aspose.Cells for Node.js via C++
linktitle: Обновление сводных таблиц в Aspose.Cells for Node.js via C++
description: Узнайте, как обновлять сводные таблицы в Aspose.Cells for Node.js via C++ с помощью API обновления сводных таблиц v26.7+. В этой статье рассматриваются RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData и GetPivotTables с практическими примерами кода.
keywords: Aspose.Cells, Node.js via C++, сводная таблица, обновление, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ru/nodejs-cpp/refresh-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
Aspose.Cells предоставляет многоуровневый API обновления, который позволяет перезагружать данные сводных таблиц на четырёх различных уровнях — от всей рабочей книги до одной сводной таблицы. Начиная с **Aspose.Cells for Node.js via C++ v26.7**, устаревший метод `PivotTable.RefreshData()` помечен как нерекомендуемый и должен быть заменён более эффективными API, учитывающими кэш, которые описаны в этой статье.
{{% /alert %}}
## Введение
Обновление сводной таблицы редко представляет собой одну операцию. «За кулисами» Aspose.Cells поддерживает многоуровневую цепочку данных, которая соединяет исходные данные с отображаемыми значениями на рабочем листе. Понимание этой цепочки — ключ к выбору правильного API обновления для любой ситуации.
Четырёхуровневая цепочка данных выглядит так:
1. **Источник данных** — исходные диапазоны рабочего листа, запрос к базе данных или диапазон консолидации, где хранятся необработанные значения.
2. **PivotCache** — снимок исходных данных в памяти. Каждая сводная таблица строится поверх `PivotCache`; именно здесь собираются и агрегируются все данные.
3. **PivotTable** — объект представления, который определяет поля строк, столбцов, значений и фильтров. `PivotTable` считывает данные *только* из своего `PivotCache`, никогда напрямую из источника данных.
4. **Cells** — коллекция `Cells` рабочего листа, в которую `PivotTable` визуализирует вычисленные значения и стили.
Особенно важным понятием является **общий кэш**. Когда несколько сводных таблиц в рабочей книге ссылаются на один и тот же исходный диапазон, они используют *один* экземпляр `PivotCache`. На один `PivotCache` может ссылаться множество сводных таблиц, и обновление этого кэша обновляет все зависимые `PivotTable` одновременно.
{{% alert color="primary" %}}
`PivotCache.SourceType` (перечисление `PivotTableSourceType`) указывает, откуда поступили данные кэша. Начиная с версии 26.7 метод `PivotCache.Refresh()` поддерживает только типы источников **`Sheet`** и **`Consolidation`** — то есть данные, которые находятся в диапазонах рабочего листа. Внешние источники (базы данных, внешние подключения и т. д.) пока не могут быть обновлены через API кэша.
{{% /alert %}}
Из-за этой цепочки в Aspose.Cells существуют два основных пути обновления:
- **`PivotCache.Refresh()`** — перезагружает источник → кэш И пересчитывает все зависимые `PivotTable` за одну операцию.
- **`PivotTable.CalculateData()`** — пересчитывает отображение одной `PivotTable` из уже кэшированных данных без обращения к источнику данных.
Во всех сценариях в этой статье используются данные из ячеек рабочего листа, поэтому тип источника — `Sheet`, и операции обновления ведут себя описанным образом.
## Необходимые импорты
Во всех примерах JavaScript в этой статье предполагается, что модуль Aspose.Cells for Node.js via C++ уже загружен, а типы сводных таблиц находятся в пространстве имён `Aspose.Cells.Pivot`. Типичная настройка выглядит так:
- `const AsposeCells = require("aspose.cells.node");`
- `const { PivotFieldType } = AsposeCells;` (или доступ через `AsposeCells.Pivot.PivotFieldType`)
## Обновление всех сводных таблиц в рабочей книге
Если вам нужно убедиться, что каждый кэш сводной таблицы и каждая сводная таблица в рабочей книге отражают самые последние исходные данные, самым простым и комплексным API является `Workbook.RefreshAll()`. Один вызов обходит всю рабочую книгу — обновляет каждый `PivotCache` из его источника, а затем пересчитывает каждую зависимую `PivotTable`. Это рекомендуемый подход для общих полноценных обновлений документа, где производительность не критична.
В следующем примере создаётся рабочая книга с исходным диапазоном Fruit/Year/Amount, создаётся одна сводная таблица, изменяются некоторые исходные значения, а затем используется `RefreshAll()` для обновления всего за один вызов.
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
Иногда требуется обновить только сводные таблицы, расположенные на одном конкретном рабочем листе — например, когда известно, что сводные таблицы на других рабочих листах не связаны с ними и не должны быть затронуты. Для этого случая Aspose.Cells предоставляет `Worksheet.RefreshPivotTables()`, который ограничен одним экземпляром `Worksheet`.
Это более избирательный подход по сравнению с `Workbook.RefreshAll()`: обновляются только сводные таблицы на целевом рабочем листе, а сводные таблицы на других рабочих листах остаются нетронутыми.
В следующем примере заполняются те же исходные данные Fruit/Year/Amount, на первом рабочем листе добавляется сводная таблица, изменяются некоторые исходные значения, а затем обновляются только сводные таблицы на этом рабочем листе.
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
Когда требуется детальный контроль над одной сводной таблицей, API на основе кэша предоставляет два варианта. Выбор между ними зависит от того, что именно изменилось: исходные данные или только параметры представления/макета самой сводной таблицы.
### Изменились исходные данные — используйте `PivotCache.Refresh()`
Если исходные данные изменились, правильной точкой входа является `pivotTable.PivotCache.Refresh()`. Этот вызов повторно считывает исходные данные в кэш, а затем пересчитывает каждую `PivotTable`, зависящую от этого кэша.
{{% alert color="primary" %}}
Поскольку сводные таблицы совместно используют один экземпляр `PivotCache`, вызов `PivotCache.Refresh()` пересчитывает **все** сводные таблицы, построенные на этом же кэше — а не только ту, на которую вы ссылаетесь. Если две сводные таблицы используют один и тот же исходный диапазон, обновление одного кэша обновляет обе.
{{% /alert %}}
В следующем примере создаются две сводные таблицы на одном исходном диапазоне для демонстрации поведения общего кэша, изменяются некоторые исходные значения, а затем выполняется обновление через ссылку на один кэш.
```javascript
const AsposeCells = require("aspose.cells");

// Создаём новую рабочую книгу и получаем доступ к первому рабочему листу
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

// Записываем строку заголовков: Fruit / Year / Amount
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// Записываем примерно 9 строк данных (виноград / черника / киви / вишня за 2020-2021 годы)
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

// Изменяем несколько значений Amount в исходных данных, чтобы имитировать изменение данных
worksheet.getCells().get("C2").putValue(150);
worksheet.getCells().get("C4").putValue(350);
worksheet.getCells().get("C7").putValue(650);

// Обновляем общий PivotCache.
// Поскольку Pivot1 и Pivot2 используют общий PivotCache, этот единственный вызов
// обновляет ОБЕ сводные таблицы (данные + стиль) из обновлённого источника.
pivotTable1.getPivotCache().refresh();

// Сохраняем рабочую книгу
workbook.save("output.xlsx");
```
### Изменились только представление/макет — используйте `CalculateData()`
Если исходные данные *не* изменились, но были изменены только параметры представления или макета сводной таблицы (например, поле было перемещено в другую область или переключён параметр обновления при открытии), нет необходимости повторно обращаться к источнику данных. Кэш уже содержит правильные данные; требуется только пересчёт отображаемой `PivotTable`. В этом случае правильным выбором является `pivotTable.CalculateData()`.
Это позволяет избежать ненужного обращения к источнику и значительно быстрее, когда многие сводные таблицы используют один и тот же кэш.
В следующем примере изменяется свойство сводной таблицы, не связанное с источником, а затем вызывается `CalculateData()` для её повторной визуализации из существующего кэша.
```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);

// Записать строку заголовков: Фрукт / Год / Сумма
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// Записать 8 строк данных (строки 2–9, соответствуют диапазону источника A1:C9)
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

// Добавить сводную таблицу с именем "Pivot1", расположенную в ячейке E3, с источником данных A1:C9
var pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Назначить поля: Fruit — в строки, Year — в столбцы, Amount — в данные
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, "Amount");

// Изменить свойство представления/макета — это изменение только для отображения,
// поэтому оно НЕ требует повторного чтения исходных данных через PivotCache.Refresh().
pivotTable.setRefreshDataOnOpeningFile(false);

// Метод CalculateData() заново отображает отображение ЭТОЙ сводной таблицы (данные + стиль)
// на основе данных, уже хранящихся в PivotCache. Поскольку исходные данные не изменились,
// обращения к источнику не происходит — пересчитываются только кэшированные значения
// в ячейках листа.
pivotTable.calculateData();

// Сохранить книгу на диск
workbook.save("output.xlsx");
```
## Получение всех сводных таблиц, использующих один и тот же PivotCache
Рабочая книга часто содержит множество сводных таблиц, которые все построены поверх одного общего кэша. Чтобы перечислить их — например, перед выполнением пакетного обновления или для диагностики влияния общего кэша — используйте `PivotCache.GetPivotTables()`. Этот метод возвращает коллекцию всех `PivotTable`, зависящих от данного кэша.
Это также самый прямой способ убедиться, что две сводные таблицы действительно используют один и тот же экземпляр `PivotCache`: вы можете сравнить ссылки на кэши или просто перебрать коллекцию, возвращаемую `GetPivotTables()`, и увидеть, какие сводные таблицы в ней присутствуют.
В следующем примере создаются две сводные таблицы на одном исходном диапазоне, проверяется, что они используют один и тот же экземпляр кэша, а затем перечисляются сводные таблицы этого кэша.
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
До Aspose.Cells for Node.js via C++ v26.7 стандартным способом обновления сводной таблицы был вызов `PivotTable.RefreshData()` для каждой сводной таблицы отдельно. Начиная с версии 26.7 этот метод помечен как **нерекомендуемый** и должен быть заменён описанными выше API, учитывающими кэш.
Есть две причины, по которым подход с вызовом `RefreshData()` для каждой таблицы по отдельности является проблематичным в реальных рабочих книгах:
- Он каждый раз заново извлекает данные из источника, даже если источник не изменился.
- Каждый вызов обновляет весь общий кэш. Когда многие сводные таблицы используют один кэш, повторные вызовы `RefreshData()` для каждой сводной таблицы приводят к многократному повторному извлечению одного и того же кэша, что очень медленно.
Рекомендуемые замены:
- **Обновить ВСЕ сводные таблицы в рабочей книге** → используйте `workbook.refreshAll();`
- **Обновить НЕКОТОРЫЕ из них** → используйте `pivotTable.PivotCache.Refresh();` для одного кэша. Поскольку кэш общий, этот единственный вызов обновляет каждую сводную таблицу, построенную поверх этого кэша. Другие сводные таблицы, которые используют уже обновлённый кэш, можно безопасно пропустить.
- **Изменились только параметры представления/макета сводной таблицы** → используйте `pivotTable.CalculateData();`, чтобы повторно отрисовать данные из существующего кэша без обращения к источнику.
В следующем примере демонстрируется новый эффективный шаблон для рабочих книг с несколькими сводными таблицами, использующими один общий кэш.
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
// Обе таблицы Pivot1 и Pivot2 используют ОДИН общий PivotCache.
// Это именно тот сценарий, в котором устаревший подход с RefreshData()
// для каждой таблицы становится неэффективным: обновление одной таблицы
// заново загружает весь общий кэш, поэтому обновление N таблиц выполняет
// ту же дорогостоящую загрузку N раз.
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
// pivotTable1.RefreshData();  // повторно загружает из источника, обновляет весь кэш
// pivotTable2.RefreshData();  // загружает СНОВА — кэш уже актуален!
// Каждый вызов перестраивает общий кэш, поэтому N таблиц = N избыточных загрузок.

// --- НОВЫЙ шаблон v26.7+: обновить кэш ОДИН раз, затем при необходимости перерисовывать ---
// Один вызов PivotCache.Refresh() подтягивает изменённые значения в общий
// кэш И пересчитывает отображение КАЖДОЙ сводной таблицы, которая на него ссылается.
// Поскольку Pivot1 и Pivot2 используют один PivotCache, этот единственный вызов
// обновляет обе таблицы — повторного обращения к источнику не требуется.
pivotTable1.getPivotCache().refresh();

// CalculateData() только перерисовывает отображение сводной таблицы (данные + стиль)
// на основе данных, уже хранящихся в кэше — он НЕ обращается к источнику.
// Мы вызываем его для Pivot2 здесь исключительно для демонстрации API: после того
// как кэш был обновлён один раз, любую зависимую таблицу можно перерисовать без
// повторного обращения к источнику. Используйте CalculateData() отдельно, когда
// изменились только параметры вида/макета сводной таблицы, а кэш уже актуален.
pivotTable2.calculateData();

workbook.save("output.xlsx");
```
## Какой API обновления мне следует использовать?
В таблице ниже приведены доступные API обновления и случаи, когда следует выбирать каждый из них.
| Цель | Рекомендуемый API | Примечания |
|------|-----------------|-------|
| Обновить всё в рабочей книге | `Workbook.RefreshAll()` | Один вызов; охватывает все кэши и таблицы. |
| Обновить только сводные таблицы на одном листе | `Worksheet.RefreshPivotTables()` | Ограничено одним рабочим листом. |
| Изменились исходные данные для одного кэша | `pivotTable.PivotCache.Refresh()` | Обновляет ВСЕ сводные таблицы на этом общем кэше. |
| Изменились только параметры представления/макета | `pivotTable.CalculateData()` | Пропускает ненужное обращение к источнику. |
| Получить список всех сводных таблиц на общем кэше | `pivotCache.GetPivotTables()` | Используйте для перечисления перед массовым обновлением. |
На практике отдавайте предпочтение API на основе кэша, а не устаревшему `RefreshData()` для каждой таблицы отдельно. Они учитывают общие кэши, избегают избыточных обращений к источнику и позволяют выбрать минимальную область, удовлетворяющую вашим требованиям к обновлению.
## Связанные статьи
- [Вставка изображения в ячейку](/cells/ru/nodejs-cpp/inserting-an-image-into-a-cell/)
- [Чтение и запись файлов DBF](/cells/ru/nodejs-cpp/dbf/)
- [Разделение файлов Excel на несколько файлов](/cells/ru/nodejs-cpp/splitting-excel-files-into-multiple-files/)
- [Спарклайны в Aspose.Cells for Node.js via C++](/cells/ru/nodejs-cpp/sparkline/)
{{< app/cells/assistant language="javascript" >}}
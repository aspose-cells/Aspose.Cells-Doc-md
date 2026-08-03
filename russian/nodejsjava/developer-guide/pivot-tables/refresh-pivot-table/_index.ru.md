---
title: Обновить сводные таблицы и кэши сводных таблиц в Aspose.Cells для Java
linktitle: Обновить сводные таблицы
description: Узнайте, как обновлять сводные таблицы в Aspose.Cells для Node.js via Java с помощью API обновления v26.7+. В этой статье рассматриваются RefreshAll, RefreshPivotTables, PivotCache.refresh, calculateData и getPivotTables с практическими примерами кода.
keywords: Aspose.Cells, Node.js via Java, сводная таблица, обновление, PivotCache, calculateData, RefreshAll, RefreshPivotTables, getPivotTables, v26.7
type: docs
weight: 200
url: /ru/nodejs-java/refresh-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---


{{% alert color="primary" %}}

Aspose.Cells предоставляет многоуровневый API обновления, который позволяет перезагружать данные сводных таблиц на четырёх различных уровнях — от всей рабочей книги до отдельной сводной таблицы. Начиная с **Aspose.Cells for Node.js via Java v26.7**, устаревший метод `PivotTable.RefreshData()` помечен как obsolete и должен быть заменён более эффективными API с поддержкой кэша, описанными в этой статье.

{{% /alert %}}

## Введение

Обновление сводной таблицы редко представляет собой одну операцию. Под капотом Aspose.Cells поддерживает многоуровневую цепочку данных, которая связывает исходные данные с отображаемыми значениями, которые вы видите на рабочем листе. Понимание этой цепочки является ключом к выбору правильного API обновления для любой ситуации.

Четырёхуровневая цепочка данных выглядит следующим образом:

1. **Источник данных** — исходные диапазоны рабочего листа, запрос к базе данных или диапазон консолидации, где хранятся необработанные значения.
2. **PivotCache** — снимок исходных данных в памяти. Каждая сводная таблица строится поверх `PivotCache`; именно здесь собираются и агрегируются все данные.
3. **PivotTable** — объект представления, который определяет поля строк, столбцов, значений и фильтров. `PivotTable` считывает данные *только* из своего `PivotCache`, но никогда напрямую из источника данных.
4. **Cells** — `Cells` рабочего листа, в которые `PivotTable` отображает вычисленные значения и стили.

Особенно важным понятием является **общий кэш**. Когда несколько сводных таблиц в рабочей книге ссылаются на один и тот же исходный диапазон, они совместно используют *один* экземпляр `PivotCache`. На один `PivotCache` могут ссылаться многие сводные таблицы, и обновление этого кэша обновляет сразу все зависимые `PivotTable`.

{{% alert color="primary" %}}

`PivotCache.SourceType` (перечисление `PivotTableSourceType`) указывает, откуда были получены данные кэша. Начиная с версии v26.7, `PivotCache.Refresh()` поддерживает только источники типов **`Sheet`** и **`Consolidation`** — то есть данные, расположенные в диапазонах рабочих листов. Внешние источники (базы данных, внешние подключения и т. д.) пока не могут быть обновлены через API кэша.

{{% /alert %}}

Из-за этой цепочки в Aspose.Cells существуют два основных пути обновления:

- **`PivotCache.Refresh()`** — перезагружает данные источника в кэш И пересчитывает все зависимые `PivotTable` за одну операцию.
- **`PivotTable.CalculateData()`** — пересчитывает отображение одной `PivotTable` из уже кэшированных данных, без обращения к источнику данных.

Все сценарии в этой статье используют данные источника из ячеек рабочего листа, поэтому тип источника — `Sheet`, и операции обновления работают так, как описано.


## Быстрый старт

Если вам нужен самый короткий код для обновления каждой сводной таблицы в книге, достаточно одного вызова:

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook("input.xlsx");
workbook.refreshAll();
workbook.save("output.xlsx");
```

В остальной части этой статьи объясняется, когда следует выбрать более узкий API.

## Необходимые импорты

Все примеры JavaScript в этой статье требуют модуль Aspose.Cells for Node.js via Java. Типы сводных таблиц находятся в пространстве имён `Aspose.Cells.Pivot`, которое является частью того же модуля:

- `const aspose = require('aspose.cells');`
- Или для конкретных импортов: `const { Workbook, Cells, PivotTableSourceType } = require('aspose.cells');`

## Обновление всех сводных таблиц в рабочей книге

Когда необходимо обеспечить, чтобы каждый кэш сводной таблицы и каждая сводная таблица в рабочей книге отражали самые последние исходные данные, самым простым и комплексным API является `Workbook.RefreshAll()`. Один вызов проходит по всей рабочей книге — обновляя каждый `PivotCache` из его источника и затем пересчитывая каждую зависимую `PivotTable`. Это рекомендуемый подход для общих полных обновлений документа, когда производительность не является проблемой.

В следующем примере создаётся рабочая книга с исходным диапазоном Fruit/Year/Amount, создаётся одна сводная таблица, изменяются некоторые значения источника, а затем используется `RefreshAll()` для обновления всего за один вызов.

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

// Обновить каждую сводную таблицу / кэш сводной таблицы в рабочей книге
workbook.refreshAll();

// Сохранить рабочую книгу
workbook.save("output.xlsx");
```

## Обновление всех сводных таблиц на одном рабочем листе

Иногда необходимо обновить только сводные таблицы, расположенные на одном конкретном рабочем листе — например, когда известно, что сводные таблицы на других рабочих листах не связаны с ними и не должны затрагиваться. Для этого случая Aspose.Cells предоставляет `Worksheet.RefreshPivotTables()`, область действия которого ограничена одним экземпляром `Worksheet`.

Это более выборочно по сравнению с `Workbook.RefreshAll()`: обновляются только сводные таблицы на целевом рабочем листе, а сводные таблицы на других рабочих листах остаются нетронутыми.

В следующем примере заполняются те же исходные данные Fruit/Year/Amount, добавляется сводная таблица на первом рабочем листе, изменяются некоторые значения источника, а затем обновляются только сводные таблицы на этом рабочем листе.

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

Если требуется детальный контроль над одной сводной таблицей, API на основе кэша предоставляет два варианта. Выбор между ними зависит от того, что именно изменилось: исходные данные или только параметры представления/макета самой сводной таблицы.

### Изменились исходные данные — используйте `PivotCache.Refresh()`

Если изменились исходные данные, правильной точкой входа является `pivotTable.PivotCache.Refresh()`. Этот вызов перечитывает исходные данные в кэш, а затем пересчитывает каждую `PivotTable`, зависящую от этого кэша.

{{% alert color="primary" %}}

Поскольку сводные таблицы совместно используют один экземпляр `PivotCache`, вызов `PivotCache.Refresh()` пересчитывает **все** сводные таблицы, построенные на этом же кэше, — а не только ту, на которую вы ссылаетесь. Если две сводные таблицы совместно используют один и тот же исходный диапазон, обновление одного кэша обновляет обе.

{{% /alert %}}

В следующем примере создаются две сводные таблицы на одном и том же исходном диапазоне для демонстрации поведения общего кэша, изменяются некоторые значения источника, а затем выполняется обновление через ссылку на один кэш.

```javascript
const AsposeCells = require("aspose.cells");

// Создаём новую книгу и получаем доступ к первому листу
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

// Записываем строку заголовков: Фрукт / Год / Количество
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
// Pivot1 и Pivot2 используют общий PivotCache, так как исходный диапазон идентичен.
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

// Сохраняем книгу
workbook.save("output.xlsx");
```

### Изменились только параметры представления/макета — используйте `CalculateData()`

Если исходные данные *не* изменились, а изменились только параметры представления или макета сводной таблицы (например, поле было перемещено в другую область или переключён параметр обновления при открытии), нет необходимости обращаться обратно к источнику данных. Кэш уже содержит правильные данные; необходимо только пересчитать отображаемую `PivotTable`. В этом случае `pivotTable.CalculateData()` является правильным выбором.

Это позволяет избежать ненужного обращения к источнику и значительно быстрее, когда многие сводные таблицы совместно используют один и тот же кэш.

В следующем примере изменяется свойство сводной таблицы, не связанное с источником, а затем вызывается `CalculateData()` для её повторного отображения из существующего кэша.

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);

// Запись строки заголовков Fruit / Year / Amount
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// Запись 8 строк данных (строки 2-9, соответствуют исходному диапазону A1:C9)
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

// Добавление сводной таблицы с именем "Pivot1", расположенной в ячейке назначения E3, с источником данных из диапазона A1:C9
var pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Назначение полей: Fruit в строки, Year в столбцы, Amount в данные
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Изменение свойства представления/макета — это изменение только для отображения,
// поэтому оно НЕ требует повторного чтения исходных данных через PivotCache.Refresh().
pivotTable.setRefreshDataOnOpeningFile(false);

// CalculateData() повторно отрисовывает отображение ДАННОЙ сводной таблицы (данные + стиль) на основе
// данных, уже хранящихся в PivotCache. Поскольку исходные данные не изменились,
// обращение к источнику не выполняется — пересчитываются только кэшированные значения
// в ячейках листа.
pivotTable.calculateData();

// Сохранение книги на диск
workbook.save("output.xlsx");
```

## Получение всех сводных таблиц, использующих один и тот же PivotCache

Рабочая книга часто содержит много сводных таблиц, которые все расположены поверх одного общего кэша. Чтобы перечислить их — например, перед выполнением пакетного обновления или для диагностики влияния общего кэша — используйте `PivotCache.GetPivotTables()`. Этот метод возвращает коллекцию всех `PivotTable`, зависящих от данного кэша.

Это также самый прямой способ убедиться, что две сводные таблицы действительно совместно используют один и тот же экземпляр `PivotCache` — можно сравнить ссылки на кэш или просто перебрать коллекцию, возвращённую `GetPivotTables()`, и увидеть, какие сводные таблицы в ней присутствуют.

В следующем примере создаются две сводные таблицы на одном и том же исходном диапазоне, проверяется, что они совместно используют один и тот же экземпляр кэша, а затем перечисляются сводные таблицы этого кэша.


## Миграция с устаревшего `PivotTable.RefreshData()`

До Aspose.Cells for Node.js via Java v26.7 стандартным способом обновления сводной таблицы был вызов `PivotTable.RefreshData()` для каждой сводной таблицы отдельно. Начиная с версии v26.7 этот метод помечен как **obsolete** и должен быть заменён описанными выше API с поддержкой кэша.

Есть две причины, по которым подход с `RefreshData()` для каждой таблицы отдельно является проблематичным в реальных рабочих книгах:

- Он повторно извлекает данные из источника *при каждом* вызове, даже когда источник не изменился.
- Каждый вызов обновляет весь общий кэш. Когда многие сводные таблицы совместно используют один кэш, повторный вызов `RefreshData()` для каждой сводной таблицы приводит к многократному повторному извлечению одного и того же кэша, что выполняется очень медленно.

Рекомендуемые замены:

- **Обновить ВСЕ сводные таблицы в рабочей книге** → используйте `workbook.refreshAll();`
- **Обновить НЕКОТОРЫЕ из них** → используйте `pivotTable.getPivotCache().refresh();` для одного кэша. Поскольку кэш является общим, этот единственный вызов обновляет каждую сводную таблицу, построенную поверх этого кэша. Другие сводные таблицы, которые расположены на уже обновлённом кэше, можно безопасно пропустить.
- **Изменились только параметры представления/макета сводной таблицы** → используйте `pivotTable.calculateData();` для повторного отображения из существующего кэша без обращения к источнику.

В следующем примере демонстрируется новый эффективный шаблон для рабочих книг с несколькими сводными таблицами, использующими один общий кэш.

```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// --- Формирование исходных данных: Фрукт / Год / Сумма (заголовок + 9 строк) ---
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

// --- Добавление первой сводной таблицы (Pivot1) в ячейку E3 ---
let idx1 = sheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable1 = sheet.getPivotTables().get(idx1);
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// --- Добавление ВТОРОЙ сводной таблицы (Pivot2) на тот же диапазон источника ---
// Pivot1 и Pivot2 используют ОДИН общий PivotCache.
// Именно в этом сценарии устаревший подход с RefreshData() для каждой таблицы
// становится неэффективным: обновление одной таблицы повторно загружает весь
// общий кеш, поэтому обновление N таблиц выполняет одно и то же дорогостоящее
// извлечение данных N раз.
let idx2 = sheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
let pivotTable2 = sheet.getPivotTables().get(idx2);
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// --- Изменение нескольких значений Amount в исходных данных ---
sheet.getCells().get("C2").putValue(5000);   // Виноград 2020
sheet.getCells().get("C5").putValue(7500);   // Вишня    2020
sheet.getCells().get("C9").putValue(9500);   // Вишня    2021

// --- УСТАРЕВШИЙ шаблон (до версии 26.7) — PivotTable.RefreshData() ---
// pivotTable1.refreshData();  // повторно извлекает данные из источника, обновляет весь кеш
// pivotTable2.refreshData();  // повторно извлекает данные СНОВА — кеш уже актуален!
// Каждый вызов перестраивает общий кеш, поэтому N таблиц = N избыточных извлечений.

// --- НОВЫЙ шаблон версии 26.7+: обновить кеш ОДИН раз, затем при необходимости перерисовать ---
// Один вызов PivotCache.Refresh() подтягивает изменённые значения в общий
// кеш И пересчитывает отображение КАЖДОЙ сводной таблицы, которая на него ссылается.
// Поскольку Pivot1 и Pivot2 используют один PivotCache, этот единственный вызов
// обновляет обе таблицы — повторного обращения к источнику не требуется.
pivotTable1.getPivotCache().refresh();

// Метод CalculateData() только перерисовывает отображение сводной таблицы (данные + стиль)
// на основе данных, уже содержащихся в кеше — он НЕ обращается к источнику.
// Мы вызываем его на Pivot2 здесь исключительно для демонстрации API: после того как
// кеш был однократно обновлён, любую зависимую таблицу можно перерисовать без
// повторного обращения к источнику. Используйте CalculateData() отдельно, когда
// изменились только параметры представления/макета сводной таблицы, а кеш актуален.
pivotTable2.calculateData();

workbook.save("output.xlsx");
```

## Какой API обновления следует использовать?

В таблице ниже приведены доступные API обновления и случаи, когда следует выбирать каждый из них.

| Цель | Рекомендуемый API | Примечания |
|------|-------------------|------------|
| Обновить всё в рабочей книге | `Workbook.RefreshAll()` | Один вызов, охватывает все кэши и таблицы. |
| Обновить только сводные таблицы на одном листе | `Worksheet.RefreshPivotTables()` | Область действия ограничена одним рабочим листом. |
| Изменились исходные данные для одного кэша | `pivotTable.PivotCache.Refresh()` | Обновляет ВСЕ сводные таблицы на этом общем кэше. |
| Изменились только параметры представления/макета | `pivotTable.CalculateData()` | Пропускает ненужное обращение к источнику. |
| Получить список всех сводных таблиц на общем кэше | `pivotCache.GetPivotTables()` | Используйте для перечисления перед массовым обновлением. |

На практике отдавайте предпочтение API на основе кэша, а не устаревшему `RefreshData()` для каждой таблицы отдельно. Они учитывают общие кэши, избегают избыточных обращений к источнику и позволяют выбрать наименьшую область действия, удовлетворяющую вашим требованиям к обновлению.

{{< app/cells/assistant language="nodejs-java" >}}

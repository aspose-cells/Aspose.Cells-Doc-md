---
title: Обновление сводных таблиц
linktitle: Обновление сводных таблиц
description: Узнайте, как обновлять сводные таблицы в Aspose.Cells for Node.js via C++ с использованием API обновления сводных таблиц версии 26.7+, В этой статье рассматриваются RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData и GetPivotTables с практическими примерами кода.
keywords: Aspose.Cells, Node.js via C++, сводная таблица, обновление, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ru/nodejs-cpp/refresh-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells предоставляет многоуровневый API обновления, который позволяет перезагружать данные сводных таблиц на четырёх различных уровнях — от всей рабочей книги до одной сводной таблицы. Начиная с версии **Aspose.Cells for Node.js via C++ v26.7**, устаревший метод `PivotTable.RefreshData()` считается нерекомендуемым и должен быть заменён более эффективными API, учитывающими кэш, описанными в этой статье.
{{% /alert %}}

## Введение
Обновление сводной таблицы редко представляет собой одну операцию. За кулисами Aspose.Cells поддерживает многоуровневую цепочку данных, которая связывает исходные данные с отображаемыми значениями, которые вы видите на рабочем листе. Понимание этой цепочки является ключом к выбору правильного API обновления для любой ситуации.
Четырёхуровневая цепочка данных выглядит следующим образом:
1. **Источник данных** — исходные диапазоны рабочего листа, запрос к базе данных или диапазон консолидации, где хранятся необработанные значения.
2. **PivotCache** — моментальный снимок исходных данных в памяти. Каждая сводная таблица построена поверх `PivotCache`; именно здесь собираются и агрегируются все данные.
3. **Сводная таблица** — объект представления, который определяет поля строк, столбцов, значений и фильтров. Сводная таблица читает данные *только* из своего `PivotCache`, никогда напрямую из источника данных.
4. **Cells** — коллекция `Cells` рабочего листа, в которую сводная таблица отображает вычисленные значения и стили.

{{% alert color="primary" %}}
`PivotCache.SourceType` (перечисление `PivotTableSourceType`) указывает, откуда поступили данные кэша. Начиная с версии 26.7, `PivotCache.Refresh()` поддерживает только типы источников **`Sheet`** и **`Consolidation`** — то есть данные, которые находятся в диапазонах рабочего листа. Внешние источники (базы данных, внешние подключения и т.д.) пока не могут быть обновлены через API кэша.
{{% /alert %}}

Из-за этой цепочки в Aspose.Cells существуют два основных пути обновления:
- **`PivotTable.CalculateData()`** — пересчитывает отображение одной сводной таблицы из уже кэшированных данных без обращения к источнику данных.
Все сценарии в этой статье используют данные из ячеек рабочего листа в качестве источника, поэтому тип источника — `Sheet`, и операции обновления работают, как описано.

## Быстрый старт
Если вам нужен только максимально короткий код, который обновляет все сводные таблицы в рабочей книге, достаточно одного вызова:

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
// Добавить сводную таблицу: исходный диапазон "A1:C9", целевая ячейка "E3", имя "Pivot1"
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

Вся остальная часть статьи объясняет, когда вместо этого следует выбрать более узкий API.

## Необходимые импорты
Все примеры JavaScript в этой статье предполагают, что модуль Aspose.Cells for Node.js via C++ загружен, а типы сводных таблиц находятся в пространстве имён `Aspose.Cells.Pivot`. Типичная настройка выглядит так:
- `const AsposeCells = require("aspose.cells.node");`
- `const { PivotFieldType } = AsposeCells;` (или доступ через `AsposeCells.Pivot.PivotFieldType`)

## Обновление всех сводных таблиц в рабочей книге
Если вам нужно убедиться, что каждый кэш сводной таблицы и каждая сводная таблица в рабочей книге отражают последние исходные данные, самый простой и всеобъемлющий API — `Workbook.RefreshAll()`. Одним вызовом он обходит всю рабочую книгу — обновляет каждый `PivotCache` из его источника, а затем пересчитывает каждую зависимую сводную таблицу. Это рекомендуемый подход для общих полных обновлений документа, когда производительность не вызывает беспокойства.
В следующем примере создаётся рабочая книга с исходным диапазоном Фрукт/Год/Сумма, создаётся одна сводная таблица, изменяются некоторые исходные значения, а затем используется `RefreshAll()` для обновления всего одним вызовом.

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

## Обновление всех сводных таблиц на одном рабочем листе
Иногда вам нужно обновить только сводные таблицы, которые находятся на одном конкретном рабочем листе — например, когда известно, что сводные таблицы на других рабочих листах не связаны и их не следует трогать. Для этого случая Aspose.Cells предоставляет метод `Worksheet.RefreshPivotTables()`, который применяется к одному экземпляру `Worksheet`.

## Обновление одной сводной таблицы
Если вам нужен детальный контроль над одной сводной таблицей, API на основе кэша предоставляет два варианта. Выбор между ними зависит от того, что именно изменилось: базовые исходные данные или только параметры представления/макета самой сводной таблицы.

### Изменились исходные данные — используйте `PivotCache.Refresh()`
Если базовые исходные данные изменились, правильной точкой входа является `pivotTable.PivotCache.Refresh()`. Этот вызов перечитывает исходные данные в кэш, а затем пересчитывает каждую сводную таблицу, зависящую от этого кэша.

### Изменились только представление/макет — используйте `CalculateData()`
Если исходные данные *не* изменились, но были изменены только параметры представления или макета сводной таблицы (например, поле было перемещено в другую область или переключён параметр обновления при открытии), нет необходимости обращаться к источнику данных. В кэше уже находятся правильные данные; пересчёта требует только отображаемая сводная таблица. В этом случае `pivotTable.CalculateData()` является правильным выбором.
В следующем примере изменяется свойство сводной таблицы, не связанное с источником, а затем вызывается `CalculateData()` для повторного отображения из существующего кэша.
Рабочая книга часто содержит множество сводных таблиц, которые все построены поверх одного общего кэша. Чтобы перечислить их — например, перед выполнением пакетного обновления или для диагностики влияния общего кэша — используйте `PivotCache.GetPivotTables()`. Этот метод возвращает коллекцию каждой сводной таблицы, зависящей от данного кэша.

## Миграция с устаревшего `PivotTable.RefreshData()`
До версии Aspose.Cells for Node.js via C++ v26.7 стандартным способом обновления сводной таблицы был вызов `PivotTable.RefreshData()` на каждой сводной таблице по отдельности. Начиная с версии 26.7 этот метод считается **устаревшим** и должен быть заменён API, учитывающими кэш, описанными выше.
Существуют две причины, по которым подход с `RefreshData()` для каждой таблицы является проблематичным в реальных рабочих книгах:
- Он повторно извлекает данные из источника *при каждом* вызове, даже когда источник не изменился.
Рекомендуемые замены:
В следующем примере демонстрируется новый эффективный шаблон для рабочих книг с несколькими сводными таблицами, использующими один кэш.

## Какой API обновления следует использовать?
В таблице ниже приведены доступные API обновления и случаи, когда следует выбирать каждый из них.
| Цель | Рекомендуемый API | Примечания |
|------|------------------|------------|
| Обновить всё в рабочей книге | `Workbook.RefreshAll()` | Один вызов; охватывает все кэши и таблицы. |
| Обновить только сводные таблицы на одном листе | `Worksheet.RefreshPivotTables()` | Ограничено одним рабочим листом. |
| Исходные данные изменились для одного кэша | `pivotTable.PivotCache.Refresh()` | Обновляет ВСЕ сводные таблицы, использующие этот общий кэш. |
| Изменились только параметры представления/макета | `pivotTable.CalculateData()` | Пропускает ненужное обращение к источнику. |
| Получить список всех сводных таблиц на общем кэше | `pivotCache.GetPivotTables()` | Используйте для перечисления перед массовым обновлением. |
На практике предпочтительнее использовать API на основе кэша вместо устаревшего `RefreshData()` для каждой таблицы. Они учитывают общие кэши, избегают избыточных обращений к источнику и позволяют выбрать наименьшую область, удовлетворяющую вашим требованиям к обновлению.

## Распространённые ошибки
- **Забыли обновить перед сохранением.** Сводная таблица записывает свои отображаемые значения на рабочий лист только после обновления цепочки данных. Если вы изменяете ячейки источника, вызовите `PivotCache.Refresh()` (или `Workbook.RefreshAll()`) перед `Workbook.save()`, иначе сохранённый файл всё ещё будет содержать старые агрегированные значения.
- **Вызов устаревшего `RefreshData()` для каждой таблицы.** В версии 26.7 метод `PivotTable.RefreshData()` считается устаревшим и повторно извлекает данные из источника при каждом вызове. При наличии нескольких сводных таблиц, использующих общий кэш, это приводит к N избыточным извлечениям данных. Замените его одним вызовом `PivotCache.Refresh()` с последующим `CalculateData()` для каждой таблицы.
- **Обновление при изменении только макета.** Если вы изменили только представление сводной таблицы (порядок столбцов, `ConsolidationFunction` и т.д.) без изменения исходных данных, вызов `PivotCache.Refresh()` не нужен и замедляет работу. Вызовите `pivotTable.CalculateData()` для повторного отображения из существующего кэша.
- **Внешний источник не поддерживается `PivotCache.Refresh()`.** Если источник сводной таблицы поступает из внешнего подключения (база данных, OLAP-куб и т.д.), `PivotCache.Refresh()` не может его обновить в версии 26.7 — в настоящее время поддерживаются только типы источников `Sheet` и `Consolidation`. Для внешних источников откройте рабочую книгу заново или перестройте кэш из источника.

```csharp
using Aspose.Cells;
Workbook workbook = new Workbook("input.xlsx");
workbook.RefreshAll();
workbook.Save("output.xlsx");
```

```javascript
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
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, "Amount");
// Modify a view/layout property — this is a presentation-only change,
// so it does NOT require re-reading the source data through PivotCache.Refresh().
pivotTable.setRefreshDataOnOpeningFile(false);
// CalculateData() re-renders THIS pivot table's display (data + style) from the
// data already held in the PivotCache. Because the source data did not change,
// no round-trip to the source is performed — only the cached values are recalculated
// into worksheet cells.
pivotTable.calculateData();
// Save the workbook to disk
workbook.save("output.xlsx");
```

{{< app/cells/assistant language="nodejs-cpp" >}}
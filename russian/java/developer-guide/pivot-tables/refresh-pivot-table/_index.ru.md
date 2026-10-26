---
title: Обновление сводных таблиц и кэшей сводных таблиц в Aspose.Cells for Java
linktitle: Обновление сводных таблиц и кэшей сводных таблиц в Aspose.Cells for Java
description: Узнайте, как обновлять сводные таблицы в Aspose.Cells for Java с помощью API обновления сводных таблиц v26.7+. В этой статье рассматриваются refreshAll, refreshPivotTables, PivotCache.refresh, calculateData и getPivotTables с практическими примерами кода.
keywords: Aspose.Cells, Java, сводная таблица, обновление, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ru/java/refresh-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells предоставляет многоуровневый API обновления, который позволяет перезагружать данные сводных таблиц на четырех разных уровнях — от всей рабочей книги до отдельной сводной таблицы. Начиная с **Aspose.Cells for Java v26.7**, прежний метод `PivotTable.refreshData()` помечен как устаревший и должен быть заменен более эффективными API, учитывающими кэш, которые описаны в этой статье.
{{% /alert %}}

## Introduction
Обновление сводной таблицы редко представляет собой одну операцию. Внутренне Aspose.Cells поддерживает многоуровневую цепочку данных, связывающую исходные данные с отображаемыми значениями, которые видны на рабочем листе. Понимание этой цепочки — ключ к выбору подходящего API обновления в любой ситуации.
Цепочка данных состоит из четырех уровней:
1. **Источник данных** — исходные диапазоны рабочих листов, запрос к базе данных или диапазон консолидации, в которых хранятся необработанные значения.
2. **PivotCache** — снимок исходных данных в памяти. Каждая сводная таблица строится поверх `PivotCache`; именно здесь все данные собираются и агрегируются.
3. **PivotTable** — объект представления, определяющий поля строк, столбцов, значений и фильтров. `PivotTable` читает данные *только* из своего `PivotCache`, а не напрямую из источника данных.
4. **Cells** — ячейки `Cells` рабочего листа, в которые `PivotTable` отрисовывает вычисленные значения и стили.

{{% alert color="primary" %}}
`PivotCache.getSourceType()` (перечисление `PivotTableSourceType`) указывает, откуда получены данные кэша. Начиная с v26.7, `PivotCache.refresh()` поддерживает только типы источников **`Sheet`** и **`Consolidation`** — то есть данные, находящиеся в диапазонах рабочих листов. Внешние источники (базы данных, внешние подключения и т. д.) пока нельзя обновить через API кэша.
Из-за этой цепочки в Aspose.Cells существуют два основных пути обновления:
- **`PivotTable.calculateData()`** — пересчитывает отображение одного `PivotTable` по уже кэшированным данным, без обратного обращения к источнику данных.
Все сценарии в этой статье используют данные из ячеек рабочего листа, поэтому тип источника — `Sheet`, а операции обновления выполняются следующим образом.
{{% /alert %}}

## Quick Start
Если требуется только кратчайший код для обновления всех сводных таблиц в рабочей книге, достаточно одного вызова:

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("input.xlsx");
workbook.refreshAll();
workbook.save("output.xlsx");
```

В остальной части статьи объясняется, когда следует выбрать более узкий API.

## Required Import Statements
Все примеры на Java в этой статье начинаются со следующих инструкций импорта, поскольку связанные со сводными таблицами типы находятся в пакете `com.aspose.cells.pivot`:
- `import java.lang.System;`
- `import com.aspose.cells.Workbook;`
- `import com.aspose.cells.pivot.*;`

## Refresh All Pivot Tables in the Workbook
Если необходимо убедиться, чтобы каждый кэш и каждая сводная таблица в рабочей книге отражали последние данные источника, используйте API `Workbook.refreshAll()`. Один вызов обрабатывает всю рабочую книгу — обновляет каждый `PivotCache` из его источника, а затем пересчитывает каждую зависимую `PivotTable`. Это рекомендуемый подход для полного обновления документа, когда производительность не критична.
В следующем примере создается рабочая книга с диапазоном источника `Fruit/Year/Amount`, создается одна сводная таблица, изменяются некоторые исходные значения, после чего `refreshAll()` актуализирует все данные одним вызовом.

```java
import com.aspose.cells.*;
// Create a new workbook
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
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
// Add a pivot table: source range "A1:C9", destination cell "E3"
PivotTable pivotTable = worksheet.getPivotTables().add("A1:C9", 2, 4);
// Assign pivot fields: Fruit to Rows, Year to Columns, Amount to Data
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
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
Иногда требуется обновить только сводные таблицы на одном конкретном рабочем листе — например, если известно, что сводные таблицы на других листах не связаны с обновляемыми данными и их не следует затрагивать. Для этого Aspose.Cells предоставляет `Worksheet.refreshPivotTables()`, который действует в пределах одного экземпляра `Worksheet`.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
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
PivotTable pivotTable = worksheet.getPivotTables().add("A1:C9", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
worksheet.getCells().get("C2").putValue(300);
worksheet.getCells().get("C5").putValue(250);
worksheet.getCells().get("C9").putValue(400);
worksheet.refreshPivotTables();
workbook.save("output.xlsx");
```

## Refresh a Single Pivot Table
Если требуется детальный контроль над одной сводной таблицей, API на основе кэша предоставляет два варианта. Выбор зависит от того, что именно изменилось: исходные данные или только настройки представления или макета самой сводной таблицы.

### Source Data Changed — Use `PivotCache.refresh()`
Если изменились исходные данные, правильной точкой входа является `pivotTable.getPivotCache().refresh()`. Этот вызов повторно считывает исходные данные в кэш, а затем пересчитывает каждую `PivotTable`, зависящую от этого кэша.

### Only View/Layout Changed — Use `calculateData()`
Если исходные данные *не* изменились, а были изменены только настройки представления или макета сводной таблицы (например, поле перемещено в другую область или переключен параметр обновления при открытии), возвращаться к источнику данных не требуется. В кэше уже хранятся правильные данные; необходимо пересчитать только отображаемую `PivotTable`. В этом случае следует использовать `pivotTable.calculateData()`.
В следующем примере изменяется свойство сводной таблицы, не относящееся к источнику, а затем вызывается `calculateData()` для повторной отрисовки из существующего кэша.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
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
// Add a pivot table placed at destination cell E3, sourcing from A1:C9
PivotTable pivotTable = worksheet.getPivotTables().add("A1:C9", 2, 4);
// Assign fields: Fruit to Row, Year to Column, Amount to Data
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// Modify a view/layout property -- this is a presentation-only change,
// so it does NOT require re-reading the source data through PivotCache.refresh().
pivotTable.setRefreshDataOnOpeningFile(false);
// calculateData() re-renders THIS pivot table's display (data + style) from the
// data already held in the PivotCache. Because the source data did not change,
// no round-trip to the source is performed -- only the cached values are recalculated
// into worksheet cells.
pivotTable.calculateData();
// Save the workbook to disk
workbook.save("output.xlsx");
```

В рабочей книге часто имеется несколько сводных таблиц, построенных поверх одного общего кэша. Чтобы перечислить их — например, перед массовым обновлением или для диагностики влияния общего кэша, — используйте `PivotCache.getPivotTables()`. Этот метод возвращает коллекцию всех `PivotTable`, зависящих от указанного кэша.

## Migrating from the Obsolete `PivotTable.refreshData()`
До Aspose.Cells for Java v26.7 стандартным способом обновления сводной таблицы был вызов `PivotTable.refreshData()` для каждой сводной таблицы отдельно. Начиная с v26.7, этот метод помечен **устаревшим** и должен быть заменен API, учитывающими кэш, которые описаны выше.
Подход с обновлением каждой таблицы отдельно создает две проблемы в реальных рабочих книгах:
- Он каждый раз повторно получает данные из источника, даже если источник не изменился.
Рекомендуемые замены:
В следующем примере демонстрируется новый эффективный подход для рабочих книг с несколькими сводными таблицами, использующими один кэш.

## Which Refresh API Should I Use?
В таблице ниже представлены доступные API обновления и рекомендации по выбору каждого из них.
| Цель | Рекомендуемый API | Примечания |
|------|-----------------|-------|
| Обновить все данные в рабочей книге | `Workbook.refreshAll()` | Один вызов; охватывает все кэши и таблицы. |
| Обновить только сводные таблицы на одном листе | `Worksheet.refreshPivotTables()` | Ограничивается одним рабочим листом. |
| Исходные данные изменились для одного кэша | `pivotTable.getPivotCache().refresh()` | Обновляет ВСЕ сводные таблицы, связанные с этим общим кэшем. |
| Изменились только настройки представления или макета | `pivotTable.calculateData()` | Исключает ненужное повторное обращение к источнику. |
| Перечислить все сводные таблицы для общего кэша | `pivotCache.getPivotTables()` | Используйте для перечисления перед массовым обновлением. |
На практике предпочитайте API, основанные на кэше, устаревшему подходу с вызовом `refreshData()` для каждой таблицы. Такие API учитывают общие кэши, исключают избыточные обращения к источнику и позволяют выбрать минимальный объем обновления, соответствующий вашим требованиям.

## Common Pitfalls
- **Забыли обновить данные перед сохранением.** Сводная таблица записывает вычисленные значения на рабочий лист только после обновления цепочки данных. Если исходные ячейки изменены, вызовите `PivotCache.refresh()` (или `Workbook.refreshAll()`) перед `Workbook.save()`, иначе сохраненный файл по-прежнему будет содержать старые агрегированные значения.
- **Вызов устаревшего `refreshData()` для каждой таблицы.** В v26.7 метод `PivotTable.refreshData()` помечен как устаревший и при каждом вызове повторно получает данные из источника. Если несколько сводных таблиц используют общий кэш, это означает N избыточных обращений к источнику. Замените его одним вызовом `PivotCache.refresh()`, после чего вызовите `calculateData()` для каждой таблицы.
- **Обновление, когда изменился только макет.** Если изменено только представление сводной таблицы (порядок столбцов, `ConsolidationFunction` и т. д.), но исходные данные не затронуты, `PivotCache.refresh()` не нужен и работает медленно. Вызовите `pivotTable.calculateData()`, чтобы повторно отрисовать таблицу из существующего кэша.
- **Внешний источник не поддерживается `PivotCache.refresh()`.** Если источник сводной таблицы берется из внешнего подключения (база данных, OLAP-куб и т. д.), `PivotCache.refresh()` не может обновить его в v26.7 — сейчас этот метод поддерживает только типы источников `Sheet` и `Consolidation`. Для внешних источников повторно откройте рабочую книгу или перестройте кэш из источника.

{{< app/cells/assistant language="java" >}}
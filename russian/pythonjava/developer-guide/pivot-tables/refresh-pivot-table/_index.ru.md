---
title: Обновление сводных таблиц и кэшей в Aspose.Cells for Python via Java
linktitle: Обновление сводных таблиц и кэшей в Aspose.Cells for Python via Java
description: Узнайте, как обновлять сводные таблицы в Aspose.Cells for Python via Java с использованием API обновления сводных таблиц версии v26.7+. В этой статье рассматриваются RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData и GetPivotTables с практическими примерами кода.
keywords: Aspose.Cells, Python via Java, сводная таблица, обновление, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ru/python-java/refresh-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells предоставляет многоуровневый API обновления, который позволяет перезагружать данные сводных таблиц на четырёх различных уровнях — от всей рабочей книги до отдельной сводной таблицы. Начиная с **Aspose.Cells for Python via Java v26.7**, устаревший метод `PivotTable.refreshData()` помечен как нерекомендуемый и должен быть заменён более эффективными API, учитывающими кэш, которые описаны в этой статье.
{{% /alert %}}

## Introduction
Обновление сводной таблицы редко представляет собой одну операцию. За кулисами Aspose.Cells поддерживает многоуровневую цепочку данных, которая связывает исходные данные с отображаемыми значениями, которые вы видите на рабочем листе. Понимание этой цепочки является ключом к выбору правильного API обновления для любой ситуации.
Цепочка данных состоит из четырёх уровней:
1. **Источник данных** — исходные диапазоны рабочего листа, запрос к базе данных или диапазон консолидации, где хранятся исходные значения.
2. **PivotCache** — снимок исходных данных в памяти. Каждая сводная таблица построена поверх `PivotCache`; именно здесь все данные собираются и агрегируются.
3. **Сводная таблица** — объект представления, который определяет поля строк, столбцов, значений и фильтров. `Сводная таблица` читает данные *только* из своего `PivotCache`, никогда напрямую из источника данных.
4. **Ячейки** — `Cells` рабочего листа, в которые `Сводная таблица` выводит вычисленные значения и стили.

{{% alert color="primary" %}}
`PivotCache.getSourceType()` (перечисление `PivotTableSourceType`) указывает, откуда были получены данные кэша. Начиная с версии v26.7, `PivotCache.refresh()` поддерживает только типы источников **`SHEET`** и **`CONSOLIDATION`** — то есть данные, которые находятся в диапазонах рабочего листа. Внешние источники (базы данных, внешние подключения и т. д.) пока не могут быть обновлены через API кэша.
Из-за этой цепочки в Aspose.Cells существуют два основных пути обновления:
- **`PivotTable.calculateData()`** — пересчитывает отображение одной `Сводной таблицы` из уже закэшированных данных, без обращения к источнику данных.
Все сценарии в этой статье используют данные источника из ячеек рабочего листа, поэтому тип источника — `SHEET`, и операции обновления ведут себя так, как описано.
{{% /alert %}}

## Quick Start
Если вам нужен лишь минимальный код, который обновляет все сводные таблицы в рабочей книге, достаточно одного вызова:

```python
import jpype
from asposecells.api import Workbook

workbook = Workbook("input.xlsx")
workbook.refreshAll()
workbook.save("output.xlsx")
```

Всё остальное в этой статье объясняет, когда следует выбрать более узкий API вместо этого.

## Required Imports
Все примеры Python в этой статье используют следующие импорты, поскольку типы сводных таблиц находятся в пространстве имён `aspose.cells.pivot`:
- `import jpype`
- `import aspose.cells as cells`
Модуль `jpype` используется для загрузки JVM, а `aspose.cells` предоставляет типы workbook/worksheet/cell/pivot, используемые на протяжении всей статьи.

## Refresh All Pivot Tables in the Workbook
Когда необходимо убедиться, что каждый кэш сводной таблицы и каждая сводная таблица в рабочей книге отражают актуальные исходные данные, самым простым и всеобъемлющим API является `Workbook.refreshAll()`. Один вызов проходит по всей рабочей книге — обновляя каждый `PivotCache` из его источника, а затем пересчитывая каждую зависимую `Сводную таблицу`. Это рекомендуемый подход для общих полных обновлений документов, когда производительность не является проблемой.
Следующий пример создаёт рабочую книгу с исходным диапазоном Fruit/Year/Amount, создаёт одну сводную таблицу, изменяет некоторые исходные значения, а затем использует `refreshAll()` для обновления всего за один вызов.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
# Create a new workbook
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Write header row into cells A1:C1
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
# Write data rows into cells A2:C9 (8 rows of fruit data across 2020 and 2021)
worksheet.getCells().get("A2").putValue("grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(50)
worksheet.getCells().get("A3").putValue("blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(60)
worksheet.getCells().get("A4").putValue("kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(70)
worksheet.getCells().get("A5").putValue("cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(80)
worksheet.getCells().get("A6").putValue("grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(90)
worksheet.getCells().get("A7").putValue("blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(100)
worksheet.getCells().get("A8").putValue("kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(110)
worksheet.getCells().get("A9").putValue("cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(120)
# Add a pivot table: source range "A1:C9", destination cell "E3", name "Pivot1"
pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)
# Assign pivot fields: Fruit to Rows, Year to Columns, Amount to Data
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
# Modify several Amount values in the source data to simulate changes
worksheet.getCells().get("C2").putValue(55)
worksheet.getCells().get("C5").putValue(85)
worksheet.getCells().get("C9").putValue(125)
# Refresh every pivot table / pivot cache in the workbook
workbook.refreshAll()
# Save the workbook
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## Refresh All Pivot Tables on a Single Worksheet
Иногда требуется обновить только те сводные таблицы, которые находятся на одном конкретном рабочем листе — например, когда известно, что сводные таблицы на других рабочих листах не связаны с ними и не должны быть затронуты. Для этого случая Aspose.Cells предоставляет `Worksheet.refreshPivotTables()`, который ограничен одним экземпляром `Worksheet`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
worksheet.getCells().get("A2").putValue("grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)
worksheet.getCells().get("A3").putValue("blueberry")
worksheet.getCells().get("B3").putValue(2021)
worksheet.getCells().get("C3").putValue(150)
worksheet.getCells().get("A4").putValue("kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(200)
worksheet.getCells().get("A5").putValue("cherry")
worksheet.getCells().get("B5").putValue(2021)
worksheet.getCells().get("C5").putValue(120)
worksheet.getCells().get("A6").putValue("grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(180)
worksheet.getCells().get("A7").putValue("blueberry")
worksheet.getCells().get("B7").putValue(2020)
worksheet.getCells().get("C7").putValue(130)
worksheet.getCells().get("A8").putValue("kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(220)
worksheet.getCells().get("A9").putValue("cherry")
worksheet.getCells().get("B9").putValue(2020)
worksheet.getCells().get("C9").putValue(140)
pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
worksheet.getCells().get("C2").putValue(300)
worksheet.getCells().get("C5").putValue(250)
worksheet.getCells().get("C9").putValue(400)
worksheet.refreshPivotTables()
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## Refresh a Single Pivot Table
Когда требуется детальный контроль над одной сводной таблицей, API на основе кэша предоставляет два варианта. Выбор между ними зависит от того, что именно изменилось: исходные данные или только параметры представления/макета самой сводной таблицы.

### Source Data Changed — Use `PivotCache.refresh()`
Если исходные данные изменились, правильной точкой входа является `pivotTable.getPivotCache().refresh()`. Этот вызов перечитывает исходные данные в кэш, а затем пересчитывает каждую `Сводную таблицу`, зависящую от этого кэша.

### Only View/Layout Changed — Use `calculateData()`
Если исходные данные *не* изменились, а изменились только параметры представления или макета сводной таблицы (например, поле было перемещено в другую область или переключена настройка обновления при открытии), нет необходимости обращаться к источнику данных. Кэш уже содержит нужные данные; необходимо только пересчитать отображаемую `Сводную таблицу`. В этом случае `pivotTable.calculateData()` является правильным выбором.
Следующий пример изменяет свойство сводной таблицы, не относящееся к источнику, а затем вызывает `calculateData()` для её повторного отображения из существующего кэша.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Write Fruit / Year / Amount header row
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
# Write 8 data rows (rows 2-9, fitting the source range A1:C9)
worksheet.getCells().get("A2").putValue("Grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)
worksheet.getCells().get("A3").putValue("Blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(200)
worksheet.getCells().get("A4").putValue("Kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(300)
worksheet.getCells().get("A5").putValue("Cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(400)
worksheet.getCells().get("A6").putValue("Grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(150)
worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(250)
worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(350)
worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(450)
# Add a pivot table named "Pivot1" placed at destination cell E3, sourcing from A1:C9
pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)
# Assign fields: Fruit to Row, Year to Column, Amount to Data
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
# Modify a view/layout property — this is a presentation-only change,
# so it does NOT require re-reading the source data through PivotCache.refresh().
pivotTable.setRefreshDataOnOpeningFile(False)
# calculateData() re-renders THIS pivot table's display (data + style) from the
# data already held in the PivotCache. Because the source data did not change,
# no round-trip to the source is performed — only the cached values are recalculated
# into worksheet cells.
pivotTable.calculateData()
# Save the workbook to disk
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

Рабочая книга часто содержит множество сводных таблиц, которые все построены поверх одного общего кэша. Чтобы перечислить их — например, перед выполнением пакетного обновления или для диагностики влияния общего кэша — используйте `PivotCache.getPivotTables()`. Этот метод возвращает коллекцию каждой `Сводной таблицы`, зависящей от данного кэша.

## Migrating from the Obsolete `PivotTable.refreshData()`
До Aspose.Cells for Python via Java v26.7 стандартным способом обновления сводной таблицы был вызов `PivotTable.refreshData()` для каждой сводной таблицы отдельно. Начиная с версии v26.7 этот метод помечен как **нерекомендуемый** и должен быть заменён описанными выше API, учитывающими кэш.
Существуют две причины, по которым подход с вызовом `refreshData()` для каждой таблицы является проблемным в реальных рабочих книгах:
- Он повторно извлекает данные из источника *при каждом* вызове, даже если источник не изменился.
Рекомендуемые замены:
Следующий пример демонстрирует новый эффективный шаблон для рабочих книг с несколькими сводными таблицами, использующими один общий кэш.

## Which Refresh API Should I Use?
В таблице ниже приведены доступные API обновления и случаи, когда следует выбирать каждый из них.
| Цель | Рекомендуемый API | Примечания |
|------|-----------------|-------|
| Обновить всё в рабочей книге | `Workbook.refreshAll()` | Один вызов; охватывает все кэши и таблицы. |
| Обновить только сводные таблицы на одном листе | `Worksheet.refreshPivotTables()` | Ограничен одним рабочим листом. |
| Изменились исходные данные для одного кэша | `pivotTable.getPivotCache().refresh()` | Обновляет ВСЕ сводные таблицы на этом общем кэше. |
| Изменились только параметры представления/макета | `pivotTable.calculateData()` | Пропускает ненужный повторный запрос к источнику. |
| Получить список всех сводных таблиц на общем кэше | `pivotCache.getPivotTables()` | Используйте для перечисления перед массовым обновлением. |
На практике предпочтительнее использовать API на основе кэша вместо устаревшего `refreshData()` для каждой таблицы. Они учитывают общие кэши, избегают избыточных обращений к источнику и позволяют выбрать наименьшую область, удовлетворяющую требованиям обновления.

## Common Pitfalls
- **Забыли обновить перед сохранением.** Сводная таблица записывает свои вычисленные значения на рабочий лист только тогда, когда её цепочка данных обновлена. Если вы изменяете исходные ячейки, вызовите `PivotCache.refresh()` (или `Workbook.refreshAll()`) перед `Workbook.save()`, иначе сохранённый файл всё ещё будет содержать старые агрегированные значения.
- **Вызов устаревшего `RefreshData()` для каждой таблицы.** В версии v26.7 метод `PivotTable.RefreshData()` помечен как нерекомендуемый и повторно извлекает данные из источника при каждом вызове. При наличии нескольких сводных таблиц, использующих общий кэш, это означает N избыточных обращений к источнику. Замените на однократный вызов `PivotCache.refresh()` с последующим `calculateData()` для каждой таблицы.
- **Обновление при изменении только макета.** Если вы изменили только представление сводной таблицы (порядок столбцов, `ConsolidationFunction` и т. д.), не затрагивая исходные данные, вызов `PivotCache.refresh()` не нужен и медленный. Вызовите `pivotTable.calculateData()`, чтобы повторно отобразить данные из существующего кэша.
- **Внешний источник не поддерживается `PivotCache.refresh()`.** Если источник сводной таблицы получен из внешнего подключения (база данных, OLAP-куб и т. д.), `PivotCache.refresh()` не может его обновить в версии v26.7 — в настоящее время он поддерживает только типы источников `Sheet` и `Consolidation`. Для внешних источников заново откройте рабочую книгу или перестройте кэш из источника.

{{< app/cells/assistant language="python" >}}
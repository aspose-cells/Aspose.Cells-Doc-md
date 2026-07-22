---
title: Обновление сводных таблиц в Aspose.Cells for Python via .NET
linktitle: Обновление сводных таблиц в Aspose.Cells for Python via .NET
description: Узнайте, как обновлять сводные таблицы в Aspose.Cells for Python via .NET с помощью API обновления сводных таблиц v26.7+. В этой статье рассматриваются RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData и GetPivotTables с практическими примерами кода.
keywords: Aspose.Cells, Python via .NET, сводная таблица, обновление, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ru/python-net/refresh-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells предоставляет многоуровневый API обновления, который позволяет перезагружать данные сводных таблиц на четырёх различных уровнях — от всей рабочей книги до одной сводной таблицы. Начиная с **Aspose.Cells for Python via .NET v26.7**, устаревший метод `PivotTable.refresh_data()` помечен как obsolete (устаревший) и должен быть заменён более эффективными API с поддержкой кэша, описанными в данной статье.

{{% /alert %}}

## Введение

Обновление сводной таблицы редко представляет собой одну операцию. За кулисами Aspose.Cells поддерживает многоуровневую цепочку данных, которая связывает исходные данные с отображаемыми значениями на рабочем листе. Понимание этой цепочки — ключ к выбору правильного API обновления для любой ситуации.

Цепочка данных состоит из четырёх уровней:

1. **Источник данных** — исходные диапазоны рабочего листа, запрос к базе данных или диапазон консолидации, где хранятся необработанные значения.
2. **PivotCache** — снимок исходных данных в памяти. Каждая сводная таблица строится поверх `PivotCache`; именно здесь все данные собираются и агрегируются.
3. **PivotTable** — объект представления, который определяет поля строк, столбцов, значений и фильтров. `PivotTable` читает данные *только* из своего `PivotCache`, и никогда напрямую из источника данных.
4. **Cells** — объект `Cells` рабочего листа, в который `PivotTable` выводит вычисленные значения и стили.

Особенно важным понятием является **общий кэш**. Когда несколько сводных таблиц в рабочей книге ссылаются на один и тот же исходный диапазон, они используют *один* экземпляр `PivotCache`. Один `PivotCache` может использоваться множеством сводных таблиц, и обновление этого кэша обновляет все зависимые `PivotTable` одновременно.

{{% alert color="primary" %}}

`PivotCache.source_type` (перечисление `PivotTableSourceType`) указывает, откуда поступили данные кэша. Начиная с версии v26.7, `PivotCache.refresh()` поддерживает только типы источников **`Sheet`** и **`Consolidation`** — то есть данные, которые находятся в диапазонах рабочего листа. Внешние источники (базы данных, внешние подключения и т. д.) пока не могут быть обновлены через API кэша.

{{% /alert %}}

Из-за этой цепочки в Aspose.Cells существуют два основных пути обновления:

- **`PivotCache.refresh()`** — перезагружает источник → кэш И пересчитывает все зависимые `PivotTable` за одну операцию.
- **`PivotTable.calculate_data()`** — пересчитывает отображение одной `PivotTable` на основе уже кэшированных данных, без обращения к источнику данных.

Во всех сценариях этой статьи используются исходные данные из ячеек рабочего листа, поэтому тип источника — `Sheet`, и операции обновления работают, как описано.

## Необходимые импорты

Все примеры Python в этой статье начинаются со следующих трёх операторов импорта, поскольку типы сводных таблиц находятся в пространстве имён `aspose.cells.pivot`:

- `import sys`
- `import aspose.cells`
- `import aspose.cells.pivot`

## Обновление всех сводных таблиц в рабочей книге

Если вам нужно обеспечить, чтобы каждый кэш сводной таблицы и каждая сводная таблица в рабочей книге отражали самые последние исходные данные, самым простым и комплексным API является `Workbook.refresh_all()`. Один вызов проходит по всей рабочей книге — обновляя каждый `PivotCache` из его источника, а затем пересчитывая все зависимые `PivotTable`. Это рекомендуемый подход для общих полных обновлений документа, где производительность не критична.

В следующем примере создаётся рабочая книга с исходным диапазоном Fruit/Year/Amount, создаётся одна сводная таблица, изменяются некоторые исходные значения, а затем с помощью `refresh_all()` всё приводится в актуальное состояние за один вызов.

```python
import aspose.cells as ac

# Создать новую рабочую книгу
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Записать строку заголовка в ячейки A1:C1
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# Записать строки данных в ячейки A2:C9 (8 строк данных о фруктах за 2020 и 2021 годы)
worksheet.cells["A2"].put_value("grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(50)

worksheet.cells["A3"].put_value("blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(60)

worksheet.cells["A4"].put_value("kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(70)

worksheet.cells["A5"].put_value("cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(80)

worksheet.cells["A6"].put_value("grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(90)

worksheet.cells["A7"].put_value("blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(100)

worksheet.cells["A8"].put_value("kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(110)

worksheet.cells["A9"].put_value("cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(120)

# Добавить сводную таблицу: исходный диапазон "A1:C9", ячейка назначения "E3", имя "Pivot1"
pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

# Назначить поля сводной таблицы: Fruit - в строки, Year - в столбцы, Amount - в данные
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# Изменить несколько значений Amount в исходных данных для имитации изменений
worksheet.cells["C2"].put_value(55)
worksheet.cells["C5"].put_value(85)
worksheet.cells["C9"].put_value(125)

# Обновить все сводные таблицы / кэши сводных таблиц в рабочей книге
workbook.refresh_all()

# Сохранить рабочую книгу
workbook.save("output.xlsx")
```

## Обновление всех сводных таблиц на одном рабочем листе

Иногда требуется обновить только сводные таблицы, которые находятся на одном конкретном рабочем листе — например, когда известно, что сводные таблицы на других листах не связаны и не должны затрагиваться. Для этого случая Aspose.Cells предоставляет `Worksheet.refresh_pivot_tables()`, который ограничен одним экземпляром `Worksheet`.

Это более выборочно, чем `Workbook.refresh_all()`: обновляются только сводные таблицы на целевом рабочем листе, а сводные таблицы на других листах остаются нетронутыми.

В следующем примере заполняются те же исходные данные Fruit/Year/Amount, добавляется сводная таблица на первый рабочий лист, изменяются некоторые исходные значения, а затем обновляются только сводные таблицы на этом листе.

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

worksheet.cells["A2"].put_value("grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(100)

worksheet.cells["A3"].put_value("blueberry")
worksheet.cells["B3"].put_value(2021)
worksheet.cells["C3"].put_value(150)

worksheet.cells["A4"].put_value("kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(200)

worksheet.cells["A5"].put_value("cherry")
worksheet.cells["B5"].put_value(2021)
worksheet.cells["C5"].put_value(120)

worksheet.cells["A6"].put_value("grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(180)

worksheet.cells["A7"].put_value("blueberry")
worksheet.cells["B7"].put_value(2020)
worksheet.cells["C7"].put_value(130)

worksheet.cells["A8"].put_value("kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(220)

worksheet.cells["A9"].put_value("cherry")
worksheet.cells["B9"].put_value(2020)
worksheet.cells["C9"].put_value(140)

pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

worksheet.cells["C2"].put_value(300)
worksheet.cells["C5"].put_value(250)
worksheet.cells["C9"].put_value(400)

worksheet.refresh_pivot_tables()

workbook.save("output.xlsx")
```

## Обновление одной сводной таблицы

Если вам нужен тонкий контроль над одной сводной таблицей, API на основе кэша предоставляет два варианта. Выбор между ними зависит от того, что именно изменилось: базовые исходные данные или только параметры представления/макета самой сводной таблицы.

### Изменились исходные данные — используйте `PivotCache.refresh()`

Если базовые исходные данные изменились, правильной точкой входа является `pivot_table.pivot_cache.refresh()`. Этот вызов перечитывает исходные данные в кэш, а затем пересчитывает каждую `PivotTable`, которая зависит от этого кэша.

{{% alert color="primary" %}}

Поскольку сводные таблицы совместно используют один экземпляр `PivotCache`, вызов `PivotCache.refresh()` пересчитывает **все** сводные таблицы, построенные на этом же кэше — а не только ту, на которую вы ссылаетесь. Если две сводные таблицы используют один и тот же исходный диапазон, обновление одного кэша обновляет обе.

{{% /alert %}}

В следующем примере создаются две сводные таблицы на одном и том же исходном диапазоне, чтобы продемонстрировать это поведение общего кэша, изменяются некоторые исходные значения, а затем выполняется обновление через ссылку на один кэш.

```python
import aspose.cells as ac

# Создаём новую книгу и получаем доступ к первому листу
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Записываем строку заголовков: Фрукт / Год / Количество
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# Записываем примерно 9 строк данных (виноград / черника / киви / вишня за 2020-2021 годы)
worksheet.cells["A2"].put_value("Grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(100)

worksheet.cells["A3"].put_value("Blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(200)

worksheet.cells["A4"].put_value("Kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(300)

worksheet.cells["A5"].put_value("Cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(400)

worksheet.cells["A6"].put_value("Grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(500)

worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(600)

worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(700)

worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(800)

# Добавляем первую сводную таблицу "Pivot1" с якорем в ячейке E3, исходный диапазон A1:C9
pivotIndex1 = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivotTable1 = worksheet.pivot_tables[pivotIndex1]

# Назначаем поля для Pivot1
pivotTable1.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivotTable1.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivotTable1.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# Добавляем ВТОРУЮ сводную таблицу "Pivot2" с якорем в E15, используя ТОТ ЖЕ исходный диапазон A1:C9
# Pivot1 и Pivot2 используют общий PivotCache, так как исходный диапазон идентичен.
pivotIndex2 = worksheet.pivot_tables.add("A1:C9", "E15", "Pivot2")
pivotTable2 = worksheet.pivot_tables[pivotIndex2]

# Назначаем те же поля для Pivot2
pivotTable2.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivotTable2.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivotTable2.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# Изменяем несколько значений ячеек Amount в исходных данных для имитации изменения данных
worksheet.cells["C2"].put_value(150)
worksheet.cells["C4"].put_value(350)
worksheet.cells["C7"].put_value(650)

# Обновляем общий PivotCache.
# Поскольку Pivot1 и Pivot2 используют общий PivotCache, этот единственный вызов
# обновляет ОБЕ сводные таблицы (данные + стиль) из обновлённого источника.
pivotTable1.pivot_cache.refresh()

# Сохраняем книгу
workbook.save("output.xlsx")
```

### Изменились только представление/макет — используйте `calculate_data()`

Если исходные данные *не* изменились, а изменились только параметры представления или макета сводной таблицы (например, поле было перемещено в другую область или был переключён параметр обновления при открытии), нет необходимости возвращаться к источнику данных. Кэш уже содержит правильные данные; требуется пересчёт только отображаемой `PivotTable`. В этом случае `pivot_table.calculate_data()` — правильный выбор.

Это позволяет избежать ненужного обращения к источнику и значительно быстрее, когда много сводных таблиц используют один и тот же кэш.

В следующем примере изменяется свойство сводной таблицы, не связанное с источником, а затем вызывается `calculate_data()` для её повторного отображения из существующего кэша.

```python
import aspose.cells as ac
import aspose.cells.pivot as acp

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Записать строку заголовков Fruit / Year / Amount
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# Записать 8 строк данных (строки 2-9, вписывающиеся в исходный диапазон A1:C9)
worksheet.cells["A2"].put_value("Grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(100)

worksheet.cells["A3"].put_value("Blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(200)

worksheet.cells["A4"].put_value("Kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(300)

worksheet.cells["A5"].put_value("Cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(400)

worksheet.cells["A6"].put_value("Grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(150)

worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(250)

worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(350)

worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(450)

# Добавить сводную таблицу с именем "Pivot1", размещённую в ячейке назначения E3, с источником из A1:C9
pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

# Назначить поля: Fruit в строки, Year в столбцы, Amount в данные
pivot_table.add_field_to_area(acp.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(acp.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(acp.PivotFieldType.DATA, "Amount")

# Изменить свойство представления/макета — это изменение только для отображения,
# поэтому оно НЕ требует повторного чтения исходных данных через PivotCache.Refresh().
pivot_table.refresh_data_on_opening_file = False

# CalculateData() повторно отображает эту сводную таблицу (данные + стиль) из
# данных, уже хранящихся в PivotCache. Поскольку исходные данные не изменились,
# обращения к источнику не происходит — пересчитываются только кэшированные значения
# в ячейках листа.
pivot_table.calculate_data()

# Сохранить книгу на диск
workbook.save("output.xlsx")
```

## Получение всех сводных таблиц, использующих один и тот же PivotCache

Рабочая книга часто содержит множество сводных таблиц, которые построены поверх одного общего кэша. Чтобы перечислить их — например, перед выполнением пакетного обновления или для диагностики влияния общего кэша — используйте `PivotCache.get_pivot_tables()`. Этот метод возвращает коллекцию каждой `PivotTable`, которая зависит от данного кэша.

Это также самый прямой способ убедиться, что две сводные таблицы действительно используют один и тот же экземпляр `PivotCache`: можно сравнить ссылки на кэши или просто перебрать коллекцию, возвращаемую `get_pivot_tables()`, и увидеть, какие сводные таблицы в ней присутствуют.

В следующем примере создаются две сводные таблицы на одном исходном диапазоне, проверяется, что они используют один и тот же экземпляр кэша, а затем перечисляются сводные таблицы этого кэша.

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Sheet1"

worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

worksheet.cells["A2"].put_value("Grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(100)

worksheet.cells["A3"].put_value("Blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(200)

worksheet.cells["A4"].put_value("Kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(300)

worksheet.cells["A5"].put_value("Cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(400)

worksheet.cells["A6"].put_value("Grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(500)

worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(600)

worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(700)

worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(800)

worksheet.cells["A10"].put_value("Grape")
worksheet.cells["B10"].put_value(2021)
worksheet.cells["C10"].put_value(900)

pivot1_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table1 = worksheet.pivot_tables[pivot1_index]
pivot_table1.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table1.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table1.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

pivot2_index = worksheet.pivot_tables.add("A1:C9", "E15", "Pivot2")
pivot_table2 = worksheet.pivot_tables[pivot2_index]
pivot_table2.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table2.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table2.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

same_cache = pivot_table1.pivot_cache is pivot_table2.pivot_cache
print("Pivot1 and Pivot2 share the same PivotCache: " + str(same_cache))

shared_pivot_tables = pivot_table1.pivot_cache.get_pivot_tables()
print("Number of pivot tables sharing the cache: " + str(len(shared_pivot_tables)))

for pt in shared_pivot_tables:
    print("Pivot table name: " + pt.name)

workbook.save("output.xlsx")
```

## Миграция с устаревшего `PivotTable.refresh_data()`

До версии Aspose.Cells for Python via .NET v26.7 стандартным способом обновления сводной таблицы был вызов `PivotTable.refresh_data()` для каждой сводной таблицы отдельно. Начиная с версии v26.7, этот метод помечен как **устаревший** (obsolete) и должен быть заменён описанными выше API с поддержкой кэша.

Есть две причины, почему подход `refresh_data()` для каждой таблицы по отдельности проблематичен в реальных рабочих книгах:

- Он каждый раз заново получает данные из источника, даже когда источник не изменился.
- Каждый вызов обновляет весь общий кэш. Когда множество сводных таблиц используют один кэш, повторные вызовы `refresh_data()` для каждой сводной таблицы приводят к повторному получению одного и того же кэша снова и снова, что очень медленно.

Рекомендуемые замены:

- **Обновить ВСЕ сводные таблицы в рабочей книге** → используйте `workbook.refresh_all();`
- **Обновить НЕКОТОРЫЕ из них** → используйте `pivot_table.pivot_cache.refresh();` для одного кэша. Поскольку кэш общий, этот единственный вызов обновляет все сводные таблицы, построенные поверх этого кэша. Другие сводные таблицы, которые построены на уже обновлённом кэше, можно безопасно пропустить.
- **Изменилось только представление/макет сводной таблицы** → используйте `pivot_table.calculate_data();` для повторного отображения из существующего кэша без обращения к источнику.

В следующем примере демонстрируется новый эффективный паттерн для рабочих книг с несколькими сводными таблицами, использующими один кэш.

```python
import aspose.cells as ac

# Создаём новую книгу и получаем доступ к первому листу
workbook = ac.Workbook()
sheet = workbook.worksheets[0]

# --- Формируем исходные данные: Фрукт / Год / Количество (заголовок + 9 строк) ---
sheet.cells["A1"].put_value("Fruit")
sheet.cells["B1"].put_value("Year")
sheet.cells["C1"].put_value("Amount")

sheet.cells["A2"].put_value("Grape")      ; sheet.cells["B2"].put_value(2020); sheet.cells["C2"].put_value(1000)
sheet.cells["A3"].put_value("Blueberry")  ; sheet.cells["B3"].put_value(2020); sheet.cells["C3"].put_value(2000)
sheet.cells["A4"].put_value("Kiwi")       ; sheet.cells["B4"].put_value(2020); sheet.cells["C4"].put_value(1500)
sheet.cells["A5"].put_value("Cherry")     ; sheet.cells["B5"].put_value(2020); sheet.cells["C5"].put_value(2500)
sheet.cells["A6"].put_value("Grape")      ; sheet.cells["B6"].put_value(2021); sheet.cells["C6"].put_value(3000)
sheet.cells["A7"].put_value("Blueberry")  ; sheet.cells["B7"].put_value(2021); sheet.cells["C7"].put_value(1800)
sheet.cells["A8"].put_value("Kiwi")       ; sheet.cells["B8"].put_value(2021); sheet.cells["C8"].put_value(2200)
sheet.cells["A9"].put_value("Cherry")     ; sheet.cells["B9"].put_value(2021); sheet.cells["C9"].put_value(2700)

# --- Добавляем первую сводную таблицу (Pivot1) в ячейку E3 ---
idx1 = sheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table1 = sheet.pivot_tables[idx1]
pivot_table1.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table1.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table1.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# --- Добавляем ВТОРУЮ сводную таблицу (Pivot2) на ТОТ ЖЕ диапазон источника ---
# Pivot1 и Pivot2 используют ОДИН общий PivotCache.
# Это именно тот сценарий, в котором устаревший подход RefreshData(),
# вызываемый для каждой таблицы, становится неэффективным: обновление одной
# таблицы повторно извлекает весь общий кэш, поэтому обновление N таблиц
# приводит к N одинаково дорогостоящим извлечениям данных.
idx2 = sheet.pivot_tables.add("A1:C9", "E15", "Pivot2")
pivot_table2 = sheet.pivot_tables[idx2]
pivot_table2.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table2.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table2.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# --- Изменяем несколько значений Amount в исходных данных ---
sheet.cells["C2"].put_value(5000)   # Grape  2020
sheet.cells["C5"].put_value(7500)   # Cherry 2020
sheet.cells["C9"].put_value(9500)   # Cherry 2021

# --- УСТАРЕВШИЙ шаблон (до версии 26.7) — PivotTable.RefreshData() ---
# pivot_table1.refresh_data();  # повторно извлекает данные из источника, обновляет весь кэш
# pivot_table2.refresh_data();  # повторно извлекает ОПЯТЬ — кэш уже свежий!
# Каждый вызов перестраивает общий кэш, поэтому N таблиц = N избыточных извлечений.

# --- НОВЫЙ шаблон v26.7+: обновляем кэш ОДИН раз, затем при необходимости перерисовываем ---
# Один вызов PivotCache.Refresh() подтягивает изменённые значения в общий
# кэш И пересчитывает отображение КАЖДОЙ сводной таблицы, которая на него ссылается.
# Поскольку Pivot1 и Pivot2 используют один PivotCache, этот единственный вызов
# обновляет обе таблицы — повторного обращения к источнику не требуется.
pivot_table1.pivot_cache.refresh()

# CalculateData() только перерисовывает отображение сводной таблицы (данные + стиль)
# из данных, уже хранящихся в кэше — он НЕ обращается к источнику.
# Мы вызываем его для Pivot2 здесь исключительно для демонстрации API: после того как кэш
# был обновлён один раз, любую зависимую таблицу можно перерисовать без повторного
# обращения к источнику. Используйте CalculateData() самостоятельно, когда изменились
# только параметры отображения/макета сводной таблицы, а кэш при этом актуален.
pivot_table2.calculate_data()

workbook.save("output.xlsx")
```

## Какой API обновления следует использовать?

В таблице ниже приведены доступные API обновления и указано, когда следует выбирать каждый из них.

| Цель | Рекомендуемый API | Примечания |
|------|-----------------|-------|
| Обновить всё в рабочей книге | `Workbook.refresh_all()` | Один вызов; охватывает все кэши и таблицы. |
| Обновить только сводные таблицы на одном листе | `Worksheet.refresh_pivot_tables()` | Ограничено одним рабочим листом. |
| Изменились исходные данные для одного кэша | `pivot_table.pivot_cache.refresh()` | Обновляет ВСЕ сводные таблицы на этом общем кэше. |
| Изменились только параметры представления/макета | `pivot_table.calculate_data()` | Пропускает ненужное обращение к источнику. |
| Список всех сводных таблиц на общем кэше | `pivot_cache.get_pivot_tables()` | Используйте для перечисления перед массовым обновлением. |

На практике отдавайте предпочтение API на основе кэша вместо устаревшего `refresh_data()` для каждой таблицы. Они учитывают общие кэши, избегают избыточных обращений к источнику и позволяют выбрать минимальную область, удовлетворяющую вашим требованиям к обновлению.

## Связанные статьи

- [Спарклайны в Aspose.Cells for Python via .NET](/cells/ru/python-net/sparkline/)

{{< app/cells/assistant language="python" >}}
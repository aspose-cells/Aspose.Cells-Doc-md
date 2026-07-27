---
title: Обновление сводных таблиц в Aspose.Cells for Python via .NET
linktitle: Обновление сводных таблиц в Aspose.Cells for Python via .NET
description: Узнайте, как обновлять сводные таблицы в Aspose.Cells for Python via .NET с использованием API обновления сводных таблиц версии v26.7+. В этой статье рассматриваются RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData и GetPivotTables с практическими примерами кода.
keywords: Aspose.Cells, Python via .NET, сводная таблица, обновление, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ru/python-net/refresh-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells предоставляет многоуровневый API обновления, который позволяет перезагружать данные сводных таблиц на четырёх различных уровнях — от всей рабочей книги до отдельной сводной таблицы. Начиная с версии **Aspose.Cells for Python via .NET v26.7** устаревший метод `PivotTable.refresh_data()` помечен как нерекомендуемый и должен быть заменён более эффективными API, учитывающими кэш и описанными в данной статье.
{{% /alert %}}
## Введение
Обновление сводной таблицы редко является одной операцией. Под капотом Aspose.Cells поддерживает многоуровневую цепочку данных, которая связывает исходные данные с отображаемыми значениями на листе. Понимание этой цепочки является ключом к выбору правильного API обновления для любой ситуации.
Цепочка данных состоит из четырёх уровней:
1. **Источник данных** — исходные диапазоны листа, запрос к базе данных или диапазон консолидации, в которых хранятся необработанные значения.
2. **PivotCache** — снимок исходных данных в памяти. Каждая сводная таблица строится поверх `PivotCache`; здесь собираются и агрегируются все данные.
3. **PivotTable** — объект представления, определяющий поля строк, столбцов, значений и фильтров. `PivotTable` читает данные *только* из своего `PivotCache` и никогда напрямую из источника данных.
4. **Cells** — ячейки листа `Cells`, в которые `PivotTable` выводит вычисленные значения и стили.
Особенно важным понятием является **общий кэш**. Когда несколько сводных таблиц в рабочей книге ссылаются на один и тот же исходный диапазон, они используют *один* экземпляр `PivotCache`. Один `PivotCache` может использоваться множеством сводных таблиц, и обновление этого кэша обновляет все зависимые `PivotTable` одновременно.
{{% alert color="primary" %}}
`PivotCache.source_type` (перечисление `PivotTableSourceType`) указывает, откуда были получены данные кэша. Начиная с версии v26.7, метод `PivotCache.refresh()` поддерживает только типы источников **`Sheet`** и **`Consolidation`** — то есть данные, расположенные в диапазонах листа. Внешние источники (базы данных, внешние подключения и т. д.) пока не могут быть обновлены через API кэша.
{{% /alert %}}
Из-за этой цепочки в Aspose.Cells существуют два основных пути обновления:
- **`PivotCache.refresh()`** — перезагружает источник в кэш И пересчитывает все зависимые `PivotTable` за одну операцию.
- **`PivotTable.calculate_data()`** — пересчитывает отображение одной `PivotTable` из уже кэшированных данных, без обращения к источнику данных.
Все сценарии в данной статье используют данные из ячеек листа, поэтому тип источника — `Sheet`, и операции обновления работают так, как описано.
## Необходимые импорты
Все примеры Python в этой статье начинаются со следующих трёх операторов импорта, поскольку типы сводных таблиц находятся в пространстве имён `aspose.cells.pivot`:
- `import sys`
- `import aspose.cells`
- `import aspose.cells.pivot`
## Обновить все сводные таблицы в рабочей книге
Когда необходимо обеспечить, чтобы каждый кэш сводных таблиц и каждая сводная таблица в рабочей книге отражали актуальные исходные данные, простейшим и наиболее полным API является `Workbook.refresh_all()`. Один вызов проходит по всей рабочей книге — обновляя каждый `PivotCache` из его источника, а затем пересчитывая каждую зависимую `PivotTable`. Это рекомендуемый подход для обычных полных обновлений документа, когда производительность не критична.
Следующий пример создаёт рабочую книгу с исходным диапазоном Fruit/Year/Amount, создаёт одну сводную таблицу, изменяет некоторые значения в источнике, а затем использует `refresh_all()` для обновления всего за один вызов.
```python
.cells as ac

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

# Назначить поля сводной таблицы: Fruit в строки, Year в столбцы, Amount в данные
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
## Обновить все сводные таблицы на одном листе
Иногда требуется обновить только сводные таблицы, расположенные на одном конкретном листе — например, когда известно, что сводные таблицы на других листах не связаны с ними и не должны затрагиваться. Для этого случая Aspose.Cells предоставляет метод `Worksheet.refresh_pivot_tables()`, который ограничен одним экземпляром `Worksheet`.
Это более избирательный подход по сравнению с `Workbook.refresh_all()`: обновляются только сводные таблицы на целевом листе, а сводные таблицы на других листах остаются нетронутыми.
Следующий пример заполняет те же исходные данные Fruit/Year/Amount, добавляет сводную таблицу на первый лист, изменяет некоторые значения в источнике, а затем обновляет только сводные таблицы на этом листе.
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
## Обновить одну сводную таблицу
Если требуется точечное управление одной сводной таблицей, API на основе кэша предоставляет два варианта. Выбор между ними зависит от того, что именно изменилось: базовые исходные данные или только параметры представления/макета самой сводной таблицы.
### Изменились исходные данные — используйте `PivotCache.refresh()`
Если изменились базовые исходные данные, правильной точкой входа является `pivot_table.pivot_cache.refresh()`. Этот вызов перечитывает исходные данные в кэш, а затем пересчитывает все `PivotTable`, зависящие от этого кэша.
{{% alert color="primary" %}}
Поскольку сводные таблицы совместно используют один экземпляр `PivotCache`, вызов `PivotCache.refresh()` приводит к пересчёту **всех** сводных таблиц, построенных на этом же кэше, — а не только той, на которую вы ссылаетесь. Если две сводные таблицы используют один и тот же исходный диапазон, обновление одного кэша обновляет обе.
{{% /alert %}}
Следующий пример создаёт две сводные таблицы на одном исходном диапазоне, чтобы продемонстрировать это поведение общего кэша, изменяет некоторые значения в источнике, а затем выполняет обновление через ссылку на один кэш.
```python
import aspose.cells as ac

# Создаём новую рабочую книгу и получаем доступ к первому листу
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Записываем строку заголовков: Fruit / Year / Amount
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# Записываем примерно 9 строк данных (grape / blueberry / kiwi / cherry за 2020-2021 годы)
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
# И Pivot1, и Pivot2 используют один общий PivotCache, поскольку исходный диапазон идентичен.
pivotIndex2 = worksheet.pivot_tables.add("A1:C9", "E15", "Pivot2")
pivotTable2 = worksheet.pivot_tables[pivotIndex2]

# Назначаем те же поля для Pivot2
pivotTable2.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivotTable2.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivotTable2.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# Изменяем несколько значений ячеек Amount в исходных данных, чтобы имитировать изменение данных
worksheet.cells["C2"].put_value(150)
worksheet.cells["C4"].put_value(350)
worksheet.cells["C7"].put_value(650)

# Обновляем общий PivotCache.
# Поскольку Pivot1 и Pivot2 используют общий PivotCache, этот единственный вызов
# обновляет ОБЕ сводные таблицы (данные + стиль) из обновлённого источника.
pivotTable1.pivot_cache.refresh()

# Сохраняем рабочую книгу
workbook.save("output.xlsx")
```
### Изменились только представление/макет — используйте `calculate_data()`
Если исходные данные *не* изменились, а изменились только параметры представления или макета сводной таблицы (например, поле было перемещено в другую область или переключена настройка обновления при открытии), нет необходимости обращаться к источнику данных. Кэш уже содержит правильные данные; требуется только пересчёт отображаемой `PivotTable`. В этом случае правильным выбором является `pivot_table.calculate_data()`.
Это позволяет избежать ненужного обращения к источнику и значительно быстрее, когда множество сводных таблиц использует один и тот же кэш.
Следующий пример изменяет свойство сводной таблицы, не связанное с источником, а затем вызывает `calculate_data()` для повторного отображения из существующего кэша.
```python
ells as ac
import aspose.cells.pivot as acp

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Записать строку заголовков Fruit / Year / Amount
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# Записать 8 строк данных (строки 2-9, соответствует исходному диапазону A1:C9)
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

# Добавить сводную таблицу с именем "Pivot1" в ячейку назначения E3, источник данных A1:C9
pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

# Назначить поля: Fruit — в строки, Year — в столбцы, Amount — в данные
pivot_table.add_field_to_area(acp.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(acp.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(acp.PivotFieldType.DATA, "Amount")

# Изменить свойство представления/макета — это изменение только отображения,
# поэтому оно НЕ требует повторного чтения исходных данных через PivotCache.Refresh().
pivot_table.refresh_data_on_opening_file = False

# CalculateData() перерисовывает отображение ЭТОЙ сводной таблицы (данные + стиль) из
# данных, уже хранящихся в PivotCache. Поскольку исходные данные не изменились,
# обращения к источнику не происходит — только кэшированные значения пересчитываются
# в ячейки листа.
pivot_table.calculate_data()

# Сохранить книгу на диск
workbook.save("output.xlsx")
```
## Получить все сводные таблицы, использующие один PivotCache
Рабочая книга часто содержит множество сводных таблиц, которые построены поверх одного общего кэша. Чтобы перечислить их — например, перед выполнением пакетного обновления или для диагностики влияния общего кэша — используйте `PivotCache.get_pivot_tables()`. Этот метод возвращает коллекцию всех `PivotTable`, зависящих от данного кэша.
Это также наиболее прямой способ убедиться, что две сводные таблицы действительно используют один и тот же экземпляр `PivotCache`: можно сравнить ссылки на кэш или просто перебрать коллекцию, возвращаемую `get_pivot_tables()`, и увидеть, какие сводные таблицы в ней присутствуют.
Следующий пример создаёт две сводные таблицы на одном исходном диапазоне, проверяет, что они используют один и тот же экземпляр кэша, а затем перечисляет сводные таблицы этого кэша.

## Миграция с устаревшего метода `PivotTable.refresh_data()`
До версии Aspose.Cells for Python via .NET v26.7 стандартным способом обновления сводной таблицы был вызов `PivotTable.refresh_data()` для каждой сводной таблицы по отдельности. Начиная с версии v26.7 этот метод помечен как **нерекомендуемый** и должен быть заменён описанными выше API, учитывающими кэш.
Существуют две причины, по которым подход с вызовом `refresh_data()` для каждой таблицы по отдельности проблематичен в реальных рабочих книгах:
- Он каждый раз заново получает данные из источника, даже если источник не изменился.
- Каждый вызов обновляет весь общий кэш. Когда множество сводных таблиц используют один кэш, повторные вызовы `refresh_data()` для каждой сводной таблицы приводят к многократному повторному получению данных из одного и того же кэша, что очень медленно.
Рекомендуемые замены:
- **Обновить ВСЕ сводные таблицы в рабочей книге** → используйте `workbook.refresh_all();`
- **Обновить НЕКОТОРЫЕ из них** → используйте `pivot_table.pivot_cache.refresh();` для одного кэша. Поскольку кэш общий, этот единственный вызов обновляет все сводные таблицы, построенные поверх этого кэша. Остальные сводные таблицы, построенные поверх уже обновлённого кэша, можно безопасно пропустить.
- **Изменилось только представление/макет сводной таблицы** → используйте `pivot_table.calculate_data();` для повторного отображения из существующего кэша без обращения к источнику.
Следующий пример демонстрирует новый эффективный паттерн для рабочих книг с несколькими сводными таблицами, использующими один кэш.
```python
import aspose.cells as ac

# Создаём новую книгу и обращаемся к первому листу
workbook = ac.Workbook()
sheet = workbook.worksheets[0]

# --- Формируем исходные данные: Фрукт / Год / Сумма (заголовок + 9 строк) ---
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

# --- Добавляем первую сводную таблицу (Pivot1) в ячейку-приёмник E3 ---
idx1 = sheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table1 = sheet.pivot_tables[idx1]
pivot_table1.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table1.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table1.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# --- Добавляем ВТОРУЮ сводную таблицу (Pivot2) на ТОТ ЖЕ диапазон источника ---
# Таблицы Pivot1 и Pivot2 совместно используют ОДИН базовый PivotCache.
# Это именно тот сценарий, в котором устаревший подход с RefreshData()
# на каждой таблице становится неэффективным: обновление одной таблицы
# заново загружает весь общий кэш, поэтому обновление N таблиц выполняет
# одну и ту же дорогостоящую загрузку N раз.
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
# pivot_table1.refresh_data();  # повторно загружает из источника, обновляет весь кэш
# pivot_table2.refresh_data();  # повторно загружает СНОВА — а кэш уже свежий!
# Каждый вызов перестраивает общий кэш, поэтому N таблиц = N избыточных загрузок.

# --- НОВЫЙ шаблон версии 26.7+: обновляем кэш ОДИН раз, затем при необходимости перерисовываем ---
# Один вызов PivotCache.Refresh() подтягивает изменённые значения в общий
# кэш И пересчитывает отображение КАЖДОЙ сводной таблицы, которая на него ссылается.
# Поскольку Pivot1 и Pivot2 используют один PivotCache, этот единственный вызов
# обновляет обе таблицы — повторного обращения к источнику не требуется.
pivot_table1.pivot_cache.refresh()

# Метод CalculateData() только перерисовывает отображение сводной таблицы
# (данные + стиль), используя данные, уже находящиеся в кэше, и НЕ обращается к источнику.
# Мы вызываем его здесь для Pivot2 исключительно, чтобы продемонстрировать API: после
# однократного обновления кэша любую зависимую таблицу можно перерисовать без
# обращения к источнику. Используйте CalculateData() отдельно в случаях, когда
# изменились только параметры отображения/макета сводной таблицы, а кэш уже актуален.
pivot_table2.calculate_data()

workbook.save("output.xlsx")
```
## Какой API обновления следует использовать?
В таблице ниже приведены доступные API обновления и указано, когда следует выбирать каждый из них.
| Цель | Рекомендуемый API | Примечания |
|------|-------------------|------------|
| Обновить всё в рабочей книге | `Workbook.refresh_all()` | Один вызов; охватывает все кэши и таблицы. |
| Обновить только сводные таблицы на одном листе | `Worksheet.refresh_pivot_tables()` | Ограничено одним листом. |
| Изменились исходные данные для одного кэша | `pivot_table.pivot_cache.refresh()` | Обновляет ВСЕ сводные таблицы на этом общем кэше. |
| Изменились только параметры представления/макета | `pivot_table.calculate_data()` | Пропускает ненужное обращение к источнику. |
| Получить список всех сводных таблиц на общем кэше | `pivot_cache.get_pivot_tables()` | Используйте для перечисления перед массовым обновлением. |
На практике отдавайте предпочтение API на основе кэша, а не устаревшему методу `refresh_data()` для отдельных таблиц. Они учитывают общие кэши, избегают избыточных обращений к источнику и позволяют выбрать минимальный объём, удовлетворяющий вашим требованиям к обновлению.

{{< app/cells/assistant language="python" >}}

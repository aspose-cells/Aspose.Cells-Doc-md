---
title: Обновление сводных таблиц в Aspose.Cells for Python via Java
linktitle: Обновление сводных таблиц в Aspose.Cells for Python via Java
description: Узнайте, как обновлять сводные таблицы в Aspose.Cells for Python via Java с помощью API обновления сводных таблиц v26.7+. В этой статье рассматриваются RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData и GetPivotTables с практическими примерами кода.
keywords: Aspose.Cells, Python via Java, сводная таблица, обновление, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ru/python-java/refresh-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
Aspose.Cells предоставляет многоуровневый API обновления, который позволяет перезагружать данные сводных таблиц в четырёх различных областях — от всей рабочей книги до отдельной сводной таблицы. Начиная с версии **Aspose.Cells for Python via Java v26.7**, устаревший метод `PivotTable.refreshData()` помечен как нерекомендуемый и должен быть заменён более эффективными API, учитывающими кэш, которые описаны в этой статье.
{{% /alert %}}
## Введение
Обновление сводной таблицы редко представляет собой одну операцию. За кулисами Aspose.Cells поддерживает многоуровневую цепочку данных, которая связывает исходные данные с отображаемыми значениями, которые вы видите на рабочем листе. Понимание этой цепочки — ключ к выбору правильного API обновления для любой ситуации.
Цепочка данных состоит из четырёх уровней:
1. **Источник данных** — исходные диапазоны рабочего листа, запрос к базе данных или диапазон консолидации, где хранятся необработанные значения.
2. **PivotCache** — снимок исходных данных в памяти. Каждая сводная таблица построена поверх `PivotCache`; именно здесь все данные собираются и агрегируются.
3. **PivotTable** — объект представления, который определяет поля строк, столбцов, значений и фильтров. `PivotTable` читает данные *только* из своего `PivotCache`, но никогда напрямую из источника данных.
4. **Cells** — `Cells` рабочего листа, в которые `PivotTable` выводит вычисленные значения и стили.
Особенно важным понятием является **общий кэш**. Когда несколько сводных таблиц в рабочей книге ссылаются на один и тот же исходный диапазон, они используют *один* экземпляр `PivotCache`. На один `PivotCache` могут ссылаться многие сводные таблицы, и обновление этого кэша обновляет все зависимые `PivotTable` одновременно.
{{% alert color="primary" %}}
`PivotCache.getSourceType()` (перечисление `PivotTableSourceType`) указывает, откуда поступили данные кэша. Начиная с версии v26.7, `PivotCache.refresh()` поддерживает только типы источников **`SHEET`** и **`CONSOLIDATION`** — то есть данные, которые находятся в диапазонах рабочего листа. Внешние источники (базы данных, внешние подключения и т. д.) пока не могут быть обновлены через API кэша.
{{% /alert %}}
Благодаря этой цепочке в Aspose.Cells существуют два основных пути обновления:
- **`PivotCache.refresh()`** — перезагружает источник → кэш И пересчитывает все зависимые `PivotTable` за одну операцию.
- **`PivotTable.calculateData()`** — пересчитывает отображение одной `PivotTable` из уже кэшированных данных без обращения к источнику данных.
Все сценарии в этой статье используют исходные данные из ячеек рабочего листа, поэтому тип источника — `SHEET`, и операции обновления работают, как описано.
## Необходимые импорты
Все примеры Python в этой статье используют следующие импорты, поскольку типы сводных таблиц находятся в пространстве имён `aspose.cells.pivot`:
- `import jpype`
- `import aspose.cells as cells`
Модуль `jpype` используется для запуска JVM, а `aspose.cells` предоставляет типы рабочей книги/рабочего листа/ячейки/сводной таблицы, которые используются на протяжении всей статьи.
## Обновление всех сводных таблиц в рабочей книге
Когда вам нужно обеспечить, чтобы каждый кэш сводной таблицы и каждая сводная таблица в рабочей книге отражали самые последние исходные данные, самым простым и исчерпывающим API является `Workbook.refreshAll()`. Один вызов проходит через всю рабочую книгу — обновляя каждый `PivotCache` из его источника, а затем пересчитывая каждую зависимую `PivotTable`. Это рекомендуемый подход для общих полных обновлений документа, где производительность не является проблемой.
Следующий пример создаёт рабочую книгу с исходным диапазоном Fruit/Year/Amount, создаёт одну сводную таблицу, изменяет некоторые исходные значения, а затем использует `refreshAll()`, чтобы привести всё в актуальное состояние за один вызов.
```python
asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# Создать новую рабочую книгу
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Записать строку заголовка в ячейки A1:C1
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# Записать строки данных в ячейки A2:C9 (8 строк данных о фруктах за 2020 и 2021 годы)
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

# Добавить сводную таблицу: исходный диапазон "A1:C9", целевая ячейка "E3", имя "Pivot1"
pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# Назначить поля сводной таблицы: Fruit в строки, Year в столбцы, Amount в данные
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# Изменить несколько значений Amount в исходных данных для имитации изменений
worksheet.getCells().get("C2").putValue(55)
worksheet.getCells().get("C5").putValue(85)
worksheet.getCells().get("C9").putValue(125)

# Обновить все сводные таблицы / кэш сводных таблиц в рабочей книге
workbook.refreshAll()

# Сохранить рабочую книгу
workbook.save("output.xlsx")

jpype.shutdownJVM()
```
## Обновление всех сводных таблиц на одном рабочем листе
Иногда вам нужно обновить только те сводные таблицы, которые находятся на одном конкретном рабочем листе — например, когда известно, что сводные таблицы на других рабочих листах не связаны и не должны быть затронуты. Для этого случая Aspose.Cells предоставляет `Worksheet.refreshPivotTables()`, который ограничен одним экземпляром `Worksheet`.
Это более выборочно, чем `Workbook.refreshAll()`: обновляются только сводные таблицы на целевом рабочем листе, а сводные таблицы на других рабочих листах остаются нетронутыми.
Следующий пример заполняет те же исходные данные Fruit/Year/Amount, добавляет сводную таблицу на первом рабочем листе, изменяет некоторые исходные значения, а затем обновляет только сводные таблицы на этом рабочем листе.
```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
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
## Обновление одной сводной таблицы
Если вам нужен точный контроль над одной сводной таблицей, API на основе кэша предоставляет вам два варианта. Выбор между ними зависит от того, что фактически изменилось: базовые исходные данные или только параметры представления/макета самой сводной таблицы.
### Исходные данные изменились — используйте `PivotCache.refresh()`
Если базовые исходные данные изменились, правильной точкой входа является `pivotTable.getPivotCache().refresh()`. Этот вызов перечитывает исходные данные в кэш, а затем пересчитывает каждую `PivotTable`, которая зависит от этого кэша.
{{% alert color="primary" %}}
Поскольку сводные таблицы совместно используют один экземпляр `PivotCache`, вызов `PivotCache.refresh()` пересчитывает **все** сводные таблицы, построенные на этом же кэше — а не только ту, на которую вы ссылаетесь. Если две сводные таблицы совместно используют один и тот же исходный диапазон, обновление одного кэша обновляет обе.
{{% /alert %}}
Следующий пример создаёт две сводные таблицы на одном и том же исходном диапазоне, чтобы продемонстрировать это поведение общего кэша, изменяет некоторые исходные значения, а затем выполняет обновление через одну ссылку на кэш.
```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# Создаём новую рабочую книгу и получаем доступ к первому листу
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Записываем строку заголовка: Фрукт / Год / Сумма
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# Записываем примерно 9 строк данных (виноград / черника / киви / вишня за 2020-2021 годы)
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
worksheet.getCells().get("C6").putValue(500)

worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(600)

worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(700)

worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(800)

# Добавляем первую сводную таблицу "Pivot1" с привязкой к ячейке E3, исходный диапазон A1:C9
pivotIndex1 = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable1 = worksheet.getPivotTables().get(pivotIndex1)

# Назначаем поля для Pivot1
pivotTable1.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable1.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable1.addFieldToArea(PivotFieldType.Data, "Amount")

# Добавляем ВТОРУЮ сводную таблицу "Pivot2" с привязкой к E15, используя ТОТ ЖЕ исходный диапазон A1:C9
# Обе таблицы Pivot1 и Pivot2 используют один общий PivotCache, поскольку исходный диапазон идентичен.
pivotIndex2 = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2")
pivotTable2 = worksheet.getPivotTables().get(pivotIndex2)

# Назначаем те же поля для Pivot2
pivotTable2.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable2.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable2.addFieldToArea(PivotFieldType.Data, "Amount")

# Изменяем значения нескольких ячеек Amount в исходных данных, чтобы имитировать изменение данных
worksheet.getCells().get("C2").putValue(150)
worksheet.getCells().get("C4").putValue(350)
worksheet.getCells().get("C7").putValue(650)

# Обновляем общий PivotCache.
# Поскольку Pivot1 и Pivot2 используют один и тот же PivotCache, этот единственный вызов
# обновляет ОБЕ сводные таблицы (данные + стиль) на основе обновлённого источника.
pivotTable1.getPivotCache().refresh()

# Сохраняем рабочую книгу
workbook.save("output.xlsx")

jpype.shutdownJVM()
```
### Изменилось только представление/макет — используйте `calculateData()`
Если исходные данные *не* изменились, но изменились только параметры представления или макета сводной таблицы (например, поле было перемещено в другую область или переключена настройка обновления при открытии), нет необходимости возвращаться к источнику данных. Кэш уже содержит правильные данные; необходимо только пересчитать отображаемую `PivotTable`. В этом случае `pivotTable.calculateData()` является правильным выбором.
Это позволяет избежать ненужного извлечения из источника и значительно быстрее, когда много сводных таблиц совместно используют один и тот же кэш.
Следующий пример изменяет свойство сводной таблицы, не относящееся к источнику, а затем вызывает `calculateData()` для повторного отображения из существующего кэша.
```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Запись строки заголовка Fruit / Year / Amount
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# Запись 8 строк данных (строки 2-9, вписывающихся в исходный диапазон A1:C9)
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

# Добавление сводной таблицы с именем "Pivot1", размещённой в ячейке назначения E3, с источником данных A1:C9
pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# Назначение полей: Fruit в строки, Year в столбцы, Amount в данные
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# Изменение свойства представления/макета — это изменение только для отображения,
# поэтому оно НЕ требует повторного чтения исходных данных через PivotCache.Refresh().
pivotTable.setRefreshDataOnOpeningFile(False)

# CalculateData() повторно отображает представление ЭТОЙ сводной таблицы (данные + стиль) из
# данных, уже хранящихся в PivotCache. Поскольку исходные данные не изменились,
# обращения к источнику не происходит — только кэшированные значения пересчитываются
# в ячейках листа.
pivotTable.calculateData()

# Сохранение книги на диск
workbook.save("output.xlsx")

jpype.shutdownJVM()
```
## Получение всех сводных таблиц, использующих один и тот же PivotCache
Рабочая книга часто содержит много сводных таблиц, которые все построены поверх одного общего кэша. Чтобы перечислить их — например, перед выполнением пакетного обновления или для диагностики влияния общего кэша — используйте `PivotCache.getPivotTables()`. Этот метод возвращает коллекцию каждой `PivotTable`, которая зависит от данного кэша.
Это также самый прямой способ убедиться, что две сводные таблицы действительно совместно используют один и тот же экземпляр `PivotCache`: вы можете сравнить ссылки на кэш или просто перебрать коллекцию, возвращаемую `getPivotTables()`, и посмотреть, какие сводные таблицы в ней присутствуют.
Следующий пример создаёт две сводные таблицы на одном и том же исходном диапазоне, проверяет, что они совместно используют один и тот же экземпляр кэша, а затем перечисляет сводные таблицы кэша.
```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTable, PivotFieldType

# перенесённый код здесь
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Sheet1")

worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

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
worksheet.getCells().get("C6").putValue(500)

worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(600)

worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(700)

worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(800)

worksheet.getCells().get("A10").putValue("Grape")
worksheet.getCells().get("B10").putValue(2021)
worksheet.getCells().get("C10").putValue(900)

pivot1Index = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable1 = worksheet.getPivotTables().get(pivot1Index)
pivotTable1.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable1.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable1.addFieldToArea(PivotFieldType.DATA, "Amount")

pivot2Index = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2")
pivotTable2 = worksheet.getPivotTables().get(pivot2Index)
pivotTable2.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable2.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable2.addFieldToArea(PivotFieldType.DATA, "Amount")

sameCache = pivotTable1.getPivotCache() is pivotTable2.getPivotCache()
print("Pivot1 and Pivot2 share the same PivotCache: " + str(sameCache))

sharedPivotTables = pivotTable1.getPivotCache().getPivotTables()
print("Number of pivot tables sharing the cache: " + str(len(sharedPivotTables)))

for pt in sharedPivotTables:
    print("Pivot table name: " + pt.getName())

workbook.save("output.xlsx")

jpype.shutdownJVM()
```
## Миграция с устаревшего `PivotTable.refreshData()`
До версии Aspose.Cells for Python via Java v26.7 стандартным способом обновления сводной таблицы был вызов `PivotTable.refreshData()` на каждой сводной таблице по отдельности. Начиная с версии v26.7 этот метод помечен как **нерекомендуемый** и должен быть заменён API, учитывающими кэш, описанными выше.
Существуют две причины, по которым подход с `refreshData()` для каждой таблицы является проблематичным в реальных рабочих книгах:
- Он повторно извлекает данные из источника *при каждом* вызове, даже если источник не изменился.
- Каждый вызов обновляет весь общий кэш. Когда много сводных таблиц совместно используют один кэш, повторный вызов `refreshData()` для каждой сводной таблицы приводит к многократному повторному извлечению одного и того же кэша, что очень медленно.
Рекомендуемые замены:
- **Обновить ВСЕ сводные таблицы в рабочей книге** → используйте `workbook.refreshAll();`
- **Обновить НЕКОТОРЫЕ из них** → используйте `pivotTable.getPivotCache().refresh();` для одного кэша. Поскольку кэш является общим, этот единственный вызов обновляет каждую сводную таблицу, построенную поверх этого кэша. Другие сводные таблицы, которые расположены на уже обновлённом кэше, можно безопасно пропустить.
- **Изменилось только представление/макет сводной таблицы** → используйте `pivotTable.calculateData();` для повторного отображения из существующего кэша без какого-либо обращения к источнику.
Следующий пример демонстрирует новый эффективный шаблон для рабочих книг с несколькими сводными таблицами, использующими один кэш.
```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# Создаём новую книгу и получаем доступ к первому листу
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)

# --- Создаём исходные данные: Фрукт / Год / Сумма (заголовок + 9 строк) ---
sheet.getCells().get("A1").putValue("Fruit")
sheet.getCells().get("B1").putValue("Year")
sheet.getCells().get("C1").putValue("Amount")

sheet.getCells().get("A2").putValue("Grape");      sheet.getCells().get("B2").putValue(2020); sheet.getCells().get("C2").putValue(1000)
sheet.getCells().get("A3").putValue("Blueberry");  sheet.getCells().get("B3").putValue(2020); sheet.getCells().get("C3").putValue(2000)
sheet.getCells().get("A4").putValue("Kiwi");       sheet.getCells().get("B4").putValue(2020); sheet.getCells().get("C4").putValue(1500)
sheet.getCells().get("A5").putValue("Cherry");     sheet.getCells().get("B5").putValue(2020); sheet.getCells().get("C5").putValue(2500)
sheet.getCells().get("A6").putValue("Grape");      sheet.getCells().get("B6").putValue(2021); sheet.getCells().get("C6").putValue(3000)
sheet.getCells().get("A7").putValue("Blueberry");  sheet.getCells().get("B7").putValue(2021); sheet.getCells().get("C7").putValue(1800)
sheet.getCells().get("A8").putValue("Kiwi");       sheet.getCells().get("B8").putValue(2021); sheet.getCells().get("C8").putValue(2200)
sheet.getCells().get("A9").putValue("Cherry");     sheet.getCells().get("B9").putValue(2021); sheet.getCells().get("C9").putValue(2700)

# --- Добавляем первую сводную таблицу (Pivot1) в ячейку E3 ---
idx1 = sheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable1 = sheet.getPivotTables().get(idx1)
pivotTable1.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable1.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable1.addFieldToArea(PivotFieldType.Data, "Amount")

# --- Добавляем ВТОРУЮ сводную таблицу (Pivot2) на ТОТ ЖЕ диапазон источника ---
# И Pivot1, и Pivot2 используют ОДИН общий PivotCache.
# Именно в этом сценарии устаревший подход с RefreshData() для каждой таблицы
# становится неэффективным: обновление одной таблицы повторно загружает весь
# общий кэш, поэтому обновление N таблиц выполняет ту же дорогостоящую загрузку N раз.
idx2 = sheet.getPivotTables().add("A1:C9", "E15", "Pivot2")
pivotTable2 = sheet.getPivotTables().get(idx2)
pivotTable2.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable2.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable2.addFieldToArea(PivotFieldType.Data, "Amount")

# --- Изменяем несколько значений Amount в исходных данных ---
sheet.getCells().get("C2").putValue(5000)   # Grape  2020
sheet.getCells().get("C5").putValue(7500)   # Cherry 2020
sheet.getCells().get("C9").putValue(9500)   # Cherry 2021

# --- УСТАРЕВШИЙ шаблон (до версии 26.7) — PivotTable.RefreshData() ---
# pivotTable1.RefreshData();  // повторно загружает из источника, обновляет весь кэш
# pivotTable2.RefreshData();  // повторно загружает СНОВА — кэш уже актуален!
# Каждый вызов перестраивает общий кэш, поэтому N таблиц = N избыточных загрузок.

# --- НОВЫЙ шаблон v26.7+: обновляем кэш ОДИН раз, затем перерисовываем по необходимости ---
# Один вызов PivotCache.Refresh() подтягивает изменённые значения в общий
# кэш И пересчитывает отображение КАЖДОЙ сводной таблицы, которая на него ссылается.
# Поскольку Pivot1 и Pivot2 используют один PivotCache, этот единственный вызов обновляет
# обе таблицы — повторный запрос к источнику не требуется.
pivotTable1.getPivotCache().refresh()

# CalculateData() только перерисовывает отображение сводной таблицы (данные + стиль)
# из данных, уже хранящихся в кэше — он НЕ обращается к источнику.
# Мы вызываем его на Pivot2 здесь исключительно для демонстрации API: после того как кэш
# был однократно обновлён, любую зависимую таблицу можно перерисовать без
# обращения к источнику. Используйте CalculateData() самостоятельно, когда изменились только
# настройки представления/макета сводной таблицы, а кэш уже актуален.
pivotTable2.calculateData()

workbook.save("output.xlsx")

jpype.shutdownJVM()
```
## Какой API обновления следует использовать?
В таблице ниже приведены доступные API обновления и случаи, когда следует выбирать каждый из них.
| Цель | Рекомендуемый API | Примечания |
|------|-----------------|-------|
| Обновить всё в рабочей книге | `Workbook.refreshAll()` | Один вызов; охватывает все кэши и таблицы. |
| Обновить только сводные таблицы на одном листе | `Worksheet.refreshPivotTables()` | Ограничено одним рабочим листом. |
| Исходные данные изменились для одного кэша | `pivotTable.getPivotCache().refresh()` | Обновляет ВСЕ сводные таблицы на этом общем кэше. |
| Изменились только параметры представления/макета | `pivotTable.calculateData()` | Пропускает ненужное обращение к источнику. |
| Список всех сводных таблиц на общем кэше | `pivotCache.getPivotTables()` | Используется для перечисления перед массовым обновлением. |
На практике отдавайте предпочтение API на основе кэша вместо устаревшего `refreshData()` для каждой таблицы. Они учитывают общие кэши, избегают избыточных обращений к источнику и позволяют выбрать наименьшую область, удовлетворяющую вашим требованиям к обновлению.
## Связанные статьи
- [Вставка изображения в ячейку](/cells/ru/python-java/inserting-an-image-into-a-cell/)
- [Чтение и запись файлов DBF](/cells/ru/python-java/dbf/)
- [Разделение файлов Excel на несколько файлов](/cells/ru/python-java/splitting-excel-files-into-multiple-files/)
- [Спарклайны в Aspose.Cells for Python via Java](/cells/ru/python-java/sparkline/)
{{< app/cells/assistant language="python" >}}
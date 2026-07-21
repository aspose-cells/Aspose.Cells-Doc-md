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

Aspose.Cells предоставляет многоуровневый API обновления, который позволяет перезагружать данные сводных таблиц на четырёх различных уровнях — от всей рабочей книги до одной сводной таблицы. Начиная с версии **Aspose.Cells for Python via Java v26.7**, прежний метод `PivotTable.refreshData()` помечен как устаревший и должен быть заменён более эффективными API, учитывающими кэш, описанными в этой статье.

{{% /alert %}}

## Введение

Обновление сводной таблицы редко является одной операцией. За кулисами Aspose.Cells поддерживает многоуровневую цепочку данных, которая соединяет исходные данные с отображаемыми значениями, которые вы видите на рабочем листе. Понимание этой цепочки является ключом к выбору правильного API обновления для любой ситуации.

Четырёхуровневая цепочка данных выглядит следующим образом:

1. **Источник данных** — исходные диапазоны рабочего листа, запрос к базе данных или диапазон консолидации, где хранятся необработанные значения.
2. **PivotCache** — моментальный снимок исходных данных в памяти. Каждая сводная таблица построена поверх `PivotCache`; именно здесь все данные собираются и агрегируются.
3. **PivotTable** — объект представления, определяющий поля строк, столбцов, значений и фильтров. `PivotTable` читает *только* из своего `PivotCache`, никогда напрямую из источника данных.
4. **Cells** — коллекция `Cells` рабочего листа, в которую `PivotTable` отображает вычисленные значения и стили.

Особенно важной концепцией является **общий кэш**. Когда несколько сводных таблиц в рабочей книге ссылаются на один и тот же диапазон источника, они используют *один* экземпляр `PivotCache`. На один `PivotCache` могут ссылаться многие сводные таблицы, и обновление этого кэша обновляет все зависимые `PivotTable` одновременно.

{{% alert color="primary" %}}

`PivotCache.getSourceType()` (перечисление `PivotTableSourceType`) указывает, откуда поступили данные кэша. Начиная с версии v26.7, `PivotCache.refresh()` поддерживает только типы источников **`SHEET`** и **`CONSOLIDATION`** — то есть данные, которые находятся в диапазонах рабочего листа. Внешние источники (базы данных, внешние подключения и т.д.) пока не могут быть обновлены через API кэша.

{{% /alert %}}

Из-за этой цепочки в Aspose.Cells существуют два основных пути обновления:

- **`PivotCache.refresh()`** — перезагружает источник → кэш И пересчитывает все зависимые `PivotTable` за одну операцию.
- **`PivotTable.calculateData()`** — пересчитывает отображение одной `PivotTable` из уже кэшированных данных, без обращения к источнику данных.

Все сценарии в этой статье используют данные из ячеек рабочего листа в качестве источника, поэтому тип источника — `SHEET`, и операции обновления работают, как описано.

## Необходимые импорты

Все примеры Python в этой статье используют следующие импорты, поскольку типы сводных таблиц находятся в пространстве имён `aspose.cells.pivot`:

- `import jpype`
- `import aspose.cells as cells`

Модуль `jpype` используется для загрузки JVM, а `aspose.cells` предоставляет типы workbook/worksheet/cell/pivot, используемые на протяжении всего документа.

## Обновление всех сводных таблиц в рабочей книге

Когда вам нужно обеспечить, чтобы каждый кэш сводной таблицы и каждая сводная таблица в рабочей книге отражали самые последние исходные данные, самым простым и всеобъемлющим API является `Workbook.refreshAll()`. Один вызов проходит через всю рабочую книгу — обновляя каждый `PivotCache` из его источника, а затем пересчитывая каждую зависимую `PivotTable`. Это рекомендуемый подход для общих полных обновлений документа, когда производительность не имеет значения.

Следующий пример создаёт рабочую книгу с исходным диапазоном Fruit/Year/Amount, создаёт одну сводную таблицу, изменяет некоторые исходные значения, а затем использует `refreshAll()` для обновления всего за один вызов.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# Создаём новую книгу
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Записываем строку заголовков в ячейки A1:C1
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# Записываем строки данных в ячейки A2:C9 (8 строк данных о фруктах за 2020 и 2021 годы)
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

# Добавляем сводную таблицу: исходный диапазон "A1:C9", ячейка назначения "E3", имя "Pivot1"
pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# Назначаем поля сводной таблицы: Fruit — в строки, Year — в столбцы, Amount — в данные
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# Изменяем несколько значений Amount в исходных данных для имитации изменений
worksheet.getCells().get("C2").putValue(55)
worksheet.getCells().get("C5").putValue(85)
worksheet.getCells().get("C9").putValue(125)

# Обновляем все сводные таблицы / кэш сводных таблиц в книге
workbook.refreshAll()

# Сохраняем книгу
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## Обновление всех сводных таблиц на одном рабочем листе

Иногда вам нужно обновить только те сводные таблицы, которые находятся на конкретном рабочем листе — например, когда известно, что сводные таблицы на других рабочих листах не связаны с ними и не должны быть затронуты. Для этого случая Aspose.Cells предоставляет `Worksheet.refreshPivotTables()`, который ограничен одним экземпляром `Worksheet`.

Это более выборочно, чем `Workbook.refreshAll()`: обновляются только сводные таблицы на целевом рабочем листе, оставляя сводные таблицы на других рабочих листах нетронутыми.

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

Когда вам нужен детальный контроль над одной сводной таблицей, API на основе кэша предоставляет вам два варианта. Выбор между ними зависит от того, что фактически изменилось: базовые исходные данные или только настройки представления/макета самой сводной таблицы.

### Исходные данные изменились — используйте `PivotCache.refresh()`

Если базовые исходные данные изменились, правильной точкой входа является `pivotTable.getPivotCache().refresh()`. Этот вызов перечитывает исходные данные в кэш, а затем пересчитывает каждую `PivotTable`, которая зависит от этого кэша.

{{% alert color="primary" %}}

Поскольку сводные таблицы совместно используют один экземпляр `PivotCache`, вызов `PivotCache.refresh()` пересчитывает **все** сводные таблицы, построенные на том же кэше — не только ту, на которую вы ссылаетесь. Если две сводные таблицы используют один и тот же диапазон источника, обновление одного кэша обновляет обе.

{{% /alert %}}

Следующий пример создаёт две сводные таблицы на одном и том же диапазоне источника, чтобы продемонстрировать это поведение общего кэша, изменяет некоторые исходные значения, а затем обновляет через ссылку на один кэш.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# Создаём новую книгу и получаем доступ к первому листу
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Записываем строку заголовков: Fruit / Year / Amount
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

# Добавляем первую сводную таблицу "Pivot1" с якорем в ячейке E3, исходный диапазон A1:C9
pivotIndex1 = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable1 = worksheet.getPivotTables().get(pivotIndex1)

# Назначаем поля для Pivot1
pivotTable1.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable1.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable1.addFieldToArea(PivotFieldType.Data, "Amount")

# Добавляем ВТОРУЮ сводную таблицу "Pivot2" с якорем в E15, используя ТОТ ЖЕ исходный диапазон A1:C9
# Pivot1 и Pivot2 используют общий PivotCache, так как исходный диапазон одинаковый.
pivotIndex2 = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2")
pivotTable2 = worksheet.getPivotTables().get(pivotIndex2)

# Назначаем те же поля для Pivot2
pivotTable2.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable2.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable2.addFieldToArea(PivotFieldType.Data, "Amount")

# Изменяем несколько значений Amount в исходных данных, чтобы имитировать изменение данных
worksheet.getCells().get("C2").putValue(150)
worksheet.getCells().get("C4").putValue(350)
worksheet.getCells().get("C7").putValue(650)

# Обновляем общий PivotCache.
# Поскольку Pivot1 и Pivot2 используют общий PivotCache, этот единственный вызов
# обновляет ОБЕ сводные таблицы (данные + стиль) из обновлённого источника.
pivotTable1.getPivotCache().refresh()

# Сохраняем книгу
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

### Изменилось только представление/макет — используйте `calculateData()`

Если исходные данные *не* изменились, но были изменены только настройки представления или макета сводной таблицы (например, поле было перемещено в другую область или был переключён параметр обновления при открытии), нет необходимости обращаться к источнику данных. Кэш уже содержит правильные данные; нужно только пересчитать отображаемую `PivotTable`. В этом случае `pivotTable.calculateData()` является правильным выбором.

Это устраняет ненужную выборку из источника и работает значительно быстрее, когда многие сводные таблицы совместно используют один и тот же кэш.

Следующий пример изменяет свойство сводной таблицы, не связанное с источником, а затем вызывает `calculateData()` для повторного отображения из существующего кэша.

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

# Добавление сводной таблицы с именем "Pivot1", размещённой в ячейке назначения E3, с источником данных из A1:C9
pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# Назначение полей: Fruit в строки, Year в столбцы, Amount в данные
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# Изменение свойства представления/макета — это изменение только для отображения,
# поэтому оно НЕ требует повторного чтения исходных данных через PivotCache.Refresh().
pivotTable.setRefreshDataOnOpeningFile(False)

# calculateData() перерисовывает отображение ЭТОЙ сводной таблицы (данные + стиль) из
# данных, уже хранящихся в PivotCache. Поскольку исходные данные не изменились,
# обращения к источнику не происходит — пересчитываются только кэшированные значения
# в ячейки листа.
pivotTable.calculateData()

# Сохранение книги на диск
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## Получить все сводные таблицы, использующие один и тот же PivotCache

Рабочая книга часто содержит много сводных таблиц, которые все построены на одном общем кэше. Чтобы перечислить их — например, перед выполнением пакетного обновления или для диагностики влияния общего кэша — используйте `PivotCache.getPivotTables()`. Этот метод возвращает коллекцию каждой `PivotTable`, которая зависит от данного кэша.

Это также самый прямой способ подтвердить, что две сводные таблицы действительно совместно используют один и тот же экземпляр `PivotCache`: вы можете сравнить ссылки на кэш или просто перебрать коллекцию, возвращённую `getPivotTables()`, и увидеть, какие сводные таблицы в ней присутствуют.

Следующий пример создаёт две сводные таблицы на одном и том же диапазоне источника, проверяет, что они совместно используют один и тот же экземпляр кэша, а затем перечисляет сводные таблицы этого кэша.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTable, PivotFieldType

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

До версии Aspose.Cells for Python via Java v26.7 стандартным способом обновления сводной таблицы был вызов `PivotTable.refreshData()` для каждой сводной таблицы отдельно. Начиная с версии v26.7 этот метод помечен как **устаревший** и должен быть заменён описанными выше API, учитывающими кэш.

Существуют две причины, по которым подход `refreshData()` для каждой таблицы проблематичен в реальных рабочих книгах:

- Он повторно извлекает данные из источника при *каждом* вызове, даже если источник не изменился.
- Каждый вызов обновляет весь общий кэш. Когда многие сводные таблицы совместно используют один кэш, повторный вызов `refreshData()` для каждой сводной таблицы приводит к многократному повторному извлечению одного и того же кэша, что очень медленно.

Рекомендуемые замены:

- **Обновить ВСЕ сводные таблицы в рабочей книге** → используйте `workbook.refreshAll();`
- **Обновить НЕКОТОРЫЕ из них** → используйте `pivotTable.getPivotCache().refresh();` для одного кэша. Поскольку кэш общий, этот единственный вызов обновляет каждую сводную таблицу, построенную поверх этого кэша. Другие сводные таблицы, которые находятся на уже обновлённом кэше, можно безопасно пропустить.
- **Изменилось только представление/макет сводной таблицы** → используйте `pivotTable.calculateData();` для повторного отображения из существующего кэша без обращения к источнику.

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

# --- Формируем исходные данные: Фрукт / Год / Сумма (заголовок + 9 строк) ---
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

# --- Добавляем первую сводную таблицу (Pivot1) в ячейку назначения E3 ---
idx1 = sheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable1 = sheet.getPivotTables().get(idx1)
pivotTable1.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable1.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable1.addFieldToArea(PivotFieldType.Data, "Amount")

# --- Добавляем ВТОРУЮ сводную таблицу (Pivot2) на ТОТ ЖЕ диапазон источника ---
# И Pivot1, и Pivot2 используют ОДИН общий PivotCache.
# Это именно тот сценарий, в котором устаревший подход с вызовом RefreshData()
# для каждой таблицы становится неэффективным: обновление одной таблицы
# повторно извлекает весь общий кэш, поэтому обновление N таблиц выполняет
# это дорогостоящее извлечение N раз.
idx2 = sheet.getPivotTables().add("A1:C9", "E15", "Pivot2")
pivotTable2 = sheet.getPivotTables().get(idx2)
pivotTable2.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable2.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable2.addFieldToArea(PivotFieldType.Data, "Amount")

# --- Изменяем несколько значений Amount в исходных данных ---
sheet.getCells().get("C2").putValue(5000)   # Виноград 2020
sheet.getCells().get("C5").putValue(7500)   # Вишня 2020
sheet.getCells().get("C9").putValue(9500)   # Вишня 2021

# --- УСТАРЕВШИЙ шаблон (до версии 26.7) — PivotTable.RefreshData() ---
# pivotTable1.RefreshData();  // повторно извлекает из источника, обновляет весь кэш
# pivotTable2.RefreshData();  // повторно извлекает СНОВА — кэш уже актуален!
# Каждый вызов перестраивает общий кэш, поэтому N таблиц = N избыточных извлечений.

# --- НОВЫЙ шаблон (v26.7+): обновляем кэш ОДИН раз, затем перерисовываем по необходимости ---
# Один вызов PivotCache.Refresh() подтягивает изменённые значения в общий
# кэш И пересчитывает отображение КАЖДОЙ сводной таблицы, которая на него ссылается.
# Поскольку Pivot1 и Pivot2 используют один PivotCache, этот единственный вызов обновляет
# обе таблицы — повторного обращения к источнику не требуется.
pivotTable1.getPivotCache().refresh()

# CalculateData() только перерисовывает отображение сводной таблицы (данные + стиль)
# из данных, уже хранящихся в кэше — он НЕ обращается к источнику.
# Мы вызываем его для Pivot2 здесь исключительно для демонстрации API: после того как кэш
# был обновлён один раз, любую зависимую таблицу можно перерисовать без
# обращения к источнику. Используйте CalculateData() отдельно, когда изменились
# только параметры отображения/макета сводной таблицы, а кэш актуален.
pivotTable2.calculateData()

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## Какой API обновления следует использовать?

В таблице ниже приведены доступные API обновления и указано, когда какой выбирать.

| Цель | Рекомендуемый API | Примечания |
|------|-----------------|-------|
| Обновить всё в рабочей книге | `Workbook.refreshAll()` | Один вызов; охватывает все кэши и таблицы. |
| Обновить только сводные таблицы на одном листе | `Worksheet.refreshPivotTables()` | Ограничено одним рабочим листом. |
| Исходные данные изменились для одного кэша | `pivotTable.getPivotCache().refresh()` | Обновляет ВСЕ сводные таблицы на этом общем кэше. |
| Изменились только настройки представления/макета | `pivotTable.calculateData()` | Пропускает ненужное обращение к источнику. |
| Список всех сводных таблиц на общем кэше | `pivotCache.getPivotTables()` | Используйте для перечисления перед массовым обновлением. |

На практике предпочтительнее использовать API на основе кэша вместо устаревшего `refreshData()` для каждой таблицы. Они учитывают общие кэши, избегают избыточных обращений к источнику и позволяют выбрать наименьшую область, удовлетворяющую вашим требованиям к обновлению.

## Связанные статьи

- [Вставка изображения в ячейку](/cells/ru/python-java/inserting-an-image-into-a-cell/)
- [Чтение и запись файлов DBF](/cells/ru/python-java/dbf/)
- [Разделение файлов Excel на несколько файлов](/cells/ru/python-java/splitting-excel-files-into-multiple-files/)
- [Спарклайны в Aspose.Cells for Python via Java](/cells/ru/python-java/sparkline/)

{{< app/cells/assistant language="python" >}}
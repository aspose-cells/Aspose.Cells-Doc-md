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

## Введение
Обновление сводной таблицы редко представляет собой одну операцию. За кулисами Aspose.Cells поддерживает многоуровневую цепочку данных, которая связывает исходные данные с отображаемыми значениями, которые вы видите на рабочем листе. Понимание этой цепочки является ключом к выбору правильного API обновления для любой ситуации.
Цепочка данных состоит из четырёх уровней:
1. **Источник данных** — исходные диапазоны рабочего листа, запрос к базе данных или диапазон консолидации, где хранятся исходные значения.
2. **PivotCache** — снимок исходных данных в памяти. Каждая сводная таблица построена поверх `PivotCache`; именно здесь все данные собираются и агрегируются.
3. **Сводная таблица** — объект представления, который определяет поля строк, столбцов, значений и фильтров. `Сводная таблица` читает данные *только* из своего `PivotCache`, никогда напрямую из источника данных.
4. **Ячейки** — `Cells` рабочего листа, в которые `Сводная таблица` выводит вычисленные значения и стили.

{{% alert color="primary" %}}
`PivotCache.getSourceType()` (перечисление `PivotTableSourceType`) указывает, откуда были получены данные кэша. Начиная с версии v26.7, `PivotCache.refresh()` поддерживает только типы источников **`SHEET`** и **`CONSOLIDATION`** — то есть данные, которые находятся в диапазонах рабочего листа. Внешние источники (базы данных, внешние подключения и т. д.) пока не могут быть обновлены через API кэша.
{{% /alert %}}

Из-за этой цепочки в Aspose.Cells существуют два основных пути обновления:
- **`PivotTable.calculateData()`** — пересчитывает отображение одной `Сводной таблицы` из уже закэшированных данных, без обращения к источнику данных.
Все сценарии в этой статье используют данные источника из ячеек рабочего листа, поэтому тип источника — `SHEET`, и операции обновления ведут себя так, как описано.

## Быстрый старт
Если вам нужен лишь минимальный код, который обновляет все сводные таблицы в рабочей книге, достаточно одного вызова:

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
# Обновляем все сводные таблицы / кэши сводных таблиц в книге
workbook.refreshAll()
# Сохраняем книгу
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

Всё остальное в этой статье объясняет, когда следует выбрать более узкий API вместо этого.

## Необходимые импорты
Все примеры Python в этой статье используют следующие импорты, поскольку типы сводных таблиц находятся в пространстве имён `aspose.cells.pivot`:
- `import jpype`
- `import aspose.cells as cells`
Модуль `jpype` используется для загрузки JVM, а `aspose.cells` предоставляет типы workbook/worksheet/cell/pivot, используемые на протяжении всей статьи.

## Обновление всех сводных таблиц в рабочей книге
Когда необходимо убедиться, что каждый кэш сводной таблицы и каждая сводная таблица в рабочей книге отражают актуальные исходные данные, самым простым и всеобъемлющим API является `Workbook.refreshAll()`. Один вызов проходит по всей рабочей книге — обновляя каждый `PivotCache` из его источника, а затем пересчитывая каждую зависимую `Сводную таблицу`. Это рекомендуемый подход для общих полных обновлений документов, когда производительность не является проблемой.
Следующий пример создаёт рабочую книгу с исходным диапазоном Fruit/Year/Amount, создаёт одну сводную таблицу, изменяет некоторые исходные значения, а затем использует `refreshAll()` для обновления всего за один вызов.

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

## Обновление всех сводных таблиц на одном рабочем листе
Иногда требуется обновить только те сводные таблицы, которые находятся на одном конкретном рабочем листе — например, когда известно, что сводные таблицы на других рабочих листах не связаны с ними и не должны быть затронуты. Для этого случая Aspose.Cells предоставляет `Worksheet.refreshPivotTables()`, который ограничен одним экземпляром `Worksheet`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Записать строку заголовков Fruit / Year / Amount
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
# Записать 8 строк данных (строки 2–9, соответствующие исходному диапазону A1:C9)
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
# Добавить сводную таблицу с именем "Pivot1", размещённую в ячейке E3, с источником данных A1:C9
pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)
# Назначить поля: Fruit — в строки, Year — в столбцы, Amount — в данные
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")
# Изменить свойство представления/макета — это изменение только оформления,
# поэтому оно НЕ требует повторного чтения исходных данных через PivotCache.Refresh().
pivotTable.setRefreshDataOnOpeningFile(False)
# calculateData() пересчитывает отображение ДАННОЙ сводной таблицы (данные + стиль)
# на основе данных, уже хранящихся в PivotCache. Так как исходные данные не изменились,
# обращения к источнику не происходит — пересчитываются только кэшированные значения
# в ячейках листа.
pivotTable.calculateData()
# Сохранить книгу на диск
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## Обновление одной сводной таблицы
Когда требуется детальный контроль над одной сводной таблицей, API на основе кэша предоставляет два варианта. Выбор между ними зависит от того, что именно изменилось: исходные данные или только параметры представления/макета самой сводной таблицы.

### Изменились исходные данные — используйте `PivotCache.refresh()`
Если исходные данные изменились, правильной точкой входа является `pivotTable.getPivotCache().refresh()`. Этот вызов перечитывает исходные данные в кэш, а затем пересчитывает каждую `Сводную таблицу`, зависящую от этого кэша.

### Изменились только представление/макет — используйте `calculateData()`
Если исходные данные *не* изменились, а изменились только параметры представления или макета сводной таблицы (например, поле было перемещено в другую область или переключена настройка обновления при открытии), нет необходимости обращаться к источнику данных. Кэш уже содержит нужные данные; необходимо только пересчитать отображаемую `Сводную таблицу`. В этом случае `pivotTable.calculateData()` является правильным выбором.
Следующий пример изменяет свойство сводной таблицы, не относящееся к источнику, а затем вызывает `calculateData()` для её повторного отображения из существующего кэша.
Рабочая книга часто содержит множество сводных таблиц, которые все построены поверх одного общего кэша. Чтобы перечислить их — например, перед выполнением пакетного обновления или для диагностики влияния общего кэша — используйте `PivotCache.getPivotTables()`. Этот метод возвращает коллекцию каждой `Сводной таблицы`, зависящей от данного кэша.

## Миграция с устаревшего `PivotTable.refreshData()`
До Aspose.Cells for Python via Java v26.7 стандартным способом обновления сводной таблицы был вызов `PivotTable.refreshData()` для каждой сводной таблицы отдельно. Начиная с версии v26.7 этот метод помечен как **нерекомендуемый** и должен быть заменён описанными выше API, учитывающими кэш.
Существуют две причины, по которым подход с вызовом `refreshData()` для каждой таблицы является проблемным в реальных рабочих книгах:
- Он повторно извлекает данные из источника *при каждом* вызове, даже если источник не изменился.
Рекомендуемые замены:
Следующий пример демонстрирует новый эффективный шаблон для рабочих книг с несколькими сводными таблицами, использующими один общий кэш.

## Какой API обновления следует использовать?
В таблице ниже приведены доступные API обновления и случаи, когда следует выбирать каждый из них.
| Цель | Рекомендуемый API | Примечания |
|------|-----------------|-------|
| Обновить всё в рабочей книге | `Workbook.refreshAll()` | Один вызов; охватывает все кэши и таблицы. |
| Обновить только сводные таблицы на одном листе | `Worksheet.refreshPivotTables()` | Ограничен одним рабочим листом. |
| Изменились исходные данные для одного кэша | `pivotTable.getPivotCache().refresh()` | Обновляет ВСЕ сводные таблицы на этом общем кэше. |
| Изменились только параметры представления/макета | `pivotTable.calculateData()` | Пропускает ненужный повторный запрос к источнику. |
| Получить список всех сводных таблиц на общем кэше | `pivotCache.getPivotTables()` | Используйте для перечисления перед массовым обновлением. |
На практике предпочтительнее использовать API на основе кэша вместо устаревшего `refreshData()` для каждой таблицы. Они учитывают общие кэши, избегают избыточных обращений к источнику и позволяют выбрать наименьшую область, удовлетворяющую требованиям обновления.

## Распространённые ошибки
- **Забыли обновить перед сохранением.** Сводная таблица записывает свои вычисленные значения на рабочий лист только тогда, когда её цепочка данных обновлена. Если вы изменяете исходные ячейки, вызовите `PivotCache.Refresh()` (или `Workbook.RefreshAll()`) перед `Workbook.save()`, иначе сохранённый файл всё ещё будет содержать старые агрегированные значения.
- **Вызов устаревшего `RefreshData()` для каждой таблицы.** В версии v26.7 метод `PivotTable.RefreshData()` помечен как нерекомендуемый и повторно извлекает данные из источника при каждом вызове. При наличии нескольких сводных таблиц, использующих общий кэш, это означает N избыточных обращений к источнику. Замените на однократный вызов `PivotCache.Refresh()` с последующим `CalculateData()` для каждой таблицы.
- **Обновление при изменении только макета.** Если вы изменили только представление сводной таблицы (порядок столбцов, `ConsolidationFunction` и т. д.), не затрагивая исходные данные, вызов `PivotCache.Refresh()` не нужен и медленный. Вызовите `pivotTable.CalculateData()`, чтобы повторно отобразить данные из существующего кэша.
- **Внешний источник не поддерживается `PivotCache.Refresh()`.** Если источник сводной таблицы получен из внешнего подключения (база данных, OLAP-куб и т. д.), `PivotCache.Refresh()` не может его обновить в версии v26.7 — в настоящее время он поддерживает только типы источников `Sheet` и `Consolidation`. Для внешних источников заново откройте рабочую книгу или перестройте кэш из источника.

```csharp
using Aspose.Cells;
Workbook workbook = new Workbook("input.xlsx");
workbook.RefreshAll();
workbook.Save("output.xlsx");
```

{{< app/cells/assistant language="python" >}}
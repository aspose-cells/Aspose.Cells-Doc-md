---
title: Обновление сводных таблиц и кэшей сводных таблиц в Aspose.Cells for Python via .NET
linktitle: Обновление сводных таблиц и кэшей сводных таблиц в Aspose.Cells for Python via .NET
description: Узнайте, как обновлять сводные таблицы в Aspose.Cells for Python via .NET с помощью API обновления сводных таблиц версии 26.7+. В этой статье рассматриваются RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData и GetPivotTables с практическими примерами кода.
keywords: Aspose.Cells, Python via .NET, сводная таблица, обновление, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ru/python-net/refresh-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells предоставляет многоуровневый API обновления, который позволяет перезагружать данные сводных таблиц на четырёх различных уровнях — от всей рабочей книги до одной сводной таблицы. Начиная с версии **Aspose.Cells for Python via .NET v26.7**, устаревший метод `PivotTable.refresh_data()` помечен как нерекомендуемый и должен быть заменён более эффективными API с поддержкой кэша, описанными в этой статье.
{{% /alert %}}

## Введение
Обновление сводной таблицы редко представляет собой одну операцию. За кулисами Aspose.Cells поддерживает многоуровневую цепочку данных, которая соединяет исходные данные с отображаемыми значениями, которые вы видите на рабочем листе. Понимание этой цепочки является ключом к выбору правильного API обновления для любой ситуации.
Цепочка данных состоит из четырёх уровней:
1. **Источник данных** — исходные диапазоны рабочего листа, запрос к базе данных или диапазон консолидации, где хранятся необработанные значения.
2. **PivotCache** — моментальный снимок исходных данных в памяти. Каждая сводная таблица построена поверх `PivotCache`; именно здесь все данные собираются и агрегируются.
3. **PivotTable** — объект представления, который определяет поля строк, столбцов, значений и фильтров. `PivotTable` читает данные *только* из своего `PivotCache`, никогда не обращаясь напрямую к источнику данных.
4. **Cells** — `Cells` рабочего листа, в которые `PivotTable` визуализирует вычисленные значения и стили.

{{% alert color="primary" %}}
`PivotCache.source_type` (перечисление `PivotTableSourceType`) указывает, откуда поступили данные кэша. Начиная с версии 26.7, `PivotCache.refresh()` поддерживает только типы источников **`Sheet`** и **`Consolidation`** — то есть данные, которые находятся в диапазонах рабочего листа. Внешние источники (базы данных, внешние подключения и т. д.) пока не могут быть обновлены через API кэша.
Из-за этой цепочки в Aspose.Cells существуют два основных пути обновления:
- **`PivotTable.calculate_data()`** — пересчитывает отображение одной `PivotTable` из уже закэшированных данных, без обращения к источнику данных.
Все сценарии в этой статье используют исходные данные ячеек рабочего листа, поэтому тип источника — `Sheet`, и операции обновления работают так, как описано.
{{% /alert %}}

## Быстрый старт
Если вам нужен только самый короткий код, который обновляет каждую сводную таблицу в рабочей книге, достаточно одного вызова:

```python
import aspose.cells as ac
workbook = ac.Workbook("input.xlsx")
workbook.refresh_all()
workbook.save("output.xlsx")
```

Всё остальное в этой статье объясняет, когда вместо этого следует выбрать более узкий API.

## Необходимые импорты
Все примеры Python в этой статье начинаются со следующих трёх операторов импорта, поскольку типы сводных таблиц находятся в пространстве имён `aspose.cells.pivot`:
- `import sys`
- `import aspose.cells`
- `import aspose.cells.pivot`

## Обновление всех сводных таблиц в рабочей книге
Когда необходимо обеспечить, чтобы каждый кэш сводной таблицы и каждая сводная таблица в рабочей книге отражали самые последние исходные данные, самым простым и наиболее полным API является `Workbook.refresh_all()`. Один вызов проходит по всей рабочей книге — обновляя каждый `PivotCache` из его источника, а затем пересчитывая каждую зависимую `PivotTable`. Это рекомендуемый подход для общих полных обновлений документа, когда производительность не является приоритетом.
В следующем примере создаётся рабочая книга с исходным диапазоном Фрукт/Год/Сумма, создаётся одна сводная таблица, изменяются некоторые исходные значения, а затем с помощью `refresh_all()` всё приводится в актуальное состояние за один вызов.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
# Создать новую рабочую книгу
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Записать строку заголовков в ячейки A1:C1
worksheet.cells.get("A1").put_value("Fruit")
worksheet.cells.get("B1").put_value("Year")
worksheet.cells.get("C1").put_value("Amount")
# Записать строки данных в ячейки A2:C9 (8 строк данных о фруктах за 2020 и 2021 годы)
worksheet.cells.get("A2").put_value("grape")
worksheet.cells.get("B2").put_value(2020)
worksheet.cells.get("C2").put_value(50)
worksheet.cells.get("A3").put_value("blueberry")
worksheet.cells.get("B3").put_value(2020)
worksheet.cells.get("C3").put_value(60)
worksheet.cells.get("A4").put_value("kiwi")
worksheet.cells.get("B4").put_value(2020)
worksheet.cells.get("C4").put_value(70)
worksheet.cells.get("A5").put_value("cherry")
worksheet.cells.get("B5").put_value(2020)
worksheet.cells.get("C5").put_value(80)
worksheet.cells.get("A6").put_value("grape")
worksheet.cells.get("B6").put_value(2021)
worksheet.cells.get("C6").put_value(90)
worksheet.cells.get("A7").put_value("blueberry")
worksheet.cells.get("B7").put_value(2021)
worksheet.cells.get("C7").put_value(100)
worksheet.cells.get("A8").put_value("kiwi")
worksheet.cells.get("B8").put_value(2021)
worksheet.cells.get("C8").put_value(110)
worksheet.cells.get("A9").put_value("cherry")
worksheet.cells.get("B9").put_value(2021)
worksheet.cells.get("C9").put_value(120)
# Добавить сводную таблицу: исходный диапазон "A1:C9", целевая ячейка "E3", имя "Pivot1"
pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]
# Назначить поля сводной таблицы: Fruit в строки, Year в столбцы, Amount в данные
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
# Изменить несколько значений Amount в исходных данных для имитации изменений
worksheet.cells.get("C2").put_value(55)
worksheet.cells.get("C5").put_value(85)
worksheet.cells.get("C9").put_value(125)
# Обновить каждую сводную таблицу / кэш сводных таблиц в рабочей книге
workbook.refresh_all()
# Сохранить рабочую книгу
workbook.save("output.xlsx")
```

## Обновление всех сводных таблиц на одном рабочем листе
Иногда требуется обновить только сводные таблицы, расположенные на одном конкретном рабочем листе — например, когда известно, что сводные таблицы на других рабочих листах не связаны с ними и их не нужно обновлять. Для этого случая Aspose.Cells предоставляет метод `Worksheet.refresh_pivot_tables()`, область действия которого ограничена одним экземпляром `Worksheet`.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Fruit")
worksheet.cells.get("B1").put_value("Year")
worksheet.cells.get("C1").put_value("Amount")
worksheet.cells.get("A2").put_value("grape")
worksheet.cells.get("B2").put_value(2020)
worksheet.cells.get("C2").put_value(100)
worksheet.cells.get("A3").put_value("blueberry")
worksheet.cells.get("B3").put_value(2021)
worksheet.cells.get("C3").put_value(150)
worksheet.cells.get("A4").put_value("kiwi")
worksheet.cells.get("B4").put_value(2020)
worksheet.cells.get("C4").put_value(200)
worksheet.cells.get("A5").put_value("cherry")
worksheet.cells.get("B5").put_value(2021)
worksheet.cells.get("C5").put_value(120)
worksheet.cells.get("A6").put_value("grape")
worksheet.cells.get("B6").put_value(2021)
worksheet.cells.get("C6").put_value(180)
worksheet.cells.get("A7").put_value("blueberry")
worksheet.cells.get("B7").put_value(2020)
worksheet.cells.get("C7").put_value(130)
worksheet.cells.get("A8").put_value("kiwi")
worksheet.cells.get("B8").put_value(2021)
worksheet.cells.get("C8").put_value(220)
worksheet.cells.get("A9").put_value("cherry")
worksheet.cells.get("B9").put_value(2020)
worksheet.cells.get("C9").put_value(140)
pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
worksheet.cells.get("C2").put_value(300)
worksheet.cells.get("C5").put_value(250)
worksheet.cells.get("C9").put_value(400)
worksheet.refresh_pivot_tables()
workbook.save("output.xlsx")
```

## Обновление одной сводной таблицы
Если требуется детальный контроль над обновлением одной сводной таблицы, API на основе кэша предоставляет два варианта. Выбор между ними зависит от того, что именно изменилось: исходные данные или только параметры представления/макета самой сводной таблицы.

### Изменены исходные данные — используйте `PivotCache.refresh()`
Если исходные данные изменились, правильной точкой входа является `pivot_table.pivot_cache.refresh()`. Этот вызов перечитывает исходные данные в кэш, а затем пересчитывает каждую `PivotTable`, которая зависит от этого кэша.

### Изменилось только представление/макет — используйте `calculate_data()`
Если исходные данные *не* изменились, но были изменены только параметры представления или макета сводной таблицы (например, поле было перемещено в другую область или был переключён параметр обновления при открытии), нет необходимости повторно обращаться к источнику данных. Кэш уже содержит нужные данные; пересчёта требует только отображаемая `PivotTable`. В этом случае `pivot_table.calculate_data()` является правильным выбором.
В следующем примере изменяется свойство сводной таблицы, не относящееся к источнику, а затем вызывается `calculate_data()` для её повторной визуализации из существующего кэша.

```python
import aspose.cells as ac
import aspose.cells.pivot as acp
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Записать строку заголовков Fruit / Year / Amount
worksheet.cells.get("A1").put_value("Fruit")
worksheet.cells.get("B1").put_value("Year")
worksheet.cells.get("C1").put_value("Amount")
# Записать 8 строк данных (строки 2-9, соответствующие исходному диапазону A1:C9)
worksheet.cells.get("A2").put_value("Grape")
worksheet.cells.get("B2").put_value(2020)
worksheet.cells.get("C2").put_value(100)
worksheet.cells.get("A3").put_value("Blueberry")
worksheet.cells.get("B3").put_value(2020)
worksheet.cells.get("C3").put_value(200)
worksheet.cells.get("A4").put_value("Kiwi")
worksheet.cells.get("B4").put_value(2020)
worksheet.cells.get("C4").put_value(300)
worksheet.cells.get("A5").put_value("Cherry")
worksheet.cells.get("B5").put_value(2020)
worksheet.cells.get("C5").put_value(400)
worksheet.cells.get("A6").put_value("Grape")
worksheet.cells.get("B6").put_value(2021)
worksheet.cells.get("C6").put_value(150)
worksheet.cells.get("A7").put_value("Blueberry")
worksheet.cells.get("B7").put_value(2021)
worksheet.cells.get("C7").put_value(250)
worksheet.cells.get("A8").put_value("Kiwi")
worksheet.cells.get("B8").put_value(2021)
worksheet.cells.get("C8").put_value(350)
worksheet.cells.get("A9").put_value("Cherry")
worksheet.cells.get("B9").put_value(2021)
worksheet.cells.get("C9").put_value(450)
# Добавить сводную таблицу с именем "Pivot1", расположенную в ячейке назначения E3, с источником A1:C9
pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]
# Назначить поля: Fruit в строки, Year в столбцы, Amount в данные
pivot_table.add_field_to_area(acp.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(acp.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(acp.PivotFieldType.DATA, "Amount")
# Изменить свойство представления/макета — это изменение только на уровне отображения,
# поэтому оно НЕ требует повторного чтения исходных данных через PivotCache.refresh().
pivot_table.refresh_data_on_opening_file = False
# calculate_data() повторно визуализирует отображение (данные + стили) ЭТОЙ сводной таблицы
# на основе данных, уже содержащихся в PivotCache. Поскольку исходные данные не изменились,
# обращения к источнику не происходит — в ячейках рабочего листа пересчитываются только
# закэшированные значения.
pivot_table.calculate_data()
# Сохранить рабочую книгу на диск
workbook.save("output.xlsx")
```

Рабочая книга часто содержит множество сводных таблиц, которые все расположены поверх одного общего кэша. Чтобы перечислить их — например, перед выполнением пакетного обновления или для диагностики влияния общего кэша — используйте `PivotCache.get_pivot_tables()`. Этот метод возвращает коллекцию каждой `PivotTable`, которая зависит от данного кэша.

## Миграция с устаревшего метода `PivotTable.refresh_data()`
До выхода Aspose.Cells for Python via .NET v26.7 стандартным способом обновления сводной таблицы был вызов `PivotTable.refresh_data()` на каждой сводной таблице по отдельности. Начиная с версии 26.7 этот метод помечен как **устаревший** и должен быть заменён описанными выше API с поддержкой кэша.
Существуют две причины, по которым подход с `refresh_data()` для каждой таблицы проблематичен в реальных рабочих книгах:
- Он повторно загружает данные из источника *при каждом* вызове, даже если источник не изменился.
Рекомендуемые замены:
В следующем примере демонстрируется новый эффективный шаблон для рабочих книг с несколькими сводными таблицами, использующими один общий кэш.

## Какой API обновления следует использовать?
В таблице ниже приведены доступные API обновления и случаи, когда следует выбирать каждый из них.
| Цель | Рекомендуемый API | Примечания |
|------|------------------|-----------|
| Обновить всё в рабочей книге | `Workbook.refresh_all()` | Один вызов; охватывает все кэши и таблицы. |
| Обновить только сводные таблицы на одном листе | `Worksheet.refresh_pivot_tables()` | Ограничено одним рабочим листом. |
| Исходные данные изменились для одного кэша | `pivot_table.pivot_cache.refresh()` | Обновляет ВСЕ сводные таблицы, использующие этот общий кэш. |
| Изменились только параметры представления/макета | `pivot_table.calculate_data()` | Пропускает ненужное обращение к источнику. |
| Перечислить все сводные таблицы на общем кэше | `pivot_cache.get_pivot_tables()` | Используется для перечисления перед массовым обновлением. |
На практике предпочтительнее использовать API на основе кэша вместо устаревшего `refresh_data()` для каждой таблицы. Они учитывают наличие общих кэшей, избегают избыточных обращений к источнику и позволяют выбрать минимальную область, удовлетворяющую требованию к обновлению.

## Распространённые ошибки
- **Забыли выполнить обновление перед сохранением.** Сводная таблица записывает свои отображаемые значения на рабочий лист только тогда, когда её цепочка данных обновлена. Если вы изменяете исходные ячейки, вызовите `PivotCache.refresh()` (или `Workbook.refresh_all()`) перед `Workbook.save()`, иначе сохранённый файл по-прежнему будет содержать старые агрегированные значения.
- **Вызов устаревшего `refresh_data()` для каждой таблицы.** В версии 26.7 метод `PivotTable.refresh_data()` помечен как устаревший и повторно загружает данные из источника при каждом вызове. При наличии нескольких сводных таблиц, использующих общий кэш, это приводит к N избыточным обращениям к источнику. Замените его единственным вызовом `PivotCache.refresh()` с последующим вызовом `calculate_data()` для каждой таблицы.
- **Обновление при изменении только макета.** Если вы изменили только представление сводной таблицы (порядок столбцов, `ConsolidationFunction` и т. д.), не затрагивая исходные данные, вызов `PivotCache.refresh()` не нужен и работает медленно. Вызовите `pivotTable.calculate_data()` для повторной визуализации из существующего кэша.
- **Внешний источник не поддерживается `PivotCache.refresh()`.** Если источник сводной таблицы поступает из внешнего подключения (база данных, OLAP-куб и т. д.), `PivotCache.refresh()` не может обновить его в версии 26.7 — в настоящее время он поддерживает только типы источников `Sheet` и `Consolidation`. Для внешних источников заново откройте рабочую книгу или перестройте кэш из источника.

{{< app/cells/assistant language="python-net" >}}
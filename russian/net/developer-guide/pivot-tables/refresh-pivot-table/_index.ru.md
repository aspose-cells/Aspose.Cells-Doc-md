---
title: Обновление сводных таблиц и кэшей сводных таблиц в Aspose.Cells for .NET
linktitle: Обновление сводных таблиц и кэшей сводных таблиц в Aspose.Cells for .NET
description: Узнайте, как обновлять сводные таблицы в Aspose.Cells for .NET с помощью API обновления сводных таблиц версии 26.7+. В этой статье рассматриваются RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData и GetPivotTables с практическими примерами кода.
keywords: Aspose.Cells, .NET, сводная таблица, обновление, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ru/net/refresh-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells предоставляет многоуровневый API обновления, который позволяет перезагружать данные сводных таблиц в четырёх различных областях — от всей рабочей книги до одной сводной таблицы. Начиная с **Aspose.Cells for .NET v26.7**, устаревший метод `PivotTable.RefreshData()` помечен как нерекомендуемый и должен быть заменён более эффективными API с поддержкой кэша, описанными в этой статье.
{{% /alert %}}

## Введение
Обновление сводной таблицы редко представляет собой одну операцию. За кулисами Aspose.Cells поддерживает многоуровневую цепочку данных, которая соединяет исходные данные с отображаемыми значениями, которые вы видите на рабочем листе. Понимание этой цепочки является ключом к выбору правильного API обновления для любой ситуации.
Цепочка данных из четырёх уровней выглядит так:
1. **Источник данных** — исходные диапазоны рабочего листа, запрос к базе данных или диапазон консолидации, где находятся необработанные значения.
2. **PivotCache** — снимок исходных данных в памяти. Каждая сводная таблица строится поверх `PivotCache`; именно здесь все данные собираются и агрегируются.
3. **PivotTable** — объект представления, который определяет поля строк, столбцов, значений и фильтров. `PivotTable` читает *только* из своего `PivotCache`, никогда напрямую из источника данных.
4. **Cells** — объект `Cells` рабочего листа, в который `PivotTable` отображает вычисленные значения и стили.

{{% alert color="primary" %}}
`PivotCache.SourceType` (перечисление `PivotTableSourceType`) указывает, откуда поступили данные кэша. Начиная с версии 26.7, метод `PivotCache.Refresh()` поддерживает только типы источников **`Sheet`** и **`Consolidation`** — то есть данные, которые находятся в диапазонах рабочего листа. Внешние источники (базы данных, внешние подключения и т. д.) пока не могут быть обновлены через API кэша.
{{% /alert %}}

Из-за этой цепочки в Aspose.Cells существуют два фундаментальных пути обновления:
- **`PivotTable.CalculateData()`** — пересчитывает отображение одной `PivotTable` из уже кэшированных данных, без обращения к источнику данных.
Все сценарии в этой статье используют данные из ячеек рабочего листа, поэтому тип источника — `Sheet`, и операции обновления работают, как описано.

## Быстрый старт
Если вам нужен только самый короткий код, который обновляет все сводные таблицы в рабочей книге, достаточно одного вызова:

```csharp
using Aspose.Cells;
Workbook workbook = new Workbook("input.xlsx");
workbook.RefreshAll();
workbook.Save("output.xlsx");
```

Всё остальное в этой статье объясняет, когда следует выбрать более узкий API.

## Необходимые директивы Using
Все примеры C# в этой статье начинаются со следующих трёх директив using, поскольку типы сводных таблиц находятся в пространстве имён `Aspose.Cells.Pivot`:
- `using System;`
- `using Aspose.Cells;`
- `using Aspose.Cells.Pivot;`

## Обновление всех сводных таблиц в рабочей книге
Когда вам нужно убедиться, что каждый кэш сводной таблицы и каждая сводная таблица в рабочей книге отражают последние исходные данные, самым простым и комплексным API является `Workbook.RefreshAll()`. Один вызов проходит через всю рабочую книгу — обновляя каждый `PivotCache` из его источника, а затем пересчитывая каждую зависимую `PivotTable`. Это рекомендуемый подход для общих полных обновлений документа, когда производительность не вызывает беспокойства.
Следующий пример создаёт рабочую книгу с диапазоном источника Fruit/Year/Amount, создаёт одну сводную таблицу, изменяет некоторые значения источника, а затем использует `RefreshAll()` для обновления всего одной командой.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// Создать новую рабочую книгу
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// Записать строку заголовка в ячейки A1:C1
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");
// Записать строки данных в ячейки A2:C9 (8 строк данных о фруктах за 2020 и 2021 годы)
worksheet.Cells["A2"].PutValue("grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(50);
worksheet.Cells["A3"].PutValue("blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(60);
worksheet.Cells["A4"].PutValue("kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(70);
worksheet.Cells["A5"].PutValue("cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(80);
worksheet.Cells["A6"].PutValue("grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(90);
worksheet.Cells["A7"].PutValue("blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(100);
worksheet.Cells["A8"].PutValue("kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(110);
worksheet.Cells["A9"].PutValue("cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(120);
// Добавить сводную таблицу: исходный диапазон "A1:C9", ячейка назначения "E3", имя "Pivot1"
int pivotIndex = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];
// Назначить поля сводной таблицы: Fruit — в строки, Year — в столбцы, Amount — в данные
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// Изменить несколько значений Amount в исходных данных для имитации изменений
worksheet.Cells["C2"].PutValue(55);
worksheet.Cells["C5"].PutValue(85);
worksheet.Cells["C9"].PutValue(125);
// Обновить все сводные таблицы / кэш сводных таблиц в рабочей книге
workbook.RefreshAll();
// Сохранить рабочую книгу
workbook.Save("output.xlsx");
```

## Обновление всех сводных таблиц на одном рабочем листе
Иногда вам нужно обновить только сводные таблицы, которые находятся на одном конкретном рабочем листе — например, когда известно, что сводные таблицы на других листах не связаны с ними и не должны быть затронуты. Для этого случая Aspose.Cells предоставляет `Worksheet.RefreshPivotTables()`, который ограничен одним экземпляром `Worksheet`.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");
worksheet.Cells["A2"].PutValue("grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(100);
worksheet.Cells["A3"].PutValue("blueberry");
worksheet.Cells["B3"].PutValue(2021);
worksheet.Cells["C3"].PutValue(150);
worksheet.Cells["A4"].PutValue("kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(200);
worksheet.Cells["A5"].PutValue("cherry");
worksheet.Cells["B5"].PutValue(2021);
worksheet.Cells["C5"].PutValue(120);
worksheet.Cells["A6"].PutValue("grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(180);
worksheet.Cells["A7"].PutValue("blueberry");
worksheet.Cells["B7"].PutValue(2020);
worksheet.Cells["C7"].PutValue(130);
worksheet.Cells["A8"].PutValue("kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(220);
worksheet.Cells["A9"].PutValue("cherry");
worksheet.Cells["B9"].PutValue(2020);
worksheet.Cells["C9"].PutValue(140);
int pivotIndex = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
worksheet.Cells["C2"].PutValue(300);
worksheet.Cells["C5"].PutValue(250);
worksheet.Cells["C9"].PutValue(400);
worksheet.RefreshPivotTables();
workbook.Save("output.xlsx");
```

## Обновление одной сводной таблицы
Когда вам нужен детальный контроль над одной сводной таблицей, API на основе кэша предоставляет два варианта. Выбор между ними зависит от того, что именно изменилось: базовые исходные данные или только параметры представления/макета самой сводной таблицы.

### Исходные данные изменились — используйте `PivotCache.Refresh()`
Если базовые исходные данные изменились, правильной точкой входа является `pivotTable.PivotCache.Refresh()`. Этот вызов перечитывает исходные данные в кэш, а затем пересчитывает каждую `PivotTable`, которая зависит от этого кэша.

### Изменились только представление/макет — используйте `CalculateData()`
Если исходные данные *не* изменились, а были изменены только параметры представления или макета сводной таблицы (например, поле было перемещено в другую область или переключена настройка обновления при открытии), нет необходимости обращаться обратно к источнику данных. В кэше уже находятся правильные данные; необходим только пересчёт отображаемой `PivotTable`. В этом случае `pivotTable.CalculateData()` является правильным выбором.
Следующий пример изменяет свойство сводной таблицы, не связанное с источником, а затем вызывает `CalculateData()` для её повторного отображения из существующего кэша.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;
var workbook = new Workbook();
var worksheet = workbook.Worksheets[0];
// Записать строку заголовка Fruit / Year / Amount
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");
// Записать 8 строк данных (строки 2-9, соответствует исходному диапазону A1:C9)
worksheet.Cells["A2"].PutValue("Grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(100);
worksheet.Cells["A3"].PutValue("Blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(200);
worksheet.Cells["A4"].PutValue("Kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(300);
worksheet.Cells["A5"].PutValue("Cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(400);
worksheet.Cells["A6"].PutValue("Grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(150);
worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(250);
worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(350);
worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(450);
// Добавить сводную таблицу с именем "Pivot1", размещённую в ячейке E3, с источником A1:C9
int pivotIndex = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.PivotTables[pivotIndex];
// Назначить поля: Fruit в строки, Year в столбцы, Amount в данные
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// Изменить свойство представления/макета — это изменение только отображения,
// поэтому оно НЕ требует повторного чтения исходных данных через PivotCache.Refresh().
pivotTable.RefreshDataOnOpeningFile = false;
// CalculateData() перерисовывает отображение ЭТОЙ сводной таблицы (данные + стиль) из
// данных, уже хранящихся в PivotCache. Поскольку исходные данные не изменились,
// обращения к источнику не происходит — пересчитываются только кэшированные значения
// в ячейки листа.
pivotTable.CalculateData();
// Сохранить книгу на диск
workbook.Save("output.xlsx");
```

Рабочая книга часто содержит много сводных таблиц, которые все построены поверх одного общего кэша. Чтобы перечислить их — например, перед выполнением пакетного обновления или для диагностики влияния общего кэша — используйте `PivotCache.GetPivotTables()`. Этот метод возвращает коллекцию каждой `PivotTable`, которая зависит от данного кэша.

## Переход с устаревшего `PivotTable.RefreshData()`
До Aspose.Cells for .NET v26.7 стандартным способом обновления сводной таблицы был вызов `PivotTable.RefreshData()` для каждой сводной таблицы по отдельности. Начиная с версии 26.7, этот метод помечен как **устаревший** и должен быть заменён API с поддержкой кэша, описанными выше.
Существуют две причины, по которым подход с потабличным вызовом `RefreshData()` является проблематичным в реальных рабочих книгах:
- Он повторно извлекает данные из источника *при каждом* вызове, даже если источник не изменился.
Рекомендуемые замены:
Следующий пример демонстрирует новый эффективный шаблон для рабочих книг с несколькими сводными таблицами, использующими один кэш.

## Какой API обновления следует использовать?
В таблице ниже приведены доступные API обновления и случаи, когда следует выбирать каждый из них.
| Цель | Рекомендуемый API | Примечания |
|------|------------------|-----------|
| Обновить всё в рабочей книге | `Workbook.RefreshAll()` | Один вызов; охватывает все кэши и таблицы. |
| Обновить только сводные таблицы на одном листе | `Worksheet.RefreshPivotTables()` | Ограничено одним рабочим листом. |
| Исходные данные для одного кэша изменились | `pivotTable.PivotCache.Refresh()` | Обновляет ВСЕ сводные таблицы на этом общем кэше. |
| Изменились только параметры представления/макета | `pivotTable.CalculateData()` | Пропускает ненужный запрос к источнику. |
| Вывести список всех сводных таблиц на общем кэше | `pivotCache.GetPivotTables()` | Используется для перечисления перед массовым обновлением. |
На практике предпочтительнее использовать API на основе кэша, а не устаревший потабличный `RefreshData()`. Они учитывают общие кэши, избегают избыточных запросов к источнику и позволяют выбрать наименьшую область, удовлетворяющую вашим требованиям к обновлению.

## Распространённые ошибки
- **Забыли обновить перед сохранением.** Сводная таблица записывает свои отображаемые значения в рабочий лист только при обновлении её цепочки данных. Если вы изменили ячейки источника, вызовите `PivotCache.Refresh()` (или `Workbook.RefreshAll()`) перед `Workbook.Save()`, иначе сохранённый файл по-прежнему будет содержать старые агрегированные значения.
- **Вызов устаревшего `RefreshData()` для каждой таблицы.** В версии 26.7 метод `PivotTable.RefreshData()` помечен как устаревший и повторно извлекает источник при каждом вызове. Если несколько сводных таблиц используют общий кэш, это означает N избыточных запросов к источнику. Замените на однократный вызов `PivotCache.Refresh()`, за которым следует `CalculateData()` для каждой таблицы.
- **Обновление при изменении только макета.** Если вы изменили только представление сводной таблицы (порядок столбцов, `ConsolidationFunction` и т. д.), не затрагивая исходные данные, вызов `PivotCache.Refresh()` не нужен и работает медленно. Вызовите `pivotTable.CalculateData()` для повторного отображения из существующего кэша.
- **Внешний источник не поддерживается `PivotCache.Refresh()`.** Если источник сводной таблицы поступает из внешнего подключения (база данных, OLAP-куб и т. д.), `PivotCache.Refresh()` не может обновить его в версии 26.7 — в настоящее время он поддерживает только типы источников `Sheet` и `Consolidation`. Для внешних источников заново откройте рабочую книгу или перестройте кэш из источника.

{{< app/cells/assistant language="csharp" >}}
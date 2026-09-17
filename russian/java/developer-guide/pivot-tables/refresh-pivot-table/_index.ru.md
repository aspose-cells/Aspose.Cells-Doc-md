---
title: Обновление сводных таблиц и кэшей сводных таблиц в Aspose.Cells for Java
linktitle: Обновление сводных таблиц и кэшей сводных таблиц в Aspose.Cells for Java
description: Узнайте, как обновлять сводные таблицы в Aspose.Cells for Java с помощью API обновления сводных таблиц v26.7+. В этой статье рассматриваются RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData и GetPivotTables с практическими примерами кода.
keywords: Aspose.Cells, Java, сводная таблица, обновление, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ru/java/refresh-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells предоставляет многоуровневый API обновления, который позволяет перезагружать данные сводных таблиц на четырёх различных уровнях — от всей рабочей книги до отдельной сводной таблицы. Начиная с версии **Aspose.Cells for Java v26.7**, устаревший метод `PivotTable.refreshData()` помечен как устаревший (obsolete) и должен быть заменён более эффективными API с поддержкой кэша, описанными в данной статье.
{{% /alert %}}

## Введение
Обновление сводной таблицы редко представляет собой одну операцию. За кулисами Aspose.Cells поддерживает многоуровневую цепочку данных, которая соединяет исходные данные с отображаемыми значениями, которые вы видите на рабочем листе. Понимание этой цепочки является ключом к выбору правильного API обновления для любой ситуации.
Цепочка данных состоит из четырёх уровней:
1. **Источник данных** — исходные диапазоны рабочего листа, запрос к базе данных или диапазон консолидации, где находятся необработанные значения.
2. **PivotCache** — снимок исходных данных в памяти. Каждая сводная таблица построена поверх `PivotCache`; именно здесь собираются и агрегируются все данные.
3. **PivotTable** — объект представления, определяющий поля строк, столбцов, значений и фильтров. `PivotTable` читает данные *только* из своего `PivotCache`, но никогда напрямую из источника данных.
4. **Cells** — коллекция `Cells` рабочего листа, в которую `PivotTable` выводит вычисленные значения и стили.

{{% alert color="primary" %}}
`PivotCache.getSourceType()` (перечисление `PivotTableSourceType`) указывает, откуда были получены данные кэша. Начиная с версии v26.7, `PivotCache.refresh()` поддерживает только типы источников **`Sheet`** и **`Consolidation`** — то есть данные, которые находятся в диапазонах рабочего листа. Внешние источники (базы данных, внешние подключения и т. д.) пока не могут быть обновлены через API кэша.
{{% /alert %}}

Из-за этой цепочки в Aspose.Cells существуют два основных пути обновления:
- **`PivotTable.calculateData()`** — пересчитывает отображение одной `PivotTable` из уже кэшированных данных без обращения к источнику данных.
Все сценарии в этой статье используют данные из ячеек рабочего листа, поэтому тип источника — `Sheet`, и операции обновления работают, как описано.

## Быстрый старт
Если вам нужен лишь минимально возможный код, который обновляет все сводные таблицы в рабочей книге, достаточно одного вызова:

```java
import com.aspose.cells.*;
// Создать новую рабочую книгу
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// Записать строку заголовков в ячейки A1:C1
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
// Добавить сводную таблицу: исходный диапазон "A1:C9", ячейка назначения "E3", имя "Pivot1"
int pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Назначить поля сводной таблицы: Fruit в строки, Year в столбцы, Amount в данные
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// Изменить несколько значений Amount в исходных данных для имитации изменений
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);
// Обновить все сводные таблицы / кэш сводных таблиц в рабочей книге
workbook.refreshAll();
// Сохранить рабочую книгу
workbook.save("output.xlsx");
```

Всё остальное в этой статье объясняет, когда следует выбирать более узкий API.

## Необходимые операторы импорта
Все примеры на Java в этой статье начинаются со следующих операторов импорта, поскольку типы сводных таблиц находятся в пакете `com.aspose.cells.pivot`:
- `import java.lang.System;`
- `import com.aspose.cells.Workbook;`
- `import com.aspose.cells.pivot.*;`

## Обновление всех сводных таблиц в рабочей книге
Когда вам нужно обеспечить, чтобы каждый кэш сводной таблицы и каждая сводная таблица в рабочей книге отражали самые актуальные исходные данные, самым простым и всеобъемлющим API является `Workbook.refreshAll()`. Один вызов обходит всю рабочую книгу — обновляя каждый `PivotCache` из его источника, а затем пересчитывая каждую зависимую `PivotTable`. Это рекомендуемый подход для общих полных обновлений документа, когда производительность не критична.
Следующий пример создаёт рабочую книгу с диапазоном источника Fruit/Year/Amount, создаёт одну сводную таблицу, изменяет некоторые значения источника, а затем использует `refreshAll()` для приведения всего в актуальное состояние одним вызовом.

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
int pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
worksheet.getCells().get("C2").putValue(300);
worksheet.getCells().get("C5").putValue(250);
worksheet.getCells().get("C9").putValue(400);
worksheet.refreshPivotTables();
workbook.save("output.xlsx");
```

## Обновление всех сводных таблиц на одном рабочем листе
Иногда требуется обновить только сводные таблицы, расположенные на конкретном рабочем листе — например, когда известно, что сводные таблицы на других рабочих листах не связаны и их не следует трогать. Для этого случая Aspose.Cells предоставляет метод `Worksheet.refreshPivotTables()`, который ограничен одним экземпляром `Worksheet`.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// Записать строку заголовка Fruit / Year / Amount
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// Записать 8 строк данных (строки 2-9, соответствует исходному диапазону A1:C9)
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
// Добавить сводную таблицу с именем "Pivot1", размещённую в ячейке назначения E3, с источником A1:C9
int pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Назначить поля: Fruit в строки, Year в столбцы, Amount в данные
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// Изменить свойство представления/макета -- это изменение только для отображения,
// поэтому оно НЕ требует повторного чтения исходных данных через PivotCache.Refresh().
pivotTable.setRefreshDataOnOpeningFile(false);
// calculateData() перерисовывает отображение ЭТОЙ сводной таблицы (данные + стиль) из
// данных, уже хранящихся в PivotCache. Поскольку исходные данные не изменились,
// обратное обращение к источнику не выполняется -- только кэшированные значения пересчитываются
// в ячейки рабочего листа.
pivotTable.calculateData();
// Сохранить рабочую книгу на диск
workbook.save("output.xlsx");
```

## Обновление одной сводной таблицы
Когда вам нужен точечный контроль над отдельной сводной таблицей, API на основе кэша предоставляет два варианта. Выбор между ними зависит от того, что именно изменилось: исходные данные или только настройки представления/макета самой сводной таблицы.

### Изменились исходные данные — используйте `PivotCache.refresh()`
Если изменились исходные данные, правильной точкой входа является `pivotTable.getPivotCache().refresh()`. Этот вызов перечитывает исходные данные в кэш, а затем пересчитывает каждую `PivotTable`, зависящую от этого кэша.

### Изменились только представление/макет — используйте `calculateData()`
Если исходные данные *не* изменились, но изменились только настройки представления или макета сводной таблицы (например, поле было перемещено в другую область или переключена настройка обновления при открытии), нет необходимости обращаться к источнику данных. Кэш уже содержит правильные данные; требуется пересчёт только отображаемой `PivotTable`. В этом случае `pivotTable.calculateData()` является правильным выбором.
Следующий пример изменяет свойство сводной таблицы, не связанное с источником, а затем вызывает `calculateData()` для её повторного отображения из существующего кэша.
Рабочая книга часто содержит множество сводных таблиц, которые все построены поверх одного общего кэша. Чтобы перечислить их — например, перед выполнением пакетного обновления или для диагностики влияния общего кэша — используйте `PivotCache.getPivotTables()`. Этот метод возвращает коллекцию всех `PivotTable`, зависящих от данного кэша.

## Миграция с устаревшего метода `PivotTable.refreshData()`
До версии Aspose.Cells for Java v26.7 стандартным способом обновления сводной таблицы был вызов `PivotTable.refreshData()` для каждой сводной таблицы по отдельности. Начиная с версии v26.7, этот метод помечен как устаревший (obsolete) и должен быть заменён API с поддержкой кэша, описанными выше.
Существуют две причины, по которым подход с вызовом `refreshData()` для каждой таблицы проблематичен в реальных рабочих книгах:
- Он повторно извлекает данные из источника *при каждом* вызове, даже если источник не изменился.
Рекомендуемые замены:
Следующий пример демонстрирует новый эффективный шаблон для рабочих книг с несколькими сводными таблицами, использующими один кэш.

## Какой API обновления следует использовать?
В таблице ниже приведены доступные API обновления и случаи, когда следует выбирать каждый из них.
| Цель | Рекомендуемый API | Примечания |
|------|-----------------|-------|
| Обновить всё в рабочей книге | `Workbook.refreshAll()` | Один вызов; охватывает все кэши и таблицы. |
| Обновить только сводные таблицы на одном листе | `Worksheet.refreshPivotTables()` | Ограничено одним рабочим листом. |
| Изменились исходные данные для одного кэша | `pivotTable.getPivotCache().refresh()` | Обновляет ВСЕ сводные таблицы на этом общем кэше. |
| Изменились только настройки представления/макета | `pivotTable.calculateData()` | Пропускает ненужный запрос к источнику. |
| Получить список всех сводных таблиц на общем кэше | `pivotCache.getPivotTables()` | Используется для перечисления перед массовым обновлением. |
На практике предпочтительнее использовать API на основе кэша вместо устаревшего `refreshData()` для каждой таблицы. Они учитывают общие кэши, избегают избыточных обращений к источнику и позволяют выбрать минимальный объём обновления, удовлетворяющий вашим требованиям.

## Распространённые ошибки
- **Забыли обновить перед сохранением.** Сводная таблица записывает свои отображаемые значения на рабочий лист только тогда, когда обновлена её цепочка данных. Если вы изменяете исходные ячейки, вызовите `PivotCache.Refresh()` (или `Workbook.RefreshAll()`) перед `Workbook.save()`, иначе сохранённый файл по-прежнему будет содержать старые агрегированные значения.
- **Вызов устаревшего метода `RefreshData()` для каждой таблицы.** В версии v26.7 метод `PivotTable.RefreshData()` помечен как устаревший (obsolete) и повторно извлекает данные из источника при каждом вызове. При наличии нескольких сводных таблиц, использующих общий кэш, это означает N избыточных обращений к источнику. Замените его одним вызовом `PivotCache.Refresh()`, за которым следует `CalculateData()` для каждой таблицы.
- **Обновление при изменении только макета.** Если вы изменили только представление сводной таблицы (порядок столбцов, `ConsolidationFunction` и т. д.) без изменения исходных данных, вызов `PivotCache.Refresh()` не нужен и замедляет работу. Вызовите `pivotTable.CalculateData()` для повторного отображения из существующего кэша.
- **Внешний источник не поддерживается `PivotCache.Refresh()`.** Если источник сводной таблицы поступает из внешнего подключения (база данных, OLAP-куб и т. д.), `PivotCache.Refresh()` не сможет обновить его в версии v26.7 — в настоящее время он поддерживает только типы источников `Sheet` и `Consolidation`. Для внешних источников заново откройте рабочую книгу или перестройте кэш из источника.

```csharp
using Aspose.Cells;
Workbook workbook = new Workbook("input.xlsx");
workbook.RefreshAll();
workbook.Save("output.xlsx");
```

{{< app/cells/assistant language="java" >}}
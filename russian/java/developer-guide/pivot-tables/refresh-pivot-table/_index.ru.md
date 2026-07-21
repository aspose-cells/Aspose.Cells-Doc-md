---
title: Обновление сводных таблиц в Aspose.Cells for Java
linktitle: Обновление сводных таблиц в Aspose.Cells for Java
description: Узнайте, как обновлять сводные таблицы в Aspose.Cells for Java с использованием API обновления сводных таблиц v26.7+. В этой статье рассматриваются методы RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData и GetPivotTables с практическими примерами кода.
keywords: Aspose.Cells, Java, сводная таблица, обновление, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ru/java/refresh-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells предоставляет многоуровневый API обновления, который позволяет перезагружать данные сводных таблиц на четырёх различных уровнях — от всей рабочей книги до одной сводной таблицы. Начиная с версии **Aspose.Cells for Aspose.Cells for Java v26.7**, устаревший метод `PivotTable.refreshData()` помечен как нерекомендуемый и должен быть заменён более эффективными, учитывающими кэш API, описанными в этой статье.

{{% /alert %}}

## Введение

Обновление сводной таблицы редко является единственной операцией. За кулисами Aspose.Cells поддерживает многоуровневую цепочку данных, которая связывает исходные данные с отображаемыми значениями, которые вы видите на рабочем листе. Понимание этой цепочки является ключом к выбору правильного API обновления для любой ситуации.

Цепочка данных состоит из четырёх уровней:

1. **Источник данных** — исходные диапазоны рабочего листа, запрос к базе данных или диапазон консолидации, в которых хранятся необработанные значения.
2. **PivotCache** — снимок исходных данных в оперативной памяти. Каждая сводная таблица построена поверх `PivotCache`; именно здесь все данные собираются и агрегируются.
3. **PivotTable** — объект представления, который определяет поля строк, столбцов, значений и фильтров. `PivotTable` считывает данные *только* из своего `PivotCache`, никогда не напрямую из источника данных.
4. **Cells** — коллекция `Cells` рабочего листа, в которую `PivotTable` выводит вычисленные значения и стили.

Особенно важной концепцией является **общий кэш**. Когда несколько сводных таблиц в рабочей книге ссылаются на один и тот же диапазон источника, они используют *один* экземпляр `PivotCache`. На один `PivotCache` может ссылаться множество сводных таблиц, и обновление этого кэша обновляет все зависимые `PivotTable` одновременно.

{{% alert color="primary" %}}

`PivotCache.getSourceType()` (перечисление `PivotTableSourceType`) указывает, откуда пришли данные кэша. Начиная с версии 26.7, `PivotCache.refresh()` поддерживает только типы источников **`Sheet`** и **`Consolidation`** — то есть данные, которые находятся в диапазонах рабочего листа. Внешние источники (базы данных, внешние подключения и т. д.) пока не могут быть обновлены через API кэша.

{{% /alert %}}

Из-за этой цепочки в Aspose.Cells существуют два основных пути обновления:

- **`PivotCache.refresh()`** — перезагружает источник → кэш И пересчитывает все зависимые `PivotTable` за одну операцию.
- **`PivotTable.calculateData()`** — пересчитывает отображение одной `PivotTable` из уже закэшированных данных, без обращения к источнику данных.

Во всех сценариях этой статьи используются исходные данные из ячеек рабочего листа, поэтому тип источника — `Sheet`, и операции обновления работают, как описано.

## Необходимые операторы импорта

Во всех примерах Java в этой статье используются следующие операторы импорта, поскольку типы сводных таблиц находятся в пакете `com.aspose.cells.pivot`:

- `import java.lang.System;`
- `import com.aspose.cells.Workbook;`
- `import com.aspose.cells.pivot.*;`

## Обновление всех сводных таблиц в рабочей книге

Если вам нужно убедиться, что каждый сводный кэш и каждая сводная таблица в рабочей книге отражают самые последние исходные данные, самым простым и комплексным API является `Workbook.refreshAll()`. Один вызов проходит по всей рабочей книге — обновляет каждый `PivotCache` из его источника, а затем пересчитывает каждую зависимую `PivotTable`. Это рекомендуемый подход для общих полнотекстовых обновлений, когда производительность не критична.

Следующий пример создаёт рабочую книгу с диапазоном источника Fruit/Year/Amount, создаёт одну сводную таблицу, изменяет некоторые исходные значения, а затем использует `refreshAll()`, чтобы привести всё в актуальное состояние за один вызов.

```java
import com.aspose.cells.*;

// Создать новую рабочую книгу
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// Записать строку заголовка в ячейки A1:C1
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

// Обновить все сводные таблицы / кэши сводных таблиц в рабочей книге
workbook.refreshAll();

// Сохранить рабочую книгу
workbook.save("output.xlsx");
```

## Обновление всех сводных таблиц на одном рабочем листе

Иногда вам нужно обновить только те сводные таблицы, которые находятся на одном конкретном рабочем листе, — например, когда известно, что сводные таблицы на других рабочих листах не связаны и их не нужно трогать. Для этого случая Aspose.Cells предоставляет метод `Worksheet.refreshPivotTables()`, который ограничен одним экземпляром `Worksheet`.

Это более избирательно, чем `Workbook.refreshAll()`: обновляются только сводные таблицы на целевом рабочем листе, а сводные таблицы на других листах остаются нетронутыми.

Следующий пример заполняет те же исходные данные Fruit/Year/Amount, добавляет сводную таблицу на первый рабочий лист, изменяет некоторые исходные значения, а затем обновляет только сводные таблицы на этом рабочем листе.

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

## Обновление одной сводной таблицы

Если вам нужен тонкий контроль над одной сводной таблицей, API на основе кэша предоставляет два варианта. Выбор между ними зависит от того, что именно изменилось: базовые исходные данные или только параметры представления/макета самой сводной таблицы.

### Изменились исходные данные — используйте `PivotCache.refresh()`

Если изменились базовые исходные данные, правильной точкой входа является `pivotTable.getPivotCache().refresh()`. Этот вызов перечитывает исходные данные в кэш, а затем пересчитывает все `PivotTable`, зависящие от этого кэша.

{{% alert color="primary" %}}

Поскольку сводные таблицы используют один экземпляр `PivotCache`, вызов `PivotCache.refresh()` пересчитывает **все** сводные таблицы, построенные на этом же кэше, — а не только ту, на которую вы ссылаетесь. Если две сводные таблицы используют один и тот же диапазон источника, обновление одного кэша обновляет обе.

{{% /alert %}}

Следующий пример создаёт две сводные таблицы на одном диапазоне источника, чтобы продемонстрировать это поведение с общим кэшем, изменяет некоторые исходные значения, а затем выполняет обновление через одну ссылку на кэш.

```java
import com.aspose.cells.*;

// Создать новую рабочую книгу и получить доступ к первому листу
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// Записать строку заголовка: Фрукт / Год / Количество
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// Записать примерно 9 строк данных (виноград / черника / киви / вишня за 2020-2021 годы)
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
worksheet.getCells().get("C6").putValue(500);

worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(600);

worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(700);

worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(800);

// Добавить первую сводную таблицу "Pivot1" с якорем в ячейке E3, исходный диапазон A1:C9
int pivotIndex1 = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable1 = worksheet.getPivotTables().get(pivotIndex1);

// Назначить поля для Pivot1
pivotTable1.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable1.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable1.addFieldToArea(PivotFieldType.DATA, "Amount");

// Добавить ВТОРУЮ сводную таблицу "Pivot2" с якорем в E15, используя ТОТ ЖЕ исходный диапазон A1:C9
// Pivot1 и Pivot2 совместно используют один PivotCache, так как исходный диапазон идентичен.
int pivotIndex2 = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
PivotTable pivotTable2 = worksheet.getPivotTables().get(pivotIndex2);

// Назначить те же поля для Pivot2
pivotTable2.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable2.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable2.addFieldToArea(PivotFieldType.DATA, "Amount");

// Изменить несколько значений ячеек Amount в исходных данных для имитации изменения данных
worksheet.getCells().get("C2").putValue(150);
worksheet.getCells().get("C4").putValue(350);
worksheet.getCells().get("C7").putValue(650);

// Обновить общий PivotCache.
// Поскольку Pivot1 и Pivot2 совместно используют один PivotCache, этот единственный вызов
// обновляет ОБЕ сводные таблицы (данные + стиль) из обновлённого источника.
pivotTable1.refreshData();

// Сохранить рабочую книгу
workbook.save("output.xlsx");
```

### Изменились только представление/макет — используйте `calculateData()`

Если исходные данные *не* изменились, но изменились только параметры представления или макета сводной таблицы (например, поле было перемещено в другую область, или был переключён параметр обновления при открытии файла), нет необходимости возвращаться к источнику данных. Кэш уже содержит правильные данные; нужно только пересчитать отображаемую `PivotTable`. В этом случае правильным выбором является `pivotTable.calculateData()`.

Это позволяет избежать ненужного обращения к источнику и значительно быстрее, когда многие сводные таблицы используют один и тот же кэш.

Следующий пример изменяет свойство сводной таблицы, не связанное с источником, а затем вызывает `calculateData()` для её повторной отрисовки из существующего кэша.

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

// Добавить сводную таблицу с именем "Pivot1", размещённую в ячейке E3, с источником данных A1:C9
int pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Назначить поля: Fruit в строки, Year в столбцы, Amount в данные
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

// Изменить свойство представления/макета -- это изменение только для отображения,
// поэтому оно НЕ требует повторного чтения исходных данных через PivotCache.Refresh().
pivotTable.setRefreshDataOnOpeningFile(false);

// calculateData() повторно отображает представление ЭТОЙ сводной таблицы (данные + стиль) из
// данных, уже хранящихся в PivotCache. Поскольку исходные данные не изменились,
// обращение к источнику не выполняется -- только кэшированные значения пересчитываются
// в ячейки листа.
pivotTable.calculateData();

// Сохранить книгу на диск
workbook.save("output.xlsx");
```

## Получение всех сводных таблиц, использующих один и тот же PivotCache

Рабочая книга часто содержит много сводных таблиц, которые все построены поверх одного общего кэша. Чтобы их перечислить, — например, перед выполнением пакетного обновления или для диагностики влияния общего кэша — используйте `PivotCache.getPivotTables()`. Этот метод возвращает коллекцию всех `PivotTable`, зависящих от данного кэша.

Это также самый прямой способ подтвердить, что две сводные таблицы действительно используют один и тот же экземпляр `PivotCache`: можно сравнить ссылки на кэш (используя оператор `==`), или просто перебрать коллекцию, возвращаемую методом `getPivotTables()`, и посмотреть, какие сводные таблицы в ней появляются.

Следующий пример создаёт две сводные таблицы на одном диапазоне источника, проверяет, что они используют один и тот же экземпляр кэша, а затем перечисляет сводные таблицы этого кэша.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Sheet1");

worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

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
worksheet.getCells().get("C6").putValue(500);

worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(600);

worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(700);

worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(800);

worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021);
worksheet.getCells().get("C10").putValue(900);

int pivot1Index = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable1 = worksheet.getPivotTables().get(pivot1Index);
pivotTable1.addFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(PivotFieldType.Data, "Amount");

int pivot2Index = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
PivotTable pivotTable2 = worksheet.getPivotTables().get(pivot2Index);
pivotTable2.addFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(PivotFieldType.Data, "Amount");

boolean sameCache = pivotTable1.getPivotCache() == pivotTable2.getPivotCache();
System.out.println("Pivot1 and Pivot2 share the same PivotCache: " + sameCache);

PivotTable[] sharedPivotTables = pivotTable1.getPivotCache().getPivotTables();
System.out.println("Number of pivot tables sharing the cache: " + sharedPivotTables.length);

for (PivotTable pt : sharedPivotTables)
{
    System.out.println("Pivot table name: " + pt.getName());
}

workbook.save("output.xlsx");
```

## Миграция с устаревшего `PivotTable.refreshData()`

До версии Aspose.Cells for Aspose.Cells for Java v26.7 стандартным способом обновления сводной таблицы был вызов `PivotTable.refreshData()` для каждой сводной таблицы отдельно. Начиная с версии 26.7, этот метод помечен как **устаревший** и должен быть заменён описанными выше API с поддержкой кэша.

Есть две причины, по которым подход с отдельным вызовом `refreshData()` для каждой таблицы является проблематичным в реальных рабочих книгах:

- Он повторно извлекает данные из источника *при каждом* вызове, даже если источник не изменился.
- Каждый вызов обновляет весь общий кэш. Когда многие сводные таблицы используют один кэш, повторные вызовы `refreshData()` для каждой сводной таблицы приводят к многократному повторному извлечению одного и того же кэша, что очень медленно.

Рекомендуемые замены:

- **Обновление ВСЕХ сводных таблиц в рабочей книге** → используйте `workbook.refreshAll();`
- **Обновление НЕКОТОРЫХ из них** → используйте `pivotTable.getPivotCache().refresh();` для одного кэша. Поскольку кэш общий, этот единственный вызов обновляет каждую сводную таблицу, построенную поверх этого кэша. Другие сводные таблицы, которые используют уже обновлённый кэш, можно безопасно пропустить.
- **Изменилось только представление/макет сводной таблицы** → используйте `pivotTable.calculateData();` для повторной отрисовки из существующего кэша без обращения к источнику.

Следующий пример демонстрирует новый эффективный шаблон для рабочих книг с несколькими сводными таблицами, использующими один кэш.

```java
import com.aspose.cells.*;
import com.aspose.cells.pivot.*;

Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);

// --- Создаём исходные данные: Fruit / Year / Amount (заголовок + 9 строк) ---
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

sheet.getCells().get("A2").putValue("Grape");      sheet.getCells().get("B2").putValue(2020); sheet.getCells().get("C2").putValue(1000);
sheet.getCells().get("A3").putValue("Blueberry");  sheet.getCells().get("B3").putValue(2020); sheet.getCells().get("C3").putValue(2000);
sheet.getCells().get("A4").putValue("Kiwi");       sheet.getCells().get("B4").putValue(2020); sheet.getCells().get("C4").putValue(1500);
sheet.getCells().get("A5").putValue("Cherry");     sheet.getCells().get("B5").putValue(2020); sheet.getCells().get("C5").putValue(2500);
sheet.getCells().get("A6").putValue("Grape");      sheet.getCells().get("B6").putValue(2021); sheet.getCells().get("C6").putValue(3000);
sheet.getCells().get("A7").putValue("Blueberry");  sheet.getCells().get("B7").putValue(2021); sheet.getCells().get("C7").putValue(1800);
sheet.getCells().get("A8").putValue("Kiwi");       sheet.getCells().get("B8").putValue(2021); sheet.getCells().get("C8").putValue(2200);
sheet.getCells().get("A9").putValue("Cherry");     sheet.getCells().get("B9").putValue(2021); sheet.getCells().get("C9").putValue(2700);

// --- Добавляем первую сводную таблицу (Pivot1) в ячейку назначения E3 ---
int idx1 = sheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable1 = sheet.getPivotTables().get(idx1);
pivotTable1.addFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(PivotFieldType.Data, "Amount");

// --- Добавляем ВТОРУЮ сводную таблицу (Pivot2) на ТОТ ЖЕ диапазон источника ---
int idx2 = sheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
PivotTable pivotTable2 = sheet.getPivotTables().get(idx2);
pivotTable2.addFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(PivotFieldType.Data, "Amount");

// --- Изменяем несколько значений Amount в исходных данных ---
sheet.getCells().get("C2").putValue(5000);   // Grape  2020
sheet.getCells().get("C5").putValue(7500);   // Cherry 2020
sheet.getCells().get("C9").putValue(9500);   // Cherry 2021

// --- НОВЫЙ шаблон v26.7+: обновляем кэш ОДИН раз, затем повторно отображаем по необходимости ---
pivotTable1.getPivotCache().refresh();

// Повторно отображаем представление/макет второй сводной таблицы, не затрагивая источник
pivotTable2.calculateData();

workbook.save("output.xlsx");
```

## Какой API обновления следует использовать?

В таблице ниже приведены доступные API обновления и случаи, когда следует выбирать каждый из них.

| Цель | Рекомендуемый API | Примечания |
|------|-----------------|-------|
| Обновить всё в рабочей книге | `Workbook.refreshAll()` | Один вызов, охватывает все кэши и таблицы. |
| Обновить только сводные таблицы на одном листе | `Worksheet.refreshPivotTables()` | Ограничено одним рабочим листом. |
| Изменились исходные данные для одного кэша | `pivotTable.getPivotCache().refresh()` | Обновляет ВСЕ сводные таблицы на этом общем кэше. |
| Изменились только параметры представления/макета | `pivotTable.calculateData()` | Пропускает ненужное обращение к источнику. |
| Получить список всех сводных таблиц на общем кэше | `pivotCache.getPivotTables()` | Используйте для перечисления перед массовым обновлением. |

На практике рекомендуется использовать API на основе кэша вместо устаревшего метода `refreshData()` для каждой таблицы. Они учитывают общие кэши, избегают избыточных обращений к источнику и позволяют выбрать минимальный объём, удовлетворяющий вашим требованиям к обновлению.

## Связанные статьи

- [Вставка изображения в ячейку](/cells/ru/java/inserting-an-image-into-a-cell/)
- [Чтение и запись файлов DBF](/cells/ru/java/dbf/)
- [Разделение файлов Excel на несколько файлов](/cells/ru/java/splitting-excel-files-into-multiple-files/)
- [Спарклайны в Aspose.Cells for Aspose.Cells for Java](/cells/ru/java/sparkline/)

{{< app/cells/assistant language="java" >}}
---
title: Обновление сводных таблиц в Aspose.Cells for Java
linktitle: Обновление сводных таблиц в Aspose.Cells for Java
description: Узнайте, как обновлять сводные таблицы в Aspose.Cells for Java с помощью API обновления сводных таблиц версии 26.7+. В этой статье рассматриваются RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData и GetPivotTables с практическими примерами кода.
keywords: Aspose.Cells, Java, сводная таблица, обновление, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ru/java/refresh-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells предоставляет многоуровневый API обновления, который позволяет перезагружать данные сводных таблиц на четырёх различных уровнях — от всей рабочей книги до отдельной сводной таблицы. Начиная с версии **Aspose.Cells for Java v26.7**, устаревший метод `PivotTable.refreshData()` помечен как нерекомендуемый и должен быть заменён более эффективными API, учитывающими кэш, которые описаны в этой статье.
{{% /alert %}}
## Введение
Обновление сводной таблицы редко представляет собой одну операцию. «За кулисами» Aspose.Cells поддерживает многоуровневую цепочку данных, которая связывает исходные данные с отображаемыми значениями на рабочем листе. Понимание этой цепочки — ключ к выбору правильного API обновления для любой ситуации.
Цепочка данных состоит из четырёх уровней:
1. **Источник данных** — исходные диапазоны рабочего листа, запрос к базе данных или диапазон консолидации, где хранятся необработанные значения.
2. **PivotCache** — моментальный снимок исходных данных в памяти. Каждая сводная таблица строится поверх `PivotCache`; именно здесь все данные собираются и агрегируются.
3. **PivotTable** — объект представления, который определяет поля строк, столбцов, значений и фильтров. `PivotTable` читает *только* из своего `PivotCache`, никогда напрямую из источника данных.
4. **Cells** — коллекция ячеек рабочего листа, в которые `PivotTable` отображает вычисленные значения и стили.
Особенно важным понятием является **общий кэш**. Когда несколько сводных таблиц в рабочей книге ссылаются на один и тот же исходный диапазон, они совместно используют *один* экземпляр `PivotCache`. Один `PivotCache` может использоваться множеством сводных таблиц, и обновление этого кэша обновляет все зависимые `PivotTable` одновременно.
{{% alert color="primary" %}}
`PivotCache.getSourceType()` (перечисление `PivotTableSourceType`) указывает, откуда поступили данные кэша. Начиная с версии 26.7, `PivotCache.refresh()` поддерживает только типы источников **`Sheet`** и **`Consolidation`** — то есть данные, которые находятся в диапазонах рабочего листа. Внешние источники (базы данных, внешние подключения и т.д.) пока не могут быть обновлены через API кэша.
{{% /alert %}}
Из-за этой цепочки в Aspose.Cells существуют два основных пути обновления:
- **`PivotCache.refresh()`** — перезагружает источник → кэш И пересчитывает все зависимые `PivotTable` за одну операцию.
- **`PivotTable.calculateData()`** — пересчитывает отображение одной `PivotTable` из уже закэшированных данных, без обращения к источнику данных.
Все сценарии в этой статье используют исходные данные из ячеек рабочего листа, поэтому тип источника — `Sheet`, и операции обновления работают, как описано.
## Необходимые операторы импорта
Все примеры на Java в этой статье начинаются со следующих операторов импорта, поскольку типы сводных таблиц находятся в пакете `com.aspose.cells.pivot`:
- `import java.lang.System;`
- `import com.aspose.cells.Workbook;`
- `import com.aspose.cells.pivot.*;`
## Обновление всех сводных таблиц в рабочей книге
Когда вам нужно убедиться, что каждый кэш сводных таблиц и каждая сводная таблица в рабочей книге отражают последние исходные данные, самым простым и полным API является `Workbook.refreshAll()`. Один вызов обходит всю рабочую книгу — обновляя каждый `PivotCache` из его источника, а затем пересчитывая каждую зависимую `PivotTable`. Это рекомендуемый подход для общих полных обновлений документа, когда производительность не критична.
Следующий пример создаёт рабочую книгу с исходным диапазоном Fruit/Year/Amount, создаёт одну сводную таблицу, изменяет некоторые исходные значения, а затем использует `refreshAll()` для обновления всего за один вызов.
```java
import com.aspose.cells.*;

// Создание новой рабочей книги
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// Запись строки заголовков в ячейки A1:C1
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// Запись строк данных в ячейки A2:C9 (8 строк данных о фруктах за 2020 и 2021 годы)
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

// Добавление сводной таблицы: исходный диапазон "A1:C9", целевая ячейка "E3", имя "Pivot1"
int pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Назначение полей сводной таблицы: Fruit — в строки, Year — в столбцы, Amount — в данные
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

// Изменение нескольких значений Amount в исходных данных для имитации изменений
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);

// Обновление всех сводных таблиц / кэшей сводных таблиц в рабочей книге
workbook.refreshAll();

// Сохранение рабочей книги
workbook.save("output.xlsx");
```
## Обновление всех сводных таблиц на одном рабочем листе
Иногда вам нужно обновить только те сводные таблицы, которые находятся на одном конкретном рабочем листе — например, когда известно, что сводные таблицы на других рабочих листах не связаны с ними и не должны затрагиваться. Для этого случая Aspose.Cells предоставляет `Worksheet.refreshPivotTables()`, область действия которого ограничена одним экземпляром `Worksheet`.
Это более выборочно, чем `Workbook.refreshAll()`: обновляются только сводные таблицы на целевом рабочем листе, а сводные таблицы на других рабочих листах остаются нетронутыми.
Следующий пример заполняет те же исходные данные Fruit/Year/Amount, добавляет сводную таблицу на первом рабочем листе, изменяет некоторые исходные значения, а затем обновляет только сводные таблицы на этом рабочем листе.
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
Если вам нужен детальный контроль над одной сводной таблицей, API на основе кэша предоставляет два варианта. Выбор между ними зависит от того, что именно изменилось: базовые исходные данные или только настройки представления/макета самой сводной таблицы.
### Исходные данные изменились — используйте `PivotCache.refresh()`
Если базовые исходные данные изменились, правильной точкой входа является `pivotTable.getPivotCache().refresh()`. Этот вызов перечитывает исходные данные в кэш, а затем пересчитывает каждую `PivotTable`, зависящую от этого кэша.
{{% alert color="primary" %}}
Поскольку сводные таблицы совместно используют один экземпляр `PivotCache`, вызов `PivotCache.refresh()` пересчитывает **все** сводные таблицы, построенные на этом же кэше, а не только ту, на которую вы ссылаетесь. Если две сводные таблицы совместно используют один и тот же исходный диапазон, обновление одного кэша обновляет обе.
{{% /alert %}}
Следующий пример создаёт две сводные таблицы на одном и том же исходном диапазоне, чтобы продемонстрировать это поведение общего кэша, изменяет некоторые исходные значения, а затем выполняет обновление через ссылку на один кэш.
```java
import com.aspose.cells.*;



// Создать новую книгу и получить доступ к первому рабочему листу

Workbook workbook = new Workbook();

Worksheet worksheet = workbook.getWorksheets().get(0);



// Записать строку заголовков: Фрукт / Год / Количество

worksheet.getCells().get("A1").putValue("Fruit");

worksheet.getCells().get("B1").putValue("Year");

worksheet.getCells().get("C1").putValue("Amount");



// Записать примерно 9 строк данных (виноград / черника / киви / вишня за 2020-2021 годы)

worksheet.getCells().get("A2").putValue("Grape");

worksheet.getCells().get("B2").putValue(2020)        // MISSING SEMICOLON HERE!
worksheet.getCells().get("C2").putValue(100);        // ERROR: extra ) here? No actually it looks like missing semicolon and continuation

worksheet.getCells().get("A4").putValue("Kiwi");     // Extra [P] markers visible
worksheet.getCells().get("B4").putValue(2020);[P].putValue(300);   // This is wrong syntax

worksheet.getCells().get("A5").putValue("Cherry");    // More [P] markers
worksheet.getCells().get("B5").putValue(2020)[P].putValue(400);

// ... many more errors
```
### Изменились только представление/макет — используйте `calculateData()`
Если исходные данные *не* изменились, но изменились только настройки представления или макета сводной таблицы (например, поле было перемещено в другую область, или переключена настройка обновления при открытии), нет необходимости повторно обращаться к источнику данных. Кэш уже содержит правильные данные; нужно только пересчитать отображаемую `PivotTable`. В этом случае правильным выбором является `pivotTable.calculateData()`.
Это позволяет избежать ненужного обращения к источнику и значительно быстрее, когда множество сводных таблиц совместно используют один кэш.
Следующий пример изменяет свойство сводной таблицы, не связанное с источником, а затем вызывает `calculateData()` для её повторного отображения из существующего кэша.
```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// Записать строку заголовков Fruit / Year / Amount
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

// Добавить сводную таблицу с именем "Pivot1" в ячейке E3, источник данных A1:C9
int pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Назначить поля: Fruit в строки, Year в столбцы, Amount в данные
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

// Изменить свойство представления/макета — это изменение только для отображения,
// поэтому оно НЕ требует повторного чтения исходных данных через PivotCache.Refresh().
pivotTable.setRefreshDataOnOpeningFile(false);

// calculateData() повторно отрисовывает отображение ЭТОЙ сводной таблицы (данные + стиль) из
// данных, уже хранящихся в PivotCache. Поскольку исходные данные не изменились,
// обратное обращение к источнику не выполняется — пересчитываются только кэшированные значения
// в ячейках листа.
pivotTable.calculateData();

// Сохранить книгу на диск
workbook.save("output.xlsx");
```
## Получение всех сводных таблиц, использующих один и тот же PivotCache
Рабочая книга часто содержит множество сводных таблиц, которые все построены поверх одного общего кэша. Чтобы перечислить их — например, перед выполнением пакетного обновления или для диагностики влияния общего кэша — используйте `PivotCache.getPivotTables()`. Этот метод возвращает коллекцию всех `PivotTable`, зависящих от данного кэша.
Это также самый прямой способ убедиться, что две сводные таблицы действительно совместно используют один и тот же экземпляр `PivotCache`: вы можете сравнить ссылки на кэш (используя оператор `==`) или просто перебрать коллекцию, возвращённую `getPivotTables()`, и увидеть, какие сводные таблицы в ней присутствуют.
Следующий пример создаёт две сводные таблицы на одном и том же исходном диапазоне, проверяет, что они совместно используют один и тот же экземпляр кэша, а затем перечисляет сводные таблицы этого кэша.

## Миграция с устаревшего `PivotTable.refreshData()`
До версии Aspose.Cells for Java v26.7 стандартным способом обновления сводной таблицы был вызов `PivotTable.refreshData()` для каждой сводной таблицы по отдельности. Начиная с версии 26.7, этот метод помечен как **нерекомендуемый** и должен быть заменён описанными выше API, учитывающими кэш.
Есть две причины, по которым подход с `refreshData()` для каждой таблицы по отдельности является проблематичным в реальных рабочих книгах:
- Он повторно извлекает данные из источника *при каждом* вызове, даже если источник не изменился.
- Каждый вызов обновляет весь общий кэш. Когда множество сводных таблиц совместно используют один кэш, повторный вызов `refreshData()` для каждой сводной таблицы приводит к многократному повторному извлечению одного и того же кэша, что очень медленно.
Рекомендуемые замены:
- **Обновить ВСЕ сводные таблицы в рабочей книге** → используйте `workbook.refreshAll();`
- **Обновить НЕКОТОРЫЕ из них** → используйте `pivotTable.getPivotCache().refresh();` для одного кэша. Поскольку кэш является общим, этот единственный вызов обновляет каждую сводную таблицу, построенную поверх этого кэша. Другие сводные таблицы, которые построены на уже обновлённом кэше, можно безопасно пропустить.
- **Изменились только представление/макет сводной таблицы** → используйте `pivotTable.calculateData();` для повторного отображения из существующего кэша без какого-либо обращения к источнику.
Следующий пример демонстрирует новый эффективный шаблон для рабочих книг с несколькими сводными таблицами, использующими один общий кэш.
```java
import com.aspose.cells.*;
import com.aspose.cells.pivot.*;

Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);

// --- Построить исходные данные: Фрукт / Год / Сумма (заголовок + 9 строк) ---
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

// --- Добавить первую сводную таблицу (Pivot1) в ячейку назначения E3 ---
int idx1 = sheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable1 = sheet.getPivotTables().get(idx1);
pivotTable1.addFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(PivotFieldType.Data, "Amount");

// --- Добавить ВТОРУЮ сводную таблицу (Pivot2) на ТОТ ЖЕ диапазон источника ---
int idx2 = sheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
PivotTable pivotTable2 = sheet.getPivotTables().get(idx2);
pivotTable2.addFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(PivotFieldType.Data, "Amount");

// --- Изменить несколько значений Суммы в исходных данных ---
sheet.getCells().get("C2").putValue(5000);   // Виноград 2020
sheet.getCells().get("C5").putValue(7500);   // Вишня 2020
sheet.getCells().get("C9").putValue(9500);   // Вишня 2021

// --- НОВЫЙ шаблон v26.7+: обновить кэш ОДИН РАЗ, затем перерисовать при необходимости ---
pivotTable1.getPivotCache().refresh();

// Перерисовать представление/макет второй сводной таблицы без изменения источника
pivotTable2.calculateData();

workbook.save("output.xlsx");
```
## Какой API обновления следует использовать?
В таблице ниже приведены доступные API обновления и указано, когда следует выбирать каждый из них.
| Цель | Рекомендуемый API | Примечания |
|------|-----------------|-------|
| Обновить всё в рабочей книге | `Workbook.refreshAll()` | Один вызов; охватывает все кэши и таблицы. |
| Обновить только сводные таблицы на одном листе | `Worksheet.refreshPivotTables()` | Ограничено одним рабочим листом. |
| Исходные данные изменились для одного кэша | `pivotTable.getPivotCache().refresh()` | Обновляет ВСЕ сводные таблицы на этом общем кэше. |
| Изменились только настройки представления/макета | `pivotTable.calculateData()` | Пропускает ненужное обращение к источнику. |
| Список всех сводных таблиц на общем кэше | `pivotCache.getPivotTables()` | Используется для перечисления перед массовым обновлением. |
На практике предпочтительнее использовать API на основе кэша вместо устаревшего `refreshData()` для каждой таблицы по отдельности. Они учитывают общие кэши, избегают избыточных обращений к источнику и позволяют выбрать наименьшую область, удовлетворяющую вашим требованиям к обновлению.

{{< app/cells/assistant language="java" >}}

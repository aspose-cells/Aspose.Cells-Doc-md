---
title: Топ-10: отображение или фильтрация в сводной таблице
linktitle: Топ-10: отображение или фильтрация в сводной таблице
description: Узнайте, как отображать только элементы с наибольшим или наименьшим рейтингом поля сводной таблицы в Aspose.Cells for .Net. В этой статье рассматриваются метод Top10AutoShow для Excel 97-2003, чтение параметров с помощью Top10AutoShowSettings и фильтр «Топ-10» для Excel 2007-365 с помощью FilterTop10.
keywords: Aspose.Cells, .NET, сводная таблица, топ-10, автопоказ, Top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, FilterTop10, PivotFilterType, PivotField, C#
type: docs
weight: 20
url: /ru/net/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
Сводную таблицу, в которой перечислены все элементы поля строки, бывает трудно читать, если это поле содержит десятки элементов. Отчет «Топ-10» оставляет только элементы с наибольшим или наименьшим рейтингом, что необходимо для отчетов с ранжированием — например, «5 самых доходных товаров» или «3 региона с наименьшим количеством продаж». Aspose.Cells поддерживает два механизма, соответствующих двум поколениям Microsoft Excel.
- **AutoShow в Excel 97-2003** — метод `PivotField.Top10AutoShow()`. Это классическая настройка «Показать N верхних/нижних элементов», которая хранится непосредственно в поле сводной таблицы. Она работает во всех версиях Excel, как старых, так и новых, поскольку входит в состав исходного формата сводной таблицы.
- **Фильтр «Топ-10» в Excel 2007-365** — метод `PivotField.FilterTop10()`. Это современный фильтр значений «Топ-10», доступный в меню поля в разделе «Фильтры значений». Он хранится в виде объекта `PivotFilter`, связанного с полем, и поддерживает ранжирование по количеству элементов и по проценту.

## **Показ топ-10 элементов в Excel 97-2003 (Top10AutoShow)**
Классический механизм `AutoShow` настраивается одним вызовом `PivotField.Top10AutoShow(bool isAutoShow, bool isTop, int count, int rankBy)`:
- `isAutoShow` — включает или отключает параметр `AutoShow` для поля.
- `isTop` — значение `true` оставляет элементы с наибольшим рейтингом (верхние), а `false` — элементы с наименьшим рейтингом (нижние).
- `count` — количество элементов, которые необходимо оставить, например 10 для классического отчета «Топ-10».
- `rankBy` — индекс поля данных (с нуля), значения которого используются для ранжирования элементов. Передайте -1, чтобы выполнить ранжирование элементов по самому полю.
Ранжирование может выполняться по полю значений или по самому полю. Ниже приведены два естественных варианта.

### **Ранжирование по полю значений**
Ранжируйте элементы поля строки по обычному полю значений, например `Sum of Sales`. В следующем примере создается сводная таблица с одним полем строки (`Sport`) и одним полем данных (`Sales`), после чего отображаются 2 вида спорта с наибольшим объемом продаж. Значение `rankBy` равно 0, поскольку `Sum of Sales` — поле данных с индексом 0.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Cells["A1"].PutValue("Sport");
worksheet.Cells["B1"].PutValue("Quarter");
worksheet.Cells["C1"].PutValue("Sales");
string[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
foreach (string sport in sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.Cells[row, 0].PutValue(sport);
        worksheet.Cells[row, 1].PutValue("Qtr" + quarter);
        worksheet.Cells[row, 2].PutValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.PivotTables.Add("A1:C16", 2, 5);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Sport");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Sales");
pivotTable.CalculateData();
PivotField sportField = pivotTable.RowFields[0];
// Показать 2 верхних элемента, отсортированных по «Сумма продаж» (индекс поля данных 0)
sportField.Top10AutoShow(true, true, 2, 0);
pivotTable.CalculateData();
workbook.Save("output-top10-by-value-field.xlsx");
```

### **Ранжирование по самому полю**
Поле также можно ранжировать по его собственным значениям — передайте -1 в качестве `rankBy`. Для этого варианта дополнительное поле данных не требуется; достаточно разместить поле в области строк или столбцов. В следующем примере показаны 3 вида спорта, занимающие нижние позиции при ранжировании по самому полю. При сохранении этой настройки атрибут `rankBy` не записывается в XML сводной таблицы, поскольку -1 является значением по умолчанию для данного формата, а `Top10AutoShowSettings.RankBy` возвращает -1.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Cells["A1"].PutValue("Sport");
worksheet.Cells["B1"].PutValue("Quarter");
worksheet.Cells["C1"].PutValue("Sales");
string[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
foreach (string sport in sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.Cells[row, 0].PutValue(sport);
        worksheet.Cells[row, 1].PutValue("Qtr" + quarter);
        worksheet.Cells[row, 2].PutValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.PivotTables.Add("A1:C16", 2, 5);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Sport");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Sales");
pivotTable.CalculateData();
PivotField sportField = pivotTable.RowFields[0];
// Показать 3 нижних элемента, ранжированных по самому полю (rankBy = -1)
sportField.Top10AutoShow(true, false, 3, -1);
pivotTable.CalculateData();
workbook.Save("output-top10-by-field-itself.xlsx");
```

## **Чтение текущих параметров (Top10AutoShowSettings)**
Свойство `PivotField.Top10AutoShowSettings` возвращает объект `PivotFieldTop10AutoShowSettings`, который предоставляет доступ к параметрам `AutoShow`, которые в данный момент сохранены в поле. С его помощью можно проверить, как будут представлены элементы существующей рабочей книги или только что настроенной сводной таблицы, в том числе при загрузке рабочей книги из файла.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook("output-top10-by-value-field.xlsx");
PivotTable pivotTable = workbook.Worksheets[0].PivotTables[0];
PivotField sportField = pivotTable.RowFields[0];
PivotFieldTop10AutoShowSettings settings = sportField.Top10AutoShowSettings;
Console.WriteLine("AutoShow enabled: " + settings.IsAutoShow);
Console.WriteLine("Direction: " + (settings.IsTop ? "Top" : "Bottom"));
Console.WriteLine("Item count: " + settings.AutoShowCount);
Console.WriteLine("Ranking data field index: " + settings.RankBy);
```

Четыре свойства соответствуют классическим атрибутам механизма `AutoShow`, записываемым в XML сводной таблицы (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`), поэтому считанные значения будут учитываться каждой версией Excel.

## **Примечание**

{{% alert color="primary" %}}
- Прямые свойства `PivotField` — `IsAutoShow`, `IsAscendShow`, `AutoShowCount` и `AutoShowField` — помечены как устаревшие. Вместо них следует использовать объект `Top10AutoShowSettings`: `IsAutoShow` заменяется на `Top10AutoShowSettings.IsAutoShow`, `IsAscendShow` — на `Top10AutoShowSettings.IsTop`, `AutoShowCount` — на `Top10AutoShowSettings.AutoShowCount`, а `AutoShowField` — на `Top10AutoShowSettings.RankBy`. Для изменения настроек используйте метод `Top10AutoShow()`.
- `Top10AutoShow` работает с полями строк и столбцов. Поле, находящееся только в области страницы (фильтра), нельзя ранжировать таким способом, поскольку его элементы не размещены в теле сводной таблицы.
{{% /alert %}}

## **Excel 2007-365: фильтр «Топ-10» (FilterTop10)**
Современные версии Excel предоставляют «Топ-10» как фильтр значений в меню поля («Фильтры значений», «Топ-10...»). В Aspose.Cells этот фильтр реализован методом `PivotField.FilterTop10(int valueFieldIndex, PivotFilterType type, bool isTop, int itemCount)`, который возвращает созданный объект `PivotFilter`:
- `valueFieldIndex` — индекс поля данных (с нуля), агрегированные значения которого используются для ранжирования элементов.
- `type` — определяет смысл `itemCount`. `PivotFilterType.Count` оставляет фиксированное количество элементов (вариант «Элементы» в диалоговом окне). `PivotFilterType.Percent` оставляет заданный процент элементов, поэтому `itemCount` задает сам процент: значение 30 оставляет верхние 30 процентов. `PivotFilterType.Sum` ранжирует элементы по накопленному объему значений.
- `isTop` — значение `true` соответствует верхним элементам, а `false` — нижним.
- `itemCount` — число N в выражении «Топ-N»; его единица измерения зависит от `type`.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Cells["A1"].PutValue("Sport");
worksheet.Cells["B1"].PutValue("Quarter");
worksheet.Cells["C1"].PutValue("Sales");
string[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
foreach (string sport in sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.Cells[row, 0].PutValue(sport);
        worksheet.Cells[row, 1].PutValue("Qtr" + quarter);
        worksheet.Cells[row, 2].PutValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.PivotTables.Add("A1:C16", 2, 5);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Sport");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Sales");
pivotTable.CalculateData();
PivotField sportField = pivotTable.RowFields[0];
// Фильтр верхних 10 — сохранить 2 верхних элемента по показателю «Сумма продаж» (индекс поля данных 0)
PivotFilter filter = sportField.FilterTop10(0, PivotFilterType.Count, true, 2);
// Для фильтра на основе процентов вместо этого сохранить верхние 30 процентов элементов:
// sportField.FilterTop10(0, PivotFilterType.Percent, true, 30);
pivotTable.PivotCache.Refresh();
pivotTable.CalculateData();
workbook.Save("output-top10-filter.xlsx");
```

{{% alert color="primary" %}}
`Top10AutoShow` и `FilterTop10` — две отдельные возможности. `AutoShow` записывает классический атрибут `autoShow` в поле сводной таблицы и применяется всеми версиями Excel начиная с Excel 97. `FilterTop10` записывает современную запись `PivotFilter`, для которой требуется Excel 2007 или более поздняя версия. Если рабочую книгу открыть в более старой версии Excel, сводная таблица с современным фильтром будет показывать все элементы. Для документов, которые должны проходить цикл открытия и сохранения с помощью устаревших инструментов, предпочтительно использовать `Top10AutoShow`; для современных рабочих книг предпочтительно использовать `FilterTop10`, поскольку его можно сочетать с другими фильтрами значений.
{{% /alert %}}

## **Связанные статьи**
- [Фильтрация сводных таблиц по метке или значению](/cells/ru/net/filter-by-label-or-value-of-pivot-table/)
- [Добавление полей строк и столбцов в сводную таблицу](/cells/ru/net/pivot-table-add-row-and-column-fields/)
- [Группировка полей сводной таблицы](/cells/ru/net/group-pivot-fields-in-the-pivot-table/)
- [Обновление сводной таблицы](/cells/ru/net/refresh-pivot-table/)
- [Добавление поля страницы в сводную таблицу](/cells/ru/net/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="csharp" >}}
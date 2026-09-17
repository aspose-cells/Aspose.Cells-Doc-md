---
title: Добавление полей строк и столбцов сводной таблицы в Aspose.Cells for C++
description: Узнайте, как добавлять базовые поля в области строк и столбцов сводной таблицы и управлять промежуточными итогами полей сводной таблицы с помощью PivotField.SetSubtotals в Aspose.Cells for C++.
linktitle: Поля строк и столбцов
keywords: Aspose.Cells, C++, сводная таблица, поле строки, поле столбца, PivotField, SetSubtotals, PivotFieldSubtotalType, промежуточные итоги
type: docs
weight: 220
url: /ru/cpp/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Добавление поля в область строк или столбцов**
Метод `PivotTable.AddFieldToArea(PivotFieldType fieldType, U16String fieldName)` перемещает базовое поле из исходных данных в одну из четырёх областей сводной таблицы. Аргумент `fieldType` принимает одно из следующих значений `PivotFieldType`.
- `Row` — поля, расположенные вертикально слева
- `Column` — поля, расположенные горизонтально сверху
- `Data` — поля, значения которых агрегируются
- `Page` — поля, используемые в качестве фильтров отчёта
Порядок вложенности полей имеет значение. Добавление `Category` в область строк первым, а затем `Item` создаёт сводную таблицу, в которой внешняя группировка — `Category`, а внутренняя — `Item`. Изменение порядка на противоположный меняет иерархию.

## **Промежуточные итоги поля сводной таблицы**
Метод `PivotField.SetSubtotals(PivotFieldSubtotalType subtotalType, bool shown)` управляет тем, какие строки промежуточных итогов отображаются для поля сводной таблицы. Каждый вызов независимо переключает один тип промежуточного итога. Передача `shown = true` отображает промежуточный итог, а `shown = false` скрывает его. Поскольку каждый вызов влияет только на один тип, многократный вызов метода с разными значениями `subtotalType` позволяет собрать произвольный набор промежуточных итогов.
Перечисление `PivotFieldSubtotalType` определяет доступные виды промежуточных итогов.
- `Automatic` — Aspose.Cells выбирает вариант по умолчанию (обычно `Sum` для числовых полей)
- `None` — подавить все строки промежуточных итогов
- `Sum`
- `Count`
- `Average`
- `Max`
- `Min`
- `Product`
- `StdDev`
- `StdDevp`
- `Var`
- `Varp`

{{% alert color="primary" %}}
Промежуточные итоги отображаются только при наличии двух или более полей сводной таблицы в области строк (или в области столбцов). Для одного поля между ними нечего осмысленно суммировать, поэтому вызовы `SetSubtotals` в этом случае не имеют видимого эффекта. Поэтому в данной статье во всех примерах используются два поля строк (`Category` — внешнее, `Item` — внутреннее), чтобы граница промежуточных итогов между группами `Category` была видна.
{{% /alert %}}

## **Сценарий 1 — Автоматические (по умолчанию) промежуточные итоги**
Если `SetSubtotals` вообще не вызывается, Aspose.Cells применяет выбор `Automatic` к числовым полям. Следующий пример явно подтверждает это поведение, вызывая `SetSubtotals(PivotFieldSubtotalType.Automatic, true)` для внешнего поля строки `Category`.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"Data");
    worksheet.GetCells().Get(0, 0).PutValue(u"Category");
    worksheet.GetCells().Get(0, 1).PutValue(u"Item");
    worksheet.GetCells().Get(0, 2).PutValue(u"Year");
    worksheet.GetCells().Get(0, 3).PutValue(u"Amount");
    worksheet.GetCells().Get(1, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(1, 1).PutValue(u"Apple");
    worksheet.GetCells().Get(1, 2).PutValue(2020);
    worksheet.GetCells().Get(1, 3).PutValue(100);
    worksheet.GetCells().Get(2, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(2, 1).PutValue(u"Apple");
    worksheet.GetCells().Get(2, 2).PutValue(2021);
    worksheet.GetCells().Get(2, 3).PutValue(150);
    worksheet.GetCells().Get(3, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(3, 1).PutValue(u"Banana");
    worksheet.GetCells().Get(3, 2).PutValue(2020);
    worksheet.GetCells().Get(3, 3).PutValue(80);
    worksheet.GetCells().Get(4, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(4, 1).PutValue(u"Banana");
    worksheet.GetCells().Get(4, 2).PutValue(2021);
    worksheet.GetCells().Get(4, 3).PutValue(90);
    worksheet.GetCells().Get(5, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(5, 1).PutValue(u"Carrot");
    worksheet.GetCells().Get(5, 2).PutValue(2020);
    worksheet.GetCells().Get(5, 3).PutValue(50);
    worksheet.GetCells().Get(6, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(6, 1).PutValue(u"Carrot");
    worksheet.GetCells().Get(6, 2).PutValue(2021);
    worksheet.GetCells().Get(6, 3).PutValue(60);
    worksheet.GetCells().Get(7, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(7, 1).PutValue(u"Daikon");
    worksheet.GetCells().Get(7, 2).PutValue(2020);
    worksheet.GetCells().Get(7, 3).PutValue(40);
    worksheet.GetCells().Get(8, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(8, 1).PutValue(u"Daikon");
    worksheet.GetCells().Get(8, 2).PutValue(2021);
    worksheet.GetCells().Get(8, 3).PutValue(45);
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:D9", u"F3", u"PivotTable1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Category");
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Item");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    PivotField categoryField = pivotTable.GetRowFields().Get(0);
    categoryField.SetSubtotals(PivotFieldSubtotalType::Automatic, true);
    pivotTable.CalculateData();
    workbook.Save(u"output_automatic.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Сценарий 2 — Подавление всех промежуточных итогов (None)**
Вызов `SetSubtotals(PivotFieldSubtotalType.None, true)` удаляет все строки промежуточных итогов из сводной таблицы, оставляя только строки полей и общий итог внизу. Это полезно, когда нужны сгруппированные данные в чистом виде без строк итогов.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);
    sheet.SetName(u"Data");
    U16String headers[] = { u"Category", u"Item", u"Year", u"Amount" };
    for (int j = 0; j < 4; j++) {
        sheet.GetCells().Get(0, j).PutValue(headers[j]);
    }
    U16String categories[] = { u"Fruit", u"Fruit", u"Fruit", u"Fruit",
                               u"Vegetable", u"Vegetable", u"Vegetable", u"Vegetable" };
    U16String items[] = { u"Apple", u"Apple", u"Banana", u"Banana",
                          u"Carrot", u"Carrot", u"Daikon", u"Daikon" };
    int years[]   = { 2020, 2021, 2020, 2021, 2020, 2021, 2020, 2021 };
    int amounts[] = {  100,  150,   80,   90,   50,   60,   40,   45 };
    for (int i = 0; i < 8; i++) {
        sheet.GetCells().Get(i + 1, 0).PutValue(categories[i]);
        sheet.GetCells().Get(i + 1, 1).PutValue(items[i]);
        sheet.GetCells().Get(i + 1, 2).PutValue(years[i]);
        sheet.GetCells().Get(i + 1, 3).PutValue(amounts[i]);
    }
    int pivotIndex = sheet.GetPivotTables().Add(u"A1:D9", u"F3", u"PivotTable1");
    PivotTable pivotTable = sheet.GetPivotTables().Get(pivotIndex);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Category");
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Item");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    PivotField categoryField = pivotTable.GetRowFields().Get(0);
    categoryField.SetSubtotals(PivotFieldSubtotalType::None, true);
    pivotTable.CalculateData();
    wb.Save(u"output_none.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Сценарий 3 — Пользовательский набор промежуточных итогов (Sum + Average)**
Вы не ограничены одним типом промежуточного итога. Каждый вызов `SetSubtotals` действует независимо для одного типа, поэтому двойной вызов метода — один раз с `Sum` и один раз с `Average` — формирует пользовательский набор из двух строк промежуточных итогов для каждой группы `Category`.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"Data");
    worksheet.GetCells().Get(u"A1").PutValue(u"Category");
    worksheet.GetCells().Get(u"B1").PutValue(u"Item");
    worksheet.GetCells().Get(u"C1").PutValue(u"Year");
    worksheet.GetCells().Get(u"D1").PutValue(u"Amount");
    worksheet.GetCells().Get(1, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(1, 1).PutValue(u"Apple");
    worksheet.GetCells().Get(1, 2).PutValue(2020);
    worksheet.GetCells().Get(1, 3).PutValue(100);
    worksheet.GetCells().Get(2, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(2, 1).PutValue(u"Apple");
    worksheet.GetCells().Get(2, 2).PutValue(2021);
    worksheet.GetCells().Get(2, 3).PutValue(150);
    worksheet.GetCells().Get(3, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(3, 1).PutValue(u"Banana");
    worksheet.GetCells().Get(3, 2).PutValue(2020);
    worksheet.GetCells().Get(3, 3).PutValue(80);
    worksheet.GetCells().Get(4, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(4, 1).PutValue(u"Banana");
    worksheet.GetCells().Get(4, 2).PutValue(2021);
    worksheet.GetCells().Get(4, 3).PutValue(90);
    worksheet.GetCells().Get(5, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(5, 1).PutValue(u"Carrot");
    worksheet.GetCells().Get(5, 2).PutValue(2020);
    worksheet.GetCells().Get(5, 3).PutValue(50);
    worksheet.GetCells().Get(6, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(6, 1).PutValue(u"Carrot");
    worksheet.GetCells().Get(6, 2).PutValue(2021);
    worksheet.GetCells().Get(6, 3).PutValue(60);
    worksheet.GetCells().Get(7, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(7, 1).PutValue(u"Daikon");
    worksheet.GetCells().Get(7, 2).PutValue(2020);
    worksheet.GetCells().Get(7, 3).PutValue(40);
    worksheet.GetCells().Get(8, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(8, 1).PutValue(u"Daikon");
    worksheet.GetCells().Get(8, 2).PutValue(2021);
    worksheet.GetCells().Get(8, 3).PutValue(45);
    PivotTableCollection pivotTables = worksheet.GetPivotTables();
    int pivotIndex = pivotTables.Add(u"A1:D9", u"F3", u"PivotTable1");
    PivotTable pivotTable = pivotTables.Get(pivotIndex);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Category");
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Item");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    PivotField categoryField = pivotTable.GetRowFields().Get(0);
    categoryField.SetSubtotals(PivotFieldSubtotalType::Sum, true);
    categoryField.SetSubtotals(PivotFieldSubtotalType::Average, true);
    pivotTable.CalculateData();
    workbook.Save(u"output_custom.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Резюме**

## **Связанные статьи**
- [Поля страниц в сводных таблицах](/cells/ru/cpp/add-page-field-in-pivot-table/)
- [Обновление сводных таблиц в Aspose.Cells for C++](/cells/ru/cpp/refresh-pivot-table/)
- [Применение стилей к сводным таблицам](/cells/ru/cpp/apply-style-to-pivot-table/)
But the related articles have their own URLs. Looking at the input:
- [Page Fields in Pivot Tables](/cells/ru/cpp/add-page-field-in-pivot-table/)
- [Refreshing Pivot Tables in Aspose.Cells for C++](/cells/ru/cpp/refresh-pivot-table/)
- [Applying Styles to Pivot Tables](/cells/ru/cpp/apply-style-to-pivot-table/)
And "Applying Styles to Pivot Tables" - "Применение стилей к сводным таблицам".
The input has:
- YAML frontmatter with title, description, linktitle, keywords, type, weight, url, ai_search_scope, ai_search_endpoint
- ## Adding a Field to the Row or Column Region section
- ## Pivot Field Subtotals section
- alert block about subtotals
- ## Scenario 1 — Automatic (Default) Subtotals with code block
- ## Scenario 2 — Suppressing All Subtotals (None) with code block
- ## Scenario 3 — Custom Subtotal Subset (Sum + Average) with code block
- ## Recap (empty)
- ## Related Articles with 3 links
- Hugo shortcode at end
- title: translate
- description: translate (no colon)
- linktitle: translate
- keywords: translate
- type: keep as "docs"
- weight: keep as 220
- ai_search_scope: keep as "cells_cpp"
- ai_search_endpoint: keep as "https://docsearch.api.aspose.cloud/ask"
linktitle: Поля строк и столбцов
keywords: Aspose.Cells, C++, сводная таблица, поле строки, поле столбца, PivotField, SetSubtotals, PivotFieldSubtotalType, промежуточные итоги
type: docs
weight: 220
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"

{{< app/cells/assistant language="cpp" >}}
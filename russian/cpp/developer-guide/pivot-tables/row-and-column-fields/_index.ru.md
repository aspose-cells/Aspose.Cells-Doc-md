---
title: Добавление полей строк и столбцов сводной таблицы в Aspose.Cells for C++
linktitle: Добавление полей строк и столбцов сводной таблицы в Aspose.Cells for C++
description: Узнайте, как добавлять базовые поля в область строк и область столбцов сводной таблицы и управлять промежуточными итогами полей сводной таблицы с помощью PivotField.SetSubtotals в Aspose.Cells for C++.
keywords: Aspose.Cells, C++, сводная таблица, поле строки, поле столбца, PivotField, SetSubtotals, PivotFieldSubtotalType, промежуточные итоги
type: docs
weight: 220
url: /ru/cpp/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Добавление поля в область строк или столбцов**
Метод `PivotTable.AddFieldToArea(PivotFieldType fieldType, U16String fieldName)` перемещает базовое поле из исходных данных в одну из четырех областей сводной таблицы. Аргумент `fieldType` принимает одно из следующих значений `PivotFieldType`.
- `Row` — поля, размещенные вертикально слева
- `Column` — поля, размещенные горизонтально сверху
- `Data` — поля, значения которых агрегируются
- `Page` — поля, используемые в качестве фильтров отчета
Порядок вложения полей имеет значение. Если сначала добавить `Category` в область строк, а затем `Item`, внешняя группировка сводной таблицы будет выполняться по полю `Category`, а внутренняя — по полю `Item`. Изменение порядка приводит к изменению иерархии.

## **Промежуточные итоги полей сводной таблицы**
Метод `PivotField.SetSubtotals(PivotFieldSubtotalType subtotalType, bool shown)` управляет отображением строк промежуточных итогов для поля сводной таблицы. Каждый вызов независимо включает или отключает отображение одного типа промежуточных итогов. Передача `shown = true` отображает промежуточный итог, а `shown = false` скрывает его. Поскольку каждый вызов затрагивает только один тип, несколько вызовов метода с различными значениями `subtotalType` позволяют сформировать настраиваемое подмножество промежуточных итогов.
Перечисление `PivotFieldSubtotalType` определяет доступные типы промежуточных итогов.
- `Automatic` — Aspose.Cells выбирает вариант по умолчанию (обычно `Sum` для числовых полей)
- `None` — скрывает все строки промежуточных итогов
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
Промежуточные итоги отображаются только тогда, когда в области строк (или области столбцов) есть два или более полей сводной таблицы. Для единственного поля не существует значений, между которыми можно было бы сформировать промежуточный итог, поэтому вызовы `SetSubtotals` в этом случае не имеют видимого эффекта. Поэтому в каждом примере этой статьи используются два поля строк (`Category` — внешнее, `Item` — внутреннее), чтобы для каждой группы `Category` была отчетливо видна граница, на которой отображается промежуточный итог.
{{% /alert %}}

## **Сценарий 1 — автоматические (по умолчанию) промежуточные итоги**
Если метод `SetSubtotals` не вызывается, Aspose.Cells применяет вариант `Automatic` к числовым полям. В следующем примере это поведение явно подтверждается вызовом `SetSubtotals(PivotFieldSubtotalType.Automatic, true)` для внешнего поля строки `Category`.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
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

## **Сценарий 2 — отключение всех промежуточных итогов (None)**
Вызов `SetSubtotals(PivotFieldSubtotalType.None, true)` удаляет все строки промежуточных итогов из сводной таблицы, оставляя только строки полей и общий итог внизу. Такое поведение полезно, когда требуется получить сгруппированные исходные данные без строк сводки.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
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

## **Сценарий 3 — настраиваемое подмножество промежуточных итогов (Sum + Average)**
Не обязательно использовать только один тип промежуточных итогов. Каждый вызов `SetSubtotals` независимо управляет одним типом, поэтому два вызова метода — один с `Sum`, другой с `Average` — формируют настраиваемое подмножество из двух строк промежуточных итогов для каждой группы `Category`.

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

## **Краткие итоги**

Три сценария различаются только вызовами `SetSubtotals`. Всё остальное — набор данных, поля и области, к которым они назначены — одинаково, что делает макеты напрямую сравнимыми.
- **Размещение полей.** `PivotTable.AddFieldToArea(PivotFieldType::Row, fieldName)` перемещает исходный столбец в область. В пределах одной области порядок вызовов определяет порядок отображения, поэтому первый вызов становится самым внешним группировочным уровнем. Подытоги требуют наличия двух или более полей в одной области: при одном поле между группами просто нечего суммировать.
- **Сценарий 1 — автоматические подытоги.** Отсутствие вызова `SetSubtotals` оставляет выбор за Excel, который применяет собственный подытог по умолчанию к числовым полям. Вызов `SetSubtotals` с параметром `PivotFieldSubtotalType::Automatic` явно фиксирует этот выбор, а не оставляет его неявным.
- **Сценарий 2 — без подытогов.** Вызов `SetSubtotals` с параметром `PivotFieldSubtotalType::None` отключает подытог по умолчанию, в результате сводная таблица сохраняет строки полей и итоговую строку, но убирает строки подытогов, которые в противном случае Excel вставлял бы между ними.
- **Сценарий 3 — выбранный поднабор.** Каждый вызов включает или выключает ровно один тип подытога, при этом вызовы накапливаются, а не сбрасывают друг друга. Таким образом, однократный вызов с параметром `PivotFieldSubtotalType::Sum` и однократный вызов с параметром `PivotFieldSubtotalType::Average` оставляют оба типа включенными, и сводная таблица отображает подытог по сумме, подытог по среднему и итоговую строку.

{{% alert color="primary" %}}
Ничего в настройке подытогов не связано исключительно с строковой областью. Те же самые вызовы `SetSubtotals` для поля, взятого из `PivotTable.ColumnFields`, дают те же три макета на оси столбцов, поскольку настройка относится к самому сводному полю, а не к оси, на которой оно размещено.
{{% /alert %}}
## **Связанные статьи**
- [Поля страницы в сводных таблицах](/cells/ru/cpp/add-page-field-in-pivot-table/)
- [Обновление сводных таблиц в Aspose.Cells for C++](/cells/ru/cpp/refresh-pivot-table/)
- [Применение стилей к сводным таблицам](/cells/ru/cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="cpp" >}}
---
title: Фильтрация сводных таблиц по подписи или значению
linktitle: Фильтрация сводных таблиц по подписи или значению
description: Aspose.Cells for C++ поддерживает полный набор возможностей фильтрации сводных таблиц. В этой статье описано, как фильтровать данные сводной таблицы с помощью фильтров по подписям, датам и значениям, фильтра «10 лучших», а также как скрывать и повторно отображать элементы сводной таблицы.
keywords: Aspose.Cells, библиотека C++, электронная таблица, сводная таблица, фильтрация, фильтр по подписи, фильтр по значению, фильтр по дате, фильтр 10 лучших, элемент сводной таблицы, скрытие элемента сводной таблицы
type: docs
weight: 10
url: /ru/cpp/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells предоставляет пять практических стратегий фильтрации отображаемых в сводной таблице данных. Можно применять фильтры по подписям к текстовым полям строк или столбцов, использовать фильтры по датам, когда поле содержит только ячейки со значениями даты и времени или пустые ячейки, применять фильтры по значениям к агрегированным числовым показателям, использовать фильтр «10 лучших» для ранжирования по полю значений либо вручную скрывать и повторно отображать отдельные элементы сводной таблицы с помощью свойства `IsHidden`. Каждая стратегия доступна через специализированные API в классах `PivotField` и `PivotItem`.
{{% /alert %}}

## **Введение**
Сводные таблицы — мощные аналитические инструменты, однако исходные сводные данные зачастую содержат значительно больше информации, чем необходимо представить в отчете. Фильтрация — основной механизм, позволяющий оставить в сводной таблице только строки, столбцы или значения, важные для конкретного отчета. Aspose.Cells for C++ предоставляет программный доступ к возможностям фильтрации, доступным в Microsoft Excel, и тем самым позволяет полностью автоматизировать создание отчетов.
В этой статье рассматриваются следующие стратегии фильтрации:
1. **Фильтр по подписи** — фильтрует элементы полей строк или столбцов по их текстовым подписям.
2. **Фильтр по дате** — фильтрует поля строк или столбцов, содержащие только значения даты и времени или пустые значения.
3. **Фильтр по значению** — фильтрует элементы по агрегированным значениям поля данных.
4. **Фильтр «10 лучших»** — отображает только N наивысших или N низших элементов, ранжированных по полю значений.
5. **Скрытие и повторное отображение элементов сводной таблицы** — позволяет вручную управлять видимостью каждого отдельного элемента в поле.
Для каждого подхода используется отдельный метод класса `PivotField` или свойство класса `PivotItem`. После применения любого фильтра необходимо вызвать `GetPivotCache().Refresh()` у сводной таблицы, чтобы кэшированные данные и вычисленные значения отражали новое состояние фильтра.

## **Фильтр по подписи**
Фильтр по подписи позволяет фильтровать элементы поля строки или столбца, сравнивая их текстовые подписи с заданным шаблоном. Это полезно, если требуется отображать только продукты, названия которых начинаются с определенной буквы, содержат определенное слово или соответствуют другому критерию, основанному на подписи.
Aspose.Cells реализует фильтрацию по подписям с помощью метода `PivotField.FilterByLabel(PivotFilterType, const char16_t*)`. Перечисление `PivotFilterType` включает такие значения, как `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` и другие. Второй аргумент задает строку подписи, используемую для сравнения.
В следующем примере загружается рабочая книга с существующей сводной таблицей, применяется фильтр по подписи, чтобы оставить видимыми только элементы, подписи которых начинаются с заданного префикса, после чего сводная таблица обновляется и результат сохраняется.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    U16String fileName(u"sample.xlsx");
    U16String prefix(u"B");
    // Load the existing workbook containing a pivot table
    Workbook wb(fileName);
    // Access the worksheet by index (first worksheet)
    Worksheet ws = wb.GetWorksheets().Get(0);
    // Access the pivot table by index
    PivotTable pt = ws.GetPivotTables().Get(0);
    // Retrieve the first row PivotField
    PivotField rowField = pt.GetRowFields().Get(0);
    // Apply the label filter — show only row items whose labels begin with the supplied prefix
    rowField.FilterByLabel(PivotFilterType::CaptionBeginsWith, prefix, U16String(u""));
    // Refresh and recalculate the pivot table data so the filter takes effect
    pt.GetPivotCache().Refresh();
    // Save the workbook back to disk
    wb.Save(fileName);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Фильтр по дате**
Фильтры по дате позволяют ограничить сводную таблицу с помощью критериев, основанных на датах, например по сегодняшнему дню, прошлой неделе, текущему месяцу, следующему кварталу или конкретному диапазону дат. Это специализированные фильтры, которые работают только с полями, в которых хранятся сведения о дате и времени.

{{% alert color="primary" %}}
Фильтр по дате работает только тогда, когда в области строк или столбцов находятся исключительно ячейки со значениями даты и времени или пустые ячейки. Если в исходном поле хранятся данные других типов, например числа или текст, фильтр по дате не даст ожидаемого результата. Перед применением этого фильтра убедитесь, что поле отформатировано как дата и что все значения являются допустимыми экземплярами `DateTime` или пустыми ячейками.
Aspose.Cells реализует фильтрацию по датам с помощью метода `PivotField.FilterByDate(PivotFilterType, const Vector<DateTime>& values)`. Перечисление `PivotFilterType` содержит специальные значения для фильтрации по датам, например `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` и `Between`. В зависимости от выбранного типа фильтра передаются одно или два значения `DateTime` (для `Between` передаются начальная и конечная даты).
В следующем примере загружается рабочая книга со сводной таблицей, в области строк которой находится поле даты, применяется фильтр по дате, ограничивающий видимые элементы определенным диапазоном дат, после чего сводная таблица обновляется и рабочая книга сохраняется.
{{% /alert %}}

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <filesystem>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    std::string inputPath = "sample.xlsx";
    std::string outputPath = "output_filtered.xlsx";
    if (!std::filesystem::exists(inputPath))
    {
        // Source workbook not found.
        Aspose::Cells::Cleanup();
        return -1;
    }
    // Load the existing workbook that contains the pivot table
    Workbook workbook(U16String(inputPath.c_str()));
    // Access the worksheet that holds the pivot table (by index)
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    // Access the pivot table by index
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);
    // Retrieve the date PivotField from the row area
    PivotField dateField = pivotTable.GetRowFields().Get(0);
    // Define the date criterion for the Between filter
    Date startDate{2020, 1, 1, 0, 0, 0, 0};
    Date endDate{2020, 12, 31, 0, 0, 0, 0};
    // Apply the date filter on the pivot field
    dateField.FilterByDate(PivotFilterType::DateBetween, startDate, endDate);
    // Refresh and recalculate the pivot table so the filter takes effect
    pivotTable.GetPivotCache().Refresh();
    // Persist the workbook
    workbook.Save(U16String(outputPath.c_str()));
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Фильтр по значению**
Фильтры по значениям работают с агрегированными значениями, которые сводная таблица рассчитывает в области данных. Вместо сопоставления с текстовыми подписями они сравнивают числовые итоги с пороговым значением. Типичные сценарии использования включают отображение только продуктов, сумма продаж которых превышает заданное значение, или только регионов, количество транзакций которых находится в определенном диапазоне.
Aspose.Cells реализует фильтрацию по значениям с помощью метода `PivotField.FilterByValue(PivotField valueField, PivotFilterType filterType, const Vector<Variant>& values)`. Для параметра `filterType` используются такие значения, как `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` и `ValueLessThanOrEqual`. Параметр `valueField` указывает, какое поле данных необходимо оценить, а последние аргументы задают пороговые значения.
В следующем примере загружается рабочая книга со сводной таблицей, применяется фильтр по значению, чтобы оставить только элементы, суммарные значения продаж которых превышают числовой порог, после чего сводная таблица обновляется и рабочая книга сохраняется.

```cpp
#include "Aspose.Cells.h"
#include <cfloat>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb(u"sample.xlsx");
    Worksheet worksheet = wb.GetWorksheets().Get(0);
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);
    PivotField rowField = pivotTable.GetRowFields().Get(0);
    PivotField dataField = pivotTable.GetDataFields().Get(0);
    int dataFieldIndex = -1;
    int dataFieldCount = pivotTable.GetDataFields().GetCount();
    for (int i = 0; i < dataFieldCount; i++)
    {
        PivotField current = pivotTable.GetDataFields().Get(i);
        if (current.GetName() == dataField.GetName())
        {
            dataFieldIndex = i;
            break;
        }
    }
    if (dataFieldIndex >= 0)
    {
        rowField.FilterByValue(dataFieldIndex, PivotFilterType::ValueGreaterThan, 5000, DBL_MAX);
    }
    // Refresh and recalculate the pivot table so the filter takes effect
    pivotTable.GetPivotCache().Refresh();
    wb.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Фильтр «10 лучших»**
Фильтр «10 лучших» — специализированная разновидность фильтра по значениям, которая оставляет только N наивысших или N низших элементов по выбранному полю значений. Его часто используют для создания отчетов с ранжированием, например «10 продуктов с наибольшей выручкой» или «5 регионов с наименьшим количеством продаж».

{{% alert color="primary" %}}
Фильтр «10 лучших» действует только тогда, когда в области данных сводной таблицы есть одно или несколько полей значений. Без хотя бы одного поля значений агрегированный показатель, по которому можно ранжировать элементы, отсутствует, поэтому фильтр нельзя применить.
Фильтр «10 лучших» реализован с помощью метода `PivotField.FilterTop10(int32_t valueFieldIndex, PivotFilterType type, bool isTop, int32_t itemCount)`. Параметр `valueFieldIndex` — индекс поля данных, агрегированные значения которого используются для ранжирования элементов; `type` определяет единицу, в которой задается `itemCount` (`PivotFilterType::Count` сохраняет фиксированное число элементов, а `PivotFilterType::Percent` сохраняет процент элементов, при этом `itemCount` задает сам процент); `isTop` указывает, следует ли оставить элементы с наивысшими (`true`) или низкими (`false`) значениями, а `itemCount` определяет, сколько элементов или какой процент следует оставить.
В следующем примере загружается рабочая книга со сводной таблицей, содержащей поле значений, применяется фильтр «10 лучших», чтобы оставить 10 элементов с наибольшей суммой продаж, после чего сводная таблица обновляется и рабочая книга сохраняется.
{{% /alert %}}

```cpp
#include "Aspose.Cells.h"
#include <stdexcept>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    U16String inputPath(u"input.xlsx");
    U16String outputPath(u"output.xlsx");
    Workbook workbook(inputPath);
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);
    if (pivotTable.GetDataFields().GetCount() == 0) {
        throw std::runtime_error("Pivot table has no value (data) PivotField.");
    }
    PivotField valueField = pivotTable.GetDataFields().Get(0);
    PivotField rowField = pivotTable.GetRowFields().Get(0);
    int valueFieldIndex = 0;
    rowField.FilterTop10(valueFieldIndex, PivotFilterType::Count, true, 10);
    // Refresh the pivot table data and recalculate it so the filter takes effect
    pivotTable.GetPivotCache().Refresh();
    workbook.Save(outputPath);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Фильтрация путем скрытия или повторного отображения элементов сводной таблицы**
Помимо структурированных API для фильтрации, Aspose.Cells позволяет напрямую управлять видимостью каждого отдельного элемента сводной таблицы. Перебирая коллекцию `PivotItems` поля `PivotField` и переключая свойство `IsHidden`, можно выборочно скрывать определенные элементы без применения фильтра на основе формулы. Установка `IsHidden = true` скрывает элемент из сводной таблицы; установка `IsHidden = false` снова делает его видимым.
Этот подход полезен, если правило фильтрации нестандартно или относится к конкретным элементам, например если необходимо скрыть небольшое количество заданных категорий, которые не должны отображаться в конкретном отчете. В примере ниже загружается рабочая книга со сводной таблицей, скрывается элемент с указанным именем, демонстрируется повторное отображение элемента, обновляется сводная таблица и сохраняется рабочая книга.

```cpp
#include "Aspose.Cells.h"
#include <string>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    // Load an existing workbook containing a pivot table
    Workbook workbook(u"pivot_table_sample.xlsx");
    // Access the first worksheet which contains the pivot table
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    // Access the pivot table by index (the first pivot table on the sheet)
    PivotTable pivotTable = sheet.GetPivotTables().Get(0);
    // Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
    PivotField pivotField = pivotTable.GetRowFields().Get(0);
    // Iterate through the PivotItems collection of the selected PivotField
    int itemCount = pivotField.GetPivotItems().GetCount();
    for (int i = 0; i < itemCount; i++)
    {
        PivotItem item = pivotField.GetPivotItems().Get(i);
        U16String name = item.GetName();
        std::string nameStr = name.ToUtf8();
        // Hide pivot items that match a specific name/criterion
        if (nameStr == "Item1" || nameStr == "Item2")
        {
            item.SetIsHidden(true);
        }
        // Demonstrate unhiding: re-show a previously hidden pivot item
        if (nameStr == "Item3")
        {
            item.SetIsHidden(false);
        }
    }
    // Refresh and recalculate the pivot table so changes take effect
    pivotTable.GetPivotCache().Refresh();
    // Save the workbook — hidden items stay in the underlying data
    // but are excluded from the displayed pivot table output
    workbook.Save(u"output_pivot_filtered.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Сводка**
Aspose.Cells for C++ предоставляет полный набор возможностей фильтрации сводных таблиц, соответствующих возможностям Microsoft Excel. Фильтры по подписям, датам и значениям охватывают наиболее распространенные аналитические сценарии, а фильтр «10 лучших» используется для отчетов с ранжированием. Если правило фильтрации нестандартно, свойство `PivotItem.IsHidden` предлагает гибкую альтернативу на уровне отдельных элементов. Сочетание этих стратегий — например, применение фильтра по подписи с последующим скрытием определенных элементов — позволяет полностью автоматизировать создание точно настроенных отчетов по сводным таблицам.

## Связанные статьи
- [Вставка сводной таблицы](/cells/ru/cpp/create-pivot-table/)
- [Добавление полей строк и столбцов сводной таблицы в Aspose.Cells for C++](/cells/ru/cpp/pivot-table-add-row-and-column-fields/)
- [Добавление полей фильтрации в сводную таблицу в Aspose.Cells for C++](/cells/ru/cpp/add-page-field-in-pivot-table/)
- [Управление полями значений сводной таблицы в Aspose.Cells for C++](/cells/ru/cpp/manage-value-fields/)
- [Обновление сводных таблиц и кэшей сводных таблиц в Aspose.Cells for C++](/cells/ru/cpp/refresh-pivot-table/)

{{< app/cells/assistant language="cpp" >}}
---
title: Форматирование части сводной таблицы
linktitle: Форматирование части сводной таблицы
description: Форматирование части сводной таблицы в Aspose.Cells for C++ путем применения стилей к семантическим областям PivotArea или прямоугольникам CellArea через PivotTable.Format, при этом форматы сохраняются в PivotTable.GetPivotFormats и сохраняются при обновлении сводной таблицы.
keywords: Aspose.Cells, сводная таблица, формат, PivotArea, CellArea, PivotTable.Format, PivotFormats, PivotTableSelectionType, LabelOnly, DataOnly, SelectField, FormatAll, C++
type: docs
weight: 20
url: /ru/cpp/format-part-of-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Варианты использования**
`PivotTable.FormatAll` применяет один стиль ко всей сводной таблице и описан на родительской странице. Он не различает метки, значения, итоги или отдельные области отчета.
На практике обычно требуется выделить только часть сводной таблицы. Часто выделяют метки, относящиеся к одному полю строки, ячейки значений, получаемые от одного поля, строку общего итога или произвольный прямоугольник, например первые две строки элементов.
Применение стиля непосредственно к ячейкам рабочего листа сводной таблицы не эквивалентно. Excel хранит форматирование сводных таблиц как семантические области `PivotArea`, а не как обычные записи стилей ячеек. Формат `PivotArea` остаётся привязанным к области, такой как метки поля или значения данных, и переопределяется при перерасчёте, обновлении или расширении сводной таблицы. Стиль, записанный непосредственно в ячейку, относится к её позиции и не отслеживается моделью сводных таблиц.
Aspose.Cells раскрывает полное семейство перегрузок `PivotTable.Format`, чтобы обеспечить оба типа форматирования:
- `Format(const PivotArea&, const Style&)` привязывает стиль к семантической области, построенной с помощью `PivotArea.Select` или `PivotArea.SelectField`.
- `Format(const CellArea&, const Style&)` привязывает стиль к прямоугольнику рабочего листа внутри сводной таблицы.
- `Format(int32_t row, int32_t column, const Style&)` нацеливается на одну ячейку.
- `FormatAll(const Style&)` форматирует всю сводную таблицу.

## **Форматирование области PivotArea**
Рабочий процесс с семантической областью рекомендуется, когда выделение должно следовать за полем или областью отчета.
1. Создайте объект `PivotArea` с помощью `PivotArea pivotArea(pivotTable);`. Этот объект описывает семантическую область, принадлежащую конкретной сводной таблице.
1. Выберите поле по его нулевой позиции на заданной оси с помощью `PivotArea.Select(PivotFieldType axisType, int32_t fieldPosition, PivotTableSelectionType selectionType)`.
   - `PivotTableSelectionType::DataAndLabel` выбирает как метки, так и данные поля.
   - `PivotTableSelectionType::LabelOnly` выбирает только метки поля.
   - `PivotTableSelectionType::DataOnly` выбирает только ячейки данных поля.
1. Выберите поле по имени с помощью `PivotArea.SelectField(PivotFieldType axisType, const char16_t* fieldName)`. При выборе поля строки по имени область разрешается в ячейки значений, полученные от элементов этого поля.
1. Создайте объект `Style` с помощью `Workbook.CreateStyle()`, настройте его шрифт, цвет переднего плана и сплошной фоновый узор, затем передайте стиль в `PivotTable.Format(pivotArea, style)`.
1. Каждый вызов перегрузки `PivotArea` добавляет одну запись `PivotTableFormat` в `PivotTable.GetPivotFormats()`.
1. Форматы, привязанные к полю, применяются при расчёте данных сводной таблицы. Поэтому после применения форматов вызовите `PivotTable.CalculateData()`, чтобы стили стали видимыми.
Следующий пример создаёт небольшую сводную таблицу продаж фруктов, применяет стиль к меткам строк `Fruit` с помощью `PivotArea.Select` и `PivotTableSelectionType::LabelOnly`, стилизует ячейки значений, полученные от того же поля строки, с помощью `PivotArea.SelectField`, а затем пересчитывает сводную таблицу, чтобы оба стиля отобразились.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    // Fruit sales data
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    U16String fruits[] = { u"Apple", u"Banana", u"Apple", u"Banana", u"Cherry", u"Cherry" };
    int years[] = { 2024, 2024, 2025, 2025, 2024, 2025 };
    int amounts[] = { 100, 150, 120, 180, 90, 110 };
    for (int i = 0; i < 6; i++)
    {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    // Pivot table with its top-left corner at E3
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    // Bold yellow fill on the row field's label cells
    Style labelStyle = workbook.CreateStyle();
    labelStyle.GetFont().SetIsBold(true);
    labelStyle.SetForegroundColor(Color::Yellow());
    labelStyle.SetPattern(BackgroundType::Solid);
    PivotArea labelArea(pivotTable);
    labelArea.Select(PivotFieldType::Row, 0, PivotTableSelectionType::LabelOnly);
    pivotTable.Format(labelArea, labelStyle);
    // Light green fill on the value cells the row field produces
    Style valueStyle = workbook.CreateStyle();
    valueStyle.SetForegroundColor(Color::LightGreen());
    valueStyle.SetPattern(BackgroundType::Solid);
    PivotArea valueArea(pivotTable);
    valueArea.SelectField(PivotFieldType::Row, u"Fruit");
    pivotTable.Format(valueArea, valueStyle);
    // Field-anchored formats are painted when the data is calculated
    pivotTable.CalculateData();
    // Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
    workbook.Save(u"FormatPivotArea.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Форматирование области CellArea сводной таблицы**
Используйте `PivotTable.Format(const CellArea&, const Style&)`, когда интересующая область представляет собой простой прямоугольник рабочего листа, а не семантическую область сводной таблицы.
`CellArea` описывается публичными полями `StartRow`, `StartColumn`, `EndRow` и `EndColumn`. Значения являются координатами рабочего листа с нулевой основой, а конечные координаты указывают последнюю включённую строку и столбец, поэтому область охватывает ячейки от начальной позиции до конечной включительно.
В отличие от формата, привязанного к полю, формат `CellArea` применяется к ячейкам сразу. Дополнительный вызов `CalculateData()` не требуется для появления стиля.
Прямоугольник `CellArea` может одновременно содержать ячейки меток и ячейки значений. Следующий раздел описывает, как Aspose.Cells и Excel представляют этот прямоугольник внутренне.
Следующий пример форматирует прямоугольник `E4:F5` сводной таблицы с помощью курсива и светло‑голубого стиля и сохраняет рабочую книгу без дополнительного пересчёта.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    U16String fruits[] = { u"Apple", u"Banana", u"Apple", u"Banana", u"Cherry", u"Cherry" };
    int years[] = { 2024, 2024, 2025, 2025, 2024, 2025 };
    int amounts[] = { 100, 150, 120, 180, 90, 110 };
    for (int i = 0; i < 6; i++)
    {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    // Highlight the first two fruit rows (the rectangle E4:F5)
    Style highlightStyle = workbook.CreateStyle();
    highlightStyle.GetFont().SetIsItalic(true);
    highlightStyle.SetForegroundColor(Color{ 0xFF, 0x99, 0xCC, 0xFF });
    highlightStyle.SetPattern(BackgroundType::Solid);
    CellArea rectangle;
    rectangle.StartRow = 3;
    rectangle.StartColumn = 4;
    rectangle.EndRow = 4;
    rectangle.EndColumn = 5;
    pivotTable.Format(rectangle, highlightStyle);
    // E4:F5 is italic on light blue immediately, no recalculation needed
    workbook.Save(u"FormatPivotCellArea.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Как сопоставляются PivotArea и CellArea**
Excel хранит форматирование сводных таблиц как записи `pivotArea`, а не как обычные записи стилей ячеек рабочего листа. Такая же модель используется в Aspose.Cells, поэтому запрос на форматирование переводится в pivot‑области при его записи.
Связь между `CellArea`, предоставленной пользователем, и внутренними pivot‑областями является многие‑ко‑многим в обоих направлениях.
- Одна `CellArea` может породить несколько pivot‑областей. Если прямоугольник охватывает как ячейки меток, так и ячейки значений, он разбивается на отдельные правила для меток и данных, поскольку модель сводных таблиц рассматривает форматирование меток и данных независимо.
- Одна pivot‑область может разрешаться в несколько разрозненных экземпляров `CellArea`. Семантическая область, например строка общего итога, или поле, у которого элементы не идут подряд, может охватывать несколько прямоугольников. Поэтому `PivotArea.GetCellAreas()` возвращает `Vector<CellArea>`, а не один прямоугольник.
Каждая операция форматирования, выполненная через `PivotTable.Format`, записывается в `PivotTable.GetPivotFormats()`. Каждая запись `PivotTableFormat` раскрывает связанный `PivotArea` и применённый к нему `Style`. Перегрузка `PivotArea` добавляет ровно одну запись за вызов, в то время как `CellArea`, содержащий разные семантические области, может добавить несколько записей.
Чтобы различать сохранённые области, каждый `PivotArea` предоставляет флаги `GetOnlyLabel()` и `GetOnlyData()`. Пример ниже форматирует один прямоугольник, охватывающий как метки, так и значения, проверяет `PivotTable.GetPivotFormats()` и выводит координаты `CellArea`, к которым каждая сохранённая pivot‑область разрешается.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    U16String fruits[] = { u"Apple", u"Banana", u"Apple", u"Banana", u"Cherry", u"Cherry" };
    int years[] = { 2024, 2024, 2025, 2025, 2024, 2025 };
    int amounts[] = { 100, 150, 120, 180, 90, 110 };
    for (int i = 0; i < 6; i++)
    {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    Style highlightStyle = workbook.CreateStyle();
    highlightStyle.GetFont().SetIsItalic(true);
    highlightStyle.SetForegroundColor(Color{ 0xFF, 0x99, 0xCC, 0xFF });
    highlightStyle.SetPattern(BackgroundType::Solid);
    // ONE rectangle in...
    CellArea rectangle;
    rectangle.StartRow = 3;
    rectangle.StartColumn = 4;
    rectangle.EndRow = 4;
    rectangle.EndColumn = 5;
    pivotTable.Format(rectangle, highlightStyle);
    // ...TWO semantic pivot areas out: the label part and the data part are stored separately
    std::cout << "Stored formats: " << pivotTable.GetPivotFormats().GetCount() << std::endl;
    for (int i = 0; i < pivotTable.GetPivotFormats().GetCount(); i++)
    {
        PivotArea storedArea = pivotTable.GetPivotFormats().Get(i).GetPivotArea();
        std::cout << "Format " << i << ": OnlyLabel=" << (storedArea.GetOnlyLabel() ? "true" : "false")
                  << ", OnlyData=" << (storedArea.GetOnlyData() ? "true" : "false") << std::endl;
        Vector<CellArea> resolved = storedArea.GetCellAreas();
        for (int j = 0; j < resolved.GetLength(); j++)
        {
            std::cout << "    rows " << (resolved[j].StartRow + 1) << "-" << (resolved[j].EndRow + 1)
                      << ", columns " << (resolved[j].StartColumn + 1) << "-" << (resolved[j].EndColumn + 1) << std::endl;
        }
    }
    // This prints:
    // Stored formats: 2
    // Format 0: OnlyLabel=true, OnlyData=false
    //     rows 4-5, columns 5-5        (E4:E5, the label part)
    // Format 1: OnlyLabel=false, OnlyData=true
    //     rows 4-5, columns 6-6        (F4:F5, the data part)
    workbook.Save(u"FormatPivotAreasMap.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}
Поскольку форматы хранятся как pivot‑области, а не как обычные стили ячеек, они сохраняются при перерасчёте и обновлении. Когда сводная таблица обновляется с помощью `PivotTable.RefreshData`, перерасчитывается через `CalculateData` или сохраняется и загружается заново, каждая сохранённая pivot‑область повторно разрешается к текущей позиции своей области, и её стиль повторно применяется.
{{% /alert %}}

Используйте `PivotArea`, построенный с помощью `Select` или `SelectField`, когда выделение должно оставаться привязанным к полю или семантической области при обновлениях, и используйте `CellArea`, когда достаточно отформатировать фиксированный прямоугольник в текущей раскладке сводной таблицы. Перегрузка `Format(int32_t row, int32_t column, const Style&)` для одной ячейки нацелена на отдельную ячейку. Применяйте `FormatAll`, описанный на родительской странице, когда требуется переоформить всю сводную таблицу сразу.

## **Related Articles**
- [Применение стиля к сводной таблице](/cells/ru/cpp/apply-style-to-pivot-table/)
- [Добавление полей строк и столбцов сводной таблицы](/cells/ru/cpp/pivot-table-add-row-and-column-fields/)
- [Управление полями значений в сводной таблице](/cells/ru/cpp/manage-value-fields/)
- [Обновление сводной таблицы](/cells/ru/cpp/refresh-pivot-table/)

{{< app/cells/assistant language="cpp" >}}
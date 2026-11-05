---
title: Добавление условного форматирования к сводной таблице
linktitle: Добавление условного форматирования к сводной таблице
description: Добавьте условное форматирование к сводной таблице в Aspose.Cells for C++ — привяжите правило к области данных с помощью ApplyTo и области PivotConditionFormatScopeType, или определите цель с помощью AddCellArea и PivotAreas, затем прикрепите правила и стили через FormatConditions.AddCondition.
keywords: Aspose.Cells for C++, сводная таблица, условное форматирование, PivotConditionalFormat, ConditionalFormats, ApplyTo, PivotConditionFormatScopeType, Data, Field, Selection, AddCellArea, PivotAreas, AddPivotArea, FormatConditions, AddCondition, FormatConditionType, C++
type: docs
weight: 30
url: /ru/cpp/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
Стили, описанные на родительской странице и на соседней странице, являются статическими — область `PivotArea` или `CellArea` окрашивается один раз и сохраняет свой стиль независимо от значений. Условное форматирование — это управляемый правилами аналог: выделять каждое значение, превышающее 200, затемнять средние пятьдесят процентов или помечать элементы с низшим рейтингом — и выделение следует за значениями каждый раз, когда сводная таблица пересчитывается или обновляется.  
В Aspose.Cells условное форматирование сводных таблиц находится в коллекции `pivotTable.GetConditionalFormats()`. Каждый элемент представляет собой `PivotConditionalFormat`, который независимо отвечает на два вопроса:
- **Где применяется правило?** Целевая область определяется либо через `ApplyTo(int row, int column, PivotConditionFormatScopeType scope)`, что отражает выбор области в пользовательском интерфейсе Excel, либо через `AddCellArea(CellArea)` и коллекцию `GetPivotAreas()`, которые явно задают область.
- **Что проверяет правило?** Одна или несколько условий добавляются через `GetFormatConditions()` с помощью `FormatConditionCollection.AddCondition(FormatConditionType type, OperatorType operatorType, String formula1, String formula2)`, причём каждое условие имеет свой собственный `Style`.

{{% alert color="primary" %}}
Не вызывайте `FormatConditionCollection.Add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` или `FormatConditionCollection.AddArea(CellArea)` у объекта `GetFormatConditions()` условного формата сводной таблицы. Эти два перегруженных метода унаследованы из обычного API условного форматирования листа и не работают со сводными таблицами — область ячеек никогда не преобразуется в область сводной таблицы, поэтому запрос молча игнорируется. Всегда задавайте область непосредственно на объекте `PivotConditionalFormat` (`ApplyTo`, `AddCellArea` или `GetPivotAreas()`) и добавляйте правило с помощью одной из перегрузок `AddCondition`.
{{% /alert %}}

## **Применение правила с областью (способ интерфейса Excel)**
Первый способ позиционирует правило так, как это делает пользовательский интерфейс Excel. Ячейка сводной таблицы определяется её нулевыми координатами листа, а область `PivotConditionFormatScopeType` указывает Aspose.Cells, насколько далеко правило должно распространяться от этой ячейки:
- `PivotConditionFormatScopeType::Data` — все ячейки значений, которые создаёт сводная таблица, включая общие итоги.
- `PivotConditionFormatScopeType::Field` — ячейки значений, принадлежащие полю, которое идентифицирует ячейка, без общих итогов. Ячейка должна быть ячейкой поля, например меткой строкового поля; передача ячейки значения вызывает исключение.
- `PivotConditionFormatScopeType::Selection` — только ячейки значений на пересечении, которое выбирает ячейка, обычно одна ячейка значения.
Пример ниже создаёт сводную таблицу продаж фруктов, левый верхний угол которой находится в E3, привязывает условный формат к ячейке F4 (строка 3, столбец 5) с областью `Data` и выделяет каждое значение более 200 полужирным шрифтом, белым цветом на красном фоне. При значениях Apple 220, Banana 330, Cherry 200 и общем итоге 750 правило окрашивает F4, F5 и F7 — применяемая область — весь столбец данных F4:F7, и только ячейки, значение которых удовлетворяет условию, подсвечиваются.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    const char16_t* fruits[] = {u"Apple", u"Banana", u"Apple", u"Banana", u"Cherry", u"Cherry"};
    int years[] = {2024, 2024, 2025, 2025, 2024, 2025};
    int amounts[] = {100, 150, 120, 180, 90, 110};
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    for (int i = 0; i < 6; ++i) {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    int index = pivotTable.GetConditionalFormats().Add();
    PivotConditionalFormat format = pivotTable.GetConditionalFormats().Get(index);
    format.ApplyTo(3, 5, PivotConditionFormatScopeType::Data);
    int conditionIndex = format.GetFormatConditions().AddCondition(
        FormatConditionType::CellValue, OperatorType::GreaterThan, u"200", nullptr);
    Style style = workbook.CreateStyle();
    Font font = style.GetFont();
    font.SetIsBold(true);
    font.SetColor(Color::White());
    style.SetForegroundColor(Color::Red());
    style.SetPattern(BackgroundType::Solid);
    format.GetFormatConditions().Get(conditionIndex).SetStyle(style);
    workbook.Save(u"PivotConditionalFormatData.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

Привязка того же правила к метке поля строки E4 (строка 3, столбец 4) с областью `Field` приводит к диапазону F4:F6 — тот же столбец данных без строки общего итога, — поскольку область теперь описывает поле `Fruit`, а не всю область значений. Область `Selection`, привязанная к F4, ограничивается только ячейкой F4.

## **Определение области вручную**
Второй способ пропускает выбор области и явно задаёт её в `PivotConditionalFormat`.

### **Прямоугольник листа с помощью AddCellArea**
`AddCellArea(CellArea)` сохраняет заданный прямоугольник в качестве цели правила. Координаты — нуль‑индексные координаты листа, и область точно соответствует предоставленному прямоугольнику — без расширения до столбца данных и без логики общих итогов. Используйте её, когда интересующие ячейки представляют собой известный фиксированный прямоугольник текущего макета сводной таблицы.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    U16String fruits[] = {
        U16String(u"Apple"),
        U16String(u"Banana"),
        U16String(u"Apple"),
        U16String(u"Banana"),
        U16String(u"Cherry"),
        U16String(u"Cherry")
    };
    int years[] = {2024, 2024, 2025, 2025, 2024, 2025};
    int amounts[] = {100, 150, 120, 180, 90, 110};
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    for (int i = 0; i < 6; ++i) {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, U16String(u"Fruit"));
    pivotTable.AddFieldToArea(PivotFieldType::Data, U16String(u"Amount"));
    pivotTable.CalculateData();
    int32_t index = pivotTable.GetConditionalFormats().Add();
    PivotConditionalFormat format = pivotTable.GetConditionalFormats().Get(index);
    CellArea area;
    area.StartRow = 3;
    area.EndRow = 5;
    area.StartColumn = 5;
    area.EndColumn = 5;
    format.AddCellArea(area);
    int32_t conditionIndex = format.GetFormatConditions().AddCondition(
        FormatConditionType::CellValue,
        OperatorType::Between,
        u"150",
        u"300");
    Style style = workbook.CreateStyle();
    style.GetFont().SetIsItalic(true);
    style.SetForegroundColor(Color::LightYellow());
    style.SetPattern(BackgroundType::Solid);
    format.GetFormatConditions().Get(conditionIndex).SetStyle(style);
    workbook.Save(u"PivotConditionalFormatCellArea.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Семантическая область сводной таблицы с PivotAreas**
`GetPivotAreas()` предоставляет ту же модель семантической области, которую использует соседняя страница для статических стилей. Создайте `PivotArea`, выберите поле или область с помощью `Select` или `SelectField` и добавьте её через `GetPivotAreas().AddPivotArea(PivotArea)`. Семантическая область остаётся привязанной к своему полю, поэтому условный формат следует за полем при обновлении сводной таблицы и смещении макета. Перегрузка `GetPivotAreas().Add(PivotArea)` всё ещё компилируется, но помечена как устаревшая — предпочтительно использовать `AddPivotArea`.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    const char16_t* fruits[] = {u"Apple", u"Banana", u"Apple", u"Banana", u"Cherry", u"Cherry"};
    int years[] = {2024, 2024, 2025, 2025, 2024, 2025};
    int amounts[] = {100, 150, 120, 180, 90, 110};
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    for (int i = 0; i < 6; ++i) {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    int index = pivotTable.GetConditionalFormats().Add();
    PivotConditionalFormat format = pivotTable.GetConditionalFormats().Get(index);
    PivotArea area(pivotTable);
    area.SelectField(PivotFieldType::Data, u"Amount");
    format.GetPivotAreas().AddPivotArea(area);
    int conditionIndex = format.GetFormatConditions().AddCondition(
        FormatConditionType::CellValue, OperatorType::LessThan, u"150", nullptr);
    Style style = workbook.CreateStyle();
    style.GetFont().SetColor(Color::Gray());
    format.GetFormatConditions().Get(conditionIndex).SetStyle(style);
    workbook.Save(u"PivotConditionalFormatPivotArea.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Где хранятся правила и как они сохраняются после перезагрузки**
Каждый вызов `pivotTable.GetConditionalFormats().Add()` добавляет один `PivotConditionalFormat` в сводную таблицу. Условия, их формулы и стили сохраняются вместе с рабочей книгой — при повторном открытии файла в примере ниже отображаются то же правило с его типом, оператором и формулой, а `GetCellAreas()` сообщает те же области. Элементы, которым никогда не было присвоено условие, отбрасываются при сохранении рабочей книги, так же, как Excel удаляет условный формат без правила.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
static const char* ToString(FormatConditionType type)
{
    switch (type)
    {
    case FormatConditionType::CellValue:
        return "CellValue";
    default:
        return "Unknown";
    }
}
static const char* ToString(OperatorType op)
{
    switch (op)
    {
    case OperatorType::GreaterThan:
        return "GreaterThan";
    default:
        return "Unknown";
    }
}
int main()
{
    Aspose::Cells::Startup();
    Workbook workbook(u"PivotConditionalFormatData.xlsx");
    PivotTable pivotTable = workbook.GetWorksheets().Get(0).GetPivotTables().Get(0);
    auto conditionalFormats = pivotTable.GetConditionalFormats();
    int formatCount = conditionalFormats.GetCount();
    std::cout << "Conditional formats: " << formatCount << std::endl;
    for (int i = 0; i < formatCount; ++i)
    {
        PivotConditionalFormat format = conditionalFormats.Get(i);
        auto formatConditions = format.GetFormatConditions();
        int conditionCount = formatConditions.GetCount();
        for (int j = 0; j < conditionCount; ++j)
        {
            FormatCondition condition = formatConditions.Get(j);
            std::cout << "Format " << i << ": "
                      << ToString(condition.GetType()) << " "
                      << ToString(condition.GetOperator())
                      << " formula1=" << condition.GetFormula1().ToUtf8()
                      << std::endl;
        }
        Vector<CellArea> areas = format.GetCellAreas();
        for (int k = 0; k < areas.GetLength(); ++k)
        {
            CellArea area = areas[k];
            std::cout << "    rows " << area.StartRow + 1 << "-" << area.EndRow + 1
                      << ", columns " << area.StartColumn + 1 << "-" << area.EndColumn + 1
                      << std::endl;
        }
    }
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Связанные статьи**
- [Применение стиля к сводной таблице](/cells/ru/cpp/apply-style-to-pivot-table/)
- [Форматирование части сводной таблицы](/cells/ru/cpp/format-part-of-pivot-table/)
- [Топ‑10 отображения или фильтрации в сводной таблице](/cells/ru/cpp/top-10-show-or-filter-in-pivot-table/)
- [Фильтрация сводных таблиц по метке или значению](/cells/ru/cpp/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="cpp" >}}
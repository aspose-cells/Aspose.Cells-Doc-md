---
title: Дискретная группировка элементов полей сводной таблицы
linktitle: Дискретная группировка
description: Узнайте, как группировать элементы полей сводной таблицы в пользовательские группы с заданными именами, например «фрукты» и «овощи», с помощью DiscreteGroupItem и PivotFieldGroupOptions.DiscreteGroupItems в Aspose.Cells for C++.
keywords: Aspose.Cells for C++, сводная таблица, дискретная группировка, DiscreteGroupItem, PivotFieldGroupOptions, группировка элементов сводной таблицы, пользовательские группы, PivotField.Group, C++, сводная таблица Excel
type: docs
weight: 90
url: /ru/cpp/discrete-group-pivot-fields/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
- Автоматическая группировка объединяет элементы по типу данных: даты — по месяцам и кварталам, а числа — по диапазонам. Дискретная группировка решает противоположную задачу, объединяя определенные несвязанные элементы в пользовательские группы с заданными именами, например продукты — в группы «фрукты» и «овощи», магазины — по регионам, а счета — по зонам. Aspose.Cells обеспечивает дискретную группировку с помощью класса `DiscreteGroupItem` и свойства `PivotFieldGroupOptions.DiscreteGroupItems`.
- Экземпляр `DiscreteGroupItem` представляет собой группу с заданным именем и входящими в нее элементами. Элементы можно идентифицировать двумя способами: по именам (`DiscreteGroupItem("fruit", { "grape", "cherry" })`) или по индексам элементов в исходных данных (нумерация начинается с нуля) (`DiscreteGroupItem("fruit", { 0, 3 })`). Обе формы дают одинаковый результат.
- Дискретная группировка применяется к полю в области строк или столбцов сводной таблицы путем передачи параметров группировки в метод `PivotField.Group(PivotFieldGroupOptions)`.

## **Группировка элементов поля по именам элементов**
В следующем примере создается небольшой список продаж (продукт, дата и сумма), на основе которого формируется сводная таблица, в которой `product` размещается в области строк, `date` — в области столбцов, а `amount` — в области данных. Затем определяются две пользовательские группы по именам элементов: `fruit` (`grape`, `cherry`) и `vegetables` (`carrot`, `potato`). В результате отображается двухуровневая структура строк: имя группы располагается на внешнем уровне, а исходные элементы вложены под ним, поэтому тенденции можно отслеживать как по каждой пользовательской группе, так и по каждому элементу.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(0, 0).PutValue(u"product");
    cells.Get(1, 0).PutValue(u"grape");
    cells.Get(2, 0).PutValue(u"carrot");
    cells.Get(3, 0).PutValue(u"potato");
    cells.Get(4, 0).PutValue(u"cherry");
    Style dateStyle = wb.CreateStyle();
    dateStyle.SetCustom(u"m/d/yyyy");
    cells.Get(0, 1).PutValue(u"date");
    cells.Get(1, 1).PutValue(Date{2021, 2, 5, 0, 0, 0, 0});
    cells.Get(2, 1).PutValue(Date{2022, 3, 8, 0, 0, 0, 0});
    cells.Get(3, 1).PutValue(Date{2023, 4, 10, 0, 0, 0, 0});
    cells.Get(4, 1).PutValue(Date{2024, 5, 16, 0, 0, 0, 0});
    for (int r = 1; r <= 4; ++r) {
        cells.Get(r, 1).SetStyle(dateStyle);
    }
    cells.Get(0, 2).PutValue(u"amount");
    cells.Get(1, 2).PutValue(50);
    cells.Get(2, 2).PutValue(60);
    cells.Get(3, 2).PutValue(70);
    cells.Get(4, 2).PutValue(80);
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=Sheet1!A1:C5", 11, 0);
    pivotTable.AddFieldToArea(PivotFieldType::Row, U16String(u"product"));
    pivotTable.AddFieldToArea(PivotFieldType::Column, U16String(u"date"));
    pivotTable.AddFieldToArea(PivotFieldType::Data, U16String(u"amount"));
    pivotTable.SetPivotTableStyleType(PivotTableStyleType::PivotTableStyleMedium10);
    DiscreteGroupItem fruit(u"fruit", Vector<U16String>{u"grape", u"cherry"});
    DiscreteGroupItem vegetable(u"vegetable", Vector<U16String>{u"carrot", u"potato"});
    PivotFieldGroupOptions groupOptions;
    groupOptions.SetDiscreteGroupItems(Vector<DiscreteGroupItem>{fruit, vegetable});
    pivotTable.GetRowFields().Get(0).Group(groupOptions);
    pivotTable.CalculateData();
    wb.Save(u"outputDiscreteGroupPivotField.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

После `CalculateData()` в области строк сводной таблицы отображаются `fruit` (`grape` 50, `cherry` 80) и `vegetable` (`carrot` 60, `potato` 70), а общий итог составляет 260; метки столбцов по-прежнему содержат четыре даты (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024).

## **Группировка элементов поля по индексам**
Если имена элементов длинные или локализованы, второй конструктор `DiscreteGroupItem` идентифицирует элементы по индексу. Индексы соответствуют позициям элементов в порядке их появления в исходных данных, а не в алфавитном порядке; нумерация начинается с нуля. В приведенных выше данных `grape` имеет индекс 0, `carrot` — индекс 1, `potato` — индекс 2, а `cherry` — индекс 3, поэтому для `fruit` используется `{ 0, 3 }`, а для `vegetable` — `{ 1, 2 }`. Результат идентичен примеру группировки по именам.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(0, 0).PutValue(u"product");
    cells.Get(1, 0).PutValue(u"grape");
    cells.Get(2, 0).PutValue(u"carrot");
    cells.Get(3, 0).PutValue(u"potato");
    cells.Get(4, 0).PutValue(u"cherry");
    Style dateStyle = wb.CreateStyle();
    dateStyle.SetCustom(u"m/d/yyyy");
    cells.Get(0, 1).PutValue(u"date");
    Date firstDate{2021, 2, 5, 0, 0, 0, 0};
    Date secondDate{2022, 3, 8, 0, 0, 0, 0};
    Date thirdDate{2023, 4, 10, 0, 0, 0, 0};
    Date fourthDate{2024, 5, 16, 0, 0, 0, 0};
    cells.Get(1, 1).PutValue(firstDate);
    cells.Get(2, 1).PutValue(secondDate);
    cells.Get(3, 1).PutValue(thirdDate);
    cells.Get(4, 1).PutValue(fourthDate);
    for (int r = 1; r <= 4; ++r) {
        cells.Get(r, 1).SetStyle(dateStyle);
    }
    cells.Get(0, 2).PutValue(u"amount");
    cells.Get(1, 2).PutValue(50);
    cells.Get(2, 2).PutValue(60);
    cells.Get(3, 2).PutValue(70);
    cells.Get(4, 2).PutValue(80);
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=Sheet1!A1:C5", 11, 0);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"product");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"date");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"amount");
    pivotTable.SetPivotTableStyleType(PivotTableStyleType::PivotTableStyleMedium10);
    DiscreteGroupItem fruit(u"fruit", Vector<int32_t>{0, 3});
    DiscreteGroupItem vegetable(u"vegetable", Vector<int32_t>{1, 2});
    PivotFieldGroupOptions groupOptions;
    groupOptions.SetDiscreteGroupItems(Vector<DiscreteGroupItem>{fruit, vegetable});
    pivotTable.GetRowFields().Get(0).Group(groupOptions);
    pivotTable.CalculateData();
    wb.Save(u"outputDiscreteGroupPivotFieldByIndex.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Примечание**

{{% alert color="primary" %}}
- Элементы, не включенные ни в одну пользовательскую группу, не теряются. Они остаются в сводной таблице на том же уровне, что и пользовательские группы, и отображаются в виде отдельных одноэлементных записей. В приведенном выше примере определение только группы `fruit` оставляет `carrot` и `potato` в области строк как отдельные записи рядом с группой `fruit`.
- Свойство `PivotFieldGroupOptions.NewPivotField` управляет компоновкой дискретной группировки. По умолчанию его значение равно `true`: сгруппированное поле добавляется как новое внешнее поле рядом с исходным, что создает двухуровневую структуру, показанную выше (количество полей в `RowFields` увеличивается до 2). Установите его в `false`, чтобы заменить исходное поле; тогда в области строк будет отображаться один уровень, содержащий только имена групп и их агрегированные значения: `fruit` 130 (50 + 80) и `vegetable` 130 (60 + 70).
- Конструкторы `DiscreteGroupItem`, основанные на именах и индексах, можно использовать совместно в рамках одной коллекции `DiscreteGroupItems`.
{{% /alert %}}

## **Связанные статьи**
- [Группировка полей сводной таблицы](/cells/ru/cpp/group-pivot-fields-in-the-pivot-table/)
- [Добавление полей строк и столбцов в сводную таблицу](/cells/ru/cpp/pivot-table-add-row-and-column-fields/)
- [Фильтрация сводных таблиц по метке или значению](/cells/ru/cpp/filter-by-label-or-value-of-pivot-table/)
- [Применение стиля к сводной таблице](/cells/ru/cpp/apply-style-to-pivot-table/)
- [Обновление сводной таблицы](/cells/ru/cpp/refresh-pivot-table/)

{{< app/cells/assistant language="cpp" >}}
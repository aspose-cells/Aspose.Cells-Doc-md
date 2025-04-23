---
title: Указание абсолютной позиции элемента сводной таблицы с помощью C++
linktitle: Указание абсолютного положения элемента сводной таблицы
type: docs
weight: 50
url: /ru/cpp/specifying-the-absolute-position-of-the-pivot-item/
description: Узнайте, как указать абсолютную позицию элементов сводной таблицы в C++ с помощью Aspose.Cells.
---

{{% alert color="primary" %}}

Иногда пользователи должны указывать абсолютную позицию элементов сводной таблицы. API Aspose.Cells ввело несколько новых свойств и метод для реализации этого требования.

- Добавлено свойство [**PivotItem.GetPosition()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getposition/), которое можно использовать для указания индекса позиции во всех PivotItems независимо от родительского узла. Добавлено свойство [**PivotItem.GetPositionInSameParentNode()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getpositioninsameparentnode/), которое можно использовать для указания индекса позиции в PivotItems под тем же родительским узлом.
- Добавлен метод [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/move/) для перемещения элемента вверх или вниз на основе значения счетчика, где счетчик — это число позиций для перемещения PivotItem вверх или вниз. Если значение счетчика меньше нуля, элемент перемещается вверх, а если больше нуля — вниз. Параметр типа Boolean `isSameParent` указывает, нужно ли выполнять операцию в рамках одного и того же родительского узла.
- Устарел метод `PivotItem.Move(int count)`; рекомендуется использовать недавно добавленный метод [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/move/).

{{% /alert %}}

Следующий пример кода создает сводную таблицу и указывает позиции элементов сводной таблицы в одном родительском узле. Вы можете скачать исходный Excel-файл [source Excel](5112632.xlsx) и итоговый файл [output Excel](5112619.xlsx) для ознакомления. Открыв итоговый файл, вы увидите, что элемент "4H12" занимает 0-ю позицию в родительском элементе "K11", а "DIF400" — 3-ю позицию. Аналогично CA32 находится на позиции 1, а AAA3 — на позиции 2.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook
    Workbook wb(srcDir + u"source.xlsx");

    // Add new worksheet for pivot table
    WorksheetCollection worksheets = wb.GetWorksheets();
    Worksheet wsPivot = worksheets.Add(u"pvtNew Hardware");
    Worksheet wsData = worksheets.Get(u"New Hardware - Yearly");

    // Get the pivot tables collection for the pivot sheet
    PivotTableCollection pivotTables = wsPivot.GetPivotTables();

    // Add PivotTable to the worksheet
    int index = pivotTables.Add(u"='New Hardware - Yearly'!A1:D621", u"A3", u"HWCounts_PivotTable");

    // Get the PivotTable object
    PivotTable pvtTable = pivotTables.Get(index);

    // Add vendor row field
    pvtTable.AddFieldToArea(PivotFieldType::Row, u"Vendor");

    // Add item row field
    pvtTable.AddFieldToArea(PivotFieldType::Row, u"Item");

    // Add data field
    pvtTable.AddFieldToArea(PivotFieldType::Data, u"2014");

    // Turn off the subtotals for the vendor row field
    PivotField pivotField = pvtTable.GetRowFields().Get(u"Vendor");
    pivotField.SetSubtotals(PivotFieldSubtotalType::None, true);

    // Turn off grand total
    pvtTable.SetShowColumnGrandTotals(false);

    // Refresh and calculate data before modifying pivot items
    pvtTable.RefreshData();
    pvtTable.CalculateData();

    // Set positions for specific pivot items
    pvtTable.GetRowFields().Get(u"Item").GetPivotItems().Get(u"4H12").SetPositionInSameParentNode(0);
    pvtTable.GetRowFields().Get(u"Item").GetPivotItems().Get(u"DIF400").SetPositionInSameParentNode(3);

    // Recalculate data after modifying pivot items
    pvtTable.CalculateData();

    // Set positions for additional pivot items
    pvtTable.GetRowFields().Get(u"Item").GetPivotItems().Get(u"CA32").SetPositionInSameParentNode(1);
    pvtTable.GetRowFields().Get(u"Item").GetPivotItems().Get(u"AAA3").SetPositionInSameParentNode(2);

    // Save the workbook
    wb.Save(outDir + u"output_out.xlsx");

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Обратите внимание, что перед использованием свойств [**PivotItem.GetPosition()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getposition/), [**PivotItem.GetPositionInSameParentNode()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getpositioninsameparentnode/) и метода [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/move/) необходимо вызвать методы `PivotTable.RefreshData` и `PivotTable.CalculateData`.

{{% /alert %}}

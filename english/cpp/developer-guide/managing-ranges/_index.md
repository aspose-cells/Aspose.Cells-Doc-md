---
title: Managing Ranges with C++
linktitle: Ranges
type: docs
weight: 105
url: /cpp/managing-ranges/
description: Learn how to manage ranges in Excel files using Aspose.Cells with C++. Create, modify, and style ranges programmatically.
---

## **Introduction**

In Excel, you can select multiple cells with a mouse box selection, the set of selected cells is called "Range".

For example, you can click the left mouse button in Cell "A1" of the Excel and then drag to cell "C4". The rectangular area you selected can also be easily created as an object by using Aspose.Cells.

Here is how to create range, put value, set style, and do more operations to the "Range" object.

## **Managing Ranges Using Aspose.Cells**

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) class contains a [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) collection that allows access to each worksheet in an Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class. The [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class provides a [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection.

### **Create Range**

When you want to create a rectangular area that extends over A1:C4, you can use the following code:

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook
    Workbook workbook;

    // Get Cells from the first worksheet
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Create a Range from A1 to C4
    Range range = cells.CreateRange(u"A1:C4");

    Aspose::Cells::Cleanup();
}
```

### **Put value into the Cells of the Range**

Say you have a range of cells that extends over A1:C4. The matrix makes 4 * 3 = 12 cells. The individual range cells are arranged sequentially: Range[0,0], Range[0,1], Range[0,2], Range[1,0], Range[1,1], Range[1,2], Range[2,0], Range[2,1], Range[2,2], Range[3,0], Range[3,1], Range[3,2].

The following example shows how to input some values into the cells of the Range.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook
    Workbook workbook;

    // Get Cells from the first worksheet
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Create a Range from A1 to C4
    Range range = cells.CreateRange(u"A1:C4");

    // Put values in specific cells
    range.Get(0, 0).PutValue(u"A1");
    range.Get(0, 1).PutValue(u"B1");
    range.Get(0, 2).PutValue(u"C1");
    range.Get(3, 0).PutValue(u"A4");
    range.Get(3, 1).PutValue(u"B4");
    range.Get(3, 2).PutValue(u"C4");

    // Save the Workbook
    workbook.Save(u"RangeValueTest.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Set style of the Cells of the Range**

The following example shows how to set style of the cells of the Range.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook
    Workbook workbook;

    // Get Cells
    WorksheetCollection sheets = workbook.GetWorksheets();
    Cells cells = sheets.Get(0).GetCells();

    // Create Range
    Range range = cells.CreateRange(u"A1:C4");

    // Put value
    range.Get(0, 0).PutValue(u"A1");
    range.Get(3, 2).PutValue(u"C4");

    // Set Style
    Style style00 = workbook.CreateStyle();
    style00.SetPattern(BackgroundType::Solid);
    style00.SetForegroundColor(Color::Red());
    range.Get(0, 0).SetStyle(style00);

    Style style32 = workbook.CreateStyle();
    style32.SetPattern(BackgroundType::HorizontalStripe);
    style32.SetForegroundColor(Color::Green());
    range.Get(3, 2).SetStyle(style32);

    // Save the Workbook
    workbook.Save(u"RangeStyleTest.xlsx");

    std::cout << "Workbook saved successfully with range styles applied!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Get CurrentRegion of the Range**

CurrentRegion is a property that returns a Range object that represents the current region. 

The current region is a range bounded by any combination of blank rows and blank columns. Read-only.

In excel, you can get CurrentRegion area by:
1. Select an area(range1) with the mouse box.
2. Click "Home - Editing - Find & Select - Go To Special - Currect region", or use "Ctrl+Shift+*", you will see excel automatically helps you select an area(range2), now you made it, range2 is the CurrentRegion of range1.

Using Aspose.Cells, you can use "Range.CurrentRegion" property to perform the same function.

Please downloaded the following test file, open it in excel, use the mouse box to select an area "A1:D7", then click "Ctrl+Shift+*", you will see area "A1:C3" selected.

[current_region.xlsx](current_region.xlsx)

Now please run the following example, see how it works in Aspose.Cells:

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook
    Workbook workbook(u"current_region.xlsx");

    // Get Cells from the first worksheet
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Create a Range from A1 to D7
    Range src = cells.CreateRange(u"A1:D7");

    // Get the CurrentRegion of the created range
    Range A1C3 = src.GetCurrentRegion();

    Aspose::Cells::Cleanup();
}
```


## **Advance topics**
- [AutoFill range of Excel file](/cells/cpp/autofill-ranges/)
- [Copy Ranges of Excel](/cells/cpp/copy-ranges-of-Excel/)
- [Copy Range Data Only](/cells/cpp/copy-range-data-only/)
- [Copy Range Data with Style](/cells/cpp/copy-range-data-with-style/)
- [Copy Range Style Only](/cells/cpp/copy-range-style-only/)
- [Create Union Range](/cells/cpp/create-union-range/)
- [Cut and Paste Range](/cells/cpp/cut-and-paste-cells/)
- [Delete Ranges](/cells/cpp/delete-ranges-from-Excel/)
- [Get Address Cell Count Offset Entire Column and Entire Row of the Range](/cells/cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [Insert Ranges](/cells/cpp/insert-ranges-to-Excel/)
- [Merge or Unmerge Range of Cells](/cells/cpp/merge-or-unmerge-range-of-cells/)
- [Move Range of Cells in a Worksheet](/cells/cpp/move-range-of-cells-in-a-worksheet/)
- [Create Workbook and Worksheet Scoped Named Ranges](/cells/cpp/create-workbook-and-worksheet-scoped-named-ranges/)
- [Search and Replace Data in a Range](/cells/cpp/search-and-replace-data-in-a-range/)
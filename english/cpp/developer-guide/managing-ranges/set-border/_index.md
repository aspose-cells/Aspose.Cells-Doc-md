---
title: Set Range Border with C++
type: docs
weight: 600
url: /cpp/set-range-border/
description: Learn how to set range borders using Aspose.Cells with C++.
---

## **Possible Usage Scenarios**
When you want to set the border for a Range, you don't need to set each cell individually. You can set the border on the range. Aspose.Cells offers this feature. This article provides a sample code that uses Aspose.Cells to set range border.

## **Set Range border in Excel**
To set the border of a range in Excel, you can follow these steps:
1. Select the range of cells that you want to apply the border to.
2. In the "Home" tab of the ribbon, locate the "Font" group.
3. Within the "Font" group, click on the "Borders" drop-down button.
<br>
<img src="border.png" />
4. Choose the type of border that you want to apply from the options in the drop-down menu. You can choose from preset border styles or customize your own border.
5. Once you have selected the desired border style, the border will be applied to the selected range of cells.

## **Set Range border using Aspose.Cells**
This example shows how to:

1. Create a workbook.
2. Add data to cells in the first worksheet.
3. Create a [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range).
4. Set inner border of Range.
5. Set outer border of Range.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new Workbook object
    Workbook workbook;

    // Obtain the reference of the newly added worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    // Setting the value to the cells
    Cell cell = cells.Get("A1");
    cell.PutValue(u"Fruit");
    cell = cells.Get("B1");
    cell.PutValue(u"Count");
    cell = cells.Get("C1");
    cell.PutValue(u"Price");

    cell = cells.Get("A2");
    cell.PutValue(u"Apple");
    cell = cells.Get("A3");
    cell.PutValue(u"Mango");
    cell = cells.Get("A4");
    cell.PutValue(u"Blackberry");
    cell = cells.Get("A5");
    cell.PutValue(u"Cherry");

    cell = cells.Get("B2");
    cell.PutValue(5);
    cell = cells.Get("B3");
    cell.PutValue(3);
    cell = cells.Get("B4");
    cell.PutValue(6);
    cell = cells.Get("B5");
    cell.PutValue(4);

    cell = cells.Get("C2");
    cell.PutValue(5);
    cell = cells.Get("C3");
    cell.PutValue(20);
    cell = cells.Get("C4");
    cell.PutValue(30);
    cell = cells.Get("C5");
    cell.PutValue(60);

    // Create a range (A1:C5)
    Range range = cells.CreateRange(u"A1", u"C5");

    // Set inner border of range
    CellsColor innerColor = workbook.CreateCellsColor();
    innerColor.SetColor(Color::Red());
    range.SetInsideBorders(BorderType::Vertical, CellBorderType::Thin, innerColor);
    innerColor.SetColor(Color::Green());
    range.SetInsideBorders(BorderType::Horizontal, CellBorderType::Thin, innerColor);

    // Set outer border of range
    CellsColor outerColor = workbook.CreateCellsColor();
    outerColor.SetColor(Color::Blue());
    range.SetOutlineBorders(CellBorderType::Thin, outerColor);

    // Save the Workbook
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
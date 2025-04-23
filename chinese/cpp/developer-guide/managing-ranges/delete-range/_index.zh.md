---
title: 用C++删除Excel中的范围
linktitle: 删除范围
type: docs
weight: 105
url: /zh/cpp/delete-ranges-from-excel/
description: 学习如何使用Aspose.Cells与C++删除Excel中的范围。
---

## **介绍**

在 Excel 中，您可以选择一个范围，然后删除它并向左或向上移动其他数据。

**![移动选项](delete-range.png)**

## **使用Aspose.Cells删除范围**

Aspose.Cells提供[Cells.DeleteRange](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterange/)方法删除范围。

## **删除范围并向左移动单元格**

用Aspose.Cells删除范围并左移单元格如下代码：

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook.
    Workbook workbook;

    // Get all the worksheets in the book.
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the first worksheet in the worksheets collection.
    Worksheet worksheet = worksheets.Get(0);

    // Gets cells.
    Cells cells = worksheet.GetCells();

    // Input some data with some formatting into a few cells in the range.
    cells.Get(u"C2").PutValue(u"C2");
    cells.Get(u"C3").PutValue(u"C3");
    CellArea ca = CellArea::CreateCellArea(u"B2", u"B3");

    // Delete the specified range of cells and shift cells to the left.
    cells.DeleteRange(ca.StartRow, ca.StartColumn, ca.EndRow, ca.EndColumn, ShiftType::Left);

    // Check if the value in B2 is equal to "C2".
    std::cout << (worksheet.GetCells().Get(u"B2").GetStringValue() == u"C2" ? "True" : "False") << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **删除范围并向上移动单元格**

用Aspose.Cells删除范围并上移单元格如下代码：

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook.
    Workbook workbook;

    // Get all the worksheets in the book.
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the first worksheet in the worksheets collection.
    Worksheet worksheet = worksheets.Get(0);

    // Gets cells.
    Cells cells = worksheet.GetCells();

    // Input some data with some formatting into a few cells in the range.
    cells.Get(u"B4").PutValue(u"B4");
    cells.Get(u"B5").PutValue(u"B5");

    // Creates a CellArea for the range B2:B3.
    CellArea ca = CellArea::CreateCellArea(u"B2", u"B3");

    // Deletes the specified range and shifts cells up.
    cells.DeleteRange(ca.StartRow, ca.StartColumn, ca.EndRow, ca.EndColumn, ShiftType::Up);

    // Check the value in cell B2 to verify the operation.
    std::cout << (worksheet.GetCells().Get(u"B2").GetStringValue() == u"B4" ? "Success" : "Failure") << std::endl;

    Aspose::Cells::Cleanup();
}
```

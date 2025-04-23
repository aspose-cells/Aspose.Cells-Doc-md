---
title: C++を使用してExcelから範囲を削除する
linktitle: 範囲の削除
type: docs
weight: 105
url: /ja/cpp/delete-ranges-from-excel/
description: Aspose.CellsをC++で使用してExcelの範囲を削除する方法を学びます。
---

## **紹介**

Excelでは、範囲を選択して削除し、他のデータを左にシフトすることができます。

**![シフトオプション](delete-range.png)**

## **Aspose.Cellsを使用した範囲の削除**

Aspose.Cellsは範囲を削除するための[Cells.DeleteRange](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterange/)メソッドを提供します。

## **範囲の削除と左にセルをシフト**

Aspose.Cellsを使用して、以下のコードのように範囲を削除し、セルを左にシフトします：

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

## **範囲の削除と上にセルをシフト**

Aspose.Cellsを使用して、以下のコードのように範囲を削除し、セルを上にシフトします：

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

---  
title: C++を使ってExcelに範囲を挿入する  
linktitle: 範囲の挿入  
type: docs  
weight: 105  
url: /ja/cpp/insert-ranges-to-excel/  
description: Aspose.Cellsを使ったC++でのExcelファイルへの範囲挿入方法を学びます。  
---  

## **紹介**

Excelでは、範囲を選択し、その後、他のデータを右または下にシフトして範囲を挿入できます。

**! [挿入オプション](InsertRange.png)**

## **Aspose.Cellsを使用した範囲の挿入**

Aspose.Cellsは、[Cells.InsertRange](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrange/)メソッドを提供し、範囲を挿入します。

## **範囲の挿入とセルの右シフト**

以下のコード例では、範囲を挿入し、セルを右にシフトします（Aspose.Cellsを使用）：

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

    // Create a range of cells.
    Range sourceRange = worksheet.GetCells().CreateRange(u"A1", u"A2");

    // Input some data with some formattings into a few cells in the range.
    sourceRange.Get(0, 0).PutValue(u"Test");
    sourceRange.Get(1, 0).PutValue(u"123");

    CellArea ca = CellArea::CreateCellArea(u"A1", u"A2");
    worksheet.GetCells().InsertRange(ca, ShiftType::Right);

    std::cout << (worksheet.GetCells().Get(u"B1").GetStringValue() == u"Test" ? "True" : "False") << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **範囲の挿入とセルの下シフト**

以下のコード例では、範囲を挿入し、セルを下にシフトします（Aspose.Cellsを使用）：

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

    // Create a range of cells.
    Range sourceRange = worksheet.GetCells().CreateRange(u"A1", u"A2");

    // Input some data with some formatting into
    // a few cells in the range.
    sourceRange.Get(0, 0).SetValue(u"Test");
    sourceRange.Get(1, 0).SetValue(u"123");
    CellArea ca = CellArea::CreateCellArea(u"A1", u"A2");
    worksheet.GetCells().InsertRange(ca, ShiftType::Down);

    std::cout << (worksheet.GetCells().Get(u"A3").GetStringValue() == u"Test" ? "True" : "False") << std::endl;

    Aspose::Cells::Cleanup();
}
```


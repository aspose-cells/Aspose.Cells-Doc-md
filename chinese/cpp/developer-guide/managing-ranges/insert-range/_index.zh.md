---  
title: 使用C++将范围插入Excel  
linktitle: 插入范围  
type: docs  
weight: 105  
url: /zh/cpp/insert-ranges-to-excel/  
description: 学习如何使用Aspose.Cells和C++将范围插入Excel文件。  
---  

## **介绍**

在 Excel 中，您可以选择一个范围，然后插入一个范围，并向右或向下移动其他数据。

**![移动选项](InsertRange.png)**

## **使用 Aspose.Cells 插入范围**

Aspose.Cells提供[Cells.InsertRange](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrange/)方法来插入范围。

## **插入范围并向右移动单元格**

使用Aspose.Cells插入范围并向右移动单元格的示例代码：

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

## **插入范围并向下移动单元格**

使用Aspose.Cells插入范围并向下移动单元格的示例代码：

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


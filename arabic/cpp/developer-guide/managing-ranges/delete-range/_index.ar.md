---
title: حذف النطاقات من إكسل باستخدام C++
linktitle: حذف المجموعات
type: docs
weight: 105
url: /ar/cpp/delete-ranges-from-excel/
description: تعلم كيفية حذف النطاقات في إكسل باستخدام Aspose.Cells مع C++.
---

## **مقدمة**

في Excel، يمكنك تحديد مجموعة، ثم حذفها وتحريك البيانات الأخرى يسارًا أو لأعلى.

**![خيارات التحريك](delete-range.png)**

## **حذف النطاقات باستخدام Aspose.Cells**

توفر Aspose.Cells طريقة [Cells.DeleteRange](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterange/) لحذف نطاق.

## **حذف النطاقات وتحريك الخلايا لليسار**

احذف نطاقًا وقم بدفع الخلايا لليسار كما هو موضح في الرموز التالية باستخدام Aspose.Cells:

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

## **حذف النطاقات وتحريك الخلايا لأعلى**

احذف نطاقًا وقم بدفع الخلايا للأعلى كما هو موضح في الرموز التالية باستخدام Aspose.Cells:

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

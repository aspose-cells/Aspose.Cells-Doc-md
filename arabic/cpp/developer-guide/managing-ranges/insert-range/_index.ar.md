---  
title: إدراج النطاقات في Excel باستخدام C++  
linktitle: إدراج المجالات  
type: docs  
weight: 105  
url: /ar/cpp/insert-ranges-to-excel/  
description: تعلم كيفية إدراج النطاقات في ملفات Excel باستخدام Aspose.Cells مع C++.  
---  

## **مقدمة**

في Excel ، يمكنك تحديد مجال ، ثم إدراج مجال ونقل البيانات الأخرى يمينًا أو لأسفل.

**![خيارات النقل](InsertRange.png)**

## **إدراج المجالات باستخدام Aspose.Cells**

توفر Aspose.Cells طريقة [Cells.InsertRange](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrange/) لإضافة نطاق.

## **إدراج مجموعات ونقل الخلايا إلى اليمين**

إدراج نطاق وتحريك الخلايا إلى اليمين كما في الرموز التالية مع Aspose.Cells:

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

## **إدراج مجموعات ونقل الخلايا للأسفل**

إدراج نطاق وتحريك الخلايا إلى الأسفل كما في الرموز التالية مع Aspose.Cells:

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


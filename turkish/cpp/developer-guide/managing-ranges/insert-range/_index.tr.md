---  
title: Excel e Aralıklar Ekleyin C++ ile  
linktitle: Aralıkları Ekle  
type: docs  
weight: 105  
url: /tr/cpp/insert-ranges-to-excel/  
description: Aspose.Cells kullanarak C++ ile Excel dosyalarına aralıklar nasıl eklenir öğrenin.  
---  

## **Giriş**

Excel'de bir aralığı seçebilir, ardından sağa veya aşağıya diğer verileri kaydırarak bir aralık ekleyebilirsiniz.

**![Kaydırma seçenekleri](InsertRange.png)**

## **Aspose.Cells Kullanarak Aralıkları Eklemek**

Aspose.Cells, aralık eklemek için [Cells.InsertRange](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrange/) metodunu sağlar.

## **Aralıkları Ekleyip Hücreleri Sağa Kaydırmak**

Aşağıdaki kodlar ile aspose.cells kullanarak bir aralık ekleyin ve hücreleri sağa kaydırın:

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

## **Aralıkları Ekleyin ve Hücreleri Aşağı Kaydırın**

Aşağıdaki kodlar ile aspose.cells kullanarak bir aralık ekleyin ve hücreleri aşağı kaydırın:

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

{{< app/cells/assistant language="cpp" >}}

---
title: C++ kullanarak Bir Aralıkta Veri Arama ve Değiştirme
linktitle: Excel de Bir Aralıktaki Verileri Arama ve Değiştirme
type: docs
weight: 170
url: /tr/cpp/search-and-replace-data-in-a-range/
description: Bu makale, C++ kodu kullanarak Excel de bir aralıkta veri arama ve değiştirme nasıl yapılır gösterir.
keywords: C++ kullanarak Excel de veri arama ve değiştirme, C++ ile excel de veri arama, C++ kullanarak aralıkta veri arama ve değiştirme, C++ ile aralıkta veri arama, C++ ile aralıkta veri arama, C++ ile arama ve değiştirme, C++ ile excel de veri arama, C++ ile aralıkta veri arama, C++ ile excel de veri arama ve değiştirme, C++ ile aralıkta veri arama ve değiştirme, C++ kullanarak aralıkta veri arama ve değiştirme
---

{{% alert color="primary" %}}

Bazen belirli bir arama yapmak ve belirli hücre değerlerini göz ardı ederek değiştirmek gerekebilir. Aspose.Cells, aramayı belirli bir aralıkla sınırlandırmanıza imkan tanır. Bu makale detayları açıklar.

{{% /alert %}}

Aspose.Cells, veri ararken aralık belirtmek için [**FindOptions::SetRange()**](https://reference.aspose.com/cells/cpp/aspose.cells/findoptions/setrange/) metodunu sağlar. Aşağıdaki kod örneği, bir aralıkta veri arama ve değiştirme işlemini gösterir.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String filePath = srcDir + u"input.xlsx";

    // Create workbook
    Workbook workbook(filePath);

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Specify the range where you want to search
    // Here the range is E9:H15
    CellArea area = CellArea::CreateCellArea(u"E9", u"H15");

    // Specify Find options
    FindOptions opts;
    opts.SetLookInType(LookInType::Values);
    opts.SetLookAtType(LookAtType::EntireContent);
    opts.SetRange(area);

    Cell cell;
    do
    {
        // Search the cell with value search within range
        cell = worksheet.GetCells().Find(u"search", cell, opts);

        // If no such cell found, then break the loop
        if (!cell)
            break;

        // Replace the cell with value replace
        cell.PutValue(u"replace");

    } while (true);

    // Save the workbook
    U16String outputPath = srcDir + u"output.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

---
title: Belirli Stilde Hücreleri Bulmak (C++)
linktitle: Belirli Stile Sahip Hücreleri Bul
type: docs
weight: 190
url: /tr/cpp/find-cells-with-specific-style/
description: Aspose.Cells for C++ API’sini kullanarak belirli bir stil uygulanan hücreleri nasıl bulup arayacağınızı öğrenin.
keywords: Belirli bir stile sahip hücreleri bul, Belirli bir stile sahip hücreleri ara
---

{{% alert color="primary" %}}

Bazı durumlarda, belirli bir stile sahip hücreleri bulmanız gerekebilir. Aspose.Cells, bir stile göre tüm hücreleri bulmak için [**FindOptions.GetStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/findoptions/getstyle/) özelliğini kullanabilir.

{{% /alert %}}

Bu örnek kod, A1 hücresiyle aynı stile sahip tüm hücreleri bulur. Kod çalıştırıldıktan sonra, A1 ile aynı stile sahip tüm hücreler "Bulundu" metnini içerir.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    U16String filePath = srcDir + u"TestBook.xlsx";

    Workbook workbook(filePath);
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Style style = worksheet.GetCells().Get(u"A1").GetStyle();

    FindOptions options;
    options.SetStyle(style);

    Cell nextCell;

    do
    {
        nextCell = worksheet.GetCells().Find(U16String(), nextCell, options);
        if (nextCell.GetRow() == -1)
            break;
        nextCell.PutValue(u"Found");
    } while (true);

    U16String outputPath = outDir + u"output.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
